# VibeFlow Kit

一个面向 **Claude Code / Cursor / VS Code Copilot / Windsurf / Cline** 的通用 AI 项目工作流模板仓库。

它不是某个 IDE 的插件，也不是某个模型专属的 Skill，而是一层**位于项目仓库内部的工作流框架**：

- 用固定工件管理需求、设计、任务、进度、变更、决策、验收
- 用固定模板约束每个阶段或每类增量工作的 Prompt
- 用统一脚本运行检查、生成任务骨架、生成变更文档、切换语言 profile
- 用轻量适配层接入不同 IDE / Agent 工具

## 它的定位

这个仓库主要解决 5 类问题：

1. **上下文失控**：项目一复杂，聊天越来越长，Agent 开始遗忘和幻觉
2. **多工具漂移**：Claude Code、Cursor、Copilot、Windsurf 的行为风格不一致
3. **质量失守**：代码、测试、静态检查、文档、进度各自为政
4. **持续开发无章法**：新增功能、修 bug、重构时容易从头乱改
5. **长期维护困难**：AI 写出来的项目能跑，但很难继续开发

所以它的核心不是“让 AI 更会写代码”，而是让 AI 处在一个**更稳定、可审计、可切换、可继续开发**的工程壳里。

## 核心方法

### 启动项目时

```text
proposal -> high-level-design -> detailed-design -> tasks -> coding
```

### 持续开发时

```text
feature change -> affected docs -> affected tasks -> coding -> acceptance
bugfix -> reproduce -> regression test -> fix -> verify
refactor -> scope -> protection tests -> refactor -> full check
```

固定原则：

- `docs/` 是唯一事实来源
- 一阶段一会话
- 一模块一会话
- 需求/设计阶段不猜，先问
- 编码阶段按文档执行，必要时记录假设
- 完成必须经过检查脚本，而不是口头宣布

## 仓库结构

```text
.
├─ docs/
│  ├─ proposal.md
│  ├─ high-level-design.md
│  ├─ detailed-design.md
│  ├─ prompt.md
│  ├─ acceptance.md
│  ├─ release-checklist.md
│  ├─ changes/
│  ├─ decisions/
│  └─ tasks/
├─ templates/
│  ├─ 01-proposal.prompt.md
│  ├─ 02-high-level-design.prompt.md
│  ├─ 03-detailed-design.prompt.md
│  ├─ 04-tasks.prompt.md
│  ├─ 05-coding.prompt.md
│  ├─ 06-bugfix.prompt.md
│  ├─ 07-feature-change.prompt.md
│  └─ 08-refactor.prompt.md
├─ .ai/
│  ├─ rules/
│  ├─ profiles/
│  ├─ state/
│  └─ project.json
├─ tools/
│  ├─ vcflow.py
│  ├─ check.py
│  └─ progress.py
├─ examples/
├─ CLAUDE.md
├─ .cursor/rules/vibeflow.mdc / vibe-coding.mdc
├─ .github/copilot-instructions.md
├─ .github/workflows/quality.yml
├─ Makefile
├─ GUIDE.zh-CN.md
└─ README.md
```

## 已提供的能力

### 1. 启动项目模板

- 5 个启动阶段模板：`templates/01` 到 `templates/05`
- 通用规则：`.ai/rules/*`
- 假设记录：`.ai/state/assumptions.md`

### 2. 持续开发模板

- `templates/06-bugfix.prompt.md`
- `templates/07-feature-change.prompt.md`
- `templates/08-refactor.prompt.md`

### 3. 增量工件

- `docs/changes/`：功能变更 / bugfix / refactor
- `docs/decisions/`：ADR 风格决策记录
- `docs/acceptance.md`：验收清单
- `docs/release-checklist.md`：发布清单

### 4. 脚手架层

`tools/vcflow.py` 当前支持：

- `init`：初始化 `docs/` 与项目配置
- `show-profile`：显示当前或指定 profile
- `set-profile`：切换活动 profile
- `new-module`：生成模块任务文件骨架
- `new-change`：生成功能/bugfix/重构变更文件
- `new-decision`：生成决策记录文件
- `doctor`：检查目录和常见命令是否齐备

