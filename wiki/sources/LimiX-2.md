---
title: "LimiX-2 — 표형 데이터 파운데이션 모델을 p(y|x)에서 p(x,y)로. 3개 벤치 Elo 1위, 그러나 1위 마진 상당수가 신뢰구간 안이다"
type: source
domain: ai-news
tags: [ai-news, hf-paper, tabular, foundation-model, in-context-learning, pfn, causal-discovery, scm, scaling-law, stable-ai, tsinghua, non-commercial]
created: 2026-09-19
updated: 2026-09-19
sources: [TabPFN.md, tabfm-1.0.0.md]
reliability: medium
---

# LimiX-2 (arXiv 2609.17488)

> [!insight] 핵심 인사이트 — **"라벨 예측기"를 "빈칸 채우기 기계"로 바꿨다. 분류·회귀·결측치 보간이 같은 질문이 된다**
> 기존 tabular PFN([[TabPFN]] 계보)은 *"designated target"* 한 열의 `p(y | x, D_context)` 를 배운다. LimiX-2의 CMN(Contextual Mechanism Networks)은 **임의의 열을 마스킹하고 나머지로 채우는** CCMM(Context-Conditional Masked Modeling)으로 `p(x, y | D_context)` 를 겨냥한다.
> 🎯 결론 절 원문이 핵심을 한 줄로 적는다: *"a design paradigm that **generalizes label prediction to the imputation of arbitrary masked columns**"* — 라벨은 "마스킹된 열 중 하나"일 뿐이다. 그래서 **한 체크포인트가 분류·회귀·결측치 보간을 파라미터 업데이트 없이** 한다(배포 README의 지원 태스크: `✅ cls ✅ reg ✅ imputation`).
> 📌 **왜 중요한가**: 실무 표 데이터의 최대 골칫거리는 결측치인데, 기존 PFN은 결측치를 "입력의 결함"으로 다뤘다. CMN은 그걸 **학습 목표 그 자체**로 삼는다. 자사 벤치 BCCO가 *"missing and incomplete features"* 에 초점을 둔 것도 이 설계와 짝이다(단 자사 벤치라는 한정 — 아래).

> [!insight] 🎯 초록에 없던 수치 — 본문 전수 (수집기는 초록만 읽었다)
> **Figure 1 / 표 2·5·6 (Elo, Random Forest=1000 고정, 95% 부트스트랩 CI 2000회)**
> ```
>            LimiX-2 Elo [CI]          차점                         본문이 밝힌 격차
> TabArena   1935 [−77, +111]          TabFM+ 1818 [−84, +109]      +117.4
> TALENT     1506 [−32, +37]           TabFM  1471 [−28, +30]       +35
> BCCO       1432 [−38, +45]           AutoGluon 1.6 (EX,4h) 1376   +56 (TabFM +63, LimiX-16M +202)
> ```
> - TabArena(51 데이터셋): improvability **3.3% vs TabFM+ 6.2%** · 평균 순위 **5.5 vs 9.0** · 집계 승수 **18.9 vs 5.3**. 분류 38개 Elo 1917 / 회귀 13개 Elo **2206**(차점 TabFM+ 2063, AutoGluon 2060).
> - TALENT(288 데이터셋): improvability **6.75% vs 9.17%**(상대 −26.4%) · 승수 84.3 vs 50.1
> - BCCO(156 데이터셋): improvability **6.97% vs 12.24%**(상대 −43.1%) · 승수 50.4 vs 16.7
> - 🎯 **"TabFM보다 4배 작은데 이긴다"** (*"surpasses TabFM despite being 4 times smaller in model parameter size"*) — LimiX-2 최대 구성 **406.2M**(배포 README 표기 400M).
> - **스케일링(표 8 전체)**: 12.5M→406.2M 6개 크기, 로그선형 OLS
> ```
> 평가              α(100M 적합 Elo)   β(2배당 Elo)   R²       RMSE
> TabArena          1863.88            34.68          0.9808   8.31
> TALENT cls        1427.25            22.16          0.9792   5.53
> TALENT reg        1545.12            18.26          0.9680   5.69
> BCCO cls          1295.86            11.24          0.9617   3.84
> BCCO reg          1795.89            30.06          0.9702   9.03
> ```
> TabArena Elo **1766(12.5M) → 1935(406.2M)**, 32.5배 크기에 +169. *"no clear evidence of performance saturation up to 406.2M"*.

