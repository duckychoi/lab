---
title: "AAArena / AHL — '금메달 6개'는 2위와 2개 차이고, 그 차이에 하네스가 섞여 있다(논문이 먼저 적는다)"
type: source
domain: ai-news
tags: [ai-news, agent-benchmark, heuristic-learning, ahl, game-agent, elo, claude-code, codex, 하네스-설계-축, 자기제한-명시, 매크로-미치환]
created: 2026-10-12
updated: 2026-10-12
sources: []
reliability: high
---

# Can AI Agents Learn Their Way to the Top? (AAArena / Adversarial Heuristic Learning)

> [!insight] 🎯 핵심 인사이트 — **가중치를 건드리지 않고 "실행 가능한 정책 코드"만 고치는 학습 패러다임**
> **AHL(Adversarial Heuristic Learning)** 정의 원문: *"a paradigm that uses AI agents as learning engines to refine game policies and supporting software **while keeping model weights fixed**."*
> 🎯 즉 학습 주체가 **그래디언트가 아니라 에이전트의 코드 수정**이다. 에이전트가 하는 일 원문: *"Agents **interpret rules, choose opponents, analyze replays, and revise game agents** to achieve their highest ranking within fixed match and evaluation budgets."*
> 📌 **이것은 RL의 대체물이 아니라 "코드가 정책인 영역"에서의 학습이다.** 볼트 [[하네스형-에이전틱-RL]] · [[에이전트축-분기]] 와 같은 계열이며, 가중치 고정이라는 조건이 **재현 비용을 0에 가깝게** 만든다.

> [!note] 🏆 **수집기 미확인 해소 — `\val{completedmodels}` = 7** (볼트가 arXiv HTML로 뚫었다)
> 수집기 10-12 자기보고 5번: *"[[AAArena]] *'completedmodels model'* (초록 원문의 오타로 보이나 **평가된 구성 수를 확정하지 못했다**)"*.
> ✅ **해소했다. 그리고 "오타"가 아니다 — LaTeX 매크로 미치환이다.** 초록 원문은 `We evaluate \val{completedmodels} model and harness configurations:` 이고, `\val{}` 명령이 치환되지 않은 채 배포됐다.
> 📌 **본문(HTML)에서 3중 교차 확인**:
> 1. *"We evaluate **7** model and harness configurations"*
> 2. *"We evaluate **seven** AI model–harness configurations on AAArena"*
> 3. *"We evaluate **seven** model–harness configurations with the default 128-small/16-full budgets"*
> ⇒ ✅ **7개 확정.** 🆕 **신종 수치 접근 장애**: 값이 없는 것도, 이미지로 봉인된 것도 아니라 **빌드 파이프라인이 삭제했다.** → [[매크로-미치환]](신설) · cf. [[벤치마크-이미지-봉인]] · [[배포출처-봉인]]

> [!warning] 🔴🔴 **"금메달 6개"는 압도적 우위가 아니다 — 2위가 4개다**
> 본문 표 말미 `Gold medals ↑` 행 실측: **6 · 4 · 4 · 2 · 2 · 3 · 1** (7개 구성)
> ⇒ 🔴 **1위 6개, 2위 그룹 4개 둘.** 격차는 **2개**다.
> 📌 수집기 한줄요약 *"Opus5.5+Claude Code 구성이 금메달 6개를 얻었으나 나머지 6개 인간 래더는 평가된 어떤 구성도 1위를 못 했다"* 는 **틀리지 않았지만**, **2위가 4개라는 사실이 빠지면 "한 구성만 되는 과제"처럼 읽힌다.** 실제로는 **여러 구성이 비슷하게 작동한다.** → [[표-부분인용]]
> ✅ 본문도 이를 뒷받침한다: *"**Several configurations** reach rank 1 on Rollman and AquaWar, whereas only Opus5.5…"*

