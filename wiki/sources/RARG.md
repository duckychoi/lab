---
title: RARG — 관련성으로 에이전틱 검색의 코퍼스 상호작용을 유도(relevance-aware ripgrep)
type: source
domain: ai-news
tags: [ai-news, agentic-search, retrieval, ripgrep, browsecomp, tencent, tool-use]
created: 2026-07-29
updated: 2026-07-29
sources: []
reliability: medium
---

# RARG (A New Role for Relevance · 논문 2607.24223)

> [!insight] 핵심 인사이트
> [[Tencent]]·IIE-CAS(Jiangnan Li 외)의 **에이전틱 검색 방법론** — 검색 에이전트가 문서 코퍼스와 상호작용하는 방식을 재설계한다. 문제의식: 전통 검색은 관련성으로 문서를 **랭킹**하지만 세밀한 탐색을 유도하지 못하고, grep식 직접 코퍼스 조작은 정밀하지만 **우선순위가 없다**. RARG는 **"relevance-aware ripgrep search"** — 문서 수준 랭킹으로 **탐색 순서를 정하고**, 매치 수준 리랭킹으로 **정보성 높은 발췌를 먼저 노출**한다. 결과: **BrowseComp-Plus 84% 정확도를 평균 23.9회 도구호출**로 달성(경쟁 방식 28.7·99.1회 대비 효율↑). [[StateAct]]("픽셀 대신 상태 직접조회")·[[book-to-skill]]·[[mark-clean]]의 **"LLM이 grep·파일·DOM으로 코퍼스를 직접·구조적으로 다룬다"** 흐름을 검색에 적용한 항.

> [!action] 위키 쿼리 엔진에 직접 이식 후보
> RARG의 **"랭킹으로 탐색 순서 + 매치 리랭킹으로 발췌 우선"**은 이 위키의 grep 기반 탐색(index→domain→page, `grep -rli`)에 그대로 적용 가능. 지금은 순진한 grep인데, **관련성 랭킹으로 어떤 페이지를 먼저 열지 + 매치 스니펫 리랭킹**을 얹으면 쿼리 응답의 토큰·정확도 개선 기대.

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐⭐⭐ — 초록·저자(Jiangnan Li·Yuqing Li·Mo Yu·Jinchao Zhang·Jie Zhou)·기관([[Tencent]]·IIE-CAS)·구체 수치(84%·23.9/28.7/99.1) WebFetch 실확인. 단 미래형 ID·독립 재현 전.
- **즉시 활용**: YES(개념) — 위키 쿼리·인제스트 탐색에 relevance-aware grep 이식. ripgrep은 내 Grep 도구와 동일 계열이라 실험 장벽 낮음.
- **6개월 영향력**: 에이전틱 검색이 "벡터 RAG"에서 **"랭킹+grep 하이브리드 도구사용"**으로 이동하는 신호. 도구호출 횟수(비용) 최적화가 실전 지표로 부상.
- **대체 관계**: 순수 벡터 RAG([[cognee]])·순수 grep의 중간. [[OpenViking]] 티어드 로딩·재귀검색과 상보.
- **허와 실**: BrowseComp-Plus 84%는 자체 벤치 — 방향(랭킹+grep 결합)은 설득력 있으나 절대치 재현 전.
- **액션**: 위키 `grep -rli` 탐색에 index 요약 기반 페이지 우선순위 + 매치 스니펫 정렬을 얹은 프로토타입 쿼리 실험.

## 관련 페이지
- [[Tencent]]
- [[StateAct]]
- [[book-to-skill]]
- [[mark-clean]]
- [[OpenViking]]
- [[cognee]]
- [[LLM-Wiki]]
- [[ai-news]]

## 원본
- 출처: https://huggingface.co/papers/2607.24223 (arXiv 2607.24223)
- 저자/기관: Jiangnan Li·Yuqing Li·Mo Yu·Jinchao Zhang·Jie Zhou / [[Tencent]]·IIE-CAS
- 업보트: 70 (HF 데일리 논문, raw 기재)
- 핵심(자체): relevance-aware ripgrep — BrowseComp-Plus 84%·평균 23.9 도구호출(vs 28.7·99.1)
- 신뢰도: ⭐⭐⭐ (초록·저자·기관·수치 WebFetch 실확인, 미래형 ID·원문 재현 미검증 medium)
