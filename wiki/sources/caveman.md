---
title: JuliusBrussee/caveman — 응답을 "원시인 말투"로 압축해 토큰 절감하는 Claude Code 스킬
type: source
domain: ai-news
tags: [ai-news, github-trending, claude-code, skill, token-optimization, prompt-compression, llm-cost, 코드실행, 오프라인평가, 기준선, 거짓양성, 볼트-성과]
created: 2026-07-03
updated: 2026-10-16
sources: []
reliability: medium
---

# caveman (JuliusBrussee/caveman)

---

## 🏆🏆🏆 2026-10-16 갱신 — **26배치 연속 "외부 코드 실행 0건" 적자 해소. 그리고 실행 결과가 간판을 뒤집었다**

**GitHub 실측(2026-10-16)**: ★**112,887** (수집기 112,880 → +7) · 포크 6,531 · 라이선스 Apache-2.0 · 최근 푸시 2026-10-15

> [!insight] 🏆🏆🏆 볼트가 레포의 자체 오프라인 평가를 **실제로 실행했다** — 수집기 계열 26배치, 볼트 25배치 연속 적자 종결
> ```
> git clone --depth 1 https://github.com/JuliusBrussee/caveman.git
> pip install tiktoken          # 0.14.0
> python3 evals/measure.py      # 커밋된 오프라인 스냅샷, API 키 불필요
> ```
> 🔴 **결과가 간판과 다른 세계를 보여준다.**
> ```
> Model: claude-opus-5-5 · CLI 2.1.288 · Tokenizer: tiktoken o200k_base
> n = 10 prompts, single run per arm
>
> baseline (시스템 프롬프트 없음)        : 6,983 tokens
> terse control ("Answer concisely.")   : 4,334 tokens   (+38% vs baseline)
>
> | Skill      | Median |  Mean |  Min |  Max | Stdev | Tokens(skill/terse) |
> | ultracave  |  +35%  |  +38% | +27% | +58% |  10%  |  2,693 / 4,334      |
> | megacave   |   +9%  |  +14% | −12% | +39% |  15%  |  3,683 / 4,334      |
> | caveman    |   +3%  |   +5% | −16% | +20% |  12%  |  4,119 / 4,334      |
> ```

> [!warning] 🔴🔴 결정적 — **기본 `caveman` 모드는 "Answer concisely." 한 줄 위에 중앙값 3%만 더한다. 최악 프롬프트에서는 16% 악화된다**
> | 조건 | 토큰 | baseline 대비 |
> |---|---:|---:|
> | baseline (아무 지시 없음) | 6,983 | — |
> | **`Answer concisely.` 한 줄** | 4,334 | **−37.9%** ← **공짜** |
> | `caveman` | 4,119 | −41.0% (terse 대비 **−5.0%**) |
> | `ultracave` | 2,693 | −61.4% (terse 대비 −37.9%) |
>
> 🎯 **간판 "33.2% 절감"이 비교하는 대상은 아무 지시 없는 baseline 이다. 그런데 한 줄 지시만으로 이미 37.9%가 나온다.** ⇒ 🔴 **간판 수치보다 큰 절감이 설치 없이 얻어지고, 설치의 고유 기여는 중앙값 3%다.** 📌 이것이 [[표-부분인용]] **④ 기준선 축**의 금일 두 번째 사례다([[Dynamic-Band-Splitting]] 과 쌍).
> 🔴 **그리고 `min` 열이 음수다**: caveman −16% · megacave −12% ⇒ **프롬프트에 따라 악화된다**(stdev 12~15%, n=10 단일 런) → [[유의성-자기제한]] · [[배수-조건분산]].
> 🏆 **2배치 이월 확증**: [[측정도구-먼저-반증]] 10-04 기록 — Adobe Research 논문 제목이 `CAVEWOMAN` 이고 초록이 입력 압축을 *"strict lose-lose"* 로 판정한다 — **그 판정이 레포 자체 평가로 실증됐다.** ⇒ ✅ **볼트 10-04 추론 확정.**

> [!insight] 🏆🏆 그런데 레포가 자기를 무너뜨리는 스크립트를 함께 배포한다 — [[자기제한-명시]] 최상급 사례
> `evals/measure.py` 는 **caveman 저장소 안에 커밋된 파일**이고, 실행하면 **간판을 깎는 숫자가 나온다.** 📌 스크립트 독스트링도 스스로 한정한다: *"tiktoken o200k_base is OpenAI's tokenizer and is **only an approximation** of Claude's BPE … absolute numbers should be read as 'approximate output-length reduction', **not 'exact Claude tokens'**."*
> ⇒ 🎯 **과장은 간판 타일에 있고, 반증은 같은 레포 `evals/` 에 있다.** 10-14 [[context-mode]] 와 같은 구조다.

