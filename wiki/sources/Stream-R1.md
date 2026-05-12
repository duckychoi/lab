---
title: Stream-R1 — 스트리밍 비디오 생성 신뢰도·혼잡도 인식 보상 증류
type: source
domain: ai-news
tags: [ai-news, video-saas, streaming-video, rl, reward-distillation, diffusion]
created: 2026-05-07
updated: 2026-05-07
sources: []
reliability: high
---

# Stream-R1: Reliability-Perplexity Aware Reward Distillation for Streaming Video Generation

> [!insight] 핵심 인사이트
> 스트리밍 비디오 생성에서 신뢰도(Reliability)와 혼잡도(Perplexity)를 동시에 인식하는 **보상 증류** 방법론. 업보트 96 — 스트리밍 영상 품질 일관성 문제를 RL 보상 신호로 직접 해결하는 접근. [[Stream-T1]]과 쌍을 이루는 연구.

**HuggingFace**: https://huggingface.co/papers/2605.03849  
**업보트**: 96 (2026-05-07 기준)  
**신뢰도**: ⭐⭐⭐⭐

## 도메인별 추출 (video-saas 관점)

- **신뢰도**: 업보트 96 — 높은 커뮤니티 관심. 스트리밍 영상 생성 품질 문제 실용적 해결
- **즉시 활용**: 직접 구현보다 스트리밍 영상 파이프라인 설계 시 품질 지표 설정 참고
- **6개월 영향력**: 실시간 스트리밍 AI 영상 생성의 품질 안정성 향상. [[Pixelle-Video]] · [[Sulphur-2-base]] 등 로컬 T2V 모델에 적용 가능
- **대체 관계**: [[Stream-T1]](테스트타임 스케일링 접근)과 같은 문제 다른 해법
- **기능 벤치마킹**: 보상 증류로 긴 영상 생성 시 품질 저하·일관성 깨짐 문제 해결 가능성

> [!note] 배경 정보
> 스트리밍 비디오 생성 = 전체 영상을 한 번에 생성하지 않고 실시간으로 프레임을 순차 생성. 이 과정에서 일관성 유지가 핵심 과제.

## 관련 페이지
- [[Stream-T1]]
- [[Pixelle-Video]]
- [[AI-영상-생성-2026]]
- [[Sulphur-2-base]]

## 원본
- 출처: https://huggingface.co/papers/2605.03849
- 신뢰도: ⭐⭐⭐⭐ (업보트 96)
