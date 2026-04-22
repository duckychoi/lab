---
title: OpenBMB/VoxCPM — 토크나이저 없는 오픈소스 TTS 모델
type: source
domain: ai-news
tags: [ai-news, github-trending, tts, voice-cloning, multilingual, tokenizer-free, openBMB]
created: 2026-04-10
updated: 2026-04-14
sources: []
reliability: high
---

# OpenBMB/VoxCPM

> [!insight] 핵심 인사이트
> 토크나이저(Tokenizer) 없이 직접 음성을 처리하는 새로운 TTS 아키텍처. 다국어 합성 + 스타일 전이 + 실제 음성 클로닝까지 하나의 모델로 처리. 스타 12,600개(2026-04-14, +1,178 today). 30개 언어 지원·48kHz 품질·RTF 0.13 실시간 처리. Apache-2.0.

## 핵심 인사이트

> [!action] 당장 할 것
> `/reat-voice` 스킬의 ElevenLabs 대체 오픈소스 후보로 검토. 로컬 배포 가능 여부 확인.

> [!note] 배경 정보
> OpenBMB(Open Big Model Benchmark)는 CPM 시리즈(Chinese Pretrained Model)로 유명. VoxCPM은 텍스트 도메인의 CPM 철학을 음성으로 확장한 것.

> [!question] 미해결 질문
> 한국어 지원 수준? 실시간(스트리밍) TTS 가능? GPU 요구사항? ElevenLabs 대비 음질?

## 도메인별 추출 (ai-news 템플릿)

- **신뢰도**: ⭐⭐⭐ — 스타 14,227개, OpenBMB 연구팀 신뢰도 높음
- **즉시 활용**: YES — reat-voice 파이프라인 ElevenLabs 비용 절감 후보
- **6개월 영향력**: TTS API 비용 0으로 만드는 경쟁 압력. ElevenLabs 포지셔닝 위협
- **대체 관계**: ElevenLabs / OpenAI TTS 대체 오픈소스 후보
- **허와 실**: "토크나이저 없음"이 실제 음질·속도 이점으로 이어지는지 검증 필요
- **액션**: 로컬 설치 + 한국어 음성 품질 테스트

## 관련 페이지

- [[TTS-오픈소스]]
- [[reat-voice]]

## 원본

- 출처: https://github.com/OpenBMB/VoxCPM
- 스타: 14,227 (2026-04-10 기준, +496 당일)
- 신뢰도: ⭐⭐⭐
