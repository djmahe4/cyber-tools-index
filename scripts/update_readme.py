#!/usr/bin/env python3
from collections import defaultdict
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent.parent
CONFIG_PATH = ROOT / "tools_config.json"
README_PATH = ROOT / "README.md"

START_MARKER = "<!-- TOOLS:START -->"
END_MARKER = "<!-- TOOLS:END -->"

# Short uppercase acronyms that shouldn't be title-cased as "Osint" or "Dfir"
ACRONYMS = {"osint", "dfir", "iot", "api", "c2", "dns", "vpn", "ssl", "tls", "ssh", "xss", "sql", "pwn"}


def fail(message: str) -> None:
    print(f"::error::{message}", file=sys.stderr)
    sys.exit(1)


def load_and_validate_config(path: Path) -> list[dict]:
    if not path.is_file():
        fail(f"Config file not found: {path}")

    try:
        raw_text = path.read_text(encoding="utf-8")
    except OSError as exc:
        fail(f"Unable to read {path.name}: {exc}")

    if not raw_text.strip():
        fail(f"{path.name} is empty.")

    try:
        data = json.loads(raw_text)
    except json.JSONDecodeError as exc:
        fail(
            f"Invalid JSON in {path.name} at line {exc.lineno}, column {exc.colno}: {exc.msg}"
        )

    if not isinstance(data, list) or len(data) == 0:
        fail(f"{path.name} must contain a non-empty JSON array of tool objects.")

    seen_names: set[str] = set()
    for idx, item in enumerate(data):
        if not isinstance(item, dict):
            fail(f"Entry at index {idx} in {path.name} is not a JSON object.")

        name = item.get("name")
        if not isinstance(name, str) or not name.strip():
            fail(f"Entry at index {idx} is missing a valid 'name' string.")

        norm_name = name.strip().lower()
        if norm_name in seen_names:
            fail(f"Duplicate tool entry '{name.strip()}' found at index {idx}.")
        seen_names.add(norm_name)

        for field in ("method", "module", "url", "description"):
            val = item.get(field)
            if val is not None and not isinstance(val, str):
                fail(
                    f"Entry '{name.strip()}' (index {idx}) has non-string field '{field}'."
                )

    return data


def format_module_heading(module_key: str) -> str:
    # Normalize separators (-, _) and split camelCase or joined "*team" suffixes
    normalized = re.sub(r"[-_]+", " ", module_key.strip())
    normalized = re.sub(r"([a-z])([A-Z])", r"\1 \2", normalized)
    normalized = re.sub(r"(?i)^([a-z]+)(team)$", r"\1 \2", normalized)

    words = [
        word.upper() if word.lower() in ACRONYMS else word.capitalize()
        for word in normalized.split()
    ]
    return " ".join(words) or "Uncategorized"


def build_index_markdown(tools: list[dict]) -> str:
    grouped: dict[str, list[dict]] = defaultdict(list)
    for entry in tools:
        module = (entry.get("module") or "uncategorized").strip()
        grouped[module].append(entry)

    lines: list[str] = []
    sorted_modules = sorted(grouped.keys(), key=lambda m: format_module_heading(m).lower())

    lines.append("## Categories\n")
    for mod in sorted_modules:
        title = format_module_heading(mod)
        anchor = re.sub(r"[^a-z0-9\- ]", "", title.lower()).replace(" ", "-")
        lines.append(f"- [{title}](#{anchor}) ({len(grouped[mod])})")
    lines.append("")

    for mod in sorted_modules:
        title = format_module_heading(mod)
        lines.append(f"## {title}\n")
        lines.append("| Tool | Description |")
        lines.append("| :--- | :--- |")

        entries = sorted(grouped[mod], key=lambda x: x.get("name", "").lower())
        for item in entries:
            name = item["name"].strip()
            url = (item.get("url") or "").strip()
            desc = (item.get("description") or "").replace("\n", " ").replace("|", "\\|").strip()

            tool_ref = f"[{name}]({url})" if url else f"**{name}**"
            lines.append(f"| {tool_ref} | {desc} |")

        lines.append("")

    return "\n".join(lines).rstrip()


def main() -> None:
    tools = load_and_validate_config(CONFIG_PATH)

    if not README_PATH.is_file():
        fail(f"Target file not found: {README_PATH}")

    readme = README_PATH.read_text(encoding="utf-8")

    if START_MARKER not in readme or END_MARKER not in readme:
        fail(f"Missing {START_MARKER} or {END_MARKER} in {README_PATH.name}")

    generated_block = build_index_markdown(tools)
    replacement = f"{START_MARKER}\n{generated_block}\n{END_MARKER}"

    pattern = re.compile(
        rf"{re.escape(START_MARKER)}.*?{re.escape(END_MARKER)}",
        flags=re.DOTALL,
    )
    updated_readme, count = pattern.subn(replacement, readme, count=1)
    if count != 1:
        fail("Failed to replace tools block cleanly.")

    if updated_readme != readme:
        README_PATH.write_text(updated_readme, encoding="utf-8")
        print(f"README.md updated with {len(tools)} tools across {len(set(t.get('module') for t in tools))} categories.")
    else:
        print("No changes detected in README.md.")


if __name__ == "__main__":
    main()
