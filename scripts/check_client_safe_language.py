#!/usr/bin/env python3
"""Scan client-facing files for protected Ocean proposal language.

Supports plain text, JSON, PPTX and PDF. The rule source is
brand/client-safe-language.json so non-engineers can review the list.
"""
from __future__ import annotations
import argparse
import json
import re
import sys
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
RULES = json.loads((ROOT / "brand" / "client-safe-language.json").read_text(encoding="utf-8"))


def read_text(path: Path) -> str:
    suffix = path.suffix.lower()
    if suffix == ".pptx":
        chunks: list[str] = []
        with zipfile.ZipFile(path) as zf:
            for name in sorted(n for n in zf.namelist() if n.startswith("ppt/slides/slide") and n.endswith(".xml")):
                root = ET.fromstring(zf.read(name))
                chunks.extend(el.text or "" for el in root.iter() if el.tag.endswith("}t"))
        return "\n".join(chunks)
    if suffix == ".pdf":
        try:
            import fitz  # PyMuPDF
        except Exception as exc:  # pragma: no cover - environment-dependent message
            raise SystemExit(f"PDF scan requires PyMuPDF: {exc}")
        with fitz.open(path) as doc:
            return "\n".join(page.get_text() for page in doc)
    return path.read_text(encoding="utf-8", errors="ignore")


def scan(text: str, include_sensitive_tools: bool, allow: set[str]) -> list[tuple[str, str, str]]:
    rules = list(RULES["blocked"])
    if include_sensitive_tools:
        rules.extend(RULES.get("sensitiveTools", []))
    hits: list[tuple[str, str, str]] = []
    for rule in rules:
        rx = re.compile(rule["pattern"], re.IGNORECASE)
        for match in rx.finditer(text):
            found = match.group(0)
            if found.lower() in allow or rule["label"].lower() in allow:
                continue
            hits.append((rule["label"], found, rule.get("reason", "Sensitive term should be reviewed before client release.")))
    return hits


def main() -> int:
    parser = argparse.ArgumentParser(description="Check client-facing proposal language.")
    parser.add_argument("files", nargs="+", type=Path)
    parser.add_argument("--allow", action="append", default=[], help="Allowed exact term or rule label; repeatable.")
    parser.add_argument("--skip-sensitive-tools", action="store_true", help="Skip tool/provider name checks.")
    args = parser.parse_args()
    allow = {item.lower() for item in args.allow}
    failed = False
    for file in args.files:
      text = read_text(file)
      hits = scan(text, not args.skip_sensitive_tools, allow)
      if hits:
          failed = True
          print(f"FAIL {file}")
          for label, found, reason in hits:
              print(f"  {found} [{label}] - {reason}")
      else:
          print(f"PASS {file}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
