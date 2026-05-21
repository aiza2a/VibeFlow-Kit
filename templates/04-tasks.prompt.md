# 阶段 4：模块任务划分

## 目标
根据需求文档和详细设计文档，为每个模块划分最小可执行任务。

## 输入
- `docs/proposal.md`
- `docs/detailed-design.md`

## 输出
- `docs/tasks/<module-name>.md`
- `docs/tasks/progress.md`

## 步骤
1. 阅读需求与详细设计。
2. 为每个模块生成独立任务文件，按最小可执行任务拆分。
3. 每个任务文件使用 checklist，体现子任务完成状态。
4. `docs/tasks/progress.md` 使用 checklist 跟踪每个模块总体状态。
5. 每个模块任务文件建议包含：
   - 模块目标
   - 前置依赖
   - 子任务列表
   - 完成定义
   - 测试要求
   - 风险与备注
6. 这里默认不再主动扩展需求；若文档已足够，则直接生成任务拆分结果。