> [!insight] 🏆🏆 **논문이 하네스 교란을 스스로 적는다 — [[자기제한-명시]] 의 강한 사례**
> 본문 Setup 원문:
> > *"All models use **max reasoning effort**. **Opus5.5 uses Claude Code; the other models use Codex, so the comparison includes both model and harness differences.** Runs stop upon reaching rank 1. We repeat each setting **three times and report the median result**."*
>
> 🎯 **즉 1위 구성만 다른 하네스를 쓴다.** 논문은 그것을 숨기지 않고 *"the comparison includes both model and harness differences"* 라고 **먼저 선언한다.**
> ⇒ 🔴 **따라서 "Opus5.5가 가장 강하다"는 결론은 이 데이터로 내릴 수 없다.** 6 vs 4 의 2개 차이가 **모델 효과인지 Claude Code 하네스 효과인지 분리되지 않았다.**
> 🏆 그런데 **이것이 감점이 아니라 가점이다** — 유인에 반해 스스로 적었다. → [[숨김유인-부호]] 반례 추가 · [[하네스-설계-축]]
> 🔗 **금일 배치 내 대조**: [[Qwen3.8-27B]] 는 **반대 방향**이다 — 모든 코딩 벤치를 **Claude Code 하네스로 통일**해 측정했다(경쟁사 하네스). ⇒ 📌 **하네스 축의 양면이 같은 날 도착했다**: AAArena는 *하네스가 달라서 교란*, Qwen은 *하네스를 통일했으나 그것이 경쟁사 것*.

> [!note] 🏆 **규칙 복잡도를 AST 노드 수로 측정했다 — 정량화가 깔끔하다**
> 본문: 12게임을 *"in ascending **rule-description size (abstract syntax tree node count)**"* 로 정렬한다. 실측 예: **Miracle 4,391 · LOTA 4,513 · AntWar2 6,368** 노드.
> 🎯 그리고 초록 주장 *"Performance is generally weaker in games with **more complex rule specifications**"* 가 이 축 위에서 나온다. ⇒ 📌 **"복잡한 규칙에서 약하다"가 인상이 아니라 측정값에 연결돼 있다.**
> ✅ 확인된 게임명(일부): **Rollman · AquaWar · Pacman · AntWar · AntWar2 · Miracle · LOTA · ProxyWar**. 🔴 12개 전체 목록은 Table 1 이미지/표 영역이라 **4개는 미확정**.

> [!warning] ⚠️ **비규칙 비중 ↔ Elo 상관은 0.35 — 약하다**
> 본문: *"Within each game, we correlate **non-rule share** (1 − rule-based fraction) with Elo across the seven configurations, using average ranks for ties. The **mean Spearman correlation across 12 games is 0.35**."*
> ⇒ 📌 **0.35는 약한 양의 상관**이다. "규칙 기반 코드 비중이 낮을수록(=학습된 휴리스틱 비중이 높을수록) Elo가 높다"는 경향은 있으나 **설명력이 작다.**
> ⚖️ 논문은 이 값을 과장하지 않고 그대로 적는다. 📌 **n=7 구성 기준의 게임별 상관을 12개 평균한 값이므로 표본이 매우 작다** — 볼트는 이 수치를 방향 참고로만 쓴다.

> [!note] ✅ 볼트 실측
> arXiv API + HTML 본문 실조회(2026-10-12): `2610.12341` · **published 2026-10-08T17:15:48Z** · **cs.AI, cs.CL** · 저자 **27명**(Kaisen Yang, Qingle Liu, Kejin Wang, Yicheng Zhao, Jieming Li, Shenghan Zheng, Ruize Yang, Bojun Yang 외) · HTML 549,355B → 본문 68,921자
> ✅ 벤치 규모 일치: **12개 실제 대전게임 · 1,920개 아카이브 인간 프로그램**
> 📌 평가 프로토콜: **128-small/16-full 예산 · retained-champion 스코어링 · 3회 반복 중앙값 · rank 1 도달 시 중단 · max reasoning effort 통일**
> 🆕 본문 등장 빈도: **GLM-5 계열 21회 > Opus5 13회** — 부록에 *"complete trajectories of the twelve GLM-5.x"* 궤적 분석이 있다. ⇒ 📌 **7개 구성의 전체 모델 명단은 미확정**이나 GLM-5 계열이 다수 포함된 것으로 보인다(볼트 추정, 확정 아님).

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐⭐⭐⭐⭐ — 업보트 40, arXiv cs.AI, **저자 27명**, 1,920개 인간 프로그램 아카이브. 🏆 **실험 규율이 금일 배치 최상위**: 3회 반복 중앙값 · 추론노력 통일 · 하네스 차이 자발 공개 · 규칙 복잡도 정량화. 🔴 감점: `\val{}` 미치환 배포, 12게임 목록 일부 미확정.
- **즉시 활용**: 🟡 **부분 YES — 개념만.** 벤치 자체를 돌릴 일은 없다. 🎯 **그런데 AHL 구조(가중치 고정 + 에이전트가 정책 코드를 반복 수정 + 리플레이 피드백)는 내 작업에 바로 대응된다**: 볼트 운영 자체가 그 형태다(스킬 코드를 고치며 결과를 누적). 본문 결론 중 *"**opponent selection and dense feedback** support policy improvement"* 와 *"agents learn from both **on-policy** replays of their own matches and **off-policy** replays of other players' matches"* 가 실무 지침으로 쓸 만하다.
- **6개월 영향력**: **중간~높음**. 📌 *"model weights fixed"* 로 성능을 올리는 경로가 정량화되면, **모델 교체 대신 하네스·루프 개선에 투자하는 판단**이 정당화된다. 이는 비용 구조를 바꾼다.
- **대체 관계**: 게임 에이전트 RL 벤치를 보완. 내 도구를 대체하는 것은 없다. 🎯 단 **"하네스를 바꾸면 결과가 바뀐다"는 증거**로서 [[하네스-설계-축]] 을 강화한다.
- **허와 실**: ✅ **실이 매우 강하다** — 불리한 사실(하네스 혼입, 6개 래더 미정복, 상관 0.35)을 **모두 본인이 적는다**. 🔴 허라고 할 것은 **배포 품질**(`\val{}` 미치환)뿐이다.
- **액션**: ✅ **즉시 적용 1개** — 아래 action.