> [!warning] 🔴 **"1위"와 "통계적 우위"는 다른 진술이다** — 본문 자체 CI로 검산
> - **TabArena**: LimiX-2 하한 1935−77 = **1858** < TabFM+ 상한 1818+109 = **1927** → **CI 겹침.** 117점 격차는 점추정.
> - **TALENT**: LimiX-2 하한 **1474** < TabFM 상한 **1501** → **겹침.** 하위 범주에서는 더 얇다 — 다중분류 **1520 vs TabFM 1517(+3)**, 회귀 **1584 vs AutoGluon 1581(+3)**, CI 폭은 ±50~90.
> - **BCCO**: 다중분류는 **AutoGluon 1.6(1443)이 LimiX-2(1414)를 이긴다** — 표 6 캡션이 스스로 밝힌다: *"AutoGluon 1.6 (EX, 4h) leads on multiclass"*. 회귀 1859의 CI는 **[−112, +158]** 로 폭 270.
> 🎯 **"highest Elo across all five evaluation categories"(TALENT) 는 참이지만, 그중 두 범주는 3점차다.** 초록의 *"outperforms"* 는 **점추정 기준 서열**로 읽어야 한다. ✅ 다만 **CI를 표에 직접 적은 것 자체는 모범 사례**다 — 볼트가 이 검산을 할 수 있었던 건 저자가 구간을 공개했기 때문이다. → [[자기제한-명시]]
> 📌 **개선도(improvability)·승수 지표에서는 격차가 더 크고 일관적**(TabArena 3.3% vs 6.2%, BCCO 승수 3.0배) — **Elo보다 이쪽이 우위의 더 강한 증거**다.

> [!warning] 🔴 평가 설계의 한정 4개 — 본문에 다 있다, 초록엔 없다
> 1. **BCCO는 자사 벤치다** — 인용이 *"BCCO (**LimiX Team**, 2025)"*. 3개 중 1개는 **출제자가 응시자**다. 이 벤치가 겨냥하는 결측·불완전 데이터가 CMN의 설계 목표와 일치한다 → [[분포내-우위]] 의 약한 형태(추정: 데이터 누수 증거는 없음, **과제 선정의 우위**).
> 2. **TALENT 12개 데이터셋 제외** — *"Excluding 12 classification datasets with **more than 10 target classes**"*. 제외 사유 미기재. [[tabfm-1.0.0]] 의 "최대 10클래스" 제약과 같은 선이다 — 비교 대상 제약 때문인지 LimiX-2 자신의 제약인지 **본문으로는 판별 불가**(미확인).
> 3. **기본값 vs 튜닝** — TabArena에서 LimiX-2는 **(D) 기본 설정**, 일부 기준선은 (T) 튜닝·(T+E) 튜닝+앙상블. 이건 LimiX-2에 **불리한** 방향이다(✅ 공정성 쪽). 단 기준선 점수는 **공개 리더보드 인용**(*"accessed September 15, 2026"*)이고 LimiX-2만 직접 실행 — 실행 환경 비대칭.
> 4. **한계(Limitations) 절이 없다.** 추론 비용·GPU 메모리·행/열 수 상한이 본문에 **0건**. 배포 README도 `cuda recommended` 만 적는다.

## 인과 골격 복원 — 한정어가 결론에서 사라진다

