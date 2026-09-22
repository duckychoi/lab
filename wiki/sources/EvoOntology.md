---
title: "EvoOntology — '자기진화 온톨로지'의 이득 절반 이상은 데이터 의미가 아니라 모델별 접근 인터페이스에서 나왔다"
type: source
domain: ai-news
tags: [ai-news, hf-paper, github, data-agent, ontology, semantic-layer, mcp, text-to-sql, self-evolving, 에이전트-메모리-레이어, 한정어-탈락]
created: 2026-09-22
updated: 2026-09-22
sources: []
reliability: medium
---

# EvoOntology: A Self-Evolving Ontology Layer for Data Agents

> [!insight] 핵심 인사이트 — **"온톨로지"라 부르지만 진화 결과는 백본마다 다르고, 옮기면 손해다**
> 구조: 온톨로지를 **MCP 서버**(Content · Schema · Tool 3층)로 감싸 에이전트가 **필요한 항목만 런타임에 조회**(`browse` · `resolve` 두 도구 + 세션 manifest)하게 한다. 빌더 에이전트가 probe 쿼리로 **근거가 확인된 후보만** 초기 온톨로지에 넣고(Evidence 보존), 진화 에이전트가 궤적을 귀인 → **한 층만 고치는 패치** → **백본별 paired 검증을 margin τ 이상 넘을 때만 채택**한다.
>
> 🎯 **§5.4 "Divergence across Backbones" 가 무엇이 갈리는지 적는다**(수집기 미정독 절):
> - 채택된 **Term 식별자 집합**의 쌍별 Jaccard가 **최대 0.62** — Claude 두 모델끼리(**0.55**)가 GPT 두 모델끼리(**0.61**)보다 **덜 겹친다**. 같은 회사 모델이라고 같은 온톨로지로 수렴하지 않는다.
> - 채택된 편집의 **종류도 다르다** — Opus-4.8은 더 자세한 manifest 변형을 남기고, GPT-5.5는 Evidence 아래 **짧은 SQL 조각 라이브러리**를 만든다.
> - **교차 이식**: 진화된 저장소를 다른 백본에 주면 **모든 비대각 칸이 최소 6.6점 하락**, 열 평균 하락 **−6.6(Sonnet-5) ~ −10.9(GPT-5.5)**.
> - 부록 C: 채택 이득의 **57%가 Tool 층 편집**(6라운드 — manifest·노출 방식) · Content 34%(11라운드) · Schema 9%(3라운드). 표 6에서도 **Tool-only(+13.2) > Content-only(+8.7)**.
>
> → **이득의 최대 몫은 "데이터가 무엇을 뜻하는가"가 아니라 "이 모델에게 어떻게 보여 줄까"에서 나왔다.** 이름은 온톨로지지만 실질은 **백본에 맞춰 튜닝된 접근 계층**에 가깝다. 모델을 바꾸면 **재진화가 필요하다**는 운영 비용이 따라온다. ⚠️ 저자 자신도 *"identifier overlap alone cannot determine semantic equivalence"* 라고 한정했다 — 의미가 정말 다른지는 미확정.

> [!note] ✅ 수집기 부록 B 수치 — **전건 원문 일치, 산술도 닫힌다**
> 표 8(DDR-Bench, 4백본 평균):
>
> | 지표 | Baseline | Initial | Evolved |
> |---|---|---|---|
> | 입력 토큰/턴(K) | 3.2 | 4.1 | **4.6** |
> | 출력 토큰/턴(K) | 0.4 | 0.4 | 0.4 |
> | 턴/과제 | 14.6 | 11.2 | 8.4 |
> | 총 토큰/과제(K) | 52.6 | 50.4 | 42.0 |
> | Traj-Wise | 69.5 | 81.8 | 89.5 |
>
> 볼트 검산: 14.6×3.6=52.6 · 11.2×4.5=50.4 · 8.4×5.0=42.0 — **세 열 전부 턴 수 × 턴당 토큰 = 총 토큰**. 약 −20%(42.0/52.6=0.80) 일치.
> 🟡 **수집기가 옮기지 않은 칸 하나**: 턴당 입력은 Initial 4.1K에서 멈추지 않고 **Evolved 4.6K로 더 늘어난다**. *"턴은 줄고 턴당 컨텍스트는 계속 늘어난다"* 가 정확한 그림이다 — 짧은 과제(턴 수가 원래 적은 과제)에서는 이 거래가 역전될 수 있다(볼트 추론, 논문에 과제 길이별 분해 없음).

