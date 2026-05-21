#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
TASKS = DOCS / "tasks"
AI_DIR = ROOT / ".ai"
PROFILES = AI_DIR / "profiles"
PROJECT_JSON = AI_DIR / "project.json"


def read_profile(name: str) -> dict[str, Any]:
    path = PROFILES / f"{name}.json"
    if not path.exists():
        raise SystemExit(f"Profile not found: {name} ({path})")
    return json.loads(path.read_text(encoding="utf-8"))


def ensure_file(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists():
        path.write_text(content, encoding="utf-8")


def load_project_config() -> dict[str, Any]:
    if not PROJECT_JSON.exists():
        raise SystemExit("Project config not found. Run: python tools/vcflow.py init --profile <name>")
    return json.loads(PROJECT_JSON.read_text(encoding="utf-8"))


def write_project_config(profile: str) -> None:
    PROJECT_JSON.parent.mkdir(parents=True, exist_ok=True)
    data = {
        "active_profile": profile,
        "docs_dir": "docs",
        "tasks_dir": "docs/tasks",
        "assumptions_file": ".ai/state/assumptions.md",
    }
    PROJECT_JSON.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def cmd_init(profile: str) -> None:
    read_profile(profile)
    DOCS.mkdir(parents=True, exist_ok=True)
    TASKS.mkdir(parents=True, exist_ok=True)

    ensure_file(DOCS / "proposal.md", "# 需求文档\n\n待生成。\n")
    ensure_file(DOCS / "high-level-design.md", "# 概要设计文档\n\n待生成。\n")
    ensure_file(DOCS / "detailed-design.md", "# 详细设计文档\n\n待生成。\n")
    ensure_file(DOCS / "prompt.md", "# 执行 Prompt\n\n待生成。\n")
    ensure_file(TASKS / "progress.md", "# 总体进度\n\n- [ ] 待生成模块任务\n")
    write_project_config(profile)
    print(f"Initialized vibe coding project with profile: {profile}")
    print(f"Project config: {PROJECT_JSON}")


def cmd_show_profile(profile: str | None) -> None:
    if profile is None and PROJECT_JSON.exists():
        data = json.loads(PROJECT_JSON.read_text(encoding="utf-8"))
        profile = data.get("active_profile")
    if not profile:
        raise SystemExit("No profile specified and no .ai/project.json found")
    data = read_profile(profile)
    print(json.dumps(data, ensure_ascii=False, indent=2))


def cmd_set_profile(profile: str) -> None:
    read_profile(profile)
    write_project_config(profile)
    print(f"Active profile set to: {profile}")


def cmd_new_module(name: str) -> None:
    config = load_project_config()
    tasks_dir = ROOT / config.get("tasks_dir", "docs/tasks")
    tasks_dir.mkdir(parents=True, exist_ok=True)
    path = tasks_dir / f"{name}.md"
    if path.exists():
        raise SystemExit(f"Module task file already exists: {path}")
    content = f"# 模块任务：{name}\n\n## 模块目标\n\n待补充。\n\n## 前置依赖\n\n- [ ] 待补充\n\n## 子任务\n\n- [ ] 任务 1\n- [ ] 任务 2\n\n## 完成定义\n\n- [ ] 代码实现完成\n- [ ] 测试已补齐\n- [ ] lint / typecheck / test 通过\n- [ ] 文档与进度已更新\n\n## 风险与备注\n\n- 待补充\n"
    path.write_text(content, encoding="utf-8")
    print(f"Created module task file: {path}")


def cmd_doctor() -> None:
    checks = {
        "docs": DOCS.exists(),
        "tasks": TASKS.exists(),
        "project_json": PROJECT_JSON.exists(),
        "templates": (ROOT / "templates").exists(),
        "claude_rules": (ROOT / "CLAUDE.md").exists(),
        "cursor_rules": (ROOT / ".cursor" / "rules" / "vibe-coding.mdc").exists(),
        "copilot_rules": (ROOT / ".github" / "copilot-instructions.md").exists(),
    }
    missing_cmds = [cmd for cmd in ["python3", "git"] if shutil.which(cmd) is None]
    for name, ok in checks.items():
        print(f"[{ 'OK' if ok else 'MISSING' }] {name}")
    if PROJECT_JSON.exists():
        data = load_project_config()
        print(f"Active profile: {data.get('active_profile')}")
    if missing_cmds:
        print("Missing common commands:", ", ".join(missing_cmds))
    else:
        print("Common commands look available.")
    if not all(checks.values()):
        raise SystemExit(1)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Vibe coding workflow helper")
    sub = parser.add_subparsers(dest="command", required=True)

    p_init = sub.add_parser("init", help="initialize docs and project config")
    p_init.add_argument("--profile", default="python", help="profile name: python/typescript/go/rust")

    p_show = sub.add_parser("show-profile", help="show active or specified profile")
    p_show.add_argument("--profile", default=None)

    p_set = sub.add_parser("set-profile", help="set active profile")
    p_set.add_argument("--profile", required=True)

    p_new = sub.add_parser("new-module", help="create a new module task file")
    p_new.add_argument("--name", required=True)

    sub.add_parser("doctor", help="check starter kit structure and common commands")

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "init":
        cmd_init(args.profile)
    elif args.command == "show-profile":
        cmd_show_profile(args.profile)
    elif args.command == "set-profile":
        cmd_set_profile(args.profile)
    elif args.command == "new-module":
        cmd_new_module(args.name)
    elif args.command == "doctor":
        cmd_doctor()
    else:
        raise SystemExit(f"Unknown command: {args.command}")


if __name__ == "__main__":
    main()
