---
title: modelscope/FunASR — 산업급 음성인식 툴킷 (170배 실시간, 50개+ 언어)
type: source
domain: ai-news
tags: [ai-news, github-trending, ASR, speech, TTS, streaming, diarization, modelscope, alibaba]
created: 2026-05-28
updated: 2026-06-04
sources: []
reliability: high
---

# modelscope/FunASR — 산업급 음성인식 툴킷

## 핵심 인사이트

> [!insight] 핵심 인사이트
> 실시간 대비 170배 속도의 음성인식 + 50개 이상 언어 + 화자 분리 + 감정 감지를 단일 툴킷으로 제공. OpenAI Whisper API 호환 인터페이스까지 갖춰 기존 파이프라인 드롭인 교체 가능. ⭐16,381.

## 도메인별 추출 (ai-news 템플릿)

- **신뢰도**: ⭐⭐⭐⭐⭐ — ⭐16,381, Alibaba ModelScope 공식 지원, 산업 배포 검증
- **즉시 활용**: YES — pip install funasr 후 Python API 또는 OpenAI 호환 서버로 바로 사용
- **6개월 영향력**: [[VibeVoice]]·[[VoxCPM2]] 등 TTS와 결합하면 완전한 음성 파이프라인 구성. 영상 자동화([[Pixelle-Video]])의 자막·자동화에 ASR 레이어로 투입 가능
- **대체 관계**: Whisper(OpenAI) 대비 속도 170x 우위, 화자 분리 내장, 스트리밍 지원. [[VibeVoice]] STT와 기능 겹침 — 언어 커버리지/산업 안정성 면에서 FunASR 우위
- **허와 실**: 170배 속도는 GPU 환경 기준. CPU 환경에서의 실측 지연시간 확인 필요. 한국어 지원 품질 검증 요
- **액션**: 설치 + 한국어 음성 파일로 WER 테스트. Whisper 대비 성능 비교

## 주요 기능

- **실시간 ASR**: 실시간 대비 170x 속도 (비스트리밍 배치 기준)
- **다언어**: 50개+ 언어 지원 (한국어 포함)
- **화자 분리 (Speaker Diarization)**: 다화자 식별
- **감정 감지**: 발화 감정 분류
- **스트리밍**: 실시간 저지연 스트리밍 ASR
- **OpenAI 호환 API**: Whisper API 드롭인 대체

## 관련 페이지

- [[VibeVoice]] — Microsoft STT/TTS, 다화자 음성 처리
- [[VoxCPM2]] — OpenBMB 다국어 TTS
- [[silero-vad]] — 음성활성감지 전처리, FunASR 파이프라인 앞단에 조합
- [[Pixelle-Video]] — 영상 자동화, ASR 통합 가능

## 원본

- 출처: https://github.com/modelscope/FunASR
- 스타: 16,381 (2026-05-28 기준)
- 언어: Python
- 신뢰도: ⭐⭐⭐⭐⭐
