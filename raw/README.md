# raw/ — 원본 소스 저장소

이 폴더는 LLM wiki의 **원본 소스 레이어**다.

## 규칙

- **Claude는 이 폴더를 절대 수정하지 않는다.** 읽기 전용.
- 파일을 추가하면 `/ingest` 스킬로 wiki에 반영 요청.
- 원본은 항상 여기에 보관 — wiki 페이지가 요약이고, 여기가 진실의 소스.

## 폴더 구조

```
raw/
├── assets/          ← Obsidian Web Clipper로 다운로드한 이미지
├── articles/        ← 기사, 블로그 포스트 (마크다운)
├── papers/          ← 논문, 기술 리포트
├── notes/           ← 직접 작성한 메모, 클로드 대화 요약
└── data/            ← 데이터 파일, 스프레드시트
```

## 파일 추가 방법

1. **Obsidian Web Clipper** (권장): 브라우저 확장 → 기사를 마크다운으로 변환 → raw/articles/에 저장
2. **직접 저장**: 논문 PDF, 메모 .md 파일을 해당 폴더에 넣기
3. **이미지 다운로드**: Obsidian Settings → Files and links → Attachment folder를 `raw/assets/`로 설정

파일 추가 후 Claude에게: "raw/articles/[파일명] 인제스트해줘"
