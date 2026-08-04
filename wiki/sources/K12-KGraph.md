---
title: K12-KGraph — 커리큘럼 정렬 지식그래프 벤치마크·학습 데이터
type: source
domain: ai-news
tags: [ai-news, hf-paper, knowledge-graph, education-llm, benchmark, multimodal, curriculum]
created: 2026-07-25
updated: 2026-07-25
sources: []
reliability: medium
---

# K12-KGraph (Curriculum-Aligned Knowledge Graph for Benchmarking and Training Educational LLMs)

> [!insight] 핵심 인사이트
> HF Daily ↑42. 기존 교육 벤치는 "모델이 시험문제를 맞히는가"만 재는데, 이 논문은 지식이 **선수관계·분류체계·교육순서로 어떻게 연결되는가**("curriculum cognition, 커리큘럼 인지")를 측정한다. 중국 K-12 교과서(수·물·화·생, 초~고)에서 **9개 노드타입·14개 관계타입**의 이종(heterogeneous) 그래프를 구축하고, ①**K12-Bench**(23,640문항, Ground·Prereq·Neighbor·Evidence·Locate 5개 태스크군) ②**K12-Train**(그래프 유도 SFT 7,335건, 텍스트/멀티모달) 3종을 함께 낸다. 강력한 상용 모델도 **커리큘럼 구조 태스크 정확도 ~57%**에 그쳐, LLM이 "사실은 알아도 지식 간 관계는 모른다"는 갭을 정량화.

> [!note] 배경 정보
> "지식을 그래프로 구조화해 근거·학습에 쓴다"는 [[RAGU]](소형모델×GraphRAG)·[[code-review-graph]](코드베이스 그래프)·[[graphify]]와 같은 **그래프 기반 근거화** 계보의 교육판. 특히 [[LLM-Wiki]] 이 위키 자체가 wikilink 그래프라, "노드타입·관계타입 스키마로 커리큘럼을 표현"하는 설계는 이 볼트의 concepts/entities 관계 설계에 참고 가치.

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐⭐ — HF 초록 WebFetch 실확인(9노드·14관계·23,640문항·7,335 SFT·상용모델 57% 구체 확인). 미래형 ID(2605.09635)·원문·재현 미검증 medium.
- **즉시 활용**: 간접 — 교육 도메인 특화라 직접 쓸 일은 적으나, **"관계타입 스키마로 지식그래프를 설계"하는 방법론**은 이 위키의 [[LLM-Wiki]] 그래프 품질 개선에 개념 이식 가능(선수관계·근거링크 명시화).
- **6개월 영향력**: LLM 평가가 "정답률"에서 "**지식 구조 이해**"로 확장되는 흐름의 데이터 포인트. 도메인 특화 그래프 유도 데이터가 동일 예산 대비 범용 인스트럭션 튜닝을 능가한다는 주장은 데이터 큐레이션 방향 시사.
- **대체 관계**: 범용 교육 벤치(시험문제형)를 **구조 이해형**으로 보강. GraphRAG([[RAGU]]) 계열의 학습데이터 생성 관점.
- **허와 실**: 중국 K-12 교과서 기반이라 언어·커리큘럼 편향. "57%"는 특정 태스크군 수치로 벤치 난이도 설계에 좌우됨.
- **액션**: 이 위키 그래프에 "선수관계/근거" 관계타입을 명시화할지 개념 검토(직접 도입보다 참고).

## 관련 페이지
- [[RAGU]]
- [[code-review-graph]]
- [[graphify]]
- [[LLM-Wiki]]
- [[ai-news]]

## 원본
- 출처: https://huggingface.co/papers/2605.09635
- HF Daily Papers: ↑42
- 구성: K12-KGraph(9노드·14관계 이종그래프) / K12-Bench(23,640문항·5태스크군) / K12-Train(7,335 SFT, 텍스트+멀티모달). 상용모델 커리큘럼 구조 ~57%
- 신뢰도: ⭐⭐ (초록 WebFetch 실확인, 미래형 ID·원문·재현 미검증 medium)
