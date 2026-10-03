---
title: On-Policy or Off-Policy Learning? — "온폴리시가 본질적으로 낫다"를 통제 실험으로 반박
type: source
domain: local-llm
tags: [ai-news, hf-paper, distillation, on-policy, off-policy, kl-divergence, rlvr, catastrophic-forgetting, cambridge]
created: 2026-10-03
updated: 2026-10-03
sources: []
reliability: high
---

# On-Policy or Off-Policy Learning? (2609.35259)

> [!insight] 핵심 인사이트
> **온폴리시의 가치는 목적함수에 의존한다 — 롤아웃 정책 자체는 중심 역할을 하지 않는다.**
> strong-to-weak 증류에서 **롤아웃 정책 · 토큰 수준 KL 방향 · 학습률**을 **독립적으로 변화**시킨 통제 실험. 통념과 반대 결론: 성능과 **출력 커버리지**를 더 분명히 결정하는 것은 **KL 방향**이고, **망각과 업데이트 희소성을 지배하는 것은 학습률**이다. **forward KL 은 롤아웃 정책 변화에 현저히 견고**하고 **reverse KL 만 민감해 학생 생성 롤아웃을 선호**한다.
> 🎯 즉 *"온폴리시가 낫다"* 는 주장은 **reverse KL 을 쓸 때만 성립하는 국소 참**이었다.

## 도메인별 추출 (local-llm · 증류/후처리)

- **실용성 판단**: 🟡 **직접 적용 가능한 설계 규칙을 준다.** 작은 모델에 큰 모델을 증류할 때 **① 목적함수(KL 방향)를 먼저 고정하고 ② 그 다음에 롤아웃 정책을 고를 것.** forward KL 을 쓰면 비싼 온폴리시 롤아웃 생성 비용을 아껴도 성능이 안정적이다. 🔴 **단 수치가 초록에 0개**여서 "얼마나 아껴도 되는가"는 모른다.
- **모델/과제 범위**: **Llama3 · Qwen2.5 계열** × **과학 · 의학 · 산술 추론**. 📌 두 계열 2종 뿐이라 **계열 일반화는 주장되지 않았다**(저자도 "families"로만 적는다).
- **트레이드오프**: **KL 방향 = 성능·커버리지** / **학습률 = 망각·업데이트 희소성**. ⇒ ⚖️ **두 축이 분리된다**는 것이 이 논문의 실질 기여다. 종전에는 "온폴리시 vs 오프폴리시" 단일 축으로 섞어 보고 있었다.
- **🟡 온폴리시가 이긴 구간도 있다(저자가 적는다)**: Countdown 산술의 **더 어려운 변형**에 대한 일반화는 **양쪽 KL 모두에서** 온폴리시 데이터로 개선된다. 🔴 **그런데 후속 RLVR 이후에는 그 이점이 신뢰성 있게 유지되지 않는다**(*"does not reliably persist"*).
- **오픈소스 구현체**: 🔴 **없다.** HF API `githubRepo` = `None` · `projectPage` = `None` · 초록에 코드 선언 0건 → [[선언된-구현체-공백]] 의 **"선언 자체가 없는" 유형**.

> [!insight] 🏆 기전을 두 경로로 뒷받침한다 — 수집기가 생략한 부분
> 수집기 요약은 결론만 전했으나 초록 전문에는 기전 근거가 **2가지**로 적혀 있다: ① **KL 그래디언트 분석** ② **연속적인 student-teacher 롤아웃 정책 스펙트럼 실험**(*"a continuous student-teacher rollout-policy spectrum"*). ⇒ 📌 **이진 비교(온/오프)가 아니라 연속 스펙트럼으로 봤다**는 것이 이 논문이 기존 비교 연구와 다른 지점이다.

