---
title: MathModelAgent — 수학 모델링 전용 멀티에이전트 (라이선스 부재)
type: source
domain: ai-news
tags: [ai-news, github-trending, agent, multi-agent, math-modeling, claude-code, agent-skills, license-risk]
created: 2026-09-12
updated: 2026-09-12
sources: []
reliability: medium
---

# MathModelAgent (jihe520/MathModelAgent)

> [!insight] 핵심 인사이트
> ⭐**4,976**(2026-09-12 GitHub API 실호출 · raw 4,970 대비 **+6 드리프트**) · fork **396** · Python · created **2025-01-30** · pushed 2026-09-10 · 이슈 **42**.
> 수학 모델링 경진대회(수학건모) 한 종목을 **전 과정 자동화**한다 — 문제 분석 → 모델링 → 코드 작성 → **오류 자가수정** → 제출 가능한 서식의 논문 출력. README 원문: *"Automatically complete mathematical modeling and generate a ready-to-submit paper."*
> 🎯 **가장 중요한 구조 변화는 에이전트 구성이 아니라 배포 형태다** — 최신 릴리스는 **데스크톱 앱이 [[Claude-Code-워크플로우|Claude Code]]와 MathModelAgent SKILLS 전체를 번들**한다(README 27행: *"The desktop app bundles Claude Code and the full set of MathModelAgent SKILLS. No Python / Node.js / Redis installation and no manual SKILL setup — install it, add one model API key, and start modeling."*).
> → 즉 이건 **에이전트 프레임워크가 아니라 "스킬 묶음 + 하네스"를 앱으로 포장한 것**이다. [[에이전트-스킬]] 계보가 **도메인 특화 수직 제품**으로 내려온 사례.

> [!warning] 🔴 LICENSE 파일이 **아예 없다** — 사내·상업 사용 보류 대상
> **볼트 실측**: GitHub API `license: null` + **루트 파일 목록 14개 직접 조회** → `.claude`, `.cursor`, `.dockerignore`, `.gitignore`, `CLAUDE.md`, `README.md`, `README_EN.md`, `backend`, `docker-compose.override.yml`, `docker-compose.yml`, `docs`, `frontend`, `skills`, `win_start.bat`. **LICENSE·COPYING 계열 파일 0건.**
> → 라이선스 부재의 기본값은 **저작권 유보**(모든 권리 보유)다. 공개 레포라는 사실은 사용 허락이 아니다.
> → 🎯 이건 [[파생표기-함정]] 과 **반대 방향의 사례**다. 그쪽은 `NOASSERTION` 을 보고 "제약 있음"으로 **과대** 판정한 오류였고([[teamai-cli]]·[[WeKnora]] 둘 다 실제로는 MIT였다), 이쪽은 **필드가 null 이고 원문도 없다** — 즉 **판정 유보가 아니라 실제로 권리가 유보된 상태**다. `null` 과 `NOASSERTION` 은 다르게 취급해야 한다.
> → raw가 이 점을 **정확히 짚었다**(*"기본값은 저작권 유보이므로 사내 사용은 보류 대상"*). 볼트 재확인 결과 **맞다**.

> [!warning] 코드 서명 미비 — raw가 놓친 항목
> README 38행: *"The Windows installer is **not code-signed yet**. Microsoft Defender SmartScreen may warn on first install or launch."*
> 라이선스 부재와 합쳐지면 **배포 신뢰 경로가 두 군데 비어 있다**(법적 근거 · 바이너리 출처). 데스크톱 앱 권장 배포인데 둘 다 없다.

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐⭐ — 스타·포크·생성일·루트 파일 목록 전부 GitHub API 실호출로 대조. 다만 **성능 주장을 검증할 외부 근거가 없다**("award-level modeling paper"는 자기 서술이고 대회 성적 데이터가 README에 없다). 라이선스 부재로 실사용 리스크 존재 → reliability **medium**.
- **즉시 활용**: **조건부 NO.** 도구 자체는 수학 모델링이라는 좁은 도메인용이라 내 워크플로와 접점이 적고, 무엇보다 **라이선스가 없어 코드를 가져다 쓸 수 없다**. 다만 **아키텍처는 읽을 가치가 있다** — `skills/` 디렉터리가 루트에 있으므로 스킬 분할 방식만 참고.
- **6개월 영향력**: "Claude Code + 도메인 스킬 묶음 → 데스크톱 앱"이라는 **패키징 패턴**이 번지면, 에이전트 제품의 단위가 *모델*이나 *프레임워크*가 아니라 **스킬 번들**이 된다. [[vercel-skills]](배급 층) · [[에이전트-스킬]] 과 같은 방향.
- **대체 관계**: 대체하지 않는다. 내 스킬 체계([[Claude-Code-워크플로우]])와 **같은 재료로 다른 수직을 만든 사례**.
- **허와 실**: 걷어낼 마케팅은 "award-level"이라는 형용사다. **대회 제출 결과·순위·채점 데이터가 전무**하다. 실제로 검증된 것은 "파이프라인이 논문 서식 문서를 출력한다"까지다.
- **액션**: `skills/` 디렉터리 구조만 열람(코드 도입 불가). 라이선스가 추가되면 재검토.

## 관련 페이지
- [[에이전트-스킬]]
- [[Claude-Code-워크플로우]]
- [[vercel-skills]]
- [[파생표기-함정]]
- [[한정어-탈락]]
- [[ai-news]]

## 원본
- 출처: https://github.com/jihe520/MathModelAgent
- GitHub API 실호출(2026-09-12): ⭐**4,976** · fork **396** · Python · **license: null** · created 2025-01-30 · pushed 2026-09-10 · open_issues 42 · topics `agent, llm, mathmodel, skills`
- 루트 파일 목록 실조회: 14개, **LICENSE 부재 확인**
- raw 대비: 스타 **+6 드리프트**, 라이선스 판정 **일치**
- 신뢰도: ⭐⭐ (수치·라이선스 실측 / 성능 주장 미검증)
