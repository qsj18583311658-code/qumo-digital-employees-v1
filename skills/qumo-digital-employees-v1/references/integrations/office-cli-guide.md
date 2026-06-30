# Office CLI Integration Guide

Use this file when the user wants to install, configure, or use Feishu/Lark, DingTalk, Tencent Docs, WeCom, or Tencent Cloud CLIs for uploading, sharing, editing, or handing off deliverables.

Sources checked on 2026-06-22:
- Lark/Feishu official CLI: https://github.com/larksuite/cli
- DingTalk official Workspace CLI: https://github.com/DingTalk-Real-AI/dingtalk-workspace-cli
- Tencent Docs community CLI: https://github.com/snomiao/qqdocs
- WeCom official CLI: https://github.com/WecomTeam/wecom-cli
- Tencent Cloud CLI: https://github.com/TencentCloud/tencentcloud-cli

## Safety Rules
- Do not install a CLI, start OAuth, upload files, send messages, or change permissions without explicit user intent.
- Explain which identity will be authorized: personal user, bot, workspace app, enterprise app, or cloud key.
- Use dry-run or status commands first when available.
- Never paste secrets into chat. Use environment variables, keychain, config prompts, or browser/device authorization flows.
- Prefer official tools. Mark `qqdocs` as community-maintained and ask the user to confirm before installing it.

## Tool Selection
| Need | Preferred tool | Notes |
|---|---|---|
| Feishu/Lark Docs, Sheets, Slides, Drive, Base, IM, Calendar | `lark-cli` | Official. Already installed on this machine at `/Users/qumo/.npm-global/bin/lark-cli` when last checked. |
| DingTalk docs, AI tables, calendar, chat, contacts, approvals | `dws` | Official DingTalk Workspace CLI. Needs enterprise/admin authorization for many actions. |
| Tencent Docs `docs.qq.com` personal/cloud docs | `qqdocs` | Community CLI. Good for docs.qq.com import/read/search when the user accepts the dependency. |
| Enterprise WeChat docs and smart sheets | `wecom-cli` | Official WeCom CLI. Prefer this when the user's Tencent docs are inside 企业微信/WeCom workflows. |
| Tencent Cloud resources | `tccli` | Official Tencent Cloud CLI; not a Tencent Docs editor. Use only for cloud APIs/resources. |

## Feishu/Lark: `lark-cli`
Best for:
- Uploading generated `.docx`, `.xlsx`, `.pptx`, `.pdf` to Drive.
- Creating or editing Docs, Sheets, Slides, Markdown, Base, Wiki.
- Sending deliverables through IM or finding calendar/context records.

Install:
```bash
npx @larksuite/cli@latest install
```

Configure:
```bash
lark-cli config init --new
lark-cli auth login --recommend
lark-cli auth status
```

Useful checks:
```bash
command -v lark-cli
lark-cli auth status
lark-cli --help
```

Agent rules:
- Use `--dry-run` for side-effectful IM commands when available.
- Use `lark-cli auth check` when a scope may be missing.
- For generated deliverables, prefer Drive upload or the specialized Lark skill already available in the Codex environment when it is more precise.

## DingTalk: `dws`
Best for:
- DingTalk workspace tasks involving docs, AI tables, calendar, chat, contacts, approvals, and agent-facing workflows.

Install on macOS/Linux:
```bash
curl -fsSL https://raw.githubusercontent.com/DingTalk-Real-AI/dingtalk-workspace-cli/main/scripts/install.sh | sh
```

Install on Windows PowerShell:
```powershell
irm https://raw.githubusercontent.com/DingTalk-Real-AI/dingtalk-workspace-cli/main/scripts/install.ps1 | iex
```

Alternative npm install:
```bash
npm install -g dingtalk-workspace-cli
```

Useful checks:
```bash
command -v dws
dws --help
dws upgrade --check
```

Agent rules:
- Prefer mono skill mode for shared or production environments.
- Explain that DingTalk enterprise data access requires enterprise/admin authorization.
- Use `--dry-run` where available before write operations.

## Tencent Docs: `qqdocs` Community CLI
Best for:
- Direct `docs.qq.com` recent document listing, search, read, import, permission management, and space operations.

Important:
- This is community-maintained, not an official Tencent Docs CLI.
- It requires Bun >= 1.x and a Tencent Docs token from docs.qq.com MCP settings.

Run without global install:
```bash
bunx qqdocs ls
```

Install:
```bash
bun add -g qqdocs
```

Auth:
```bash
export TENCENT_DOCS_TOKEN=...
qqdocs ls --json
```

Common operations:
```bash
qqdocs search <query> --json
qqdocs read <file_id_or_url>
qqdocs import ./report.docx --title "复盘报告"
qqdocs perm get <file_id_or_url>
```

Agent rules:
- Confirm the user accepts a community CLI before installing.
- Do not request or expose `TENCENT_DOCS_TOKEN` in chat.
- Use `qqdocs tools` to inspect the live MCP surface because Tencent Docs capabilities may change.

## Enterprise WeChat / WeCom: `wecom-cli`
Best for:
- 企业微信 messages, docs, smart sheets, contacts, todos, meetings, and schedules.
- Tencent-side document workflows inside WeCom rather than direct docs.qq.com personal docs.

Install:
```bash
npm install -g @wecom/cli
npx skills add WeComTeam/wecom-cli -y -g
```

Configure:
```bash
wecom-cli init
wecom-cli contact get_userlist '{}'
```

Agent rules:
- Use this when the user's Tencent document workflow is actually 企业微信文档 or 智能表格.
- Explain whether access uses an enterprise account, bot, or app credentials.

## Tencent Cloud: `tccli`
Best for:
- Tencent Cloud resource APIs, not collaborative Tencent Docs editing.

Install in China/common Tencent Cloud repo:
```bash
pip install tccli
```

Install international variant:
```bash
sudo pip install tccli-intl-en
```

Configure:
```bash
tccli configure
tccli --version
```

Agent rules:
- Do not confuse `tccli` with Tencent Docs or WeCom document operations.
- Never ask the user to paste SecretId/SecretKey into chat.
- Prefer environment variables or interactive configuration.

## Integration Workflow
1. Identify platform: Feishu/Lark, DingTalk, Tencent Docs, WeCom, or Tencent Cloud.
2. Check existing CLI with `command -v <tool>`.
3. If missing, show the install command and ask for explicit installation intent.
4. After install, run a status/help command.
5. Start auth only after the user confirms identity and scope.
6. For generated deliverables, create the local file first, then upload/share with the chosen platform tool.
7. Report final local file path and online link or document ID if upload succeeds.
