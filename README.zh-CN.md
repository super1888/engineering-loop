# Engineering Loop

**明确取舍，小步实现，用证据说明完成。**

[English](README.md) · [安装](#安装) · [设计边界](docs/DESIGN.md) · [参与贡献](CONTRIBUTING.md)

面向 Claude Code 和 Codex 的通用工程流程 skill，覆盖需求、编码、评审、测试、发布与运维。由人决定关键取舍，AI 在已授权范围内持续推进，各阶段指导按需读取。

**当前 v0.1 是实验性初版。** 已执行的包装与安装检查不等于证明能减少 bug 或提高开发速度；行为评估方案公开，效果需要实际项目验证。

## 解决什么问题

- 需求含糊时先查事实，按依赖分批提出有代价说明的选择。
- 恢复项目时核对有效需求、代码和环境，不盲信过期交接。
- 简单修改保持轻量；跨模块、数据和权限变化按风险增加验证。
- 评审需求符合性与工程正确性，检查遗漏、越界和测试被削弱。
- 验证完整用户行为，以及相关的失败、重试和恢复路径。
- 经验优先沉淀为回归、自动检查和项目决定，并允许淘汰低收益规则。
- 新项目把业务规则、模块与契约负责人、实际检查对应起来；迁移经验时验证防护在当前项目确实生效。

没有运行时依赖、后台服务、自动执行 hooks、强制多代理或固定技术栈。skill 提供指导，实际权限和工程工具负责约束；它不保证零错误。

## 安装

每个工具、每个作用域选择一种安装方式，避免重复加载。这里的支持范围是本地 Claude Code / Codex；其他产品及客户端需要分别验证。

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
| 明确要求按此流程开发 | 进入所需阶段 |
| 恢复项目但状态不明确 | 先核对现状与交接 |
| 跨模块工作有关键未决项 | 组织澄清与验证 |
| 已确定方案，只要求评审或测试 | 直接进入对应阶段 |
| 解释代码、改文案、明确的局部修改 | 使用原有项目流程，不重启完整访谈 |

默认保留范围明确的自动发现；是否触发受宿主与模型影响，显式调用最便于复现。没有“每个任务必须调用”的全局钩子。需要完全手动触发时，见[兼容说明](docs/COMPATIBILITY.md#explicit-only-use)。

### 新项目如何接入与沉淀

按需读取[项目接入指南](skills/engineering-loop/references/project.md)，复用项目已有载体，确认当前功能的业务样例、模块与数据归属、共享契约负责人及验证命令。先完成一个可验收的功能，再扩展类似实现；多人工作集成后验证相互影响。

问题先进入项目回归或自动检查，技术栈经验进入相应模板或规则，跨项目反复出现的流程问题才进入通用 skill。新项目只选择相关经验并运行防护检查；仅复制文档不能证明问题已被预防。详细示例见[工作流程](examples/workflows.md)。

## 如何控制上下文

入口只负责识别任务、恢复状态和选择当前指南。各阶段细则分别保存，按需读取；同一任务不因每次编辑或工具调用重新路由。必要的持久状态放进项目已有载体，详细日志与历史方案通过索引访问。

分文件不能清除已进入会话的内容，也不保证固定 token 消耗；长任务仍需在适当检查点整理有效状态后交接。

## 如何逐步验证

仓库提供包装检查、离线打包脚本和行为评估场景。行为场景覆盖错误触发、重复提问、旧交接、测试降级、遗漏、权限与恢复等；多数仍待执行。已记录一轮[本地入库对照与文案试跑](evals/results/2026-09-21-local/report.md)，保留产物、独立验收结果及评估工具自身缺陷的修复证据。入库两组均通过，尚未证明 skill 带来质量优势或提速。

```sh
python scripts/check.py
python -m unittest discover -s tests -v
python scripts/package.py --output dist/engineering-loop.zip
```

Python 3.10+ 仅用于仓库检查、打包和本地评估工具，使用 skill 本身不需要 Python。CI 执行分发检查和工具单元测试，不运行模型。具体已测范围见[兼容与验证状态](docs/COMPATIBILITY.md)；实际问题的本地沉淀见[项目经验](docs/LESSONS.md)。

当前未发布修订明确了受影响返回路径的可见结果、视觉缺陷的实际渲染证据和已知修复回放的结论边界（[三个场景](evals/README.md#unreleased-flow-visual-and-learning-revision)），并补充参考项目继承、有效约定维护、门禁证据、实际使用效果及纠正的跨会话保留（[七个场景](evals/README.md#unreleased-reference-inheritance-and-effective-guidance-revision)）。这十个场景均待执行；历史产品检查不能证明新指导有额外收益。保留现有阶段路由，不强制统一项目架构。

可选的[协作指南](skills/engineering-loop/references/collaboration.md)补充职责归属、规格分歧裁决、已接受变更的同步和独立验证，不要求固定 agent 团队。对应[另四个协作场景](evals/README.md#unreleased-collaboration-revision)也尚未试跑；增加 agent 不代表已经提高准确率。

[2026-09-22 前端 A/B 小型试验](evals/results/2026-09-22-local-ui/report.md)比较了当前指导与两条候选指导，覆盖列表状态恢复和纯文案修改。对应任务的产物字节一致，独立浏览器检查均通过；未观察到额外正确性收益。两组均未委派，真实多 agent 协调仍待验证。

欢迎在 [Issues](https://github.com/super1888/engineering-loop/issues) 提供脱敏反例，在 [Discussions](https://github.com/super1888/engineering-loop/discussions) 讨论流程取舍。重点是实际减少重复沟通、遗漏与返工，不以规则条数或文档数量作为成熟度。

如果对你有用，欢迎 Star；可复现的反馈更能帮助项目成长。

[MIT 许可](LICENSE) · [参考与致谢](ACKNOWLEDGMENTS.md) · [后续方向](docs/ROADMAP.md)
