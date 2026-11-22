---
title: "janhq/jan — 오프라인 로컬 LLM 데스크톱 앱 (★46k · OpenAI 호환 localhost:1337 · MCP) — 급상승이 아니라 3년 된 성숙 프로젝트"
type: source
domain: local-llm
tags: [local-llm, github-trending, desktop-app, on-device, openai-compatible, mcp, tauri]
created: 2026-11-22
updated: 2026-11-22
sources: [https://github.com/janhq/jan]
reliability: high
---

**GitHub**: ★46,011(볼트 API 11-22 · 수집기 11-21 45,975 · 당일 +101) · Rust(Tauri) · GitHub 표기 NOASSERTION(수집기가 LICENSE 본문에서 Apache-2.0 확인) · 생성 2023-08-17

## 핵심 인사이트
> [!insight] 로컬 모델 GUI + API 서버 + 클라우드 연결을 한 앱에
> HuggingFace 의 Llama · Gemma · Qwen 등을 내려받아 로컬 실행, OpenAI · Anthropic · Mistral · Groq · MiniMax 클라우드 연결, `localhost:1337` OpenAI 호환 로컬 API, MCP 연동, 커스텀 어시스턴트. 수집기 스스로 적었듯 **스타 총량 기준 통과분**이지 신작이 아니다.

## 도메인별 추출 (local-llm)
- **실용성 판단**: Windows/macOS/Linux 실배포 가능. README 에 성능 수치 0 — 속도는 내부 런타임과 모델에 달렸다.
- **메모리 아키텍처**: 해당 없음(앱).
- **Hermes 적용**: ChinameBot 은 서버형이라 GUI 앱 이점 적음. `localhost:1337` 호환 API 만 쓸 거면 더 가벼운 서버가 있다.
- **트레이드오프**: 편의(설치 한 번) vs 추론 엔진 선택 자유도.
- **오픈소스 구현체**: 본 레포.

## 관련 페이지
- [[omlx]] · [[openvino]] · [[splash]] (같은 배치 · Mac 전용 엔진) · [[local-llm]]

## 원본
- 출처: https://github.com/janhq/jan
- 확인 범위: GitHub API(스타 · 언어 · 라이선스 표기 · 생성일) · 🔴 README · LICENSE 본문은 수집기 판독
- 신뢰도: ⭐⭐⭐⭐ (★46k · 3년)
