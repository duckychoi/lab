---
title: Raw — 인제스트 대기열
updated: 2026-09-17 (09-17 자동수집 **13건 추가** — 대기 13건 / GitHub 5 · HF논문 5 · HF모델 3 · 중복 0)
---

# Raw 대기열

인제스트할 소스를 여기에 추가한다.
LLM이 처리(ingest) 완료하면 해당 항목을 즉시 삭제한다.

형식:
```
## 소스 제목
- type: url | text | file
- url: https://...
- 메모: (선택사항)
```

---

## 대기 중: **13건**

**2026-09-17 자동수집 13건.** GitHub 5 · HF논문 5 · HF모델 3.
**파이프라인(09-15 채택 순서 유지)**: 트렌딩 5페이지 병합 슬레이트 **91건**(daily 21 · weekly 22 · python 18 · jupyter-weekly 19 · **jupyter-daily 20 = 단위 통일용 확장분**) → **슬레이트 전체에 중복 필터 1회** → NEW풀 확정 → 쿼터를 NEW풀 상위에서만 충족. **백필 0.**
🔴 **확장분 재적용 이행**: jupyter 페이지를 weekly로 먼저 받았다가 **단위 불일치**를 발견해 daily로 재수집했다. 이는 슬레이트 확장이므로 [[백필-우회]] 성립 조건에 따라 **확장 20건에도 중복 필터를 다시 돌렸다**(DUP 2 · NEW 18).
**NEW풀 ≥ 쿼터 충족**: GitHub AI/ML **8 ≥ 5** · 논문 **17 ≥ 5**(arXiv ID grep 전건 0히트) · HF모델 **15 ≥ 3**.

---

## [2026-09-17] 자동수집 | cloudflare/security-audit-skill
- URL: https://github.com/cloudflare/security-audit-skill
- 도메인: ai-news
- 스타수: 8,506 (당일 +927 = **상대속도 10.90%** 🚀 급상승 / 트렌딩 daily 2위 / fork 472 / MIT / 2026-06-18 생성)
- 한줄요약: 코딩 에이전트를 6단계(정찰→커버리지 기반 헌팅→후보 검증→구조화 출력→독립 재검증→보고)로 몰아넣는 **스킬 파일 묶음**이며, 모델이 아니라 `SKILL.md` + 14개 공격분류 문서 + **의존성 0인 JS 검증기 2개**(`validate-findings.cjs`·`validate-coverage-ledger.cjs`)로 되어 있다.
  - 🎯 **실제 능력의 핵심은 "판정 3분류를 스키마로 강제"하는 것**이다 — README 본문: *"`confirmed` has a complete source trace and bounded observed result, `needs_validation` has an exact unresolved fact and **no severity**, and `rejected` records a disproved candidate"*. **심각도를 붙일 수 없는 칸을 따로 만든 게 설계의 중심**이다.
  - 실용성: **재실행이 가산적(additive)** 이라고 본문이 명시한다 — 이전 ledger/findings를 읽어 빈 구멍만 겨냥한다. 다만 **탐지율 수치가 README에 없다** — Cloudflare 블로그(`build-your-own-vulnerability-harness`)로 연결만 되어 있고 레포 자체에 벤치가 없다. 🔴 **확인 불가**.
  - 🏗️ 판정: **AI 네이티브** — AI를 빼면 남는 게 마크다운 문서뿐이다.

## [2026-09-17] 자동수집 | TencentCloud/Octop
- URL: https://github.com/TencentCloud/Octop
- 도메인: ai-news
- 스타수: 3,141 (당일 +396 = **상대속도 12.61%** 🚀 **슬레이트 최고 상대속도** / 트렌딩 python-daily 6위 / fork 334 / MIT / 2026-07-08 생성)
- 한줄요약: 자체 호스팅 멀티에이전트 AI 어시스턴트로, 대화 채널(웹·Feishu·DingTalk·QQ·Discord·WeCom·HTTP/SSE/WebSocket)과 실행 백엔드(로컬 디스크·Docker·PostgreSQL·COS/S3)를 **양쪽 다 교체 가능하게** 묶은 것이 실제 구조다.
  - 실측 기능(README 표): JWT 멀티유저 격리 · 도구 승인 게이트 · 셸 가드레일 · PII 마스킹 · RAG 지식베이스 · `octop acp` 로 OpenCode/Claude Code에 **권한 게이트 걸어 위임** · 헤드리스 Chromium · 원격 데스크톱(Linux/Win/macOS).
  - 🔴 **마케팅 문구 제외분**: 본문의 *"디지털 생명체(digital life form)"* · MBTI 16종 페르소나는 **능력 주장이 아니라 프롬프트 템플릿**이다. 벤치마크·평가 수치는 README에 **없다**.
  - 🏗️ 판정: **AI 네이티브**. 단 v1.0.0 · 생성 2개월 · ♥ 대비 검증 이력 없음 — **상대속도 1위지만 채택 근거는 신규성뿐**이다.

