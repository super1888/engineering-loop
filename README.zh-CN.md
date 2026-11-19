# Engineering Loop

**接通团队协作，追问关键假设，用证据交付。**

[English](README.md) · [安装](#安装) · [设计边界](docs/DESIGN.md) · [参与贡献](CONTRIBUTING.md)

面向 Claude Code 和 Codex 的团队任务与交付统一入口。路由执行前必须通过 PMS MCP 接入校验，每个阶段及专业 skill 路由都核对关键假设，组织建任务、领取、执行与验收，并关联可追溯证据。

**在已有 Git 仓库使用？** 只需将完整的 [`skills/engineering-loop`](skills/engineering-loop/SKILL.md) 目录复制到该项目的 skill 安装位置。保留目录内的 `references/` 和 `agents/`；本仓库其余内容用于开发和评估。

**当前 v0.1 是实验性初版。** 已执行的包装与安装检查不等于证明能减少 bug 或提高开发速度；行为评估方案公开，效果需要实际项目验证。

## 解决什么问题

- 需求含糊时先查事实，按依赖分批提出有代价说明的选择。
- 恢复项目时核对有效需求、代码和环境，不盲信过期交接。
- 简单修改保持轻量；跨模块、数据和权限变化按风险增加验证。
- 评审需求符合性与工程正确性，检查遗漏、越界和测试被削弱。
- 验证完整用户行为，以及相关的失败、重试和恢复路径。
- 经验优先沉淀为回归、自动检查和项目决定，并允许淘汰低收益规则。
- 新项目把业务规则、模块与契约负责人、实际检查对应起来；迁移经验时验证防护在当前项目确实生效。

路由执行依赖已配置、已认证的 PMS MCP，当前内置 Kaneo 适配。skill 安装和服务配置分别完成，依赖声明不会自动安装或认证服务。没有后台守护进程、自动 hooks、强制 agent 团队或固定应用技术栈。指南要求接入失败即阻断；权限、并发领取和状态流转的强制执行仍依赖宿主与 PMS，不保证零错误。

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

不要只复制 `SKILL.md`，还需要 `references/` 和 `agents/`。[发行版 ZIP](https://github.com/super1888/engineering-loop/releases/tag/v0.1.0) 解压后包含同名 skill 文件夹。Windows PowerShell 和 macOS/Linux 的具体复制命令见 [英文安装说明](README.md#3-manual-copy--no-package-manager)。已安装时先查看差异，不盲目覆盖本地修改。

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

## 五阶段入口

用户输入与项目／任务上下文 → MCP 硬校验 → 定位本次任务阶段，不确定且影响工作时提问 → 读取阶段规范 → 检查当前切片并按需加载专业细则 → 执行、验收、按授权回写 PMS。

一级目录采用五阶段，定位对象是当前任务或交付物。同一项目的不同模块可以处于不同阶段；已有输入足够时直接进入所需阶段，不重走之前的工作。

| 阶段 | 聚焦入口 |
|---|---|
| 01 需求分析与确认 | [问题、证据与行为边界](skills/engineering-loop/references/stages/01-requirements.md) |
| 02 方案设计与规划 | [产品、架构、UI 与交付规划](skills/engineering-loop/references/stages/02-design.md) |
| 03 开发与联调 | [前后端实现、Bug 修复与集成](skills/engineering-loop/references/stages/03-development.md) |
| 04 测试与验收 | [测试执行、证据与业务验收](skills/engineering-loop/references/stages/04-testing.md) |
| 05 发布与验证 | [部署、上线验证与相关运维](skills/engineering-loop/references/stages/05-release.md) |

每个阶段统一包含六项：进入条件、所需输入、执行与规范索引、PMS 使用、交付物、通过与返回条件。五阶段目录定义这些契约；开发分支进一步索引已有规则，具体团队标准保留后续补充位置。UI 设计归阶段 02，实现归阶段 03；开发自测仍属于开发工作。实际运维事件可直接进入阶段 05 的相关分支，不强制变成发布任务或重走前面阶段。

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

未发布的 v0.1.26 补齐全部 28 个场景的执行基线，保留短索引与项目既有选择。React/Vue 条件行为检查引用官方文档；未提供的团队包／样式标准与实际组件模板继续待补。[细则场景](evals/fixtures/development-details/TASK.md)和[验证记录](evals/fixtures/development-details/RESULTS.md)区分源码／格式检查与真实任务／运行行为，旧版本结果单独保留。

未发布的 v0.1.25 增加开发场景子路由，并归位已有共通与风险规则，保留原约束。待补技术栈／模板内容与可用指导分开标明。[开发路由场景](evals/fixtures/development-routing/TASK.md)及[验证记录](evals/fixtures/development-routing/RESULTS.md)区分源码／分发检查与实际任务执行；目录更细本身不证明命中率提高、少读内容或模型质量收益。

未发布的 v0.1.24 将一级导航收敛为五阶段入口，并统一六项阶段规范。现有专业与支持指南保留，MCP 门禁、授权和验收边界继续生效。目录是指导索引，并非自动选择器；v0.1.23 的历史试验不能为新路由背书。本轮执行状态见[证据索引](evals/STATUS.md)。

未发布的 v0.1.23 将强制连接／共同拷问核心与任务操作、专业 skill 协调分开，阶段焦点迁回各自指南。首个切片将共同入口与参考文本从 21,772 减到 12,007 字节；字节不等于实测 token 或质量、成本收益。全部门禁与有效项目约束继续生效。[受控局部文案试验](evals/fixtures/core-route/TASK.md)区分实际模型／工具观察与适配器检查；它不代表旧矩阵全面通过，也未实现通用规则引擎或项目 profile 注册表。

未发布的 v0.1.22 将入口调整为团队任务与交付协调，加入强制 [PMS MCP 接入门禁](skills/engineering-loop/references/connection.md)、Kaneo 依赖声明及每个路由的原创 [grill-me 式拷问](skills/engineering-loop/references/grill.md)。任务写入仍遵守已有授权，仅分析不自动建卡。其[行为矩阵](evals/fixtures/pms-grill-routing/TASK.md)仍未执行；这不是服务端强制门禁或原子领取实现，历史结果不能为新门禁背书，也不证明减少缺陷。

仓库提供包装检查、离线打包脚本和可复用的行为评估场景。多数场景仍待执行；已有本地试跑未证明 skill 带来质量优势或提速。试跑原始输出留在本地，不纳入当前源码树。

```sh
python scripts/check.py
python -m unittest discover -s tests -v
python scripts/package.py --output dist/engineering-loop.zip
```

Python 3.10+ 仅用于仓库检查、打包和本地评估工具，使用 skill 本身不需要 Python。CI 执行分发检查和工具单元测试，不运行模型。具体已测范围见[兼容与验证状态](docs/COMPATIBILITY.md)；实际问题的本地沉淀见[项目经验](docs/LESSONS.md)。

小型黄金集和盲评门禁可用于对照测试；模型试跑不等于人工验收，也不是 CI 中的模型检查。

当前未发布修订明确了受影响返回路径的可见结果、视觉缺陷的实际渲染证据和已知修复回放的结论边界（[三个场景](evals/README.md#unreleased-flow-visual-and-learning-revision)），并补充参考项目继承、有效约定维护、门禁证据、实际使用效果及纠正的跨会话保留（[七个场景](evals/README.md#unreleased-reference-inheritance-and-effective-guidance-revision)）。这十个场景均待执行；历史产品检查不能证明新指导有额外收益。保留现有阶段路由，不强制统一项目架构。

可选的[协作指南](skills/engineering-loop/references/collaboration.md)涵盖职责归属、已接受变更的同步、独立验证和明确授权的持续目标，不要求固定 agent 团队。完成一个切片不代表持续目标结束；有限任务完成后仍然停止。[评估状态](evals/README.md#unreleased-collaboration-revision)区分检查点练习与真实协作执行；增加 agent 不代表已经提高准确率。

未发布的 v0.1.11 修订补充已授权的对话轮换：用终态产物核对过期归属、移交活跃句柄，并精简贡献者摘要读取。新增 D/E [检查点对照](evals/fixtures/delegated-continuation/TASK.md)尚未执行；本次恢复不能证明 skill 的实测收益。

未发布的 v0.1.12 修订要求在依赖回执移交归属或继续任务前，核对保存内容中的身份和状态。[回执检查点对照](evals/fixtures/handoff-receipt/TASK.md)涵盖 null、过期内容、修复回执及普通文字交接；尚未执行，不宣称模型行为收益。

[发布指南](skills/engineering-loop/references/release.md)现要求用已有隔离 CI 夹具验证新增门禁，并核对发行产物的实际字节与平台相关的权限证据。[跨平台场景](evals/README.md)仍未试跑。

未发布的原生命令修订要求在依赖写入或验证前检查失败的前置步骤，同时允许结果符合预期的负向检查。[隔离脚本复现](evals/README.md#unreleased-native-command-gating-revision)已在 Windows 通过；新聊天的指导迁移效果及其他宿主尚未验证。

[评估协议](evals/README.md)保留可复用的场景、夹具和检查；历史试跑记录可从 Git 历史查阅，不能据此推断普遍收益。

欢迎在 [Issues](https://github.com/super1888/engineering-loop/issues) 提供脱敏反例，在 [Discussions](https://github.com/super1888/engineering-loop/discussions) 讨论流程取舍。重点是实际减少重复沟通、遗漏与返工，不以规则条数或文档数量作为成熟度。

如果对你有用，欢迎 Star；可复现的反馈更能帮助项目成长。

[MIT 许可](LICENSE) · [参考与致谢](ACKNOWLEDGMENTS.md) · [后续方向](docs/ROADMAP.md)

未发布的 v0.1.13 修订补充按需触发的产品假设挑战与聚焦的 [UI 工作指南](skills/engineering-loop/references/ui.md)，明确局部修改保持轻量。第一轮对照的条件与实际结果记录在[评估说明](evals/README.md)；包装检查本身不证明行为收益。

未发布的 v0.1.14 增加前端范围门禁：默认仅桌面端，用户明确要求时才加入对应移动端设计与验收。保留已有移动行为，约定冲突须在依赖变更前明确。

未发布的 v0.1.15 补充按风险触发的运维准备：业务进度信号、响应归属、有限恢复演练与数据可恢复性证据。本地任务与有意使用的手动 worker 保持轻量，实际演练结果和边界记录在[评估说明](evals/README.md)。

未发布的 v0.1.16 明确委派执行环境：按子任务实际工作目录、环境和权限核对相关能力，不能由主进程的主机能力推断。复用有效证据、简单只读任务保持轻量；通过正确调用修复环境差异，不默认放宽保护或新增工具链。

未发布的 v0.1.17 将通用验证判断与条件化边界场景分开：核心指南按相关风险路由到聚焦参考，保留既有验收约束与轻量反例。结构保留检查和新上下文路由观察记录在[评估入口](evals/README.md)；首次文本变小不等于证明 token 节省或结果提升。

未发布的 v0.1.19 明确同一对话中的插入提问应保留未完成任务，并尊重明确停止、替换目标和仅起草不发送的限制。新增行为用例及反例；尚未进行模型行为评估。

未发布的 v0.1.18 修正评估与分发维护缺陷：门禁执行前准备回执输出、刷新失败检查完整库存保留、根目录本地虚拟环境不参与项目文件验证、路径摘要保留无关前缀。这些是工具修复，不是新的模型质量收益证据。

未发布的 v0.1.20 检查全部打包 skill 文档和 JSON，同名本地产物目录也不能绕过；仓库本地产物仍保持排除。这是分发检查修正。

未发布的 v0.1.21 修复带空格尖括号目标和可选标题的行内链接检查；不宣称完整解析 Markdown。

本地 v0.1.21 双轮样例在确认缺失文件恢复后未继续原摘要任务；明确停止的对照得到遵守。见[实际观察及限制](evals/fixtures/same-chat-continuation/RESULTS.md)。
