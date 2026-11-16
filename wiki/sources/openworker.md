---
title: "andrewyng/openworker — 승인 게이트·감사 로그·샌드박스를 갖춘 로컬 우선 AI 데스크톱 코워커 + Harness SDK"
type: source
domain: ai-news
tags: [ai-news, github-trending, agent-harness, governance, sandbox, local-first]
created: 2026-11-16
updated: 2026-11-16
sources: [https://github.com/andrewyng/openworker]
reliability: medium
---

**레포**: [andrewyng/openworker](https://github.com/andrewyng/openworker) · ★**19,364**(볼트 11-16 실측) · fork 2,761 · Python · MIT · repo id 1306128367 · 생성 2026-07-20 · API description **비어 있음**. 같은 저자의 [[aisuite]] 가 앱 엔진 기반(수집기).

## 핵심 인사이트
> [!insight] 거버넌스 4단 — "자율성은 사다리로 올라가고, 바닥은 못 내린다"
> ① 어떤 모드로도 낮출 수 없는 **사람 전용 하드 플로어** ② 승인 → 상설 규칙 → allowlist 로 올라가는 자율성 사다리 ③ 승인 출처가 붙은 도구 호출 감사 로그 ④ [[OpenShell]] 컨테이너 샌드박스(세션 폴더만 · 키 없음 · 네트워크 allowlist). 무인 실행은 **자가 승인 없이 인박스 대기**. [[CopilotKit-OpenBot]] · [[LoopForge]] 와 같은 "게이트 우선" 계열이지만 개인 데스크톱 · 로컬 모델(Ollama · LM Studio · llama.cpp · vLLM) 쪽이다.

## 도메인별 추출 (ai-news)
- **신뢰도**: ★19,364 · 4개월 차 · 정량 벤치 0.
- **즉시 활용**: 부분 — **Harness SDK**(`@openworkerai/harness-sdk`, Rust 엔진 임베드: 루프 · 도구 호출 · 승인 · 스트리밍 · 세션 영속화)는 자체 하네스 설계 레퍼런스. 데스크톱 앱은 오픈 베타.
- **6개월 영향력**: 승인 정책을 "모드 스위치"가 아닌 **누적 규칙**으로 다루는 UX 가 Claude Code 류 권한 시스템과 수렴할 가능성.
- **대체 관계**: Claude Desktop/Cowork 류 상용 코워커의 오픈 대안. 커넥터 25+ · Slack `@OpenWorker` 위임 · 예약 작업(수집기).
- **허와 실**: 🔴 Windows 빌드 **코드 서명 안 됨**(README 29행 *"SmartScreen will warn; signing is in progress"*). "클라우드 구성요소는 OAuth 중개뿐"은 주장(미검증).
- **액션**: 하네스 설계 참고(승인 사다리 · 감사 로그 스키마). 설치는 보류.

## 관련 페이지
- [[aisuite]] · [[OpenShell]] · [[LoopForge]] · [[CopilotKit-OpenBot]] · [[하네스-설계-축]] · [[NVIDIA]] · [[에이전트-스킬]]

## 원본
- 출처: https://github.com/andrewyng/openworker
- 확인 범위: GitHub API 메타 · README 29행(볼트) · 🔴 거버넌스 4단 · SDK · 커넥터 서술은 수집기 판독 · 실행 미확인
- 신뢰도: ⭐⭐ (★1.9만 · 측정 0 · 미서명 빌드)
