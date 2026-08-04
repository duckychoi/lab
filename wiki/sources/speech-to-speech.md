---
title: speech-to-speech — 오픈소스 로컬 음성 에이전트 파이프라인 (HF)
type: source
domain: local-llm
tags: [ai-news, local-llm, github-trending, voice-agent, tts, stt, realtime-api, huggingface]
created: 2026-07-06
updated: 2026-08-01
sources: []
reliability: high
---

# huggingface/speech-to-speech (GitHub ⭐9,955)

> [!update] 2026-08-01 갱신 — ⭐9,955 (당일 +1,275, 당일 급상승 최상위·1만 목전)
> ⭐**9,955**(2026-08-01 자동수집, 당일 +1,275 — 이날 GitHub 급상승 1위) ← 9,425(07-31). 하루 새 +530, **1만 목전**. 로컬 음성 에이전트(VAD→STT→LLM→TTS)·OpenAI Realtime 호환 성격 동일 — 수요 견인 지속. [[VibeVoice]]·[[airi]]와 로컬 음성 스택 동반 급성장, [[reat-voice]] 대체 후보 묶음 평가 유지. *raw 자동수집 수치 반영 — GitHub 실WebFetch 미수행(타임라인 유지).*

> [!update] 2026-07-31 갱신 — ⭐9,425 (당일 +628, 급상승 지속·WebFetch "9.4k"·Apache-2.0 실확인)
> ⭐**9,425**(2026-07-31 자동수집, 당일 +628) ← 8,141(07-30). 이틀 새 +1,284로 급상승 유지 — 로컬 음성 에이전트(VAD→STT→LLM→TTS) 수요 견인. **WebFetch 재확인: 9.4k·Python·Apache-2.0**, OpenAI Realtime 호환 WebSocket으로 로컬 스택 스왑 가능한 성격 동일. [[VibeVoice]]·[[airi]]와 로컬 음성 스택 동반 급성장 — [[reat-voice]] 대체 후보 묶음 평가 actionable 유지.

> [!update] 2026-07-30 갱신 — ⭐8,141 (당일 +827, 급상승)
> ⭐**8,141**(2026-07-30 자동수집·API 실검증, 당일 +827 급상승, Apache-2.0) ← 6,530(07-27). 사흘 새 +1,611로 재가속 — 로컬 음성 에이전트(STT→LLM→TTS) 수요 견인. 같은 배치 [[VibeVoice]](⭐51,534) TTS·[[airi]] 컴패니언과 함께 **로컬 음성 스택** 동반 성장.

**GitHub**: https://github.com/huggingface/speech-to-speech
**스타수**: 6,530 (2026-07-27, 당일 +81) ← 6,089 (07-12, +94) ← 5,401 (07-06, +78) / Python / Apache 2.0

> [!insight] 핵심 인사이트
> HuggingFace 공식 **저지연·완전 모듈형 음성 에이전트 파이프라인** — `VAD → STT → LLM → TTS`를 **OpenAI Realtime 호환 WebSocket API**로 노출. 결정적 설계는 "**엔드포인트만 바꾸면 호스티드 OpenAI ↔ 자체 로컬 스택 스왑**" — LLM 슬롯이 OpenAI 호환 프로토콜을 말하므로 vLLM/llama.cpp 서버로 가리키면 *완전 로컬·완전 오픈* 음성 에이전트 완성. 실제로 수천 대 **Reachy Mini** 로봇의 대화 백엔드로 프로덕션 가동 중 — 데모가 아니라 실배포 검증.

## 핵심 인사이트

> [!note] 기본 로컬 스택 (README 실측)
> - **STT**: Parakeet TDT (로컬)
> - **TTS**: Qwen3-TTS (로컬)
> - **LLM**: OpenAI 호환 — HF Inference Providers / vLLM / llama.cpp 중 선택. 예시로 **[[Gemma-4-31B]] 계열 gemma-4-E4B-it-GGUF를 llama.cpp로** 서빙
> - 서버: `ws://localhost:8765/v1/realtime`, 모든 OpenAI Realtime 클라이언트 연결 가능
> - 라이선스 **Apache 2.0**, `pip install speech-to-speech` 즉시 실행

> [!action] reat-voice / 로컬 음성 스택에 직결
> 내 [[reat-voice]]는 ElevenLabs TTS(클라우드·유료) 의존. speech-to-speech는 Qwen3-TTS+Parakeet+로컬 LLM으로 **완전 로컬·무과금 음성 파이프라인** 대안 제시 — 자막·나레이션 생성을 로컬로 내리는 실험 후보. OpenAI Realtime 호환이라 클라이언트 재사용 가능.

## 도메인별 추출 (local-llm)

- **실용성 판단**: 실배포 검증됨(Reachy Mini 수천 대). Parakeet+Qwen3-TTS+소형 Gemma는 상위 로컬 머신/단일 GPU에서 저지연 대화 가능. 엣지는 모델 크기 선택에 달림.
- **메모리 아키텍처**: 파이프라인형(각 컴포넌트 스왑), 상태는 LLM 컨텍스트에 의존. RAG/메모리는 별도 결합 필요.
- **Hermes 적용**: LLM 슬롯에 로컬 에이전트 모델을 꽂아 음성 인터페이스화 가능 — ChinameBot류 음성화 경로.
- **트레이드오프**: 완전 로컬(무과금·프라이버시) vs 클라우드 TTS 품질/지연. 실시간성 위해 배치-1 저지연 서빙 필요.
- **오픈소스 구현체**: 그 자체가 즉시 사용 가능한 pip 패키지. llama.cpp/vLLM 백엔드 자유.

## 관련 페이지
- [[reat-voice]] — 내 TTS 스킬 (클라우드→로컬 대안)
- [[Gemma-4-31B]] — 예시 로컬 LLM 백엔드
- [[Qwen3.6-35B-A3B]] — 로컬 LLM 후보
- [[Embodied-cpp]] — 로봇 온디바이스 런타임 (같은 로컬·엣지 축)
- [[local-llm]]

## 원본
- 출처: https://github.com/huggingface/speech-to-speech
- GitHub: ⭐**9,955** (2026-08-01 자동수집, 당일 +1,275·급상승 1위) ← 9,425(07-31) ← 8,141(07-30) ← 6,530(07-27) ← 5,401 (2026-07-06), Apache 2.0
- 스택: VAD→STT(Parakeet TDT)→LLM(OpenAI 호환)→TTS(Qwen3-TTS), OpenAI Realtime WS API
- 검증: Reachy Mini 로봇 수천 대 프로덕션 백엔드
- 신뢰도: ⭐⭐⭐⭐⭐ (HF 공식, 실배포 검증, README 실측)
