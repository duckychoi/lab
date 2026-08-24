---
title: Qwen3.5-Omni Technical Report
type: source
domain: ai-news
tags: [ai-news, qwen, omni, multimodal, speech, vision, text, any-to-any]
created: 2026-04-20
updated: 2026-04-20
sources: []
reliability: high
---

# Qwen3.5-Omni Technical Report

> [!insight] 핵심 인사이트
> Qwen3.5-Omni는 텍스트·음성·이미지·비디오 전방위 모달리티 처리 통합 모델 — 음성·시각 이해 통합 성능 상위권. [[Qwen3.6-35B-A3B]]의 멀티모달 확장 경로를 보여주며, Any-to-Any 모델 경쟁(Gemma-4 시리즈, GPT-4o)에서 Qwen 생태계의 포지션을 확인.

## 도메인별 추출

**신뢰도**: ⭐⭐⭐⭐ (arXiv 2604.15804, Alibaba DAMO Academy, upvote 9)
**즉시 활용**: YES — HuggingFace에 모델 공개 예정 / 이미 일부 공개. 음성-텍스트-비전 통합 파이프라인에 활용
**6개월 영향력**: Any-to-Any 모델 경쟁이 오픈소스로 확산되는 분기점 확인
**대체 관계**: GPT-4o(클로즈드), Gemma-4 E4B의 오픈소스 대안

## 주요 기능

- 텍스트, 음성, 이미지, 비디오 통합 입출력
- 실시간 음성 대화 지원
- 시각 이해 + 언어 이해 통합 추론
- Apache 2.0 오픈소스

> [!note] 배경 정보
> Qwen 시리즈는 Alibaba가 오픈소스 LLM 생태계에서 급격히 영향력을 확장 중. Qwen3.5-Omni는 GPT-4o 포지션을 직접 겨냥.

> [!note] 2026-08-24 — 옴니 계열의 실시간 상호작용 실측치가 처음 나왔다 ([[OmniAssistBench]])
> [[OmniAssistBench]](HF 데일리 신규 2위·초록 원문 실검증)가 **Qwen3-Omni-Instruct 51.2 / 100**(상용 Gemini-3-Pro 66.4)을 보고했다. 이 페이지가 다루는 Qwen 옴니 계열과 **정확히 같은 모델은 아니나 가장 가까운 공개 실측치**이며, 오픈 옴니 모델이 **실시간 어시스턴트 상호작용 축에서는 상용 대비 15.2점 뒤진다**는 첫 정량 근거다. 공통 실패는 **시각 프롬프트(손동작) 처리·멀티턴 히스토리 유지·목표 이벤트까지 응답 지연**이다. ⚠️모델명 표기가 다르므로(`Qwen3-Omni-Instruct`) **본 페이지 모델의 점수로 그대로 인용하지 말 것.**

## 관련 페이지

- [[Qwen3.6-35B-A3B]]
- [[Qwen3.5-Claude-Distilled]]
- [[Gemma-4-E4B]]
- [[OmniVoice]]

## 원본

- 출처: https://huggingface.co/papers/2604.15804
- 업보트: 9 (2026-04-20)
- 신뢰도: ⭐⭐⭐⭐
