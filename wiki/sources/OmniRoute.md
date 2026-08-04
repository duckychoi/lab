---
title: diegosouzapw/OmniRoute — 236개 프로바이더 통합 무료 AI 게이트웨이
type: source
domain: ai-news
tags: [ai-news, github-trending, ai-gateway, routing, token-compression, mcp, typescript, cost-optimization]
created: 2026-07-01
updated: 2026-07-25
sources: []
reliability: high
---

# OmniRoute (diegosouzapw/OmniRoute)

> [!update] 2026-07-25 갱신 — ⭐29,343 + 프로바이더 290+ 확장
> ⭐**29,343**(2026-07-25, GitHub API 실측 · WebFetch "29.3k" 일치) ← ⭐22,500(07-21). 나흘 +6,843로 성장 가속, 프로바이더 **271→290+**·무료풀 **43개 ~1.53B 토큰/월**로 확장. 자동 폴백·토큰압축 15~95%·MCP·26+ 코딩에이전트 연동·로컬 우선(무텔레메트리) 유지. "never stop coding"(한도에 안 걸리는 무중단 코딩) 슬로건대로 **비용 최적화 게이트웨이**로 안착. reliability high 유지(무료 토큰량은 프로바이더 약관 종속).

> [!update] 2026-07-21 갱신 — WebFetch 실검증 + 프로바이더 확장
> GitHub ⭐**22,500**(WebFetch 실확인, raw ⭐22,537·+1,107/일과 일치) ← ⭐8,948(07-01). 20일간 **+1.35만(2.5배)** 폭발적 성장. 프로바이더도 **236→271개**로 확장(무료 티어 90+), 자동 폴백·토큰 압축 15~95%·MCP 104툴·26+ 코딩 에이전트 연동은 유지. 게이트웨이가 "단순 라우팅→비용 최적화 레이어"로 자리잡는 흐름을 스타 급증이 방증. 무료 프로바이더에 [[Zhipu AI]] GLM-Flash 포함 신호도 지속. reliability high 유지(헤드라인 수치는 프로바이더 약관 종속이라 실측 필요).

> [!insight] 핵심 인사이트
> ⭐8,948 (2026-07-01, 당일 +387). **하나의 엔드포인트로 236개 AI 프로바이더(50+ 무료 티어)를 Claude/GPT/Gemini API 형식으로 연결하는 오픈소스 AI 게이트웨이**(TypeScript/Node, MIT). [[Claude-Code-워크플로우]]·Codex·Cursor·Cline·Copilot 같은 코딩 에이전트를 무료 프로바이더에 꽂고 **자동 폴백(auto-fallback)**으로 한도에 걸리지 않게 한다. 핵심 차별점은 **RTK + Caveman 압축으로 토큰을 15~95% 절감** — 게이트웨이가 단순 라우팅을 넘어 *비용 최적화 레이어*가 되는 흐름. 흥미롭게도 무료 프로바이더 목록에 [[Zhipu AI]]의 **Z.AI GLM-Flash**가 무제한 무료로 포함돼, 중국발 오픈 모델이 "게이트웨이 기본 무료 티어"로 편입되는 신호다.

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐⭐⭐⭐ — ⭐8.9K + npm/Docker Hub/Electron 배포 + 41개 언어 README로 실제 운영 프로젝트임이 확인됨. 다만 "1.6B 무료 토큰/월", "236개 프로바이더" 등 헤드라인 수치는 프로바이더 약관·rate limit 변동에 종속되므로 실측 필요.
- **즉시 활용**: YES(후보) — 내 코딩/봇 워크플로에 OpenAI 호환 엔드포인트 하나로 여러 무료·유료 프로바이더를 스위칭하는 비용 절감 레이어로 시험 가능. RTK/Caveman 토큰 압축은 [[firecrawl]]·[[mark-clean]]로 수집한 긴 컨텍스트를 LLM에 넣을 때 직접 절감 효과.
- **6개월 영향력**: 높음 — "모델을 고르는 시대"에서 "게이트웨이가 알아서 라우팅·폴백·압축하는 시대"로. 개인 개발자의 API 비용 구조를 바꿀 수 있는 인프라 계층.
- **대체 관계**: OpenRouter·LiteLLM 같은 라우팅 게이트웨이를 *무료 티어 애그리게이션 + 토큰 압축* 관점에서 보강/대체. Docker·Electron 로컬 우선(local-first) 실행이 강점.
- **허와 실**: "~1.6B 무료 토큰/월"은 개별 무료 풀 합산이라 실제 지속 가용량은 각 프로바이더 약관·한도에 크게 좌우됨. "자동 폴백"의 실효는 프로바이더 품질 편차(무료 모델의 성능 저하)로 갈릴 수 있어, 품질 민감 작업엔 프로바이더 고정 권장.
- **액션**: star + Docker로 로컬 기동 → OpenAI 호환 엔드포인트에 Claude Code 연결, 토큰 압축 on/off로 실제 절감률·품질 저하 측정.

> [!warning] 무료 티어·압축 주의
> 무료 프로바이더는 rate limit·품질·데이터 취급 정책이 제각각이라 민감 데이터·품질 중요 작업엔 부적합할 수 있음. Caveman 압축은 손실 압축이므로 코드·정확 수치가 중요한 프롬프트에서는 압축 강도별 품질 검증 필수.

> [!action] 당장 할 것
> Docker로 1회 기동 후 Claude Code를 OmniRoute 엔드포인트로 붙여 무료 프로바이더 폴백·토큰 압축 실측. GLM-Flash 등 무료 티어 품질을 유료 대비 체감.

## 관련 페이지
- [[Claude-Code-워크플로우]]
- [[Zhipu AI]]
- [[firecrawl]]
- [[mark-clean]]
- [[AI-에이전트-프레임워크]]

## 원본
- 출처: https://github.com/diegosouzapw/OmniRoute
- 스타: ⭐8,948 (2026-07-01, 당일 +387)
- 라이선스: MIT · npm `omniroute` · Docker Hub · Electron 데스크톱 · MCP/A2A 지원
- 신뢰도: ⭐⭐⭐⭐ (실배포 확인 — 무료 토큰량·프로바이더 수 헤드라인은 실측 필요)
