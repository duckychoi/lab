---
title: "PhysBrain 1.5 — 28벤치 절반을 이겼다. 그리고 1.0이 쟀던 로봇 제어 벤치는 사라졌다"
type: source
domain: slam-3dgs
tags: [slam-3dgs, ai-news, hf-paper, embodied, vla, vlm, world-model, action-tokenizer, deepcybo, qwen3-vl]
created: 2026-09-19
updated: 2026-09-19
sources: [PhysBrain.md, ActionPiece.md]
reliability: medium
---

# PhysBrain 1.5 (arXiv 2609.14973)

> [!insight] 핵심 인사이트 — **"이해·행동·예측을 하나의 토큰열로"라는 제목의 세 능력 중 정량 평가된 것은 하나(이해)뿐이다**
> 언어 응답 · 엔드이펙터 궤적(**[[ActionPiece]] 토크나이저**, 512 어휘) · 미래 RGB/깊이/로봇마스크(VQ-VAE 16,384 어휘)를 **Qwen3-VL-8B 어휘에 추가**해 다음토큰예측 하나로 학습한다.
> - **이해**: 28벤치 표 1개(아래 전량) — 정량 ✅
> - **행동**: 이미지평면·3D 궤적 **그림** + 부록 B.3 **액션 토큰 퍼플렉시티**(ID 17.12→5.07 · OOD RoboDojo 12.39→6.57) — 🔴 **폐루프 실행·과제 성공률 0건.** 저자 원문: *"The evidence concerns **offline trajectory prediction** conditioned on observed action history, **rather than closed-loop execution or full-task success**."*
> - **예측**: 1초 앞 RGB/깊이/마스크 **예시 그림만** — 🔴 정량 0건.
> 🎯 **그리고 전작과 비교하면 후퇴가 보인다**: PhysBrain 1.0(2605.15298)은 초록에서 **SimplerEnv-WidowX · LIBERO · RoboCasa** 제어 벤치 결과를 보고했다. **1.5는 LIBERO·RoboCasa·VLA-Arena를 SFT 학습 데이터로 쓰면서 평가표에서는 뺐다.** "VLM → 물리 파운데이션 모델"로 범위를 넓힌 버전이 **제어 성능은 재지 않았다.**

