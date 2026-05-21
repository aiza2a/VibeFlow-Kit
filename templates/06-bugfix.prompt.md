# 阶段 6：Bug 修复 Prompt

## 目标
针对一个已知 bug，执行稳定的修复流程：复现 -> 回归测试 -> 修复 -> 验证。

## 输入
- 相关模块任务文件，例如 `docs/tasks/<module>.md`
- 相关设计文档，例如 `docs/detailed-design.md`
- 若存在，读取对应变更文件：`docs/changes/bugfix-<name>.md`
- 当前 bug 描述、报错、复现步骤

## 输出
- 修复后的代码与测试
- 必要时更新 `docs/tasks/<module>.md`
- 必要时更新 `docs/changes/bugfix-<name>.md`
- 更新 `docs/tasks/progress.md`

## 步骤
1. 先确认 bug 的可观察现象和复现条件。
2. 优先补一个能稳定捕获问题的回归测试。
3. 在模块边界内修复问题，不无关扩展。
4. 若修复不改变需求边界，通常不改 `docs/proposal.md`；若暴露设计缺陷，再更新相关设计文档。
5. 修复后运行对应 profile 的 lint / typecheck / test。
6. 若有重要假设或取舍，写入 `.ai/state/assumptions.md` 或变更文件。