> [!warning] 🔴 수집기 인용이 결론의 3분의 1만 전했다
> 수집기는 *"온폴리시의 가치는 **목적함수**에 의존한다"* 로 요약했다. 초록 원문 마지막 문장은 가치가 **세 가지**에 의존한다고 적는다:
> *"their value depends critically on the **objective, evaluation setting, and optimisation hyperparameters**."*
> ⚖️ **목적함수 · 평가 설정 · 최적화 하이퍼파라미터 3개 중 1개만 인용됐다.** 인용 규약상 **3개를 함께 적는다** → [[표-부분인용]] · [[복합지표-분해]].

> [!insight] ✅ 견고성 자발 공개 — 반증 조건을 스스로 적었다
> *"Our broader conclusions remain robust to **removing gradient clipping**, using **sampled KL estimators**, and training on tasks requiring **longer reasoning chains**."*
> ⇒ **3가지 교란 조건에서 결론이 유지된다**고 명시한다. [[자기제한-명시]] 의 변종인 **"견고성 범위 명시형"**. 🔴 **단 "유지된다"는 서술이고 수치가 아니다.**

> [!warning] 🔴 정량 수치 0개 — 볼트 대조 불가
> 초록 **1,802자 전문 전수 검색** 결과 성능 수치 **0개**. *"more clearly shapes"* · *"remarkably robust"* · *"substantially more sensitive"* 등 **비교 서술만** 있다.
> 🔴 **그리고 수집기는 초록 길이를 "1,900자"로 보고했으나 볼트 실측은 1,802자**(+98자 = **+5.4% 과대**). 📌 사소하나 [[단위-불일치]] 축에 기록한다 — 수집기가 길이를 반올림/추정했다.

> [!question] 미해결 질문
> - forward KL 이 견고한 **기전**이 무엇인가(그래디언트 분석의 결론을 초록이 요약하지 않는다 — PDF 확인 필요).
> - **RLVR 이후 온폴리시 이점이 사라지는 이유**가 무엇인가. 🎯 이것이 같은 배치의 [[Sharpening-Tax]] 와 **직접 맞물린다** — 그쪽은 RL 후처리가 **커버리지를 깎는다**고 측정한다.

## 🎯 같은 배치 교차 발견 — 2건이 "커버리지"를 같은 통화로 쓴다
- 이 논문: **KL 방향이 "task performance and output coverage" 를 결정**한다.
- [[Sharpening-Tax]]: **RL 후처리가 pass@1 을 올리고 solution coverage 를 깎는다.**
⇒ ⚖️ **증류 목적함수 쪽과 RL 후처리 쪽에서, 같은 날 두 팀이 독립적으로 "커버리지"를 핵심 비용으로 지목했다.** 📌 그리고 **둘 다 Countdown 과제를 쓴다**([[HC-DLM]] 까지 포함하면 **오늘 5건 중 3건이 Countdown 공유**).
🔴 **단 이 논문은 "커버리지"를 정의하지 않고 쓰며 측정 지표도 적지 않는다** — Sharpening Tax 쪽은 pass@K 로 조작화한다. **같은 단어가 같은 것을 재는지 미확인.**

## 관련 페이지
- [[Sharpening-Tax]] — 같은 배치 · 커버리지를 같은 통화로 사용
- [[HC-DLM]] — 같은 배치 · Countdown 공유
- [[Beyond-Memory-PoS]] — 같은 배치
- [[local-llm]] · [[에이전트-메모리-레이어]]
- [[하네스-설계-축]] · [[선언된-구현체-공백]] · [[표-부분인용]] · [[자기제한-명시]]
- [[Cambridge-University]]

## 원본
- 출처: https://huggingface.co/papers/2609.35259
- 제목(원문): *On-Policy or Off-Policy Learning? A Systematic Study of Distillation Dynamics*
- **볼트 독립 검증**: upvote **130**(수집기 130 = 드리프트 0) · publishedAt **2026-09-28** ✅ · 저자 **3명** ✅ · 초록 **1,802자**(🔴 수집기 1,900자)
- 소속: **University of Cambridge** (HF API `organization`)
- 10-02 게시분 **upvote 2위**
- 신뢰도: ⭐⭐⭐⭐ (통제 실험 설계 + 견고성 자발 공개 / 🔴 수치 0개 · 구현체 0건)