> [!insight] 🎯 28벤치 전량 — **이긴 14개와 진 14개를 모두 옮긴다** (표 4, 0~100, 오픈소스 8종 대비 순위)
> **오픈소스 1위 14개**:
> ```
> 벤치              PB1.5   오픈 차점(모델)        폐쇄 최고(모델)
> BLINK             87.9    86.1 (Hy-Emb-VLM)      89.2 (Gemini 3.6F)
> CV-Bench          90.0    89.4 (MiMo)            90.0 (Gemini 3.6F)
> 3DSRBench         63.0    62.1 (Hy-Emb-VLM)      67.7 (Gemini 3.6F)
> Q-Spatial-Bench   81.2    76.2 (Hy-Emb/RoboB)    87.1 (Gemini 3.6F)
> RoboSpatial-Home  73.9    72.0 (Emb-R1.5)        73.7 (GPT-6 Astra)
> ViewSpatial       62.5    56.4 (RynnBrain1.1)    56.6 (Gemini 3.6F)
> COSMOS            72.8    67.5 (Emb-R1.5)        75.7 (GPT-6 Astra)
> EgoPlan-Bench2    62.1    53.1 (Emb-R1.5)        69.3 (GPT-6 Astra)
> ERQA-PLUS         85.2    83.6 (RynnBrain1.1)    92.2 (Gemini 3.6F)
> RoboVQA           61.5    60.9 (RynnBrain1.1)    41.7 (Gemini 3.6F)
> VLABench          76.4    50.9 (Hy-Emb-VLM)      66.3 (GPT-6 Astra)
> Part-Affordance   84.0    83.4 (Emb-R1.5)        78.1 (Opus 5)
> PIOBench          68.3    64.8 (RynnBrain1.1)    80.9 (Gemini 3.6F)
> RoboRefit         89.6    86.2 (Cosmos3 Nano)    85.9 (Gemini 3.6F)
> ```
> **오픈소스 1위가 아닌 14개** (🔴 수집기 지적 — 이게 나머지 절반이다):
> ```
> 벤치              PB1.5   오픈 1위(모델)          PB 오픈순위  폐쇄 최고
> EmbSpatial        81.8    82.1 (Cosmos3 Nano)       3위       84.7
> MindCube          86.2    94.2 (ACE-Brain-0.5)      2위       78.8
> MMSI-Bench        41.0    46.0 (RynnBrain1.1)       2위       57.9
> SAT               79.3    81.3 (Hy-Emb-VLM)         2위       96.7
> VSI-Bench         61.9    65.9 (RynnBrain1.1)       2위       59.8
> ERQA              52.8    56.3 (Hy-Emb-VLM)         2위       75.8
> PixMo-Points      62.2    65.6 (ACE-Brain-0.5)      3위       75.2
> PointBench        64.3    64.5 (Emb-R1.5)           2위       71.9
> RefSpatial-Bench  50.9    63.2 (RynnBrain1.1)       6위       78.0
> RoboAfford        80.4    81.1 (Cosmos3 Nano)       2위       84.6
> VABench-Point     65.2    75.7 (Emb-R1.5)           2위       65.3
> Where2Place       72.1    75.0 (Emb-R1.5)           4위       76.9
> ShareRobot-Traj.  84.9    85.2 (RoboBrain2.5)       2위       83.1
> VABench-V.-Trace  89.8    92.3 (Emb-R1.5)           2위       91.6
> ```
> 🎯 **패배가 몰린 곳**: *공간 접지·포인팅·어포던스* 9개 중 **6개 패배**, *시각 궤적 추론* 2개 **전패**. 즉 **"행동"에 가장 가까운 이해 범주에서 약하다** — 이 모델이 액션 토큰을 내는 모델이라는 점을 생각하면 역설적이다. 🔴 **RefSpatial-Bench는 오픈 6위**(50.9 vs 63.2)로 표 전체 최악.
> 📌 평균(Overall): Gemini 3.6 Flash 73.0 · GPT-6 Astra 73.3 · Claude Opus 5 67.9 · Hy-Embodied-VLM-1.0 66.0 · Embodied-R1.5 64.9 · RynnBrain1.1 63.1 · Cosmos3 Nano 62.3 · Qwen3-VL-8B 59.5 · ACE-Brain-0.5 59.0 · RoboBrain2.5 58.2 · MiMo Embodied 57.4 · **PhysBrain 1.5 72.5**. 오픈 2위 이내 **24개** · 베이스 Qwen3-VL-8B 대비 **28/28 전부 우위** — ✅ 볼트 재계산 일치.

> [!warning] 🔴 "on par with GPT-6-Astra"를 읽기 전에 알아야 할 조건 3개
> 1. **폐쇄 모델은 가장 낮은 추론 설정으로 쟀다** — *"minimal thinking for Gemini, low thinking for GPT, and adaptive thinking with low effort for Claude"*. 오픈 경쟁 모델 중 Hy-Embodied·MiMo는 thinking을 켰다.
> 2. **모든 비교 모델을 DeepCybo가 자체 재평가했다** — *"we independently re-evaluate all comparison models using a single canonical metric … some scores in our table may differ from those reported in the original papers."* 평가 도구는 자사 `PhysBrainEvalKit`.
> 3. **표현이 채널마다 다르다** — 초록 *"on par with"* · 본문 *"approaches"* · 결론 *"approaching"*. 수치로는 72.5 vs 73.0/73.3 = **−0.5 / −0.8점**. → 볼트는 **"근접"** 으로 적는다 → [[한정어-탈락]]