> [!insight] 표 7 전체 — **F1은 6개 데이터셋 전부 1위, SHD는 6개 중 5개 1위**
> 방법: 각 변수를 차례로 타깃으로 두고 **피처 어텐션 점수에 임계값**을 걸어 무방향 골격을 만든다. 인과발견 방법은 방향 그래프를 무방향으로 변환해 비교.
> ```
> F1 ↑            Sachs   UF      CausalCh.  PATHFINDER  DIABETES  PIGS
> LimiX-2         0.7143  0.8617  0.7013     0.7829      0.7846    0.9385
> EXAONE Tabular  0.6429  0.6492  0.5195     0.5486      0.6994    0.8955
> TabFM           0.4286  0.2727  0.4156     0.2400      0.6028    0.6895
> TabICLv2        0.6429  0.1818  0.2857     0.1600      0.2277    0.1612
> TabPFN-3        0.5714  0.6845  0.3636     0.1429      0.0426    0.0271
> Xiaomi-TabLDM   0.3704  0.2364  0.2078     0.0114      0.2211    0.2426
> XGBoost         0.5714  0.2545  0.2632     0.2914      0.4111    0.8125
> TabCausal       0.5600  0.4000  0.5970     0.0000      0.1855    0.0000
> PC              0.6400  0.3817  0.4000     0.3659      0.4674    TIMEOUT
> GES             0.6400  0.6044  0.6234     TIMEOUT     TIMEOUT   TIMEOUT
> LiNGAM          0.5600  0.5521  0.6667     –           –         –
> AVICI           0.5000  0.4783  0.2917     0.0485      0.0251    0.0000
> NOTEARS-MLP     0.5600  0.4030  0.4571     0.6146      TIMEOUT   0.8907
> DAG-GNN         0.4167  0.0860  0.2642     0.3846      0.4320    0.1529
>
> SHD ↓           Sachs   UF      CausalCh.  PATHFINDER  DIABETES  PIGS
> LimiX-2         8       26      23         76          263       77
> EXAONE Tabular  10      67      37         158         367       131
> TabFM           16      80      45         266         485       389
> TabICLv2        10      90      55         294         943       1051
> TabPFN-3        12      59      49         300         1169      1219
> Xiaomi-TabLDM   17      84      61         346         951       949
> XGBoost         12      82      56         248         719       235
> TabCausal       11      81      27         189         685       592
> PC              9       81      39         156         449       TIMEOUT
> GES             9       72      29         TIMEOUT     TIMEOUT   TIMEOUT
> LiNGAM          11      73      21 🔴      –           –         –
> AVICI           12      72      34         196         622       592
> NOTEARS-MLP     11      80      38         158         TIMEOUT   145
> DAG-GNN         14      85      39         144         497       543
> (🔴 CausalChamber SHD는 LiNGAM 21 < LimiX-2 23 — 유일하게 1위를 놓친 칸)
> ```
> 🎯 **이건 인상적이다** — 전용 인과발견 알고리즘(PC·GES·NOTEARS)이 12시간 타임아웃에 걸리는 이산 네트워크에서 LimiX-2는 **추가 학습 없이 한 번의 forward pass 부산물(어텐션)로** F1 0.78~0.94를 낸다.
> 🔴 **성립 조건 (추정)**: 이산 3종(PATHFINDER·DIABETES·PIGS)은 bnlearn 베이지안 네트워크(*Scutari, 2026* 인용)에서 샘플링한 데이터 — 즉 **알려진 DAG에서 생성된 데이터**다. LimiX-2는 **SCM(구조적 인과모형)으로 생성한 합성 데이터로만** 사전학습됐다. 평가 데이터의 생성 과정이 사전학습 사전분포와 **같은 종류**다 → [[분포내-우위]] 가능성(추정, 저자 미언급). 다만 차점 대비 F1 격차는 연속(+0.07·+0.18·+0.03)과 이산(+0.17·+0.09·+0.04)이 **뚜렷이 갈리지 않고**, SHD 1위를 놓친 유일한 칸은 연속 쪽(CausalChamber)이다 — **표 7만으로는 이 가설을 지지도 반증도 못 한다.**

> [!warning] 🔴 [[한정어-탈락]] 발생 — **같은 문서 안에서 "골격 복원"이 "인과 추론"이 된다**
> ```
> 초록     "enabling accurate causal skeleton recovery"                (골격, 무방향)
> 본문 §5.5 "causal skeleton recovery performance as an operational measurement of causal awareness"
> 결론     "LimiX-2 performs classification, regression, missing-value imputation,
>           and causal inference in a single forward pass"               ← 🔴 골격 → 인과 추론
> HF README "the CMN paradigm also endows LimiX-2 with causal awareness"  ← 초록 "promotes" → "endows"
> ```
> 🎯 **골격(skeleton)은 "어느 변수 쌍이 직접 연결됐는가"까지다. 방향도, 개입 효과도 아니다.** "인과 추론"은 그보다 훨씬 넓은 주장이다. ✅ 수집기는 *"방향성(DAG 전체)이 아니라 골격까지라는 한정을 보존"* 했다 — **초록 기준으로는 정확했고, 저자 결론이 그 한정을 스스로 떨어뜨렸다.**
> 📌 그리고 **배포물의 지원 태스크에 인과발견은 없다**(`✅ cls ✅ reg ✅ imputation`). 어텐션 추출·임계값 설정 코드가 공개됐는지 **미확인** — 현재로서 표 7은 **재현 경로가 문서화되지 않은 결과**다.

## 저자·소속 — 본문 확인

