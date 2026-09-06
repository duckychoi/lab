---
title: diagram-design — Mermaid를 버리고 자체완결 HTML+SVG로 간 다이어그램 문법 38종
type: source
domain: ai-news
tags: [ai-news, github-trending, diagram, svg, claude-code, design-reference]
created: 2026-09-06
updated: 2026-09-06
sources: []
reliability: high
---

# diagram-design: 38 editorial diagram types for Claude Code, Codex, and Pi

**GitHub**: https://github.com/cathrynlavery/diagram-design
**지표(2026-09-06 API 실측)**: ⭐ **31,898** · fork **2,051** · 오픈이슈 **32** · **HTML** · **MIT** · 생성 **2026-04-16** · push 2026-09-03
**raw 수집값(09-05)**: ⭐31,255 → **+643**(24시간 증가율 **2.06%** — 배치 내 1위).
**레포 설명 원문**: *"Self-contained HTML + SVG. No shadows. No Mermaid slop."*

> [!insight] 핵심 인사이트 — **에이전트 출력물의 "편집 가능성"을 형식이 결정한다**
> 이 레포의 선택은 명시적 거부로 정의된다: **Mermaid를 안 쓴다.** 대신 **자체 완결(self-contained) HTML+SVG**를 정적 출력으로 낸다.
> 차이는 취향이 아니라 **소유권**이다. Mermaid는 *렌더러가 있어야* 그림이 되고, 렌더러의 레이아웃 결정에 결과가 종속된다. SVG는 **그 자체가 최종 결과물이고 노드 하나를 손으로 옮길 수 있다.** 에이전트가 만든 산출물을 사람이 이어받아 고칠 수 있느냐가 갈린다.
> 볼트 관점에서 이건 [[국소-수리-원리]]의 **출력 형식판**이다 — *잘된 부분은 두고 틀어진 지점만 고친다*가 가능하려면 **출력이 부분 수정 가능한 형식**이어야 한다. Mermaid는 재생성만 가능하고 SVG는 국소 수리가 된다.

> [!insight] 생성 4개월 반 만에 ⭐31,898 — 그리고 24시간 증가율 배치 1위
> **2026-04-16 생성**으로 이 배치에서 [[miles]] 다음으로 젊다. 그런데 09-05→09-06 하루 증가율이 **2.06%** 로 배치 최고다([[opencode]] 0.25%, [[spec-kit]] 0.08%). **절대 스타는 배치 4위인데 유입 속도는 1위** — 아직 확산 중인 자산이라는 뜻이다.
> ⚠️ 단 이는 **2개 시점 관측**이다. 볼트 규칙상 **2건이면 추세 확정 보류** — 다음 배치에서 재확인 대상으로 고정한다.

> [!note] 2.5.10에서 10종 추가 — Sankey · fishbone · Wardley map · kanban 등
> 38종이 고정 목록이 아니라 **버전 단위로 늘고 있다.** Wardley map·fishbone 같은 항목은 범용 차트가 아니라 **전략·원인분석 전용 서식**이다. 즉 이 레포의 실제 자산은 SVG 코드가 아니라 **"어떤 그림을 언제 쓰는가"의 목록**이다.

> [!warning] ⚠️ 품질 근거 없음 · 저자는 개인 계정
> owner `cathrynlavery`는 **organization이 아니라 user(id 50469282)**. 다이어그램 품질에 대한 대조 평가는 없고 *"No Mermaid slop"* 은 **미학적 주장**이다. ⭐3.2만은 그 주장에 대한 동의 표시일 뿐 검증이 아니다.

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐⭐⭐⭐ high — API 실측(스타·언어 HTML·MIT·생성일 확인).
- **즉시 활용**: **YES.** Claude Code 대상으로 명시된 자산이고 MIT다. 볼트가 [[LLM-Wiki]] 그래프 시각화(`/tmp/wiki-graph.html` D3.js)를 이미 하고 있으므로 **38종 목록을 서식 카탈로그로 바로 흡수**할 수 있다.
- **6개월 영향력**: **중간.** 에이전트 산출물이 늘수록 *"고칠 수 있는 형식으로 뽑아라"* 압력이 커진다. 다만 다이어그램은 작업 방식을 바꾸기보다 **품질을 올리는** 층.
- **대체 관계**: **Mermaid를 명시적으로 대체하려 한다.** 볼트가 문서에 Mermaid를 쓰고 있다면 직접 비교 대상.
- **허와 실**: 실은 **형식 선택의 논리(자체완결·편집가능)**. 허는 **"editorial 품질"이라는 미검증 수사**.
- **액션**: 38종 목록만 먼저 확보해 **볼트 시각화 서식 카탈로그**에 반영(중간). Wardley map·fishbone은 **synthesis/ 교차분석 표현에 직접 쓸모**가 있다.

> [!question] 미해결 질문
> - **38종의 실제 산출 품질** — 스타로는 판정 불가. 1종 직접 생성해 봐야 안다.
> - **하루 +2.06% 증가가 지속되는가** — 다음 배치 확인 대상(2건 관측이므로 현재 보류).

## 관련 페이지
- [[국소-수리-원리]] — 출력 형식의 부분 수정 가능성이라는 연결
- [[LLM-Wiki]] — 볼트 그래프 시각화에 직접 적용 가능
- [[Claude-Code-워크플로우]] — 명시된 대상 환경
- [[opencode]] · [[spec-kit]] · [[context7]] — 같은 배치
- [[Meta]] — 에이전트 지향 디자인 시스템(astryx) 인접 사례

## 원본
- 출처: https://github.com/cathrynlavery/diagram-design
- 신뢰도: ⭐⭐⭐⭐ (GitHub API 2026-09-06 실측)