> [!warning] 🔴 SFT 데이터에 평가 벤치의 **학습 분할·동일 출처**가 다수 들어 있다 (표 2·3, 볼트 이름 대조)
> SAT-Train · VSI-Train-10K/VSI-590K · MindCube-Train · EgoPlan-IT · RoboVQA-Train · VLABench · RoboRefIt-Train · PixMo-Points · RefSpatial-Train · RoboPoint(Where2Place 출처) · RoboSpatial-Train · RoboAfford-Train · ShareRobot — **28개 중 13개 벤치**가 학습 데이터 목록에 대응 항목이 있다.
> 🎯 **이건 오염(test leak)이 아니라 분포 내 학습이다** — 이름이 `-Train` 인 공식 학습 분할이다. 🔴 그러나 **최대 격차 벤치 VLABench(+25.5, 76.4 vs 50.9)가 SFT 데이터에 VLABench를 직접 넣은 경우**다 → [[분포내-우위]].
> ✅ 반대 증거도 있다: 13개 중 **8개(SAT·VSI·MindCube·PixMo·RefSpatial·Where2Place·RoboAfford·ShareRobot)는 오히려 졌다.** 학습 분할을 넣었다고 이기지는 않았다. 🔴 **경쟁 모델들이 같은 분할을 썼는지는 볼트가 확인하지 않았다** — 공정성 판정 보류.

## 🔀 전작·동조직 대비 — 무엇이 바뀌었나

| 항목 | PhysBrain 1.0 (2605.15298) | PhysBrain 1.5 (2609.14973) |
|---|---|---|
| 공개 | 2026-05-14 · 저자 13 · 업보트 61(09-19 실측) | 2026-09-14 · 저자 54(53명+"DeepCybo Team") · 업보트 166 |
| 핵심 | 1인칭 사람 영상 → **물리 상식 QA 감독** → VLA 정책으로 이전 | 언어·**액션 토큰**·**미래 시각 토큰**을 **하나의 자기회귀 어휘**로 통합 |
| 출력 | 언어(VLM) + 별도 VLA 정책 | 언어 + 16스텝 손목 궤적(32토큰) + 1초 미래 RGB/깊이/마스크 |
| 평가 | ERQA · PhysBench · **SimplerEnv-WidowX · LIBERO · RoboCasa**(제어) | 28 이해 벤치 + 12 일반 벤치 · **제어 벤치 0** |
| 코드 | `Phys-Brain/PhysBrain-VLA` ★42 | `DeepCybo-PhysAI/PhysBrain-1.5` ★44 — **파일 5개(README·PDF·로고)**, 코드 없음 |
| 가중치 | — (볼트 미확인) | HF `PhysBrain1.5-8B`(DL 357 · ♥25) · `-2B`(DL 209 · ♥13) |

- 🎯 **[[ActionPiece]] 와의 관계가 확정됐다**: 1.5가 ActionPiece 토크나이저를 **2,870만 개 16스텝 궤적 세그먼트(4.592억 타임스텝)** 로 학습해 액션 어휘로 쓴다. HF 컬렉션 `DeepCybo/physbrain-15` 에 두 논문이 함께 묶여 있다. → ActionPiece의 LIBERO 94.8%는 **토크나이저 단독 정책 실험**이고, **1.5 본체의 제어 성능은 아니다.** 둘을 합쳐 "PhysBrain 1.5가 LIBERO 94.8%"로 읽으면 안 된다.
- 🔴 **볼트 [[PhysBrain]] 페이지 정정 필요**: 그 페이지는 1.0을 *"물리 법칙 추론(역학·열역학·광학 등) 특화 멀티모달 모델"* 로 적었으나, **1.0 초록(HF API 09-19 실측)은 역학·열역학·광학을 한 번도 언급하지 않는다** — 실제 내용은 *"converting large-scale human egocentric video into structured physical commonsense supervision"* 과 VLA 이전이다. **로봇/임바디드 모델을 "과학 계산 AI"로 잘못 분류했다.**
- 📌 소속: README 로고 대체텍스트 *"DeepCybo · Zhongguancun Academy · Zhongguancun Institute of Artificial Intelligence"* — 볼트 [[PhysBrain]] 페이지의 "신생 기관" 서술에 **중관촌 연구원 계열**이라는 정보가 추가된다(🔴 조직 관계의 세부는 미확인).

