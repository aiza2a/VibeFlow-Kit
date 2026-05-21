# 工作流

## 阶段链

`proposal -> high-level-design -> detailed-design -> tasks -> coding`

## 增量变更链

- 功能新增：`change -> affected docs -> affected tasks -> coding -> acceptance`
- Bug 修复：`reproduce -> regression test -> fix -> verify`
- 重构：`scope -> protection tests -> refactor -> full check`

## 阶段原则

- 一阶段一会话
- 一模块一会话
- 一阶段只产出该阶段要求的文件
- 下一阶段只读取上一步已落盘的文件

## 标准推进方式

### 1. 需求确认
- 输入：项目背景、已有工程、资源、限制条件
- 输出：`docs/proposal.md`
- 若需求不明确，先提问，不直接写代码

### 2. 概要设计
- 输入：`docs/proposal.md`
- 输出：`docs/high-level-design.md`
- 目标：模块划分、依赖关系、边界、关键技术选择

### 3. 详细设计
- 输入：`docs/proposal.md`、`docs/high-level-design.md`
- 输出：`docs/detailed-design.md`
- 目标：接口、数据结构、关键流程、测试边界

### 4. 任务切片
- 输入：`docs/proposal.md`、`docs/detailed-design.md`
- 输出：`docs/tasks/*.md`、`docs/tasks/progress.md`
- 目标：把模块切成最小可执行任务，并明确完成标准

### 5. 编码实现
- 输入：前述文档 + 当前模块任务文件
- 输出：代码、测试、文档更新、任务状态更新
- 要求：实现后立即检查，不把大批未验证改动堆到最后

## 持续开发方式

### 新增功能
- 先创建 `docs/changes/feature-<name>.md`
- 评估是否影响 `proposal` / `detailed-design`
- 只为受影响模块更新任务文件
- 按模块增量实现

### Bug 修复
- 先创建 `docs/changes/bugfix-<name>.md`
- 先复现，再补回归测试，再修复
- 若不改变需求边界，通常不改 `proposal.md`

### 重构
- 先创建 `docs/changes/refactor-<name>.md`
- 优先保证外部行为稳定
- 先补保护性测试，再动结构

## 会话控制

- 若当前会话已包含较长历史，应主动切换新会话
- 新会话中只提供必要文件路径和本轮目标
- 不要把整个工程所有文件一次性塞入上下文
