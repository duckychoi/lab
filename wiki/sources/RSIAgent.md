---
title: "RSIAgent — '오픈 모델이 GPT-6를 넘었다'의 대부분은 RSI가 아니라 하네스 몫이다"
type: source
domain: ai-news
tags: [ai-news, hf-paper, agent, rsi, agent-memory, computer-use, osworld, multi-agent, training-free, 비교조건]
created: 2026-09-19
updated: 2026-09-19
sources: [NeoHorse-1-Paper.md, ModularRSI.md, Kimi-K3.md, GLM-5.3.md]
reliability: medium
---

# RSIAgent (arXiv 2609.15364)

> [!insight] 핵심 인사이트 — **비교 조건 판정: 폐쇄 모델은 메모리도, 같은 하네스도 받지 않았다. 저자가 부록에서 그렇게 적었다**
> 부록 10.4 원문: *"Published systems retain their original harnesses and execution budgets; **the cross-system comparison does not use a matched evaluation protocol**."* 폐쇄 모델 점수는 **리더보드·기술보고서에서 복사**했다(표 1 캡션: *"Baseline results are mostly copied from their official technical reports or blogs"*).
> → 수집기가 제기한 질문(*"폐쇄 모델에도 같은 메모리를 줬는가"*)의 답은 **아니오**다. 🎯 **초록의 "Kimi-K3·GLM-5.3이 GPT-6를 앞선다"는 모델 비교가 아니라 시스템(GLM-5.3 actor + Kimi-K3 verifier/curriculum + 탐색 메모리) 대 단일 모델 보고치 비교다.**

> [!insight] 🎯 그리고 더 중요한 것 — **격차의 대부분은 RSI 이전에 이미 있었다**
> 표 1 해당 행 — 전행(OSWorld 2.0 0808 offline 82과제 / ALE Near-term 67과제):
> ```
>                         OSWorld Partial  Binary   ALE Partial  Binary
> Kimi-K3 (보고치)             58.30          —        71.60      40.30
> Claude Opus 5               70.19        34.72      79.54      46.27
> GPT-6 Astra                 72.60          —        82.26      52.24
> RSIAgent (w/o RSI)          71.97        37.80      83.75      49.25
> RSIAgent                    78.98        42.68      84.82      50.75
> ```
> - **메모리 없는 하네스(w/o RSI)만으로** ALE Partial이 이미 GPT-6 Astra를 넘고(83.75 > 82.26), OSWorld는 0.63점 차다.
> - **RSI의 순기여**: OSWorld Partial **+7.01** · Binary **+4.88**(31→35과제) / ALE Partial **+1.07** · Binary **+1.50 = 67과제 중 1과제**(33→34).
> - 🔴 **ALE Binary는 여전히 GPT-6 Astra에 진다(50.75 < 52.24)** — 저자 스스로 부록 10.4에 *"the partial-credit advantage does not extend to every reported metric"* 라고 적었다. 초록에는 이 문장이 없다 → [[한정어-탈락]] 이 **저자 초록 단계에서** 일어난 사례.
> 🎯 **읽는 법**: "오픈 모델 + 다중 에이전트 검증 하네스(액터 500 반복 · 10시간 워치독)"가 1차 이득이고, "탐색 메모리(RSI)"는 OSWorld에서 의미 있고 ALE에서는 1과제다.

> [!warning] 🔴 RSI 열은 **절반 과제만** 실제 RSI 결과다 — 그리고 과제 선정이 있다
> - OSWorld: 82과제 중 **41개만** RSI 결과로 교체, 나머지 41개는 **기준선 점수를 그대로 둠**. ALE: 67과제 중 **19개만** RSI, 48개는 기준선.
> - 선정 규칙(부록 10.3): *"tasks were selected when their recorded baseline score was **below full credit**"* — 올릴 여지가 있는 과제에 탐색을 집중했다.
> - README 원문: *"The RSI column includes **selected retries and checkpoints** with differing budgets; it is not an average over matched repeated runs."*
> 🎯 **판정**: 퇴행도 포함했다고 적었으므로 순수 체리피킹은 아니지만, **재시도·체크포인트 선택**이 들어간 값은 **단일 실행 기대값이 아니다.** 볼트는 이 열을 **"상한에 가까운 보고치"** 로 읽는다.

