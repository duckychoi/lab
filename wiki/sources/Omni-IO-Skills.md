---
title: "Omni-IO Skills — 오늘 논문 중 수치가 가장 많은데 upvote는 가장 낮다"
type: source
domain: ai-news
tags: [ai-news, hf-paper, arxiv, harness, agent-skills, multimodal, omni, asset-registry, 하네스-설계-축, 에이전트-스킬]
created: 2026-09-30
updated: 2026-09-30
sources: []
reliability: high
---

# Omni-IO Skills: Harnessing Your Agent Omni-Native

**HF 논문**: https://huggingface.co/papers/2609.31847 · **arXiv**: 2609.31847
**지표(2026-09-30)**: upvote **57**(수집기 09:04 관측 52 대비 **+5** · 볼트 09:13 실측) · 데일리 5위 · 공개 **2026-09-25**(수집기 일치)

> [!insight] 🏆 핵심 인사이트 — **모델을 갱신하지 않고 모달리티를 늘린다**
> 초록 원문: *"**Extending a foundation model to additional modalities ties capability growth to costly model updates**, while assembling specialist models and tools leaves unresolved how procedures, dependencies, intermediate assets, and cross-turn revisions should be coordinated."*
> 📌 **[[하네스-설계-축]] 의 정의를 가장 선명하게 실증한 오늘의 소스다.** 그 축의 한 줄은 *"모델을 바꾸지 않고 감싸는 층만 바꿔서 정확도·비용을 움직인다"* 였다. 이 논문은 **그 층으로 "능력 자체(입력 지원 모달리티)"를 늘린다** — 정확도·비용이 아니라 **커버리지**를 움직였다. 축의 적용 범위가 넓어졌다.
> 구성 4종(초록 실측): **계층적 Skills** · **표준화된 멀티모달 실행 인터페이스** · **의존성 인식 오케스트레이션** · **영속 Asset Registry**.
> 🎯 **볼트가 주목할 자료구조는 Declare Execution Graphs 다** — *"Multi-asset workflows are represented as **Declare Execution Graphs**, which **schedule independent operations concurrently** and **register successful outputs for downstream and cross-turn reuse** across **replaceable execution backends**."* 🔴 **수집기가 이 이름을 옮기지 않았다**(볼트 원문 대조로 확보 — 누락 보완).

> [!insight] ✅ 오늘 논문 5건 중 **수치 최다** — 수집기 인용 전건 일치 + 볼트 보완 2건
> ✅ **수집기 보고 전부 원문과 일치**(볼트 arXiv 직접 대조):
> - 입력 지원률: **GPT-5.6 Sol 40.00% → 100%** · **Claude Sonnet 5 38.89% → 100%**
> - 상대 SQCS(Semantic–Quality Coupled Score): **26.99 → 74.94** · **27.82 → 77.78**
> - **Strict Structure Score 100.00 · 99.78**
> - **27 Skills · 38 태스크 · 7 모달리티**
> 🎯 **볼트 보완 ①**: 초록은 능력을 **4계열(capability families)** 로 분류한다 — *"understanding, generation, reasoning, and retrieval"*. 수집기가 *"7 모달리티"* 는 옮겼으나 **4계열은 빠뜨렸다.** 38개 태스크의 축이 둘(모달리티 7 × 계열 4)이라는 점이 커버리지 주장의 구조다.
> 🎯 **볼트 보완 ②**: 모달리티 7종의 내역이 초록 첫 문장에 있다 — *"text, images, audio, video, documents, 3D assets, and code"*. **3D assets 와 documents 가 포함**된다는 것이 볼트에 중요하다([[slam-3dgs]]·문서 RAG 축과 직접 접점).
> 📌 **입력 지원률 40.00% → 100% 는 "정확도 개선"이 아니라 "받을 수 있게 됨"이다.** 두 수치를 같은 종류로 읽으면 과대해석이 된다 — 100%는 **완주율이 아니라 입력 수용률**이다. SQCS(26.99→74.94)가 품질 축이고, 이쪽은 100%가 아니다.

