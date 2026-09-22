---
title: "Code2Skill — '스킬 100만 건'의 공개본은 75만 장이고, 비교한 궤적 스킬뱅크는 스킬 없음보다 낮았다"
type: source
domain: ai-news
tags: [ai-news, hf-paper, github, hf-dataset, agent-skills, skill-bank, code-mining, 에이전트-스킬, 단위-불일치, 게시일-이중화, ant-international]
created: 2026-09-22
updated: 2026-09-22
sources: []
reliability: medium
---

# Code2Skill: Grounded Skill Synthesis from Code at Scale for Agentic Intelligence

> [!insight] 핵심 인사이트 — **스킬 원천을 "에이전트 궤적"에서 "소스 코드"로 옮겼다. 검증 장치가 핵심이다**
> 코드 단위를 원자 연산·복합 워크플로·반복 패턴 레코드로 추출 → **소스 본문·레포명·경로를 가린 채** 레코드만 보고 코드를 재생성 → 소스와 비교하는 판정기가 직접 채택하거나, 실패하면 **재판정(adjudication)** 으로 넘긴다. 에이전트 경험이 쌓이기 **전에** 쓸 수 있는 스킬을 만든다는 것이 논지다.
> 🎯 볼트 [[에이전트-스킬]] 의 ③ 증류 축에서 [[Repo-To-Skill]](레포 1,000개 → 5,000+개)의 **규모를 약 200배로 키운 사례**다. 그리고 [[Repo-To-Skill]] 에 대해 볼트가 적은 공백 — *"5,000개를 전부 로드할 수 없으므로 **검색이 곧 성능**인데 그 부분이 비어 있다"* — 에 **RQ4가 부분 답을 준다**: k=3에서 **요약 렌더링이 컨텍스트를 88.9% 줄이고(6,352→707자) 성능을 유지·개선**, k를 1→10으로 늘려도 이득은 미미(Qwen +1.40, DS4-Flash는 무스킬 이하).

> [!note] ✅ "+11.7%" 는 **상대 향상**이다 — 본문이 명시한다
> 본문 §1: *"improves the macro-average score from **42.90** without skills to **47.90** with skills, achieving an **11.7 % relative gain** and improving on 57 of 72 evaluation runs."*
> 볼트 검산(표 1, 9개 설정 Avg 열): 평균 **42.901 → 47.903**, 절대 **+5.00점**, 상대 **+11.66%**. 설정별 절대 +2.26~+7.39점, 상대 +6.0~+20.7% 도 본문과 일치.
> 🎯 **같은 날 [[CodeMidas]] 초록도 "+11.7%" 를 쓰는데 그쪽은 %p(절대)다**(10.0→21.7, 상대로는 +117%). **같은 인쇄 숫자가 10배 다른 크기를 뜻한다** → [[단위-불일치]] 사례.

> [!warning] 🟡 "72 중 57" — 나머지 15건의 내역 (볼트 표 1 전수 계산)
> **57 향상 · 6 동점 · 9 하락.** 동점 6건 중 **5건이 LongCLI**(점수 0.00/20.00 등 5점 단위의 작은 과제 세트), 1건 AgentBench.
> 하락 9건: **BigCode 3 · AgentBench 3** · Terminal 1 · GPQA 1 · HMMT 1. 저자도 *"mixed results under reasoning mode on BigCodeBench"* 라 인정.
> ✅ 수집기의 *"15건은 못 이김"* 은 정확하다 — 다만 **"못 이김" 중 6건은 지지 않았다.**

> [!warning] 🔴 RQ2 "궤적 스킬뱅크 7개 벤치 전승" — **비교군 셋 다 스킬 없음보다 낮다**
> 표 2(DS4-Flash reasoning, 5회 평균) 7개 벤치 평균: Trace2Skill **31.0** · ExpeL **27.9** · SkillRL-Bank **32.8** · Code2Skill **49.5**.
> 볼트 대조: **같은 모델·같은 루프의 무스킬 행(표 1 DS4-Flash reasoning No, GPQA 제외 7개)** 평균은 **41.6**이다. 세 궤적 뱅크가 **7개 중 5~6개 벤치에서 무스킬보다 낮다**(예: SWE — 무스킬 34.32 vs Trace2Skill 6.0 · ExpeL 7.5).
> 🎯 **"궤적 스킬보다 낫다"는 사실이지만, 비교군이 스킬을 안 쓰는 것보다 해로운 상태였다.** 저자 설명: 궤적 뱅크는 Qwen3.5-397B로 **별도 과제 분할**에서 만들었다. 이게 공정한 재현인지, 이식 실패인지 논문은 논의하지 않는다. 헤드라인 *"outperforms on all seven"* 은 [[한정어-탈락]] 이 아니라 **기준선 선택의 문제**다.
> ⚠️ 부수 관찰: 표 2의 Code2Skill 7개 값(44.7·42.3·70.0·53.3·45.2·30.0·61.3)이 표 1 단일 행(44.70·42.34·70.00·53.33·45.20·30.00·61.32)과 **반올림까지 전부 같다.** 표 2는 "5회 평균 ± std"라 적혀 있다 — 표 1도 5회 평균이면 문제없고, 아니면 한쪽 라벨이 틀렸다. **미확인.**

