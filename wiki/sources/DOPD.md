---
title: DOPD — Dual On-policy Distillation (이중 온폴리시 증류)
type: source
domain: ai-news
tags: [ai-news, hf-paper, on-policy-distillation, knowledge-distillation, llm, vlm, rl]
created: 2026-07-01
updated: 2026-07-01
sources: []
reliability: high
---

# DOPD: Dual On-policy Distillation (HF papers 2606.30626)

> [!insight] 핵심 인사이트
> **HF 데일리 3위 (↑56, 2026-07-01).** [[온폴리시-증류]](OPD)의 다음 진화. OPD 성능을 더 끌어올리려 교사·학생에 **특권 정보(privileged information)**를 주입하면 **"특권 착각(privilege illusion)"**이라는 실패 모드가 생긴다 — *학생이 실제로 좁혀야 할 능력 격차*와, *모방만 가능하고 복제는 불가능한 정보 비대칭 격차*를 혼동하는 것. DOPD는 **어드밴티지 격차와 상대 확률에 따라 토큰 단위 감독을 특권 교사↔특권 학생 사이로 동적으로 라우팅**해, 각 토큰이 서로 다른 강도·목표·전략의 신호를 받게 함으로써 특권 착각을 완화한다. LLM·VLM 양쪽에서 Vanilla OPD와 경쟁 기법을 일관되게 능가. [[온폴리시-증류]] 클러스터([[DanceOPD]]·[[OPID]]·[[Draft-OPD]]·[[TrOPD]])에 "특권 정보의 함정"이라는 새 축을 더한다.

## 도메인별 추출 (ai-news / local-llm 교차)

- **신뢰도**: ⭐⭐⭐⭐ — HF 데일리 3위 + LLM/VLM 양 설정 + 안정성·강건성·지속학습·OOD까지 검증 범위 넓음. [[온폴리시-증류]] 다수 독립팀 수렴 흐름의 최신 사례로 신뢰 높음.
- **즉시 활용**: NO — 증류 학습 기법이라 직접 학습을 안 하는 내 워크플로엔 즉시 적용 없음. 다만 [[local-llm]] GGUF·소형 모델 품질 향상 경로로 간접 관련.
- **6개월 영향력**: 중~높음 — "학생 자기생성 샘플 + 교사 신호"라는 OPD 패러다임이 성숙기에 진입, 각 팀이 세부 실패 모드(특권 착각·credit assignment)를 메우는 국면. 결과적으로 소형 오픈 모델의 품질 상향으로 귀결.
- **대체 관계**: Vanilla OPD·off-policy KD를 대체. [[GBC]](멀티에이전트 토큰 단위 credit assignment)와 "토큰 단위 신호 정밀화"라는 문제의식 공유.
- **허와 실**: "특권 착각"은 개념적으로 유용하나 실무 적용에는 특권 정보 설계·어드밴티지 추정 정확도가 관건. 벤치 우위가 실제 배포 모델 품질 격차로 얼마나 이어지는지는 별개.
- **액션**: 개념 노트로 [[온폴리시-증류]]에 통합. 향후 소형 모델 파인튜닝 필요 시 OPD 계열 우선 검토.

## 관련 페이지
- [[온폴리시-증류]]
- [[DanceOPD]]
- [[OPID]]
- [[Draft-OPD]]
- [[GBC]]
- [[local-llm]]

## 원본
- 출처: https://huggingface.co/papers/2606.30626 (arXiv:2606.30626)
- HF 데일리: 3위 ↑56 (2026-07-01)
- 신뢰도: ⭐⭐⭐⭐ (LLM+VLM 검증, 온폴리시 증류 수렴 흐름의 최신판)