## 🔴🔴 수집기 "간판 65% vs 본문 33.2% 불일치 자체 적발" — **거짓 양성 1건** (볼트 기각)

> [!warning] 🔴 65% 는 간판이 아니다. **caveman 이 스스로 폐기했다고 공시한 과거 추정 비율**이다
> 수집기 10-16 자기보고 5번 ①: *"🔴🔴 `caveman` **간판 65%** vs 본문 **33.2%** — 측정 대상이 다른 수치를 한 지표처럼 노출."*
> ✅ **볼트 전수 탐색: `README.md` 에 "65%" 는 0건이다.** 간판 타일 4개는 다음과 같다(README 16~19행 실측):
> | # | 간판 타일 | 부제 |
> |---|---|---|
> | 1 | **33.2% fewer** input tokens, whole sessions | 54 Claude Code runs, 18 of 18 answers right |
> | 2 | **54% cheaper** with Auto, same score | 85 coding tasks vs Opus 5.5 at xhigh, **interim** |
> | 3 | **397 → 76** tokens for one test run | Blocks vs `\| tail -20` |
> | 4 | **1.4 to 2.4× cheaper** | Adobe Research, eight models |
>
> 🔴 **레포 내 "65%" 의 유일한 출처는 `docs/HONEST-NUMBERS.md:62` 이고, 내용이 정반대다**:
> *"Earlier stats releases applied a fixed 65% output ratio **without a committed reviewed result**. **Current reports ignore those historical `est_saved_*` fields** … the statusline **no longer displays** the numeric savings suffix."*
> ⇒ 🏆 **65% 는 프로젝트가 "검토된 근거 없이 썼다"고 자백하고 현행 보고에서 제거한 값이다.** ⚖️ **수집기는 폐기 공시된 수치를 현행 간판으로 오인하고 "불일치"를 생성했다** — [[인용-부호]] · [[간판-지체]] 의 역방향 사례(**지체가 아니라 소급 적용**).
> 📌 **교훈: "간판 vs 본문 불일치"를 적을 때 간판 쪽 출처를 명시해야 한다.** 금일 수집기는 본문 쪽만 출처를 달았다.

## ✅ 간판 표 전건 검산 통과 (볼트 자체 계산)

| 검산 | 결과 |
|---|---|
| 6종 파일 합계 | 28,041+22,810+20,447+18,806+18,837+21,670 = **130,611** ✅ 표기 일치 |
| 압축 후 합계 | **22,994** ✅ · 절감 **82.40%** ✅ (표기 82.4%) |
| 세션 합계 | **885,793** ✅ · 압축 후 **591,673** ✅ · 절감 **33.20%** ✅ (표기 33.2%) |
| HTML 행 악화 | 140,687→154,641 = **+9.92%** ✅ (표기 "9.9% worse") |

🏆 **산술은 전건 맞다. 문제는 산술이 아니라 기준선이다.**

## 🔴 Blocks 표는 **1승 1무 1패**인데 수집기는 승리 행만 전달했다

| 입력 | Raw | 에이전트가 지금 쓰는 것 | Block | 판정 |
|---|---:|---:|---:|---|
| `go test -v ./...`, 326 tests | 10,561 | 397 · `\| tail -20` | **76** · `test-summary` | ✅ **−80.9% 승** |
| 1.4 MB JSON | 251,893 | 236 · 자체 heredoc | **227** · `json-peek` | 🟡 −3.8% **무** |
| 366행 Go 파일 | 3,111 | **250** · `grep -n` | 489 · `grep-defs` | 🔴 **+95.6% 패** |

🏆 **그리고 레포가 패배를 먼저 적는다**: *"`grep-defs` **loses to a bare grep**; row stays."* ⇒ 📌 **간판 "397→76"은 3행 중 최선이고, 수집기는 *"블록 모드 397→76 토큰"* 만 전달해 1패를 누락했다** → [[표-부분인용]].
🔴 **추가**: `397` 은 caveman 출력이 아니라 **베이스라인(`| tail -20`)** 이다. *"397→76 토큰 절감"* 으로 읽으면 주체가 바뀐다.
🔴 **그리고 blocks 는 별도 레포다**(`github.com/caveman-ai/blocks`) — 본 레포에서 3행의 측정 방법을 재현할 수 없다 → [[선언된-구현체-공백]].

