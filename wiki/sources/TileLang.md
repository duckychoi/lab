---
title: "TileLang — 커널을 파이썬으로 쓰는 DSL, 그리고 NOASSERTION 이 두 번째로 MIT 였다"
type: source
domain: ai-news
tags: [ai-news, github-trending, kernel-dsl, tvm, gpu, npu, ascend, compiler, 벤치마크-이미지-봉인, 메타데이터-부재-추론, 저수준축]
created: 2026-10-02
updated: 2026-10-02
sources: []
reliability: high
---

# TileLang — GPU/CPU/NPU 커널용 Pythonic DSL (TVM 기반)

**GitHub**: https://github.com/tile-ai/tilelang
**지표(수집 2026-10-02 09:00:58 UTC / 볼트 실측 동일자)**: ⭐**8,185**(수집기 8,183 → 드리프트 **+2**) · fork **822**(**완전 일치**) · open_issues **386**(**완전 일치**) · 라이선스 메타 **NOASSERTION** · Python · created **2024-10-03** · pushed **2026-09-30** · 당일 +163 · 랭크 11위
**볼트 지위**: 🆕 **신규** — 정규명 재검사에서도 index/log 언급 0회

> [!insight] 🎯 핵심 인사이트 — **볼트가 2년 가까이 수집해 온 축 중 가장 아래층이 처음 들어왔다**
> 볼트의 ai-news 수집은 **에이전트 하네스**([[pi-agent-harness]]·[[OpenShell]]·[[paperclip]])와 **모델**([[Qwen-Image-2.1]]·[[Nemotron-3-Diarization]])에 쏠려 있었다. TileLang 은 그 아래 — **커널 컴파일러** 층이다. 하네스가 "모델을 어떻게 감싸는가"라면 이것은 "행렬곱이 실제로 어느 명령어로 내려가는가"다.
> 📌 **[[하네스-설계-축]] 의 바닥이 하나 더 생겼다.** 09-18 에 4층(SDK·자동탐색·대조실험·학습루프), 09-30 에 [[OpenShell]] 로 "격리·감사" 층이 붙었고, 오늘은 **그 아래 "커널 생성" 층**이다. 이 축은 위로만 자라는 줄 알았는데 **아래로도 자란다**.
> 🎯 **이 저장소의 성격은 커밋 단위가 하드웨어라는 것이다** — SM75 MMA(FP16/INT8/INT4) · Blackwell SM100 MXFP8 · SM120 NVFP4 블록스케일 · Apple M5 협동텐서 GEMM · TMA gather/scatter · 클러스터 복사가 **각각 개별 PR 로 축적**된다. 즉 **기능 목록이 곧 하드웨어 연대기**다.

> [!insight] 🏆 **볼트 자체 발견 — `NOASSERTION` 을 열었더니 1행이 `MIT License` 였다. 두 번째 사례다.**
> 수집기는 *"라이선스 `NOASSERTION` 실체(LICENSE 파일 미열람)"* 로 미확인 남겼다. 볼트가 열었다.
> ```
> GET raw.githubusercontent.com/tile-ai/tilelang/main/LICENSE
>   → HTTP 200 · 1,283 바이트 · 23행
>   1행: "    MIT License"
>   3행: "    Copyright (c) Tile-AI."
> ```
> 🔴 **그런데 원인이 [[openclaw]] 와 다르다.** openclaw(10-01)는 **말미 2행의 THIRD_PARTY_NOTICES 참조** 때문에 탐지기가 포기했다. TileLang 은 두 가지가 겹쳤다 —
> 1. **전체 23행이 4칸 공백으로 들여쓰기**돼 있다(`    MIT License`). 표준 MIT 텍스트의 행머리 일치가 깨진다.
> 2. **4~5행에 비표준 조항이 삽입**돼 있다: *"**During the period from December 1, 2024, to Mar 14, 2025, this project is subject to additional collaboration terms with Microsoft Corporation.**"* — 마크다운 `**` 강조까지 파일 안에 들어가 있다.
> ⇒ **[[메타데이터-부재-추론]] 신규 하위유형: 서식(들여쓰기)과 삽입 조항이 탐지기를 실패시킨다.** openclaw 는 *꼬리*, TileLang 은 *머리와 몸통*이다.
> ✅ **실용 결론 — 삽입 조항의 유효기간이 이미 지났다.** 2024-12-01 ~ 2025-03-14 는 **오늘(2026-10-02) 기준 1년 7개월 전에 종료**됐다. 따라서 현재 이 코드는 **추가 조항 없는 순수 MIT** 로 읽는 것이 문서상 타당하다. 🔴 단 볼트는 법률 판단을 하지 않는다 — **문서가 그렇게 적혀 있다는 사실만 기록한다.**

