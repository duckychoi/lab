---
title: ppt-master — 문서에서 진짜 편집 가능한 PPT를 생성하는 AI 도구
type: source
domain: ai-news
tags: [ai-news, github-trending, pptx, presentation, document-ai, claude-code, tts]
created: 2026-06-28
updated: 2026-06-28
sources: []
reliability: high
---

# ppt-master (hugohe3/ppt-master)

> [!insight] 핵심 인사이트
> GitHub ⭐33,405 — 임의 문서(PDF·Word 등)를 받아 **이미지 캡처가 아닌 진짜 편집 가능한 PowerPoint**를 생성. 모든 슬라이드가 네이티브 DrawingML 도형·텍스트박스·차트로 구성되어 PPT에서 직접 클릭·수정 가능하다는 점이 핵심 차별점 — "AI가 만든 슬라이드 = 손댈 수 없는 이미지 덩어리"라는 통념을 깬다. 발표자 노트를 **음성 내레이션으로 합성**(보이스 클로닝 포함)하고, 슬라이드 전환·등장 애니메이션까지 네이티브로 넣는다. Claude Code·Cursor·VS Code 등 AI IDE 안에서 동작.

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐⭐⭐ — ⭐33,405. Python 86.7% 기반, 추가 외부 의존성 없이 `pip install -r requirements.txt`로 구동(Pandoc은 레거시 포맷용 선택). 규모로 신뢰도 높음.
- **즉시 활용**: YES(후보) — 내 [[reat-slides]] 슬라이드 영상 파이프라인과 인접. 다만 reat-slides는 *영상* 출력, ppt-master는 *편집 가능한 PPTX 객체* 출력이라 용처가 갈린다. 보고서·문서를 발표 자료로 빠르게 변환하는 입력 게이트로 후보.
- **6개월 영향력**: "AI 슬라이드 생성"이 이미지 플래튼(Gamma류)에서 **네이티브 객체 생성**으로 이동하는 신호. 편집 가능성이 확보되면 사람이 마지막 10%를 손보는 실무 워크플로에 실제로 편입 가능.
- **대체 관계**: 이미지 기반 AI 슬라이드 도구, 수동 PPT 제작을 대체·보강. 16:9 PPT 외 샤오훙수·위챗 등 다중 포맷 출력 지원.
- **허와 실**: "real, editable" 클레임은 DrawingML 객체 출력으로 뒷받침되나, 복잡 레이아웃·한국어 폰트·표/수식의 실제 편집 품질은 검증 필요. 음성 내레이션·보이스 클로닝은 부가 기능으로, 품질은 백엔드 TTS에 의존.
- **액션**: 한국어 문서 1건으로 PPTX 생성 → 도형/텍스트가 실제로 네이티브 편집되는지, 한글 폰트·표 깨짐 여부 확인.

> [!action] 당장 할 것
> Python 3.10+ 환경에서 `pip install -r requirements.txt` → 한국어 보고서 1건을 입력해 편집 가능 여부·한글 렌더링 품질을 [[pptx-generate]] 스킬 출력과 대조.

## 관련 페이지
- [[reat-slides]]
- [[Open-Generative-AI]]
- [[Claude-Code-워크플로우]]
- [[ai-news]]

## 원본
- 출처: https://github.com/hugohe3/ppt-master
- GitHub 스타: ⭐33,405 (2026-06-28)
- 스택: Python 86.7% (+ JS/HTML/CSS), Python 3.10+, `pip install -r requirements.txt`
- 신뢰도: ⭐⭐⭐ (대형 레포, 네이티브 PPTX 객체 출력 — 한국어·복잡 레이아웃 편집 품질은 미검증)