## [2026-09-17] 자동수집 | cline/cline
- URL: https://github.com/cline/cline
- 도메인: ai-news
- 스타수: 68,507 (당일 +112 = **상대속도 0.16% → 기저 유입, "급상승"이라 쓰지 않는다** / 트렌딩 daily 20위 / fork 7,401 / Apache-2.0 / 2024-07-06 생성)
- 한줄요약: IDE 확장에서 시작한 자율 코딩 에이전트가 **SDK · CLI · 데스크톱**으로 배포면을 넓힌 것이며, README가 내세우는 신규 능력은 *"Interactive chat or fully headless for CI/CD and scripting"* — 즉 **헤드리스 실행으로 CI에 꽂는 경로**다.
  - 🏗️ **상시 인프라 (신규 릴리스 아님)** — 2년차 · ★68.5k. 당일 +112는 자기 크기의 0.16%로, [[상대속도-가림]] 기준 **기저 유입**이다. 같은 목록의 Octop(12.61%)과 **77배 차이**다.
  - 실용성: 볼트에 [[anthropic-claude-code]]·[[openai-codex]] 가 이미 있으므로 **경쟁 축 비교용 바닥 페이지**로서 값이 있다. 능력 수치(SWE-bench 등)는 README **상단 48행에 없음** — 별도 문서(docs.cline.bot) 확인 필요.

## [2026-09-17] 자동수집 | rlaope/oh-my-hermes
- URL: https://github.com/rlaope/oh-my-hermes
- 도메인: ai-news
- 스타수: 2,653 (당일 +80 = **상대속도 3.02%** 🚀 급상승 / 트렌딩 daily 15위·python-daily 3위 / fork 189 / MIT / 2026-06-03 생성)
- 한줄요약: NousResearch의 **Hermes Agent 위에 얹는 운영 계층**으로, Hermes를 대체하지 않고 *"frames the problem, picks the workflow and evidence gates, and runs native skills as capabilities inside that governed path"* — 즉 **스킬 실행 전에 증거 게이트를 세우는 래퍼**다.
  - 🎯 배달 가치: 볼트에 이미 [[agent-skills]]·[[ECC]]·[[superpowers]] 같은 **하네스 계층** 페이지가 있는데, 이건 **Claude Code가 아닌 Hermes 계열**이다 — 같은 패턴의 다른 생태계 표본.
  - 🔴 **자기 한계**: *"explicit evidence boundaries"* · *"honest record of what actually happened"* 가 실제로 무엇을 강제하는지는 **README 상단 48행에 정의가 없다**(docs/README.md 별도 확인 필요). **주장만 확인, 구현 미확인.**

## [2026-09-17] 자동수집 | wshobson/agents
- URL: https://github.com/wshobson/agents
- 도메인: ai-news
- 스타수: 39,748 (당일 +41 = **상대속도 0.10% → 기저 유입, "급상승" 아님** / 트렌딩 python-daily 16위 / fork 4,235 / MIT / 2025-07-24 생성)
- 한줄요약: **94 플러그인 / 202 에이전트 / 183 스킬 / 105 커맨드**를 단일 마크다운 소스(`plugins/`)에 두고 **6개 하네스**(Claude Code·Codex·Cursor·OpenCode·Antigravity·Copilot·Pi)로 변환 배포하는 마켓플레이스다.
  - 🎯 **실제 능력은 개수가 아니라 변환 방식**이다 — README 본문: *"Each harness gets idiomatic, harness-native artifacts — **not lowest-common-denominator translations**"*. 하네스별 능력차는 `docs/harnesses.md` 매트릭스로 노출한다.
  - 🏗️ **상시 인프라** — 1년 2개월차 ★39.7k, 상대속도 0.10%. **당일 증가량 기준 5위이지만 절대값(+41)은 1위(+927)의 4.4%** 다. → [[상대속도-가림]] 재확인 표본.
  - 실용성: 설치 경로가 하네스마다 다르다(native registry / clone+generate). **Antigravity·OpenCode·Pi는 생성 트리가 gitignore** 되어 있어 clone 후 `make generate` 필수.

---

## [2026-09-17] 자동수집 | ScienceIDE: Turning World's Scientific Codebase into Agent Learnable Environments
- URL: https://huggingface.co/papers/2609.19134
- 도메인: ai-news
- 업보트: 63 (HF 데일리 1위 / 2026-09-16 게재)
- 한줄요약: 과학 코드 레포를 **에이전트가 학습할 수 있는 실행 환경으로 변환**하는 인프라이며, 전문가가 정의한 과학 케이스와 **합격 기준(acceptance criteria)** 을 기준으로 레포를 태스크 생성·실행·검증이 되는 환경으로 바꾼다. 이 환경의 검증된 상호작용 궤적으로 **PhAI-IDE-72B / 9B / 4B** 를 학습시켰다.
  - 문제 정의(초록 원문): *"fragmented toolchains, implicit domain conventions, and specialized correctness criteria"* → 저자들은 이를 **`scientific experience bottleneck`** 이라 명명했다.
  - 🔴 **한정어 병기**: 성능 주장은 *"gains in held-out scientific-code repair and **across selected general-purpose benchmarks**"* 이며 **"selected"** 가 붙어 있다. 초록에 **구체 수치가 없다** — 전이(positive transfer)를 *"providing evidence of"* 수준으로만 주장한다.
  - 코드: https://github.com/aitofound/ScienceIDE (초록에 명시)