> [!warning] 🔴 "1,006,822 채택 레코드" ≠ 공개된 것 (볼트 HF 데이터셋 실측)
> HF `ant-intl/DeveloperSkills-Code2Skill` 의 `RELEASE_STATUS.json` / `statistics.json`:
> - `cards` **750,748행** (목적 클러스터 대표 카드)
> - `edges` **945,993행** (= `support_sum`, 카드에 묶인 원 레코드)
> - `dropped` **60,829행** — *"excluded by the low-value filter … for audit, not model training"*
>
> 🎯 **945,993 + 60,829 = 1,006,822** — 헤드라인 100만은 **저가치 필터로 스스로 뺀 6만 건을 포함한 수**다. 부록 B에서 그 풀은 **보존가치 0%** 판정을 받았다. 에이전트가 실제로 검색하는 단위는 **75만 장**이다.
> ⚠️ 그리고 그 대표 카드 방식(purpose indexing)은 RQ4에서 **4개 모델-렌더러 조합 중 3개에서 성능을 낮췄다**(*"mixed effects on pass rate"*). **공개본의 기본 뷰가 논문에서 혼재 결과를 낸 설정**이다.

> [!warning] 🔴 공개 상태가 서로 모순된다
> 1. **GitHub README**: *"The repository is currently **pre-release and privately hosted**; it is **not yet a public open-source release**."* / *"**No license is implied** by the current local repository."* — 그런데 이 README가 **공개 레포**에 올라와 있다. GitHub API `license: null`.
> 2. **HF 데이터셋 카드** 프론트매터: `license: apache-2.0`. 같은 저장소 안 `LICENSE_REVIEW.md`: *"public publication requires a provenance and license decision … **Do not replace `license: other` with a standard license** until the dataset authors decide"* · *"no verified upstream URL, commit SHA, or per-repository license identifier."*
> → **카드는 Apache-2.0, 내부 검토 문서는 "표준 라이선스 붙이지 말 것"**. 19,769개 레포의 원 라이선스 추적이 안 된 상태라는 것을 저자 문서가 자인한다. [[검사가능성-공사]] 와 반대로 **출처 칸이 비어 있다고 스스로 적어 둔** 경우다.
> 3. ⚠️ HF datasets-server: *"No (supported) data files found"* — 카드의 `configs` 경로(`data/cards/*.parquet`)와 실제 파일 위치(`codeskillbank_hf_release_with_patterns_20260814/data/...`)가 어긋나 **뷰어/기본 로딩이 안 된다**(볼트 추정 원인, 로딩 직접 시도는 안 함).

> [!note] 📌 부록 B 인간 평가 — 표 4 원문
> | 결과 풀 | 설명 정확도 | 재구성 정확 | 보존 가치 |
> |---|---|---|---|
> | 가치 필터 제거 | 88% | – | 0% |
> | 직접 채택 | 96% | 84% | 76% |
> | 재판정 채택 | 88% | **0%** | 84% |
> | 최종 거부 | 32% | 0% | 28% |
> | 채택뱅크 요약 | 92% | 84% | 80% |
>
> ⚠️ **표본 수·평가자 수가 적혀 있지 않다.** 모든 칸이 4의 배수라 **풀당 25건**과 정합한다(볼트 추정, 원문 미기재).
> ⚠️ 요약 행 92%·80%는 두 채택 풀의 **단순 평균**((96+88)/2, (76+84)/2)과 같다 — 두 풀의 실제 크기 비율로 가중했는지 불명이고, 재판정 채택 비율 자체가 본문에 없다.
> 🎯 **재판정 채택 레코드는 재구성이 0% 맞았다** — 즉 은행 안 일부는 *"설명은 정확하지만 그 설명만으로는 코드가 재현되지 않은"* 레코드다. "검증된 스킬"의 검증이 두 등급이다.

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐⭐ — 업보트 92 · GitHub ★32(**라이선스 없음, 저자 스스로 "비공개 사전 릴리스"**) · `.py` 21개(파이프라인 실재, `pipeline.py`·`prompts.py` 등) · HF 데이터셋 266 다운로드/15 좋아요 / 궤적 비교군이 무스킬 이하 · 라이선스 모순 · 인간평가 n 미기재.
- **즉시 활용**: **부분 YES.** 75만 카드의 `task_family`(validation 46.4% 등)·요약 필드를 **로컬 검색 스킬풀**로 써 볼 수 있다. 🔴 단 **라이선스가 확정되지 않았다**(내부 문서가 표준 라이선스 부착을 막고 있음) — 개인 실험까지만.
- **6개월 영향력**: 🎯 **"스킬은 경험에서 쌓는다"는 전제가 흔들린다** — 코드에서 먼저 깔아 둘 수 있다. RQ5도 같은 방향: SWE-World 코딩 RL(Qwen3-32B, step 150)에서 **사후 리뷰 주입 24→38%**, 정책 프롬프트 32%·보상측 31%. ⚠️ 저자 자인 *"single checkpoint without repeated seeds or learning curves"*.
- **대체 관계**: 궤적 기반 스킬 증류(Trace2Skill·ExpeL·SkillRL)와 **경쟁**, [[COBRA-Skills]](어느 스킬을 고를지)와는 **직렬**.
- **허와 실**: ✅ +11.7%는 상대값이라고 저자가 정확히 썼고, RQ6 *"initial evidence"*·*"does not establish equivalence"* 한정어도 정직하다. 🔴 93.50 vs 93.00은 **스킬 50개짜리 두 뱅크를 400문항에 돌린 결과로 0.5%p = 2문항**이고(서로 다르게 푼 문항 16개: 7 vs 9), **무스킬 기준선이 본문에 없다** — AI코드 스킬이 "쓸모 있다"는 근거로는 약하다.
- **액션**: HF 데이터셋 `cards` 샤드 1개를 내려받아 **요약 필드만 k=3으로** 볼트 코딩 질문에 붙여 본다(RQ4 권장 설정).