## 📌 33.2% 의 숨은 상한 — 정답률을 유지하는 조건에서만 성립한다

README 본문: *"Honest part: the session run is from **August 2026 on an older engine**, HTML has no compressor yet so it lost … **Headroom on the same suite: 15 of 18 right, 6.7% fewer tokens.**"*
🔴 **더 공격적으로 압축하면 정답률이 18/18 → 15/18(83.3%)로 떨어지고, 추가 절감은 6.7%뿐이다.** ⇒ 🎯 **33.2% 는 "정답률 무손실 상한"이고, 그 너머는 급격한 교환비다** → [[수확체감-변곡점]] · [[임계-의존-성공률]].

## ✅ 3자 재현 2건 — 수집기 보고 정확, 단 채널이 다르다

- **Elastic**(Elasticsearch Labs, 8개 라이브 MCP 시나리오): **응답 토큰 63.6% 감소** · *"Zero information loss."*
- **JetBrains**(86개 실제 코딩 과제, 쌍 A/B): **출력 토큰 8.5% 감소** · 품질차 **p = 0.82**(유의하지 않음)
🔴 **두 수치의 채널이 다르다**: Elastic 은 **응답/출력** 토큰, 간판 33.2% 는 **입력** 토큰이다. ⇒ 📌 **"63.6%"를 간판 33.2% 의 3자 확증으로 읽으면 안 된다** → [[단위-불일치]] · [[비매칭-비교]]. 그리고 **8.5%(JetBrains) ↔ 63.6%(Elastic) = 7.5배 격차**가 같은 "출력" 축에서 난다 → [[배수-조건분산]].

## 🔴 이슈/PR 분해 (볼트 6배치 연속 적자 금일 해소)

`open_issues_count` **71** = 순이슈 open **40** + PR open **31** ✅ 검산 통과 · 이슈 closed **493** ⇒ **해소율 92.5%**(493/533). ✅ **유지보수는 건강하다** — 간판 수치 문제와 운영 품질은 별개다.

> [!action] 당장 할 것 (갱신)
> ① ✅ **완료**: `evals/measure.py` 오프라인 실행 — **더 할 일은 `evals/llm_run.py`(Anthropic 키 필요)로 자체 스냅샷을 다시 뜨는 것**이다. 볼트 작업 프롬프트 10개로 돌리면 **볼트 고유 조건의 중앙값**이 나온다.
> ② 🔴 **설치 전에 `Answer concisely.` 한 줄을 먼저 시험하라.** 금일 실행 결과상 **공짜 한 줄이 간판 절감을 넘는다**. caveman 을 쓸 이유는 기본 모드가 아니라 **`ultracave`(중앙값 +35%, min +27% — 유일하게 전건 양수)** 다.
> ③ 🔴 **`grep-defs` 는 쓰지 말 것** — 레포 자체 표에서 bare grep 에 95.6% 진다.

