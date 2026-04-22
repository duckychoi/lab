---
title: LLM-Wiki
type: concept
tags: [knowledge-management, LLM, PKM, wiki]
created: 2026-04-09
updated: 2026-04-09
sources: [llm-wiki-karpathy-2026.md]
---

# LLM-Wiki

LLM을 활용하여 개인 지식베이스를 **복리 축적형**으로 구축하는 패턴. [[Andrej Karpathy]]가 2026년 공개한 아이디어 가이드에서 비롯됨.

---

## 핵심 철학

기존 [[RAG vs LLM-Wiki|RAG]] 방식은 쿼리마다 원본에서 재추출한다 — 지식이 쌓이지 않는다.
LLM-Wiki는 다르다: LLM이 **영속적 위키를 점진적으로 구축·유지**한다.

> "The wiki is a persistent, compounding artifact. The cross-references are already there. The contradictions have already been flagged." — Karpathy

**인간의 역할**: 소싱, 탐색, 좋은 질문
**LLM의 역할**: 요약, 교차 참조, 정리, 북키핑 전체

---

## 3계층 아키텍처

| 레이어 | 소유자 | 역할 |
|--------|--------|------|
| Raw Sources | 인간 | 원본 소스. 불변. 진실의 원천. |
| Wiki | LLM | 마크다운 파일 모음. LLM이 작성·유지. |
| Schema | 인간+LLM | CLAUDE.md — LLM을 위키 관리자로 만드는 설정 |

---

## 3가지 핵심 작업

### Ingest (인제스트)
새 소스 추가 → LLM이 읽고 → 위키에 통합
- 단일 소스가 10~15개 페이지에 영향 가능
- entity 페이지, concept 페이지, 모순 표시 등 자동화

### Query (쿼리)
위키 대상으로 질문 → LLM이 관련 페이지 탐색 → 인용 포함 답변 합성
- **좋은 답변은 위키 페이지로 보존** → 탐색 자체도 지식 복리 축적

### Lint (린트)
주기적 위키 건강 점검:
- 페이지 간 모순
- 고아 페이지 (인바운드 링크 없음)
- 낡은 주장 (최신 소스에 의해 대체됨)
- 자체 페이지 없는 중요 개념

---

## 왜 작동하는가

> "LLMs don't get bored, don't forget to update a cross-reference, and can touch 15 files in one pass."

지식베이스 유지의 핵심 장벽은 **북키핑** — 교차 참조 업데이트, 요약 최신화, 모순 표시. 인간은 이 부담이 커지면 위키를 포기한다. LLM은 지루함을 모르고 한 번에 15개 파일을 처리한다.

---

## Vannevar Bush의 Memex와의 연결

1945년 Vannevar Bush가 꿈꾼 **Memex** — 개인적·능동적으로 큐레이션되며, 문서 간 연결이 문서 자체만큼 가치 있는 지식 저장소. Bush가 해결 못한 "누가 유지 관리하는가" 문제를 LLM이 담당한다.

---

## 실용 도구

- **Obsidian**: 위키 뷰어. 그래프 뷰, Dataview 플러그인, Marp 슬라이드
- **Obsidian Web Clipper**: 웹 기사 → 마크다운 변환
- **qmd**: 위키용 로컬 검색 엔진 (BM25+벡터 하이브리드)
- **Git**: 버전 관리, 브랜칭, 협업

---

## 관련 페이지

- [[RAG vs LLM-Wiki]]
- [[Andrej Karpathy]]
