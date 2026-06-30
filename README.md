# 趣摩数字员工

趣摩数字员工是一个面向美妆时尚内容电商团队的 Codex 插件。它把广告公司常见岗位组织成一套固定的数字员工协作机制，用来做复盘报告、数据分析、PPT 汇报、小红书图文卡片和文案优化。

它不是单纯追求“多 agent 表演”，而是让策略、数据、内容、创意、投放、客户和报告设计这些岗位各自承担明确判断，最后由项目总监统一收口成可交付的业务文件。

## 核心能力

- 9 个固定岗位：项目总监、策略总监、数据分析师、内容策划、创意总监、投放/电商运营、客户经理、PPT/报告设计师、短视频编导
- 复盘报告：大促、月度、结案、品牌账号、自播和平台活动复盘
- 数据分析：千川、抖音、自播、内容矩阵、素材矩阵和行动清单
- 文件交付：优先生成或规划 `.docx`、`.xlsx`、`.pptx`、`.pdf`
- 内置 PPTX 生成器：从结构化 JSON 生成基础可编辑 PPT
- 内置小红书图文生成器：生成 1080x1440 图文卡片和 contact sheet
- 办公协同引导：飞书、钉钉、腾讯文档、企业微信等 CLI 接入说明

## 插件安装

当前仓库已经是 Codex 插件结构，适合通过插件方式分享和安装。

本地安装：

```bash
mkdir -p ~/plugins
git clone https://github.com/qsj18583311658-code/qumo-digital-employees-v1.git ~/plugins/qumo-digital-employees
mkdir -p ~/.agents/plugins
python3 - <<'PY'
import json
from pathlib import Path

path = Path.home() / ".agents/plugins/marketplace.json"
data = {
    "name": "personal",
    "interface": {"displayName": "Personal"},
    "plugins": []
}
if path.exists():
    data = json.loads(path.read_text(encoding="utf-8"))

plugins = [p for p in data.get("plugins", []) if p.get("name") != "qumo-digital-employees"]
plugins.append({
    "name": "qumo-digital-employees",
    "source": {"source": "local", "path": "./plugins/qumo-digital-employees"},
    "policy": {"installation": "AVAILABLE", "authentication": "ON_INSTALL"},
    "category": "Productivity"
})
data["plugins"] = plugins
path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
PY
codex plugin add qumo-digital-employees@personal
```

安装后新开一个 Codex 线程使用。

如果你已经从 Codex 插件页拿到了分享链接，也可以直接通过分享链接安装，不需要手动编辑 marketplace。

## Skill 兼容安装

如果暂时不使用插件，也可以只安装内部 skill：

```bash
python3 ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo qsj18583311658-code/qumo-digital-employees-v1 \
  --path skills/qumo-digital-employees-v1
```

安装后重启 Codex。

## 使用示例

```text
用趣摩数字员工做一个 618 美妆品牌复盘，并生成 Word 报告结构。
```

```text
用趣摩数字员工分析这份千川数据，整理成 Excel 分析表。
```

```text
把这个复盘整理成 PPT。
```

```text
生成一套小红书图文卡片，主题是夏季底妆不闷。
```

```text
让趣摩数字员工一起修改这条小红书文案，输出 docx 前后对比结构。
```

## 工作方式

每次任务会从 9 个固定岗位中选择 5-7 个参与协作。岗位不会使用随机人名；即使 Codex 侧边栏中的 subagent 显示为随机英文昵称，最终输出也统一使用固定职位。

默认输出结构是：

- 决策者摘要
- 本轮协作阵容
- 各岗位第一轮判断
- 交叉质询/分歧点
- 共识结论
- 最终交付物/文件说明
- 下一步行动清单

## 内置脚本

插件内置两个本地脚本，不依赖用户访问 GitHub：

```bash
python3 skills/qumo-digital-employees-v1/scripts/build_pptx_deck.py \
  skills/qumo-digital-employees-v1/examples/pptx-deck-example.json \
  --out output/qumo-deck.pptx
```

```bash
python3 skills/qumo-digital-employees-v1/scripts/generate_xhs_cards.py \
  skills/qumo-digital-employees-v1/examples/xhs-cards-example.json \
  --out output/xhs-cards \
  --contact-sheet
```

## 设计边界

- 不会编造 GMV、ROI、CTR、转化率等业务数据。
- 缺失数据会标记为 `待补数据`。
- 不会自动登录飞书、钉钉、腾讯文档或企业微信。
- 不会自动上传文件、发送消息或修改权限。
- 第三方 GitHub skill 只作为参考，不会默认安装或执行。

## License

MIT
