---
title: ProgramDistill — 지시문 없이 "동작하는 앱을 조작해" 기능을 알아내게 하는 벤치마크
type: source
domain: ai-news
tags: [ai-news, paper, benchmark, swe, coding-agent, curriculum, difficulty-control]
created: 2026-09-17
updated: 2026-09-17
sources: []
reliability: high
---

# 논문: ProgramDistill: From Interactive Web Apps to Verifiable Reference-Guided SWE Tasks

**URL**: https://huggingface.co/papers/2609.18805
**지표(2026-09-17 볼트 API 실측)**: 업보트 **40** · HF 데일리 **3위** · 게재 **2026-09-16** · 저자 8명
**드리프트**: raw 40 → 볼트 **40 = 0 (완전일치)**

> [!insight] 🎯 **평가의 입력 형식을 바꿨다 — 지시문이 아니라 동작하는 소프트웨어**
> 볼트 초록 전문 대조: *"Coding agents are typically evaluated with desired behavior specified through **issues or instructions**. In practical web development, however, agents may need to **infer behavior from working software** and implement it in an incomplete application."*
> 🎯 **이것이 기여의 핵이다.** 기존 SWE 평가는 목표를 **말로** 준다. 실무에서는 **완성된 참조 앱을 직접 만져 보고** 기능을 알아낸 뒤 미완성 앱에 구현한다.
> 📌 **즉 "명세 이해"가 아니라 "탐색으로 명세 복원"을 잰다** — 태스크의 종류가 다르다.

> [!insight] ✅ 파이프라인이 사람 개입 없이 검증된 태스크를 만든다
> `mine-craft-patch` 파이프라인 실측(볼트 문자 일치): 26개 앱에서 **재생 검증된(replay-verified) 행동 1,975개**를 발견해 **사람 개입 없이 4,063 태스크** 구성.
> 원문: *"discovers 1,975 replay-verified behaviors across 26 applications and constructs 4,063 tasks **without human intervention**"*
> 🔗 **같은 배치 [[ScienceIDE]] 와 정확히 반대 축이다** — 저쪽은 *"expert-defined scientific cases and acceptance criteria"* 를 전제하고, 이쪽은 **사람을 뺐다.**
> 🎯 **가르는 변수는 정답 검증 방식이다**: 웹 앱은 **행동을 재생(replay)해 검증**할 수 있고, 과학 코드는 **정확성 기준이 도메인 특수적**이어서 전문가가 필요하다. → 자동화 가능성은 **도메인이 아니라 검증 가능성이 결정한다.**

> [!warning] 🔴 **지는 축을 초록이 직접 적는다 — 최고 성능도 절반 미달**
> 9개 프런티어 에이전트 평가, 전체 앱 복원의 **누적 워크플로 성공률**:
> - **GPT-6 Astra 49.2%**
> - **Claude Opus 5 28.8%**
>
> 🎯 **1위가 49.2%다** — 즉 **최고 모델도 절반을 못 넘는다.** 그리고 1위와 2위 격차가 **20.4점**으로 매우 크다.
> 📌 볼트 규칙(*지는 축을 함께 적는다*)을 **저자가 스스로 지켰다** → [[한정어-탈락]] 반대 사례. 벤치 제안 논문이 **자기 벤치가 어렵다는 것을 헤드라인 수치로** 보여준다.

> [!insight] 🎯 **난이도가 통제된다는 증거 — 깊이 하나가 축이다**
> 부분 앱 복원에서 **복원 깊이를 1 → 8** 로 올렸을 때:
> - **100% → 64.0%**
> - **96% → 32%**
>
> 🎯 **단일 파라미터로 성공률을 100%에서 32%까지 끌어내린다.** 이것이 *"controlled difficulty"* 주장의 실체이며, **벤치마크가 포화되지 않도록 조절 가능**하다는 뜻이다.
> 🔗 [[수확체감-변곡점]] 과 **반대 방향의 같은 도구**다 — 저쪽은 *"어디서 이득이 꺾이나"*, 이쪽은 *"어디서 난이도가 꺾이나"*. **둘 다 단일 축을 여러 점에서 재야 보인다.**
> 저자 직접 언급: *"a natural basis for **future curriculum-based training**"* — 커리큘럼 학습의 근거로 쓸 수 있다.

> [!note] 🔴 볼트가 짚는 미해결 — 두 계열의 시작점이 다르다
> 부분 복원 결과가 **100%→64.0%** 와 **96%→32%** 두 쌍으로 제시된다. 초록은 **두 계열이 무엇인지 밝히지 않는다**(모델별? 앱 카테고리별? 태스크 입도별?).
> 🎯 중요한 이유: 시작점이 100%와 96%로 **거의 같은데 끝점이 64.0%와 32%로 두 배 차이**다. **같은 깊이 증가가 한쪽에서 두 배 더 치명적**이라는 뜻이며, **무엇이 그 차이를 만드는지가 이 벤치의 가장 유용한 정보**일 수 있다. **본문 확인 대상.**

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐⭐⭐ high. 🎯 **분모 전부 공개**(26앱·1,975행동·4,063태스크·9에이전트) · **지는 축 자발 공개**(49.2%/28.8%) · **난이도 통제 증거 제시**. 볼트가 검증할 수 있는 형태로 다 적혀 있다
- **즉시 활용**: **NO**(벤치 실행 인프라 필요). 🎯 **다만 수치는 즉시 쓸 수 있다** — *"프런티어 에이전트가 참조 앱 복원에서 49.2%"* 는 에이전트 능력 상한의 **인용 가능한 바닥값**
- **6개월 영향력**: 🎯 **높음.** ① 최고가 49.2%면 **헤드룸이 크다** → 후속 연구가 몰린다 ② 깊이 파라미터로 **포화 방지**가 되므로 오래 쓰인다 ③ 커리큘럼 학습 데이터로 재사용 가능
- **대체 관계**: SWE-bench 류를 **대체하지 않고 다른 능력을 잰다**(명세 이해 vs 명세 복원). 🔗 [[ScienceIDE]] 와는 **도메인 분업**
- **허와 실**: 🎯 **허가 없다.** 자기 벤치에서 최고 모델이 절반 미달임을 앞세운다 — 과장할 유인이 있는 자리에서 **반대로 갔다**
- **액션**: 🎯 **GPT-6 Astra 49.2% / Claude Opus 5 28.8% 를 볼트 에이전트 능력 기준선으로 등재.** 볼트가 인용해 온 SWE 수치들과 **측정 대상이 다름을 명시**해야 함

## 관련 페이지
- [[ScienceIDE]] — 🎯 **같은 배치·반대 자동화 축**(전문가 정의 vs 사람 개입 없음) · 가르는 변수는 **검증 가능성**
- [[수확체감-변곡점]] — 단일 축 다점 측정의 같은 도구 · [[한정어-탈락]] — 지는 축 자발 공개 사례
- [[검사가능성-공사]] — replay-verified 가 검증을 먼저 만든 구조
- [[cline]] · [[anthropic-claude-code]] · [[openai-codex]] — 평가 대상 에이전트 계열
- [[HuggingFace]] · [[ai-news]]

## 원본
- 출처: https://huggingface.co/papers/2609.18805
- 검증: HF papers API 실호출(2026-09-17) · **초록 전문 대조** — 수집기 인용 **전건 문자 일치**(1,975 · 26앱 · 4,063 · 49.2%/28.8% · 100→64.0/96→32 · `without human intervention` · `curriculum-based training`)
- 신뢰도: ⭐⭐⭐
