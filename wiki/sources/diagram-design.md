---
title: "diagram-design — 44종 다이어그램을 단일 HTML+SVG로 그리는 에이전트 스킬"
type: source
domain: ai-news
tags: [ai-news, github-trending, agent-skills, diagram, svg, 출력매체인식, 접근성, 공급망]
created: 2026-10-10
updated: 2026-10-10
sources: []
reliability: medium
---

# diagram-design — 크기 프리셋이 타이포 램프까지 바꾼다

**GitHub**: https://github.com/cathrynlavery/diagram-design
**★48,325** (당일 **+1,739** · 트렌딩 **4위**) · fork 3,057 · watchers 136
**open_issues 81 = 순수이슈 20 + PR 61**(PR 비중 **75.3%**) · MIT · HTML · created 2026-04-16 · pushed 2026-10-10

> [!insight] 핵심 인사이트
> **출력 매체가 타이포그래피를 결정하는 설계다.** 크기 프리셋 10종(`slide-16x9` · `print-a4-landscape` 등)이 **viewBox 와 폰트 램프를 함께 바꾼다** — 투사 슬라이드는 노드명 **16px**, 문서는 **12px**.
> 🎯 **볼트 [[reat]] 레이아웃 축과 직결된다**: 슬라이드/문서/소셜별 폰트 크기를 산출물이 아니라 **프리셋이 결정한다.** 이 배치 유일한 출력매체-인식 사례다.

> [!insight] 🆕 배포 출처 봉인 명시 — [[자기제한-명시]] 와 다른 축
> *"Official builds come only from this repository… a listing under any other name is an unofficial copy"* + `PRIVACY.md` 로 네트워크 전송 항목을 분리한다.
> ⇒ **공급망 사칭을 README 가 선제 경고한다.** 자기 능력을 제한하는 서술(자기제한)이 아니라 **배포 경로의 정당성을 봉인하는** 서술이다. → [[배포출처-봉인]]

> [!warning] 🆕 트렌딩 순위와 당일 증분이 어긋난다 — 반례 1건 실측
> 3위 [[mattpocock-skills]] **+1,687** < 4위 본 레포 **+1,739**.
> ⇒ ⚖️ **GitHub Trending 은 "당일 스타 증분" 단조 정렬이 아니다.** 📌 **규약: 트렌딩 순위를 증분 순위로 인용하면 틀린다.** → [[지표-창길이]]

> [!warning] 측정 수치 0개
> **44종은 기능 카운트이고 다이어그램 품질·정확도 측정이 아니다.** *"No shadows. No Mermaid slop."* 는 마케팅 문구이므로 요약에서 제외했다.

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐⭐⭐ — API 실측 확실 · 품질 측정 0.
- **즉시 활용**: 🎯 **YES — 금일 3순위 actionable.** 자기완결 `.html` 1개(HTML+SVG)로 출력하므로 **볼트 `html/` 산출물 관행과 동형**이고, 접근성 처리(스크린리더 제목·설명 · `prefers-reduced-motion` 정적 프레임)는 볼트 HTML 리포트에 **즉시 이식 가능한 패턴**이다.
- **6개월 영향력**: 다이어그램을 이미지가 아니라 **텍스트 산출물(SVG)**로 내는 쪽이 기본값이 되면 버전관리·편집 가능성이 달라진다. 볼트 canvas/HTML 라인과 경쟁이 아니라 보완.
- **대체 관계**: Mermaid 를 명시적 비교 대상으로 둔다(품질 주장은 미검증).
- **허와 실**: 📌 호스트 9종 이상 지원 명시(Cursor·Claude Code·Codex·Copilot·Gemini CLI·Cline·Windsurf·Amp·Zed·Warp·Roo·Kilo) = **스킬 포맷의 호스트 중립성 주장**이고 **미검증**이다.
- **액션**: 아래.

> [!action] 당장 할 것
> **① 접근성 패턴 이식** — 스크린리더 제목/설명 + `prefers-reduced-motion` 정적 프레임을 볼트 HTML 리포트 템플릿에 넣는다.
> **② 프리셋 ↔ 타이포 램프 매핑표를 추출해 [[reat]] 레이아웃 카탈로그와 1:1 대조한다**(슬라이드 16px / 문서 12px 가 볼트 기준과 어긋나는지).

> [!question] 미해결
> - 44종의 **실제 목록** 미확보.
> - 호스트 9종 중 **Claude Code 에서의 동작** 미검증.
> - PR 61건의 생성일 분포 미확인(PR 비중 75.3% 는 10-06 [[text-to-cad]] 100% 에 이은 상위값).

## 관련 페이지
- [[배포출처-봉인]] — 🆕 본 소스가 신설 계기
- [[지표-창길이]] — 트렌딩 순위 ≠ 증분 순위 반례
- [[reat]] — 레이아웃·타이포 램프 적용 대상
- [[에이전트-스킬]] · [[rea]] · [[mattpocock-skills]] — 같은 날 `skills.sh` 3건
- [[cathrynlavery]] · [[ai-news]]

## 원본
- 출처: https://github.com/cathrynlavery/diagram-design
- 수집: 2026-10-10 자동수집 (ai-news)
- 검증: GitHub API 실측 · `open_issues` 분해 81=20+61 검산 통과
- 신뢰도: ⭐⭐⭐
