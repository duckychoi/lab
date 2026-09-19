---
title: RSI 프레이밍 — 두 조직이 같은 달에 "재귀적 자기개선"을 미래형으로 썼다
type: concept
domain: ai-news
tags: [ai-news, concept, rsi, 한정어, 마케팅, 신설]
created: 2026-09-18
updated: 2026-09-19
sources: [SoL-Pi.md, NeoHorse-1-4B.md, NeoHorse-1-9B.md, TokenRhythm.md, NeoHorse-1-Paper.md, ModularRSI.md, RSIAgent.md]
reliability: medium
---

# RSI 프레이밍

> [!insight] 한 줄
> **2026-09 에 두 독립 조직이 "재귀적 자기개선(RSI)"을 채택했고, 양쪽 다 달성이 아니라 지향으로 적었다. 저자는 선을 지켰고 — 넘는 것은 요약하는 쪽이다.**


> [!insight] 🆕 2026-09-19 — 모논문 본문이 **"루프 1회"를 저자 서술로 확정**했다 → [[NeoHorse-1-Paper]]
> *"The results also reflect a **single pass** of the evaluation–selection–update loop"* · *"an **initial attempt** at recursive self-improvement **rather than a definitive demonstration**"*.
> 🎯 볼트 캔버스의 "RSI 최소조건 = 루프 2회, 아직 1회"가 **추정에서 저자 확인으로** 올라갔다. **이 논문은 [[자기제한-명시]] 의 모범 사례다** — 제목·초록·결론·한계 절 네 곳이 전부 미래형/한정형.
> 🔴 **정정**: 사례 ②의 "업보트 421 · ★535"는 09-19 실측 **170 · ★599(GitHub)**. 그리고 ★599 레포는 **학습 코드가 없다**(README·PDF·추론 예제 2개) — "코드 공개"로 읽지 말 것.
> ❓ 아래 "둘이 왜 같은 단어를 골랐나"의 ②(한쪽이 다른 쪽을 따랐다)는 **여전히 미확인** — NeoHorse 본문의 RSI 인용은 [11, 31]이고 SoL-Pi 인용 여부는 볼트가 대조하지 않았다.

## 사례 2건, 같은 달, 다른 조직

**① [[SoL-Pi]] — [[NVIDIA]] NVlabs · 2026-09-17 · 업보트 35 · ★2,185**
초록: *"We take an **RSI-inspired** approach at the harness layer"*
🎯 **`-inspired`** 가 한정어다. RSI를 했다고 하지 않고 **RSI에서 착상했다**고 적었다.
✅ 그리고 **주장은 효율 수치로 한정**된다 — 토큰 44.7~49.0% 절감, 정확도는 *"comparable"*(동등). **능력 개선을 주장하지 않는다.**

**② [[TokenRhythm]] — 논문 `arxiv:2609.08183` · 2026-09-08 · 업보트 421 · ★535**
제목: *"**Towards** Recursive Self-Improvement via Agentic Post-Training with Routing Harness"*
모델 카드: *"RSI를 향한 **초기 프로토타입**"* · *"extending this loop across successive iterations is the **next step**"*
🎯 **`Towards` · `초기 프로토타입` · `next step` — 세 곳 모두 미래형이다.**

## 🎯 공통 구조 — RSI는 결과가 아니라 **동기 서술**로 쓰인다

두 사례 모두 같은 자리에 RSI를 놓는다: **"왜 이 일을 하는가"** 의 답이고, **"무엇을 달성했는가"** 의 답이 아니다.
실제 달성분은 둘 다 **측정 가능한 좁은 것**이다 — 토큰 절감률(SoL-Pi) · 10벤치 평균 +5.93(NeoHorse).

📌 **볼트 판정: 이건 과장이 아니다.** [[자기제한-명시]] 의 기준으로 보면 **양쪽 다 합격**이다 — 자기 주장의 상한을 스스로 적었다.
🔴 **위험은 전달 단계에 있다.** *"RSI를 구현한 모델"* 로 한 단계만 옮기면 저자가 쓰지 않은 주장이 된다 → [[한정어-탈락]]

## 🔴 그런데 왜 둘이 같은 단어를 골랐는가 — 볼트가 모르는 것

같은 달, 다른 조직(NVIDIA vs 미상), 같은 프레이밍, **둘 다 하네스 층**.
🎯 **가능한 설명 셋, 구분 불가**: ① 분야 어휘가 실제로 이동했다 ② 한쪽이 다른 쪽을 따랐다(NeoHorse 논문이 9일 먼저다) ③ 자금·주목 환경이 이 단어를 보상한다.
🔴 **볼트는 SoL-Pi 본문을 읽지 않았고 인용 관계를 확인하지 않았다.** 🎯 **NeoHorse 논문이 업보트 421인데 볼트에 없다**([[선발창-누락]]) — **그것을 읽으면 ②를 확인할 수 있다.**

## 볼트 규율 — 이 단어를 만났을 때

1. **시제를 먼저 본다** — `towards` · `-inspired` · `next step` · `초기` 는 **전부 미래형 표지**다
2. **측정된 것만 옮긴다** — RSI는 동기, 숫자는 결과. **둘을 같은 문장에 넣지 않는다**
3. 🔴 **"루프가 반복됐다"는 증거를 요구한다** — RSI의 최소 조건은 **2회 이상의 반복**이고, 두 사례 모두 *"다음 단계"* 라고 적었다 = **아직 1회다**
4. ✅ **한정어를 지운 요약을 발견하면 원문 시제로 되돌린다**

> [!question] 미해결
> **RSI 주장의 최소 검증 기준이 무엇인가.** 🔴 볼트에 기준이 없다. *"루프 2회 이상 + 각 회차 성능 기록"* 이 후보이지만 **어느 논문도 그 형태로 보고하지 않는다.**
> 그리고 **이 어휘가 몇 건까지 늘어나는지 세어야 한다** — 2건은 우연일 수 있다. 📌 **다음 배치부터 `RSI`·`self-improving`·`recursive` 를 카운트한다.**


> [!insight] 🆕 2026-09-19 — **7일간 "RSI" 명칭 논문 5건, 개선 대상이 4종으로 갈렸다**
> 가중치([[NeoHorse-1-Paper]], 루프 1회) · **하네스 코드**([[ModularRSI]], 3 에폭×5모듈+통합 = 16 에폭·generation 14) · 탐색 정책([[Dream-RSI]]) · **메모리 파일**([[RSIAgent]], 학습 없음).
> 🎯 **[[ModularRSI]] 가 "루프 2회+ · 세대별 기록" 최소조건을 형식상 처음 충족**했다 — 단 대상은 가중치가 아니라 하네스 코드.
> 🎯 같은 날 두 논문이 일반화에 **정반대 프로토콜**: ModularRSI 는 벤치와 분리된 2,000과제로만 진화 / RSIAgent 는 목표 과제 자체를 연습.
> 📌 위 "둘이 왜 같은 단어를 골랐나"의 설명 ①(분야 어휘 이동) 쪽으로 기운다 — 4개 논문 모두 NeoHorse(2609.08183)를 인용하지 않는다(서브 조사 확인).

## 관련 페이지
- [[ModularRSI]]
- [[RSIAgent]]
- [[NeoHorse-1-Paper]]
- [[SoL-Pi]]
- [[TokenRhythm]]
- [[NeoHorse-1-4B]]
- [[NeoHorse-1-9B]]
- [[하네스-설계-축]]
- [[선발창-누락]]
- [[한정어-탈락]]
- [[자기제한-명시]]
- [[NVIDIA]]
- [[Dream-RSI]]
- [[AutoResearchClaw]]
