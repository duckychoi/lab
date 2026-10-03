---
title: Agent-Reach
type: source
domain: ai-news
tags: [agent, tool-use, twitter, reddit, youtube, github, real-time-search, mcp]
created: 2026-06-09
updated: 2026-10-03
sources: []
reliability: high
---

# Agent-Reach

> [!update] 2026-10-03 갱신 — ★89,190 (볼트 실측) · 🔴 **18일 동결 유지**
> **볼트 독립 실측 ★89,190** ↔ 수집기 ★89,176 = **드리프트 +14**. 기존 베이스라인 ★65,181(2026-08-03) → **+24,009 / 61일 = 일평균 ≈393**.
> ✅ **전 필드 일치**: fork **7,855**(수집기 7,854 = +1) · open_issues **194**(193 = +1) · **MIT** · topics **17** · created 2026-02-24 · **pushed 2026-09-15T16:16:24Z**.
> 🆕 **볼트 신규 확인**: 주언어 **Python**(기존 볼트 페이지에 언어 미기재였다).
> 🔴 **18일 동결 확증** — `pushed` 가 2026-09-15 에 멈춰 있고 ★는 일평균 393으로 붙는다.
> 🎯 **오늘 배치가 이 관찰에 대조군을 줬다**: 같은 배치의 [[ponytail]] 은 어제까지 볼트가 *"18일 동결"* 로 적었는데 **오늘 하루에 15커밋 + 릴리스**를 냈다. **같은 "동결" 라벨이 붙은 두 레포가 하루에 갈렸다** ⇒ ⚖️ **`pushed` 동결은 유지보수 중단이 아니라 릴리스 리듬의 한 국면일 수 있다. 동결을 방치의 증거로 쓰면 안 된다** → [[지표-창길이]] · [[암묵을-명시로]].
> 🔴 **미해결 유지**: 수집기가 README 353행 중 `차단·ToS 리스크` 서술을 확인하지 못했다. **공식 API 키 불요**가 이 레포의 핵심 주장이고 동시에 **유일한 단일 장애점**인데 문서가 말하지 않는다. 볼트의 [[last30days-skill]] 파이프라인에 직결되므로 **채택 전 필독 항목**이다(오늘도 미열람 — 📌 actionable 유지).

> [!update] 2026-08-03 갱신 — ⭐65,181 (당일 +659)
> ⭐**65,181**(2026-08-03 자동수집, 당일 +659) ← 63,584(08-01). Twitter·Reddit·YouTube·GitHub 동시 소셜 검색 커넥터 레이어 지속 급성장. [[last30days-skill]]+[[Agent-Reach]] 조합 자동 트렌드 리포트 파이프라인 actionable 유지. *raw 자동수집 수치 반영 — GitHub 실WebFetch 미수행(타임라인 유지).*

> [!update] 2026-08-01 갱신 — ⭐63,584 (당일 +503, 6만 돌파)
> ⭐**63,584**(2026-08-01 자동수집, 당일 +503) ← 42,824(06-27). 약 5주 새 +약2.1만으로 소셜 검색 커넥터 레이어 지속 급성장. Twitter·Reddit·YouTube·GitHub 동시 검색 성격 동일. [[last30days-skill]]+[[Agent-Reach]] 조합 자동 트렌드 리포트 파이프라인 actionable 유지. *raw 자동수집 수치 반영 — GitHub 실WebFetch 미수행(타임라인 유지).*

## 핵심 인사이트

> [!insight] AI 에이전트에 실시간 소셜 검색 능력 부여 — 정보 수집 에이전트의 표준 레이어
> Twitter·Reddit·YouTube·GitHub 실시간 검색·읽기 능력을 AI 에이전트에 붙이는 도구. 에이전트가 최신 정보를 스스로 수집할 수 있게 해주는 인프라 레이어.

## 도메인별 추출

**핵심 기능:**
- GitHub ⭐42,824, 당일 +1,194 (2026-06-27) — 지속 급성장 (06-18 33,813 → 06-27 42,824)
- 지원 소스: Twitter(X), Reddit, YouTube, GitHub 동시 검색
- 실시간 데이터 접근 → LLM의 학습 데이터 시점 한계 극복
- [[last30days-skill]]과 함께 소셜 인텔리전스 에이전트 스택 구성 가능

**포지셔닝:**
- [[awesome-codex-skills]], [[vercel-skills]] 같은 스킬 생태계에서 데이터 수집 레이어로 활용
- [[TrendRadar]], [[worldmonitor]] 같은 트렌드 모니터링 도구와 시너지
- Claude Code 에이전트에 소셜 리서치 능력 추가하는 즉시 적용 도구

> [!action] last30days-skill + Agent-Reach 조합으로 자동 트렌드 리포트 파이프라인 구성 검토

## 관련 페이지
- [[last30days-skill]]
- [[awesome-codex-skills]]
- [[TrendRadar]]
- [[worldmonitor]]

## 원본
- 출처: https://github.com/Panniantong/Agent-Reach
- GitHub ⭐65,181 (2026-08-03 자동수집, +659/일) ← ⭐63,584 (08-01, +503) ← ⭐42,824 (06-27) ← ⭐33,813 (06-16)
- 신뢰도: ⭐⭐⭐⭐