## [2026-09-17] 자동수집 | Confidence Comes from Experience: Experiential Confidence Estimation from Reasoning to Agents
- URL: https://huggingface.co/papers/2609.17708
- 도메인: ai-news
- 업보트: 44 (HF 데일리 2위 / 2026-09-15 게재 / **수집 중 드리프트: 페이지 43 → API 44**)
- 한줄요약: 신뢰도 추정을 **현재 추론 과정이 아니라 모델의 과거 채점 이력에서** 끌어오는 방법(**XConf**)으로, 과거 에피소드(태스크·반성·당시 신뢰도·결과·채점 후 작성한 교훈)를 저장해 두고 Recall 단계에서 **유사 태스크 + 유사 신뢰도**의 과거 성공률을 읽고, Reflect 단계에서 반복 실패 모드를 스스로 지목하게 한 뒤 신뢰도를 재진술한다.
  - 🎯 **분모가 공개된 수치**: 9개 벤치마크 · 3개 패밀리 4개 모델에서 **24개 비교 중 23개**에서 10샘플 self-consistency의 AUROC를 **이기거나 동일**, ECE는 더 낮고 **생성 비용은 1/10**(답변 1회 생성).
  - 선택적 예측: 가장 자신 없는 **10%를 포기**하면 에이전트 태스크 실측 성공률이 **최대 +8.7점**.
  - ✅ 실용 조건(초록 명시): **logit 접근·가중치 업데이트 불필요**, 포맷 무관. → API-only 모델에도 적용 가능.

## [2026-09-17] 자동수집 | ProgramDistill: From Interactive Web Apps to Verifiable Reference-Guided SWE Tasks
- URL: https://huggingface.co/papers/2609.18805
- 도메인: ai-news
- 업보트: 40 (HF 데일리 3위 / 2026-09-16 게재)
- 한줄요약: 이슈·지시문으로 목표를 주는 기존 SWE 평가와 달리, **완성된 참조 앱을 직접 조작해 기능을 알아내고 미완성 앱에 구현**하게 하는 벤치마크다. `mine-craft-patch` 파이프라인이 26개 앱에서 **재생 검증된(replay-verified) 행동 1,975개**를 찾아 **사람 개입 없이 4,063 태스크**를 만들었다.
  - 🔴 **지는 축을 함께 적는다** — 9개 프런티어 에이전트 중 누적 워크플로 성공률: **GPT-6 Astra 49.2% / Claude Opus 5 28.8%**. 즉 **최고 성능도 절반 미달**이다.
  - 🎯 **난이도가 통제된다는 증거**: 부분 앱 복원에서 복원 깊이를 1→8로 올리자 성공률이 **100%→64.0%** 및 **96%→32%** 로 떨어진다. 깊이 하나가 축이다.
  - 실용성: 커리큘럼 학습의 근거로 쓸 수 있다고 저자가 직접 언급(*"a natural basis for future curriculum-based training"*).

## [2026-09-17] 자동수집 | Rethinking Critic Learning in PPO: Understanding and Mitigating Value Flattening
- URL: https://huggingface.co/papers/2609.18708
- 도메인: ai-news
- 업보트: 35 (HF 데일리 4위 / 2026-09-16 게재)
- 한줄요약: LLM용 PPO의 크리틱에서 **Value Flattening** 이라는 실패 모드를 규정했다 — 몬테카를로 continuation으로 추정한 실제 상태가치는 중간 상태에서 급하게 변하는데 **크리틱 예측은 상대적으로 평평하게 남는다**. 원인을 크리틱 손실의 **암묵적 분산 페널티**와 시간적으로 상관된 상태들의 **중복 업데이트**로 귀속시키고, 응답당 **잘 분리된 소수 상태에만 value loss를 적용하는 SP³O**를 제안한다.
  - 🎯 **성립 조건이 초록에 있다**: FrozenLake 통제 환경에서 **상태공간이 커질수록 현상이 심해진다** — 즉 작은 태스크에서는 안 보이는 문제다.
  - 실측: Qwen3-Base에서 **응답당 3개 상태만 감독**해도 모델 크기·평가 스위트 전반에서 일관된 개선. 🔴 단 **개선폭 수치가 초록에 없다**(*"consistently improve"* 까지만).
  - 실용성: 기존 PPO 파이프라인에 **손실 적용 지점만 바꾸는 변경**이라 이식 비용이 낮다.

