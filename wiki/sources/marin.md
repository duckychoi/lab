---
title: "Marin — 실패를 산출물로 내는 오픈 개발 LLM 플랫폼. 회고 문서에 '우리가 망친 것' 목록이 수치와 함께 있다"
type: source
domain: ai-news
tags: [ai-news, github-trending, pretraining, open-development, scaling-law, moe, reproducibility, stanford-crfm, tpu, agent-skills]
created: 2026-09-19
updated: 2026-09-19
sources: []
reliability: high
---

# Marin (marin-community/marin)

> [!insight] 핵심 인사이트 — **이 프로젝트의 산출물은 모델보다 "변경 이력"이다. 그리고 그 이력이 결과 해석을 바꾼다**
> README의 가치 선언: *"Every step, from raw data to the final model, is recorded. **Failed experiments are part of that record.**"* — 볼트가 `docs/reports/` 의 8B·32B 회고를 열어 확인한 결과 **이건 수사가 아니다.** 32B 회고는 실험마다 **이슈 번호 + 커밋 고정 스크립트 경로**를 붙이고(#1295·#1390·#1380·#1395·#1529·#1681), **실패한 개입을 실패했다고** 적는다.
> 🎯 가장 값진 실패 기록 3개(32B):
> 1. **손실 스파이크 → 완화책 두 개 실패 → 아키텍처 교체**: grad-norm 클립을 1.0→0.2로 조임(56.4K step) · "update-norm 클립" 추가(72.2K) — *"didn't seem to prevent loss spikes"*. 결국 **Llama형 → Qwen3형(QK-Norm) 백본으로 80K step에서 교체**해 안정화. 교훈 원문: *"**Pride goeth before a fall.** … We should have tested QK-Norm earlier."*
> 2. **GSM8K 오염이 점수를 *올린* 게 아니라 *떨어뜨렸다***: 캐시된 Dolmino 수학 번들에 GSM8K `test.json` 이 섞였는데, Dolmino는 OLMES 포맷이라 LM Eval 기본 프롬프트의 `<<16-7=9>>` 태그에 대한 surprisal이 폭증 → **가장 약한 기준선보다 약 22점 낮게** 나왔다. 저자 표현: *"we (accidentally) cheated but we cheated badly."*
> 3. **셔플 버그**: 선형 합동(LCG) 기반 순열이 상관된 배치를 만들어 **데이터를 안 바꿨는데 학습 손실이 위상 이동** → Feistel 셔플로 교체.
> → 🔴 **2번은 볼트에 새로운 형태다**: 오염은 보통 "점수를 부풀린다"로만 의심하는데, **포맷이 다른 오염은 점수를 깎아 오염 자체를 가린다.** 저자도 *"our MATH performance was also quite poor, and we have no reason to believe it was contaminated"* 라고 원인 분리를 유보했다.

> [!warning] 🔴 README 한 문장의 범위 — "Llama 3.1 8B를 이겼다"는 **베이스 모델 · 19과제 · LM Eval Harness 기본값 · 오염 경고 동반**이다
> 수집기는 *"our base-model benchmark suite"* 한정어를 보존했다 ✅. 볼트가 회고 원문 표를 끝까지 읽은 결과 한정어가 **세 개 더** 있다:
> - **베이스 대 베이스**: Marin 8B Base(Deeper Starling) 평균 **66.6** vs Llama 3.1 Base **65.3** vs OLMo 2 Base 64.9 — 19과제 중 Llama 대비 **14승 2무 3패**(패: GPQA 30.3 vs 32.3 · OpenBookQA 44.2 vs 45.8 · WSC 82.1 vs 83.5). 저자 자평: *"We **can't claim any particular standout** performance on any one task … just a general improvement."*
> - **오염 경고를 저자가 먼저 건다**: *"all these results come with an asterisk … many of these tasks are highly contaminated"* (DCLM·Dolmino·Nemotron-CC, Llama 3도 동일).
> - **SFT 단계에선 못 이겼다**: Marin 8B SFT 평균 **43.8** vs Llama 3.1 **Tulu 50.0** — *"So we **still haven't surpassed** Llama 3.1 Tulu"*. (Llama 3.1 Instruct 39.8보다는 높음.) GSM8K-CoT는 68.9로 Llama 3.1 Instruct 82.6보다 낮다.
> 🎯 **README는 이긴 문장만 올렸고, 진 문장은 한 클릭 아래 회고에 있다.** 은폐가 아니라 링크를 걸어뒀다는 점에서 [[자기제한-명시]] 의 양성 사례이지만, **README만 읽는 수집기에겐 [[표-부분인용]] 이 구조적으로 발생한다.**

## 도메인별 추출 (ai-news)

- **신뢰도**: GitHub **★3,751** · 포크 300 · Apache-2.0 · 핵심 기여 **Stanford CRFM + Open Athena**(README 명시, 수집기 누락) · 후원 Google TPU Research Cloud(TPU) · **Jen-Hsun and Lori Huang Foundation(GPU 클러스터)** · Siegel Family Endowment · Schmidt Sciences. HF: `marin-8b-base` DL 3,558 / ♥17 · `marin-32b-base` DL 565 / ♥49 · `marin-8b-instruct` DL 478 / ♥32 · `marin-community` 조직 모델 **360개**(그중 id에 `delphi` 포함 **88개**). → reliability **high**(학술 기관 + 회고 문서 수준의 공개).
- **즉시 활용**: **NO (학습)** — TPU v4-2048 / v5p-512급 인프라 전제. 🎯 **YES (방법론)** — 회고 두 편은 **"대형 런을 도중에 고치는 법"의 실전 체크리스트**다: grad-norm 평상치(~0.2)보다 크면 스파이크 전조 · update-norm 스파이크가 grad-norm 스파이크보다 **먼저** 온다 · 깊은 쿨다운에서 z-loss가 필요 · 캐시된 데이터셋 내용 재검증.
- **6개월 영향력**: **중간.** 진행 중인 **5e24 FLOPs · 500B+ 파라미터 MoE**(README, **결과 아님**)가 나오면 "완전 공개(open source ≠ open weights)" 진영의 최대 규모가 된다. 🔴 그 전까지는 계획이다.
- **대체 관계**: [[Allen Institute for AI (AI2)]] OLMo 계열과 **같은 "완전 공개" 칸**의 경쟁자. 32B 회고는 스스로를 **"open source"**(가중치+코드+데이터)로, Qwen·Gemma 3·Nemotron Nano를 **"open weights"** 로 구분하는 용어 절을 따로 둔다.
- **허와 실**: ✅ **걷어낼 게 거의 없다** — 오히려 README가 회고보다 **덜** 말한다. 🔴 단 하나: 블로그 제목 *"Scaling Laws That Extrapolate **300×** Past the Fit"* 의 조건(아래 note).
- **액션**: 🎯 **32B 회고의 "Lessons Learned" 5줄과 8B의 "Main Takeaways" 6줄을 읽는다.** 코드 설치는 불필요.

### Marin 32B — 평균·순위·승수가 서로 다른 답을 준다 (회고 원문, LM Eval Harness 기본값, 19과제)
```
모델                          평균    평균순위(↓)   MRR(↑)   Mantis 대비 승수
Marin 32B (Mantis)            65.2    3.05 (1위)   0.44     —
NVIDIA Nemotron Nano 12B v2   68.6    3.68         0.38     Marin이 10/19 우위, 평균 −3.4
Qwen 2.5 32B Base             68.1    3.16         0.54(1위) Marin이 8/19 우위, 평균 −2.8
Gemma 3 27B PT                65.1    3.37         0.39     Marin이 9/19 우위, 평균 +0.1 ("more or less on par")
OLMo 2 32B Base               63.2    3.89         0.34     Marin이 14/19 우위, 평균 +2.0
Marin 32B (Bison, 오염본)     63.0    3.68         0.39
```
🎯 **"Marin 32B가 1등인가?"의 답이 지표마다 다르다** — 평균순위 1위 · MRR은 Qwen 2.5가 1위 · 평균 점수는 Nemotron Nano 12B·Qwen 2.5에 뒤진다. **저자가 이 셋을 전부 게시했다.** 🔴 저자 캐비엇: 19과제는 *"out of many possible tasks"* · **영어 텍스트 과제만** · 베이스 모델(명령 튜닝·RLHF 없음, *"This is planned"*) · 롱컨텍스트 미확장. 총 학습 토큰 ≈ **6.437T**(폐기된 Bison 쿨다운·진단 재시작 제외).

> [!note] 📌 Delphi "300×"의 조건 — 볼트가 블로그 원문 대조 (openathena.ai/blog/delphi, 2026-05-11)
> - 적합: **3e18 ~ 3e20 FLOPs** 의 IsoFLOP 최적점 7개 → 예측 대상: **1e23 FLOPs (25B 파라미터 · 600B 토큰)** 런 = 약 **333배** 외삽.
> - 결과: *"A **pre-registered** forecast … predicted the final **loss** … within **0.2%**"* · 1e21·1e22 홀드아웃은 **0.5%** 이내(시드 3개씩).
> - 🔴 한정어 ①: 맞춘 것은 **손실(loss)** 이지 벤치마크 점수가 아니다(벤치는 별도 2단 회귀). ② 부트스트랩 95% 신뢰구간은 1e23에서 **±4%** 로 넓다 — **0.2% 적중은 넓은 구간 안의 한 점**이다. ③ 🎯 **첫 시도는 실패했다고 적었다**: *"diverged when extrapolated 30× past them"* — 1e22 홀드아웃이 **2.5% 빗나가고 1e23 런은 발산**. 레시피(토큰 호라이즌 보정 + 가중감쇠 제거 옵티마이저)를 고친 **두 번째 시도**가 300×다.
> - 📌 **"사전등록(pre-registered)"** 이라는 단어가 볼트에서 드물다 — 예측을 먼저 박아두고 런을 돌렸다는 뜻. [[측정도구-먼저-반증]] 의 정신을 저자 측이 실행한 사례.

> [!note] 📌 이슈 = 실험 장부 — 수집기 주장 **원문으로 입증**
> `open_issues_count` **597**(수집기 595, 조회 시차) = **열린 이슈 500 + 열린 PR 97**(search API). 🎯 회고 문서가 실험을 **이슈 번호로 인용**한다(8B: #600 · 오염 추적 #1321 · 데이터 혼합 #702 / 32B: #1295·#1368·#1390·#1380·#1395·#1529·#1681). **이 레포에서 open_issues 비율(15.86%)은 결함 적체가 아니라 실험 개수에 가깝다** — 수집기 판정 ✅ 동의. → [[측정도구-먼저-반증]]: 같은 필드가 레포 문화에 따라 다른 것을 잰다.

> [!note] 📌 방법론을 **에이전트 스킬**로 배포한다
> Delphi 산출물 목록에 *"Development methodology as the `add_scaling_heuristic` **agent skill**"* 이 들어 있고, README는 기여자에게 `.agents/skills/`(= `.claude/skills/`) 를 안내한다(예: `add-dataset`). 🎯 **연구 절차 자체를 에이전트가 불러 쓰는 스킬 파일로 공개한 것은 볼트 최초 관측(추정 — 전수 검색은 안 함).** → [[에이전트-스킬]] 의 "스킬의 생산 방식" 축에 **"연구 방법론 패키징"** 사례.

> [!action] 당장 할 것
> **32B 회고의 GSM8K 오염 절(§Contamination anomaly)을 [[한정어-탈락]] 옆에 "역방향 오염" 사례로 기록할지 판단한다** — 볼트의 벤치 판정 규칙은 "오염 → 부풀림"만 가정한다. **포맷 불일치 오염은 점수를 깎고, 그래서 오염 탐지 신호(비정상적 고점)가 나오지 않는다.** 검증 체크리스트에 "비정상적 **저점** + 프롬프트 취약성"도 오염 신호로 넣을지 결정.

> [!question] 미해결 질문
> - 진행 중인 5e24 FLOPs MoE의 **예정 공개 시점·중간 결과**는? README는 목표만 적었다(이슈 추적 번호 미확인).
> - Delphi 곡선이 *"Marin 32B, Kimi K2.5, DeepSeek V4, GPT-4, Opus, GPT-5"* 를 외삽선 위에 올려놓는데, **닫힌 모델의 컴퓨트는 Epoch AI 추정치**다 — 이 그림을 인용할 땐 "추정치 위의 외삽"임을 붙여야 한다.
> - 8B 회고의 SFT 표에서 **MMLU 등 베이스 과제가 SFT 후 하락**했다(저자 인정). 개선판 체크포인트가 나왔는가? (미확인)

## 관련 페이지
- [[Allen Institute for AI (AI2)]]
- [[NVIDIA]]
- [[Alibaba]]
- [[Google]]
- [[에이전트-스킬]]
- [[측정도구-먼저-반증]]
- [[자기제한-명시]]
- [[표-부분인용]]
- [[한정어-탈락]]
- [[Stanford-CRFM]] *(신설 제안)*
- [[포맷-불일치-오염]] *(신설 제안)*

## 원본
- 출처: https://github.com/marin-community/marin · 회고 `docs/reports/marin-8b-retro.md`(701행) · `docs/reports/marin-32b-retro.md`(536행) · 블로그 https://openathena.ai/blog/delphi/
- 볼트 실측(2026-09-19, GitHub API): `stargazers_count` **3,751** ✅ · `forks_count` 300 · `open_issues_count` **597**(수집기 595) = 이슈 500 + PR 97 · `created_at` 2024-03-22 ✅ · `pushed_at` 2026-09-19 · `license` Apache-2.0 ✅ · 트렌딩 Python 데일리 `17 stars today` ✅
- 볼트 실측(2026-09-19, HF models API): marin-8b-base `downloads` 3,558 · `likes` 17 / marin-32b-base 565 · 49 / marin-8b-instruct 478 · 32 / 조직 모델 수 360(delphi 88)
- 수집기 대조: README 169행 ✅ · 5e24 FLOPs · 500B+ MoE(진행 중) ✅ · Delphi 3e18→1e23 ✅ · Pythia 영향 ✅ · Nemotron-CC·StarCoderData·ProofPile 2 ✅ · `wandb_url` 전 행 ✅ · 300× ✅(조건 보강) · 32B-A5B(1e22) ✅ · "our base-model benchmark suite" 한정어 ✅ · 이슈 #1337 ✅ · 🔴 open_issues 595 → 597(시차)
- 볼트 추가: 회고 2편 열람 — 8B 19과제 14승2무3패 · SFT에서 Tulu에 패 · 32B 평균/순위/MRR 3지표 불일치 · 역방향 GSM8K 오염 · QK-Norm 교체 · Delphi 첫 시도 실패와 CI ±4% · Stanford CRFM/Open Athena · 후원처 · 방법론 스킬 배포
- 신뢰도: ⭐⭐⭐ (학술기관 · 회고 문서가 실패·오염·패배를 수치로 게시 · 🔴 벤치 전부 LM Eval 기본값·영어 한정 · 현재 MoE는 미완)