> [!action] 당장 할 것 (1건)
> `DeveloperSkills-Code2Skill` 의 `cards/train-00000.parquet` 1개만 받아 `task_family` 분포와 요약 필드 길이를 확인 → **[[Repo-To-Skill]] 5,000개와 같은 과제로 k=3 요약 주입 비교**. (라이선스 미확정이므로 재배포 금지.)

> [!question] 미해결 질문
> 1. 1,006,822 중 **재판정 채택 비율** — 재구성 0% 레코드가 은행의 몇 %인가.
> 2. 표 1과 표 2의 Code2Skill 값이 동일한 이유(표 1도 5회 평균인가).
> 3. 궤적 뱅크 비교군이 무스킬보다 낮은 원인 — 구축 모델(Qwen3.5-397B)과 평가 모델(DS4-Flash) 불일치 영향?

## 관련 페이지
- [[에이전트-스킬]]
- [[Repo-To-Skill]]
- [[COBRA-Skills]]
- [[CodeMidas]]
- [[단위-불일치]]
- [[선택비용과-중복성]]
- [[검사가능성-공사]]
- [[한정어-탈락]]
- [[게시일-이중화]]
- [[ai-news]]

## 원본
- 출처: https://huggingface.co/papers/2609.05571 · https://arxiv.org/abs/2609.05571 · https://github.com/ant-intl/Code2Skill · https://huggingface.co/datasets/ant-intl/DeveloperSkills-Code2Skill
- 날짜: arXiv `publishedAt` **2026-09-04**(v1) · HF 데일리 `submittedOnDailyAt` **2026-09-21** → **17일 차**. 🔴 [[게시일-이중화]] 페이지의 *"최대 7일"* 관측을 **깬다**.
- 볼트 실측(2026-09-22): 업보트 **92**(수집기 56) · 저자 7(Ant International) · GitHub ★**32**(수집기 10) · fork 0 · **license null** · 파일 38 / `.py` 21 · created·pushed 2026-09-08 · HF 데이터셋 cards 750,748 / edges 945,993 / dropped 60,829 · 카드 `license: apache-2.0` ↔ `LICENSE_REVIEW.md` 모순 · datasets-server 로딩 실패
- 수치 출처: arXiv HTML **목차 + 표 1(전수 재계산)·2·3·4 + §5.4–5.7 + 부록 B·C.3** 원문 실열람, GitHub README, HF 데이터셋 `RELEASE_STATUS.json`·`statistics.json`·`LICENSE_REVIEW.md`·`data_dictionary.md`
- raw 대비: ✅ 57/72 · 93.50/93.00 · 17일 차 · 부록 B 4풀 구조 일치 · ✅ **+11.7% = 상대(42.90→47.90, +5.0점) 확정** · 🟡 15건 = 동점 6 + 하락 9 · 🔴 궤적 비교군 전원 무스킬 이하 · 🔴 100만 = 채택 94.6만 + 필터 제거 6.1만, 공개 카드 75만 · 🔴 라이선스 모순 · ⚠️ 인간평가 n 미기재
- 신뢰도: ⭐⭐ (파이프라인 코드·데이터 실재 · 상대/절대 명시 정직 / 비교군 약함 · 라이선스 미확정 · 표본 수 미기재)
