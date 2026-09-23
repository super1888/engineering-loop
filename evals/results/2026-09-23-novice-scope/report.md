# 新手需求范围迭代试跑（2026-09-23）

上一轮[单次试跑](../2026-09-23-novice-onboarding/report.md)发现：用户已经举出“午餐 20 元、关掉网页再打开仍可见”的第一步，助手仍把收入、修改、删除等完整记账功能带进当前范围。本轮先冻结[四组开发场景](../../goldens/novice-scope-v2.json)，再按同一输入连续测试旧版和两次窄幅修订；看到第二次修订在完整第一版里新增“历史月份切换”后，另冻[三组复测场景](../../goldens/novice-scope-v3.json)，比较旧版与第三次修订。两套场景共完成 18 次独立的双轮模型对话（36 个模型回合），所有回合都正常结束。

## 运行条件和证据

- Windows 11、Codex CLI `0.146.1`、账号默认模型；CLI JSON 事件未暴露具体模型身份。每组从独立空工作区和新会话开始，放入对应 skill 快照；两轮在同一工作区恢复。使用 `--ignore-user-config --skip-git-repo-check --sandbox read-only`，没有委派或产品文件写入。判定标准没有提供给被测会话。
- [运行器](../../run_dialogue_trial.py)保留每轮完整事件、最终回复、退出码、用量和实际命令次数；五个版本各有运行清单，例如[旧版清单](baseline/manifest.json)，并保留对应案例的 `turn1/turn2` 记录。事件中的本机用户名已脱敏。中间两版需求指南快照为[第一次修订](skill-iterations/requirements-v1.md)和[第二次修订](skill-iterations/requirements-v2.md)；旧版对应源修订 `01e1ba6`，最终版见当前 `references/requirements.md`。各运行清单记录了完整 skill 文件哈希与场景哈希。
- 五个版本依次为 `baseline`（原指导）、`candidate-v1`（区分下一切片与完整第一版）、`candidate-v2`（不让可逆字段选择阻塞已给出的示例）、`v3-baseline`（旧指导重跑）及 `v3-candidate`（同时约束完整第一版的无依据扩展）。对应模型回合数为 8、8、8、6、6；CLI 输入/输出 token 分别为 575,623/13,833、634,117/12,981、691,599/15,349、645,848/14,590、611,410/12,202。这是实际 CLI 用量，不是价格或受控效率比较；墙钟时间没有统一记录。

## 观察到的迭代

| 版本 | 已观察到的关键结果 |
|---|---|
| 旧版，四组开发场景 | 单笔支出组在给出可验收步骤后，仍问“先只记支出还是同时记收入”；[第二轮回复](baseline/single-expense/turn2/final.txt)。读书记录、完整记账和跨设备隐私组保住了主要要求。 |
| 第一次修订 | 单笔支出组不再问收入，但改问“日期是否自动记录”才能确定第一步；[第二轮回复](candidate-v1/single-expense/turn2/final.txt)。 |
| 第二次修订 | 单笔支出组形成可直接实现的闭环；[第二轮回复](candidate-v2/single-expense/turn2/final.txt)。读书记录仍额外请求接受浏览器清理数据后的丢失限制；完整记账组把未要求的“月份切换”写成 V1 必做，这是评审输出时发现的范围扩张，原 v2 判定点未覆盖，未事后把它算作预先定义的失败。跨设备组保住了同步和未登录隔离。 |
| 旧版，三组新复测 | 喝水打卡和“本月完整记账、历史月份以后再说”对照通过；午餐重复组又问是否加入收入；[第二轮回复](v3-baseline/single-expense-repeat/turn2/final.txt)。 |
| 最终修订，三组新复测 | [喝水打卡](v3-candidate/habit-first-step/turn2/final.txt)和[午餐](v3-candidate/single-expense-repeat/turn2/final.txt)组均给出第一步并停止非必要提问；[完整记账](v3-candidate/current-month-release/turn2/final.txt)保留收入、支出、改删及本月汇总，明确把历史月份专门浏览留到以后。 |

三组复测的匿名配对材料在 [reviewer/packet.json](reviewer/packet.json)，左右对应关系在 [private/key.json](private/key.json)。冻结的 v3 场景只为盲评补入两轮用户原话，生成 [review-suite-v3.json](review-suite-v3.json)；判定点未更改。[独立模型评审](reviewer/review.json)逐项评定最终版 9/9 通过，旧版 7/9 通过；最终版在喝水打卡和午餐组获偏好，完整记账组并列。[探索性门禁](pilot-decision.json)通过。[发布门禁](release-decision.json)按预期拒绝，因为没有人工盲评；没有据此声称可发布。

最终指导只在[需求指南](../../../skills/engineering-loop/references/requirements.md)增加一个紧贴现有“当前切片”原则的段落：用户的具体示例足以确定下一步时，直接给出可检查行为，把可逆细节作为默认建议；明确要求的完整第一版则保留全部必需项，同时不自动加入邻近产品功能。入口、阶段路由和技术栈选择未改。更广的模型质量、真实新手可理解性、可写环境下的执行表现以及成本收益仍未验证；单次随机输出和模型盲评都不能证明普遍提升。
