---
title: Sharpening Tax in Post-Training — RL 후처리가 커버리지를 깎는 비용을 지표화 (42케이스)
type: source
domain: local-llm
tags: [ai-news, hf-paper, rl-post-training, pass-at-k, coverage, agentic, harness, ptgs, meta, pdf-verified]
created: 2026-10-03
updated: 2026-10-03
sources: []
reliability: high
---

# Sharpening Tax in Post-Training (2610.01509)

> [!insight] 핵심 인사이트
> **경량 추론 하네스를 붙인 사전학습(base) 모델이 유능한 에이전트로 동작하고, pass@1 은 훨씬 낮아도 테스트시 예산이 충분하면 후처리 모델의 해법 커버리지(pass@K)를 자주 상회한다.**
> 기제: **후처리는 과제를 "항상 풀림 / 절대 안 풀림" 두 극단으로 밀어**(bimodalize) 샘플링 효율과 일관성을 올리는 대신 **커버리지를 지불한다.** 그 비용을 단일 스칼라로 재는 진단 지표가 **Sharpening Tax**.
> 🎯 **[[하네스-설계-축]] 과 직결** — *"무엇을 모델에 넣고 무엇을 하네스에 둘 것인가"* 를 **커버리지라는 측정 가능한 통화로** 바꾼다. 그리고 저자 스스로 결론을 *"surprising"* 이라 적는다.

> [!insight] 🏆 볼트 PDF 열람 — **"논문 PDF 0건 15배치 연속" 한계가 16배치째 깨졌다**
> `https://arxiv.org/pdf/2610.01509` → **HTTP 200 · 8,156,988B(8.16MB) · PDF 1.7 · 62페이지** 획득 후 `pypdf` 로 **187,230자 추출**. arXiv 스탬프 **`arXiv:2610.01509v1 [cs.AI] 1 Oct 2026`** 확인 ⇒ publishedAt 2026-10-01 과 일치.
> ⚖️ **그래서 이 페이지의 아래 수치는 초록 인용이 아니라 본문 실측이다.** 📌 종전 15배치 동안 볼트는 초록만 봤고, 초록 대조는 *"수집기가 옳게 인용했는가"* 만 검증하고 *"주장이 참인가"* 는 검증하지 않았다.

## 🏆 PDF 가 드러낸 것 — 초록이 숨긴 설정

**① 테스트시 예산의 실제 값: pass@128**
초록은 *"given a sufficient test-time budget"* 이라고만 적는다. 본문 전수 집계: `pass@1` **59회** · **`pass@128` 37회** · `pass@K` 24회.
⇒ ⚖️ **"충분한 예산" = K=128 롤아웃이다.** 📌 **이것이 채택 판단을 바꾼다** — base 모델이 커버리지로 이기는 조건은 **128배 샘플링**이고, 그 비용은 후처리 모델 1회 호출과 비교 대상이 아니다. 🔴 **초록만 읽으면 "base 모델이 더 낫다"로 오독할 수 있다.**

**② 벤치마크 3종 중 2종 확인: BFCL · WebShop**
본문 언급 빈도 **BFCL 103회 · WebShop 97회**(+ GAIA 1회는 인용). 저자 서술: *"three representative basic benchmarks for agentic tasks"* / *"three agentic benchmarks that require **multi-turn tool calling** for final goal achievement"*.
🔴 **3번째 벤치 이름은 볼트가 확정하지 못했다**(빈도 집계에서 분리되지 않음 — 미확인으로 남긴다).

**③ 모델 계열 4종: Gemma-4 · Qwen2.5 · Qwen3.5 (+1 미확정)**
빈도 **Gemma/gemma-4 계열 105회 · Qwen2.5 42회 · Qwen3.5 36회** · Olmo 3 · Mistral 8 · DeepSeek 2.
🔴 **4번째 계열은 Olmo/Mistral/DeepSeek 중 어느 것인지 확정 불가**(빈도만으로 실험 대상과 인용을 구분할 수 없다).

**④ PTGS 의 적용 대상이 구체적이다**
초록은 *"two agentic environments"* 만 적는다. 본문: *"Plugged into common RL algorithms (**e.g., PPO and GRPO**), PTGS pays a …"* ⇒ **PPO · GRPO 양쪽에 꽂는 plug-and-play** 다.

