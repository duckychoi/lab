---
title: humanlayer/skills — 스킬이 "제어 루프를 설계해주는" 층으로 올라섰다 (⭐3,326 · raw 오류 1건 정정)
type: source
domain: ai-news
tags: [ai-news, github-trending, agent-skills, humanlayer, claude-code, control-loop, 4층-진화]
created: 2026-09-07
updated: 2026-09-07
sources: []
reliability: high
---

# humanlayer/skills — HumanLayer 배포 Claude Code 스킬

**GitHub**: https://github.com/humanlayer/skills
**스타수**: **3,326** (2026-09-07 API 실측 · raw 표기 3,324 대비 **+2**)
**포크 98 · 이슈 7 · 워치 7 · 생성 2026-03-18 · 최종 push 2026-08-13 · 주 언어 TypeScript**
**라이선스**: **MIT** · 배포: `npx skills add humanlayer/skills --skill <이름>`
**루트 구조 실측**: `.claude-plugin/` · `plugins/` · `LICENSE` · `README.md` — **`skills/` 디렉터리가 없다**

> [!warning] 🔴 raw.md 기재 오류 — **스킬은 3종이 아니라 5종이다**
> raw는 *"Claude Code 스킬 **3종**"* 으로 적었다. README 헤딩을 실측하면 **5종**이다:
> `improve-claude-md` · `narrow-react-prop-types` · `build-iterated-agentic-loop` · **`design-control-loop`** · **`show-me`**
> 누락된 2종 중 **`design-control-loop` 이 이 레포에서 가장 중요한 스킬**이다(아래). **raw 요약만 믿고 인제스트했다면 이 배치의 핵심을 통째로 놓쳤다.**
> → 볼트 규칙 재확인: **raw의 한줄요약은 수집기의 요약이지 소스가 아니다.** 09-06에 세운 *"raw 수집값과 실측을 전건 대조"* 규칙을 **지표(숫자)뿐 아니라 내용(구성)에도 적용**해야 한다. `actionable.md` 반영.

> [!insight] 핵심 인사이트 — 4층(진화)에 **"루프를 설계해주는 스킬"** 이 등장했다
> `design-control-loop` 의 README 설명(원문): *"당신을 **인터뷰**해서 — 센서·컨트롤러·액추에이터·외란(disturbances) — 코드베이스에 맞는 에이전틱 제어 루프를 설계하고, 로컬 실행 가능한 컴포넌트 + 스케줄된 코딩 에이전트 워크플로로 **빌드까지 한다**."*
> 볼트의 [[에이전트-스킬]] 4층은 지금까지 **스킬이 스스로를 고치는**([[SkillEvo]]) 또는 **스킬을 생성하는**([[JIT-Agent]]) 사례였다. 여기서는 스킬이 **자기 자신이 아니라 "사용자의 자동화 시스템 전체"를 설계**한다.
> 게다가 어휘가 **제어공학**이다 — 센서/컨트롤러/액추에이터/외란. LLM 에이전트를 *"프롬프트 체인"* 이 아니라 **피드백 제어 시스템**으로 모델링하는 프레이밍이며, 볼트가 이 어휘를 스킬 층에서 본 것은 **처음**이다.

> [!insight] `build-iterated-agentic-loop` 와 짝을 이룬다 — **설계 → 빌드의 2단**
> - `design-control-loop`: **무엇을 만들지**를 인터뷰로 확정
> - `build-iterated-agentic-loop`: 레포 로컬 스킬 + **GitHub Actions 워크플로 · 프롬프트 · 메모리 파일 · 레퍼런스 템플릿**을 생성
> 둘 다 산출물에 **스케줄된 CI 워크플로**가 들어간다. → **스킬의 출력이 "이번 대화의 결과물"이 아니라 "계속 도는 시스템"** 이다. [[에이전트-스킬]] 이 정리한 *"스킬 = 절차 지식"* 정의를 **"스킬 = 시스템 부트스트래퍼"** 로 확장해야 할 수 있다.