## [2026-09-17] 자동수집 | ActionPiece: Rethinking Action Tokenization for Autoregressive Vision-Language-Action Models
- URL: https://huggingface.co/papers/2609.18487
- 도메인: ai-news
- 업보트: 32 (HF 데일리 5위 / 2026-09-16 게재)
- 한줄요약: VLA 모델의 액션 토크나이저를 **MSE 같은 점별 복원 오차로 평가하는 관행을 반증**하고, 복원 후 **국소 물리 거리 순위가 보존되는지**를 재는 지표 **PRC(physical rank consistency)** 를 제시한 뒤, 표현학습과 양자화를 공동 감독해 관계를 지키는 **ActionPiece**를 내놓는다.
  - 🎯 **측정도구를 먼저 반증한 사례**: 초록 원문 — *"small individual errors do not fully characterize how faithfully action adjustments across demonstrations are preserved"*, 압축 후 유사 동작이 대표 모션으로 뭉치면서 문맥별 조정이 *"diminished, distorted, **or even reversed**"* 된다. → [[측정도구-먼저-반증]] 과 같은 구조.
  - 실측(동일 Qwen3-VL-4B 정책 학습 설정): **LIBERO 94.8%** · **미학습 LIBERO-Plus 68.8%** · SimplerEnv 71.9% · VLA-Arena L0–L2 **51.5%**.
  - 🔴 **지는 축**: 학습 분포(94.8%)와 미학습(68.8%) 사이 **−26.0점 격차**가 있고, VLA-Arena L0–L2는 **51.5%** 로 절반 수준이다. 일반화는 해결되지 않았다.

---

## [2026-09-17] 자동수집 | deepseek-ai/DeepSeek-R1
- URL: https://huggingface.co/deepseek-ai/DeepSeek-R1
- 도메인: ai-news
- 다운로드수: 740,958 (♥ 14,252 / **DL:♥ = 52:1** / trendingScore 126 / MIT / gated 아님)
- 한줄요약: 671B 총 파라미터 중 **37B만 활성화되는 MoE 추론 모델**(컨텍스트 128K)이며, 모델카드 표 기준 MMLU-Redux 92.9 · MATH-500 97.3 · AIME 2024 79.8 · Codeforces 2029로 **o1-1217과 벤치마다 서로 이기고 지는 관계**다(o1이 MMLU 91.8·GPQA-D 75.7·SWE-V 48.9에서 우세, R1이 MATH-500·AIME·AlpacaEval2.0 87.6에서 우세).
  - 🏗️ **상시 인프라 (신규 릴리스 아님)** — 2025-01-20 생성 · **최종 수정 2025-03-27**. 1년 6개월 갱신 없이 트렌딩에 있다. → [[상대속도-가림]] 규칙 적용.
  - 🔍 **DL:♥ 52:1 은 이 채널에서 이례적으로 낮다** — [[ms-marco-MiniLM-L6-v2]] 의 *"자동화 지문"*(고DL·저♥)과 **반대 방향**이다. 다운로드 74만에 ♥ 1.4만 = 사람이 페이지를 실제로 방문한다.
  - ✅ **09-16 볼트 요청 이행 — 디스틸 패밀리 5점 비교** (카드 표 AIME 2024 pass@1 / MATH-500 / GPQA-D / CodeForces):
    - `Qwen-1.5B` 28.9 / 83.9 / 33.8 / 954
    - `Qwen-7B` 55.5 / 92.8 / 49.1 / 1189 — params ×4.7, **AIME +26.6**
    - `Qwen-14B` 69.7 / 93.9 / 59.1 / 1481 — params ×2.0, **AIME +14.2**
    - `Qwen-32B` 72.6 / 94.3 / 62.1 / 1691 — params ×2.3, **AIME +2.9**
    - `Llama-70B` 70.0 / 94.5 / 65.2 / 1633 — params ×2.2, **AIME −2.6 · CodeForces −58**
    - 🎯 **변곡점은 14B다.** 14B→32B에서 AIME 증가가 +2.9로 꺾이고, **32B→70B에서는 AIME·CodeForces가 실제로 하락**한다(MATH-500은 +0.2로 포화, GPQA-D만 +3.1로 계속 오른다). → [[수확체감-변곡점]] 에 **"꺾인 뒤 음수로 넘어가는 구간"** 사례로 보강.
    - 🔍 **크기가 순위를 정하지 않는 반례가 같은 표 안에 있다**: `Llama-8B` 50.4 < `Qwen-7B` 55.5 — **더 큰 모델이 AIME에서 5.1점 낮다**. 베이스 모델(Qwen2.5-Math-7B vs Llama-3.1-8B)이 크기보다 크게 작동했다.
  - 🔴 **`arxiv:2501.12948` 태그 관련(09-16 볼트 규칙)**: 이 경우는 태그가 실제로 자기 논문이다 — 카드 본문 46행이 `DeepSeek_R1.pdf` 로 직접 링크하고, 인용 블록(231–233행)이 같은 arXiv ID를 가리킨다. **태그만 보고 적은 것이 아니라 본문에서 대조했다.**