### 5. 检查层

`tools/check.py`：按当前 profile 统一执行：

- `format`（可选）
- `lint`
- `typecheck`
- `test`

`tools/progress.py`：根据 `docs/tasks/*.md` 自动刷新 `progress.md`

### 6. 多语言层

已内置 profile：

- `python`
- `typescript`
- `go`
- `rust`

### 7. IDE 适配层

- `CLAUDE.md`
- `.cursor/rules/vibe-coding.mdc`
- `.github/copilot-instructions.md`

## 快速开始

### 新项目

```bash
python tools/vcflow.py init --profile python
python tools/vcflow.py doctor
```

然后按顺序使用：

1. `templates/01-proposal.prompt.md`
2. `templates/02-high-level-design.prompt.md`
3. `templates/03-detailed-design.prompt.md`
4. `templates/04-tasks.prompt.md`
5. `templates/05-coding.prompt.md`

### 持续开发

#### 新增功能

```bash
python tools/vcflow.py new-change --type feature --name tags
```

然后让 IDE 读取：

- `docs/changes/feature-tags.md`
- `docs/proposal.md`
- `docs/detailed-design.md`
- `templates/07-feature-change.prompt.md`

#### 修复 bug

```bash
python tools/vcflow.py new-change --type bugfix --name search-crash
```

然后让 IDE 读取：

- `docs/changes/bugfix-search-crash.md`
- `docs/detailed-design.md`
- 对应模块任务文件
- `templates/06-bugfix.prompt.md`

#### 重构

```bash
python tools/vcflow.py new-change --type refactor --name storage-cleanup
```

然后让 IDE 读取：

- `docs/changes/refactor-storage-cleanup.md`
- `docs/detailed-design.md`
- 对应模块任务文件
- `templates/08-refactor.prompt.md`

### 常用命令

```bash
python tools/vcflow.py init --profile python
python tools/vcflow.py set-profile --profile rust
python tools/vcflow.py show-profile
python tools/vcflow.py doctor
python tools/vcflow.py new-module --name parser
python tools/vcflow.py new-change --type feature --name tags
python tools/vcflow.py new-change --type bugfix --name search-crash
python tools/vcflow.py new-change --type refactor --name storage-cleanup
python tools/vcflow.py new-decision --title "Choose local file storage"
python tools/check.py
python tools/check.py --include-format
python tools/progress.py
```

或使用 Makefile：

```bash
make init
make doctor
make check
make fmt
make new-module name=parser
make new-feature name=tags
make new-bugfix name=search-crash
make new-refactor name=storage-cleanup
make new-decision title="Choose local file storage"
make progress
```

## 推荐使用方式

### Claude Code

- 先让它读取 `CLAUDE.md`
- 启动项目时，每次只给当前模板 + 当前输入文件
- 持续开发时，先创建 `docs/changes/*.md`，再进入实现
- 长会话后主动切换新会话
- 编码阶段按 `docs/tasks/*.md` 一模块一轮

### Cursor

- 长期规则放 `.cursor/rules/vibe-coding.mdc`
- 当前任务依然由 `templates/*.prompt.md` 驱动
- 让 Cursor 优先读取 `docs/`，不要依赖聊天历史

### Copilot / Copilot Chat

- 仓库中保留 `.github/copilot-instructions.md`
- 用模板推进各阶段，而不是把所有需求一次性丢给 Copilot
- 持续开发时优先用 `docs/changes/*.md` 管理本轮目标

### Windsurf / Cline

- 能配置 workspace rules 就接入 `.ai/rules/`
- 不能配置就直接把 `docs/` 和当前模板作为输入上下文

## 与 Skill、MCP、Agent 的区别

- **Skill**：能力说明书
- **MCP**：工具/资源接入协议
- **Agent**：执行主体与调度逻辑
- **VibeFlow Kit**：项目工作流与工件组织框架

它不是替代前三者，而是在它们之上补了一层：

> 当 AI 真正进入长期项目开发时，项目如何稳定推进、稳定变更、稳定验收。