> [!warning] 🔴 "새 환경에서 재사용할 메모리"가 아니라 **목표 과제 자체를 연습한 메모리**다
> 부록 10.2: *"The target query guides the curriculum agent in **both stages**"* · 부록 12: *"In these runs, DRS includes **practice on the target itself**."*
> → 초록은 *"memory is frozen and can be directly reused for **downstream tasks**"* 라고 쓰지만, 실험의 "downstream task"는 **탐색을 이끈 바로 그 목표 과제**다. 🎯 이건 **과제별 테스트타임 탐색(test-time search)** 에 가깝다. 한 번 만든 메모리가 **다른 과제로 이전되는지는 측정되지 않았다.**
> 📌 비교: [[ModularRSI]] 는 정반대 방향이다 — 진화 과제를 평가 벤치와 **분리**하고 동결 후 평가했다. **같은 날 나온 두 "RSI" 논문이 일반화에 대해 정반대 프로토콜을 쓴다.**

## RSI 루프는 몇 바퀴? — [[RSI-프레이밍]] 대조
- **BRS(넓게)**: 명목 예산 **8개 탐색 프로젝트**, 최대 4개 동시 실행. 웨이브 단위로 예산을 확인해 **실제로는 8개를 넘을 수 있다** — 사례: T044 **10개** · T049 **8개** · T065 **11개**.
- **DRS(깊게)**: 순차 반복, **커리큘럼 에이전트가 "더 연습할 가치 없음"이라고 판단할 때 종료**(`curriculum_review`). 고정 회수 없음.
- 그림 3: 세 과제의 **RSI step 0~8** 곡선(T044·T065 100%, T049 80% 도달). 🔴 **3과제만**, 전체 벤치의 회차별 곡선은 없다.
- 메모리 크기(부록 12.1): 최종 동결 시 **316,541 / 141,312 / 281,085 바이트**(T044/T049/T065).
- 🎯 **판정**: 루프는 **여러 회 돌았다**(NeoHorse의 single pass와 다름). 🔴 그러나 개선되는 것은 **가중치도 하네스 코드도 아닌 텍스트 메모리 파일**이다. [[NeoHorse-1-Paper]](사후학습 루프) · [[ModularRSI]](하네스 코드 진화) · [[Dream-RSI]](탐색 정책) · 이 논문(메모리 파일) — **"RSI" 한 단어가 네 가지 다른 대상을 가리킨다.**

## 절제·보조 실험
- **단계 절제(4과제, OSWorld)**: Full RSI 평균 **74.54%** · BRS만 **65.52%** · DRS만 **56.50%**. DRS만 쓰면 T085·T089에서 **기준선보다 낮아진다**. 🔴 이 4과제는 *"an exploratory cohort **selected for improvements** over recorded baselines"* 에서 골랐다(부록 10.5) — **개선이 확인된 과제로 절제를 했다.** Full RSI는 과거 평가 2회 평균, 단일 단계 조건은 1회.
- **게임 개발(GameCraft-Bench 40과제, 표 2)**: 4개 생성기 전부 `RSIAgent > RSIAgent(w/o RSI) > Play2Code` (Codex+GPT-5.5 생성기에서는 Play2Code가 기준선보다 **낮음** 51.05 < 52.77). 🔴 평가자가 **Qwen3.8-27B**이고 플레이테스터도 같은 모델이다.
- **실패 분석(§4.6)** — 🎯 **이 논문에서 가장 쓸모 있는 절이다**: ① 약점을 겨냥하지 못한 탐색 ② **불완전 검증** — *"the verifier agent returned PASS despite unsupported field values"* ③ **불안정한 메모리 통합** — 검증이 부실한 결정이 **재사용 규칙으로 굳는다**(빈칸 표시를 유효 답으로 저장한 사례). *"useful memory must preserve the conditions and uncertainty of an experience, rather than treating local acceptance as evidence of general validity."*

