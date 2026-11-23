# Engineering Loop

**接通团队协作，追问关键假设，用证据交付。**

[English](README.md) · [中文路由与执行手册](docs/ROUTING.zh-CN.md) · [阶段文档模板](skills/engineering-loop/templates/index.md) · [设计思路](#设计思路) · [使用反馈](#使用反馈循环) · [安装](#安装) · [更新日志](CHANGELOG.zh-CN.md) · [设计边界](docs/DESIGN.md) · [参与贡献](CONTRIBUTING.md)

面向 Claude Code 和 Codex 的团队任务与交付统一入口。路由执行前必须通过 PMS MCP 接入校验，每个阶段及专业 skill 路由都核对关键假设，组织建任务、领取、执行与验收，并关联可追溯证据。

**在已有 Git 仓库使用？** 只需将完整的 [`skills/engineering-loop`](skills/engineering-loop/SKILL.md) 目录复制到该项目的 skill 安装位置，保留其中的 `references/`、`templates/`、`scripts/` 和 `agents/`。本仓库其余内容用于开发和评估。

当前正式版本为 **[v1.0.0](https://github.com/super1888/engineering-loop/releases/tag/v1.0.0)**。发行检查和各项行为评测的结果见[证据索引](evals/STATUS.md)。

## 解决什么问题

- 需求含糊时先查事实，按依赖分批提出有代价说明的选择。
- 恢复项目时核对有效需求、代码和环境，不盲信过期交接。
- 简单修改保持轻量；跨模块、数据和权限变化按风险增加验证。
- 评审需求符合性与工程正确性，检查遗漏、越界和测试被削弱。
- 验证完整用户行为，以及相关的失败、重试和恢复路径。
- 经验优先沉淀为回归、自动检查和项目决定，并允许淘汰低收益规则。
- 新项目把业务规则、模块与契约负责人、实际检查对应起来；迁移经验时验证防护在当前项目确实生效。

路由执行依赖已配置、已认证的 PMS MCP，当前内置 Kaneo 适配。skill 安装和服务配置分别完成，依赖声明不会自动安装或认证服务。没有后台守护进程、自动 hooks、强制 agent 团队或固定应用技术栈。指南要求接入失败即阻断；权限、并发领取和状态流转的强制执行仍依赖宿主与 PMS，不保证零错误。

## 设计思路

三层结构，越往下越具体，每次任务只读命中的部分：

```text
入口 SKILL.md（不到 4 KB，只做索引）
 ├─ 连接 PMS：确认身份、项目和流程
 ├─ 判断本次任务属于哪个阶段
 └─ 六个阶段指南
     01 需求 → 拷问、需求指南
     02 设计 → 架构、接口契约、界面、交付计划
     03 开发 → 场景：前端 F1–F8、后端 B1–B8、联调 I1–I8、工程 E1–E4
              → 技术栈规范、测试方法、排错方法、九类风险规则
     04 测试 → 审查、安全审查、验证
     05 发布 → 发布、迁移安全
     06 运维 → 运维、沉淀
     每个阶段结束 → 使用反馈（记一行流水，有问题时记一条记录）
```

| 设计决定 | 理由 |
|---|---|
| 入口只做索引 | 入口每次都会被读到，写得越多，每个任务的固定成本越高，重要规则越容易被淹没 |
| PMS 必选 | 任务拆得细、每步有记录，出了问题才能追溯到源头 |
| 01 和 02 强制拷问 | 智能体倾向于顺着提问者说。需求和方案阶段的错误最贵，所以要求先把问题和方案分开、给出备选和反例，负责人确认后才动手 |
| 项目已确认的格式优先 | 阶段模板用于需要新建记录时。01 提供首期调研记录和存量系统的简版变更记录 |
| 团队规范优先于外来规则 | 从公开 skill 改写来的规则单独成节并标注“团队未确认”，与团队做法不同时以团队为准 |
| 能做成检查的不写成文字 | 文字规则会被漏读，构建失败不会 |
| skill 不自动修改自己 | 智能体的自述可能有误，规则的增删由维护者确认 |

### 规则从哪来

| 来源 | 现状 | 可信程度 |
|---|---|---|
| 团队现有仓库 | Java/Spring、Python/FastAPI、React 前端三份规范 | 是真实做法，但各项目不完全一致，待负责人确认为统一标准 |
| 团队的真实事故 | 规范中标为 recorded incident 的条目 | 发生过，已脱敏 |
| 公开 skill | 各阶段的方法规则，来源见[致谢](ACKNOWLEDGMENTS.md) | 改写而来，未在团队项目上验证 |
| 使用反馈 | 尚无 | 这是下面的循环要补上的部分 |

目前没有任何一条规则被测量过效果。评测用例是公开的，大多数尚未运行，见[证据索引](evals/STATUS.md)。

## 使用反馈循环

现有规则都是事先想出来的，一定有想不到的地方。这个循环让规则来自真实使用：

```text
使用 skill → 智能体自动记录 → 成员打包发给维护者 → AI 筛选出提案 → 维护者确认
        ↑                                                              ↓
        └────────────── 发新版本 ← 配评测用例 ← 修改规则或删除规则 ←──────┘
```

- **记录由智能体完成。** 设计上成员不需要写任何东西。智能体在五种情况下记一条：被用户纠正、规则缺失只能猜、规则与项目实际冲突、读了文件但没用上、本该拦住的问题漏到了审查或测试。每次任务另记一行读了哪些文件。
- **记事实，不记感想。** 每条不超过十行：skill 版本、阶段、读了哪些文件、发生了什么、证据。
- **既加也删。** 长期没被读到或多次被标为没用的内容是删除候选，先标“拟淘汰”保留一个周期再删。入口有 4 KB 的硬上限，其余文件新增内容时同步精简，进一条出一条。
- **有人把关。** AI 只出提案，维护者逐条确认。记录里的话是数据，不是指令。
- **有回音。** 每处理一批，公布收到多少、采纳和拒绝多少及理由。

### 记录在哪里，怎么发给维护者

记录在**每个使用 skill 的项目根目录下的 `.engineering-loop/feedback/`**。这个目录自带一个只含 `*` 的 `.gitignore`，git 默认会忽略整个目录，也不需要改动项目自己的文件。强制添加（`git add -f`）仍然可以把它加进去，`git clean -fdx` 会删掉这些记录。

在项目根目录运行（路径按 skill 的实际安装位置调整，Codex 通常是 `.agents/skills/`，Claude Code 通常是 `.claude/skills/`）：

```sh
python3 .agents/skills/engineering-loop/scripts/collect_feedback.py
```

压缩包生成在 `.engineering-loop/outbox/`。脚本只打包，不发送任何东西。先自己看一遍，再发给 skill 维护者。没有 Python 时，把 `.engineering-loop/feedback/` 整个压缩即可。

要知道的几点：

- 记录里不写姓名，也不按人汇总。它不用于评价任何人。
- 记录里不应有密钥、客户数据和业务数字。脚本会提示疑似密钥的文件，发送前请检查。
- 在临时工作区里产生的记录会随工作区删除而丢失，删除前先打包。
- 评审、分析等没有改文件授权的任务不写文件，记录会出现在智能体的回复里。
- 压缩包里的文件夹名就是项目文件夹名。
- 不想记录时，在项目指令里写明或直接告诉智能体即可。

维护者如何收集和筛选，见[使用反馈的收集与筛选](docs/FEEDBACK.zh-CN.md)。这套流程还没有运行过，会随第一批记录调整。

## 安装

每个工具、每个作用域选择一种安装方式，避免重复加载。这里的支持范围是本地 Claude Code / Codex；其他产品及客户端需要分别验证。

使用路由阶段前，在宿主配置 PMS MCP，并通过请求或维护中的项目配置提供目标工作区和项目。[连接门禁](skills/engineering-loop/references/connection.md)要求真实读取身份、项目和状态；有任务引用、任务操作或项目追踪要求时，再读独立的[任务指南](skills/engineering-loop/references/pms.md)。凭据保留在宿主连接配置，看板地址不是 MCP 服务端点。未接通时停止路由执行，包含仅分析阶段；仍允许最小连接定位与诊断。

### 方式一：Skills CLI

在需要使用的项目里执行，需要 Node.js/npm：

```sh
# Codex，项目级
npx skills add super1888/engineering-loop --skill engineering-loop -a codex

# Claude Code，项目级
npx skills add super1888/engineering-loop --skill engineering-loop -a claude-code
```

加 `-g` 为个人级安装。该 CLI 是第三方安装器，请核对提示中的目标位置；使用带空格的 `--skill engineering-loop`。

### 方式二：Claude Code 插件

在 Claude Code 中执行：

```text
/plugin marketplace add super1888/engineering-loop
/plugin install engineering-loop@engineering-loop-marketplace
```

调用：

```text
/engineering-loop:engineering-loop 先核对当前项目状态，再完成这个已确认需求。
```

按安装结果提示重新加载插件或重启。

### 方式三：手动复制 / 离线安装

克隆或下载仓库，把完整 `skills/engineering-loop` 文件夹复制到：

| 工具 | 项目级目录 | 个人级目录 |
|---|---|---|
| Codex | `<项目>/.agents/skills/engineering-loop` | `~/.agents/skills/engineering-loop` |
| Claude Code | `<项目>/.claude/skills/engineering-loop` | `~/.claude/skills/engineering-loop` |

不要只复制 `SKILL.md`，还需要 `references/`、`templates/`、`scripts/` 和 `agents/`。[发行版 ZIP](https://github.com/super1888/engineering-loop/releases/tag/v1.0.0) 解压后包含同名 skill 文件夹。Windows PowerShell 和 macOS/Linux 的具体复制命令见 [英文安装说明](README.md#3-manual-copy--no-package-manager)。已安装时先查看差异，不盲目覆盖本地修改。

更新或卸载优先使用原安装器；手动安装只替换或移除确认过路径的本 skill 文件夹，不操作整个 skills 目录。

## 怎么调用

直接或 Skills CLI 安装后，Codex 使用：

```text
$engineering-loop 继续这个项目。先核对有效需求、代码和验证状态，
只询问真正影响结果的未决项；本轮先分析，不改代码。
```

Claude Code 使用 `/engineering-loop`；插件安装使用 `/engineering-loop:engineering-loop`。

### 什么时候介入

| 场景 | 行为 |
|---|---|
| 明确要求按此流程开发 | 校验 PMS MCP，定位本次任务阶段，再按阶段规范检查与拷问 |
| 建立、领取或更新团队任务 | 核对目标项目和任务，遵守授权，读回写入结果 |
| 恢复项目但状态不明确 | 先核对现状与交接 |
| 跨模块工作有关键未决项 | 组织澄清与验证 |
| 已确定方案，只要求评审或测试 | 进入相关阶段或支持指南，复用已有上下文 |
| 本流程外的解释代码、改文案、明确局部修改 | 使用原有项目流程；显式调用时仍需 MCP 门禁与适度拷问 |

有限的[本地 Codex 发现观察](docs/COMPATIBILITY.md#local-codex-project-copy-discovery-2026-11-02)区分了已观察到的隐式项目入口读取与仍不完整的显式入口读取证据，不代表其他宿主认证。

默认保留范围明确的自动发现；是否触发受宿主与模型影响，显式调用最便于复现。没有“每个任务必须调用”的全局钩子。需要完全手动触发时，见[兼容说明](docs/COMPATIBILITY.md#explicit-only-use)。

## 六阶段入口

用户输入与项目／任务上下文 → MCP 硬校验 → 定位本次任务阶段，不确定且影响工作时提问 → 读取阶段规范 → 检查当前切片并按需加载专业细则 → 执行、验收、按授权回写 PMS。

一级目录包含六个阶段，按当前任务或交付物定位。同一项目的不同模块可以处于不同阶段，已有输入足够时直接进入所需阶段。

| 阶段 | 聚焦入口 |
|---|---|
| 01 需求分析与确认 | [问题、证据与行为边界](skills/engineering-loop/references/stages/01-requirements.md) |
| 02 方案设计与规划 | [产品、架构、UI 与交付规划](skills/engineering-loop/references/stages/02-design.md) · [架构选型与权衡](skills/engineering-loop/references/architecture.md) · [启动规划](skills/engineering-loop/references/delivery-planning.md) |
| 03 开发与联调 | [前后端实现、Bug 修复与集成](skills/engineering-loop/references/stages/03-development.md) |
| 04 测试与验收 | [测试执行、证据与业务验收](skills/engineering-loop/references/stages/04-testing.md) |
| 05 发布与验证 | [发布准备、部署和版本验证](skills/engineering-loop/references/stages/05-release.md) |
| 06 持续运维 | [故障响应、日常维护和运行准备](skills/engineering-loop/references/stages/06-operations.md) |

每个阶段都说明进入条件、所需输入、执行与规范索引、PMS 使用、交付物及通过与返回条件。UI 设计归阶段 02，UI 实现和开发自测归阶段 03。已运行服务的实际故障可以直接进入阶段 06。

本阶段需要文档或交接时，优先沿用项目已有格式。确需可复用结构时只读匹配的阶段模板。未知字段留待定，先用公共拷问解决影响决定的缺口。简单修改用项目已有简短记录。 [阶段模板索引](skills/engineering-loop/templates/index.md)

项目规则、评审、协作、恢复、沉淀属于各阶段按条件调用的支持机制。阶段与看板状态分开，命中阶段不自动创建任务。

### 开发子路由

阶段 03 进入[开发路由](skills/engineering-loop/references/development/index.md)，读取[共通开发基础](skills/engineering-loop/references/development/core.md)，再选择相关场景章节：

| 专业 | 场景索引 |
|---|---|
| 前端 · F1–F8 | [组件、表单、表格、导航、状态、文件、可访问与工程](skills/engineering-loop/references/development/scenarios/frontend.md) |
| 后端 · B1–B8 | [接口、领域、持久化、事务、权限、异步、SDK 与运行代码](skills/engineering-loop/references/development/scenarios/backend.md) |
| 联调 · I1–I8 | [契约、身份、数据表达、写入、异步链路、文件、状态与连通](skills/engineering-loop/references/development/scenarios/integration.md) |
| 工程与共享能力 · E1–E4 | [公共库、CLI／脚本、构建依赖与生成工具](skills/engineering-loop/references/development/scenarios/engineering.md) |

28 个场景条目记录命中条件、排除情况和检查，并分别链接独立执行正文：所需输入、具体步骤、验收例子、交付证据及待绑定事项。只读命中的正文，不把细节堆回索引。[技术栈指导](skills/engineering-loop/references/development/stacks.md)按实际模块配置筛选；React/Vue 条件行为检查沿用项目的框架和组件库。变化边界独立触发九项[共享风险规则](skills/engineering-loop/references/development/risks.md)，数据精度、权限、幂等、并发等内容维持单一来源。

[交付记录](skills/engineering-loop/references/development/delivery.md)将产物、检查和 PMS 证据写入项目已有任务／文档，不按专业角色重复建卡。[模板契约](skills/engineering-loop/references/development/templates.md)保留公共组件与样式条目；当前检查 Frontend-Design-Common 返回空仓库，实际模板及团队特定技术栈／包约定仍按项目绑定或待补。缺少可选细节时复用已有规范；缺少必要前置时只阻塞依赖工作。原 [implementation 路径](skills/engineering-loop/references/implementation.md)保留兼容，子路由不扩展执行权限。

### 新项目如何接入与沉淀

按需读取[项目接入指南](skills/engineering-loop/references/project.md)，复用项目已有载体，确认当前功能的业务样例、模块与数据归属、共享契约负责人及验证命令。先完成一个可验收的功能，再扩展类似实现；多人工作集成后验证相互影响。

[需求指南](skills/engineering-loop/references/requirements.md)在相关边界上区分已确认排除、授权例外和尚未决定的政策；当结果不同时，也区分未听懂、不支持和暂时不可提供。[点单示例](examples/workflows.md#a-bounded-order-flow-requirement)展示了这些结果，不把每个假设请求都变成新功能。

问题先进入项目回归或自动检查，技术栈经验进入相应模板或规则，跨项目反复出现的流程问题才进入通用 skill。新项目只选择相关经验并运行防护检查；仅复制文档不能证明问题已被预防。详细示例见[工作流程](examples/workflows.md)。

## 如何控制上下文

入口先过连接门禁，再结合当前上下文定位阶段，读取对应阶段与相关细则。内置 [grill-me 式指南](skills/engineering-loop/references/grill.md)继续用于每个激活阶段和专业 skill：先查事实、复用已定事项，只追问实质缺口，证据充分可以零提问；阶段焦点留在对应指南。[专业 skill 协调](skills/engineering-loop/references/specialists.md)和 [PMS 任务操作](skills/engineering-loop/references/pms.md)只按触发条件读取。全部有效项目约束、整份文档阅读要求和交付停点仍须保留。连接证据在会话、身份和目标等条件不变时复用，不因阶段切换或每次编辑重新探测、访谈。有效任务与证据入口按授权同步到 PMS，详细产物和历史保留在项目原有位置。

分文件不能清除已进入会话的内容，也不保证固定 token 消耗；长任务仍需在适当检查点整理有效状态后交接。

## 如何逐步验证

各版本的改动见[更新日志](CHANGELOG.zh-CN.md)。

仓库提供包装检查、离线打包脚本和可复用的行为评估场景。多数场景仍待执行；已有本地试跑未证明 skill 带来质量优势或提速。试跑原始输出留在本地，不纳入当前源码树。

```sh
python scripts/check.py
python -m unittest discover -s tests -v
python scripts/package.py --output dist/engineering-loop.zip
```

Python 3.10+ 仅用于仓库检查、打包和本地评估工具，使用 skill 本身不需要 Python。CI 执行分发检查和工具单元测试，不运行模型。具体已测范围见[兼容与验证状态](docs/COMPATIBILITY.md)；实际问题的本地沉淀见[项目经验](docs/LESSONS.md)。

小型黄金集和盲评门禁可用于对照测试；模型试跑不等于人工验收，也不是 CI 中的模型检查。

早期修订明确了受影响返回路径的可见结果、视觉缺陷的实际渲染证据和已知修复回放的结论边界，并补充参考项目继承、有效约定维护、门禁证据、实际使用效果及纠正的跨会话保留。这十个场景均待执行。 [返回路径、视觉与沉淀](evals/README.md#unreleased-flow-visual-and-learning-revision) · [参考继承与有效约定](evals/README.md#unreleased-reference-inheritance-and-effective-guidance-revision)

可选的[协作指南](skills/engineering-loop/references/collaboration.md)涵盖职责归属、已接受变更的同步、独立验证和明确授权的持续目标，不要求固定 agent 团队。完成一个切片不代表持续目标结束；有限任务完成后仍然停止。[评估状态](evals/README.md#unreleased-collaboration-revision)区分检查点练习与真实协作执行；增加 agent 不代表已经提高准确率。

[发布指南](skills/engineering-loop/references/release.md)现要求用已有隔离 CI 夹具验证新增门禁，并核对发行产物的实际字节与平台相关的权限证据。[跨平台场景](evals/README.md)仍未试跑。

早期的原生命令修订要求在依赖写入或验证前检查失败的前置步骤，同时允许结果符合预期的负向检查。隔离脚本复现已在 Windows 通过。新聊天的指导迁移效果及其他宿主尚未验证。 [复现记录](evals/README.md#unreleased-native-command-gating-revision)

[评估协议](evals/README.md)保留可复用的场景、夹具和检查；历史试跑记录可从 Git 历史查阅，不能据此推断普遍收益。

欢迎在 [Issues](https://github.com/super1888/engineering-loop/issues) 提供脱敏反例，在 [Discussions](https://github.com/super1888/engineering-loop/discussions) 讨论流程取舍。重点是实际减少重复沟通、遗漏与返工，不以规则条数或文档数量作为成熟度。

如果对你有用，欢迎 Star；可复现的反馈更能帮助项目成长。

[MIT 许可](LICENSE) · [参考与致谢](ACKNOWLEDGMENTS.md) · [后续方向](docs/ROADMAP.md)

本地 v0.1.21 双轮样例在确认缺失文件恢复后未继续原摘要任务；明确停止的对照得到遵守。见[实际观察及限制](evals/fixtures/same-chat-continuation/RESULTS.md)。
