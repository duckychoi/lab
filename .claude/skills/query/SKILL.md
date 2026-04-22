---
name: query
description: Query the LLM wiki for information, analysis, or synthesis. Use when the user asks a question that should be answered from the accumulated wiki knowledge. Reads relevant wiki pages, synthesizes an answer with citations, and optionally files valuable answers back as new wiki pages.
---

# Query — LLM Wiki 질문/탐구

wiki에 축적된 지식으로 질문에 답하는 워크플로우.

## 실행 순서

### Step 1: wiki/index.md 읽기
항상 index.md를 먼저 읽어서 관련 페이지를 파악.
```bash
# index.md에서 관련 항목 검색
obsidian read path="wiki/index.md"
```

### Step 2: 관련 페이지 읽기
질문과 연관된 pages:
1. 직접 관련 concept/entity 페이지
2. domain 페이지 (더 넓은 맥락)
3. overview.md (전체 그림)

### Step 3: 답변 합성

답변 형식 (질문 유형별):
| 질문 유형 | 답변 형식 |
|---|---|
| 개념 설명 | 마크다운 섹션 |
| 비교/대조 | 테이블 |
| 현황 파악 | 항목 목록 + 갭 표시 |
| 연결/관계 | 다이어그램 또는 계층 목록 |
| 분석 | 구조화된 섹션 |

항상 **인용** 포함:
```markdown
...Qwen-Image는 이중 인코딩 구조를 사용한다
(출처: [[entities/qwen-image]], [[sources/qwen-research-notes]])
```

### Step 4: 가치 있는 답변 저장 제안

다음 기준을 충족하면 wiki 페이지로 저장 제안:
- 여러 소스를 합성한 새로운 통찰
- 비교 분석 (A vs B)
- 미래 참조할 가능성이 높은 답변
- 사용자가 "이걸 저장해줘"라고 하는 경우

저장 위치:
- `wiki/syntheses/[slug].md` — 분석/비교/발견

### Step 5: log.md 업데이트 (선택)
중요한 쿼리는 log에 기록:
```markdown
## [YYYY-MM-DD] query | [질문 제목]

질문: [원래 질문]
읽은 페이지: [페이지 목록]
주요 발견: [1-2줄 요약]
저장됨: [저장된 경우 파일명] (선택)
```

---

## Query 유형별 접근

### "X가 뭐야?" (개념 설명)
→ concepts/ 페이지 + 연관 entity 읽기

### "X vs Y 비교해줘"
→ 두 페이지 모두 읽기 → 비교 테이블 생성 → wiki에 저장 제안

### "현재 X 분야 상황이 어때?"
→ domain 페이지 + 관련 entity 전부 읽기 → 갭 표시

### "X에 대해 더 알고 싶어"
→ 관련 페이지 + "열린 질문들" 섹션 확인 → 탐구 방향 제안

### "X를 wiki에 추가해줘"
→ `/ingest` 스킬로 전환

---

## 참고

- wiki에 정보가 없으면 솔직하게 "아직 인제스트 안 됨" 표시
- 웹 검색이 필요하면 WebSearch/WebFetch 사용 후 ingest 제안
- 답변은 항상 wiki 내용 기반 (hallucination 방지)