> [!warning] 🔴 초록 ↔ 본문 불일치 — **"네 개 백본" vs "여섯 개 백본"**
> 초록: *"three well-adopted data-agent benchmarks with **four** LLM backbones"*. 본문 §4.2: *"We evaluate EvoOntology on **six** LLM backbones: GPT-5.5, GPT-5.6-sol, Claude-Sonnet-5, Claude-Opus-4.8, DeepSeek-V4-Flash, Qwen3.5-Flash"*. 결론은 다시 *"six"*.
> 실제 구조: **주 결과표(1·3·4)는 6개**, **분석·절제(§5, 표 2·5–8)는 GPT·Claude 4개 부분집합**. 🎯 **빠진 두 개가 약한 백본이다** — Qwen3.5-Flash의 DDR Traj-Wise 이득 **+4.8**(6개 중 최소), DeepSeek-V4-Flash 기준선 30.3. **절제·비용 분석은 강한 모델에서만 했다.**

> [!warning] ⚠️ "기존 시맨틱 레이어 대비 우위"의 **비교 대상은 자기 빌더의 산출물**이다
> 초록 *"outperforms … **existing semantic-layer approaches**"*. 실제 `Baseline + SL` 의 정의: *"prepends **the builder-agent's semantic layer** into the agent's context as a static prompt fragment"* — 인용된 방법들은 **전달 방식**의 출처일 뿐, **내용물은 EvoOntology 빌더가 만든 것**이다. dbt·OWL 같은 외부 시맨틱 레이어 제품과 비교한 게 아니다.
> 🎯 그래서 이 대조가 실제로 보여 주는 것은 **"같은 내용을 프롬프트에 다 넣기 vs MCP로 골라 조회하기"** 다 — 그 자체로는 유용한 결과다: 정적 주입은 DDR Claude-Sonnet-5에서 **−15.0**, BIRD GPT-5.5 EX **−5.6**(반면 VES는 전 백본 상승 — *"SQL은 잘 짜지만 정답은 틀린다"*).
> ⚠️ **InsightBench 표 3에서 두 행이 완전히 같다**: GPT-5.5 `53.4 / 48.6 / 51.0` · Claude-Opus-4.8 `55.8 / 50.5 / 53.2` 가 **Baseline+SL 행과 EvoOntology 행에서 소수점까지 동일**하다. 즉 6개 중 2개 백본에서 EvoOntology는 **정적 SL을 이기지 않았다(동점)**. 본문은 설명하지 않는다 — 진화 라운드가 하나도 채택되지 않았는지, 전사 오류인지 **미확인**. InsightBench 평균 이득은 **+1.9점**, 초기→진화 기여는 **+0.2점**(4백본)으로 원래 작다.

> [!note] 📌 볼트 실측 (2026-09-22)
> HF API: 업보트 **126**(수집기 56 → +70) · 저자 4(Renmin University of China, 교신 Shaolei Zhang) · `publishedAt` **2026-09-14** · `submittedOnDailyAt` **2026-09-21**(7일 차, 수집기 일치).
> GitHub API: ★**310**(수집기 213 → +97) · fork 25 · **MIT** · Python · created 2026-09-15 · pushed 2026-09-21 · **파일 345개 · `.py` 180개** — `evoontology/`(ontology·runtime·evolution·evaluation·trajectory·trigger·visualization) · `benchmarks/`(bird · ddr_10k · insightbench) · `plugins/`(claude-code · evoontology-codex, 각각 `.mcp.json`) · `tests/`. ✅ **코드 실재, 벤치 어댑터까지 공개.**
> ⚠️ **README 설치 명령이 가리키는 레포가 공개돼 있지 않다**: `claude plugin marketplace add MeiduoChong/EvoOntology` — GitHub API상 `MeiduoChong/EvoOntology` 는 **404**, 사용자 `MeiduoChong` 의 공개 레포는 **0개**. 조직 레포(`ruc-datalab`)에는 marketplace 매니페스트 파일이 없다. **README의 원라인 설치는 현재 그대로는 안 될 가능성이 높다**(설치 자체는 미시도 — 확인 필요). 조직 레포에서 `plugins/claude-code/` 를 직접 쓰는 우회는 가능해 보인다.
> README 성능표(4백본 평균) BIRD 63.6→72.4 · InsightBench 53.2→54.2 — 볼트가 논문 표 3·4 행으로 재계산해 **일치 확인**.

## 도메인별 추출 (ai-news)

**도메인 판단**: `local-llm`(에이전트 메모리) 후보였으나 **ai-news** 로 둔다. 이유 — ① 작업 간 **근거를 남겨 재사용**한다는 점은 메모리 성격이 맞고, 표 2가 실제로 **ReAct+Memory(69.5→75.8)** 와 비교해 13.7점 앞선다. ② 그러나 실험 백본이 전부 API급 대형 모델이고, 포함된 소형 계열(Qwen3.5-Flash)에서 이득이 **최소(+4.8)** 다. 로컬/소형 실배포 근거가 없다. 볼트의 같은 계열 페이지([[WrenAI]] · [[DataFlow-Harness]] · [[PageIndex]])도 ai-news다. 메모리 축과의 연결은 [[에이전트-메모리-레이어]] 링크로 둔다.

