---
title: SWE-Bench Pro Verified — 표준 벤치가 오염됐다는 교정판
type: source
domain: ai-news
tags: [ai-news, hf-paper, benchmark, coding-agent, evaluation, reward-hacking, reliability]
created: 2026-09-12
updated: 2026-09-12
sources: []
reliability: high
---

# SWE-Bench Pro Verified (2609.08149)

> [!insight] 핵심 인사이트 — **업보트 최하위인데 오늘 배치에서 가장 실무를 바꾸는 논문**
> HF 업보트 **22**(2026-09-12 API 실호출 · raw와 **일치**) — **오늘 논문 5건 중 최저**. published **2026-09-08** · 저자 **8인**(Pujun Zheng, Zixin Shang, Shufan Jiang, Wenhui Tian, Dongsheng Zhu 외).
> 주장: *"SWE-Bench Pro has emerged as a **standard benchmark**"* 인데 그 평가가 **두 갈래로 무너져 있다**:
> - **리워드 해킹** — *"enabled by **leakage of gold solutions or hidden evaluation information**"* (정답 유출 · 숨은 평가정보)
> - **태스크 품질 문제** — *"**misleading problem statements** and **improperly scoped tests**"* (오도하는 문제 서술 · 잘못 설정된 테스트 범위)
>
> 처방: 정상 에이전트 동작을 방해하지 않으면서 주요 유출 경로를 제거하는 **안티해킹 안전장치** + 결함 인스턴스를 **최소 수정**하는 태스크 정제.
> 🎯 결론이 이 논문의 값이다: *"Evaluations on SWE-Bench Pro Verified reveal that **some models perform substantially worse than previously reported**, suggesting that existing results **may overestimate real software engineering capability**."*

> [!warning] 🔴 볼트에 즉시 적용 — **인용한 벤치 수치의 버전을 확인해야 한다**
> raw 판정(*"벤치 인용 시 버전 확인 필요"*) **정확하고, 볼트에 직접 해당한다.**
> 볼트에는 **SWE-bench 계열 수치를 인용한 페이지가 이미 여럿 있다** — 예: [[MiniCPM5-2B]] 의 *"SWE-bench Verified **46.4** vs 차상위 36.8"*(09-10 기록), [[SWE-bench-Science]](08-21) 등.
> → ⚠️ **다만 정확히 구분해야 한다**(여기서 실수하면 이 논문의 교훈을 잘못 적용한다):
> - 이 논문이 교정한 것은 **SWE-Bench *Pro***다
> - MiniCPM5-2B가 인용한 것은 **SWE-bench *Verified***(원조 SWE-bench의 검증 서브셋)로 **다른 벤치다**
> → 🎯 즉 **볼트의 기존 수치가 자동으로 무효가 되는 건 아니다.** 대신 규칙이 하나 생긴다: **"SWE-bench"라는 이름은 최소 4개 변종(원조 · Verified · Pro · Pro Verified · Multimodal 등)을 가리키므로, 이름만으로 같은 벤치라고 가정하지 말 것.**
> → 이것은 [[단위-불일치]] 의 **벤치마크판**이다 — 같은 이름의 수가 다른 것을 센다.

> [!insight] 🎯 오늘 배치의 짝 — [[T1]] 과 정확히 맞물린다
> 같은 날 [[T1]] 은 초록에서 **선제적으로** 이렇게 방어했다: *"isolated seeds and synthesized tasks **disjoint from Terminal-Bench 2.1** ensures gains reflect **genuine capability transfer over benchmark overfitting**."*
> → **한쪽은 오염을 실증하고(SWE-Bench Pro Verified), 한쪽은 오염되지 않았다고 선언한다(T1).**
> → 그런데 이 논문이 보여준 것은 정확히 **"저자 선언으로는 부족하고 제3자가 감사해야 드러난다"** 이다. SWE-Bench Pro도 발표 당시 오염을 의도하지 않았다.
> → 🎯 **그래서 T1의 분리 선언도 현재는 미검증 상태로 남겨야 한다.** 두 논문을 함께 읽으면 결론이 이렇게 된다: **에이전트 벤치 수치는 「누가 감사했는가」가 「몇 점인가」보다 먼저다.**
> → 볼트의 [[측정도구-먼저-반증]] 개념이 세 번째 실증 사례를 얻었다.

> [!question] 초록만으로는 남는 것
> - **어떤 모델이 얼마나 떨어졌는지** 초록에 없다(*"some models... substantially worse"* 라는 서술만). **교정 전후 표가 본문에 있을 것** — 인용하려면 본문 확인 필요
> - **누가 만들었는가**: 원 SWE-Bench Pro 팀의 자체 교정인지 제3자 감사인지 초록에 없다. **이 논문 자신의 독립성**이 곧 신뢰도이므로 중요한 미확인 항목
> - 교정판이 **커뮤니티 표준으로 채택될지** 미지수 — 리더보드가 옮겨가지 않으면 오염된 수치가 계속 인용된다

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐⭐⭐ — HF API 업보트 실호출 + **초록 원문 전문 대조**. 주장이 검증 가능한 형태(교정판 공개 + 재평가 결과)이고 **자기 이익에 반하는 방향**(기존 수치를 깎는다)이라 동기 왜곡이 적다 → **high**. ⚠️ 단 구체적 하락폭·독립성은 본문 미확인.
- **즉시 활용**: **YES — 오늘 배치에서 가장 즉시 적용 가능한 항목.** 도구를 설치할 필요가 없다. **볼트 인제스트 규칙 한 줄**로 끝난다: 벤치 수치를 옮길 때 **벤치 이름의 정확한 변종과 버전을 함께 적는다.** 비용 0, 효과 즉시.
- **6개월 영향력**: 코딩 에이전트 마케팅의 근거가 흔들린다. 모델 벤더가 인용하는 SWE-Bench 계열 점수는 **버전 명시 압박**을 받게 된다. 그리고 이 흐름이 **다른 에이전트 벤치로 번질 가능성**이 높다(같은 오염 기전 — 유출·테스트 범위 — 은 특정 벤치의 문제가 아니다).
- **대체 관계**: SWE-Bench Pro를 **대체하는 것이 목적**인 논문. 볼트 기존 페이지 [[SWE-bench-Science]] 와는 **다른 축** — 저쪽은 *새 도메인으로 확장*, 이쪽은 *기존 벤치를 정화*.
- **허와 실**: 마케팅이 거의 없다. 오히려 **주장을 신중하게 한정**한다(*"suggesting that... **may** overestimate"*). 걷어낼 것보다 확인할 것(본문 수치)이 남은 논문.
- **액션**: 🔴 **볼트 규칙 등재** — 벤치 수치 인용 시 변종·버전 병기(actionable 등록).

## 관련 페이지
- [[T1]]
- [[SWE-bench-Science]]
- [[MiniCPM5-2B]]
- [[측정도구-먼저-반증]]
- [[단위-불일치]]
- [[한정어-탈락]]
- [[hyperresearch]]
- [[ai-news]]

## 원본
- 출처: https://huggingface.co/papers/2609.08149
- 제목 원문: *"SWE-Bench Pro Verified: A Reliable Benchmark for Software Engineering Agents"*
- HF API 실호출(2026-09-12): 업보트 **22**(배치 최저) · published **2026-09-08** · 저자 **8인**
- raw 대비: 업보트 **일치**, 서술 **일치**(리워드 해킹 · 태스크 품질 · 점수 하락 · 버전 확인 필요)
- 신뢰도: ⭐⭐⭐ (초록 원문 대조 / 구체 하락폭·논문 독립성은 본문 미확인)