- **저자 60명** ✅ (HF API `authors` 60 · 본문 §8 Contribution: Project Design and Lead **2**명(Xingxuan Zhang, Peng Cui) + Core Contributors **27** + Contributors **31** = 60)
- **소속**: 본문 표제 *"LimiX Team / Affiliation: **Stable AI & Tsinghua University**"* ✅
- 🔴 **"Stable AI" ≠ Stability AI** — 혼동 주의:
  - HF org `stable-ai`(fullname "Stable AI", 멤버 3·모델 5) ≠ `stabilityai`(fullname "Stability AI") — 별개 org (HF API 2026-09-19)
  - 모델 LICENSE 원문: *"Stable AI Technology Co., Ltd. … Wen Zhun (Xiong'an) Technology Co., Ltd. … **稳准智能(雄安)科技有限公司** … alternative Chinese and English names of the same legal entity"* → **중국 슝안 소재 법인**이다.
- 📌 60명 = 09-18 척도상 **기업 보고서형** ✅. 본문도 스스로 *"technical report"* 라 부른다.

## 라이선스 전환 — 🔴 이게 실무에서 가장 중요한 사실일 수 있다

> [!warning] LimiX-1(Apache 2.0) → **LimiX-2 가중치는 비상업 전용**
> - 배포 README 뉴스 원문: 2025-09 LimiX는 *"open-sourced under the **Apache 2.0** license"*
> - LimiX-2 가중치: **"StableAI LimiX Non-Commercial License"** — 원문 *"This License is a custom non-commercial model license. It is **not an open source license** and does not grant commercial usage rights."* Derivative Model 정의에 **파인튠·LoRA·증류 전부 포함**.
> - 코드: Apache 2.0 파생 + 추가 조항(*"Additional Attribution and Model Naming Requirements"*). GitHub API `license` = `other`/`NOASSERTION`.
> 🎯 [[tabfm-1.0.0]] 도 비상업이다. **표형 파운데이션 모델 상위권이 연달아 비상업으로 닫히는 흐름** — 상용 파이프라인에 넣을 수 있는 건 여전히 GBDT·AutoGluon 쪽이다(AutoGluon은 이 논문에서 차점권).

## 도메인별 추출 (ai-news)

- **신뢰도**: HF 업보트 **261**(`upvotes`) · 공개 2026-09-15(`publishedAt`) · `githubStars` **4,211**(HF 필드) / GitHub API `stargazers_count` **4,214** · fork 304 · open_issues 8 · 가중치 공개(`stable-ai/LimiX-2`, 다운로드 348·♥41, `LimiX-2.ckpt` 1,625,774,719 B) · 데모 Space 1개 (전부 2026-09-19 조회). → **medium**: CI·프로토콜·전체 표 공개로 문서 품질은 높으나, 3벤치 중 1개가 자사 벤치이고 제3자 재현·공식 TabArena 리더보드 등재는 미확인.
- **즉시 활용**: **부분 YES** — 비상업 실험 한정. 표 데이터 1건을 `LimiX-infer --task_type Classification` 으로 돌려 LightGBM과 비교 가능. GPU 권장. **상업 서비스 투입 불가**(라이선스).
- **6개월 영향력**: "표 데이터 = GBDT" 상식에 대한 파운데이션 모델 쪽의 가장 강한 근거 중 하나. 특히 **결측치 많은 실무 표**에서 "보간 → 모델 학습" 2단 파이프라인을 1단으로 줄일 수 있다. 스케일링 곡선이 406M까지 포화 없음 → 10억급 후속이 예고됐다(*"forecasts rather than measured performance"* 라고 저자가 한정).
- **대체 관계**: [[TabPFN]] · [[tabfm-1.0.0]](본문 비교 대상 TabFM으로 추정 — 인용 *"Kong & Das, 2026"*, 동일 모델 여부 미확인) · AutoGluon · XGBoost/LightGBM 튜닝 파이프라인. 결측치 보간 도구(MICE 등)도 겨냥.
- **허와 실**: 예측 성능 우위는 **점추정상 일관적**이고 improvability·승수에서 더 선명하다. 그러나 "압도"는 아니다(CI 겹침). 인과 주장은 **골격 복원**까지이며 재현 경로 미공개.
- **액션**: [[금융-AI]] 류 표 데이터로 LimiX-2 vs LightGBM vs TabPFN 3자 비교(비상업 PoC). 우선순위 낮음~중간.

