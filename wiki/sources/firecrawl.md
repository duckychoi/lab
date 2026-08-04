---
title: firecrawl — 웹 스크래핑/검색 → LLM 입력 정제 API
type: source
domain: ai-news
tags: [ai-news, github-trending, web-scraping, rag, agent-data, api, data-pipeline]
created: 2026-06-23
updated: 2026-07-07
sources: []
reliability: high
---

# firecrawl/firecrawl

> [!update] 2026-07-07 갱신
> ⭐146,774 (2026-07-07 자동수집; 이전 ⭐137,749 2026-06-23, 2주 +9,025). 웹 데이터 수집 인프라 지위 지속. 라이선스 AGPL-3.0(SDK/UI는 MIT), TS 68.7%/Python 15%/Rust 4.7% WebFetch 실측 확인.

> [!insight] 핵심 인사이트
> ⭐146,774 (2026-07-07). 웹페이지를 대규모로 크롤·검색해 LLM 입력용 정제 마크다운/구조화 데이터로 변환하는 API. RAG·에이전트의 "데이터 수집 레이어" 사실상 표준. 13만+ 스타는 도구를 넘어 인프라 지위 — 에이전트가 웹을 읽는 방식의 기본기.

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐⭐⭐⭐⭐ — ⭐137,749, 성숙 프로젝트, 광범위 채택. 클레임이 아니라 검증된 실사용.
- **즉시 활용**: YES — 위키 인제스트 파이프라인의 소스 수집 단계에 직접 투입 가능. 현재 쓰는 [[mark-clean]](defuddle) 단일 페이지 추출 대비 **대량 크롤 + 검색**까지 커버.
- **6개월 영향력**: RAG·에이전트 데이터 공급의 기본 의존성. 자체 스크래퍼 유지보수 부담을 제거 → 수집 품질 경쟁이 정제·구조화로 이동.
- **대체 관계**: [[mark-clean]]/defuddle(단건 정제), 자체 BeautifulSoup 스크래퍼를 대체·상위 호환. self-host 옵션 있어 비용/프라이버시 제어 가능.
- **허와 실**: 강력하나 동적 JS 사이트·봇 차단·요금이 변수. self-host 시 인프라 운영 비용 발생.
- **액션**: self-host 또는 API로 위키 자동수집 파이프라인 PoC — GitHub Trending/HF 페이지 크롤 자동화.

> [!action] 당장 할 것
> firecrawl로 raw.md 자동 채우기 실험 — 트렌딩 페이지 크롤 → 정제 → raw.md 인제스트 큐 자동 적재 파이프라인 PoC.

## 관련 페이지

- [[mark-clean]]
- [[deer-flow]]
- [[codebase-memory-mcp]]
- [[OpenMontage]]
- [[LLM-Wiki]]

## 원본
- 출처: https://github.com/firecrawl/firecrawl
- 스타: ⭐137,749 (2026-06-23, 당일 +615)
- 신뢰도: ⭐⭐⭐⭐⭐ (성숙·검증된 인프라)
