---
name: ingest
description: Process a new source into the LLM wiki. Use when the user provides a new article, paper, note, URL, or file to add to the knowledge base. Reads the source, extracts key information, and writes wiki pages using a tiered approach to minimize file creation.
---

# Ingest — LLM Wiki 소스 추가 (최적화 버전)

소스 1개당 **최소 3개 파일**만 필수 생성. 나머지는 조건부.

---

## 필수 (항상, 3개)

### 1. `wiki/sources/[slug].md` 생성

```markdown
---
title: [제목]
type: source
tags: [태그1, 태그2]
created: YYYY-MM-DD
updated: YYYY-MM-DD
source_url: [URL] (있으면)
author: [저자] (있으면)
---

# [제목]

**인제스트일**: YYYY-MM-DD

## 한 줄 요약
[한 문장]

## 핵심 발견
- [항목1]
- [항목2]

## 새로 등장한 개념/엔티티 (페이지 없음)
> 아직 독립 페이지 없음. 여러 소스에서 반복되면 생성.
- `[개념명]` — [한 줄 설명]

## 관련 페이지
- [[domains/...]]
```

### 2. `wiki/index.md` — 1줄 추가

Sources 섹션 맨 아래에:
```
- [[sources/[slug]]] — [한 줄 요약]
```
상단 페이지 카운트 +1.

### 3. `wiki/log.md` — 1항목 append

```markdown
## [YYYY-MM-DD] ingest | [소스 제목]
소스: [URL 또는 파일명]
핵심: [1-2줄]. 생성: sources/[slug].md
```

---

## 조건부 (기준 충족 시만)

### 새 concept 페이지 생성 — 둘 중 하나라도 해당될 때
- 이 개념이 **이미 다른 wiki 페이지에서 언급**되고 있음 (= 두 번째 등장)
- 이 소스의 **중심 주제**이고 앞으로 여러 소스에서 계속 참조될 것이 확실

→ `wiki/concepts/[slug].md` 생성 + index.md Concepts 섹션에 추가

### 새 entity 페이지 생성 — 둘 중 하나라도 해당될 때
- 이 엔티티(모델/도구/인물)가 이미 다른 페이지에서 언급됨
- 이 소스의 주인공이고 여러 속성/관계를 정리할 만큼 복잡함

→ `wiki/entities/[slug].md` 생성 + index.md Entities 섹션에 추가

### domain 페이지 업데이트 — 해당될 때
- 해당 도메인의 "현재 커버리지"가 실질적으로 변하는 소스

→ `wiki/domains/[domain].md`의 커버리지 섹션에 1-3줄 추가만 (재작성 X)

### overview.md 업데이트 — 해당될 때
- wiki 전체 흐름을 바꾸는 중요한 발견
- "열린 질문" 해소 또는 새 질문 등장

---

## 결정 흐름

```
소스 읽기
  ↓
sources/[slug].md 생성 (항상)
index.md +1줄 (항상)
log.md +1항목 (항상)
  ↓
이 개념이 이미 wiki에 언급됨? ──→ YES → concept 페이지 생성
                              ──→ NO  → sources/ 페이지의 "새 개념" 섹션에 메모만
  ↓
entity가 복잡하고 중요함?      ──→ YES → entity 페이지 생성
                              ──→ NO  → sources/ 페이지에 인라인 설명
  ↓
domain 커버리지 실질 변화?    ──→ YES → domain 페이지 1-3줄 추가
  ↓
완료
```

---

## 그래프 갱신 (선택)

인제스트 후 graph.json / wiki-graph.html을 최신화하려면:
```bash
python3 scripts/wiki-graph.py
```

Claude는 `wiki/graph.json`을 읽어서 현재 연결 구조를 파악할 수 있음.

---

## 결과 규모 기준

| 소스 유형 | 예상 생성/수정 파일 수 |
|---|---|
| 짧은 기사 | 3개 (필수만) |
| 중요 기사 | 4-5개 (+ concept 또는 entity) |
| 핵심 논문/레퍼런스 | 5-7개 |
| 도메인 정의 소스 | 6-8개 |