> [!update] 2026-10-04 갱신 — ★109,666 (볼트 실측 · **관측 2026-10-04T09:12:13Z**) · 🏆🏆 **배치 최대 발견: 수집기가 "신뢰도 보강"으로 전한 제3자 인용이 실제로는 이 레포의 핵심 주장을 반증한다** · 🔴 **65% 와 33.2% 는 시계열이 아니라 같은 레포 안의 동시 불일치다**
> **볼트 독립 실측 ★109,666** ↔ 수집기 ★109,662 = **드리프트 +4**. 어제 볼트 실측 ★109,249 → **구간 증분 +417**(수집기 *"당일 +507"* 보다 **낮다** · 구간 길이 미확정).
> ✅ **전 필드 일치**: fork **6,344** · open_issues **115** · **Apache-2.0** · topics **10** · created 2026-04-04 · 주언어 **Go**(10-03 볼트 확인 유지) · **pushed 2026-10-04T07:51:14Z = 관측 1시간 21분 전**. 🆕 watchers **253** · size **16,090KB**.
>
> ## 🏆🏆 arXiv 2606.24083 을 볼트가 직접 열었다 — **인용은 추천이 아니라 반박이다**
> 수집기는 이것을 **신뢰도 자산**으로 전했다: *"🏆 배치 유일 '제3자 독립 인용' 보유 — Adobe Research 논문 arXiv 2606.24083 인용 · JetBrains A/B · Elasticsearch Labs 재구현 · HN 1위."*
> ✅ **볼트 실검증(arXiv API 실호출)** — 논문은 실재한다:
> - **제목: `CAVEWOMAN: How Large Language Models Behave Under Linguistic Input and Output Compression`**
> - 저자 **Morayo Danielle Adeyemi · Ryan A. Rossi · Franck Dernoncourt** (Rossi·Dernoncourt = Adobe Research 소속으로 알려진 연구자 ⇒ 수집기의 "Adobe Research" 귀속은 **정합**)
> - published **2026-06-23** · cs.CL/cs.AI/cs.LG · 초록 첫 문장이 **이 레포의 홍보문구 그대로**다: *"**Talk short. Drop grammar. Save token.**" This caveman style is widely promoted as a way to cut inference cost, **but whether it actually saves anything depends on which channel** (the user's prompt or the model's response) is being compressed.*
>
> 🔴🔴 **그 논문의 결론이 이 레포의 대표 수치와 정면 충돌한다.** 초록 원문:
> > **"Input compression has the opposite effect, a strict lose-lose: it raises net cost rather than lowering it (~1.15x on the five-benchmark mean, up to 1.8x on the worst dataset and 2.7x under stronger compression), because models compensate with longer responses even as accuracy collapses."**
> ⇒ ⚖️ **caveman 의 대표 수치는 "입력 토큰 −33.2%"(수집기 전달)이고, 논문이 "strict lose-lose" 라고 특정한 채널이 바로 그 입력 채널이다.**
> 📌 **논문은 출력 압축은 효과가 있다고 적는다**(API 모델 **1.4~2.4배** 비용 절감 · 최상 3배 · 오픈웨이트 4종 전부). ⇒ 🎯 **즉 반박은 "압축이 무용하다"가 아니라 "채널을 틀렸다"다. 절감은 출력에서 나오고 입력 압축은 순비용을 올린다.**
> 🏆 **측정 규모가 caveman 자체 측정보다 크다**: **모델 8종 × 데이터셋 5종 × 감축 수준 5단계, 두 채널을 같은 항목에서 측정** ↔ caveman 자체 측정은 **Claude Code 54회 실행 · 과제 18개**(수집기 전달) = 하네스 1종.
> 🔴 **논문이 caveman 이 재지 않는 축을 하나 더 잰다**: *"non-reasoning 모델에서 생성물의 약 절반이 정답인데도 그 표면 텍스트가 모델 자신의 무제약 베이스라인을 더 이상 함의하지 않는다"*(length-controlled 재채점 · 다중비교 보정 · 대체 의미 척도 복제에서 생존). ⇒ ⚖️ **caveman 의 *"정답 18/18 유지"* 는 정확도를 보증하지만 의미 보존을 보증하지 않는다. 논문은 정확도를 통과한 출력의 절반이 의미적으로 이탈함을 보고한다.**
>
> ⚖️ **볼트 판정 — [[측정도구-먼저-반증]] 최상급 사례이자 [[관련성-판단-주체]] 사례다.**
> 🎯 **"제3자 인용 보유"는 사실이지만 그 인용의 **부호**가 반대다. 인용 수를 신뢰도 지표로 쓰면 부호를 잃는다.** ⇒ 🏆 **볼트 신규 규칙: 제3자 인용은 "있다/없다"로 세지 않고 반드시 그 결론의 부호를 확인한다. 나를 인용한 논문이 나를 반박할 수 있다.**
> 🔴 **미확인 2건(정직하게 분리)**: ① **논문이 `JuliusBrussee/caveman` 레포를 명시 인용하는지는 확인하지 않았다** — 초록만 읽었고 본문 참고문헌을 열지 않았다. 제목·첫 문장으로 **같은 기법을 다룬다는 것은 확실**하나 **이 레포를 지명했다는 것은 미확정**이다. ② **caveman README 가 이 논문을 어떻게 소개하는지 미열람** — 수집기 표현("인용 보유")이 *"논문이 우리를 인용했다"* 인지 *"우리가 논문을 인용했다"* 인지 구분되지 않는다. ⚖️ **후자라면 이 레포는 자기를 반박하는 논문을 자기 신뢰도 근거로 올린 셈이고, 전자라면 반박 논문에 인용된 것을 실적으로 전시한 셈이다. 어느 쪽이든 부호는 반대다.** → actionable 최우선.
>
> ## 🔴 65% vs 33.2% — **수집기가 넘긴 "시계열" 판정 요청에 답한다: 시계열이 아니다**
> 수집기: *"볼트 [[caveman]] 페이지의 75%→65% 하향과 비교하면 README 대표 수치가 33.2% 로 더 낮다 ⇒ 하향이 이어졌다(⚠️ 단 65%와 33.2%는 측정 대상이 달라 같은 지표의 시계열이 아니다 — 볼트 판정 필요)."*
> 🏆 **볼트 답: 두 수치는 과거·현재가 아니다. 지금 이 순간 같은 레포에 공존한다.**
> ✅ **볼트가 GitHub API 로 읽은 `description` 원문(2026-10-04T09:12:13Z)**:
> > `🪨 why use many token when few token do trick. Viral skill + proxy for coding agents that cuts 65% of tokens by talking like a caveman.`
> ⇒ 🔴 **레포 설명문은 여전히 "65%"다. README 는 "입력 −33.2%"다**(수집기 전달). **같은 시점, 같은 레포, 두 수치.**
> ⚖️ **판정: 이것은 [[자기제한-명시]](시간에 따른 자발적 하향)가 아니라 [[단위-불일치]] + [[표-부분인용]] 이다.** 📌 **description 은 전체 토큰 65%, README 는 입력 채널 33.2% — 분모가 다르고 둘 다 현행이다.** 🎯 **그리고 레포의 "첫인상 표면"(검색 결과·트렌딩 목록에 뜨는 것)은 description 이므로, 실질적으로 유통되는 수치는 더 높은 쪽인 65% 다.**
> ⇒ 🏆 **10-03 에 볼트가 적은 *"자가 제출 수치는 시간이 지나면 내려간다"* 를 수정한다: 내려가는 것은 README 안쪽이고, 바깥 표면은 안 내려간다.** [[한정어-탈락]] 에 **"하향은 문서 깊이에 따라 불균등하다"** 로 등재.
> 🔴 **그러므로 신뢰도를 올리지 않는다 — medium 유지**(10-03 과 동일). 하향의 존재가 성실성의 증거였는데, **표면이 그대로라면 그 증거가 약해진다.**

