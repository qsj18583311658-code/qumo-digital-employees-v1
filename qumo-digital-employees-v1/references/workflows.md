# Workflows

Use this file to choose the minimum necessary role cards, domain references, and deliverable references. Avoid loading unrelated files.

## Task Classification
- `复盘报告`: campaign, monthly/weekly review, closing report, brand account review, livestream review, platform performance summary.
- `数据分析`: tables, platform metrics, spend, GMV, ROI, CTR, CPM, CPE, conversion, audience, content ranking, traffic source.
- `PPT生成`: deck, slides, presentation, decision-maker report, client report, page outline.
- `文案修改`: copy, title, hook, Xiaohongshu note, Douyin caption, script line, ecommerce selling point.
- `图文生成`: Xiaohongshu/Rednote image cards, carousel cards, cover images, posters, social cards, image-heavy PPT pages, visual asset generation.

## Role Count Rules
- Use 5 roles for narrow copy edits or simple data interpretation.
- Use 6 roles for ordinary retrospectives, analysis memos, and PPT outlines.
- Use 7 roles for decision-maker/client-facing reports, major reviews, full PPT generation, or ambiguous high-stakes requests.
- Always include `项目总监` as the main thread.
- Keep fixed job titles; do not assign personal names.

## Reference Loading Map
| Task | Role cards | Domain references | Deliverable references |
|---|---|---|---|
| 复盘报告 | project-director, strategy-director, data-analyst, content-planner, performance-operator, account-manager, deck-report-designer | campaign-retrospective, beauty-content-commerce, douyin-qianchuan, livestream-review when relevant | docx-report, pdf-final when final export is needed |
| 数据分析 | project-director, data-analyst, performance-operator, strategy-director, content-planner, account-manager | douyin-qianchuan, beauty-content-commerce, campaign-retrospective when reviewing activity results | xlsx-analysis |
| PPT生成 | project-director, strategy-director, deck-report-designer, data-analyst, creative-director, account-manager | campaign-retrospective, beauty-content-commerce | pptx-structure, pdf-final when share version is needed |
| 文案修改 | project-director, creative-director, content-planner, performance-operator, account-manager, strategy-director | xiaohongshu-copy, beauty-content-commerce, douyin-qianchuan when platform sales copy is involved | docx-report when comparing versions |
| 短视频脚本 | project-director, short-video-director, content-planner, creative-director, performance-operator, account-manager | beauty-content-commerce, douyin-qianchuan, xiaohongshu-copy when relevant | docx-report |
| 图文生成 | project-director, content-planner, creative-director, deck-report-designer, account-manager, strategy-director | xiaohongshu-copy, beauty-content-commerce | xhs-image-cards, pptx-structure when image-heavy slides are requested |

## Integration Loading Rule
- If the user asks for PPT visual enhancement, editable PPT, image-heavy PPT, image-to-editable PPT, Xiaohongshu/Rednote image cards, covers, carousel images, poster images, or GitHub visual skills, read `references/integrations/github-visual-skills.md`.
- If the user asks to install, configure, upload to, share through, sync with, or operate Feishu/Lark, DingTalk, Tencent Docs, WeCom, or Tencent Cloud, read `references/integrations/office-cli-guide.md`.
- If the user only asks to create a local `.docx`, `.xlsx`, `.pptx`, or `.pdf`, do not load integration references.
- If authentication or credential setup is required, pause for explicit user action unless the user has already authorized the setup.

## Collaboration Flow
1. `项目总监` states the task, known inputs, missing inputs, selected roles, and target file format.
2. Each role gives one concise first-round judgment based on its role card.
3. Project Director asks 2-4 cross-role challenges. Keep them useful, not theatrical.
4. Project Director writes the consensus conclusion.
5. Produce the final deliverable or a file-ready structure according to `references/deliverables/`.
6. If data is missing, produce a qualitative version and mark `待补数据` inside the deliverable.

## Delivery Format Rules
- If the user asks for `报告`, `复盘`, `结案`, `说明`, or `客户/汇报对象可读版本`, produce or offer `.docx`; export `.pdf` when a final read-only version is needed.
- If the user asks for `数据分析`, `看板`, `表格`, `数据拆解`, `行动清单`, `达人矩阵`, `素材矩阵`, or `排期`, produce or offer `.xlsx`.
- If the user asks for `PPT`, `汇报`, `deck`, `slides`, or `演示`, produce or offer `.pptx`.
- If the user asks for `文案修改`, produce `.docx` when there are multiple versions, comments, or before/after comparisons; in-chat output is acceptable for short single-copy tasks.
- If the user asks for `小红书图文`, `图文卡片`, `封面`, `轮播图`, `海报`, `社媒卡片`, or `Rednote cards`, produce or offer `.png/.jpg` assets plus a `.docx` or `.md` source draft when useful.
- Markdown is only a preview or working draft. Do not make `.md` the main artifact unless the user explicitly requests Markdown.
- When producing files, include a short in-chat decision-maker summary plus generated file paths.
