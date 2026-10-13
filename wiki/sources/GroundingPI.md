---
title: "GroundingPI — 볼트가 '34개 벤치'를 열었더니 고유 데이터셋은 22개였다"
type: source
domain: slam-3dgs
tags: [slam-3dgs, hf-papers, grounding, vla, 임바디드-AI, 자율주행, 로봇조작, xpeng, 단위-불일치, 복합지표-분해]
created: 2026-10-13
updated: 2026-10-13
sources: []
reliability: high
---

# GroundingPI — 금일 유일하게 수치를 가진 논문, 그리고 그 수치의 분모가 부풀어 있다

**HF Papers**: https://huggingface.co/papers/2609.39601
**업보트 96**(수집기 92 → 볼트 재조회 **+4**) · 저자 **26명** · published **2026-09-30** · submittedOnDaily **2026-10-13**
🆕 **볼트가 수집기 미수집 메타데이터 4건을 발굴**: 소속 **XPENG AI**(샤오펑) · projectPage `groundingpi.github.io` · githubRepo `groundingpi/GroundingPI` · linkedModels 1 · linkedSpaces 3

> [!info] 🔄 **도메인 재판정 — 수집기 `ai-news` → 볼트 `slam-3dgs`**
> 근거: 평가 대상이 **RoboTwin 2.0**(로봇 조작 OOD 4설정) · **RoboCasa-GR1**(시연 효율) · **nuScenes**(자율주행 오픈루프 L2 **0.296m**) 이고, 자기 규정이 *"foundation models of **physical intelligence**"* 다.
> 📌 선례 준수: 2026-10-12 에 [[Reflex]](cs.RO)를 같은 사유로 `ai-news → slam-3dgs` 재배치했다. **본 건은 그 2번째 적용이다.**

> [!insight] 🏆🏆 **최대 발견 — "34개 벤치 평균 73.68%"의 34는 데이터셋 수가 아니라 (데이터셋 × 과제형식) 엔트리 수다**
> 수집기가 미확인으로 남긴 *"34개 벤치 목록"* 을 볼트가 **GitHub `eval/README.md` 원문(10,430 B)으로 뚫었다.** 전문 표:
> | 태스크 그룹 | 엔트리 | 벤치 구성 |
> |---|---:|---|
> | Detection | 4 | COCO · LVIS · Dense200 · VisDrone |
> | Referring boxes | 6 | RefCOCOg val/test · RefCOCO · RefCOCOg · RefCOCO+ · HumanRef |
> | Object pointing | 7 | RefCOCOg val/test · COCO · LVIS · Dense200 · VisDrone · HumanRef |
> | Spatial pointing | 4 | RefSpatial Location/Placement/Unseen · RoboSpatial Context |
> | GUI grounding | 3 | ScreenSpot-Pro · ScreenSpot-V2 · OSWorld-G |
> | OCR | 4 | HierText · ICDAR2015 · TotalText · SROIE |
> | Document layout | 2 | DocLayNet · M6Doc |
> | Visual prompting | 4 | FSC147 · Dense200 · COCO · LVIS |
> ✅ **볼트 검산 통과**: 4+6+7+4+3+4+2+4 = **34** — 초록의 "34 grounding benchmarks" 와 **정확히 일치**.
> 🔴🔴 **그런데 고유 데이터셋을 세면 22개다.** 재등장: **RefCOCOg 5회** · **COCO 3회** · **LVIS 3회** · **Dense200 3회** · VisDrone 2회 · HumanRef 2회.
> 🎯 ⇒ **COCO 하나가 Detection·Object pointing·Visual prompting 3개 엔트리로 평균에 3번 들어간다.** 📌 **따라서 73.68% 는 "34개 서로 다른 벤치의 평균"이 아니라 "22개 데이터셋에 중복 가중된 34개 엔트리의 평균"이다.**
> 🆕 **볼트 규약 제안: 벤치 개수를 인용할 때 "엔트리 수"와 "고유 데이터셋 수"를 분리해 적는다.** → [[단위-불일치]] **신규 축** · [[복합지표-분해]]
> ⚖️ **이것이 부정행위라는 뜻은 아니다.** 같은 데이터셋을 박스·포인팅·비주얼프롬프트로 **다른 과제 형식**으로 쓰는 것은 그라운딩 평가에서 정당하다. 🔴 **문제는 "34개 벤치"라는 표기가 그 구조를 숨긴다는 것이다.**

