---
name: lint
description: Health-check the LLM wiki. Use periodically to find contradictions, stale claims, orphan pages, missing cross-references, and knowledge gaps. Produces a lint report and optionally fixes issues found.
---

# Lint — LLM Wiki 건강 점검

wiki 상태를 주기적으로 점검하는 워크플로우.
`/lint` 명령으로 실행. 결과는 lint 리포트로 출력하고 log.md에 기록.

## 실행 순서

### Step 1: 전체 파일 목록 파악
```bash
find wiki/ -name "*.md" | sort
```
총 페이지 수 확인.

### Step 2: index.md vs 실제 파일 비교
- index.md에 등록됐지만 파일 없는 링크 → **깨진 링크**
- 파일은 있지만 index.md에 없는 것 → **미등록 페이지**

### Step 3: Orphan 페이지 탐지
인바운드 wikilink가 없는 페이지 찾기:
```bash
# 각 페이지 파일명으로 역방향 링크 확인
grep -r "\[\[concepts/X\]\]" wiki/
```

### Step 4: 모순/구 정보 탐지
페이지 간 내용 비교:
- 동일 주제에 대해 상충되는 주장
- 날짜가 오래된 주장 (더 최신 소스로 superseded)
- "~할 예정" 또는 "아직 없음" 상태인데 이미 해결된 것

### Step 5: 누락된 크로스 레퍼런스 탐지
- A 페이지가 B를 언급하지만 [[B]] 링크 없음
- 관련 개념이지만 서로 연결 안 됨

### Step 6: 지식 공백 탐지
- 여러 페이지에서 언급되지만 독립 페이지 없는 개념
- domain 페이지의 "현재 커버리지"가 비어있는 영역
- "열린 질문들" 중 이미 답변 가능한 것

### Step 7: 개선 제안
웹 검색으로 채울 수 있는 갭 목록 제시.

---

## Lint 리포트 형식

```markdown
# Lint Report — YYYY-MM-DD

## 요약
- 총 페이지: N개
- 발견된 이슈: N개
- 즉시 수정: N개 | 검토 필요: N개

## 🔴 즉시 수정 필요
### 깨진 링크
- `wiki/concepts/llm-wiki.md` → [[entities/unknown]] 파일 없음

### 모순
- `wiki/entities/qwen-image.md`: "20B 파라미터" vs
  `wiki/sources/qwen-research-notes.md`: "파라미터 수 불명"

## 🟡 검토 권장
### Orphan 페이지 (인바운드 링크 없음)
- `wiki/concepts/novel-view-synthesis.md` ← 링크 없음

### 독립 페이지 필요한 개념
- "LoRA fine-tuning" — 여러 페이지에서 언급되나 페이지 없음

## 🟢 제안 (선택)
### 채울 수 있는 지식 공백
- Flux, SD3.5 등 T2I 모델 비교 → 웹 검색으로 채우기
- Cinema Studio 도메인 소스 인제스트 제안

## 다음 lint 권장 시기
약 N개 소스 추가 후 또는 YYYY-MM-DD
```

---

## Step 8: log.md에 lint 기록

```markdown
## [YYYY-MM-DD] lint | 정기 wiki 건강 점검

총 페이지: N개
발견된 이슈: N개 (즉시 수정 M개, 검토 필요 K개)
수정된 이슈: [목록]
미해결 이슈: [목록]
```

---

## 수동 lint 체크리스트 (빠른 버전)

급할 때:
- [ ] index.md의 페이지 수가 실제와 맞는가
- [ ] 최근 인제스트 이후 업데이트 안 된 domain 페이지 있는가
- [ ] overview.md의 "지식 베이스 맵"이 최신인가
- [ ] log.md의 마지막 항목이 실제 마지막 작업과 일치하는가

---

## 참고

- lint는 wiki가 5-10개 소스 이상 쌓이면 특히 유용
- 모순은 새 소스 인제스트 직후에 자주 발생
- orphan 페이지는 ingest 시 cross-reference를 빠뜨린 신호