> [!warning] 🔴 단위 불일치 — 같은 논문 초록 ↔ 본문 ([[단위-불일치]] 4번째 유형)
> **초록**: *"Across **14 base/post-trained model pairs** from four families and three agentic benchmarks (**42 cases** in total)"*
> **본문**: *"Across **14 model backbones** from popular open source model families and three representative basic benchmarks"*
> ⚖️ **"14 쌍(pairs)" 과 "14 백본(backbones)" 은 같은 수가 아니다.** 14쌍이면 모델 28개, 14백본이면 쌍은 7개다. 그리고 42 = 14×3 이므로 **42케이스는 "14 × 벤치 3" 이고 여기서 14는 쌍이어야 42가 맞는다** ⇒ 📌 **본문 쪽 "backbones" 표기가 느슨한 것으로 보이나, 볼트가 어느 쪽이 틀렸다고 단정하지 않는다.**
> ⚖️ **인용 규약: "14 base/post 쌍 × 3 벤치 = 42케이스" 를 쓴다. "14 백본" 단독 금지.**
> 📌 종전 3유형은 전부 **서로 다른 문서 간**(제목↔초록 등)이었다. **같은 논문의 초록↔본문 불일치는 처음이다.**

> [!warning] 🔴 PDF 를 열었는데도 핵심 수치는 여전히 봉인이다
> Sharpening Tax 의 **실제 값**을 찾아 본문 전수 검색했으나, 수치는 **Figure 6 · Figure 7 · Figure 26** 에 들어 있고 **본문 텍스트에는 없다**(*"Figure 6 reports both tax variants' values …"* · *"Figure 26 provides the full results"*).
> ⚖️ **그래서 [[벤치마크-이미지-봉인]] 이 재발했고, 이번은 성격이 다르다 — PDF 열람이 수치 봉인을 해제하지 못했다.** 📌 **이미지 안의 수치는 PDF 를 열어도 봉인이다.** 종전에는 "README 를 안 봐서" 봉인이었고 열면 풀렸다. **이번은 열었는데도 안 풀린다** ⇒ 🆕 **봉인 유형 2종으로 분해: "미열람형"(열면 풀림)과 "그림매장형"(열어도 안 풀림).**
> 🔴 **따라서 "tax 가 얼마인가"는 오늘도 모른다.** 알게 된 것은 *"가장 큰 백본에서는 거의 모든 k 에서 tax 가 양수"*(본문 523행) 라는 **방향 서술**뿐이다.

## 도메인별 추출 (local-llm · 후처리/하네스)

- **실용성 판단**: 🟡 **진단 지표로는 즉시 유용, 운영 전략으로는 비용 재계산 필요.** *"소수 롤아웃으로 추정 가능하고 다른 지표와 상관이 높다"*(초록) ⇒ **싼 측정으로 비싼 결론을 미리 안다**는 주장이다. 🔴 **그러나 "base 모델 + 하네스" 경로의 전제가 pass@128 이므로, 비용이 중요한 환경에서는 그 경로가 답이 아니다.**
- **🎯 볼트에 직접 걸리는 지점**: 본문이 에이전트 과제가 수학/코딩과 다른 이유를 **4가지로 분해**한다 — ① 구조화된 액션 실행 ② 시나리오별 인터페이스로 다양한 도구 호출 ③ 불확실성 하 이질적 환경 피드백 반영 ④ 장기 궤적 일관성 유지. ⇒ 📌 이것이 [[하네스-설계-축]] 의 **과제 쪽 분해**다. 볼트는 지금까지 축을 *제공자 쪽*(모델/하네스)으로만 쪼갰다 → [[암묵을-명시로]].
- **대체 관계**: 후처리를 대체하지 않는다. **후처리의 가격표를 붙인다.** 그리고 **PTGS 는 후처리를 더 싸게 만드는 쪽**(고정 온도 대신 난이도별 적응 온도)이다.
- **허와 실**: ✅ 42케이스 규모 · 저자 스스로 *"surprising"* 명시 · 단일 도메인 RL 튜닝도 tax 를 낸다고 추가 확인. 🔴 **tax 수치 전부 그림 매장** · 🔴 **pass@128 비용을 초록이 숨긴다.**
- **액션**: 📌 **구현체가 공개돼 있다 → 아래 참조.** 단 라이선스 제약이 있다.