## [2026-09-17] 자동수집 | DavidAU/Qwen3.8-27B-TWIN-TURBO-Fable-Cold-Fusion-709-L-Uncensored-NM-DAU-NEO-MTP-GGUF
- URL: https://huggingface.co/DavidAU/Qwen3.8-27B-TWIN-TURBO-Fable-Cold-Fusion-709-L-Uncensored-NM-DAU-NEO-MTP-GGUF
- 도메인: ai-news
- 다운로드수: 114,335 (♥ 150 / **DL:♥ = 762:1** / trendingScore 139 / Apache-2.0 / 2026-09-10 생성·09-17 수정)
- 한줄요약: Qwen3.8-27B를 다단계 파인튜닝·머지한 커뮤니티 모델의 **GGUF 양자화 재배포판**이며, 실제로 검증 가능한 변경은 **추론 토큰 수 감소**(카드 주장 1/2~1/20)와 **거부 응답 제거**다 — 카드 표 실측: KL divergence 0.0535 / **거부 0/100회** (원본 Qwen3.8-27B는 **99/100회 거부**).
  - 🔴 **마케팅 문구 제외분**: *"The most powerful, smartest open source multi-stage model fine tune"* · *"Closed source level of intelligence"* · *"The OpenAI, Claude and Gemini zone of intelligence"* 는 **제3자 검증이 없는 자기 주장**이다.
  - ✅ **패밀리 3점 비교(카드 본문 수치)**: arc-c **709**(8비트) / **701**(4비트) / 원본 Qwen3.8-27B **591**(카드의 *"118 pts higher"* 에서 역산). 즉 **8→4비트 양자화 손실은 −8점이고, 튜닝 이득은 +118점**이라는 주장 구조다.
    - 🔴 **분모·방법론 미공개**: arc-c가 몇 문항 기준인지, 어떤 하네스로 쟀는지 카드에 **없다**. 같은 저자가 *"ELEVEN 모델 모두 700 arc-c 초과"*(186행), *"Qwen3.5 9B가 640 ARC-C"*(203·561행)라고 적고 있어 **자체 측정치 계열 전체가 같은 미공개 방법론**을 공유한다. **확인 불가.**
  - 🔍 **DL:♥ 762:1** — DeepSeek-R1(52:1)의 **14.6배**. 다운로드는 많고 사람의 반응은 적은 [[ms-marco-MiniLM-L6-v2]] 형 지문이지만, 이쪽은 상시 인프라가 아니라 **1주일 된 신규 릴리스**다. GGUF 양자화 파일 다중 다운로드가 분자를 부풀리는 구조로 보인다 — **추정, 확인 필요.**
  - 🏗️ **신규 릴리스** (생성 7일 · 어제도 수정).

## [2026-09-17] 자동수집 | Comfy-Org/YuE2
- URL: https://huggingface.co/Comfy-Org/YuE2
- 도메인: ai-news
- 다운로드수: 59,231 (♥ 153 / **DL:♥ = 387:1** / trendingScore 147 / **CC-BY-NC-4.0 = 비상업** / 2026-09-11 생성)
- 한줄요약: 새 모델이 아니라 **ComfyUI용 재포장(repackage)** 이다 — 카드 전문이 *"Repackaged model files for ComfyUI"* 이고, 파일은 `yue2_3b_bf16.safetensors` · `yue2_3b_int8_convrot.safetensors` · `sheetsage2_bf16.safetensors` **3개뿐**(전체 5개 중 나머지는 README·gitattributes).
  - 🔴 **중복 관계를 명시한다**: 원본 `m-a-p/YuE2-3B` 는 **볼트 기보유**([[YuE2-3B]]). 리터럴 grep으로는 NEW지만 **실질은 파생 저장소**다. 중복 필터를 통과한 이유는 **repo id가 다르기 때문**이며, 새 능력이 추가된 것은 아니다.
  - 🎯 **그래도 배달하는 이유 — 양자화 축이 새로 생겼다**: 원본에 없는 `int8_convrot` 변형이 여기 있다. 같은 모델을 **bf16 / int8** 두 점으로 비교할 수 있는 파일이 한 레포에 모여 있다.
  - 🔴 **라이선스가 원본과 갈린다**: 이 레포는 **CC-BY-NC-4.0(비상업)**. base_model 태그는 `m-a-p/YuE2-3B` 와 `m-a-p/SheetSage2` 둘을 가리킨다 — **음악 생성 본체 + 오디오 인코더**가 한 배포에 묶였다. 상업 사용 시 원본 라이선스 별도 확인 필요.
  - 🔍 성능 수치: **카드에 없다.** 벤치는 원본 [[YuE2-3B]] 페이지 참조.

---

### 📌 도메인 불일치 제외 기록 — README 본문 인용 (09-15 볼트 규칙 상시 적용)

NEW풀에 남았으나 **AI/ML이 아니어서** 제외한 건. 판정 기준은 09-16 볼트 신설 규칙 **"AI를 빼면 그 기능이 사라지는가"**.

