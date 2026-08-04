---
title: DocsGPT — 온프레미스형 프라이빗 AI 에이전트·엔터프라이즈 검색 플랫폼
type: source
domain: ai-news
tags: [ai-news, rag, agent-builder, enterprise-search, document-analysis, on-premise, privacy]
created: 2026-07-29
updated: 2026-07-29
sources: []
reliability: high
---

# DocsGPT (arc53/DocsGPT · GitHub ⭐18.2k)

> [!insight] 핵심 인사이트
> [[arc53]]의 **"에이전트·어시스턴트·엔터프라이즈 검색을 위한 프라이빗 AI"** 플랫폼 — 다양한 문서로부터 검색 가능한 지식베이스와 지능형 어시스턴트를 만들되 **배포 통제(온프레미스/쿠버네티스)와 프라이버시**를 유지한다. 기능은 **에이전트 빌더 + 딥리서치 + 문서분석(PDF·DOCX·CSV·XLSX·EPUB·MD·이미지·오디오)**, URL·사이트맵·Reddit·GitHub 웹 연동, **출처 인용 기반 "환각 없는 답변"**, API 키 발급, 사전제작 위젯·봇 통합, OpenAI/Google/Anthropic·로컬 모델 지원. [[OpenViking]](컨텍스트 DB)·[[cognee]] 같은 순수 메모리 레이어와 달리, **완성형 RAG 애플리케이션**으로 조직이 바로 배포하는 제품층. MIT.

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐⭐⭐⭐ — 스타 18.2k·MIT·기능 목록 WebFetch 실확인. 오래된 성숙 프로젝트로 실사용 기반 존재.
- **즉시 활용**: 조건부 — 내 [[LLM-Wiki]]는 이미 자체 인제스트·쿼리 파이프라인 보유라 통째 대체는 불필요. 단 **다포맷 문서 로더(EPUB·XLSX·오디오)**와 **출처 인용 강제** 설계는 위키 인제스트의 입력 다양화·신뢰도 표기에 참고.
- **6개월 영향력**: "프라이빗·온프레미스 RAG 플랫폼"의 표준 제품형. 로컬/엔터프라이즈 검색이 완성형 제품으로 상품화되는 흐름 확인.
- **대체 관계**: [[OpenViking]]·[[cognee]]가 컨텍스트 저장 레이어라면 DocsGPT는 그 위 **완성 애플리케이션** — 상호보완. 웹 연동은 [[Firecrawl]]·[[mark-clean]] 역할과 겹침.
- **허와 실**: "환각 없는 답변"은 마케팅 — 실제로는 **출처 인용으로 검증 가능성**을 높인 것. 완전 무환각 아님.
- **액션**: 문서 로더(오디오 전사·EPUB 파싱) 구현을 코드로 참고해 위키 인제스트 입력 게이트 확장 여부 판단.

## 관련 페이지
- [[arc53]]
- [[OpenViking]]
- [[cognee]]
- [[Firecrawl]]
- [[mark-clean]]
- [[LLM-Wiki]]
- [[에이전트-메모리-레이어]]
- [[ai-news]]

## 원본
- 출처: https://github.com/arc53/DocsGPT
- 스타: ⭐18.2k (2026-07-29, 당일 +37 — raw 18,174와 일치), MIT
- 기능: 에이전트 빌더·딥리서치·다포맷 문서분석·웹 연동(URL/사이트맵/Reddit/GitHub)·출처 인용·API 키·위젯/봇·쿠버네티스 배포·OpenAI/Google/Anthropic+로컬 모델
- 신뢰도: ⭐⭐⭐⭐ (스타·라이선스·기능 WebFetch 실확인)
