---
title: "mastra-ai/mastra — TypeScript AI 에이전트 · 워크플로 프레임워크 (★29.7k · YC W25 · ee/ 는 별도 엔터프라이즈 라이선스)"
type: source
domain: ai-news
tags: [ai-news, github-trending, agent-framework, typescript, workflow, mcp, rag]
created: 2026-11-22
updated: 2026-11-22
sources: [https://github.com/mastra-ai/mastra]
reliability: high
---

**GitHub**: ★29,728(볼트 API 11-22 · 수집기 일치) · TypeScript · GitHub 표기 NOASSERTION(Apache-2.0 + `ee/` Mastra Enterprise License 혼재라 자동 판별 불가 — 수집기 판독과 정합) · 생성 2024-08-06 · push 2026-11-22

## 핵심 인사이트
> [!insight] TS 스택의 에이전트 백엔드 기본값 후보 — 라이선스 경계는 디렉터리 단위
> 40+ 프로바이더 모델 라우팅, 툴 사용 에이전트, 그래프 기반 워크플로(일시정지/재개 human-in-the-loop), 대화 메모리 · RAG, MCP 서버 작성, 내장 evals · observability, 로컬 Studio UI(`localhost:4111`). React/Next.js/Node 앱에 내장하거나 독립 엔드포인트로 배포.

## 도메인별 추출 (ai-news)
- **신뢰도**: ⭐⭐⭐⭐ — ★29.7k · 2년 · YC W25. 벤치성 수치 없음(프레임워크).
- **즉시 활용**: 🟡 볼트 사용자의 영상 SaaS 프런트가 Next.js 라면 에이전트 백엔드를 같은 언어로 붙일 수 있다. Python 파이프라인 쪽은 해당 없음.
- **6개월 영향력**: human-in-the-loop 워크플로 + evals 내장이 TS 진영 표준 구성이 된다.
- **대체 관계**: LangGraph.js 대안.
- **허와 실**: `ee/` 기능(auth 등)은 소스 공개이지만 상용 운영 시 라이선스 필요 — "Apache-2.0" 한 단어로 전하면 틀린다. PR 은 협업자만.
- **액션**: 관찰(에이전트 백엔드 선정 시 후보).

## 관련 페이지
- [[AI-에이전트-프레임워크]] · [[에이전트-메모리-레이어]] · [[rig]] (같은 배치 · Rust) · [[ai-news]]

## 원본
- 출처: https://github.com/mastra-ai/mastra
- 확인 범위: GitHub API(스타 · 언어 · 라이선스 표기 · 생성일) · 🔴 README · 라이선스 구성은 수집기 판독
- 신뢰도: ⭐⭐⭐⭐
