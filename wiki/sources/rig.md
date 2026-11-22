---
title: "0xPlaygrounds/rig — Rust LLM 라이브러리 + Bevy 플러그인형 터미널 코딩 에이전트 (★9.2k · MIT)"
type: source
domain: ai-news
tags: [ai-news, github-trending, rust, llm-library, coding-agent, wasm, opentelemetry]
created: 2026-11-22
updated: 2026-11-22
sources: [https://github.com/0xPlaygrounds/rig]
reliability: medium
---

**GitHub**: ★9,218(볼트 API 11-22 · 수집기 일치) · Rust · MIT · 생성 2024-06-05 · push 2026-11-22

## 핵심 인사이트
> [!insight] 라이브러리가 코딩 에이전트를 "자기 위에" 지었다
> 라이브러리: 20+ 모델 프로바이더와 10여 개 벡터 스토어를 단일 인터페이스로, 툴 사용 에이전트 · 스트리밍 · 타입 훅, 임베딩 · 전사 · 오디오 · 이미지 모델, OpenTelemetry GenAI 규약, `rig-core`/`rig-agent` 는 브라우저 WASM 빌드 가능. 최근 `cargo install rig` 로 터미널 코딩 에이전트 배포 — 툴 · 명령 · 세션 · 로그인 · 화면이 전부 Bevy 플러그인이라 교체 가능, `/reload` 로 세션 유지한 채 재빌드.

## 도메인별 추출 (ai-news)
- **신뢰도**: ⭐⭐⭐ — ★9.2k · 2년 · MIT. 코딩 에이전트는 신생, 측정 0.
- **즉시 활용**: NO — 볼트 사용자 스택에 Rust 서비스 없음.
- **6개월 영향력**: 에이전트 하네스를 플러그인 조립으로 만드는 방식([[하네스-설계-축]])의 Rust 사례.
- **대체 관계**: TS 는 [[mastra]], 최소형은 [[mini-swe-agent]].
- **허와 실**: Rust 1.97.1+ · Linux/macOS 전용 · 첫 실행 빌드 수 분.
- **액션**: 없음.

## 관련 페이지
- [[mastra]] · [[mini-swe-agent]] · [[rtk]] (같은 Rust 생태계) · [[하네스-설계-축]] · [[AI-에이전트-프레임워크]]

## 원본
- 출처: https://github.com/0xPlaygrounds/rig
- 확인 범위: GitHub API(스타 · 언어 · MIT · 생성일 · push) · 🔴 README 내용은 수집기 판독
- 신뢰도: ⭐⭐⭐
