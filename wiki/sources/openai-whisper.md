---
title: openai/whisper — 대규모 약지도 학습 기반 범용 음성 인식 모델
type: source
domain: ai-news
tags: [ai-news, github-trending, openai, whisper, asr, speech-recognition, open-source, multilingual, tts-pipeline]
created: 2026-06-07
updated: 2026-06-07
sources: []
reliability: high
---

# openai/whisper (GitHub ⭐101,966)

> [!insight] 핵심 인사이트
> GitHub ⭐10만 돌파 — 음성 인식 오픈소스 중 사실상 업계 표준. 100개 언어 전사·번역 동시 수행, 약지도 학습으로 범용성 확보. 지금도 STT 파이프라인 기본 선택지.

## 핵심 인사이트

> [!action] 당장 할 것
> [[reat-voice]] 스킬의 STT 단계에서 Whisper 직접 활용 가능. ElevenLabs 없이 로컬 음성 인식 파이프라인 구성 검토.

> [!note] 배경 정보
> 2022년 OpenAI가 공개한 자동 음성 인식(ASR) 모델. 약 68만 시간의 다국어 데이터로 약지도 학습(weakly supervised). Tiny(39M)~Large-v3(1.55B)까지 5종 사이즈 제공. GGML/Faster-Whisper 등 경량화 버전으로 엣지 실행 가능.

> [!note] 지속적 스타 증가
> 오늘 +150 — 꾸준한 관심 유지 확인. 신규 모델이 아님에도 여전히 트렌딩 상위.

## 도메인별 추출 (ai-news 템플릿)

- **신뢰도**: ⭐⭐⭐⭐⭐ — OpenAI 공식, ⭐101,966, 수천 개 downstream 레포
- **즉시 활용**: YES — `pip install openai-whisper` 즉시 실행, GPU 없이도 tiny/base 모델 동작
- **6개월 영향력**: 여전히 STT 파이프라인 기본값. faster-whisper, WhisperX 파생 생태계가 활발하므로 직접 대체 가능성 낮음
- **대체 관계**: [[VibeVoice]], [[VoxCPM]]이 합성(TTS) 측면에서 경쟁. 인식(ASR) 측면에선 whisper.cpp, faster-whisper가 경량화 대안
- **허와 실**: 번역 품질은 언어·억양에 따라 편차 큼. hallucination 이슈(무음 구간에서 가짜 텍스트 생성) 주의
- **액션**: faster-whisper 또는 whisper.cpp로 로컬 STT 파이프라인 구성 검토

## 관련 페이지

- [[VibeVoice]] — Microsoft STT/TTS 통합 플랫폼
- [[VoxCPM]] — 토크나이저 없는 오픈소스 TTS
- [[음성-합성]]

## 원본

- 출처: https://github.com/openai/whisper
- 신뢰도: ⭐⭐⭐⭐⭐ (OpenAI 공식 GitHub 101,966 스타)
