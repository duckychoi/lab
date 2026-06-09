---
title: WBench — Multi-turn Benchmark for Interactive Video World Model
type: source
domain: ai-news
tags: [ai-news, benchmark, video-world-model, multi-turn, interactive, evaluation]
created: 2026-05-26
updated: 2026-05-26
sources: []
reliability: medium
---

# WBench — 인터랙티브 비디오 월드 모델 멀티턴 벤치마크

> [!insight] 핵심 인사이트
> 인터랙티브 비디오 월드 모델(사용자가 행동을 입력하면 이후 영상을 예측)의 멀티턴 추론·예측 능력을 종합적으로 평가하는 새 벤치마크. 기존 단일 프레임 평가 한계를 극복.

## 핵심 인사이트

**WBench가 측정하는 것**:
- 인터랙티브 행동(클릭, 드래그 등) 입력 후 다음 장면 예측 정확도
- 멀티턴 대화처럼 여러 번 상호작용하며 일관된 세계 상태 유지 능력
- 물리 일관성, 객체 영속성, 인과 추론

**연결 관계**: WorldMark, Matrix-Game-3.0, WBench — 비디오 월드 모델 평가 프레임워크가 동시다발 등장 → 인터랙티브 월드 모델 경쟁 본격화 신호

> [!note] 배경 정보
> [[WorldMark]], [[WildClawBench]], [[ClawMark]] 등 AI 에이전트·월드 모델 벤치마크 출시 급증 — 2026년 AI 성능 평가 표준 확보 경쟁 중

## 도메인별 추출 (ai-news)

- **신뢰도**: arXiv 2605.25874, HF 업보트 44 — 논문 있음, 중간 반응
- **즉시 활용**: NO — 벤치마크 논문, 직접 활용 범위 제한적
- **6개월 영향력**: 인터랙티브 월드 모델 선택 시 WBench 점수가 품질 기준이 될 가능성
- **대체 관계**: GameWorld, occubench 등 에이전트 평가 벤치마크와 보완적 관계
- **허와 실**: 새 벤치마크이므로 채택률이 낮을 수 있음 — 기존 SOTA와의 비교 결과 검증 필요
- **액션**: 인터랙티브 영상 생성 도구 평가 시 참조 지표로 활용

## 관련 페이지

- [[WorldMark]]
- [[Matrix-Game-3.0]]
- [[GameWorld]]
- [[AI-영상-생성-2026]]
- [[Seedance]]

## 원본

- 출처: https://huggingface.co/papers/2605.25874
- 신뢰도: ⭐⭐ (논문 있음, 채택 미검증)
