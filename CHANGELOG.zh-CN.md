# 更新日志

按版本倒序。后续方向见[路线图](docs/ROADMAP.md)，已执行的评测见[证据索引](evals/STATUS.md)。[English](CHANGELOG.md)

## v1.0.0 · 2026-11-23

01 阶段提供[首期需求分析与确认](skills/engineering-loop/templates/requirements.md)和[存量需求与修改情况说明](skills/engineering-loop/templates/requirements-change.md)。存量简版记录有效基线、本次变化、需保留的行为、验收与回归预期，以及确认或待定事项。可沿用项目现有记录及标识。新增和修订的[模板选择用例](evals/fixtures/stage-templates/TASK.md)尚未运行。

## 早期开发版本

未发布的 v0.1.36 加入使用反馈循环。智能体在五种可观察事件下把 skill 自身的问题记到项目根目录的 `.engineering-loop/feedback/`，该目录自我忽略、不进 git；每次任务另记一行读取了哪些文件。新增打包脚本，只打包不发送。维护者的收集、筛选、晋级、淘汰和回音流程单独成文，skill 不自动修改自己。README 增加设计思路、规则来源和反馈循环三节，各版本说明移到本文件。入口仍在 4 KB 以内。这套流程尚未运行，新增用例尚未运行。 [使用反馈规则](skills/engineering-loop/references/feedback.md) · [收集与筛选](docs/FEEDBACK.zh-CN.md) · [用例](evals/fixtures/skill-feedback/TASK.md)

未发布的 v0.1.35 用改写自公开 skill 的具体方法规则填充六个阶段：需求扫描与确认、架构取舍、接口契约与幂等设计、界面定形与样稿、任务切片、测试与排错方法、React、Spring Boot 4、FastAPI 和 SQL 的技术栈规则、带安全审查的审查流程、声明与证据对照、发布撤销路径、迁移安全、有边界的生产操作，以及教训形式的判定。新增六份专题文件。不捆绑第三方原文，团队规范优先于改写规则，阶段模板未改动，入口没有变大。新增用例尚未运行，效果未测量。 [审查](skills/engineering-loop/references/review.md) · [测试方法](skills/engineering-loop/references/development/testing.md) · [接口设计](skills/engineering-loop/references/api-design.md) · [来源](ACKNOWLEDGMENTS.md) · [用例](evals/fixtures/absorbed-methods/TASK.md)