> [!warning] 🔴 **초록의 "11 perceptual capabilities" ↔ 평가 스위트의 8 태스크 그룹 — 수가 안 맞는다**
> 초록: *"34 grounding benchmarks spanning **11 perceptual capabilities**"*. 그러나 볼트가 연 `eval/README.md` 의 과제 분류는 **8개 그룹**이다(위 표).
> ⇒ ⚖️ **가능한 해석 2가지이고 볼트는 확정하지 못했다**: ① 11 은 8 그룹을 더 잘게 쪼갠 것 ② 논문 본문과 공개 스위트의 분류 체계가 다르다.
> 📌 **추정을 사실로 적지 않는다** — 미해결로 올린다.

> [!insight] 🆕 **볼트 신규 — "4B 그라운딩 모델"의 정체가 README 에서 드러났다(초록에 없는 정보)**
> `README.md` 265행 원문: *"GroundingPI combines a **MoonViT-V2 (Kimi K3)** visual encoder, a learnable multimodal projector, and a **Qwen3-4B** language backbone."*
> 🎯 ⇒ **자체 설계가 아니라 기존 공개 부품의 조립이다**: Kimi 계열 비전 인코더 + Qwen3-4B 언어 백본.
> 📌 **이것이 평가에 미치는 함의**: 비교 대상 **GPT-6 Astra(71.54%)** 는 범용 모델이고 본 모델은 **그라운딩 전용 후학습**이다 ⇒ **"더 작은 모델이 더 큰 모델을 이겼다"는 서사는 맞지만, 전용화 대 범용의 비교**다. → [[특화-역류]] · [[비매칭-비교]]
> ⚖️ 초록의 *"the larger GPT-6 Astra"* 는 **파라미터 수를 밝히지 않는다**(4B 대 ?B). 배수를 모르면 "작은데 이겼다"의 강도를 정량화할 수 없다.

> [!warning] 🔴🔴 **SOTA 주장과 관심도가 정반대다 — GitHub ★24**
> 볼트 GitHub API 실측(HTTP 200): `groundingpi/GroundingPI` ★**24** · fork **2** · open_issues **0** · Apache-2.0 · created 2026-09-30 · pushed 2026-10-06.
> 🎯 ⇒ **34개 벤치 SOTA·44개 베이스라인 비교를 주장하는 논문의 공식 레포가 별 24개다.** 같은 배치 [[rea]] 는 ★**179,917** 로 **7,496배**다.
> 📌 **이것은 [[관심-검증-역상관]] 의 역방향 사례다**: 지금까지 수집한 것은 *관심 많고 검증 없음*(rea)이었는데, 본 건은 **검증 풍부하고 관심 없음**이다.
> 🆕 **⇒ 역상관 명제를 양방향으로 보강한다: 관심도와 검증 가능성은 같은 축이 아니다 — 어느 쪽으로도 벌어진다.**
> ⚖️ **단 공개 9일차**(09-30 생성)이므로 누적 관심이 쌓일 시간이 짧다. **절대 비교는 공정하지 않다.**

## 도메인별 추출 (slam-3dgs)

