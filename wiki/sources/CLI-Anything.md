---
title: CLI-Anything — 모든 소프트웨어를 에이전트 네이티브로 전환하는 CLI 프레임워크
type: source
domain: ai-news
tags: [ai-news, agent, cli, framework, agent-native, HKUDS]
created: 2026-05-19
updated: 2026-05-20
sources: []
reliability: high
---

# CLI-Anything — 모든 소프트웨어를 에이전트 네이티브로 전환하는 CLI 프레임워크

## 핵심 인사이트

> [!insight] 핵심 인사이트
> HKUDS(홍콩대 데이터 과학 연구소)가 개발한 CLI-Hub 기반 범용 에이전트 인터페이스 프레임워크. 기존 CLI 소프트웨어를 수정 없이 AI 에이전트가 사용할 수 있도록 래핑 — "AI 에이전트 네이티브"로의 전환 비용을 극단적으로 낮추는 접근.

## 도메인별 추출 (ai-news)

- **신뢰도**: GitHub ⭐38,098 (+1,038 오늘, 2026-05-20; 이전 ⭐37,137), HKUDS(RAG-Anything 개발 그룹) — 신뢰할 수 있는 연구 기관
- **즉시 활용**: YES — 기존 CLI 도구를 에이전트 워크플로우에 통합할 때 즉시 적용 가능. 특정 LLM 종속 없음
- **6개월 영향력**: [[chrome-devtools-mcp]](브라우저 제어 MCP)·[[n8n-mcp]](n8n 워크플로우 MCP)와 함께 "기존 소프트웨어 에이전트화" 패턴의 핵심 인프라 후보. 에이전트가 임의 CLI 도구를 사용할 수 있으면 컴퓨터 사용(Computer-Use) 에이전트의 범용성이 폭발적으로 확장됨
- **대체 관계**: [[trycua-cua]](GUI 에이전트 인프라) 대비 CLI 레이어 특화. 보완 관계
- **허와 실**: 복잡한 인터랙티브 CLI(vim, htop 등)에서의 동작 안정성 검증 필요
- **액션**: [[Claude-Code-워크플로우]] 내 CLI 도구 자동화에 통합 테스트. [[RAG-Anything]] + CLI-Anything 연동 파이프라인 구성 가능성 확인

## 관련 페이지

- [[AI-에이전트-프레임워크]] — 에이전트 프레임워크 전체 지형도
- [[RAG-Anything]] — HKUDS 동일 그룹의 멀티모달 RAG 프레임워크
- [[chrome-devtools-mcp]] — Chrome DevTools 공식 MCP (브라우저 제어)
- [[n8n-mcp]] — n8n 워크플로우 MCP 브리지
- [[trycua-cua]] — GUI 에이전트 샌드박스·SDK 인프라

## 원본

- 출처: https://github.com/HKUDS/CLI-Anything
- 신뢰도: ⭐⭐⭐ (⭐38,098, +1,038 오늘, HKUDS 검증된 연구 기관)
