---
title: FreeToken — Edge-Native MoE Serving with Bandwidth-Adaptive Execution (HF 논문)
type: source
domain: local-llm
tags: [ai-news, local-llm, edge-ai, moe, serving, bandwidth-adaptive, on-device, hf-paper]
created: 2026-08-19
updated: 2026-11-03
sources: []
reliability: medium
---

# FreeToken — 대역폭 적응 실행으로 엣지 MoE 서빙

**HF 논문**: https://huggingface.co/papers/2608.16157
**지표**: 업보트 **37** (2026-08-19 HF 데일리 **2위**) · **도메인**: local-llm(교차 ai-news)

> [!insight] 핵심 인사이트
> **엣지 디바이스에서 MoE(전문가 혼합) 모델을 서빙**하되, 가용 **대역폭에 적응해 실행 경로를 조정(bandwidth-adaptive execution)**해 효율을 끌어올리는 방법. MoE는 파라미터 총량 대비 활성 파라미터가 작아 온디바이스에 유리하지만, **전문가 가중치 로딩·라우팅의 메모리·대역폭 병목**이 실배포의 실질 장벽이다 — FreeToken은 바로 그 병목을 실행 시점에 적응시키는 접근으로 읽힌다. 같은 배치 로컬 실행 계층 [[omlx]](Apple Silicon·SSD 캐싱)·양자화 웨이트([[Qwen3.8-27B-FP8]]·[[Qwen3.8-27B-GGUF]])와 함께 **"대형 모델을 엣지·로컬에서 굴리는" 축**을 보강한다.

> [!warning] 신뢰도 — 미래형 arxiv ID·수치 미검증 (medium)
> arxiv ID **2608.16157**은 미래형으로 **원문 초록·처리량/지연 수치·평가 하드웨어를 재현할 수 없다**(실WebFetch 미수행). 업보트 37·데일리 2위는 raw 순위 지표. "대역폭 적응 실행"의 구체 메커니즘(오프로딩 스케줄링? 전문가 프루닝? 캐싱?)은 **미기재 → 원문 재현 전 미검증**([[CLAUDE.md]] 사실확인 원칙).

## 도메인별 추출 (local-llm)

- **실용성 판단**: 잠재 높음 — 엣지 MoE 서빙 효율은 로컬 LLM 실배포의 핵심 난제. 단 구현체·재현 코드 공개 여부 미확인.
- **메모리 아키텍처**: 대역폭을 변수로 둔 적응 실행 — [[omlx]]의 SSD 캐싱(대역폭 병목 트레이드오프)과 문제의식이 정확히 겹침. 오프로딩·티어드 로딩 계열로 추정(미확정).
- **Hermes 적용**: 직접 적용은 거리가 있으나, 로컬 MoE를 저사양에서 굴릴 때의 서빙 전략 참고.
- **트레이드오프**: 대역폭 절감 vs 적응 오버헤드·품질 손실 — 수치 미기재로 판정 불가.
- **오픈소스 구현체**: 미확인. 공개 시 [[local-llm]] 엣지 서빙 레퍼런스 후보.

## 관련 페이지
- [[omlx]] — 같은 배치, 대역폭·캐싱 병목 문제의식 공유(Apple Silicon 서빙)
- [[Qwen3.8-27B-FP8]] — 같은 배치, 엣지/서버 메모리 절감 양자화 웨이트
- [[에이전트-메모리-레이어]]
- [[local-llm]]

## 원본
- 출처: https://huggingface.co/papers/2608.16157
- 지표: 업보트 37 (2026-08-19 HF 데일리 2위)
- 신뢰도: ⭐⭐ (미래형 arxiv ID·원문 미재현·수치 미검증 medium·raw 자동수집)
- 수집: 2026-08-19 아침 자동수집 (HF 논문)

## 🔄 2026-11-03 갱신 (인제스트 2026-11-03) — ★16,352 · **논문 구현체가 실존(Apache-2.0) · RTX 5090 77–83 tok/s 확인, 단 6스레드 제한 '렌트 서버' 측정**

> [!note] 이 페이지의 첫 GitHub 기록
> 08-19 본문은 HF 논문만 보고 *"구현체·재현 코드 공개 여부 미확인"* · *"arxiv 원문 미재현"* 으로 남겼다. 오늘 둘 다 해소한다.

**GitHub API 실측(11-03 09시대)**: `FlashML-org/FreeToken` ★**16,352**(수집기 16,349 · +3) · fork **1,603** ✅ · open_issues **469** · Apache-2.0 ✅ · Python ✅ · created 2026-07-20 · pushed 2026-11-03T05:29Z · 릴리스 **v0.2.1(10-26)** · v0.2.0(10-21) · v0.1.3(09-16) · v0.1.2(**08-19**, 논문 HF 데일리와 같은 날) · `nightly`(롤링, 매일 덮어씀)
- 📈 볼트 기존 기록은 GitHub 수치 없음(HF upvote 37 · 08-19). HF API `api/papers/2608.16157` 현재 **upvotes 112** · `githubRepo` = 이 레포로 연결됨.
- ✅ **arXiv 원문 대조**(abs·HTML 직접 조회 · v1 2026-08-17 제출 · 저자 Yang·Keutzer·Han·Zaharia·Stoica 등):
  - "RTX 5090에서 **Qwen3.6-35B-A3B 77–83 tok/s · DeepSeek-V4-Flash 22–25 tok/s**, 최선 비교군 대비 디코드 **1.5–2.3배**" ✅ 축자 일치. 세부: Qwen3.6 **1.8–2.3×** · DSV4-Flash **1.5–1.9×**(각 워크로드의 strongest baseline 기준).
  - "멀티턴 디코드 감소 12% 이내" ✅ · "최악 TTFT 44초 미만, 비교군은 각자 ≥1개 설정에서 150초 초과" ✅ — 비교군 최악값 llama.cpp **232s** · Ollama **179s** · KTransformers **946s**.
  - 8GB 노트북 35B · 게이밍 데스크톱 284B · 워크스테이션 1장 753B GLM-5.2 ✅(초록). 노트북 수치 **RTX 4060 Laptop 39.3 tok/s**(NVFP4) · 5개 소비자 기기 전반 **1.3–2.1×**.
  - "초록에는 tok/s 수치가 없다" ✅ — arXiv abs 페이지 초록 0건, HTML 본문(서론·§5)에만 있다.