> [!action] 당장 할 것
> 🎯 **볼트 운영에 두 가지를 반영한다.**
> 1. **off-policy 리플레이 활용** — 본문: 에이전트는 *"자기 경기의 on-policy 리플레이"* 와 *"다른 플레이어 경기의 off-policy 리플레이"* **양쪽에서 배운다**. ⇒ 📌 볼트에서는 **수집기의 자기보고(남의 리플레이)** 가 off-policy 리플레이에 해당한다. 지금까지도 쓰고 있으나, **"수집기 보고를 체계적 학습 입력으로 본다"** 는 근거가 생겼다.
> 2. **dense feedback** — 매 배치 1회 평가보다 **중간 피드백이 정책 개선을 돕는다**는 결과. ⇒ 볼트 log.md 의 배치별 기록이 그 역할이다. **유지한다.**

> [!question] 미해결 질문
> 1. 🔴 **7개 구성의 전체 모델 명단** — Claude Code 1개 + Codex 6개는 확정, 모델명 전부는 미확정.
> 2. 🔴 **12게임 전체 목록** — 8개 확인, 4개 미확정(Table 1 영역).
> 3. 🔴 `128-small/16-full` **예산의 정확한 의미**(경기 수 단위 추정, 확정 아님).
> 4. 🔴 **1,920개 인간 프로그램의 출처 대회** — "real-world game competitions" 만 명시.
> 5. `\val{completedmodels}` 가 **v1 이후 수정됐는지** — 재확인 미실시.

## 관련 페이지
- [[매크로-미치환]] — **본 소스가 최초 사례** (신설)
- [[하네스-설계-축]] — Opus5.5만 Claude Code, 나머지 Codex
- [[자기제한-명시]] · [[숨김유인-부호]] — 하네스 교란 자발 공개
- [[표-부분인용]] — 금메달 6 vs 2위 4
- [[하네스형-에이전틱-RL]] · [[에이전트축-분기]] · [[AI-에이전트-프레임워크]]
- [[Claude-Code-워크플로우]]
- [[Qwen3.8-27B]] — **같은 날, 하네스 축의 반대면**
- [[Anthropic]] · [[Zhipu-AI]]
- [[DiffusionART]] · [[Reflex]] · [[SoftwareGym]] · [[VisionWeave]] — 2026-10-12 동일 배치
- [[ai-news]]

## 원본
- 출처: https://huggingface.co/papers/2610.12341 · arXiv `2610.12341`
- 볼트 실측(2026-10-12): arXiv API(초록) **+ HTML 본문**(`arxiv.org/html/2610.12341v1`, 549,355B → 본문 68,921자)
- HF 데일리: 업보트 **40** · published **2026-10-08T17:15:48Z**
- raw 대비: ✅ 12게임·1,920프로그램·금메달 6·나머지 6래더 미정복·규칙복잡도 경향 **일치** · 🏆 **볼트 해소: 평가 구성 = 7개 (3중 교차)** · 🏆 **볼트 신규: 금메달 분포 6/4/4/3/2/2/1 — 2위가 4개** · 🏆 **볼트 신규: 하네스 교란 자기인정 원문** · 🏆 **볼트 신규: Spearman 0.35 · AST 노드 수 정량화 · 3회 중앙값** · 🆕 **"오타"가 아니라 LaTeX 매크로 미치환으로 재판정**
- 신뢰도: ⭐⭐⭐⭐⭐ (실험 규율 금일 최상 / 배포 품질 결함, 명단·게임목록 일부 미확정)