- ❌ **`Lakr233/vphone-cli`** (트렌딩 daily **6위** · ★13,528 · 당일 +547 = 4.05% · NEW) — **README 62행 확인.** topics가 비어 있어 본문으로 판정했다. 4행: *"Boot a virtual iPhone via Apple's **Virtualization.framework** using PCC research VM infrastructure."* 명령 목록(`vm create`/`launch`/`clone`/`export`)도 전부 VM 수명주기다. **AI를 빼도 가상 iPhone 부팅이 그대로 남는다** → AI 무관. 🔴 **상대속도 4.05%로 이번 슬레이트 3위인데 제외했다** — 지표가 아니라 도메인으로 갈랐음을 명시한다.
- ❌ **`microsoft/Data-Science-For-Beginners`** (jupyter-daily **13위** · ★37,056 · 당일 +101 · NEW) — **README 커리큘럼 표 확인.** topics: `data-analysis,data-science,data-visualization,pandas,python` — **ai/ml 없음.** 본문 154행이 결정적이다: 1강 학습목표가 *"Learn the basic concepts behind data science and **how it's related to** artificial intelligence, machine learning, and big data"* — **ML은 주제가 아니라 "관련 분야"로 소개된다.** 20강 구성은 SQL·NoSQL·pandas·데이터 준비·시각화·통계·윤리다. **ML을 빼도 커리큘럼이 온전히 남는다** → AI 부가.
  - 🔴 **이 제외가 순위를 바꿨다**: +101/일은 채택 3위 `cline`(+112)과 4위 `oh-my-hermes`(+80) **사이**다. 제외하지 않았다면 4·5위가 밀려났다. **제외 판정 하나가 배달 2건을 결정했으므로 근거를 본문에서 인용했다.**
- ❌ 지표 기준 미달 없음 — **NEW ∩ AI/ML 8건 전부 ★1,000 이상**이었다. 이번 배치에서 스타수로 탈락한 건은 **0건**이다.
- 📋 **AI/ML로 인정했으나 쿼터 밖(6~8위)**: `onyx-dot-app/onyx`(★32,144 · +19 = 0.06%) · `facebookresearch/sam2`(★19,879 · +10 = 0.05%) · `higgsfield-ai/higgsfield`(★4,220 · daily 미진입). **셋 다 상대속도 0.1% 미만 또는 daily 부재** — 다음 배치에서도 같은 위치면 [[상대속도-가림]] 기준 상시 인프라로 분류될 후보다.

---

### 📌 수집기 자기 한계 (2026-09-17)

1. **README 상단만 읽었다.** `cline`·`oh-my-hermes` 는 48행, 나머지는 60~62행이다. `oh-my-hermes` 의 *"evidence boundaries"* 실제 구현과 `cline` 의 능력 수치는 **별도 문서에 있고 읽지 않았다.** 주장/구현을 구분해 표기했다.
2. **논문 5건 모두 초록만 읽었다.** 본문·부록 미확인. `SP³O` 개선폭과 `ScienceIDE` 의 *"selected benchmarks"* 가 무엇인지는 **초록에 없어서 적을 수 없었다** — 없다는 사실까지가 이번 범위다.
3. **`DavidAU` 의 arc-c 709/701/591 을 재현하지 못했다.** 방법론이 카드에 없어 **반증도 불가**하다. 수치를 옮기되 *"자기 주장"* 으로 못 박았다.
4. **HF 트렌딩 모델 페이지 파싱이 실패해 API(`sort=trendingScore`)로 우회했다.** 웹 페이지의 `ModelList` props가 비어 반환됐다(`models: 0`). 따라서 **이번 모델 3건의 순위 근거는 웹 화면이 아니라 API 응답**이다 — 화면과 API가 어긋날 가능성을 배제하지 못한다.
5. **`Comfy-Org/YuE2` 는 리터럴 기준 NEW이지만 실질 파생이다.** 중복 필터가 `org/name` 리터럴이므로 **재포장·양자화 파생 저장소를 잡지 못한다** — 이번엔 수집기가 수동으로 발견해 명시했지만, **필터 자체는 이 구조를 놓친다.**

> ### 📌 볼트에 묻는다 — **딱 하나**
> **재포장·양자화 파생 저장소를 중복으로 볼 것인가, 새 축으로 볼 것인가.**
>
> `Comfy-Org/YuE2` 는 `org/name` 이 달라 필터를 통과했지만 **가중치는 볼트가 이미 가진 [[YuE2-3B]]** 다. 그런데 **원본에 없는 `int8_convrot` 양자화 파일**이 붙어 있고 **라이선스가 CC-BY-NC로 갈린다** — 즉 *"같은 모델"* 이라고 하기에도 걸리는 게 있다.
>
> **선택지**: (a) `base_model` 태그가 볼트 기보유를 가리키면 **중복 처리** · (b) 양자화/라이선스/런타임이 갈리면 **파생 축으로 채택** · (c) 원본 페이지에 **섹션으로 병합**.
>
> 이번 배치는 **(b)로 배달했고 관계를 명시**했다. 판정해 주면 다음 배치부터 `base_model` 태그를 **중복 필터 2차 키로 추가**할 수 있다 — 현재 필터는 `org/name` 리터럴 단일 키다.

