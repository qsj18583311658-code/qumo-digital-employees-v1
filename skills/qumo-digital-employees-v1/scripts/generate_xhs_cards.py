#!/usr/bin/env python3
"""Generate Xiaohongshu/Rednote image cards from a JSON spec."""

from __future__ import annotations

import argparse
import json
import math
import re
from pathlib import Path
from typing import Any

from PIL import Image, ImageDraw, ImageFont


CANVAS = {
    "xhs": (1080, 1440),
    "square": (1080, 1080),
}

THEMES = {
    "beauty-clean": {
        "bg": "#F8F5F1",
        "panel": "#FFFFFF",
        "ink": "#24201E",
        "muted": "#786E66",
        "accent": "#C55A6A",
        "accent2": "#2D7C72",
    },
    "editorial-dark": {
        "bg": "#171717",
        "panel": "#242424",
        "ink": "#F8F2EA",
        "muted": "#C7BEB4",
        "accent": "#E0B05F",
        "accent2": "#A9D8CE",
    },
    "fresh-lab": {
        "bg": "#F3F8F7",
        "panel": "#FFFFFF",
        "ink": "#1D2A2A",
        "muted": "#677575",
        "accent": "#2E8E84",
        "accent2": "#D7667D",
    },
}


def find_font(preferred: list[str], size: int) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    candidates = []
    for name in preferred:
        candidates.extend(
            [
                Path("/System/Library/Fonts") / name,
                Path("/Library/Fonts") / name,
                Path("/usr/share/fonts/truetype") / name,
                Path("/usr/share/fonts/opentype") / name,
            ]
        )
    candidates.extend(
        [
            Path("/System/Library/Fonts/PingFang.ttc"),
            Path("/System/Library/Fonts/STHeiti Light.ttc"),
            Path("/Library/Fonts/Arial Unicode.ttf"),
            Path("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"),
        ]
    )
    for path in candidates:
        if path.exists():
            try:
                return ImageFont.truetype(str(path), size)
            except OSError:
                continue
    return ImageFont.load_default()


def text_width(draw: ImageDraw.ImageDraw, text: str, font: ImageFont.ImageFont) -> int:
    if not text:
        return 0
    box = draw.textbbox((0, 0), text, font=font)
    return box[2] - box[0]


def wrap_text(draw: ImageDraw.ImageDraw, text: str, font: ImageFont.ImageFont, max_width: int) -> list[str]:
    lines: list[str] = []
    for para in str(text).splitlines():
        para = para.strip()
        if not para:
            lines.append("")
            continue
        current = ""
        chunks = re.findall(r"[A-Za-z0-9_./:%+-]+|\s+|.", para)
        for chunk in chunks:
            if chunk.isspace() and not current:
                continue
            trial = current + chunk
            if current and text_width(draw, trial, font) > max_width:
                lines.append(current.rstrip())
                current = chunk.lstrip()
            else:
                current = trial
        if current:
            lines.append(current.rstrip())
    return lines


def draw_wrapped(
    draw: ImageDraw.ImageDraw,
    text: str,
    xy: tuple[int, int],
    font: ImageFont.ImageFont,
    fill: str,
    max_width: int,
    line_gap: int,
    max_lines: int | None = None,
) -> int:
    x, y = xy
    lines = wrap_text(draw, text, font, max_width)
    if max_lines is not None and len(lines) > max_lines:
        lines = lines[:max_lines]
        lines[-1] = lines[-1].rstrip("。,.，") + "..."
    ascent, descent = font.getmetrics() if hasattr(font, "getmetrics") else (font.size, 0)
    line_height = ascent + descent + line_gap
    for line in lines:
        draw.text((x, y), line, font=font, fill=fill)
        y += line_height
    return y


def normalize_cards(spec: dict[str, Any]) -> list[dict[str, Any]]:
    cards = spec.get("cards") or spec.get("pages") or []
    if not cards:
        cards = [
            {
                "title": spec.get("title", "小红书图文标题"),
                "subtitle": spec.get("subtitle", ""),
                "body": spec.get("body", "请在 JSON 中提供 cards 数组。"),
            }
        ]
    normalized = []
    for i, card in enumerate(cards, 1):
        body = card.get("body", "")
        if isinstance(body, list):
            body = "\n".join(f"• {item}" for item in body)
        normalized.append(
            {
                "title": card.get("title") or f"第 {i} 页",
                "subtitle": card.get("subtitle") or "",
                "body": body,
                "footer": card.get("footer") or spec.get("footer") or "趣摩数字员工",
                "visual_prompt": card.get("visual_prompt") or card.get("image_prompt") or "",
            }
        )
    return normalized