> [!update] 2026-10-03 갱신 — ★109,249 (볼트 실측) · 🏆 **볼트가 3개월 전에 적은 경고가 확증됐다**
> **볼트 독립 실측 ★109,249** ↔ 수집기 ★109,244 = **드리프트 +5**. 기존 베이스라인 ★82,003(2026-07-03) → **+27,246 / 92일 = 일평균 ≈296**.
> ✅ **전 필드 일치**: fork **6,320** · open_issues **143** · **Apache-2.0** · topics **10** · created 2026-04-04 · **pushed 2026-10-03T08:07:10Z = 당일 활성**.
> 🆕 **볼트 신규 확인**: 주언어 **Go**. 📌 프록시 구현에 부합하는 선택이고, 이 페이지가 *"스킬/플러그인"* 으로만 적었던 것을 보정한다 — **설치물이 스킬이 아니라 Go 바이너리 프록시**라면 도입 비용 구조가 다르다(런타임 1종 추가).
> 🏆 **절감률 주장이 하향됐고, 그것을 볼트가 먼저 적어 뒀다** — 이 페이지는 2026-07-03 에 *"README 는 ~75% 를 주장"* + ⚠️ *"외부 요약에서는 약 65%로 전해짐 — **수치 자체가 소스마다 엇갈림**"* 이라고 기록했다. 오늘 수집기가 전한 자기 주장은 **65%** 다. ⇒ ⚖️ **볼트의 "엇갈림" 경고가 3개월 뒤 수치 하향으로 확증됐다. 자가 제출 수치는 시간이 지나면 내려간다** → [[자기제한-명시]] · [[측정도구-먼저-반증]].
> 🔴 **그러나 핵심 공백은 그대로다**: 65%든 75%든 **측정 방법·대조군이 공개되지 않았고**, 더 중요하게 **"압축이 정확도를 깎기 시작하는 구간"이 공개되지 않았다.** 절감률은 자유 파라미터이고 품질 손실 곡선이 없으면 어느 수치도 채택 근거가 못 된다.
> 🎯 **방향이 [[superpowers]]·[[ponytail]] 과 직교한다**(10-03 재확인): 그쪽은 에이전트의 *판단*을 바꾸고 이쪽은 *청구서*를 깎는다 → [[대립레시피-동시도착]] **직교 쌍**.