---

## 📮 2026-09-16 배치 판정 (볼트 → 수집기) — 이번 배치에 적용 완료


### ✅ **요청을 이행했다 — 그리고 요청 범위를 넘어섰다**

볼트 09-15 요청: *"GitHub 후보를 도메인 불일치로 제외할 때 README 서두(최소 60행)를 확인했다고 적고, 제외 근거를 topics가 아닌 본문에서 인용할 것."*

**판정 기준은 *"제외 건에 README 인용이 붙어 있는가"* 였다. 수집기는 4건 전부에 인용을 붙였고, 그 위에 하나를 더 했다 — 제외 근거를 찾다가 [[gods-eye-view]] 와 같은 패턴을 발견하고 재판정을 요청했다.**

🎯 **이게 09-15와 다른 점이다.** 09-15에는 수집기가 topics만 보고 제외한 뒤 *"틀렸다면 재판정 요청"* 을 자기 한계에 적었고, **볼트가 검증해서 오판을 찾았다.**
09-16에는 **수집기가 자기 배치 안에서 스스로 찾았다.** 규칙이 **사후 검증에서 사전 탐지로** 이동했다.

**볼트 독립 검증 — 보고가 사실이다:**
```
org/name 리터럴 grep   : 5건 전부 0히트
arXiv 논문 ID grep     : 5건 전부 0히트
HF repo id grep        : 3건 전부 0히트
────────────────────────────────────────
13/13 NEW · 중복 0%   (2배치 연속)
```

**지표 드리프트 (볼트 API 재호출):**
- GitHub: pi **+10** · LibreChat **+2**(fork 9,038 **완전일치**) · 9router **+1** · worktrunk **+2** · atlas **+2** · omniget **+10**
- HF모델: ms-marco **0** · electra **0** · 🔴 **bge-small +620,302 (+0.97%)**
- 논문 업보트: 273(**0**) · 84(+1) · 84(+1) · 46(**0**) · 29(+2) — **전부 상승 또는 동일**
- ✅ **초록 5건 전문 대조 — 수집기 인용 전건 문자 일치** · README 인용(pi 41행 · omniget 주석) **전건 일치**

---

### ⚖️ **`omniget` 재판정 — 제외 유지. 단, 근거를 바꾼다**

**결론은 같고 이유가 다르다.** → [[omniget-재판정]] 페이지 생성

- ❌ **수집기 근거로는 가를 수 없다**: *"158개 도구 중 AI 카테고리 6개"* 는 **비중 논거**인데, [[gods-eye-view]] 도 기능 3개 중 1개였고 **그건 채택 대상이었다.**
- ✅ **볼트 근거**: 🎯 **omniget의 AI는 목적이 아니라 인터페이스다.** README 252행이 직접 말한다 — *"each tile is one job: an isolated Rust command with JSON in and JSON out, **which is also what lets AI agents drive them**"*. **JSON in/out 설계가 먼저 있고 MCP는 그 파생 효과다.**
  반면 gods-eye-view의 *"Hands-free voice control powered by a realtime AI agent"* 는 **AI 없이는 존재하지 않는 기능**이다.

> **볼트 규칙 (신설)**: 도메인 판정은 **"AI를 빼면 그 기능이 사라지는가"** 로 한다.
> 사라진다 → AI 네이티브(채택) · 남는다(느려질 뿐) → AI 부가(제외).
> **비중(몇 %)이 아니라 의존성(없으면 성립하는가)을 본다.**

🎯 **그리고 수집기가 찾은 README 주석이 09-15 볼트 추론을 저자 진술로 확정했다**:
> *"**GitHub allows 20 topics. The repository uses exactly these 20**"*
**AI 기능이 없어서 topics에 AI가 없는 게 아니라, 자리가 없어서 없다.**

---

### 🔴 볼트 발견 3건 — 수집기 자기 한계 2·3번에 대한 답을 겸한다

**1. `arxiv:` 태그는 모델의 논문이 아니다 (자기 한계 2번 관련)**
수집기: *"`electra-base-discriminator` 의 SQuAD 2.0 주장을 원논문으로 대조하지 않았다."*
→ 🔴 **볼트가 확인한 것은 더 근본적인 문제다. 이 모델의 유일한 arxiv 태그 `1406.2661` 은 ELECTRA 논문이 아니라 GAN 원논문(Goodfellow)이다.**
카드 11행 *"similar to the discriminator of a [GAN](arxiv.org/pdf/1406.2661.pdf)"* 를 **HF가 자동 파싱**한 결과이며, **ELECTRA 원논문은 openreview에만 있어 태그가 될 수 없었다.**
✅ **그리고 카드 13행에 원논문 링크가 실재한다**(`openreview.net/pdf?id=r1xMH1BtvB`) — 정확한 상태는 *"수치가 없다"* 가 아니라 **"수치를 1차 출처로 위임했다"** 이다.
📌 [[bge-small-en-v1.5]] 도 **태그 5개 중 1개**만 자기 논문(2309.07597)이다. → [[파생표기-함정]] 4번째 사례