## 일반 멀티모달 — "retaining"의 실제 (표 5·6, 베이스 대비 전량)
```
          MME      MMStar  RealWorldQA VideoMME MVBench POPE  AI2D  ChartQA DocVQA TextVQA V*    ScreenSpot
Qwen3-VL  2392.70  64.99   68.37       69.07    68.53   88.40 83.74 84.96   95.66  81.94   83.77 91.59
PB 1.5    2330.07  65.60   69.41       68.22    66.07   89.49 82.16 86.24   94.43  81.58   87.96 90.17
```
🔴 **12개 중 7개 하락**(MME −62.63 · MVBench −2.46 · AI2D −1.58 · ScreenSpot −1.42 · DocVQA −1.23 · VideoMME −0.85 · TextVQA −0.36), 5개 상승(V* +4.19 최대). 저자 표현 *"comparable to that of the base model"* 는 **틀리진 않지만 "유지"보다는 "소폭 손실 동반"** 이다 → [[에이전트축-분기]] 의 임바디드 판본(특화 이득 ↔ 범용 비용).

## 도메인별 추출 (slam-3dgs)
🔀 **도메인 재판정: 수집기 `ai-news` → 볼트 `slam-3dgs`** — 선례 [[ActionPiece]](같은 조직, 같은 기준으로 재판정). 평가 대상이 공간 추론·포인팅·궤적이고 [[임바디드-AI]] 누적선이 이 도메인에 있다.
- **현재 SOTA**: 오픈 임바디드 VLM 중 28벤치 평균 1위(72.5, **자체 재평가 기준**). 🔴 전역 SOTA 아님 — 폐쇄 2종보다 낮고, 포인팅·궤적 범주는 [[HY-Embodied]]·Embodied-R1.5·RynnBrain이 앞선다.
- **실시간 가능성**: 🔴 **지연시간·제어 주파수 수치 0건.** 액션 1청크 = 32토큰, 미래 프레임 1장 = 770토큰(3모달 × 256 + 경계 2) — **미래 예측을 매 스텝 쓰면 실시간은 어렵다**(볼트 추정, 측정 없음).
- **카메라 파이프라인**: 입력 RGB(+이전 액션 청크 선택) → 출력 손목 궤적(카메라/로봇별 좌표계 **비정렬** — 저자: *"we do not impose a single globally canonicalized coordinate frame"*). 🔴 **체화체 간 좌표 정규화를 하지 않았다** — 궤적을 다른 로봇에 그대로 쓸 수 없다는 뜻.
- **응용 가능성**: 🔴 볼트 직접 응용 경로 없음(로봇 미보유). 🎯 **공간 VQA·포인팅 백본**으로는 8B·2B 가중치가 공개돼 바로 시험 가능 — 단 라이선스 필드가 비어 있다(HF `cardData.license` 없음, GitHub license None).
- **필수 레퍼런스**: [[ActionPiece]](액션 어휘) · 평가도구 `DeepCybo-PhysAI/PhysBrainEvalKit` · 비교축 [[HY-Embodied]].

> [!warning] 수집기 대조
> - ✅ 원문 대조 일치: 업보트 166 · githubStars 44 · 저자 54 · org DeepCybo · 28벤치 평균 72.5 · 오픈 최고 14개 · "on par"(초록 원문) · 사람 영상 전량 사전학습 · SFT 혼합 · ActionPiece 동조직(HF API `organization.name` DeepCybo 확인) · 볼트 기보유.
> - 🔴 정정: 수집기 *"궤적 생성·미래 장면 예측은 정량 평가 없음"* → **궤적은 부록 B.3에 오프라인 액션 토큰 퍼플렉시티 수치가 있다**(17.12→5.07 / OOD 12.39→6.57). 결론 방향(폐루프 성능 미측정)은 **유지** — 저자 본인이 그렇게 적었다.
> - 📌 보강: 저자 54 = 개인 53명 + `"DeepCybo Team"` 항목 1개. 본문 "on par"는 초록에만 있고 본문·결론은 "approaches".