> [!warning] 🔴 벤치마크를 인용할 수 없다 — [[벤치마크-이미지-봉인]] 재발
> README 217~247행 *"Benchmark Summary"* 절이 **전부 이미지 파일**(`op_benchmark_consistent_gemm_fp16.png` 등)이고 본문에 수치 텍스트가 없다. 텍스트로 확인되는 정량치는 **DeepSeek V3.2 top-k 최적화 ≈1.9배** 1건뿐이며, 이것도 *"reported benchmark"* 라는 **자기 인용**이다.
> 📌 **이 개념(09-26 신설)이 오늘 두 축에서 동시에 재발했다** — 여기와 [[Qwen-Image-2.1-Uncensored-GGUF]](카드 Benchmark 절이 이미지 1장). **커널 컴파일러와 이미지 모델이라는 완전히 다른 도메인에서 같은 형태**로 나타난 것은, 이것이 분야 관행이 아니라 **README/모델카드라는 매체의 속성**임을 시사한다.
> 🔴 **그래서 TileLang 의 성능 주장은 오늘 하나도 검증되지 않았다.** 존재·활력·라이선스는 확인됐고 **속도는 확인되지 않았다.**

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐**8,185** 로 기준선(1,000+) 통과 · **실측 MIT**(메타 NOASSERTION 교정) · created 2024-10-03 으로 **약 2년** — 오늘 GitHub 5건 중 **가장 오래된 저장소**다. 2년간 ★8,185 는 폭발이 아니라 **누적**이고, 당일 +163(증분 하위)이 그것과 일관된다.
- **즉시 활용**: 🔴 **NO.** 볼트는 커널을 쓰지 않는다. **단 간접 경로가 있다** — TileLang 의 백엔드 목록(CUDA·ROCm·Metal·LLVM CPU·WebGPU·**Ascend 950 NPU**)은 `local-llm` 도메인의 *"어떤 하드웨어에서 돌리나"* 질문에 직접 답하는 지도다. **읽을 가치는 코드가 아니라 백엔드 표에 있다.**
- **6개월 영향력**: NVIDIA 외 가속기(Ascend·Apple M5)에서 **커널을 손으로 안 쓰고 얻는 경로**가 성숙하면, 로컬 추론의 하드웨어 선택지가 넓어진다. 🔴 단 오늘 확인된 것은 *"지원한다고 적혀 있다"* 까지다.
- **대체 관계**: Triton(OpenAI) 과 같은 자리를 노리나 **TVM 인프라 위에 올라탄 점**이 다르다. 🔴 Triton 대비 수치 비교 **README 에 0건**.
- **허와 실**: 확인 = ★8,185 · MIT(실측) · 백엔드 6종 명시 · 디버깅 도구 5종(Pass Visualizer·IR Lower Trace·Pass Diff·소스 위치 진단·LSP) · 2년 누적. **미확인 = 모든 성능 수치 · Triton 대비 · open_issues 386 의 PR 비중**([[복합지표-분해]] 미적용) · DeepSeek V3.2/V4 예제 실측.
- **액션**: 백엔드 지원 표만 발췌해 `local-llm` 도메인 하드웨어 지도에 반영(actionable 등록). 커널 작성은 **하지 않는다** — 볼트 용도가 아니다.

## 관련 페이지
- [[하네스-설계-축]] — 이 소스가 추가하는 최하층("커널 생성")
- [[메타데이터-부재-추론]] — `NOASSERTION` 2번째 사례 · **신규 하위유형(서식·삽입조항)**
- [[벤치마크-이미지-봉인]] — 재발 · [[openclaw]] — `NOASSERTION` 1번째 사례
- [[복합지표-분해]] — open_issues 386 미분해
- [[OpenShell]] · [[ponytail]] · [[pi-agent-harness]] · [[UniMate]] — 같은 배치 GitHub 동시 관측
- [[local-llm]] — 백엔드 표의 활용처

## 원본
- 출처: https://github.com/tile-ai/tilelang
- 신뢰도: ⭐⭐⭐ (★8,185 · 실측 MIT · 2년 누적 / 🔴 성능 수치 0건)
- 검증: 2026-10-02 GitHub REST API 실호출 — ★+2 드리프트 · **fork·issues 완전 일치** · 생성일 일치 · **LICENSE 원문 23행 직접 열람(봉인 해제)**
