#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
diagrams/src/*.svg を docs/assets/images/*@2x.png へ書き出す。

- 書き出し時のみ font-family を単一ファミリへ置換（cairosvg はフォールバック非対応のため）
- 全テキストがフォントに収録されているか検査し、欠字があれば異常終了（豆腐の混入を防ぐ）

使い方:
    python diagrams/build.py            # 書き出し
    python diagrams/build.py --check    # 検査のみ（CI用）
"""
import re
import subprocess
import sys
from pathlib import Path

import cairosvg
from fontTools.ttLib import TTFont

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "diagrams" / "src"
OUT = ROOT / "docs" / "assets" / "images"

RENDER_FONT = "Noto Sans CJK JP"   # 書き出し環境に実在するファミリ名
SCALE = 2                          # @2x


def font_cmap(family: str):
    path = subprocess.check_output(["fc-match", "-f", "%{file}", family]).decode()
    resolved = subprocess.check_output(["fc-match", "-f", "%{family}", family]).decode()
    if family.split(",")[0].strip("'\" ") not in resolved:
        sys.exit(f"[ERROR] フォント '{family}' が解決できません（実際: {resolved}）。"
                 f" fonts-noto-cjk をインストールしてください。")
    return TTFont(path, fontNumber=0).getBestCmap()


def check_glyphs(svg_text: str, cmap, name: str) -> list:
    chars = set("".join(re.findall(r">([^<>]*)</text>", svg_text)))
    return sorted(c for c in chars if c.strip() and ord(c) not in cmap)


def main():
    check_only = "--check" in sys.argv
    cmap = font_cmap(RENDER_FONT)
    OUT.mkdir(parents=True, exist_ok=True)

    svgs = sorted(SRC.glob("*.svg"))
    if not svgs:
        sys.exit(f"[ERROR] {SRC} に SVG がありません。")

    failed = []
    for svg in svgs:
        text = svg.read_text(encoding="utf-8")

        missing = check_glyphs(text, cmap, svg.name)
        if missing:
            failed.append((svg.name, missing))
            print(f"[NG] {svg.name} 未収録文字: "
                  + ", ".join(f"{c!r}(U+{ord(c):04X})" for c in missing))
            continue
        print(f"[OK] {svg.name} 欠字なし")

        if check_only:
            continue

        m = re.search(r'viewBox="0 0 ([\d.]+) ([\d.]+)"', text)
        if not m:
            sys.exit(f"[ERROR] {svg.name} に viewBox がありません。")
        w, h = float(m.group(1)), float(m.group(2))

        rendered = re.sub(r'font-family="[^"]*"', f'font-family="{RENDER_FONT}"', text)
        dest = OUT / f"{svg.stem}@{SCALE}x.png"
        cairosvg.svg2png(bytestring=rendered.encode(), write_to=str(dest),
                         output_width=int(w * SCALE), output_height=int(h * SCALE))
        print(f"     -> {dest.relative_to(ROOT)} ({int(w*SCALE)}x{int(h*SCALE)})")

    if failed:
        sys.exit(f"\n[FAILED] {len(failed)} 件に未収録文字があります。"
                 f" 記号は <path>/<circle> で描画してください。")
    print("\n全て正常に完了しました。")


if __name__ == "__main__":
    main()
