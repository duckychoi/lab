---
title: Tiel-Coder-35B-A3B-GGUF — 4bit 22GB로 Opus 4.6과 동률, 대신 지식을 팔았다 (n=25의 한계 포함)
type: source
domain: local-llm
tags: [local-llm, ai-news, hf-model, gguf, moe, agentic-coding, quantization, imatrix, swe-bench, vision]
created: 2026-09-07
updated: 2026-09-07
sources: []
reliability: medium
---

# peculiar-ragdoll/Tiel-Coder-35B-A3B-GGUF

**HF**: https://huggingface.co/peculiar-ragdoll/Tiel-Coder-35B-A3B-GGUF
**다운로드(최근 30일)**: **238,588** (2026-09-07 API 실측 · raw 표기와 **완전 일치**)
**좋아요 230 · 생성 2026-08-19 · 최종수정 2026-08-30 · `gated: False`**
**라이선스**: **MIT** · **베이스**: `ornith-ai/Ornith-1.5-35B-A3B`(MoE) · `base_model_relation: quantized`
**태그 실측**: `qwen35moe` `moe` `imatrix` `unsloth-dynamic` `agentic-coding` `token-efficient` **`vision`** · `pipeline_tag: image-text-to-text` · **en/zh**

> [!insight] 핵심 인사이트 — **양자화 배포자가 "무엇을 팔고 무엇을 잃었는지" 둘 다 공개했다**
> 이 모델은 Ornith-1.5-35B-A3B 를 **자체 imatrix로 동적 재양자화**하고 **Sharp 채팅 템플릿을 GGUF 안에 심은** 4bit·22GB 빌드다. 카드 첫 문단 원문: *"**Pick it for work. Pick something else for exams.**"*
> 볼트가 [[Huihui-Qwen3.8-27B-abliterated-GGUF]](같은 배치, 벤치마크 전무)와 나란히 두면 대비가 선명하다 — **같은 GGUF 재배포자 층인데, 한쪽은 아무것도 재지 않았고 이쪽은 이득과 손실을 모두 수치로 냈다.**

## 수치 (모델 카드 원문 실측)

**SWE-bench-Live (25문제 · 로컬 빌드 비교)**

| 모델 | 해결 | 시도당 시간 |
|---|---|---|
| Qwen3.8-27B (dense) | **16** | 50.2분 |
| Dirk-Qwen3.8-27B | **15** | 20.1분 |
| **Tiel-Coder-35B-A3B** | **12** | **8.6분(중앙값)** · 12.3분(평균) |
| Ornith-1.5 (베이스) | 8 | — |
| stock Qwen3.6-35B-A3B | 8 | 5.5분 |

- **Opus 4.6 (medium)**: 12 — **Tiel과 동률**
- **Nail-Qwen3.6-35B-A3B**: 9 (Tiel **+3**) · 중앙 7.2분 / 평균 **15.7분**
- **Sonnet 5 (medium)**: 8 (Tiel **+4**)

**Claw-Eval 멀티턴** (각 114개 대화 채점): **Tiel 67.2** · Ornith 65.3 · Nail 60.5
**MMLU-Pro** (4bit): **Tiel 73.7** · Nail 84.0 · Ornith 78.0 · stock Qwen3.6-35B-A3B 85.3

> [!insight] 저자가 자기 열세의 원인을 **분해해서** 밝혔다 — 볼트 기준 상위 서술 정직성
> MMLU-Pro 73.7 vs Nail 84.0 은 **10.3점 열세**다. 카드는 이걸 숨기지 않고 **원인을 나눈다**(원문):
> - **대부분은 상속**: Ornith-1.5 가 78.0 인데 stock Qwen3.6-35B-A3B 는 85.3 → **베이스에서 이미 7.3점 잃었다**
> - **양자화는 원인이 아니다**: *"the same quant carrying Ornith's own template **scores exactly what Ornith scores**"* → **통제 실험(대조군)을 넣었다**
> - **남은 4.3점**: **Sharp 템플릿이 답변을 짧게 만든** 대가 — *"the trade this build exists to make"*
> → **자기 손실을 3분해하고 그중 하나에 대조군을 붙였다.** 볼트가 [[Repo-To-Skill]] 이후 찾던 *"통제 실험을 가진 자산"* 의 두 번째 사례이며, **재배포자 층에서는 처음**이다.

> [!insight] 대화 품질의 대가도 밝혔다 — "더 물어보지 않아서 이긴다"
> Claw-Eval 67.2(베이스 65.3) 의 내역(원문): 베이스 대비 **답변 품질 +3.8**, **해명 질문 -5.1**. 점수가 **답변에 4:1 가중**이라 트레이드가 이득이 된다.
> 카드의 경고 원문: *"if you want a model that **interrogates a vague request before acting**, the base does that better."*
> 🔴 **볼트 교차 — 같은 배치 [[Ask-Before-You-Optimize]] 가 정확히 이 능력을 재는 벤치마크다.** 그 논문의 결론은 *"불완전한 요구에 되묻는 능력이 평가에서 누락돼 왔다"* 였고, Tiel은 **그 능력을 의도적으로 깎아서 점수를 얻었다.**
> → **평가 가중치가 능력의 방향을 만든다.** Claw-Eval이 답변에 4:1 가중을 주는 한, 모델은 **덜 묻는 쪽으로 최적화된다.** 두 소스를 같은 날 함께 읽지 않았다면 보이지 않았을 연결이다.

