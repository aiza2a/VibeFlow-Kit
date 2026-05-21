# 阶段 7：功能变更 Prompt

## 目标
为现有项目新增一个功能，并以增量方式更新文档、任务和实现。

## 输入
- `docs/proposal.md`
- `docs/detailed-design.md`
- `docs/tasks/progress.md`
- 对应变更文件：`docs/changes/feature-<name>.md`

## 输出
- 必要时更新 `docs/proposal.md`
- 必要时更新 `docs/detailed-design.md`
- 新增或更新 `docs/tasks/*.md`
- 完成代码、测试与进度更新

## 步骤
1. 先评估这次功能影响哪些模块和验收标准。
2. 若变更会影响需求边界或用户可见行为，先更新 `docs/proposal.md`。
3. 若变更会影响接口、数据流或模块边界，更新 `docs/detailed-design.md`。
4. 为受影响模块新增或更新任务文件。
5. 按模块逐步实现，不一次性改完整个项目。
6. 每完成一个模块都运行检查，并更新 `progress.md`。
