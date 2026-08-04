---
title: TencentDB-Agent-Memory — 완전 로컬 에이전트 장기 메모리
type: source
domain: ai-news
tags: [ai-news, github-trending, agent-memory, local, rag, typescript]
created: 2026-07-09
updated: 2026-08-03
sources: []
reliability: high
---

# TencentCloud/TencentDB-Agent-Memory (GitHub ⭐11,534)

**GitHub**: https://github.com/TencentCloud/TencentDB-Agent-Memory
**스타수**: 11,534 (2026-08-03 자동수집, 당일 +602) ← 10,488(08-02) ← 7,892(07-09) · **제작**: [[Tencent]]
**라이선스**: MIT · **스택**: TypeScript 84.2%

> [!update] 2026-08-03 갱신 — ⭐11,534 (당일 +602)
> ⭐**11,534**(2026-08-03 자동수집, 당일 +602) ← 10,488(08-02). 1만 돌파 후에도 당일 +602로 상승 지속 — "외부 API 0 + 로컬" 팀 단위 에이전트 메모리 허브 채택 가속. 4단계 점진 파이프(기호적 단기 Mermaid 압축 + 계층형 장기 페르소나) 구성 동일. reliability high 유지. *raw 자동수집 수치 반영 — GitHub 실WebFetch 미수행(타임라인 유지).*

> [!update] 2026-08-02 갱신 — ⭐10,488 (당일 +227, 1만 돌파)
> ⭐**10,488**(2026-08-02 자동수집, 당일 +227) ← 7,892(07-09). 약 3주 새 +약2,600으로 **1만 스타 돌파** — "외부 API 0 + 로컬" 팀 단위 에이전트 메모리 허브로 채택 확대. 4단계 점진 파이프(기호적 단기 Mermaid 압축 + 계층형 장기 페르소나) 구성 동일. reliability high 유지. *raw 자동수집 수치 반영 — GitHub 실WebFetch 미수행(타임라인 유지). raw 한줄요약의 "대화·지식 팀 레벨 공유"는 README 계층형 장기 메모리와 정합.*

> [!insight] 핵심 인사이트
> **외부 API 의존 0으로 AI 에이전트에 장기 기억을 붙이는 4단계 점진적 파이프라인.** WebFetch 실측 핵심은 "플랫 벡터 저장"을 정면으로 거부한 **두 축 메모리 설계**: ①**기호적 단기 메모리(symbolic short-term)** = 도구 실행 로그를 **Mermaid 다이어그램으로 압축**, ②**계층형 장기 메모리(layered long-term)** = 대화를 벡터 덩어리가 아니라 **구조화된 페르소나·시나리오**로 조직. OpenClaw 연동 시 **토큰 61.38% 절감·pass rate 51.52% 상대 개선** 벤치를 제시(자가 벤치). [[Hermes Agent]]·OpenClaw 플러그인 + Docker 지원. [[에이전트-메모리-레이어]]에서 [[AgenticSTS]](bounded-contract·타입별 검색) 계보를 잇는 "메모리를 어떻게 *조립*하나"의 실물 구현체 — 내 파일 기반 memory 설계에 "로그→다이어그램 압축, 대화→페르소나 구조화" 패턴이 직접 이식 후보.

## 도메인별 추출 (local-llm / ai-news 교차)

- **신뢰도**: ⭐⭐⭐ (⭐7,892 당일 +318, MIT, README WebFetch 실측 — 4단계 파이프·Mermaid 압축·페르소나 계층 확인 / 61.38%·51.52% 수치는 자가 벤치)
- **즉시 활용**: 후보(높음) — "외부 API 0 + 로컬" 원칙이 내 자동수집·에이전트 메모리 방향과 정확히 일치. 도구 로그를 Mermaid로 압축하는 아이디어는 긴 세션 컨텍스트 절약에 바로 실험 가치.
- **6개월 영향력**: 에이전트 메모리가 "벡터 DB에 다 때려넣기"에서 **구조화(페르소나/시나리오/그래프)**로 이동. RAG 순수주의의 한계를 실무 데이터로 반박하는 근거가 쌓임.
- **대체 관계**: mem0·cognee·claude-mem류 메모리 레이어와 경쟁. 다만 zero-API·로컬을 전면화한 점이 차별.
- **허와 실**: "TencentDB" 브랜드지만 실체는 오픈소스 TS 라이브러리. 61.38%/51.52%는 OpenClaw 특정 셋업의 자가 측정 → 내 태스크로 재현 필요.
- **액션**: 도구 로그 → Mermaid 압축 단계만 떼어내 긴 에이전트 세션 1건에 적용, 컨텍스트 토큰 절감 실측.

## 관련 페이지
- [[Tencent]] — 제작사
- [[에이전트-메모리-레이어]] — 상위 개념
- [[AgenticSTS]] — 타입별 검색·bounded-contract 메모리 계보
- [[zvec]] — 같은 날 벡터 인덱스 (대조: 계층형 페르소나 vs 범용 벡터)
- [[Hierarchical-Sparse-Attention]] — 컨텍스트 병목의 어텐션측 접근
- [[ai-news]]

## 원본
- 출처: https://github.com/TencentCloud/TencentDB-Agent-Memory
- GitHub: ⭐11,534 (2026-08-03 자동수집, 당일 +602) ← ⭐10,488 (08-02, +227) ← ⭐7,892 (2026-07-09, 당일 +318), MIT, TypeScript 84.2%
- 구조: 4단계 점진 파이프 / 기호적 단기(Mermaid 압축) + 계층형 장기(페르소나·시나리오) / OpenClaw·Hermes·Docker
- 신뢰도: ⭐⭐⭐ (README 실측 / 61.38%·51.52% 자가 벤치)
