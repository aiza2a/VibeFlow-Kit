# 阶段 5：Vibe Coding 执行 Prompt 生成

## 目标
生成用于编码执行的主 Prompt。

## 输入
- `docs/proposal.md`
- `docs/high-level-design.md`
- `docs/detailed-design.md`
- `docs/tasks/`
- `.ai/rules/definition-of-done.md`
- `.ai/state/assumptions.md`

## 输出
- `docs/prompt.md`

## 步骤
1. 阅读所有输入文件，理解当前工程、模块边界、任务列表与完成定义。
2. 生成一个用于主 Agent 的执行 Prompt，要求：
   - 主 Agent 负责跟踪整体进度、分发模块、汇总结果
   - 子 Agent 或独立会话负责单模块实现与测试
   - 整个过程中优先依据 `docs/` 文档，不依赖历史聊天
3. Prompt 中必须要求每个模块实现时：
   - 先读对应任务文件
   - 只在本模块边界内改动
   - 编写并运行必要测试
   - 通过当前语言 profile 对应的 lint / typecheck / test
   - 更新任务 checklist 与 `docs/tasks/progress.md`
4. 若语言为弱类型或高动态语言，应强调测试和静态检查。
5. 若有重要歧义且现有文档不足以支撑编码，再向我提问；否则直接生成 `docs/prompt.md`。
