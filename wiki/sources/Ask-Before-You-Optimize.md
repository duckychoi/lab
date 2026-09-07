---
title: Ask Before You Optimize — "언제 되물어야 하는가"를 평가 대상으로 만든 벤치마크 (OR-Clarify · InterOPT)
type: source
domain: ai-news
tags: [ai-news, hf-paper, agent, clarification, optimization, operations-research, benchmark, evaluation]
created: 2026-09-07
updated: 2026-09-07
sources: []
reliability: high
---

# Ask Before You Optimize: Dynamic Pre-Formulation Clarification for Interactive Optimization

**arXiv**: 2609.05258 · **HF 업보트 11** · **공개 2026-09-04**
**저자 6인**: Sihan Ge, Yichen Lin, Chenyu Zhou, Jianghao Lin, Tao Yao, Dongdong Ge
**산출물**: **OR-Clarify**(벤치마크) + **InterOPT**(방법)

> [!insight] 핵심 인사이트 — **기존 평가가 "완전한 명세"를 전제해서 놓친 능력**
> LLM이 자연어 서술로부터 최적화 모델을 세우는 일은 이미 흔하다. 그런데 실제 OR(운영연구) 요구는 **불완전하게** 들어온다 — **목적함수·제약·업무 규칙이 빠지면 결과 수리모형 자체가 달라진다.**
> 초록의 결정적 문장: *"Existing evaluations **largely assume a complete specification** and therefore **overlook whether an agent knows when clarification is needed** before modeling."*
> → **평가 설계가 전제를 깔았기 때문에, 측정된 적 없는 능력이 있었다.** 이 논문은 그 능력에 이름을 붙이고 **잴 수 있게** 만든다.
> 볼트 교차: [[검사가능성-공사]] 가 *"무엇을 검사 가능하게 만드는가"* 축이라면, 이건 **"검사되지 않아 존재가 가려진 능력"** 을 드러낸 사례다. **벤치마크의 전제가 능력의 지도를 만든다.**

> [!insight] 이 배치의 반대 극 — [[Enoki]]·[[Motion-Omni]]가 단계를 **없앨** 때, 이건 단계를 **추가**한다
> - [[Motion-Omni]]: 캐스케이드 2패스 **제거**
> - [[Enoki]]: claim↔span 정렬 **제거**
> - **Ask Before You Optimize: 모델링 앞에 "질문" 단계 추가**
> 모순이 아니다. 가르는 변수는 **입력의 완전성**이다 —
> - 입력이 완전하면 중간 변환은 **순손실** → 없앤다
> - 입력이 **불완전**하면 그 사실을 모른 채 진행하는 게 손실 → **되물어야 한다**
> → 볼트의 [[선택비용과-중복성]](*"선택 메커니즘의 가치는 대상의 중복성에 반비례한다"*)과 **같은 형식의 명제**를 다른 변수로 얻었다: **추가 단계의 가치는 입력의 완전성에 반비례한다.**

## OR-Clarify 설계 (초록 실측)

- 각 과제는 **일부만 공개된 문제 서술**을 제시하고, **구조화된 슬롯을 숨긴다**
- **시뮬레이션 사용자**와의 **제한된(bounded) 상호작용**으로 에이전트를 평가
- **개방형(open-ended)** 과 **선택형(choice-based)** 해명 **모두 지원**
- 측정 항목 4종: **슬롯 복구율** · **중단 행동(stopping behavior)** · **암묵적 가정(silent assumptions)** · **상호작용 비용**

> [!insight] **"암묵적 가정"과 "중단 행동"을 잰다** — 이 벤치마크의 진짜 기여
> 슬롯 복구율만 재면 *"무조건 많이 물어보는"* 에이전트가 이긴다. 그래서 **상호작용 비용**과 **중단 행동**을 함께 잰다. 그리고 **암묵적 가정** — *묻지 않고 조용히 채워 넣은 것* — 을 별도로 잰다.
> → **묻지 않는 실패**와 **너무 묻는 실패**를 동시에 처벌하는 구조다. 볼트가 [[에이전트-스킬]] 에서 반복 지적한 *"스킬에는 효과 측정이 없다"* 의 반대 사례이며, **평가 설계가 잘 된 것 자체가 관측 가치**다.

## InterOPT (제안 방법)