> [!warning] 🎯 **upvote와 검증가능성이 역상관이다 — 오늘 배치가 이걸 두 끝에서 보여 준다**
> ```
> 논문                     upvote(09-30 실측)   초록 정량 수치
> ──────────────────────────────────────────────────────────
> [[Raven]]                254 (1위)           🔴 0개
> [[MaLiang-Harness]]      189 (2위)           ✅ 5개
> [[PanoVLN]]               88 (3위)           ✅ 2개
> [[Simple-WAM]]            55 (4위)           🔴 0개
> Omni-IO Skills            57 (5위→4위)        ✅ 7개 (최다)
> ```
> 🔴 **1위(254)가 수치 0개이고, 수치 최다(7개)가 최하위권이다.** 볼트가 [[벤치마크-이미지-봉인]] 계열에서 본 *"근거를 감추면 오히려 잘 팔린다"* 와 같은 방향이지만, 여기서는 **감춘 게 아니라 아무도 안 봤다**. 관심 지표를 품질 대리지표로 쓰면 **정확히 거꾸로 간다** → [[측정도구-먼저-반증]].
> ✅ **수집기의 동점 판정이 하루 뒤 옳았음이 확인됐다**: 수집기는 *"VoxMem(2609.32607)과 52 동점 — HF 자체 정렬로 본건 선발, VoxMem 미선발"* 이라고 자기 선발 근거를 밝혔다. **09-30 09:13 실측: Omni-IO 57 · VoxMem 52.** 동점이 **Omni-IO 쪽으로 풀렸다** — 수집기 선택이 사후 검증됐다. 🎯 **자기 선발 규칙을 적어 둔 덕분에 검증이 가능했다** → [[자기제한-명시]].

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐⭐⭐ **높음.** arXiv 게재 · 초록 수치 7개 · 벤치명(UniM-90) 명시 · 평가 대상 모델명 2종 명시(GPT-5.6 Sol · Claude Sonnet 5). 🔴 단 **UniM-90 이 자체 제작 벤치인지 미확인**(초록에 출처 없음 — 자체 제작이면 [[Qwen3.8-27B]] 사내 벤치 문제와 같은 계열).
- **즉시 활용**: **YES(개념), 조건부(코드).** Asset Registry + Declare Execution Graph 패턴은 볼트의 다단 생성 파이프라인([[reat-render]] 계열)에 **지금 설계로 반영 가능**하다 — 중간 산출물을 등록해 후속·턴간 재사용하는 구조가 정확히 볼트에 없는 것이다. 🔴 저장소 URL 초록에 없음.
- **6개월 영향력**: 크다. *"모델 갱신 없이 옴니모달화"* 가 성립하면 **모델 선택보다 하네스 선택이 능력을 결정**한다. 볼트의 모델 추적 방식(DL·★ 중심)이 **하네스 추적으로 이동해야 할 근거**다.
- **대체 관계**: [[에이전트-스킬]] 계열을 **표준 인터페이스 축에서 강화**. 개별 도구 호출을 Skill 계층으로 흡수한다.
- **허와 실**: 🎯 **오늘 5건 중 허가 가장 적다.** 수치·벤치·대상모델·규모가 전부 초록에 있고, 100%의 의미(입력 수용률)도 문장으로 구분 가능하다. **남은 허 = UniM-90 출처 미확인 · 저장소 미확인.**
- **액션**: Declare Execution Graph + Asset Registry 설계 차용(actionable 등록, 우선순위 높음 — 오늘 5건 중 **즉시 적용 가능성이 가장 높다**).

## 관련 페이지
- [[하네스-설계-축]] — 축의 적용 범위를 "커버리지"로 확장
- [[에이전트-스킬]] — 계층적 Skills 연결점
- [[Raven]] — 같은 배치, upvote 1위/수치 0개 대조군
- [[MaLiang-Harness]] — 같은 배치 하네스 논문(생성 검증)
- [[측정도구-먼저-반증]] — upvote↔검증가능성 역상관
- [[자기제한-명시]] — 수집기 동점 선발 근거 명시가 사후 검증을 가능하게 했다
- [[Qwen3.8-27B]] — 자체 벤치 문제 계열(UniM-90 미확인 항목)

## 원본
- 출처: https://huggingface.co/papers/2609.31847 · arXiv 2609.31847
- 신뢰도: ⭐⭐⭐ (upvote 57 · **초록 수치 7개로 오늘 최다** · 전건 원문 일치)
- 검증: 2026-09-30 09:13 UTC arXiv 원문 직접 열람(42,441 바이트) — 수치 전건 일치 · **볼트 보완 2건**(4 capability families · Declare Execution Graphs · 모달리티 7종 내역)
