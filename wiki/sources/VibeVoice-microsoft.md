---
title: microsoft/VibeVoice
type: source
domain: ai-news
tags: [ai-news, tts, asr, speech-ai, microsoft, real-time, open-source]
created: 2026-04-29
updated: 2026-04-29
sources: []
reliability: high
---

# microsoft/VibeVoice

> [!insight] 핵심 인사이트
> Microsoft가 TTS(1.5B)·ASR(7B)·실시간TTS(0.5B) 3모델 구성의 오픈소스 음성 AI 공개. 60분 음성 단일 패스 인식, 90분 다화자 음성 합성 지원. GitHub ⭐45,300 (오늘 +1,483) — 출시 당일 폭발적 반응.

## 도메인별 추출

**신뢰도**: GitHub ⭐45,300, Microsoft 공식 레포 → 신뢰도 HIGH
**즉시 활용**: YES — 오픈소스, TTS/ASR 파이프라인 즉시 대체 가능
**6개월 영향력**: 장시간 음성 처리(60분 ASR, 90분 TTS) 표준화 가능성. [[VoxCPM2]]·[[silero-vad]] 대체 후보
**대체 관계**: [[VoxCPM]]·[[VoxCPM2-HF]] 대체, [[silero-vad]] 보완
**허와 실**: 3모델 구성이라 메모리 요구량 검토 필요. 실시간 TTS 0.5B는 경량
**액션**: 실시간 TTS(0.5B) 먼저 테스트, [[reat-voice]] 파이프라인 교체 검토

## 모델 구성

- TTS: 1.5B — 고품질 음성 합성, 90분 다화자 지원
- ASR: 7B — 60분 음성 단일 패스 인식
- 실시간 TTS: 0.5B — 저지연 경량 추론

## 관련 페이지
- [[VoxCPM2-HF]]
- [[silero-vad]]
- [[VibeVoice]]

## 원본
- 출처: https://github.com/microsoft/VibeVoice
- 신뢰도: ⭐⭐⭐ (⭐45,300, Microsoft 공식)
