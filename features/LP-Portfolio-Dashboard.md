---
id: lp-portfolio-dashboard
type: feature
name: LP Portfolio Dashboard
tags: [finance, dashboard, portfolio, read-only, transparency]
last_updated: 2026-08-07
---

# LP Portfolio Dashboard

## Definition

只读的投资状态看板：LP 用自己的话看懂自己投了什么、现在值多少、花了多少费用、发生了什么。平台不提供交易、不提供建议——**只读是特性，不是缺陷**。

## Core Loop

1. LP 登录（仅限已认购 PI）
2. 快照：投入、当前净值、分红、已付费用、收益（每项带口径与日期）
3. AI 白话解读："这个月为什么跌：BTC 回调，基金仓位 X"（只解释发生了什么，不回答该怎么办）
4. 事件时间线：经理变动、NAV 更新、分红、费用计提
5. 月度白话报告沉淀

## UX Flow

从 [LP Onboarding](../ux-flows/LP-Onboarding.md) 进入。关键决策：金额口径一致（会计正负号：投入为负、分红为正、净值变动对账归零）、NAV 延迟必须标注、解读不下结论。

## AI Integration

- 白话解读净值变动，只解释"发生了什么"，绝不滑向"该怎么办"
- 数据带来源（NAV 快照、基金文件）；无数据 → 明示"无来源"
- 护栏：解读越界次数必须为 0

## Metrics

月度登录率、报告打开率、复述测试（LP 能讲清自己的费用和风险）、看板与基金文件口径一致率。

## Examples

- 好机制：私行月结单 + Perplexity 式引用解读
- 反例：券商 App 把"看"和"买"放在同一屏——看板即营销位，克制感尽失

## Pitfalls

- 数据延迟不标注（NAV 滞后 = 误导）
- 从"解释变动"滑向"建议操作"（护栏红线）
- 金额口径错误（正负号、费用归属、币种）

