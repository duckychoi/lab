---
title: altic-dev/FluidVoice — 로컬 온디바이스 macOS 음성 받아쓰기
type: source
domain: local-llm
tags: [ai-news, github-trending, stt, on-device, local-llm, macos, privacy, voice]
created: 2026-06-30
updated: 2026-07-01
sources: []
reliability: medium
---

# FluidVoice (altic-dev/FluidVoice)

> [!insight] 핵심 인사이트
> ⭐5,165 (2026-07-01, 당일 +588) ← ⭐4,623 (06-30). **인터넷 연결 없이 로컬에서 동작하는 macOS 음성→텍스트(STT) 받아쓰기 앱.** 온디바이스 STT로 *프라이버시 보장*이 강점 — 클라우드 STT API의 종량제·데이터 유출 우려를 피한다. [[voicebox]](로컬 음성 클로닝/생성)가 출력(TTS) 쪽 온디바이스라면, FluidVoice는 입력(STT) 쪽 온디바이스. [[local-llm]]의 "온디바이스로 프라이버시·비용 동시 해결" 흐름이 음성 인식 영역까지 확장된 사례.

## 도메인별 추출 (local-llm)

- **실용성 판단**: macOS 한정·로컬 실행 → Apple Silicon에서 즉시 배포 가능. 받아쓰기는 지연시간이 UX 핵심인데 온디바이스라 네트워크 왕복 제거가 유리.
- **메모리 아키텍처**: 해당 없음 — STT 모델(Whisper 계열 추정) 로컬 추론. 모델 백엔드 확인 필요.
- **Hermes 적용**: 직접 무관하나, 음성 코딩([[Claude-Code-워크플로우]]의 음성 입력)에 로컬 STT를 끼우면 프라이버시·오프라인 작동.
- **트레이드오프**: 온디바이스라 정확도(특히 한국어)·모델 크기 vs 프라이버시·오프라인의 교환. 클라우드 대비 정확도 격차 검증 필요.
- **오픈소스 구현체**: 본 레포 자체가 즉시 사용 가능한 macOS 앱.

> [!action] 당장 할 것
> Apple Silicon Mac에서 설치 → 한국어 받아쓰기 정확도·지연시간 측정. 합격 시 음성 코딩/메모 워크플로의 클라우드 STT 대체 후보.

> [!question] 미해결 질문
> STT 백엔드 모델(Whisper? 자체 모델?)과 한국어 정확도? Windows/Linux 지원 계획?

## 관련 페이지
- [[voicebox]]
- [[local-llm]]
- [[Claude-Code-워크플로우]]
- [[reat-voice]]

## 원본
- 출처: https://github.com/altic-dev/FluidVoice
- 스타: ⭐5,165 (2026-07-01, 당일 +588) ← ⭐4,623 (06-30)
- 신뢰도: ⭐⭐ (2일 연속 급등 신규 도구, 정확도·언어 지원 미검증)
