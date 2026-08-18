# 每日任务（每天 10:00）

这是 APIE 开源库的每日成长机制的执行手册。自动爬取与数据集重建由 GitHub Actions 在 02:00 UTC（= 北京时间 10:00）自动完成；**内容生成（拆解、模式、创新挑战）由每日任务执行者完成**——可以是人，也可以是定时运行的 AI agent。

## 每日输出

### 1. 新产品追踪（自动 + 人工）

- `crawl_hn.py` / `crawl_github.py` 已自动拉取（见 daily-pipeline workflow）
- 人工/agent：扫一眼昨日信号，把机制新、值得跟的产品记入 `datasets/Top100.json`，或直接排入拆解队列

### 2. 每日拆解（Day N）

队列（当前）：**Day 010 — Kimi Work**（已于 2026-08-18 完成；Day 009 OpenClaw 2026-08-17、Day 008 Windsurf 2026-08-16），Day 011 — TBD（候选: Gamma / Granola / Harvey / Speko）

流程：`products/_TEMPLATE.md` → 按 [Product Schema](APIE-Product-Schema-v1.md) 填 → 事实带来源和 as-of 日期 → 至少链接一个 pattern → 更新 `PRODUCTS.md` 与分类 README。

### 3. 模式挖掘

- 昨日新产品/拆解里有没有新机制 → `patterns/<Pattern>.md`（status: emerging）
- 是已有模式的变体 → 更新该模式 Examples
- 每次挖掘至少产生一个 cross-domain 候选

### 4. 创新挑战

- 随机两个产品 → 生成 20 个组合 → `examples/Innovation-Challenge-<A>-x-<B>.md`
- 规则：每个 idea 必须标注来源 pattern 组合，无出处即丢弃

### 5. 每周报告（周五）

`docs/reports/Weekly-YYYY-WW.md`：本周新模式、模式变化、值得研究的发布。

## 收尾（每天必做）

```bash
python3 scripts/build_dataset.py --quiet   # 重建 JSON
python3 scripts/build_dataset.py --validate
# 检查链接（CI 也会做）
git add -A
git commit -m "feat: Day N - <product> teardown + <pattern>"
git push
```

## 质量门

1. Schema 校验零错误
2. 每个事实有来源和 as-of 日期
3. 拆解至少链接一个 pattern；pattern 至少 2 个实例
4. **敏感内容红线（公开库）：** 任何真实商业安排、合作条款、未公开的产品计划**不得进入公开仓库**——放 `_private/`（gitignored）。发布前跑 `rg -n "FundPilot|联合GP|carry|LPF" .`
5. 提交信息用 Conventional Commits

## 在 Codex 应用里设置 10:00 定时任务

在 Codex 桌面应用创建「每天早上 10:00」的 recurring task，任务提示词：

```text
执行 APIE 开源库的每日任务（docs/DAILY-TASK.md）：
1) 检查拆解队列，完成今日 Day N 拆解（当前队列见 docs/DAILY-TASK.md）
2) 模式挖掘：从近期新产品中发现新模式并入库
3) 生成今日创新挑战（20 个组合，标注来源 pattern）
4) 周五额外生成 Weekly Pattern Report
5) 重建数据集、校验、更新索引、git commit
红线：任何真实商业安排/未公开产品计划不得进公开库（放 _private/）。
```