- ⚖️ **수집기 누락(핵심) — 77–83 tok/s는 '소비자 PC'가 아니다**: §5.1 *"The 3090, 4090, and 5090 systems are **rented dual-socket servers** whose CPUs far exceed any edge host, so every serving run … is **capped at 6 CPU threads** and pinned to the GPU's NUMA node"* — 표 1의 "5090" 행은 **2× Xeon Gold 6459C · DDR5 180GB**. 실제 소비자 기기(5090 desktop = Ryzen 9 9950X3D · 4060 laptop)는 에뮬레이션 검증용이며, 논문은 5090 서버→데스크톱 이동 시 FreeToken **−4%**, llama.cpp는 **80%만 유지**라고 적는다(즉 실기기에서 격차는 오히려 커진다는 저자 주장 · 5090 desktop 2.1×). ⇒ 헤드라인 수치는 **에뮬레이션 조건**이고 실기기 결과는 별도 열이다 → [[배수-조건분산]].
- ⚖️ README 대 논문 불일치: README 14행 *"Run **290B+** frontier MoE models locally on your gaming PC at **blistering interactive speeds**"* — 논문은 게이밍 데스크톱 **284B**(DeepSeek-V4-Flash, 활성 13B). README 본문(raw 86행)에 tok/s 수치 **0건**. → [[한정어-탈락]](284B → "290B+", "interactively" → "blistering").
- ✅ 수집기 서술 확인(README 18~22행): 대역폭 적응형 CPU–GPU 공동실행($q^\star$ 정책) · 전역 LRU 전문가 캐시 · 시맨틱 앵커 체크포인트 · 무재시작 VRAM 재할당 · Anthropic/OpenAI 호환 API · RTX 30/40/50. v0.2.1 = GGUF mmproj 이미지 입력 · `deepseek4` 아키텍처 ✅.
- ⚖️ 수집기 누락(릴리스): v0.2.1 `--embed-weights host` **디코드 +8.7%**(Qwen3.6-35B-A3B · 여유 VRAM 24GiB) · v0.2.0 llama.cpp GGUF 직접 서빙(ggml 커널 벤더링) · NVFP4 W4A4로 MoE 레이어 RTX 5090 **3.72×**(≥128 tok/expert). 전부 저자 보고.
- 🛠 사고·보안 공개: **0건**(v0.2.1·v0.2.0·nightly 노트 확인). 단 `docs/ftw-hotfix.md` — *"구 빌드로 변환한 FTW 체크포인트가 현 빌드에서 로드 실패할 수 있다"* 며 수리 스크립트 제공(GLM-5.2 router bias·Qwen3.8-Flash-Next PLE 테이블 47.7GiB 누락 등). 체크포인트 포맷 호환성 파손이 반복됐다는 기록이다.
- 출처 보강: README Acknowledgment — mini-sglang에서 영감, SGLang·vLLM·FlashInfer·fla·LightLLM·llama.cpp 코드 재사용 명시.

> [!insight] "엣지 MoE"의 속도 수치는 엣지가 아닌 곳에서 쟀다 — 그리고 저자가 그걸 숨기지 않았다
> 논문은 서버 CPU를 6스레드로 묶어 소비자 대역폭(56.7–77.3 GB/s)을 흉내 냈고 실기기 2대로 검증했다고 **본문에 적었다.** 문제는 그 다음 단계 — 수집기 요약과 README가 "RTX 5090 77–83 tok/s"·"gaming PC 290B+"로 **조건을 떼고** 옮긴다. 실기기 기준 인용은 "4060 노트북 39.3 tok/s(35B NVFP4)" · "5090 desktop에서 최선 비교군 대비 2.1×(W2)" 쪽이 정확하다. [[ktransformers|KTransformers]] · [[omlx]] 와 같은 오프로딩 축의 첫 **구현+논문 동시 보유** 사례.

- **실용성(재판정)**: 🟡 → **조건부 가능**. RTX 30/40/50 + Linux x86_64(nightly는 CPython 3.12·CUDA 13.0 휠). 볼트 서버엔 GPU 없음 → 실행 불가. 데스크톱 앱(Windows/Linux)은 flashml.ai 배포. 코드 미실행.
- **수집기 평가**: 수치 인용은 축자 정확. 누락 = 에뮬레이션 측정 조건 · README "290B+" 과장 · open_issues 469.
- 관련: [[DeepSeek-V4-Flash]] · [[Qwen3.6-35B-A3B]] · [[GLM-5.2]] · [[local-llm]]
