# Claude Code 项目规则

在当前项目中工作时，请遵守以下规则：

1. 先读取 `docs/` 下已有工件，再行动。
2. `docs/` 是唯一事实来源；若历史对话与文档冲突，以文档为准。
3. 启动项目时按阶段推进：`proposal -> high-level-design -> detailed-design -> tasks -> coding`。
4. 持续开发时，优先走增量流：功能新增 / bug 修复 / 重构，不默认从头重跑全部阶段。
5. 需求和设计阶段不要猜测；若存在关键歧义，先提问。
6. 编码阶段只处理当前模块，不同时扩展多个无关目标。
7. 若需增加未在文档中出现的假设，写入 `.ai/state/assumptions.md`。
8. 完成一个任务前，必须通过对应 profile 的 `lint`、`typecheck`、`test`。
9. 完成后更新任务 checklist 和 `docs/tasks/progress.md`。
10. 若会话已很长，应主动建议切换新会话，并只携带必要文件继续。
11. 不要把“看起来没问题”当成完成依据。
12. 新增功能优先创建 `docs/changes/feature-<name>.md`；修 bug 优先创建 `docs/changes/bugfix-<name>.md`；结构优化优先创建 `docs/changes/refactor-<name>.md`。

优先读取：

- `.ai/rules/core.md`
- `.ai/rules/workflow.md`
- `.ai/rules/definition-of-done.md`
- `.ai/state/assumptions.md`
