---
title: Ring-Zero — 조 단위 파라미터 Zero RL 스케일링 (inclusionAI)
type: source
domain: ai-news
tags: [ai-news, hf-paper, reinforcement-learning, zero-rl, scaling, reasoning, trillion-params, inclusionai]
created: 2026-07-16
updated: 2026-07-16
sources: []
reliability: medium
---

# Ring-Zero: 조 단위 파라미터 Zero RL 스케일링

> [!insight] 핵심 인사이트
> HF 추천 **66 (2026-07-16 처리)**. [[inclusionAI]](Ant Group 계열)가 **별도 SFT(지도 파인튜닝) 없이 Zero RL을 1조(trillion) 파라미터 규모로 확장**해 창발적 추론 능력을 유도했다고 보고. DeepSeek-R1-Zero가 연 "SFT 생략, 순수 RL로 추론 창발" 노선을 조 단위 스케일로 밀어붙인 것. 핵심 함의는 *추론 능력은 정답 검증 가능한 리워드(RLVR)만으로도 대규모에서 창발한다*는 명제의 스케일 검증 — [[verifiers]]의 검증 환경, [[온폴리시-증류]], [[Trust-Region-Policy-Distillation]]와 같은 RL 사후학습 계보의 상단. "SFT 데이터 큐레이션 없이도 스케일이 답"이라는 주장은 데이터·컴퓨트 전략에 큰 시사.

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐⭐ — HF 추천 66. 미래형 ID(2607.12395)로 초록 수준 자동수집 기반·원문 미검증(reliability medium). 조 단위 규모 주장은 재현·자원 접근성 측면에서 독립검증 어려움.
- **즉시 활용**: NO — 조 단위 프리트레이닝은 개인 자원 밖. **RL 사후학습 트렌드 해석 프레임 갱신용**.
- **6개월 영향력**: "Zero RL이 스케일에서 통한다"가 굳어지면 SFT 중심 파이프라인이 RLVR 중심으로 이동 가속. 오픈 대형 모델의 추론 향상 레시피에 영향.
- **대체 관계**: SFT→RLHF 순차 파이프라인의 "순수 RL" 대안 노선. [[verifiers]]·RLVR 환경이 이 접근의 인프라.
- **허와 실**: "1조 파라미터"·"창발"은 강한 클레임 — 컴퓨트 규모가 성능을 견인했는지, 방법이 견인했는지 분리가 어려움. 자체발표 검증 대상.
- **액션**: 원문 공개 시 "SFT 생략 시 손실 vs 이득"·소형 스케일 재현 가능성 확인. RLVR 채점기([[verifiers]]) 조합 관점으로 읽기.

## 관련 페이지
- [[inclusionAI]]
- [[verifiers]]
- [[온폴리시-증류]]
- [[Trust-Region-Policy-Distillation]]
- [[ai-news]]

## 원본
- 출처: https://huggingface.co/papers/2607.12395
- HF 추천: 66 (2026-07-16)
- 신뢰도: ⭐⭐ (미래형 ID·초록 수준 자동수집, 원문 미검증)