- **현재 SOTA**: 주장상 **그라운딩 34엔트리 평균 73.68%**(GPT-6 Astra 71.54% 대비 **+2.14%p**). ⚖️ **분모가 중복 가중**이라는 점을 반드시 병기해야 한다(위 최대 발견).
- **실시간 가능성**: 🔴 **미확인.** 초록이 *"fast enough for closed-loop control"* 을 **동기로** 제시하지만 **지연시간·FPS 수치가 없다**. 폐루프 제어를 내세우면서 레이턴시를 안 적은 것은 공백이다.
- **카메라 파이프라인**: 점·박스를 **공유 어휘의 양자화 좌표**로 출력(언어모델 토큰 공간에 좌표를 넣는 방식). 비전 인코더 **MoonViT-V2**.
- **응용 가능성**: 🟡 **백본 교체형으로 쓰인다.** RoboTwin 2.0 OOD **4개 설정 전부**에서 최강 백본 대비 최대 **+24.8%(상대값)**; RoboCasa-GR1 은 **시연 50% 학습으로 75% 학습 베이스라인 상회**(= 데이터 효율 주장); nuScenes 오픈루프 L2 평균 **0.296m**.
- **필수 레퍼런스**: `eval/README.md`(34엔트리 정확 목록·재현 경로) · `vla/README.md`(StarVLA·OpenWAM 백본 비교 워크플로우 — **24.8% 의 기준 백본명이 여기 있을 가능성**).

> [!action] 당장 할 것
> `vla/README.md` 와 `eval/README.md#full-suite` 를 열어 ① **+24.8% 의 기준 백본명** ② **11 capabilities 의 정확한 분류** 를 확정한다. 경로는 이미 특정됐다(볼트가 레포 구조를 확인함).

> [!question] 미해결
> - **+24.8% 의 기준 백본명** — `vla/README.md` 에 있을 것으로 보이나 **미열람**(경로 확보).
> - **"11 perceptual capabilities" ↔ 8 태스크 그룹** 불일치의 정체.
> - **GPT-6 Astra 의 파라미터 수** — *"the larger"* 의 배수가 미상.
> - **지연시간/FPS** — 폐루프 제어를 동기로 들면서 수치 없음.

## 관련 페이지
- [[단위-불일치]] — 🆕 **34 엔트리 ≠ 22 데이터셋**(신규 축)
- [[복합지표-분해]] — 평균이 중복 가중을 숨긴다
- [[관심-검증-역상관]] — 🆕 **역방향 사례**(검증 풍부 · ★24)
- [[특화-역류]] · [[비매칭-비교]] — 전용 4B 가 범용 대형을 이긴 구조
- [[임바디드-AI]] · [[월드모델]] · [[Reflex]] — 같은 재판정 경로(ai-news → slam-3dgs)
- [[S-Space]] — 같은 배치, **수치 0 vs 수치 최다** 의 대조군
- [[XPENG-AI]] · [[slam-3dgs]]

## 원본
- 출처: https://huggingface.co/papers/2609.39601
- 수집: 2026-10-13 자동수집(ai-news) · 인제스트 2026-10-13 · 🔄 **도메인 재판정 slam-3dgs**
- 검증: HF API `api/papers/2609.39601` HTTP 200(6,932 B) · GitHub API `groundingpi/GroundingPI` HTTP 200 · `README.md` 24,631 B · `eval/README.md` 10,430 B · 🏆 **34엔트리 합계 검산 통과(4+6+7+4+3+4+2+4=34)** · 고유 데이터셋 22 계수
- raw 대비: ✅ 73.68/71.54/+2.14%p · 34벤치 · 44베이스라인 · 24.8% · 50%vs75% · 0.296m **전건 일치** · 🏆 **볼트 신규 3건**: 34엔트리 목록 해소 · 고유 데이터셋 22 발견 · 아키텍처(MoonViT-V2+Qwen3-4B) 확정 · 🏆 **소속 XPENG AI 발굴**
- 신뢰도: ⭐⭐⭐⭐ (수치가 풍부하고 재현 스위트가 공개됨 / **분모 구조에 주의 필요**)