- **신뢰도**: ⭐⭐ — ★310 · MIT · 코드·벤치 어댑터 공개 · 비용 부록 산술 일치 / 초록↔본문 백본 수 불일치 · SL 비교군이 자기 산출물 · InsightBench 동일 행 2건 · 설치 경로 404.
- **즉시 활용**: **조건부 YES.** Claude Code 플러그인(`.mcp.json` 포함)이 레포 안에 있다. 볼트/ChinameBot 쪽 SQLite·CSV가 있다면 조직 레포 경로로 붙여 볼 수 있다. 🔴 단 **진화는 held-out 검증 세트(적응 폴드의 30%)와 채점기가 있어야 돈다** — 정답 채점이 없는 개인 데이터에서는 **빌더(Initial)까지만** 현실적이다. Initial만으로도 DDR에서 69.5→81.8(이득의 약 60%)이다.
- **6개월 영향력**: 🎯 **"시맨틱 레이어를 프롬프트에 붙이지 말고 도구로 조회시켜라"** 가 실측 근거를 얻었다. [[WrenAI]] 류 컨텍스트 레이어 제품과 같은 방향. 동시에 **모델 교체 = 레이어 재튜닝**이라는 비용도 수치로 드러났다(−6.6 ~ −10.9).
- **대체 관계**: 정적 스키마 설명·data dictionary 프롬프트 주입을 **대체**. 에피소드 메모리([[mem0]] 류 궤적 재생)와는 **경쟁**하되, 저자 주장은 *"타입이 있는 구조를 노출한다"* 는 차이.
- **허와 실**: ✅ 비용 부록은 정직하다(턴당 비용 증가를 숨기지 않음). ✅ 절제가 게이트(−11.2) · 귀인(−6.3)을 하중 부품으로 지목 — *"더 자주 고치기"보다 "덜 받아들이기"* 가 핵심. 🔴 "기존 시맨틱 레이어 대비"는 과장된 표현이고, 🔴 초록의 백본 수가 틀렸다.
- **액션**: 조직 레포의 `plugins/claude-code/` 로 **Build 단계만** 로컬 SQLite 1개에 돌려 manifest 크기와 `browse`/`resolve` 호출 수를 본다.

> [!action] 당장 할 것 (1건)
> `ruc-datalab/EvoOntology` 의 `plugins/claude-code/` 를 직접 경로로 설치해 **볼트가 가진 SQLite/CSV 하나에 Build(Initial)만** 실행 → 턴당 입력 토큰 증가분(논문 3.2K→4.1K)이 **짧은 질의에서도 이득인지** 턴 수와 함께 기록한다.

> [!question] 미해결 질문
> 1. InsightBench 표 3의 **Baseline+SL = EvoOntology 동일 행 2건**은 진화 미채택인가 전사 오류인가.
> 2. Tool 층 편집(이득 57%)이 **백본별로 얼마나 다른가** — 교차 이식 하락의 주원인이 Tool인지 Content인지 분해 없음.
> 3. `MeiduoChong/EvoOntology` 마켓플레이스가 비공개인지, 이름이 바뀐 것인지.

## 관련 페이지
- [[에이전트-메모리-레이어]]
- [[관련성-판단-주체]]
- [[WrenAI]]
- [[DataFlow-Harness]]
- [[AgenticDataBench]]
- [[R3-SQL]]
- [[PageIndex]]
- [[mem0]]
- [[하네스-설계-축]]
- [[한정어-탈락]]
- [[게시일-이중화]]
- [[ai-news]]

## 원본
- 출처: https://huggingface.co/papers/2609.15779 · https://arxiv.org/abs/2609.15779 · https://github.com/ruc-datalab/EvoOntology
- 날짜: arXiv `publishedAt` **2026-09-14**(v1) · HF 데일리 `submittedOnDailyAt` **2026-09-21**(7일 차) → [[게시일-이중화]]
- 볼트 실측(2026-09-22): 업보트 **126**(수집기 56) · 저자 4 · GitHub ★**310**(수집기 213) · fork 25 · MIT · 파일 345 / `.py` 180 · 벤치 어댑터 3종 · Claude Code·Codex 플러그인 · `MeiduoChong/EvoOntology` **404**
- 수치 출처: arXiv HTML **목차 + 표 1·2·3·4·5·6·7·8 + §5.4 + 부록 A·B·C** 원문 실열람, GitHub README 성능표 대조
- raw 대비: ✅ 부록 B 수치 전건 일치 · 🟡 Evolved 턴당 입력 4.6K 누락 · 🎯 §5.4 정독(Jaccard ≤0.62, 교차 이식 −6.6~−10.9) · 🔴 초록 "4 backbones" ↔ 본문 6 · ⚠️ SL 비교군 = 자기 빌더 산출물 · ⚠️ InsightBench 동일 행 2건 · ⚠️ 설치 경로 404
- 신뢰도: ⭐⭐ (코드·벤치 공개 · 비용 산술 일치 / 초록 불일치 · 비교군 자작 · 설치 경로 미공개)
