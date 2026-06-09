---
title: supertone-inc/supertonic — ONNX 기반 온디바이스 경량 다국어 TTS
type: source
domain: ai-news
tags: [ai-news, local-llm, tts, onnx, on-device, edge-ai, multilingual, supertone]
created: 2026-05-16
updated: 2026-05-17
sources: []
reliability: high
---

# supertone-inc/supertonic

> [!insight] 핵심 인사이트
> ONNX 기반 온디바이스 경량 다국어 TTS 엔진. 저지연·고품질 음성 합성을 클라우드 없이 로컬에서 네이티브 실행. ⭐6,270(+719 당일) — Supertone은 한국 AI 음성 기술 선두 스타트업(Krafton 자회사)으로, 기업급 TTS 노하우를 오픈소스화했다는 점에서 신뢰도가 특히 높다.

**GitHub**: https://github.com/supertone-inc/supertonic — 스타 ⭐6,270 (+719 당일, 2026-05-16)
**HuggingFace (supertonic-3)**: https://huggingface.co/Supertone/supertonic-3 — 다운로드 20,200 (likes 331, 2026-05-17)
**신뢰도**: ⭐⭐⭐⭐

## 도메인별 추출 (ai-news + local-llm)

- **신뢰도**: ⭐⭐⭐⭐ — Supertone(Krafton 자회사, AI 음성 기술 전문 기업) 공식 오픈소스. ONNX 표준 포맷 = 플랫폼 이식성 보장
- **즉시 활용**: YES — ONNX Runtime 설치 후 바로 실행 가능. 별도 GPU 불필요 (CPU 추론 가능)
- **6개월 영향력**: [[VoxCPM]], [[VoxCPM2]], [[OmniVoice]] 등 TTS 경쟁 구도에서 **온디바이스 저지연** 포지셔닝으로 차별화. 모바일 앱·IoT·로봇 음성 인터페이스 표준 후보
- **대체 관계**: [[silero-vad]](VAD, 전처리 단계)와 파이프라인 연계 가능. [[OmniVoice]](1M+ 다운로드, 다국어 TTS)보다 경량·로컬 중심
- **허와 실**: "고품질"의 실제 MOS 점수 미공개. 다국어 지원 범위(특히 한국어 품질) 확인 필요
- **액션**: GitHub 클론 → 한국어 음성 합성 품질 테스트 → 지연시간 벤치마크 (목표: 200ms 이하)

> [!action] 당장 할 것
> Monday TTS 파이프라인 후보로 평가. [[silero-vad]] VAD + supertonic TTS 조합 테스트. 한국어 지원 품질 및 ONNX 추론 지연시간 측정.

> [!note] 배경 정보
> Supertone은 보이스 클로닝·AI 음성 합성 전문 기업으로, HYBE 등 엔터테인먼트 산업에 음성 AI 납품 이력 보유. 오픈소스 버전인 supertonic은 경량화 버전이나 기업 기술력 배경 보유.

## 관련 페이지
- [[VoxCPM]] — OpenBMB 오픈소스 TTS (토크나이저 없는 방식)
- [[VoxCPM2]] — OpenBMB 30개 언어 TTS + 음성 복제
- [[OmniVoice]] — 다국어 TTS HF 트렌딩
- [[silero-vad]] — 음성활성감지, TTS 파이프라인 전처리
- [[local-llm]] — 로컬/엣지 AI 도메인

## 원본
- GitHub: https://github.com/supertone-inc/supertonic — 스타 ⭐6,270 (+719 당일, 2026-05-16)
- HuggingFace (supertonic-3): https://huggingface.co/Supertone/supertonic-3 — 다운로드 20,200 (likes 331, 2026-05-17)
- 신뢰도: ⭐⭐⭐⭐ (Supertone, Krafton 자회사, AI 음성 전문 기업)
