#!/usr/bin/env python3
"""Rewrite AWS vault: move files per manifest, retag line 1, fix ### heading, remap wikilinks."""
import os
import subprocess
import sys

ROOT = "/Users/lizard/Library/Mobile Documents/iCloud~md~obsidian/Documents/AWS"
MANIFEST = os.path.join(ROOT, "tools", "moves.tsv")
SKIP_DIRS = {".git", ".trash", ".obsidian", ".makemd", ".space", "Tags", "tools", "docs"}


def load_manifest():
    moves = []
    with open(MANIFEST, encoding="utf-8") as fh:
        for line in fh:
            line = line.rstrip("\n")
            if not line or line.startswith("#"):
                continue
            old, new, tag, kind = line.split("\t")
            moves.append((old, new, tag, kind))
    return moves


def relink_map(moves):
    m = {}
    for old, new, tag, kind in moves:
        old_base = os.path.splitext(os.path.basename(old))[0]
        new_base = os.path.splitext(os.path.basename(new))[0]
        if old_base != new_base:
            m[old_base] = new_base
    return m


def retag_content(path, name, tag, kind):
    with open(path, encoding="utf-8") as fh:
        lines = fh.read().split("\n")
    if lines:
        lines[0] = f"#AWS #{kind} #{tag}"
    for i, ln in enumerate(lines):
        if ln.startswith("### "):
            lines[i] = f"### {name}"
            break
    return "\n".join(lines)


def main():
    moves = load_manifest()
    rmap = relink_map(moves)
    for old, new, tag, kind in moves:
        oldp = os.path.join(ROOT, old)
        newp = os.path.join(ROOT, new)
        os.makedirs(os.path.dirname(newp), exist_ok=True)
        if os.path.exists(oldp):
            subprocess.run(["git", "mv", oldp, newp], check=False)
            if not os.path.exists(newp) and os.path.exists(oldp):
                os.rename(oldp, newp)
        if os.path.exists(newp):
            name = os.path.splitext(os.path.basename(new))[0]
            content = retag_content(newp, name, tag, kind)
            for oldb, newb in rmap.items():
                content = content.replace(f"[[{oldb}", f"[[{newb}")
            with open(newp, "w", encoding="utf-8") as fh:
                fh.write(content)
    for dirpath, dirs, files in os.walk(ROOT):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for fn in files:
            if not fn.endswith(".md"):
                continue
            p = os.path.join(dirpath, fn)
            with open(p, encoding="utf-8") as fh:
                c = fh.read()
            changed = False
            for oldb, newb in rmap.items():
                if f"[[{oldb}" in c:
                    c = c.replace(f"[[{oldb}", f"[[{newb}")
                    changed = True
            if changed:
                with open(p, "w", encoding="utf-8") as fh:
                    fh.write(c)
    print("retag.py complete: moved/retagged/linked")


if __name__ == "__main__":
    main()
