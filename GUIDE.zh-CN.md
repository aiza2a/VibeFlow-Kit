# 使用指南（中文）

## 这个仓库解决什么问题

它解决的不是“某个 Agent 不会写代码”，而是：

- 项目一复杂，聊天上下文越来越乱
- AI 改一点坏一点，最后变成垃圾场
- 不同 IDE / Agent 工具之间规则不一致
- 代码、文档、测试、进度没有统一事实来源

这个仓库把这些问题收敛成一套固定工作流：

1. 先写需求文档
2. 再写概要设计
3. 再写详细设计
4. 再拆成模块任务
5. 最后生成执行 Prompt 并进入编码

## 你该怎么用

### 新项目

1. 复制本仓库模板到你的项目根目录
2. 运行：

```bash
python tools/vcflow.py init --profile python
```

3. 把 `templates/01-proposal.prompt.md` 粘给你的 IDE Agent
4. 让 Agent 产出 `docs/proposal.md`
5. 切换新会话，继续 `02 -> 03 -> 04 -> 05`

### 现有项目

1. 把本仓库中的这些目录复制到现有项目：
   - `templates/`
   - `.ai/`
   - `tools/`
   - `CLAUDE.md`
   - `.cursor/rules/`
   - `.github/copilot-instructions.md`
2. 运行 `init`
3. 从需求梳理或增量需求梳理开始，而不是直接让 AI 改代码

## 最重要的使用原则

- 一阶段一会话
- 一模块一会话
- 文件是事实来源，聊天不是
- 不明确时先问，别让 AI 猜
- 编码完成不等于完成，过检查才算完成

## 不同工具怎么接入

### Claude Code
- 让它先读 `CLAUDE.md`
- 每一轮只给当前模板和当前输入文件

### Cursor
- 保留 `.cursor/rules/vibe-coding.mdc`
- 让它优先读 `docs/`

### Copilot
- 保留 `.github/copilot-instructions.md`
- 仍然用 `templates/*.prompt.md` 驱动

### Windsurf / Cline
- 能配 workspace 规则就配 `.ai/rules/`
- 不能配就直接喂 `docs/` 和模板

## 什么时候不适合用它

- 5 分钟能写完的一次性脚本
- 需求极其稳定、代码量极小、完全不需要长期维护的任务
- 你只想快速做个 throwaway prototype，做完就扔

## 什么时候特别适合

- 需求会反复变化
- 你要在多个 IDE / Agent 之间切换
- 你想让 AI 长期持续开发，而不是只生成一次代码
- 你需要文档、进度、测试、检查一起受控
