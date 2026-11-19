---
title: "Jeveration — System One 모델(Jev)이 이미지도 1회 forward로 생성 (78ms · 122× · GenEval 0.74 < Janus-Pro 0.80)"
type: source
domain: ai-news
tags: [ai-news, system-one, image-generation, single-step, vlm, paper]
created: 2026-11-19
updated: 2026-11-19
sources: [https://huggingface.co/papers/2611.24738]
reliability: medium
---

**논문**: arXiv 2611.24738 · 업보트 34 · National University of Singapore · 코드 [Carol-lyh/Jeveration](https://github.com/Carol-lyh/Jeveration) (🆕 볼트 확인 — 수집기 미기재)

## 핵심 인사이트
> [!insight] "점수화"하던 System One 계열이 "생성"으로 확장됐다
> 고정된 VLM(Jev) 위에서, **모든 위치를 공유 랜덤 상태에 조건화**해 병렬 예측이 하나의 일관된 이미지로 수렴하게 한다(직접 이미지 감독 시 모델이 랜덤 상태를 무시하므로 이산 이미지 코드 분포를 먼저 학습). 한 체크포인트로 t2i · i2i · 밀집 예측(깊이 등)을 각각 1회 forward. 볼트 [[System-One-모델]] 개념의 정의("생성 대신 점수화")가 이 논문으로 **경계가 흐려진다**.

> [!warning] 속도는 앞서고 품질은 뒤진다 (arXiv HTML 표 볼트 대조)
> - Jeveration: 5.2B · 1 step · 512px · **0.74 GenEval · 78.24 DPG** · 77.8ms (H200)
> - Janus-Pro-7B: 576 step · 384px · **0.80 · 83.91** · 9,508.4ms — 122× 는 이 모델 대비다.
> - SANA-Sprint 0.6B: 1 step · **1024px** · 0.72 · 78.63 · 121.2ms — 같은 1-step 대비로는 **해상도 절반에 비슷한 점수**.
> ⇒ "122× 빠름"은 가장 느린 통합 모델 기준. 초록의 "competitive image quality" 는 [[한정어-탈락]] 없이 읽어야 한다.

## 도메인별 추출 (ai-news)
- **신뢰도**: ⭐⭐⭐ — 본문 표 · 코드 공개.
- **즉시 활용**: NO — 이미지 품질이 실무 기준선 미달. 하나의 체크포인트로 3과제를 하는 **구조**가 관심 대상.
- **6개월 영향력**: 에이전트용 저지연 VLM 이 생성까지 겸하면 "판단 + 시각 피드백" 루프 비용이 낮아진다.
- **허와 실**: 속도 우위는 실측, 품질 우위 주장은 없음.

## 관련 페이지
- [[System-One-모델]] · [[Jeva]] · [[VideoJev]] · [[SearchJev]] · [[AutoTrust-JEV-27B]] · [[SANA-WM]] · [[비매칭-비교]] · [[한정어-탈락]]

## 원본
- 출처: https://huggingface.co/papers/2611.24738 · https://arxiv.org/html/2611.24738
- 확인 범위: HF papers API 초록 · arXiv HTML 비교 표 행(Jeveration · Janus-Pro-7B · SANA-Sprint) 문자열 대조 · 🔴 i2i · 밀집 예측 수치 미확인
- 신뢰도: ⭐⭐⭐
