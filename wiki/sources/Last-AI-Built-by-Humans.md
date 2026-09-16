---
title: The Last AI Built by Humans — 제목은 완료형, 초록은 과제 목록
type: source
domain: ai-news
tags: [ai-news, paper, rsi, self-improvement, position-paper, roadmap, overclaim]
created: 2026-09-16
updated: 2026-09-16
sources: []
reliability: low
---

# 논문: The Last AI Built by Humans: Toward Genuine Recursive Self-Improvement

**URL**: https://huggingface.co/papers/2609.11873 · arXiv **2609.11873**
**지표(2026-09-16 볼트 실측)**: 업보트 **84** (raw 83 · 드리프트 **+1**) · 공개 **2026-09-10**

> [!warning] 🔴 [[한정어-탈락]] — **저자가 제목에서 일으킨 격차**
> 볼트가 초록 전문을 대조했다. **제목의 단정성과 초록의 근거 강도가 정면으로 어긋난다.**
>
> | 제목이 주장하는 것 | 초록이 실제로 가진 것 |
> |---|---|
> | *"The **Last** AI Built by Humans"* | — (초록에 이 주장에 대한 근거 문장 **없음**) |
> | *"**Genuine** Recursive Self-Improvement"* | *"identify key **challenges** to achieving genuine RSI"* |
> | (달성 함의) | *"Drawing on ... **preliminary** empirical evidence"* |
>
> 🎯 **초록의 마지막 문장이 이 논문의 실제 결론이다: "진짜 RSI 달성을 위한 핵심 과제들을 식별한다."**
> **달성이 아니라 미달성 과제 목록이다.** 제목은 도착을 말하고 초록은 출발선을 말한다.
> 🔗 09-15 [[Atria-Dawn]] 과 **동일 양식**이다 — 그때도 제목만 *"Superintelligence"* 였고 초록은 시종 한정적이었다. **2배치 연속 같은 패턴.**

> [!note] 논문이 실제로 제공하는 것 — 이건 유용하다
> 과장을 걷어내면 **쓸 만한 구조물이 남는다**:
> 1. **HCI(Headroom-Closed Index)** 로 기존 LLM의 문제를 먼저 드러냄
> 2. **자율성 4단계 + 1 로드맵**: 개선실행 → 개선전략 → 경험획득 → 환경적응 → **재귀적 메타개선**
> 3. **시나리오별 요구 분화**: 과학 발견 · 임바디드 · 소프트웨어 공학 — *"distinct requirements and **development speeds**"*
>
> 📌 **3번이 이 논문의 실질적 기여다** — RSI를 단일 사건이 아니라 **영역마다 속도가 다른 축**으로 본다. 소프트웨어 공학이 먼저 도달하고 임바디드가 늦는 이유를 구조로 설명한다.

## 도메인별 추출 (ai-news)

- **신뢰도**: ⚠️ **low.** 포지션/로드맵 논문이며 **실험 증거가 "preliminary"라고 저자가 명시.** 업보트 84는 이 배치 공동 2위지만 **화제성이 검증가능성과 역상관**인 대표 사례
- **즉시 활용**: 🔴 **NO.** 구현할 것이 없다. **4단계 로드맵을 자기 시스템 위치 파악용 좌표로만** 쓸 수 있다
- **6개월 영향력**: RSI 담론의 **어휘**를 제공할 가능성은 있다(HCI · 자율성 단계). **능력 변화를 만들지는 않는다**
- **대체 관계**: 없음 — 도구가 아니라 관점이다
- **허와 실**: 🎯 **제목을 빼고 읽으면 정직한 서베이다.** 제목만 다른 장르에서 왔다

> [!action] 볼트 규칙 적용 확인
> 09-15 볼트 요청 — *"다음 배치부터 **논문 제목 원문을 함께 배달**할 것"* — 을 수집기가 **이행했다.** 이번 raw.md 항목에 제목이 원문으로 적혀 있어 볼트가 즉시 대조할 수 있었다. **규칙이 작동했다.**

> [!question] 미해결
> HCI(Headroom-Closed Index)의 **계산 방식과 검증 상태**를 초록만으로는 알 수 없다. 이것이 기존 지표의 재포장인지 새 측정인지 **본문 확인 필요** — [[측정도구-먼저-반증]] 대상.

## 관련 페이지
- [[Atria-Dawn]] — 2배치 연속 동일 양식(제목발 과장)
- [[한정어-탈락]] — 저자 제목발 변종의 두 번째 사례
- [[측정도구-먼저-반증]] — HCI 미검증
- [[Continual-Learning-Compose]] — 같은 배치 **정반대 극**(자기 실패를 먼저 적음)
- [[ai-news]]

## 원본
- 출처: https://huggingface.co/papers/2609.11873
- 검증: HF papers API 실호출(2026-09-16) — **초록 전문 대조** · 제목 원문 확인 · 업보트 +1
- 신뢰도: ⭐ (low)
