# PPTX Structure Deliverables

Use `.pptx` for briefings, campaign review presentations, client reports, and decision-maker decks.

## Default Page Flow
1. Title page
2. One-page conclusion
3. Overall performance
4. Funnel or channel breakdown
5. Content/creator findings
6. Platform/ecommerce findings
7. Key problems
8. Strategy for next stage
9. Action plan
10. Data appendix

## Slide Title Rule
Use conclusion-style titles, not topic labels.

Good:
- `曝光已放大，但成交承接仍不稳定`
- `素材B更接近成交人群，应作为复刻样本`

Weak:
- `数据表现`
- `素材分析`

## Chart Suggestions
- Funnel: exposure -> click -> enter room/store -> add-to-cart -> order.
- Matrix: creator/content by exposure and conversion.
- Trend: daily spend, GMV, ROI, CVR.
- Table: action plan and owner suggestions.

## Visual Production Modes
- `Editable-first`: Use native PowerPoint text, shapes, charts, and simple SVG/image assets. Choose this for client decks, recurring reports, and slides that the team must revise.
- `Image-heavy`: Generate each slide or key visual as a full-page image, then package into PPT/PDF. Choose this for mood boards, high-impact covers, campaign visual concepts, or quick preview decks where editability is less important.
- `Hybrid`: Keep titles, labels, charts, and notes editable; use generated images only for hero visuals, backgrounds, product scenes, or illustration blocks.
- `Image-to-editable`: If a slide already exists only as screenshot/PDF/full-page image, reconstruct text boxes, shapes, and visual layers into an editable PPTX when the user needs future editing.

## Production QA
- Render or preview slides before delivery when possible.
- Check text clipping, font substitution, unreadable labels, chart legibility, and inconsistent margins.
- Keep source artifacts when possible: outline, page list, image prompts, generated images, and authoring script.
- Do not rasterize important text into images unless the user explicitly accepts lower editability.

## Bundled Generator
Use `scripts/build_pptx_deck.py` when a simple editable PPTX is enough or when the user needs a local no-GitHub workflow.

Example:

```bash
python3 scripts/build_pptx_deck.py examples/pptx-deck-example.json --out output/qumo-deck.pptx
```

Input should be a JSON deck spec with `theme`, `title`, and `slides`. Supported slide types: `cover`, `summary`, `metrics`, `two-column`, `actions`.

## Speaker Notes
Add short speaking prompts when the user asks for a presentation. Focus on what the intended reader should understand and decide.

## PDF Export
Offer `.pdf` when the deck needs to be forwarded or locked as final.

## Related Visual Skill Patterns
See `references/integrations/github-visual-skills.md` when the user asks for advanced PPT generation, image-heavy slides, editable reconstruction, or GitHub skill integration.
