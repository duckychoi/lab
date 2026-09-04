---
title: Magnitude — 하드웨어를 프로파일링해 로컬 모델을 골라 주는 추론 서버 (⭐2,106)
type: source
domain: local-llm
tags: [local-llm, ai-news, github-trending, inference-server, on-device, agent-harness, ollama-alt]
created: 2026-09-04
updated: 2026-09-04
sources: []
reliability: medium
---

# magnitudedev/magnitude — "에이전트가 추측하지 않게" 만드는 층

**GitHub**: https://github.com/magnitudedev/magnitude
**스타수**: **2,106** (2026-09-04 API 실측 · raw 2,105 대비 **+1**)
**포크 150 · 이슈 15 · 워치 13 · 라이선스 **Apache-2.0** · 생성 **2026-06-12**(약 3개월) · 최종 push 2026-09-03
**당일 +161 — 스타 대비 상승률 8.3%로 배치 최고**

> [!insight] 핵심 인사이트
> Ollama류와의 차이를 레포가 직접 FAQ로 답했고, 그 답이 이 소스의 전부다 — *"에이전트에게 Ollama를 깔라고 시키면 **에이전트는 추측한다.** 네 하드웨어도, 어떤 양자화가 맞는지도, 얼마나 빠를지도 모른다."* Magnitude는 칩·메모리·대역폭을 **프로파일링**해 **예상 tok/s가 계산된 카탈로그**를 에이전트에게 준다. 즉 이 도구가 파는 건 추론 속도가 아니라 **모델 선택에 필요한 근거**다. 볼트의 [[local-llm]] 축이 5개월간 *"어떤 모델이 좋은가"* 를 물어 온 데 반해, 이건 ***"내 기계에서 무엇이 도는가"* 를 자동으로 답하는 첫 도구**다.

> [!action] 당장 할 것 — 이 배치 최우선
> ```
> npm i -g @magnitudedev/cli && magnitude setup
> ```
> 목적은 설치가 아니라 **프로파일 결과 확보**다. 볼트에는 [[Gemma-4-31B]]·[[Gemma-4-26B]]·[[Gemma-4-E4B]]·[[Qwen3.8-27B]]·[[VoxCPM]] 등 *"로컬에서 돌려보자"* actionable이 **최소 5건 대기 중**인데, 전부 **이 기계에서 실제로 도는지 모른 채** 쌓여 있다. `magnitude setup` 한 번이면 **그 5건을 한꺼번에 판정**한다 — 돌릴 수 없는 항목은 대기열에서 빼야 한다.

## 구조 (README 실측)

- **연결되는 하네스**: Pi · OpenCode · **Hermes** · OpenClaw · Codex · **Claude Code** · Oh My Pi · Cline — 또는 내장 하네스
- **온보딩이 에이전트 경유**: 사람이 아니라 *에이전트에게* `magnitude docs onboarding` 을 시키면, 에이전트가 프로파일링→추천→다운로드→**자기 설정 파일을 새 모델로 교체**까지 수행
- **런타임**: 요청 시 모델 로드, 유휴/메모리 압박 시 언로드. 투기적 디코딩(speculative decoding)·동시성 자동 튜닝
- **플랫폼**: macOS·Linux, Windows는 WSL

> [!warning] 신뢰도 medium — 수치가 하나도 없다
> ⭐2,106 · **생성 3개월** · **워치 13 · 포크 150**. README는 *"free / private / offline / tuned end to end"* 를 나열하지만 **벤치마크·tok/s 실측·지원 모델 목록·양자화 정책이 전부 없다.** *"best local models for your hardware"* 의 **"best"를 무엇으로 정하는지가 미공개**다 — 이 도구의 유일한 판매점이 바로 그 선택 로직인데도. 볼트 규칙(*"근거 없는 우위 주장은 마케팅"*) 적용 대상. **이슈 15건·워치 13은 실사용 표본이 아직 얇다는 뜻**이므로, 설치는 하되 **파이프라인 의존은 금지**.

## 도메인별 추출 (local-llm)

- **실용성 판단**: **설치는 즉시 가능**(npm, Apache-2.0). 다만 *실배포* 판단은 프로파일 결과를 봐야 함. 지연시간 수치 **레포에 없음**.
- **메모리 아키텍처**: 해당 없음 — 이건 모델이 아니라 **서빙·오케스트레이션 층**이다. 다만 *유휴 시 언로드 / 요청 시 로드* 는 [[에이전트-메모리-레이어]]의 **모델 상주 비용 문제**를 다루는 방식.
- **Hermes 적용**: **README가 Hermes를 명시적으로 지원 하네스에 넣었다.** 볼트의 오래된 대기 항목 *"hermes-agent 검토"* 와 직접 연결 — [[hermes-agent]]를 로컬 모델로 돌리는 **경로가 생겼다**.
- **트레이드오프**: 토큰 비용 0 · 완전 오프라인 vs **품질은 하드웨어 상한에 묶임**. 정량치 없음.
- **오픈소스 구현체**: 본체가 Apache-2.0 오픈소스. `@magnitudedev/cli`.

## 관련 페이지
- [[hermes-agent]] · [[에이전트-메모리-레이어]] · [[AI-에이전트-프레임워크]] · [[Claude-Code-워크플로우]] · [[Gemma-4-31B]] · [[Qwen3.8-27B]] · [[LMCache]] · [[Random-Attention]] · [[Compile-by-Training]] · [[NousResearch]]

## 원본
- 출처: https://github.com/magnitudedev/magnitude
- 문서: https://docs.magnitude.dev/
- 수집: 2026-09-04 자동수집 (raw 도메인 ai-news → **local-llm 로 재분류**: 내용이 로컬 추론 서버이므로)
- 검증: README defuddle 원문 + GitHub API 실측 (2026-09-04)
- 신뢰도: ⭐⭐ (medium — 규모 작음·수치 부재)
