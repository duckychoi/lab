---
title: pocket-tts — CPU 2코어로 도는 100M 로컬 TTS
type: source
domain: ai-news
tags: [ai-news, github-trending, tts, local-first, cpu, on-device, voice-cloning, kyutai]
created: 2026-07-08
updated: 2026-07-08
sources: []
reliability: high
---

# kyutai-labs/pocket-tts (GitHub ⭐6,432)

**GitHub**: https://github.com/kyutai-labs/pocket-tts
**스타수**: 6,432 (2026-07-08 기준, 당일 +531) · 포크 662
**라이선스**: MIT · **제작**: [[kyutai-labs]] · **스택**: Python 3.10–3.14 + PyTorch 2.5+ (CPU 전용, GPU PyTorch 불필요)

> [!insight] 핵심 인사이트
> **GPU·웹 API 없이 CPU 2코어만으로 도는 1억(100M) 파라미터 TTS**. M4 맥북에어 기준 실시간 6배 속도, **첫 청크 200ms 지연**, 음성 클로닝 + 6개 언어(영·불·독·포·이·스). 핵심 가치는 "**진짜로 온디바이스에서 끝나는 음성 합성**" — [[speech-to-speech]]가 로컬 음성 파이프의 큰 그림이라면, pocket-tts는 그중 TTS 단을 **초경량·무GPU로 극단 최적화**한 조각. [[reat-voice]](ElevenLabs 클라우드·유료)의 로컬 무과금 대안이며, [[VibeVoice]]/[[VoxCPM2]] 같은 대형 음성 모델과 달리 "작고 빠르고 어디서나 돈다"는 축으로 차별화. [[kyutai-labs]]는 Moshi 계열 실시간 음성으로 검증된 랩이라 신뢰도 높음.

## 도메인별 추출 (ai-news / local-llm 교차)

- **신뢰도**: ⭐⭐⭐⭐ (⭐6,432 당일 +531, MIT, README WebFetch 실측 — CPU 2코어·200ms·6x·6언어 확인 / kyutai 트랙레코드)
- **즉시 활용**: YES — 내 나레이션/자막 음성을 **완전 로컬·무과금**으로 생성. 특히 GPU 없는 서버·엣지에서도 도는 점이 강점. reat-voice의 로컬 폴백 후보 1순위.
- **6개월 영향력**: "TTS는 클라우드 API"라는 전제 붕괴. 실시간 6배·200ms면 대화형 에이전트 음성 출력을 로컬에서 실용화 가능.
- **대체 관계**: [[reat-voice]](클라우드 TTS)를 로컬로 대체·보완. 품질은 대형 모델 대비 낮을 수 있으나 지연·비용·프라이버시에서 압도.
- **트레이드오프**: 100M 초경량 = 표현력·감정·자연스러움은 수십억 파라미터 모델 대비 제한. 실측 비교 필요.
- **액션**: pip 설치 → 내 나레이션 대본 1건을 pocket-tts vs reat-voice(ElevenLabs)로 생성해 지연·품질·비용 3축 비교.

## 관련 페이지
- [[kyutai-labs]] — 제작사 (Moshi 실시간 음성 계열)
- [[speech-to-speech]] — 로컬 음성 파이프 (VAD→STT→LLM→TTS)
- [[reat-voice]] — 클라우드 TTS 스킬 (대체 대상)
- [[VibeVoice]] · [[VoxCPM2]] — 대형 음성 생성 모델 (대조군)
- [[ai-news]]

## 원본
- 출처: https://github.com/kyutai-labs/pocket-tts
- GitHub: ⭐6,432 (2026-07-08, 당일 +531), MIT, 포크 662
- 성능: CPU 2코어 · M4 맥북에어 실시간 6배 · 첫 청크 ~200ms · 6개 언어 · 음성 클로닝
- 신뢰도: ⭐⭐⭐⭐ (라이브 스타·README WebFetch 실측 / kyutai 트랙레코드)
