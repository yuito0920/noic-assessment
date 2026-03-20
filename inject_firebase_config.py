#!/usr/bin/env python3
"""Firebase コンソールの firebaseConfig（JSON）を index.html の FB_CONFIG に埋め込む。"""
import json
import re
import sys
from pathlib import Path

KEYS = (
    "apiKey",
    "authDomain",
    "projectId",
    "storageBucket",
    "messagingSenderId",
    "appId",
)


def build_js_object(cfg: dict) -> str:
    lines = ["const FB_CONFIG = {"]
    for i, k in enumerate(KEYS):
        if k not in cfg:
            raise SystemExit(f"missing key: {k}")
        comma = "," if i < len(KEYS) - 1 else ""
        val = json.dumps(cfg[k], ensure_ascii=False)
        lines.append(f"  {k}: {val}{comma}")
    lines.append("};")
    return "\n".join(lines)


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: inject_firebase_config.py <firebase-config.json> [index.html]", file=sys.stderr)
        sys.exit(1)
    cfg_path = Path(sys.argv[1])
    html_path = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("index.html")
    cfg = json.loads(cfg_path.read_text(encoding="utf-8"))
    html = html_path.read_text(encoding="utf-8")
    new_block = build_js_object(cfg)
    pattern = r"const FB_CONFIG = \{[\s\S]*?\n\};"
    if not re.search(pattern, html):
        raise SystemExit("FB_CONFIG block not found in HTML")
    out = re.sub(pattern, new_block, html, count=1)
    html_path.write_text(out, encoding="utf-8")
    print(f"Updated {html_path}")


if __name__ == "__main__":
    main()
