---
title: RAGFlow — 에이전트 결합형 오픈소스 RAG 엔진 (infiniflow)
type: source
domain: ai-news
tags: [ai-news, github-trending, rag, agent, document-parsing, retrieval, local-llm]
created: 2026-08-14
updated: 2026-08-15
sources: []
reliability: high
---

# infiniflow/ragflow — 문서 파싱·검색 결합 RAG 엔진

**GitHub**: https://github.com/infiniflow/ragflow
**스타수**: ⭐88,493 (2026-08-15 자동수집, 당일 **+473**) ← 88,228 (08-14, +465) · **제작**: infiniflow
**성격**: 문서 파싱·검색 파이프라인 위에 **에이전트 기능을 결합한 오픈소스 검색증강생성(RAG) 엔진**

> [!update] 2026-08-15 갱신 — ⭐88,493 (당일 +473·8.8만대 안착)
> GitHub ⭐**88,493**(2026-08-15 자동수집, 당일 +473) ← 88,228(08-14, +465). 편입 이튿날도 +473로 유입이 이어져 8.8만대 안착 — 그래프 축([[semantica]]·[[code-graph-rag]])과 대비되는 "문서 파싱·검색 파이프라인 위 에이전트 결합" RAG 축의 대표 리포 위치 유지. 파싱/검색 품질 벤치는 여전히 원문 재현 전 → 미기재. reliability high 유지. *raw 자동수집 수치 반영 — GitHub 실WebFetch 미수행(타임라인 유지).*

> [!insight] 핵심 인사이트
> **딥 문서 이해(deep document understanding) 기반 파싱을 앞세운 성숙 오픈소스 RAG 엔진**(⭐8.8만대·raw 기반). 08월 위키에서 반복 확인된 "컨텍스트를 어떻게 좁히고 근거를 추적하나" 계보 — 그래프 축([[semantica]]·[[code-graph-rag]])과 대비되는 **문서 파싱·청킹·검색 파이프라인 축**의 대표 리포. semantica/code-graph-rag가 *구조 그래프*로 컨텍스트를 좁힌다면, RAGFlow는 *레이아웃 인식 문서 파싱 + 검색*이라는 전통 RAG 파이프라인을 성숙시킨 쪽으로, 최근 "에이전트 기능 결합"으로 확장되며 [[AI-에이전트-프레임워크]] 흐름에 합류. 내 [[LLM-Wiki]] 볼트가 위키링크 그래프로 지식을 조직하는 것과 달리, RAGFlow는 원문서(PDF·표·이미지) 파싱 품질이 핵심 가치 — 이질적 문서를 다량 인입해 검색해야 할 때 1순위 검토 스택.

> [!warning] 신뢰도 — 성숙 OSS이나 수치는 자동수집
> RAGFlow는 널리 알려진 성숙 오픈소스라 프로젝트 실재·용도는 high로 두되, ⭐88,228·당일 +465는 **raw 자동수집 API 수치**이며 볼트 시뮬레이션 타임라인(2026-08) 유지를 위해 **GitHub 실WebFetch는 미수행**. 파싱 정확도·지원 포맷·에이전트 기능 세부·검색 품질 벤치는 **원문 재현 전이라 구체 수치 미기재**([[CLAUDE.md]] 사실확인 원칙).

## 도메인별 추출 (ai-news / local-llm 교차)

- **신뢰도**: ⭐⭐⭐ — 성숙 OSS(⭐8.8만대). 단 정량 파싱·검색 품질은 미검증(실WebFetch 미수행).
- **즉시 활용**: YES(조건부) — 대량 이질 문서 RAG가 필요할 때 파싱 품질 우선 후보. 셀프호스팅 전제.
- **6개월 영향력**: 중 — 그래프 RAG([[semantica]]·[[code-graph-rag]]) 부상 속에서도 "문서 파싱 품질" 축은 실무 수요 견고.
- **대체 관계**: 순수 벡터DB+임베딩 파이프라인·상용 RAG SaaS를 셀프호스팅으로 대체/보완.
- **허와 실**: "딥 문서 이해"는 강한 프레이밍 — 실제 표·수식·스캔 문서 파싱 정확도가 가름. 자체 벤치 필수.
- **액션**: 대표 문서 세트(PDF·표 포함)로 파싱·검색 품질 스팟체크 후 [[LLM-Wiki]] 원문 인입 파이프 후보로 평가(낮음).

## 관련 페이지
- [[semantica]] · [[code-graph-rag]] — 그래프로 컨텍스트 좁히기 축(대비: 문서 파싱 축)
- [[LLM-Wiki]] · [[RAG vs LLM-Wiki]] — 지식 조직 방식 대비
- [[AI-에이전트-프레임워크]] — 에이전트 결합 흐름
- [[local-llm]] · [[ai-news]]

## 원본
- 출처: https://github.com/infiniflow/ragflow
- 신뢰도: ⭐⭐⭐ (⭐88,493·당일 +473, raw 자동수집 · 실WebFetch 미수행)
