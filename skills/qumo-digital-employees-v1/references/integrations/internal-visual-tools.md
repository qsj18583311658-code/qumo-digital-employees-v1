# Internal Visual Tools

Use this file when the user needs local PPTX generation, Xiaohongshu/Rednote image cards, covers, carousel images, social cards, or a no-GitHub visual workflow.

## Why Internalized
- Users may not have GitHub access.
- Third-party skills may change, disappear, or require extra dependencies.
- 趣摩数字员工 should own the visible workflow: strategy, content, creative direction, layout QA, and client-safe wording.

## Bundled Tools

### `scripts/generate_xhs_cards.py`
Generates Xiaohongshu/Rednote PNG cards from a JSON spec.

Use for:
- 小红书图文
- 轮播图
- 封面图
- 社媒卡片
- beauty/fashion visual notes

Command:

```bash
python3 scripts/generate_xhs_cards.py examples/xhs-cards-example.json --out output/xhs-cards --contact-sheet
```

Input fields:
- `theme`: `beauty-clean`, `editorial-dark`, or `fresh-lab`.
- `canvas`: `xhs` for 1080x1440 or `square` for 1080x1080.
- `footer`: brand/account footer.
- `cards`: array of pages with `title`, `subtitle`, `body`, `visual_prompt`, and optional page-level `footer`.

Output:
- Numbered `.png` cards.
- Optional `contact-sheet.jpg` for quick review.

### `scripts/build_pptx_deck.py`
Generates a simple editable `.pptx` from a JSON spec.

Use for:
- 快速汇报 PPT
- 复盘结构转 PPT
- 会议版 deck 草稿
- data-light decision-maker presentations

Command:

```bash
python3 scripts/build_pptx_deck.py examples/pptx-deck-example.json --out output/qumo-deck.pptx
```

Input fields:
- `theme`: `qumo-clean` or `editorial-dark`.
- `title`, `subtitle`: deck-level defaults.
- `slides`: array of pages.
- Supported slide types: `cover`, `summary`, `metrics`, `two-column`, `actions`.

Output:
- Editable `.pptx` with text boxes, metric cards, tables, and action pages.

## Workflow
1. `项目总监` classifies the request and decides whether local visual generation is enough.
2. `策略总监` writes the storyline or card purpose.
3. `内容策划` writes page/card copy.
4. `创意总监` sets theme, visual prompt, and tone.
5. `PPT/报告设计师` converts the structure into JSON and runs the bundled script.
6. `客户经理` checks claims and client-facing wording before final export.

## When Not Enough
- Use Codex presentations or a stronger external PPT skill when the deck needs complex charts, master templates, animations, or brand theme preservation.
- Use image generation/editing when the cards need actual product photography, AI-generated backgrounds, or image retouching.
- Use `references/integrations/github-visual-skills.md` only when the user explicitly wants to install or compare external GitHub skills.