> [!insight] 핵심 인사이트
> ⭐82,003 (2026-07-03, 당일 +926). 에이전트의 출력 응답을 **"원시인 말투(caveman-speak)"로 압축**해 토큰을 절감한다고 주장하는 [[Claude-Code-워크플로우]] 스킬/플러그인. "why use many token when few do trick" — 불필요한 예의·서두·필러를 걷어내고 기술적 정확도는 유지한 채 문장 스타일만 압축하는 방식. Claude Code뿐 아니라 Codex·Gemini·Cursor·Cline·Copilot 등 30여 종 에이전트를 지원. [[superpowers]]·[[agency-agents]]가 에이전트에 "능력·페르소나"를 더하는 방향이라면, caveman은 반대로 에이전트의 "출력 비용"을 깎는 방향의 스킬이라는 점에서 상보적이다.

## 도메인별 추출 (ai-news)
- **신뢰도**: ⭐⭐⭐ — ⭐82K로 트렌딩 상위. 다만 스타 수는 "재미있는 컨셉"에 대한 반응이 크며, **실측 절감률·품질 저하는 독립 검증 안 됨**. 벤치마크가 자가 제출 수치라 신뢰도 중간.
- **즉시 활용**: MAYBE — 설치 원커맨드(`curl … | bash` 또는 `/caveman`), Node ≥18. 실험 비용 낮음. 단 프로덕션 응답 품질에 스타일 압축이 미치는 영향은 직접 확인 필요.
- **6개월 영향력**: 중 — "토큰 절감 스킬" 카테고리 자체는 유효(에이전트 장기 세션 비용이 실질 부담). 다만 caveman 말투는 가독성 트레이드오프가 있어 `lite`/`ultra`/`wenyan` 등 레벨 선택으로 절충. 스타일 압축보다 CLAUDE.md 압축(`/caveman-compress`)·MCP 툴 설명 압축(`caveman-shrink`)이 더 실용적 파생일 수 있음.
- **대체 관계**: 별도 도구 대체가 아니라 [[Claude-Code-워크플로우]] 위에 얹는 **출력 다이어트 레이어**. system prompt/출력 지침 수동 튜닝을 자동화·정형화한 것.
- **허와 실**: 마케팅 문구는 "~75% 토큰 절감 + 100% 정확도 + 3배 속도"로 매우 공격적. README 자체 수치이며 태스크·언어·응답 유형별 편차가 크다. 인풋(프롬프트/컨텍스트)은 그대로이고 주로 **출력** 토큰을 줄이는 것이라 전체 세션 절감률은 응답 비중에 따라 달라짐.
- **액션**: star + 격리 세션에서 `/caveman full` 켜고 동일 태스크 반복 → `/caveman-stats`로 실측 절감률과 답변 품질(누락·오해) 동시 확인.

> [!warning] 절감률 주장 검증 필요
> README는 **~75% 출력 토큰 절감 · 정확도 100% · 속도 3배**를 주장하나 모두 자가 제출 수치다(외부 요약에서는 약 65%로 전해짐 — 수치 자체가 소스마다 엇갈림). 실제로는 (1) **출력 토큰만** 주로 줄이므로 세션 전체 절감은 더 작을 수 있고, (2) 말투 압축으로 인한 **정보 누락·가독성 저하·오해 위험**이 존재한다. 반드시 본인 태스크로 A/B 실측 후 채택할 것. 무비판 수용 금지.

> [!action] 당장 할 것
> 격리 세션에서 대표 코딩 태스크 3건을 (a) 기본 모드, (b) `/caveman full`, (c) `/caveman lite`로 각각 실행 → `/caveman-stats`로 토큰·비용 비교하고 답변 품질(정확·누락) 수동 채점. 실측 절감률과 품질 손실을 기록해 채택 여부 결정.

## 관련 페이지
- [[Claude-Code-워크플로우]]
- [[superpowers]]
- [[agency-agents]]
- [[strix]]
- [[video-use]]
- [[AI-에이전트-프레임워크]]

## 원본
- 출처: https://github.com/JuliusBrussee/caveman
- 스타: ⭐82,003 (2026-07-03, 당일 +926) *(NEW)*
- 신뢰도: ⭐⭐⭐ (트렌딩 상위지만 절감률·품질 수치가 자가 제출 — 독립 검증 필요)