> [!action] 당장 할 것
> 1. **[[PhysBrain]] 페이지 정정**(1.0 = 사람 1인칭 영상 → 물리 상식 → VLA, "물리 법칙/과학 계산" 아님) — 오케스트레이터 반영 대상
> 2. **ActionPiece ↔ PhysBrain 1.5 연결** 기록 — "토크나이저 정책 실험(LIBERO 94.8%)"과 "본체 제어 성능(미측정)"을 분리해 적는다
> 3. (낮음) 공간 VQA 필요 시 `PhysBrain1.5-2B` 로 RefSpatial·포인팅 약점 재현 확인 — 라이선스 먼저 확인

> [!question] 미해결 질문
> - 1.5 본체를 LIBERO·SimplerEnv에서 폐루프로 돌리면? 1.0보다 나은가? (제어 벤치를 SFT에만 쓰고 평가에서 뺀 이유가 본문에 없다)
> - 경쟁 오픈 모델들도 SAT-Train·VSI-Train·RoboRefIt-Train 등을 썼는가? 안 썼다면 13개 벤치의 비교는 분포 내 우위다
> - 폐쇄 모델을 기본/높은 추론 설정으로 재면 격차는?
> - 미래 예측 1초 horizon의 정량 오차(깊이 오차·마스크 IoU)는?

## 관련 페이지
- [[PhysBrain]] — 1.0 (🔴 정정 필요)
- [[ActionPiece]] — 액션 토크나이저(같은 조직, 같은 HF 컬렉션)
- [[HY-Embodied]] — 오픈 비교축 1위 경쟁자(Hy-Embodied-VLM-1.0 66.0)
- [[임바디드-AI]]
- [[월드모델]]
- [[분포내-우위]]
- [[표-부분인용]]
- [[한정어-탈락]]
- [[에이전트축-분기]]
- [[Alibaba]] — 베이스 Qwen3-VL-8B/2B-Instruct
- [[MiniMax-H3-Physical-Reasoning]] — 같은 배치, 물리세계 추론을 **생성 모델** 쪽에서 잰 제3자 평가

## 원본
- 출처: https://huggingface.co/papers/2609.14973 · 본문 https://arxiv.org/html/2609.14973
- 레포: https://github.com/DeepCybo-PhysAI/PhysBrain-1.5 · 가중치: https://huggingface.co/collections/DeepCybo/physbrain-15
- 볼트 실측(2026-09-19): HF papers API `upvotes` 166 · `githubStars` 44 · `authors` 54 · `organization.name` DeepCybo · `publishedAt` 2026-09-14 / GitHub API `stargazers_count` 44 · `forks_count` 0 · `open_issues_count` 1 · `created_at` 2026-09-08 · license None · 트리 5파일 / HF models API `DeepCybo/PhysBrain1.5-8B` `downloads` 357 · `likes` 25 · `cardData.base_model` Qwen/Qwen3-VL-8B-Instruct · `safetensors.total` 8,903,438,576 · `-2B` `downloads` 209 · `likes` 13 · base Qwen3-VL-2B-Instruct / 비교용 HF papers API 2605.15298(PhysBrain 1.0) `upvotes` 61 · `githubRepo` Phys-Brain/PhysBrain-VLA · `githubStars` 42 · 저자 13 / 2609.18487(ActionPiece) `upvotes` 39 · org DeepCybo / arXiv HTML 본문 전문 읽음(표 1~6, 부록 B.1·B.3; 한계 절 **없음**)
- 신뢰도: ⭐⭐ (가중치 공개 · 28벤치 전량 게시 · 🔴 비교 모델 전원 자체 재평가 · 폐쇄 모델 최저 추론 설정 · 제어/예측 정량 0 · 학습 분할 다수 포함 · 코드 레포에 코드 없음)
