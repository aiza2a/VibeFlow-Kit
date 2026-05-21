# Claude Code 项目规则

在当前项目中工作时，请遵守以下规则：

1. 先读取 `docs/` 下已有工件，再行动。
2. `docs/` 是唯一事实来源；若历史对话与文档冲突，以文档为准。
3. 按阶段推进：`proposal -> high-level-design -> detailed-design -> tasks -> coding`。
4. 需求和设计阶段不要猜测；若存在关键歧义，先提问。
5. 编码阶段只处理当前模块，不同时扩展多个无关目标。
6. 若需增加未在文档中出现的假设，写入 `.ai/state/assumptions.md`。
7. 完成一个任务前，必须通过对应 profile 的 `lint`、`typecheck`、`test`。
8. 完成后更新任务 checklist 和 `docs/tasks/progress.md`。
9. 若会话已很长，应主动建议切换新会话，并只携带必要文件继续。
10. 不要把“看起来没问题”当成完成依据。

优先读取：

- `.ai/rules/core.md`
- `.ai/rules/workflow.md`
- `.ai/rules/definition-of-done.md`
- `.ai/state/assumptions.md`