## 도메인별 추출 (ai-news)
- **신뢰도**: HF 업보트 **74** · 저자 **6명**(Aether AI · UCSD · UIC; 교신 Kun Zhou) · org `AetherLabs-AI` · GitHub `AetherLabsAI/RSIAgent` **★343**(HF 필드 339) · 포크 39 · Apache-2.0 · 파일 207개(`core/actor.py`·`verifier.py`·`explore/` 등 실제 구현). 🎯 **부록과 README의 보고 규약 공개가 매우 정직하다**(비매칭 프로토콜·선택 재시도·ALE Binary 패배를 스스로 적음). 🔴 그러나 **제목·초록의 헤드라인 주장은 그 부록과 어긋난다.** → reliability **medium**(정보 정직성은 높고, 헤드라인 주장은 low).
- **즉시 활용**: 🎯 **YES — 실패 분석 3항목을 볼트 메모리 규칙으로.** 볼트는 사실상 "인제스트로 메모리를 축적하는 에이전트"다. **"국소 검증 통과를 일반 규칙의 증거로 삼지 말고, 조건과 불확실성을 함께 저장하라"** 는 [[MiniMax-H3]] 09-06 교훈(*비율 주장은 관측 시점에 결박된다*)과 같은 결론이다.
  - verifier의 3값 판정 `PASS · FAIL · UNVERIFIED`(부록 10.2: *"an unverified outcome requests additional evidence instead of being treated as success"*) → [[NeoHorse-1-Paper]] 의 `NOT_EVALUATED` 와 **같은 칸**. [[검사가능성-공사]] 의 **네 번째 독립 수렴 사례**.
- **6개월 영향력**: **중간.** 컴퓨터 사용 에이전트에서 **"모델 교체 대신 과제별 탐색 예산"** 이라는 축이 커질 수 있다. 🔴 단 이 논문은 **탐색 비용을 수치로 보고하지 않았다**(한계 절: *"can introduce substantial computation cost"* 만).
- **대체 관계**: 모델 업그레이드를 대체한다고 주장하나, 실제로 보인 것은 **테스트타임 연산 증가 → 점수 증가**다. 동일 연산을 폐쇄 모델에 준 비교가 없으므로 **대체 여부는 판단 불가.**
- **허와 실**: ✅ 실: w/o RSI 대비 OSWorld +7.01 Partial · 게임 4생성기 전부 개선 · 실패 모드 분석. ❌ 허: "오픈 모델이 GPT-6를 넘었다"(비매칭 · 하네스 몫이 대부분 · ALE Binary 패배) · "새 환경 재사용 메모리"(목표 과제 연습 포함) · "RSI"(가중치·코드 불변, 메모리 파일 누적).
- **액션**: 🎯 **레포의 `explore/memory_hash.py`·`core/verifier.py` 를 읽고 UNVERIFIED 처리 방식 확인** → 볼트 판정 체계 3값화 설계 참고.

