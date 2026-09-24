---
title: Vercel Labs
type: entity
domain: ai-news
tags: [ai-news, 조직, vercel, rust, npm]
created: 2026-09-24
updated: 2026-09-24
sources: [agent-browser.md]
reliability: high
---

# Vercel Labs

[[agent-browser]](★43,140 · Rust · Apache-2.0) 제작. Vercel의 실험 제품 조직으로, README에 **`LABS-PRODUCT` 공식 배지**를 달고 vercel.com/labs#labs-products 로 링크한다(볼트 실측).

> [!insight] 🎯 볼트 GitHub 소스 중 **npm 실채택 수치가 가장 큰 조직**
> [[agent-browser]] npm 월 다운로드 **5,326,951**(2026-08-23~09-21 실측) · 버전 **127개** · latest `0.38.1`.
> 🔴 **그런데 ★ 당일 증분은 +62로 둔화 중이다.** 볼트가 그동안 *"스타는 활성도가 아니다"*([[TradingAgents]]·[[mattpocock-skills]])를 기록해 왔는데, 이 조직은 **그 반대 방향의 가장 강한 사례**를 제공한다 — **★가 포화한 뒤에도 설치는 월 500만대로 계속된다.** ★ 증분 둔화를 쇠퇴로 읽으면 틀린다 → [[상대속도-가림]]

## 확인된 것
- 공식 Vercel Labs 제품(배지·링크 실측) · Apache-2.0(배지·API·npm 3중 일치)
- **5플랫폼 전부 네이티브 Rust** 바이너리 배포(macOS ARM64/x64 · Linux ARM64/x64 · Windows x64)
- 배포 경로 4종: npm 글로벌/로컬 · Homebrew · cargo
- `skills.sh/vercel-labs/agent-browser` 배지 보유 — **스킬 배급 채널에 편입돼 있다** → [[에이전트-스킬]]
- 🔴 open issues **813건 = ★ 대비 1.9%** — 같은 배치 최고 비율

## ⬜ 미확인
- Vercel 본사와 Labs의 조직 관계(독립 팀인지 브랜딩인지) 미확인.
- 다른 Labs 레포 보유 목록 미조회.
- 월 532만 DL 중 CI 재설치·미러 비중 분리 불가.

## 관련 페이지
- [[agent-browser]] — 확인된 산출물
- [[상대속도-가림]] — ★ 둔화 vs npm 532만
- [[에이전트-스킬]] · [[에이전트-웹접근]]
- [[ai-news]]
