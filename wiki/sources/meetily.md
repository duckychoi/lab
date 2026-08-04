---
title: meetily — 100% 로컬 AI 회의록 어시스턴트 (Rust/Tauri)
type: source
domain: ai-news
tags: [ai-news, github-trending, local-first, transcription, whisper, parakeet, ollama, meeting-notes, privacy]
created: 2026-07-07
updated: 2026-07-07
sources: []
reliability: high
---

# Zackriya-Solutions/meetily (GitHub ⭐19,911)

**GitHub**: https://github.com/Zackriya-Solutions/meetily
**스타수**: 19,911 (2026-07-07 기준, 당일 +2,494 급상승)
**라이선스**: MIT · **스택**: Rust(백엔드) + Next.js/TypeScript(프론트) + Tauri(데스크톱)

> [!insight] 핵심 인사이트
> 회의 오디오를 **클라우드 없이 100% 로컬**로 실시간 전사(Whisper/Parakeet) → 요약(Ollama/Claude/Groq/OpenRouter 선택)까지 처리하는 데스크톱 앱. 핵심 가치는 "**프라이버시 우선 회의록**" — 민감한 내부 회의를 외부 API에 흘리지 않고 온디바이스에서 끝냄. Apple Silicon·NVIDIA CUDA·AMD/Intel Vulkan 하드웨어 가속 지원으로 실사용 성능 확보. 당일 +2,494 급상승은 "로컬 우선 생산성 도구" 수요가 실재함을 보여줌 — [[speech-to-speech]](로컬 음성 파이프)의 회의 특화 응용판.

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐⭐⭐⭐ (⭐19,911 당일 +2,494, MIT, README 실측 확인)
- **즉시 활용**: 부분 YES — 내 회의/인터뷰 기록을 로컬에서 전사·요약해 위키 raw.md로 넣는 파이프라인에 응용 가능. Parakeet(NVIDIA) 실시간 전사는 [[VibeVoice]]/[[StepAudio-2.5]] 계열 음성 스택과 대조 대상.
- **6개월 영향력**: "회의 요약 SaaS(Otter/Fireflies)"의 로컬 대체. 데이터 주권 요구가 큰 조직에서 채택 압력. 화자 분리(diarization)는 PRO 예정으로 아직 미완.
- **대체 관계**: 클라우드 회의록 SaaS를 로컬로 대체. 요약 백엔드로 Ollama뿐 아니라 Claude/Groq/OpenRouter도 붙일 수 있어 하이브리드 가능.
- **허와 실**: 마케팅 걷어내면 = Whisper 전사 + LLM 요약을 Tauri로 깔끔히 묶은 로컬 앱. 화자 분리는 "planned"(미구현)이라 회의록 완성도는 아직 제한적.
- **액션**: macOS/Linux 빌드 설치 → 내 인터뷰 녹음 1건으로 로컬 전사→요약 품질 테스트, down-analysis 대비 정확도 비교.

## 관련 페이지
- [[speech-to-speech]] — 로컬 음성 VAD→STT→LLM→TTS 파이프
- [[VibeVoice]] — 음성 생성 스택
- [[down-analysis]] — 영상/음성 트랜스크립트 분석 스킬 (대조군)
- [[firecrawl]] — 로컬/셀프호스트 데이터 수집 계열
- [[ai-news]]

## 원본
- 출처: https://github.com/Zackriya-Solutions/meetily
- GitHub: ⭐19,911 (2026-07-07, 당일 +2,494), MIT
- 스택: Rust 46% + TypeScript 30% + C++ 10% / Tauri 데스크톱 (macOS·Windows·Linux)
- 신뢰도: ⭐⭐⭐⭐ (라이브 스타 급상승, README 실측 / 화자분리 미구현 감안)
