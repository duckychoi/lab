---
title: Ideas Have Genomes — 과학 아이디어 계보 추론 벤치
type: source
domain: ai-news
tags: [ai-news, huggingface, paper, scientific-lineage, idea-generation, sjtu, benchmark]
created: 2026-07-10
updated: 2026-07-10
sources: []
reliability: medium
---

# HF논문: Ideas Have Genomes — Benchmarking Scientific Lineage Reasoning (arXiv 2607.08758)

**HuggingFace**: https://huggingface.co/papers/2607.08758
**기관**: 상하이교통대(SJTU, Yifan Zhou 외) · **벤치명**: IdeaGene-Bench (IG-Bench)

> [!insight] 핵심 인사이트
> **과학 연구를 "아이디어 게놈(Idea Genome)"으로 모델링해, 개념 계보 추적 추론과 계보 근거 아이디어 생성을 벤치마킹.** WebFetch로 초록 실측: 논문을 타입화·증거기반 구성요소를 가진 게놈 객체로 표현하고, **GenomeDiff**로 6가지 진화 동역학(상속·변이·소실·외부도입·신규삽입·재조합)을 추적. 두 트랙: ①**IG-Exam**(42개 태스크로 게놈 추상화·상속 추적·계보 검증 폐쇄형 추론), ②**IG-Arena**(유전·변이·선택가치를 재는 Population-Evolution Score로 생성 평가). 결과: 14개 LM 시스템 중 **최고도 계보 추론 정확도 27.3%**에 그침 = 심각한 조합적 병목. 이것은 개념적으로 내 [[LLM-Wiki]]·[[graphify]]와 같은 그래프-사고 계열 — "아이디어를 노드로, 영향 관계를 엣지로" 다루며, 위키의 synthesis(교차 인사이트)가 노리는 "계보/파생 관계 추론"이 **최신 LLM에게도 27.3%로 어렵다**는 현실을 보여줌.

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐⭐⭐ (arXiv 2607.08758 초록 WebFetch 검증 — IG-Exam/Arena·6동역학·최고 27.3% 확인. 재현 미실측 → medium)
- **즉시 활용**: 간접 — 벤치. 단 "아이디어 게놈 + GenomeDiff 6동역학"은 내 위키가 소스 간 계보를 추적할 때(예: [[온폴리시-증류]] 클러스터, [[임바디드-AI]] 5각 루프) 채택할 사고 프레임.
- **6개월 영향력**: LLM 과학 조력이 "요약"에서 "아이디어 계보 추적·근거 생성"으로 요구가 올라가나, 27.3% 병목이 그 한계를 못박음.
- **대체 관계**: [[NatureBench]](SOTA 재현)과 짝 — 재현 vs **계보 추론**으로 과학 에이전트 평가 축 이원화.
- **허와 실**: "27.3%"는 초록 명시. 낙관 마케팅 없이 오히려 한계를 강조하는 논문 — 신뢰도 프레이밍은 건전.
- **액션**: 위키 synthesis 페이지 작성 시 6동역학(상속/변이/소실/도입/삽입/재조합) 라벨로 소스 계보를 태깅하는 실험(예: 어텐션 효율 계보에 적용).

## 관련 페이지
- [[graphify]] — 코드 지식 그래프(같은 배치, 그래프-사고 공명)
- [[LLM-Wiki]] — 소스 계보·synthesis = 아이디어 게놈의 위키판
- [[NatureBench]] — 과학 SOTA 재현 벤치(짝)
- [[ai-news]]

## 원본
- 출처: https://huggingface.co/papers/2607.08758
- arXiv: 2607.08758, IdeaGene-Bench (상하이교통대)
- 성과: 아이디어 게놈 + GenomeDiff 6동역학 / IG-Exam 42태스크 + IG-Arena / 최고 27.3% 계보 추론
- 신뢰도: ⭐⭐⭐ (초록 원문 검증 / 재현 미실측)