> [!warning] 🔴 **n=25** — 이 카드 수치의 가장 큰 구조적 한계
> SWE-bench-Live 비교가 전부 **25문제**다. **1문제 = 4%p** 다. Tiel 12 vs Nail 9 의 *"+3"* 은 **3문제 차이**이고, Opus 4.6 과의 *"동률"* 도 **12 대 12**다.
> **표본 25에서 나온 순위는 재실행 시 뒤집힐 수 있다.** 카드는 시간 지표에는 중앙값/평균을 병기하며 분포를 신경 썼는데, **해결 수에는 신뢰구간이 없다.**
> 추가로 **모든 수치가 저자 자체 측정**이며, 카드 본문이 아니라 **`assets/card_*.png` 이미지의 alt 텍스트**에 실려 있다 — 독립 검증 없음. 볼트 규칙상 **"저자 자체 측정"으로 명시해 인용**하고, *"Opus 4.6 급"* 같은 일반화는 **금지**.

> [!note] 놓치기 쉬운 실측 사항 — raw가 빠뜨린 것들
> - **`vision` 태그 · `pipeline_tag: image-text-to-text`** → **비전 입력을 지원**한다. raw 요약에 없다.
> - **KV 캐시가 작다**: 카드 원문 *"<5 GB RAM for 262k context at 16-bit KV"* — MoE라 27B dense 대비 유리. **긴 컨텍스트 로컬 에이전트에 실질 이점.**
> - **저자 권장**: UD-Q4 **미만으로 내리지 말 것**. VRAM에 다 넣으려고 양자화를 낮추느니, **RAM+VRAM에 걸쳐 Q4 이상 + 131k~262k 컨텍스트 + 최소 q8_0 KV** 를 택하라.
> - **MTP 변종 별도 배포**: `Tiel-Coder-35B-A3B-GGUF-MTP`

## 도메인별 추출 (local-llm)

- **실용성 판단**: **높음.** 4bit **22GB**·MIT·gated 아님·GGUF. 소비자 GPU에 부분 오프로딩으로 올릴 수 있고, **중앙값 8.6분/시도**는 [[Qwen3.8-27B]](50.2분)의 **5.8배 빠르다**. **에이전틱 코딩에서 시간이 곧 사용성**이라는 점에서 12/25 라는 낮은 절대치를 상쇄한다.
- **메모리 아키텍처**: MoE(A3B = 활성 3B급) → **KV 캐시 262k에 5GB 미만**. 볼트의 [[Random-Attention]]·[[LatentPress]] 계열 KV 최적화와 **곱해질 수 있는** 구조.
- **Hermes 적용**: **이 배치 3개 모델 중 1순위 후보.** 이유는 성능이 아니라 **측정이 있기 때문**이다. [[Huihui-Qwen3.8-27B-abliterated-GGUF]] 는 수치가 없고, [[timesfm-3.0-pytorch]] 는 **상업 이용 불가**다.
- **트레이드오프**: **명시적** — 지식(MMLU-Pro **-10.3** vs Nail) 과 **되묻기(-5.1)** 를 팔아 **코딩 성공률(+3)** 과 **속도(1.8배)** 와 **대화 품질(+6.7)** 을 샀다. 시험형 지식이 필요한 용도에는 Nail, 그 외 코딩·긴 대화에는 Tiel.
- **오픈소스 구현체**: 모델 자체가 GGUF. llama.cpp 즉시 구동.

> [!action] 당장 할 것
> **UD-Q4 이상 + q8_0 KV 로 로컬 구동 1회.** 검증할 것은 벤치 재현이 아니라 **볼트 자신의 작업**이다 — `/wiki` 인제스트 파이프라인의 소스 요약을 이 모델로 돌려보고, [[Ask-Before-You-Optimize]] 가 지적한 **"불완전한 입력에 조용히 가정하는"** 성향이 실제로 나타나는지 본다. 카드가 **그 성향을 스스로 예고**했으므로 검증 가설이 이미 서 있다.

> [!question] 미해결
> **베이스 Ornith-1.5-35B-A3B 와 Sharp 채팅 템플릿이 각각 무엇인가.** 둘 다 볼트에 페이지가 없다. 특히 **Sharp 템플릿이 MMLU-Pro 4.3점과 해명질문 5.1점을 동시에 깎았다면**, 그건 템플릿 하나가 모델 행동을 크게 바꾼다는 뜻 — **[[에이전트-스킬]] 의 "프롬프트가 능력을 만든다" 축과 직결**된다. 추적 공백 2건.

## 관련 페이지
- [[Qwen3.8-27B]] · [[Qwen3.8-27B-GGUF]] · [[Huihui-Qwen3.8-27B-abliterated-GGUF]] · [[Ask-Before-You-Optimize]] · [[Random-Attention]] · [[LatentPress]] · [[Minima]] · [[Dont-Drop-Dropout]] · [[Repo-To-Skill]] · [[에이전트-스킬]] · [[선택비용과-중복성]] · [[검사가능성-공사]] · [[Alibaba]]

## 원본
- 출처: https://huggingface.co/peculiar-ragdoll/Tiel-Coder-35B-A3B-GGUF
- 베이스: https://huggingface.co/ornith-ai/Ornith-1.5-35B-A3B (**미인제스트**)
- 수집: 2026-09-07 자동수집 (raw 도메인 ai-news → **local-llm 재분류**)
- 검증: HF 모델 API 실측 + 모델 카드 원문 대조 (2026-09-07 · DL 238,588 raw와 일치)
- 신뢰도: ⭐⭐⭐ (**전 수치가 저자 자체 측정 · n=25 · 독립 검증 없음** — 단 통제군과 자기 열세를 함께 공개한 점은 가점)