## 수집기 대조

- ✅ 일치: 업보트 261 · 공개 2026-09-15 · githubRepo `limix-ldm-ai/LimiX` · githubStars 4,211(HF 필드값) · 저자 60명 · org Stable AI · `p(y|x,D)` → `p(x,y|D)` · SCM 합성 데이터 전용 사전학습 · 평가 3벤치 · 초록 수치 0개 · 초록 비교 대상 모델명 0개 · "골격까지" 한정 보존 · 기업 보고서형 분류
- ⚠️ 보강: 초록 수치 0 → **본문에 Elo·CI·improvability·스케일링·인과 표 전부 있음**(위). 초록의 "dataset-specific models and tabular foundation models"의 실제 명단은 본문 §5.1에 **18종**(트리 4 · AutoGluon 1 · 신경망 5 · 파운데이션 8).
- ⚠️ 주의 추가: "Stable AI"는 Stability AI가 아니다(LICENSE 원문 법인명).
- 미확인: *"7일 누적 창 1위(미수집 기준)"* — 볼트가 7일 창 전체 순위를 재구성하지 않았다.
- 📌 레포 URL 표기 불일치(무해): 논문·README는 `github.com/limix-ldm/LimiX`, HF `githubRepo` 는 `limix-ldm-ai/LimiX` — GitHub API상 전자가 **301 리다이렉트로 같은 저장소(id 1045442783)** 다. HF 링크 표기도 `stableai-org` 와 `stable-ai` 가 섞여 있다.

> [!action] 당장 할 것
> 1. **(낮음~중간)** 비상업 PoC: 결측치가 있는 표 1건으로 LimiX-2(imputation+cls) vs LightGBM(자체 결측 처리) 비교 — CMN 설계의 실익이 가장 크게 드러날 조건.
> 2. **(낮음)** LimiX 레포에서 **어텐션 기반 골격 추출 코드**가 공개됐는지 확인 → 없으면 표 7은 "재현 불가 결과"로 볼트 표기 유지.

> [!question] 미해결 질문
> - TALENT에서 **10클래스 초과 12개를 왜 뺐나** — LimiX-2의 제약인가, 비교 대상(TabFM·TabPFN)의 제약인가?
> - **추론 비용**: 406M 셀 단위 표현(행이 아니라 **셀마다** 벡터)은 행×열에 비례해 메모리가 늘어날 텐데 상한이 어디인가? 본문 0건.
> - 인과 골격 **임계값**(*"determined by a threshold over the overall score distribution"*)을 어떻게 정했나 — 정답 그래프 없이 정할 수 있는 규칙인가?
> - TabArena 공식 리더보드에 LimiX-2가 **제3자 제출로 등재**됐는가?

## 관련 페이지
- [[TabPFN]] — PFN 계보, `p(y|x,D)` 패러다임의 원형
- [[tabfm-1.0.0]] — 비교 대상(추정 동일), 같은 비상업 라이선스·10클래스 선
- [[분포내-우위]] — BCCO 자사 벤치 · SCM 사전분포 vs bnlearn 평가 데이터
- [[한정어-탈락]] — 골격 → 인과 추론
- [[표-부분인용]] — 이 페이지는 표 7(F1·SHD)·표 8을 전체 전사. 표 2·5·6은 LimiX-2·차점 행만 인용했음을 명시(전체는 원문)
- [[자기제한-명시]] — CI 공개(+) / Limitations 절 부재(−)
- [[측정도구-먼저-반증]]
- [[금융-AI]]
- [[Stable-AI]] *(신설 제안)*
- [[ai-news]]

## 원본
- 출처: https://huggingface.co/papers/2609.17488 · 본문 https://arxiv.org/html/2609.17488 (전문 열람)
- 측정: HF papers API `upvotes` 261 · `authors` 60 · `organization.fullname` "Stable AI" · `githubStars` 4,211 · `publishedAt` 2026-09-15 / GitHub API `stargazers_count` 4,214 · `forks_count` 304 · `open_issues_count` 8 · `license` other / HF model `stable-ai/LimiX-2` `downloads` 348 · `likes` 41 · `createdAt` 2026-09-15 (전부 2026-09-19)
- 가중치·라이선스: https://huggingface.co/stable-ai/LimiX-2 (README·LICENSE 원문)
- 신뢰도: ⭐⭐⭐ (업보트 261 · 전문·CI 공개 · 자사 벤치 포함 · 비상업)