**2단계 구조**: ① **미해결 formulation-critical 격차를 식별** → ② 그 격차로 **다음 질문을 할지 멈출지 결정**

| 설정 | 결과 (초록 원문) |
|---|---|
| **선택형(choice-based)** | 정확 슬롯 복구에서 **모든 베이스라인을 크게 상회**(substantially outperforms) |
| **개방형(open-ended)** | 강한 기존 방법과 **대등**(remains competitive) |

> [!warning] 성능은 설정에 따라 갈린다 — 뭉뚱그리면 틀린다
> **선택형에서만 큰 우위**이고 **개방형에서는 대등**이다. 실무의 해명은 대개 **개방형**에 가깝다 → *"질문을 잘하는 에이전트"* 라는 일반화는 **초록이 지지하지 않는다.**
> 🔴 **절대 수치는 초록에 없다.** raw 기재대로이며, 인용은 위 두 표현까지만.

> [!note] 저자들의 재프레이밍 — 이 논문이 남기는 문장
> *"reframe OR assistance as a **selective completeness decision**: **clarify when needed, stop when ready, and quantify what remains missing**."*
> → **"모르는 것을 알고, 물을지 말지 정하고, 남은 결손을 수치화한다."** 이건 OR을 넘어 **에이전트 일반의 요구사항** 서술에 가깝다. 볼트의 [[암묵을-명시로]] 개념과 직접 맞닿는다 — 그 개념이 *"암묵지를 문서로"* 였다면, 여기서는 **"암묵적 가정을 질문으로"** 다.

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐⭐⭐⭐ — 초록 원문 대조·벤치마크와 방법 동시 제시·평가 설계 정교. **감점**: 절대 수치 없음, 공개 여부 미확인.
- **즉시 활용**: **개념은 YES, 코드는 미확인.** 볼트 운영자에게 직접 걸리는 지점: **에이전트가 불완전한 지시를 받았을 때 조용히 가정하고 진행하는 문제**는 OR만의 것이 아니다. `/wiki` 인제스트도 raw 항목이 불완전할 때 **묻지 않고 채운다**(이번 배치 [[humanlayer-skills]] 의 *"3종"* 오류가 정확히 그 사례 — raw를 믿고 실측하지 않으면 그대로 통과했다).
- **6개월 영향력**: **"묻는 능력"이 평가 축이 되면** 에이전트 설계에서 *"항상 진행"* 이 기본값이 아니게 된다. 볼트의 자동 파이프라인에도 **중단 조건**이 필요해진다.
- **대체 관계**: 없음. **평가 공백을 메우는** 논문.
- **허와 실**: OR 도메인 한정 벤치마크다. *"에이전트가 질문을 잘한다"* 로 일반화하면 근거 초과.
- **액션**: 아래.

> [!action] 당장 할 것
> **볼트 인제스트에 "중단 조건" 하나를 도입한다.** 이번 배치가 실증했다 — raw 요약과 실측이 **내용 수준에서 불일치**하면([[humanlayer-skills]]) 진행하지 말고 **원문을 읽는다**. 이 논문의 *"silent assumptions"* 를 볼트 용어로 옮기면 **"raw 요약을 소스로 취급한 것"** 이다. → `actionable.md` 반영.

> [!question] 미해결
> **OR-Clarify 와 InterOPT 이 공개됐는가.** 초록에 공개 선언이 명시되지 않았다(*"We introduce"* 까지). 같은 배치 [[Motion-Omni]]·[[WorldSculpt]]·[[Enoki]] 는 명시적으로 release 를 적었는데 이 논문만 표현이 약하다 — **의도적 차이인지 확인 필요.**

## 관련 페이지
- [[검사가능성-공사]] · [[암묵을-명시로]] · [[선택비용과-중복성]] · [[Enoki]] · [[Motion-Omni]] · [[WorldSculpt]] · [[AI-에이전트-프레임워크]] · [[에이전트-스킬]] · [[humanlayer-skills]] · [[LLM-Wiki]] · [[금융-AI]]

## 원본
- 출처: https://huggingface.co/papers/2609.05258 (arXiv 2609.05258)
- 수집: 2026-09-07 자동수집 (ai-news)
- 검증: HF 논문 API 초록 원문 대조 (2026-09-07 · 업보트 11 raw와 일치)
- 신뢰도: ⭐⭐⭐⭐ (초록 검증 · **절대 수치 미공개** · 공개 여부 미확인)
