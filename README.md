# Vibe Coding Starter Kit

一个面向 **Claude Code / Cursor / VS Code Copilot / Windsurf / Cline** 的通用 Vibe Coding 工作流模板仓库。

它不是某个 IDE 的插件，也不是某个模型专属的 Skill，而是一层**位于项目仓库内部的工作流框架**：

- 用固定工件管理需求、设计、任务、进度
- 用固定模板约束每个阶段的 Prompt
- 用统一脚本运行检查、生成任务骨架、切换语言 profile
- 用轻量适配层接入不同 IDE / Agent 工具

## 它的定位

这个仓库主要解决 4 类问题：

1. **上下文失控**：项目一复杂，聊天越来越长，Agent 开始遗忘和幻觉
2. **多工具漂移**：Claude Code、Cursor、Copilot、Windsurf 的行为风格不一致
3. **质量失守**：代码、测试、静态检查、文档、进度各自为政
4. **长期维护困难**：AI 写出来的项目能跑，但很难继续开发

所以它的核心不是“让 AI 更会写代码”，而是让 AI 处在一个**更稳定、可审计、可切换、可继续开发**的工程壳里。

## 核心方法

固定阶段链：

```text
proposal -> high-level-design -> detailed-design -> tasks -> coding
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
├─ docs/                      # 项目工件，唯一事实来源
│  ├─ proposal.md
│  ├─ high-level-design.md
│  ├─ detailed-design.md
│  ├─ prompt.md
│  └─ tasks/
│     └─ progress.md
├─ templates/                 # 5 个阶段的 prompt 模板
├─ .ai/
│  ├─ rules/                  # 通用规则
│  ├─ profiles/               # 语言 profile
│  ├─ state/                  # 当前项目状态与假设
│  └─ project.json            # init 后生成
├─ tools/
│  ├─ vcflow.py               # 初始化 / profile / doctor / new-module
│  ├─ check.py                # 统一检查入口
│  └─ progress.py             # 根据任务文件刷新 progress.md
├─ examples/
│  └─ python-demo/
├─ CLAUDE.md                  # Claude Code 适配
├─ .cursor/rules/vibe-coding.mdc
├─ .github/copilot-instructions.md
├─ .github/workflows/quality.yml
├─ Makefile
├─ GUIDE.zh-CN.md
└─ README.md
```

## 已提供的能力

### 1. 模板层

- 5 个阶段模板：`templates/01` 到 `templates/05`
- 通用规则：`.ai/rules/*`
- 假设记录：`.ai/state/assumptions.md`

### 2. 脚手架层

`tools/vcflow.py` 当前支持：

- `init`：初始化 `docs/` 与项目配置
- `show-profile`：显示当前或指定 profile
- `set-profile`：切换活动 profile
- `new-module`：生成模块任务文件骨架
- `doctor`：检查目录和常见命令是否齐备

### 3. 检查层

`tools/check.py`：按当前 profile 统一执行：

- `format`（可选）
- `lint`
- `typecheck`
- `test`

`tools/progress.py`：根据 `docs/tasks/*.md` 自动刷新 `progress.md`

### 4. 多语言层

已内置 profile：

- `python`
- `typescript`
- `go`
- `rust`

### 5. IDE 适配层

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

### 现有项目

把本仓库文件复制到现有项目根目录，然后执行：

```bash
python tools/vcflow.py init --profile python
```

如果你需要先给某个模块建任务文件：

```bash
python tools/vcflow.py new-module --name auth
python tools/progress.py
```

### 常用命令

```bash
python tools/vcflow.py init --profile python
python tools/vcflow.py set-profile --profile rust
python tools/vcflow.py show-profile
python tools/vcflow.py doctor
python tools/vcflow.py new-module --name parser
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
make progress
```

## 推荐使用方式

### Claude Code

- 先让它读取 `CLAUDE.md`
- 每次只给当前模板 + 当前输入文件
- 长会话后主动切换新会话
- 编码阶段按 `docs/tasks/*.md` 一模块一轮

### Cursor

- 长期规则放 `.cursor/rules/vibe-coding.mdc`
- 当前任务依然由 `templates/*.prompt.md` 驱动
- 让 Cursor 优先读取 `docs/`，不要依赖聊天历史

### Copilot / Copilot Chat

- 仓库中保留 `.github/copilot-instructions.md`
- 用模板推进各阶段，而不是把所有需求一次性丢给 Copilot

### Windsurf / Cline

- 能配置 workspace rules 就接入 `.ai/rules/`
- 不能配置就直接把 `docs/` 和当前模板作为输入上下文
