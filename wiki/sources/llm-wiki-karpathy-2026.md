---
title: LLM-Wiki 원문 (Karpathy 2026)
type: source
tags: [LLM, PKM, wiki, knowledge-management]
created: 2026-04-09
updated: 2026-04-09
source_url: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
source_type: gist
author: Andrej Karpathy
date: 2026-04-04
---

# LLM-Wiki 원문 (Karpathy 2026)

**출처**: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
**작성자**: [[Andrej Karpathy]]
**날짜**: 2026-04-04

---

## 요약

LLM을 활용한 개인 지식베이스 구축 패턴 ([[LLM-Wiki]]) 아이디어 가이드.
의도적으로 추상적으로 작성됨 — 특정 구현이 아닌 아이디어 자체를 전달하는 것이 목적.

---

## 핵심 내용

### 문제 정의
RAG는 지식을 매번 재추출한다. 합성, 교차 참조, 모순 감지가 없다.

### 해법
LLM이 영속적 위키를 점진적으로 구축·유지. 소스 추가 시 위키에 통합.

### 아키텍처
- Raw Sources (불변, 진실의 원천)
- Wiki (LLM 소유, 마크다운)
- Schema (CLAUDE.md — LLM을 위키 관리자로 만드는 설정)

### 작업
- **Ingest**: 소스 → 위키 통합 (10~15개 페이지 영향)
- **Query**: 위키 → 답변 합성 (좋은 답변은 위키에 저장)
- **Lint**: 위키 건강 점검 (모순, 고아 페이지, 낡은 주장)

### 인덱싱
- `index.md`: 콘텐츠 중심 카탈로그
- `log.md`: 시간순 append-only 기록

---

## 주요 인사이트

1. 북키핑 비용이 거의 0 → 인간이 포기했던 위키 관리 문제 해결
2. 좋은 답변을 위키에 저장 → 탐색 자체가 복리 축적
3. Memex(1945) 정신의 현대적 구현
4. "에이전트 활용 능력은 21세기의 핵심 스킬"

---

## 관련 페이지

- [[LLM-Wiki]]
- [[RAG vs LLM-Wiki]]
- [[Andrej Karpathy]]
