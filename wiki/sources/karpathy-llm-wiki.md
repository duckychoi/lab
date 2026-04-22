---
title: "Karpathy — LLM Wiki (2026)"
type: source
tags:
  - knowledge-management
  - llm
  - pkm
  - pattern
created: 2026-04-10
updated: 2026-04-17
source_url: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
author: Andrej Karpathy
cssclasses:
  - wide-page
---

# Karpathy — LLM Wiki

> [!abstract] Source Summary
> LLM이 개인 지식 베이스(wiki)를 점진적으로 빌드하고 유지하는 패턴.
> RAG와 달리 지식이 축적된다.

| Field | Value |
|---|---|
| **Source** | GitHub Gist |
| **Author** | Andrej Karpathy |
| **Ingested** | 2026-04-10 |
| **URL** | https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f |

---

## Key Quotes

> [!quote]
> *"The tedious part of maintaining a knowledge base is not the reading or the thinking — it's the bookkeeping."*

> [!quote]
> *"The wiki stays maintained because the cost of maintenance is near zero."*

> [!quote]
> *"The human's job is to curate sources, direct the analysis, ask good questions, and think about what it all means. The LLM's job is everything else."*

> [!quote]
> *"This is the key difference: **the wiki is a persistent, compounding artifact.**"*

---

## Document Structure

1. **The core idea** — RAG와의 차이, persistent compounding artifact
2. **Architecture** — 3레이어: raw sources / wiki / schema
3. **Operations** — Ingest, Query, Lint
4. **Indexing and logging** — index.md (내용) + log.md (시간)
5. **Optional: CLI tools** — qmd (검색 엔진)
6. **Tips and tricks** — Obsidian Web Clipper, graph view, Marp, Dataview, git
7. **Why this works** — 유지보수 비용 0, Vannevar Bush Memex 연결
8. **Note** — 의도적으로 추상적, 구현은 사용자 + LLM이 결정

---

## Application Domains (from original)

- **Personal**: 목표, 건강, 심리, 자기계발
- **Research**: 수주~수개월 논문 + 기사 심층 탐구
- **Reading a book**: 챕터별 인제스트 (Tolkien Gateway 같은 팬 wiki)
- **Business/team**: Slack, 회의록, 프로젝트 문서 → LLM 유지 팀 wiki
- **기타**: 경쟁 분석, 실사, 여행 계획, 강의 노트, 취미 심층 탐구

---

## Recommended Tool Stack

| Tool | Use |
|---|---|
| Obsidian Web Clipper | 기사 → 마크다운 변환 |
| Obsidian Graph View | wiki 토폴로지 시각화 |
| Marp | wiki → 슬라이드 |
| Dataview | frontmatter 쿼리 |
| qmd | BM25/벡터 하이브리드 로컬 검색 (규모 커지면) |
| Git | 버전 히스토리 + 협업 |

---

## Application in This Vault

이 소스를 기반으로 `CLAUDE.md`(스키마)와 `wiki/` 디렉토리 전체를 설계함.
Karpathy가 의도적으로 추상적으로 남긴 부분을 이 vault의 맥락에 맞게 구체화:
- 디렉토리 구조: `wiki/concepts/`, `wiki/entities/`, `wiki/domains/`, `wiki/sources/`
- Skill 시스템: `/ingest`, `/query`, `/lint`
- 한국어/영어 혼용 컨벤션

---

## Derived Pages

- [[concepts/llm-wiki]] — 이 패턴의 개념 정리
- [[overview]] — vault 현재 상태
