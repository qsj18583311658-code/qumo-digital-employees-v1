# 趣摩数字员工 v1.2

趣摩数字员工是一个面向内容整合营销公司的 Codex Skill。它将 Codex 的 subagent 能力包装成一套广告公司式的数字员工协作流程，用固定岗位完成复盘报告、数据分析、PPT 汇报、文案修改和办公协同工具接入引导。

## 核心能力

- 固定岗位协作：项目总监、策略总监、数据分析师、内容策划、创意总监、投放/电商运营、客户经理、PPT/报告设计师、短视频编导。
- 多数字员工流程：决策者摘要、本轮协作阵容、岗位判断、交叉质询、共识结论、最终交付物、下一步行动清单。
- 行业参考：美妆内容电商、活动复盘、抖音/千川、自播复盘、小红书文案。
- 交付格式优先：Word、Excel、PPT、PDF；Markdown 只作为预览或草稿。
- 办公工具指引：飞书/Lark、钉钉、腾讯文档、企业微信/WeCom、腾讯云 CLI 的安装和使用边界说明。

## 目录结构

```text
qumo-digital-employees-v1/
├── SKILL.md
├── agents/
│   └── openai.yaml
└── references/
    ├── agency-roles.md
    ├── workflows.md
    ├── output-templates.md
    ├── roles/
    ├── domain/
    ├── deliverables/
    └── integrations/
```

## 安装方法

将 skill 目录复制到 Codex skills 目录：

```bash
mkdir -p ~/.codex/skills
cp -R qumo-digital-employees-v1 ~/.codex/skills/
```

安装后重启 Codex，让 skill 重新加载。

## 使用方法

显式调用：

```text
Use $qumo-digital-employees-v1 帮我做一个618美妆品牌复盘，并生成 Word 报告结构。
```

自然语言触发：

```text
用趣摩数字员工分析这份千川数据，整理成 Excel 分析表。
```

```text
让趣摩数字员工一起修改这条小红书文案，输出 docx 前后对比结构。
```

## 设计原则

- 不给数字员工起个人名，只使用固定岗位。
- Codex subagent 的随机 UI 昵称只作为工具句柄，不作为产品身份。
- 不使用夸张出勤表，保留轻量协作感。
- 不编造平台数据；缺失指标统一标记为 `待补数据`。
- 文件交付优先于聊天长文。

## 办公工具集成

`references/integrations/office-cli-guide.md` 收录了常用办公工具 CLI 的安装和使用指引：

- Lark/Feishu: `lark-cli`
- DingTalk: `dws`
- Tencent Docs: `qqdocs`（社区工具）
- WeCom: `wecom-cli`
- Tencent Cloud: `tccli`

该 skill 只提供引导，不会自动安装、登录、上传文件、发送消息或修改权限。涉及外部账号、OAuth、token、企业权限时，需要用户明确授权。

## 许可

暂未声明开源许可证。公开仓库默认仅供查看和参考，复用前请自行补充许可证。