未发布的 v0.1.34 澄清 Spring 事务代理的实际行为，保留团队仅在 `public` 方法使用 `@Transactional` 的约定。同时修正了 GitHub Ubuntu 作业中因 `/tmp` 路径触发失败的评测记录断言。 [Java / Spring 规范](skills/engineering-loop/references/development/stacks/java-spring.md) · [复现记录](evals/TOOLING.md#preserve-unrelated-path-prefixes)

未发布的 v0.1.33 将入口收敛为路由：连接门禁、六阶段表、支持文件表和五条始终生效的规则，维护上限由 7 KB 降到 4 KB。阶段和支持指南里已有的通用守则从入口删除，只在入口出现过的几句移入开发共通基础、验证和恢复指南。规则本身不打算改变；移出入口的规则只在对应指南被读取时生效，这一影响尚未测量。新增用例尚未运行。 [入口](skills/engineering-loop/SKILL.md) · [用例](evals/fixtures/slim-entry/TASK.md)

未发布的 v0.1.32 将公共拷问分为两档。01 和 02 的交付物使用完整档，要求五项书面产出、可用时的全新上下文复核，以及负责人确认后才开展依赖工作；已确定的局部修改保持轻量档。同时加入从团队现有服务和产品中提取的 Java/Spring、Python/FastAPI 和 React 前端规范，状态为部分可用，团队尚未统一的选择保持待定，阶段模板未改动。新增用例尚未运行。 [公共拷问](skills/engineering-loop/references/grill.md) · [技术栈绑定](skills/engineering-loop/references/development/stacks.md) · [用例](evals/fixtures/challenge-depth-and-stack-rules/TASK.md)

未发布的 v0.1.31 将发布前的《缺陷跟踪与测试验收记录》归入 04。06 跟踪线上缺陷时引用同一份原记录及受影响版本，沿用项目已有格式与存放位置。调整后的交接用例尚未运行。 [测试验收模板](skills/engineering-loop/templates/acceptance-record.md) · [持续运维模板](skills/engineering-loop/templates/operations-record.md) · [模板路由用例](evals/fixtures/stage-templates/TASK.md)

未发布的 v0.1.30 为六阶段提供按需使用的文档及交接模板。新增用例覆盖两类需求、直接进入运维及沿用已有简短记录，目前均未运行。 [阶段模板索引](skills/engineering-loop/templates/index.md) · [模板路由用例](evals/fixtures/stage-templates/TASK.md) · [证据索引](evals/STATUS.md)

未发布的 v0.1.29 为阶段 02 增加可复用的启动计划。沿用项目格式，用同一份计划承接草稿、开工决定及获准的 PMS 任务同步。 [启动计划模板](skills/engineering-loop/templates/kickoff-plan.md) · [启动规划用例](evals/fixtures/kickoff-planning/TASK.md) · [证据索引](evals/STATUS.md)

未发布的 v0.1.28 为阶段 02 增加实质架构决定的指导。架构选型结合公共拷问，按可测负载、总成本和验证证据比较可行方案。 [架构选型用例](evals/fixtures/architecture-tradeoffs/TASK.md) · [证据索引](evals/STATUS.md)

未发布的 v0.1.27 增加独立的持续运维阶段。阶段 05 处理与具体版本发布相关的工作，阶段 06 处理故障和服务的持续运行。路由用例规定两个阶段的边界，证据索引记录执行过的检查及其验证范围。 [六阶段用例](evals/fixtures/six-stage-routing/TASK.md) · [证据索引](evals/STATUS.md)

未发布的 v0.1.26 补齐全部 28 个场景的执行基线，保留短索引与项目既有选择。React/Vue 条件行为检查引用官方文档；未提供的团队包／样式标准与实际组件模板继续待补。[细则场景](evals/fixtures/development-details/TASK.md)和[验证记录](evals/fixtures/development-details/RESULTS.md)区分源码／格式检查与真实任务／运行行为，旧版本结果单独保留。

未发布的 v0.1.25 增加开发场景子路由，并归位已有共通与风险规则，保留原约束。待补技术栈／模板内容与可用指导分开标明。[开发路由场景](evals/fixtures/development-routing/TASK.md)及[验证记录](evals/fixtures/development-routing/RESULTS.md)区分源码／分发检查与实际任务执行；目录更细本身不证明命中率提高、少读内容或模型质量收益。

未发布的 v0.1.24 将一级导航收敛为五阶段入口，并统一六项阶段规范。现有专业与支持指南保留，MCP 门禁、授权和验收边界继续生效。目录是指导索引，并非自动选择器；v0.1.23 的历史试验不能为新路由背书。本轮执行状态见[证据索引](evals/STATUS.md)。

未发布的 v0.1.23 将强制连接／共同拷问核心与任务操作、专业 skill 协调分开，阶段焦点迁回各自指南。首个切片将共同入口与参考文本从 21,772 减到 12,007 字节；字节不等于实测 token 或质量、成本收益。全部门禁与有效项目约束继续生效。[受控局部文案试验](evals/fixtures/core-route/TASK.md)区分实际模型／工具观察与适配器检查；它不代表旧矩阵全面通过，也未实现通用规则引擎或项目 profile 注册表。

未发布的 v0.1.22 将入口调整为团队任务与交付协调，加入强制 [PMS MCP 接入门禁](skills/engineering-loop/references/connection.md)、Kaneo 依赖声明及每个路由的原创 [grill-me 式拷问](skills/engineering-loop/references/grill.md)。任务写入仍遵守已有授权，仅分析不自动建卡。其[行为矩阵](evals/fixtures/pms-grill-routing/TASK.md)仍未执行；这不是服务端强制门禁或原子领取实现，历史结果不能为新门禁背书，也不证明减少缺陷。

未发布的 v0.1.21 修复带空格尖括号目标和可选标题的行内链接检查；不宣称完整解析 Markdown。

未发布的 v0.1.20 检查全部打包 skill 文档和 JSON，同名本地产物目录也不能绕过；仓库本地产物仍保持排除。这是分发检查修正。

未发布的 v0.1.19 明确同一对话中的插入提问应保留未完成任务，并尊重明确停止、替换目标和仅起草不发送的限制。新增行为用例及反例；尚未进行模型行为评估。

未发布的 v0.1.18 修正评估与分发维护缺陷：门禁执行前准备回执输出、刷新失败检查完整库存保留、根目录本地虚拟环境不参与项目文件验证、路径摘要保留无关前缀。这些是工具修复，不是新的模型质量收益证据。

未发布的 v0.1.17 将通用验证判断与条件化边界场景分开：核心指南按相关风险路由到聚焦参考，保留既有验收约束与轻量反例。结构保留检查和新上下文路由观察记录在[评估入口](evals/README.md)；首次文本变小不等于证明 token 节省或结果提升。

未发布的 v0.1.16 明确委派执行环境：按子任务实际工作目录、环境和权限核对相关能力，不能由主进程的主机能力推断。复用有效证据、简单只读任务保持轻量；通过正确调用修复环境差异，不默认放宽保护或新增工具链。

未发布的 v0.1.15 补充按风险触发的运维准备：业务进度信号、响应归属、有限恢复演练与数据可恢复性证据。本地任务与有意使用的手动 worker 保持轻量，实际演练结果和边界记录在[评估说明](evals/README.md)。

未发布的 v0.1.14 增加前端范围门禁：默认仅桌面端，用户明确要求时才加入对应移动端设计与验收。保留已有移动行为，约定冲突须在依赖变更前明确。

未发布的 v0.1.13 修订补充按需触发的产品假设挑战与聚焦的 [UI 工作指南](skills/engineering-loop/references/ui.md)，明确局部修改保持轻量。第一轮对照的条件与实际结果记录在[评估说明](evals/README.md)；包装检查本身不证明行为收益。

未发布的 v0.1.12 修订要求在依赖回执移交归属或继续任务前，核对保存内容中的身份和状态。[回执检查点对照](evals/fixtures/handoff-receipt/TASK.md)涵盖 null、过期内容、修复回执及普通文字交接；尚未执行，不宣称模型行为收益。

未发布的 v0.1.11 修订补充已授权的对话轮换：用终态产物核对过期归属、移交活跃句柄，并精简贡献者摘要读取。新增 D/E [检查点对照](evals/fixtures/delegated-continuation/TASK.md)尚未执行；本次恢复不能证明 skill 的实测收益。