> [!warning] 🔴 구현체 라이선스 — `NOASSERTION` 의 실체가 **CC BY-NC(비상업 금지)** 다
> HF API `githubRepo` = `https://github.com/changdaeoh/sharpening-tax` · **볼트 독립 실측 ★21**(HF 보고 19 = **+2 드리프트**) · fork 1 · created **2026-09-30** · pushed **2026-10-02** · **Python 108,627B + Shell 4,943B** · 루트 18항목(`CODE_OF_CONDUCT.md`·`CONTRIBUTING.md`·`pytest.ini`·`requirements-rollout.txt`·`ptgs/`·`configs/`·`examples/`) ⇒ ✅ **테스트 설정까지 있는 실체 있는 코드다.**
> 🔴 **그러나 `license` = `NOASSERTION` 이고 LICENSE 실체 열람(19,347B) 결과 1행이 `Attribution-NonCommercial 4.0 International` = **CC BY-NC 4.0**.
> ⚖️ **이것이 [[메타데이터-부재-추론]] 의 결론을 정정한다.** 볼트의 앞선 2사례([[openclaw]]·[[TileLang]])는 `NOASSERTION` → **실체 MIT**(허용적)였다. **3번째는 실제로 제한적이다.** ⇒ 📌 **`NOASSERTION` 은 라이선스 성격에 대한 정보가 0이다. 2/2 가 MIT 였다고 "서식 문제"로 일반화하면 틀린다 — 열어 봐야만 안다.**
> 🎯 **원인 추정(사실로 적지 않는다)**: 코드 저장소에 **소프트웨어용이 아닌 CC 라이선스**를 썼기 때문에 GitHub 탐지기의 SPDX 매칭이 실패한 것으로 보인다.
> 🔴 **실용 파급**: **상업적 사용 금지**다. 볼트가 실험용으로 읽는 것은 가능하나 제품에 넣을 수 없다.

> [!action] 당장 할 것
> `changdaeoh/sharpening-tax` 를 clone 해 **`ptgs/` 모듈만 읽는다**(PTGS 는 *plug-and-play 베이즈 샘플러*라 단독 이해가 가능하다). 목표는 **tax 수치가 코드/설정에 하드코딩돼 있는지** 확인해 **그림 매장 봉인을 코드로 우회**하는 것. 🔴 **CC BY-NC 이므로 읽기·실험까지만.**

> [!question] 미해결 질문
> - 3번째 벤치마크 이름 · 4번째 모델 계열은 무엇인가(PDF 표 추출 필요).
> - tax 의 실제 수치 범위는? (Figure 6/26 — 그림 매장)
> - 🎯 **같은 배치 [[On-Policy-or-Off-Policy-Distillation]] 의 *"RLVR 이후 온폴리시 이점이 유지되지 않는다"* 와 이 논문의 *"후처리가 커버리지를 깎는다"* 가 같은 현상인가?** 두 논문은 서로를 인용하지 않는다(같은 날 게시).

## 관련 페이지
- [[On-Policy-or-Off-Policy-Distillation]] — 같은 배치 · 커버리지를 같은 통화로 사용
- [[HC-DLM]] · [[Beyond-Memory-PoS]] · [[Adaptive-Reward-Routing]] — 같은 배치
- [[하네스-설계-축]] — 이 논문이 측정 통화를 제공
- [[단위-불일치]] · [[벤치마크-이미지-봉인]] · [[메타데이터-부재-추론]] · [[선언된-구현체-공백]] · [[암묵을-명시로]]
- [[local-llm]] · [[Meta]]

## 원본
- 출처: https://huggingface.co/papers/2610.01509
- PDF: https://arxiv.org/pdf/2610.01509 (**볼트 열람 완료** · 8.16MB · 62p)
- 구현체: https://github.com/changdaeoh/sharpening-tax (★21 · **CC BY-NC 4.0**)
- 프로젝트: https://changdaeoh.github.io/sharpening-tax/
- **볼트 독립 검증**: upvote **69** ✅(수집기 일치) · publishedAt **2026-10-01** ✅ · 저자 **10명** ✅ · 초록 **1,689자**
- 🏆 **저자 소속이 API 보고보다 많다**: HF `organization` = **Meta** 단일이나 PDF 실측은 **Meta Superintelligence Labs · University of Wisconsin–Madison · NYU · Stanford University 4개 기관**. 제1저자 **Changdae Oh**(Meta+UW–Madison) · **Azalia Mirhoseini**(Stanford) · **Sharon Li**(UW–Madison) 포함. ⇒ 📌 **`organization` 필드는 제1저자 소속 1개만 반영한다** → [[복합지표-분해]] 와 동형(단일 필드가 다수를 숨긴다).
- 10-02 게시분 **upvote 6위**
- 신뢰도: ⭐⭐⭐⭐⭐ (42케이스 규모 · PDF 실측 · 구현체 실체 확인 / 🔴 tax 수치 그림 매장 · 비상업 라이선스)
