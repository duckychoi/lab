---
title: OpenWhispr — 로컬 STT 데스크톱 앱, 그리고 "런타임이 하드웨어를 버리면 기능이 사라진다" (⭐7,664)
type: source
domain: ai-news
tags: [ai-news, github-trending, stt, whisper, parakeet, on-device, privacy, electron, onnx]
created: 2026-09-07
updated: 2026-09-07
sources: []
reliability: high
---

# OpenWhispr — 프라이버시 우선 받아쓰기 앱

**GitHub**: https://github.com/OpenWhispr/openwhispr
**스타수**: **7,664** (2026-09-07 API 실측 · raw 표기 7,659 대비 **+5**)
**포크 941 · 이슈 335 · 워치 20 · 생성 2025-06-19 · 최종 push 2026-09-05 · 주 언어 JavaScript**
**라이선스**: **MIT** · 스택(README 실측): React 19 · TypeScript · Tailwind v4 · **Electron 41** · better-sqlite3 · **whisper.cpp** · **sherpa-onnx** · shadcn/ui

> [!insight] 핵심 인사이트
> README 첫 줄이 포지션을 직접 밝힌다 — *"**WisprFlow와 Granola의 오픈소스 무료 대안**."* 핫키를 누르고 말하면 **커서 위치에 텍스트가 꽂힌다.**
> 볼트가 [[openai-whisper]]·[[VoiceStudio]] 등에서 본 건 **엔진**이었다. 이건 **엔진을 일상 입력기로 감싼 제품**이다. 그리고 로컬(whisper.cpp/Parakeet)과 클라우드(BYOK)를 **사용자가 고른다** — 볼트의 [[local-llm]] 축에서 반복 관측된 *"로컬이냐 클라우드냐"* 를 **제품이 런타임 선택지로 노출**한 사례.
> 기능 범위가 받아쓰기를 넘는다: **회의 녹취**(Zoom·Teams·FaceTime 자동 감지 + 라이브 화자 분리 + 음성 지문 + 캘린더 연동)·**노트**(폴더·시맨틱 검색·AI 액션).

> [!warning] 이 소스의 진짜 교훈 — **의존 런타임이 아키텍처를 버리면 기능이 통째로 사라진다**
> README 각주(원문 실측): *"Intel Mac에서는 **라이브 화자 식별과 음성 지문을 쓸 수 없다**. ONNX Runtime에 의존하는데 [**1.24에서 macOS x86_64 바이너리 배포를 중단**](https://github.com/microsoft/onnxruntime/releases/tag/v1.24.1)했기 때문이다. 녹취와 전사는 정상 동작하고, **노트 검색은 시맨틱 검색 대신 키워드 매칭으로 폴백**한다."*
> raw 기재가 **정확**하며, 구조적으로 다음을 뜻한다:
> - **모델도 앱도 아닌 "런타임 배포 정책"이 최종 사용자 기능을 결정했다.** sherpa-onnx → ONNX Runtime → x86_64 바이너리 중단 → 화자 분리 소멸.
> - 볼트가 [[MiniMax-H3]] 에서 세운 *"오픈 가중치 ≠ 오픈 시스템"*, [[anthropics-skills]] 에서 본 *"레포 레벨 라이선스 ≠ 실제 라이선스"* 와 **같은 계열의 세 번째 변종**: **표면 지표(MIT·오픈소스·크로스플랫폼 배지)가 실제 가용 기능을 보증하지 않는다.**
> - README는 상단 배지에 `platform-macOS | Windows | Linux` 를 달고 **각주로 예외를 밝힌다**. 볼트 규칙상 **배지가 아니라 각주가 사실**이다.

> [!note] 폴백 설계 자체는 정직하다
> 기능이 빠질 때 **앱이 죽지 않고 키워드 검색으로 내려앉는다.** 그리고 그 사실을 README에 **먼저 적었다.** [[anthropics-skills]] 의 *"실제 동작은 다를 수 있다"*, [[VoiceStudio]] 의 *"646 언어, 단 실제 커버리지는 엔진에 달림"* 과 같은 **주장 약화형 정직성** 계열. 볼트가 이 계열을 관측한 **네 번째 사례**이며, 신뢰도 판정 시 **가점 요인**으로 취급한다.

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐⭐⭐⭐ — ⭐7,664 실측·MIT·활발한 push(09-05)·제약을 스스로 문서화. ⚠️ **오픈 이슈 335건**(포크 941 대비 높은 편)은 성숙도 신호로 유보.
- **즉시 활용**: **YES.** 크로스플랫폼 바이너리 배포 중이고 로컬 모드는 **오디오가 기기를 떠나지 않는다**. 볼트 운영자의 작업 흐름(받아쓰기 → 노트)에 바로 얹을 수 있다. ⚠️ **Apple Silicon / Windows / Linux 에서만 전 기능**.
- **6개월 영향력**: 받아쓰기가 **OS 입력기 층**으로 내려오면 "텍스트 입력"의 기본값이 바뀐다. 볼트 인제스트의 앞단(사람이 raw에 메모를 넣는 단계)을 음성으로 대체할 여지.
- **대체 관계**: **WisprFlow·Granola 직접 대체 표방**(README 명시). 엔진 층에서는 [[openai-whisper]]·NVIDIA Parakeet 을 **감싸는** 관계이지 대체가 아니다.
- **허와 실**: *"완전 프라이빗"* 은 **로컬 모델 선택 시에만** 참이다. BYOK 클라우드 모드를 쓰면 오디오는 나간다. README도 *"선택"* 이라고 적었지 *"항상 로컬"* 이라 하지 않았다 — **마케팅 문구(프라이버시 우선)와 실제 구성(선택형)의 간극**을 인용 시 유지할 것.
- **액션**: 아래.

> [!action] 당장 할 것
> 설치 전 **자기 하드웨어부터 확인**한다. Intel Mac이면 화자 분리·시맨틱 검색이 **없다**. Apple Silicon/Windows/Linux면 **로컬 Whisper(Metal/CUDA/Vulkan 가속)** 로 설정해 오디오 외부 전송을 끈 뒤 받아쓰기만 먼저 시험.

> [!question] 미해결
> **로컬 모드에서 "노트 AI 액션"과 "시맨틱 검색"이 어떤 모델을 쓰는가.** 임베딩 모델이 로컬인지 클라우드인지에 따라 *"오디오는 안 나가지만 텍스트는 나가는"* 구성이 될 수 있다. 프라이버시 주장의 실제 경계가 여기서 갈린다.

## 관련 페이지
- [[openai-whisper]] · [[VoiceStudio]] · [[pyannote-community-1]] · [[MiniMax-H3]] · [[anthropics-skills]] · [[NVIDIA]] · [[에이전트-메모리-레이어]] · [[open-science]] · [[LLM-Wiki]]

## 원본
- 출처: https://github.com/OpenWhispr/openwhispr
- 수집: 2026-09-07 자동수집 (ai-news)
- 검증: GitHub API 실측 + README 원문 대조(Intel Mac 각주 포함) (2026-09-07)
- 신뢰도: ⭐⭐⭐⭐
