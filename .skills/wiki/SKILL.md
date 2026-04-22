---
name: wiki
description: LLM-Wiki 패턴으로 개인 지식베이스를 관리한다. 소스 인제스트, 쿼리, 린트를 수행한다.
---

# Wiki 스킬

볼트 경로: `/home/monday/vault`
스키마: `/home/monday/vault/CLAUDE.md` (반드시 먼저 읽을 것)

## 시작하기 전에 반드시

```bash
cat /home/monday/vault/CLAUDE.md
cat /home/monday/vault/index.md
```

---

## raw.md — 인제스트 대기열

소스는 파일로 쌓지 않고 `raw.md` 하나에 항목으로 관리한다.
**ingest 완료 후 해당 항목을 raw.md에서 즉시 삭제한다.**

```bash
cat /home/monday/vault/raw.md
```

---

## Ingest — 새 소스 추가

### URL 인제스트
```bash
VAULT="/home/monday/vault"
# 1. 소스 내용 가져오기
defuddle parse "URL" --md
# 2. 위키 페이지 생성/업데이트 (CLAUDE.md 스키마 따름)
# 3. index.md 업데이트
# 4. raw.md에서 해당 항목 삭제
# 5. log.md 기록
```

### 텍스트/붙여넣기 인제스트
```bash
VAULT="/home/monday/vault"
# 사용자가 텍스트를 직접 제공한 경우
# → 위키 통합 작업 수행 후 log.md 기록
```

### raw.md 일괄 처리
```bash
cat /home/monday/vault/raw.md
# → 항목 하나씩 처리 후 raw.md에서 삭제
```

---

## Query — 위키 질문

```bash
VAULT="/home/monday/vault"
cat "$VAULT/index.md"
cat "$VAULT/wiki/concepts/관련개념.md"
# → 답변 합성, 좋은 답변은 queries/ 에 저장
```

---

## Lint — 위키 건강 점검

```bash
VAULT="/home/monday/vault"
find "$VAULT/wiki" -name "*.md" | while read f; do
  page=$(basename "$f" .md)
  count=$(grep -rl "\[\[$page\]\]" "$VAULT/wiki" "$VAULT/index.md" 2>/dev/null | wc -l)
  if [ "$count" -eq 0 ]; then echo "고아 페이지: $f"; fi
done
grep "^## \[" "$VAULT/log.md" | tail -10
```

---

## 빠른 탐색

```bash
VAULT="/home/monday/vault"
grep -rli "키워드" "$VAULT/wiki" --include="*.md"
find "$VAULT/wiki" -name "*.md" -type f
```
