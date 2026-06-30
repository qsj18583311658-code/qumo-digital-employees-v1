# GitHub Visual Skill Integration Guide

Use this file when a task asks for PPT visual generation, editable PPT, image-heavy decks, image-to-PPT reconstruction, Xiaohongshu/Rednote image cards, covers, posters, carousel cards, or GitHub skill integration.

## Integration Policy
- Do not vendor third-party code into this skill by default. GitHub projects change quickly and may bring dependency, license, account, or security issues.
- Use external projects as patterns first: workflow shape, deliverable structure, QA checks, visual modes, and install candidates.
- Clone, install, run, authenticate, or publish through external tools only after the user explicitly asks.
- Prefer Codex built-in presentations/slides and image generation capabilities when available. Use GitHub skills for specialized workflows or when the user explicitly wants them installed.
- Keep 趣摩数字员工 as the orchestrator: fixed roles still own strategy, content, creative direction, layout QA, and client-safe wording.

## PPT Skill Patterns From GitHub

### Editable PPTX First
Use when the output must be revised by a team or client after delivery.

- Pattern: source outline -> PowerPoint-native text/shapes/charts -> render/QA -> final `.pptx`.
- Good for:复盘报告, client decks, board-style updates, regular templates.
- Reference: `siril9/presentation-skill` emphasizes treating decks like source-controlled artifacts with an outline, build script, and validation loop.
- Reference: OpenAI's slide-deck workflow recommends keeping slide text and simple charts editable where practical.

### Image-Heavy Deck
Use when visual impact is more important than editability.

- Pattern: brief -> storyline -> visual system -> per-slide image prompt -> full-page image -> QA -> PDF/PPT packaging.
- Good for: mood boards, campaign concepts, high-impact covers, creative previews.
- Risk: text and charts may be rasterized; future edits are harder.
- Reference: `ningzimu/codex-ppt-skill` and `qybaihe/codex-ppt` both use staged image-first deck production.

### Image-To-Editable PPT
Use when the user has screenshots, PDF slides, or image-based PPT and wants editable output.

- Pattern: render/source image -> detect text/layout -> rebuild text boxes and visual layers -> merge into `.pptx`.
- Good for: converting client screenshots, old image decks, generated visual decks, or PDF slide references.
- Reference: `ningzimu/image-to-editable-ppt-skill` is a Codex skill for converting slide images, PDFs, and image-based decks into editable PowerPoint.

### Template-Based PPT Editing
Use when the user supplies a brand template or previous deck.

- Pattern: inspect existing deck -> preserve aspect ratio, theme, fonts, and master style -> edit or add slides -> render QA.
- Good for: brand-safe decks and recurring client report formats.
- Reference: MiniMax `pptx-generator` documents PowerPoint reading/editing, PptxGenJS creation, slide types, design system, and common pitfalls.

## Xiaohongshu / Rednote Visual Skill Patterns

### Card Carousel Workflow
Use when the user asks for a full 小红书图文组图.

- Pattern: note topic -> page split -> cover + body cards -> visual system -> HTML/Canvas render -> PNG batch export.
- Good for: beauty product notes, campaign tips, tutorial cards, content repurposing.
- Reference: `op7418/guizang-social-card-skill` supports Xiaohongshu/Rednote carousels, WeChat cover pairs, 1080x1440 cards, layout systems, themes, and image-source workflows.

### Note Copy + Card Rendering Pipeline
Use when the task should go from written note to rendered images.

- Pattern: copy draft -> card Markdown -> themed cover/body images -> optional publishing flow.
- Good for: repeatable creator workflows and reusable style packs.
- Reference: `cnfjlhj/xhs-note-creator` separates note copy, card Markdown, cover/body rendering, style docs, assets, and scripts.

### Markdown-To-Image Local Tool
Use when the source is already Markdown or the user wants privacy-friendly local rendering.

- Pattern: Markdown -> theme selection -> live preview -> auto pagination -> batch export.
- Good for: knowledge cards, listicles, checklist posts, internal review before posting.
- Reference: `simonwong/redbook-text2img` describes Markdown support, themes, live preview, batch export, and local processing.

### Cover Generator
Use when the user only needs a cover or wants stable visual templates.

- Pattern: long content -> cover layout -> text pagination -> reusable visual templates -> bulk export.
- Good for: cover A/B tests, title testing, regular account operation.
- Reference: `Fmaverick/cover-generator` focuses on fast, consistent, reusable Xiaohongshu cover workflows.

## Routing Rules
- If user says `做PPT`, `生成PPT`, `汇报deck`, or `改PPT`: load `deliverables/pptx-structure.md` and choose editable-first by default.
- If user says `更高级`, `更像设计稿`, `视觉冲击`, `封面`, or `整页图`: consider image-heavy or hybrid mode.
- If user says `可编辑`, `后续还要改`, `客户要改字`, or `模板`: choose editable-first or image-to-editable mode.
- If user says `小红书图文`, `图文卡片`, `轮播图`, `封面`, `海报`, or `Rednote`: load `deliverables/xhs-image-cards.md` and choose card carousel workflow.
- If user says `安装这个 GitHub skill`, ask for or confirm the exact repository before installing. Do not choose a third-party tool silently.

## Source References
- OpenAI Codex slide deck use case: https://developers.openai.com/codex/use-cases/generate-slide-decks
- siril9 presentation-skill: https://github.com/siril9/presentation-skill
- qybaihe codex-ppt: https://github.com/qybaihe/codex-ppt
- ningzimu codex-ppt-skill: https://github.com/ningzimu/codex-ppt-skill
- ningzimu image-to-editable-ppt-skill: https://github.com/ningzimu/image-to-editable-ppt-skill
- MiniMax pptx-generator skill: https://github.com/MiniMax-AI/skills/blob/main/skills/pptx-generator/SKILL.md
- Guizang social card skill: https://github.com/op7418/guizang-social-card-skill
- xhs-note-creator: https://github.com/cnfjlhj/xhs-note-creator
- redbook-text2img: https://github.com/simonwong/redbook-text2img
- cover-generator: https://github.com/Fmaverick/cover-generator