def draw_card(card: dict[str, Any], index: int, total: int, spec: dict[str, Any], out_path: Path) -> None:
    size = CANVAS.get(spec.get("canvas", "xhs"), CANVAS["xhs"])
    theme = THEMES.get(spec.get("theme", "beauty-clean"), THEMES["beauty-clean"])
    w, h = size
    img = Image.new("RGB", size, theme["bg"])
    draw = ImageDraw.Draw(img)

    title_font = find_font(["PingFang.ttc", "Arial Unicode.ttf"], 74 if h > 1200 else 58)
    subtitle_font = find_font(["PingFang.ttc", "Arial Unicode.ttf"], 38 if h > 1200 else 32)
    body_font = find_font(["PingFang.ttc", "Arial Unicode.ttf"], 42 if h > 1200 else 34)
    small_font = find_font(["PingFang.ttc", "Arial Unicode.ttf"], 28)
    mark_font = find_font(["PingFang.ttc", "Arial Unicode.ttf"], 26)

    margin = int(w * 0.075)
    top = int(h * 0.075)
    bottom = h - int(h * 0.075)

    # Accent blocks.
    draw.rounded_rectangle((margin, top, w - margin, bottom), radius=36, fill=theme["panel"])
    draw.rectangle((margin, top, margin + 18, bottom), fill=theme["accent"])
    draw.ellipse((w - margin - 180, top + 40, w - margin - 40, top + 180), fill=theme["accent2"])

    y = top + 78
    y = draw_wrapped(draw, card["title"], (margin + 54, y), title_font, theme["ink"], w - margin * 2 - 140, 14, 3)
    if card["subtitle"]:
        y += 18
        y = draw_wrapped(draw, card["subtitle"], (margin + 56, y), subtitle_font, theme["accent"], w - margin * 2 - 112, 10, 2)

    y += 44
    divider_y = y
    draw.line((margin + 56, divider_y, w - margin - 56, divider_y), fill=theme["accent"], width=3)
    y += 48
    max_body_height = bottom - y - 168
    max_lines = max(4, math.floor(max_body_height / 62))
    y = draw_wrapped(draw, card["body"], (margin + 56, y), body_font, theme["ink"], w - margin * 2 - 112, 18, max_lines)

    prompt = card.get("visual_prompt", "")
    if prompt:
        prompt_box_top = bottom - 190
        draw.rounded_rectangle((margin + 56, prompt_box_top, w - margin - 56, bottom - 78), radius=22, fill=theme["bg"])
        draw.text((margin + 84, prompt_box_top + 24), "画面提示", font=small_font, fill=theme["accent"])
        draw_wrapped(draw, prompt, (margin + 84, prompt_box_top + 64), small_font, theme["muted"], w - margin * 2 - 168, 8, 2)

    draw.text((margin + 56, bottom - 46), card["footer"], font=mark_font, fill=theme["muted"])
    page = f"{index:02d}/{total:02d}"
    page_w = text_width(draw, page, mark_font)
    draw.text((w - margin - 56 - page_w, bottom - 46), page, font=mark_font, fill=theme["muted"])

    img.save(out_path, quality=95)


def write_contact_sheet(paths: list[Path], out_path: Path) -> None:
    thumbs = []
    for path in paths:
        img = Image.open(path).convert("RGB")
        img.thumbnail((270, 360))
        thumbs.append(img.copy())
    if not thumbs:
        return
    cols = min(4, len(thumbs))
    rows = math.ceil(len(thumbs) / cols)
    sheet = Image.new("RGB", (cols * 310 + 40, rows * 410 + 40), "#F2F2F2")
    for i, thumb in enumerate(thumbs):
        x = 40 + (i % cols) * 310
        y = 40 + (i // cols) * 410
        sheet.paste(thumb, (x, y))
    sheet.save(out_path, quality=92)


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate Xiaohongshu/Rednote PNG cards from JSON.")
    parser.add_argument("spec", type=Path, help="JSON spec path")
    parser.add_argument("--out", type=Path, default=Path("xhs_cards"), help="output directory")
    parser.add_argument("--contact-sheet", action="store_true", help="also create a preview contact sheet")
    args = parser.parse_args()

    spec = json.loads(args.spec.read_text(encoding="utf-8"))
    cards = normalize_cards(spec)
    args.out.mkdir(parents=True, exist_ok=True)
    generated = []
    for i, card in enumerate(cards, 1):
        safe_title = re.sub(r"[^A-Za-z0-9\u4e00-\u9fff_-]+", "-", card["title"]).strip("-")[:28]
        out_path = args.out / f"{i:02d}-{safe_title or 'card'}.png"
        draw_card(card, i, len(cards), spec, out_path)
        generated.append(out_path)

    if args.contact_sheet:
        write_contact_sheet(generated, args.out / "contact-sheet.jpg")

    print(json.dumps({"generated": [str(p) for p in generated]}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