> **요청**: **HF 모델 배달 시 `arxiv:` 태그를 "논문"으로 적지 말 것.** 원논문은 카드 본문의 *"our paper"* 문장에서 찾는다.

**2. 🔴 `bge-small-en-v1.5` 한줄요약이 v1.5의 변경 방향과 반대다**
수집기: *"검색용 질의에 **지시문 프리픽스를 붙이는 방식**의 소형 영문 임베딩 모델"*
→ **카드 2652행**: *"release `bge-*-v1.5` ... and **enhance its retrieval ability without instruction**"*
🎯 **v1.5의 존재 이유가 "지시문 의존을 줄인 것"이다.** 프리픽스는 사용법 표에 **여전히 보이지만** 그건 v1.0부터의 표기이고, **버전이 바꾼 것은 표가 아니라 변경 이력에 적혀 있다.**
📌 자기 한계 3번(58.09 집계)은 **수집기 판단이 옳다** — 분모를 밝혔기 때문에 볼트가 *"Retrieval 27/68 = 39.7% 편중"* · *"Summarization n=1"* 을 지적할 수 있었다. **분모 공개를 기본값으로 유지할 것.**

**3. 🎯 표를 2행만 읽으면 결론의 성격이 달라진다**
수집기는 `ms-marco` 카드에서 **L6 vs L12** 2행을 비교해 *"−0.01인데 1.875배"* 를 얻었다. **맞는 계산이다.**
**볼트가 표 16행 전체를 읽고 L4를 추가하자 다른 것이 보였다**:
- L4→L6: NDCG **+1.26** / 처리량 −28% ← **싸다**
- L6→L12: NDCG **+0.01** / 처리량 −47% ← **비싸다**
🎯 **L6은 "L12보다 나은 선택"이 아니라 곡선이 꺾이는 무릎이다.** 8,886만 DL의 이유가 여기 있다. → [[수확체감-변곡점]] 신설

> **요청**: **모델 패밀리 비교 시 최소 3점을 잡을 것.** 2점 비교는 *"어느 쪽이 나은가"* 만 답하고, 3점은 **기울기가 어디서 꺾이는가**를 답한다.

---

### 📌 볼트 자기 한계

1. **코드를 읽지 않았다.** pi의 권한 부재 · omniget의 MCP 통합 깊이 · atlas의 공유 메모리 구현 — 전부 **README·초록 수준 확인**이다. 수집기 한계 4번과 **같은 한계**다.
2. **openreview 본문을 읽지 않았다.** ELECTRA의 SQuAD 2.0 주장은 여전히 미대조다. 볼트가 추가한 것은 **"어디로 가면 있는지"** 까지다.
3. **[[bge-small-en-v1.5]] small/base/large 3점 비교를 하지 않았다.** [[수확체감-변곡점]] 을 신설해 놓고 **정작 같은 배치의 다른 패밀리에 적용하지 않았다.** 카드에 MTEB 결과가 있으므로 **계산 가능한데 하지 않았다** — 다음 배치 숙제로 남긴다.
4. **9router의 RTK 압축률을 측정하지 않았다.** *"20-40%"* 가 틀렸다고 말할 근거도 없다 — **레포에 방법론이 없어 확인 불가**까지가 볼트 범위다.

---

> ### 📌 다음 배치 요청 — **딱 하나**
> **HF 모델 배달 시, 모델카드에 성능표가 있으면 "내 모델 행"만이 아니라 같은 패밀리 3점 이상을 함께 옮길 것.**
>
> 이번에 `ms-marco` 표에서 **L4 한 행이 추가되자 결론이 바뀌었다** — *"L12는 손해"* 에서 *"L6이 수확체감 변곡점"* 으로.
> **비용 비대칭**: 표에서 2행 더 옮기기 = 후보당 몇 초 / 놓치는 것 = **채택 수치의 진짜 원인.**
>
> **판정 기준**: *다음 배치 HF 모델 중 카드에 패밀리 성능표가 있는 건이 있다면, 그 항목에 **3점 이상 비교**가 적혀 있는가. 표가 없는 건뿐이라면 이 요청은 자동 충족으로 본다.*
>
> 다른 규칙(±10행 · 표 우선 · 지는 축 · 라이선스 본문 · 단위 불일치 · 한정어 병기 · 성립 조건 같은 불릿 · 72시간/7일 지표 · 정체 임계선 · `org/name` 리터럴 1순위 · **선발 전 중복 필터** · **논문 제목 원문 배달** · **상시 인프라/신규 릴리스 구분** · **README 60행 인용**)은 이번에 전부 적용됐으므로 **유지**한다.
>
> 🎯 **5배치 연속 개선이다.** 09-12 중복 탐지 → 09-13 한정어 → 09-14 성립 조건 → 09-15 백필 구조적 제거 → **09-16 제외 근거 본문 인용 + 자체 재판정 발의.**
