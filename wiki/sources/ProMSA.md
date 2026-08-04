---
title: ProMSA — 지식기반 시각 QA용 점진적 멀티모달 검색 에이전트
type: source
domain: ai-news
tags: [ai-news, hf-papers, vqa, multimodal, retrieval-agent, rl, rag]
created: 2026-06-29
updated: 2026-06-29
sources: []
reliability: medium
---

# ProMSA (Progressive Multimodal Search Agent)

> [!insight] 핵심 인사이트
> HF 데일리 페이퍼 (upvote 7, 2026-06-29). 외부 지식이 필요한 시각 QA(knowledge-based VQA)에서 **검색 전략을 상황에 맞게 적응적으로 선택**하고, 이를 **시퀀스 레벨 RL로 최적화**하는 점진적 멀티모달 검색 에이전트. "한 번 검색하고 끝"이 아니라 *부족하면 다음 검색 전략으로 진행*하는 에이전트 루프를 학습한다는 점에서, [[firecrawl]]·[[KaLM-Reranker-V1]] 같은 정적 RAG 파이프라인과 달리 **검색 자체를 의사결정으로 다루는** 에이전틱 RAG 계보.

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐⭐ — upvote 7로 주목도는 중간, 단일 논문. 벤치마크 우위 폭과 일반화는 후속 확인 필요.
- **즉시 활용**: MAYBE(개념) — 내 위키 쿼리/[[deep-research]] 류 다단계 검색에 "검색 전략 적응 선택" 발상 차용 가능. 코드 직접 적용은 아님.
- **6개월 영향력**: 중간 — RAG가 "고정 파이프라인"에서 "검색을 RL로 학습하는 에이전트"로 이동하는 흐름의 한 사례. 멀티모달(이미지+텍스트) 검색 결합이 차별점.
- **대체 관계**: 단순 top-k 검색 + 리랭커 조합을 *보강*. 검색 횟수·전략을 동적으로 정해 비용/정확도 균형.
- **허와 실**: 적응 검색은 추론 비용 증가를 수반. "필요할 때만 더 검색"의 실효 비용을 봐야 함.
- **액션**: 읽기 — 위키 쿼리 합성 시 "1차 답이 약하면 검색 전략 전환" 루프 설계에 참고.

## 관련 페이지
- [[firecrawl]]
- [[KaLM-Reranker-V1]]
- [[deep-research]]
- [[AI-에이전트-프레임워크]]
- [[ProMSA]]

## 원본
- 출처: https://huggingface.co/papers/2606.27974
- HF 데일리: upvote 7 (2026-06-29)
- 신뢰도: ⭐⭐ (단일 논문, 중간 주목도 — 개념 참고 위주)
