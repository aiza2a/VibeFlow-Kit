#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
TASKS_DIR = ROOT / "docs" / "tasks"
PROGRESS = TASKS_DIR / "progress.md"

CHECKED = re.compile(r"^- \[x\]", re.IGNORECASE)
UNCHECKED = re.compile(r"^- \[ \]")


def module_done(path: Path) -> bool:
    lines = path.read_text(encoding="utf-8").splitlines()
    has_unchecked = any(UNCHECKED.match(line.strip()) for line in lines)
    has_checked = any(CHECKED.match(line.strip()) for line in lines)
    return has_checked and not has_unchecked


def main() -> None:
    TASKS_DIR.mkdir(parents=True, exist_ok=True)
    task_files = sorted(p for p in TASKS_DIR.glob("*.md") if p.name != "progress.md")

    lines = ["# 总体进度", ""]
    if not task_files:
        lines.append("- [ ] 暂无模块任务文件")
    else:
        for path in task_files:
            name = path.stem
            mark = "x" if module_done(path) else " "
            lines.append(f"- [{mark}] {name}")

    PROGRESS.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Updated progress: {PROGRESS}")


if __name__ == "__main__":
    main()
