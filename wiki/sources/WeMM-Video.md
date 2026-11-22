---
title: "WeMM-Video — Tencent 오픈소스 옴니모달 영상 이해 모델군 2B · 4B · 9B · 35B-A3B (120+ 벤치 주장 · 초록 점수 0 · Gemini-3.0-Flash 에는 열세)"
type: source
domain: video-saas
tags: [video-saas, paper, omni-modal, video-understanding, tencent, open-weights]
created: 2026-11-22
updated: 2026-11-22
sources: [https://huggingface.co/papers/2611.26409]
reliability: medium
---

**논문**: arXiv 2611.26409 · 업보트 45(볼트 11-22 · 수집기 40) · [[Tencent]] · 저자 12 · 코드 [Tencent/WeMM-Video](https://github.com/Tencent/WeMM-Video) ★68

## 핵심 인사이트
> [!insight] "120개 벤치"와 "점수 0개"가 같은 초록에 있다
> 중 · 영 이중언어 옴니모달(텍스트 · 이미지 · 오디오 · 영상) 4종, instruct/사고 겸용. 약 1.2조 토큰 사전학습 후 다중 교사 OPD · 반복 억제 MrDPO · 전문 RL 로 후학습. 초록은 서술형 주장만 한다: 35B-A3B 가 오디오 동반 영상 평가에서 오픈소스 최고 · Qwen3.5-Omni-Flash 와 Seed2.0-Mini-0428 상회, 9B 가 Qwen3-Omni-30B-A3B-Instruct 상회.

> [!warning] 불리한 쪽 (볼트 초록 원문 확인)
> *"while narrowing the gap with the strong Gemini-3.0-Flash"* = **여전히 열세**. 초록에 `%` 0건, **Korean 문자열 0건**(한국어 지원 언급 없음).

## 도메인별 추출 (video-saas)
- **기능 벤치마킹**: 영상 SaaS 의 자동 캡션 · 장면 검색 · 품질 검수에 쓸 오픈 영상 이해 모델 후보. 9B 가 30B 급을 넘는다는 주장이 맞다면 자체 호스팅 비용이 내려간다 — 단 수치 미확인.
- **크리에이터 인사이트**: 오디오 동반 영상 이해가 주 평가축 → 쇼츠(음성 + 화면) 분석에 맞는 방향.
- **경쟁 우위 빈틈**: 한국어 미확인이라 한국어 쇼츠 분석에는 [[Qwen3.5-Omni]] 계열과 직접 비교 필요.

## 관련 페이지
- [[Tencent]] · [[WeVisForensics]] · [[Qwen3.5-Omni]] · [[ALIVE]] (같은 배치 · 스트리밍 영상 LLM) · [[한정어-탈락]] · [[video-saas]]

## 원본
- 출처: https://huggingface.co/papers/2611.26409
- 확인 범위: HF papers API(초록 전문 — narrowing 문장 · Korean 0 · % 0) · 🔴 본문 표 · 모델 카드 미열람
- 신뢰도: ⭐⭐⭐