> [!note] `improve-claude-md` — 볼트에 직접 걸리는 스킬
> *"CLAUDE.md를 `<important if>` 블록으로 재작성해 **지시 준수율**을 개선한다."*
> 볼트에는 `/home/monday/vault/CLAUDE.md`(위키 스키마)와 `~/CLAUDE.md`(행동 지침)가 **둘 다 있고**, 이 스킬이 겨냥하는 게 정확히 그 파일 형식이다.
> ⚠️ **단 효과 근거는 없다** — "준수율 개선"의 측정치가 README에 없다. 볼트가 [[에이전트-스킬]] 에 반복 기록한 *"스킬에는 품질 보증 수단이 사실상 없다"* 가 **또 성립**한다. [[Repo-To-Skill]](통제 실험 보유)이 여전히 이 층의 유일한 예외.

> [!warning] 배포 구조가 이미 "플러그인"으로 넘어가 있다
> 루트에 **`skills/` 가 없고 `plugins/` 와 `.claude-plugin/` 이 있다**(contents API 실측). README는 `npx skills add` 로 안내하는데 **레포 실제 구조는 플러그인 레이아웃**이다.
> → 같은 배치의 [[openai-skills]] 가 *"스킬 레포 → 플러그인"* 이동을 **선언**했다면, 이 레포는 그 이동을 **이미 조용히 마친 상태**다. **같은 날 같은 방향의 독립 사례 2건** — 3층 재편이 벤더 한 곳의 결정이 아님을 시사한다.

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐⭐⭐ — ⭐3,326 실측·MIT·README 원문 대조. **효과 수치 없음**, 스타 규모도 이 배치 스킬 3건 중 최소. 단 **내용의 신규성은 이 배치 최고**.
- **즉시 활용**: **YES(부분).** `improve-claude-md` 를 볼트 `CLAUDE.md` 2종에 시험 적용 가능. 단 **원본 백업 필수** — 자동 재작성 스킬이고 효과 근거가 없다.
- **6개월 영향력**: 스킬이 **CI 워크플로를 산출물로 내놓기 시작**하면, 볼트의 인제스트 파이프라인 자체를 *"스케줄된 제어 루프"* 로 재구성할 수 있다. 현재 이 볼트는 **자동수집 → 수동 `/wiki` 실행** 구조인데, `design-control-loop` 의 센서/컨트롤러/액추에이터 분해가 정확히 그 갭을 겨냥한다.
- **대체 관계**: 대체 아님. [[SkillEvo]]·[[JIT-Agent]] 와 **같은 4층**이되 대상이 다름(자기 자신 → 사용자 시스템).
- **허와 실**: 제어공학 어휘가 **실제 폐루프 제어**를 뜻하는지, 아니면 **비유**인지 확인 안 됐다. 진짜 센서/피드백이 있는지는 스킬 본문을 읽어야 판정된다.
- **액션**: 아래.

> [!action] 당장 할 것
> **`design-control-loop` 의 SKILL.md 본문만 읽는다.** 확인할 것 하나: *"센서"가 실제 관측 신호를 읽는가, 아니면 사용자 인터뷰 응답의 은유인가.* 전자면 볼트 인제스트 자동화의 설계 템플릿으로 쓸 수 있고, 후자면 [[에이전트-스킬]] 4층에 **새 층이 아니라 어휘만 바뀐 사례**로 기록하고 넘어간다.

> [!question] 미해결
> `show-me` 는 **무엇을 하는 스킬인가.** README 헤딩만 확인했고 본문을 못 읽었다. raw가 놓친 2종 중 하나이며, 이름만으로는 판정 불가. 다음 회차 확인 대상.

## 관련 페이지
- [[에이전트-스킬]] · [[SkillEvo]] · [[JIT-Agent]] · [[Repo-To-Skill]] · [[openai-skills]] · [[marketingskills]] · [[anthropics-skills]] · [[superpowers]] · [[claude-plugins-official]] · [[Claude-Code-워크플로우]] · [[LLM-Wiki]] · [[암묵을-명시로]]

## 원본
- 출처: https://github.com/humanlayer/skills
- 수집: 2026-09-07 자동수집 (ai-news)
- 검증: GitHub API 실측 + README 원문 대조 + 루트 contents API 실측 (2026-09-07)
- **정정**: raw "스킬 3종" → **실제 5종**(README 헤딩 실측)
- 신뢰도: ⭐⭐⭐
