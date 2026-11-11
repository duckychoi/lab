---
title: "APEX 스트리밍 확장 (Condition Shifting) — few-step 스트리밍 영상 증류에서 fake-score 네트워크를 없앤다: 학습 메모리 −4.4% · 반복 시간 −9.2%, 품질 차이는 소수점 둘째 자리"
type: source
domain: video-saas
tags: [video-saas, hf-paper, video-generation, distillation, streaming, avatar, tsinghua]
created: 2026-11-11
updated: 2026-11-11
sources: [https://huggingface.co/papers/2611.14033]
reliability: medium
---

**논문**: [2611.14033](https://huggingface.co/papers/2611.14033) *Few-Step Streaming Video Generation via Condition Shifting* · Tsinghua University · 업보트 **13** · 코드 링크 없음

## 핵심 인사이트
> [!insight] 이득은 화질이 아니라 학습 비용이다
> DMD 는 few-step 생성기를 감독하려고 별도의 fake-score 네트워크를 둔다. 이 논문은 **같은 생성기 파라미터에 "이동된 조건(shifted condition)"을 넣어** 생성 분포의 속도장을 추정해 그 네트워크를 없앤다(APEX 의 스트리밍 확장). 동일 학습 설정에서 DMD 대비 GPU 피크 메모리 **−4.4%** · 평균 반복 시간 **−9.2%**. 품질은 S2-Avatar 대비 지시 이행 3.856 vs 3.831, 시각 미학 0.6419 vs 0.6326 — 차이가 0.025 · 0.009 다(초록 전문 일치).

> [!warning] 초록이 스스로 적은 약점 (정방향 사례)
> - **모션 품질은 S2-Avatar 가 우세**, AV 동기화는 대체로 동률, 사용성은 변화 없음 — 저자가 초록에 직접 적었다.
> - 인간 평가는 70건. 지시 이행 순선호 +30.0% 는 크지만 일관성·화질은 각 +4.3%(70건 기준 약 3건 차이, 볼트 계산)다.
> - 자동 지표 차이에 분산·유의성 표기는 초록에 없다.

## 도메인별 추출 (video-saas)
- **기능 벤치마킹**: 내 SaaS 에 직접 넣는 기능이 아니라 **학습 파이프라인 최적화**. 180초 길이 스트리밍 아바타 영상을 few-step 으로 만드는 계열의 학습비를 약 10% 줄인다.
- **크리에이터 인사이트**: 사용자 체감 변화는 지시 이행 쪽에 한정.
- **프롬프트 패턴**: 해당 없음.
- **워크플로우**: 평가 구성 — 180초 영상 · 블록당 백본 평가 3회 + 1스텝 공간 Refiner · 인간 평가 70건 · StreamAV-Bench 320건.
- **경쟁 우위 빈틈**: 장시간 아바타 스트리밍은 모션 품질이 여전히 열려 있다.

## 관련 페이지
- [[MiniMax-H3]] · [[Viggle-Remake]] · [[MiniMax-H3-Image]]

## 원본
- 출처: https://huggingface.co/papers/2611.14033
- 확인 범위: HF papers API 초록 전문 · 🔴 본문 미열람 · S2-Avatar · APEX 원논문 미조회
- 신뢰도: ⭐⭐ (업보트 13 · 코드 없음)
