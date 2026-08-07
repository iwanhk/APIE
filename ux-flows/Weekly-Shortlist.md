---
id: weekly-shortlist
type: flow
name: Weekly Shortlist Review
tags: [shortlist, curation, finance, habit]
last_updated: 2026-08-07
---

# Weekly Shortlist Review

## Goal

用户每周用 ~10 分钟看完 3–5 只精选基金，做出 keep/skip 决定，带走一个明确的下一步。

## Entry Points

- 周一推送（"本周 3 只，10 分钟看完"）+ 站内固定入口
- 持仓雷达触发（持有的基金有变动时，顺带推荐本周边角）

## Steps

1. **打开清单** — 3–5 张卡片：一句话是什么 + 适合度 + 主要风险
2. **扫卡片** — 每张 30 秒内可判断是否值得深入
3. **深入** — 点开 [Fund Passport](../features/Fund-Passport.md)，随时问 AI（答案带引用）
4. **决定** — keep（进入下一步意向）/ skip（选原因：不感兴趣/太贵/风险高/已有同类）
5. **行动** — keep 后一键表达意向（经持牌通道），不 keep 则下一张
6. **收尾** — 全部看完或明确跳过；给一个下周预告

## Decision Points & Failure Paths

- 看不懂 → 卡片上"用一句话解释"按钮，AI 白话解释（带引用）
- 想比较两只 → 并排白话对比（费率/风险/经理）
- 全部 skip → 触发画像重校准 + 策展团队复盘（是清单问题还是画像问题）
- 用户连续 3 周不打开 → 降频为双周，推送改摘要（尊重注意力，不刷存在感）

## Success Criteria

完成一轮 review（看完或明确跳过全部），且至少一次产生"我理解了"的动作（提问、对比、打开 Passport 完整阅读）。

## Metrics

完成率、每轮耗时（目标 10 分钟内）、keep 率、skip 原因分布、组合多样性、清单-风险带偏差（必须为 0）。

