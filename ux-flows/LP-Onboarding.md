---
id: lp-onboarding
type: flow
name: LP Onboarding
tags: [onboarding, suitability, finance, profile]
last_updated: 2026-08-07
---

# LP Onboarding

## Goal

In ~3 minutes, a novice LP gets a usable investment profile, a confirmed risk band, and a first shortlist of 3 funds — without reading a single form.

## Entry Points

- Landing page "回答 6 个问题，3 分钟后看到你的第一份精选" 
- Referral from a friend's shareable recap
- Deep link from educational content

## Steps

1. **欢迎** — 一句话定位："我们不卖基金，我们帮你选。" 建立信任预期（来源可查、风险线）。
2. **6 个白话问题** — 目标（攒钱/退休/增长）、期限、最大可承受回撤（用情境而非术语："跌 20% 你能睡着吗"）、知识水平、计划金额、已有经验。
3. **AI 生成画像 + 风险带确认** — 显示"你的范围：30–60% 增长资产"，可调整；歧义时取保守侧（[Suitability Matching](../patterns/Suitability-Matching.md)）。
4. **首份精选（3 只）** — 每只一张"为什么适合你"卡片（[Curated Shortlist](../features/Curated-Shortlist.md)）。
5. **引导** — 打开第一张 [Fund Passport](../features/Fund-Passport.md)，而不是直接引导入金。

## Decision Points & Failure Paths

- 用户答"不知道" → 给情境示例 + 默认建议（选默认 = 保守侧）
- 用户想跳过问题 → 允许，但画像标记"未校准"，风险带默认最保守，首月后校准
- 用户第一次见亏损（显性画像冲突）→ 触发画像重校准而非锁死
- 合规卡点（年龄/身份/地区）→ 透明说明，不硬绕

## Success Criteria

画像完成 + 风险带确认 + 打开至少 1 张 Passport（不是完成入金——入金发生在理解之后）。

## Metrics

完成率（进入→拿到首份精选）、画像-行为一致性（30 天后画像 vs 实际行为）、首份精选点击率、合规拦截率。

