#!/usr/bin/env python3
"""Validate every skills/*/SKILL.md against the Agent Skills spec (agentskills.io/specification)."""
import json, pathlib, re, sys
import yaml

root = pathlib.Path(__file__).resolve().parent.parent
errors = []
for skill_md in sorted(root.glob("plugin/skills/*/SKILL.md")):
    d = skill_md.parent
    text = skill_md.read_text(encoding="utf-8")
    parts = text.split("---", 2)
    if len(parts) < 3 or parts[0].strip():
        errors.append(f"{skill_md}: missing YAML frontmatter"); continue
    fm = yaml.safe_load(parts[1]) or {}
    name, desc = fm.get("name", ""), fm.get("description", "")
    if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", name) or len(name) > 64:
        errors.append(f"{skill_md}: invalid name '{name}'")
    if name != d.name:
        errors.append(f"{skill_md}: name '{name}' != folder '{d.name}'")
    if not 1 <= len(desc) <= 1024:
        errors.append(f"{skill_md}: description length {len(desc)} not in 1..1024")
    for k, v in (fm.get("metadata") or {}).items():
        if not isinstance(v, str):
            errors.append(f"{skill_md}: metadata.{k} must be a string")
    lines = text.count("\n")
    if lines > 500:
        errors.append(f"{skill_md}: {lines} lines (spec recommends < 500)")
    for ref in re.findall(r"`((?:references|scripts|assets)/[^`]+)`", text):
        if not (d / ref).exists():
            errors.append(f"{skill_md}: referenced file missing: {ref}")
    for j in d.glob("evals/*.json"):
        try: json.loads(j.read_text(encoding="utf-8"))
        except ValueError as e: errors.append(f"{j}: invalid JSON ({e})")
    print(f"checked {d.name}: {lines} lines, description {len(desc)} chars")

for j in list(root.glob(".claude-plugin/*.json")) + list(root.glob("plugin/.claude-plugin/*.json")):
    try: json.loads(j.read_text(encoding="utf-8"))
    except ValueError as e: errors.append(f"{j}: invalid JSON ({e})")

if errors:
    print("\n".join(errors)); sys.exit(1)
print("OK")