> [!warning] 수집기 대조
> - ✅ 원문 대조 일치: 업보트 74 · githubStars 339(HF 필드; GitHub API ★343) · 저자 6 · org AetherLabs-AI · training-free · 3에이전트 · broad-then-deep · 메모리 동결 재사용 · OSWorld-v2/ALE · Kimi-K3·GLM-5.3 > GPT-6 주장 · 초록 수치 0개 · "RSI = 가중치 갱신 없는 메모리 축적" 용어 주의.
> - ✅ **수집기의 조건부 경고가 맞았다** — 판별 결과 **"오픈 모델 + RSIAgent" vs "폐쇄 모델 단독 보고치"** 이고, 폐쇄 모델에 메모리를 주지 않았다. 수집기 표현 그대로 **"시스템 대 모델 비교"** 다.
> - 🔴 보강: 초록은 *"including GPT-6"* 이고 본문은 **GPT-6 Astra**, 서론은 **Claude Opus 5** 도 함께 언급한다. 역할 배분은 **GLM-5.3 = actor, Kimi-K3 = verifier·curriculum** 이다(두 모델을 각각 개선한 것이 아니다).

> [!action] 당장 할 것
> 1. **볼트 판정 체계에 `UNVERIFIED` 3번째 값 도입 검토** — [[NeoHorse-1-Paper]]·이 논문 = 같은 주 두 건 → [[검사가능성-공사]]
> 2. **볼트 메모리 규칙 추가 시 "조건·불확실성 동반 저장"** — 규칙 본문에 관측일·표본을 붙인다(§4.6 ③의 볼트 적용)
> 3. [[RSI-프레이밍]] 에 **"RSI 대상 4분류"**(가중치 · 하네스 코드 · 탐색 정책 · 메모리 파일) 추가 제안

> [!question] 미해결 질문
> - 같은 액터-검증자 하네스 + 같은 탐색 예산을 **GPT-6 Astra 에 주면** 몇 점인가? (이게 있어야 "오픈 모델이 넘었다"가 성립)
> - 과제 A에서 만든 메모리를 **과제 B**에 쓰면 이득이 남는가? (환경 수준 재사용 — 초록 주장 — 은 미측정)
> - 과제당 탐색 비용(토큰·시간)은? 워치독은 10시간이지만 *"not a ten-hour ceiling on the complete exploration lineage"*
> - GLM-5.3 **단독** 보고치가 표 1에 없는 이유 — actor 모델의 원래 점수가 빠져 있다

## 관련 페이지
- [[RSI-프레이밍]]
- [[ModularRSI]] — 같은 날(09-14), 정반대 일반화 프로토콜(벤치 분리)
- [[NeoHorse-1-Paper]] — `NOT_EVALUATED` ↔ 여기 `UNVERIFIED`
- [[Dream-RSI]]
- [[하네스-설계-축]]
- [[검사가능성-공사]]
- [[한정어-탈락]]
- [[표-부분인용]]
- [[자기제한-명시]]
- [[Kimi-K3]]
- [[GLM-5.3]]
- [[MiniMax-H3]] — 09-06 "관측 시점 결박" 교훈과 §4.6 ③의 동형

## 원본
- 출처: https://huggingface.co/papers/2609.15364 · 본문 https://arxiv.org/html/2609.15364
- 코드: https://github.com/AetherLabsAI/RSIAgent · 사이트: https://aetherlabsai.github.io/RSIAgent/
- 볼트 실측(2026-09-19): HF papers API `upvotes` 74 · `githubStars` 339 · `authors` 6 · `organization.name` AetherLabs-AI · `publishedAt` 2026-09-14 / GitHub API `stargazers_count` 343 · `forks_count` 39 · `open_issues_count` 5 · `created_at` 2026-09-13 · `pushed_at` 2026-09-16 · Apache-2.0 · 파일 207개 / README 원문(보고 규약 · 41/19 교체 · 선택 재시도 명시) / arXiv HTML 본문 전문 읽음(표 1·2·A2~A4, 부록 10.1~10.5, 12, 한계 절, 참고문헌 — **2609.08183(NeoHorse)·SoL-Pi 인용 없음**)
- 신뢰도: ⭐⭐ (코드 공개·보고 규약 정직 · 🔴 헤드라인 비교 비매칭 · RSI 열 절반만 실측 · 목표 과제 연습 · 비용 미보고 · 분산 없음)
