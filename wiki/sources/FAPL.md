---
title: "FAPL — 영상 DiT 는 MLLM 피처를 '우회'한다: 그 우회를 끊는 3단계 학습 (코드는 '곧 공개' 배지뿐)"
type: source
domain: video-saas
tags: [video-saas, hf-paper, video-generation, dit, mllm, cinematic, multi-shot, factor-control, tencent, hkust, 선언된구현체공백, 규약15]
created: 2026-10-24
updated: 2026-10-24
sources: []
reliability: medium
---

# Making MLLM Latents Matter: Factor-Aware Predictive Learning for Cinematic Video Generation

**arXiv**: 2610.30926 · **HF**: https://huggingface.co/papers/2610.30926
**업보트**: **165** (수집기 165 **일치**) · HF 데일리 10-23 목록 **2위 — 미확정**(규약 ⑮)
**날짜**: `publishedAt` 2026-10-22 · `submittedOnDailyAt` 2026-10-23
**저자**: 11인 — 🔴 **1저자·교신(Anyi Rao)은 MMLab@HKUST**, 7인은 **Tencent Video**, 1인 LIX(École Polytechnique). HF `organization` 필드는 **tencent 단일** → [[복합지표-분해]](단일 org 필드가 기관을 숨긴다)
**코드**: https://github.com/Songlin1998/ShotVerse2.0 (★1) — **README + assets 만** · **프로젝트**: https://shotverse.github.io/fapl/
**신뢰도**: ⭐⭐

> [!insight] 핵심 인사이트 — 문제 정의가 이 논문의 이전 가능한 부분이다
> *"a Video DiT **may bypass** them [MLLM representations] through native conditioning pathways"*
> ⇒ 🎯 **MLLM 을 영상 생성기에 붙여도, DiT 가 기존 텍스트 인코더·VAE 참조 경로로 일을 하면 MLLM 은 장식이 된다.** FAPL 의 해법은 구조 변경이 아니라 **학습 중 다른 조건 경로를 끄는 것**이다(Stage I: *"Separate text-encoder and VAE-reference conditions are disabled during training"*).
> 📌 [[OpenGCUA]] 의 "하네스가 쥐던 결정을 모델로 이전"과 같은 모양 — **능력이 있는 부품이 실제로 쓰이는지는 배선이 정한다.**

## 3단계 (README·본문 대조)
1. **Stage I — MLLM 단독 조건 접지**: MLLM·커넥터 동결, DiT 만 학습. 텍스트 단독 / 텍스트+완전영상 관측이 **같은 영상 타깃**을 공유(1:1).
2. **Stage II — 팩터 스팬 치환**: 프롬프트를 `character / scene / action / camera` **4필드 구조화**, 한 필드만 다른 영상 쌍(팩터당 25K)으로 **해당 토큰 스팬만 교체** → 바뀔 것/보존할 것을 동시에 감독.
3. **Stage III — DiT 동결, MLLM+커넥터를 DiT 를 통해 최적화** — 제한 입력에서 예측하는 표현을 학습.

## 본문 수치 (arXiv HTML Table 1·2 · 초록에 없음)

| 지표 | UniVideo 13B (베이스) | **FAPL** | 변화 |
|---|---|---|---|
| Motion Order (%) | 48 | **61** | +13pp |
| Trans. Error | 0.0763 | **0.0586** | −23.2% |
| Rot. Error (rad) | 1.54 | **1.02** | −33.8% |
| ∩-Acc (%) (팩터 편집) | 42 | **58** | +16pp |
| Subject / Scene (멀티샷 일관성) | 0.462 / 0.427 | **0.516 / 0.471** | |
| FaceSim-Arc | 0.451 | **0.523** | |

> [!warning] 🔴 비교 구조의 한계 — 베이스 대비 개선 논문이다
> - **FAPL 은 UniVideo(13B DiT) 위에 만들었고**, 비교 대상은 그 UniVideo 와 Omni-Video 2(1.3B·14B) **3개뿐**이다. ⇒ "베이스라인 대비 일관 우위"는 사실상 **자기 베이스 대비 +α** 다. Kling·Veo·Seedance 같은 상용 영상 모델과의 비교는 **없다**.
> - 평가셋 **CineFactor-10K 는 저자 구성**(CoinVE-200K·OmniVBench 학습셋의 held-out 그룹) — sparse-to-video 5K · 팩터 편집 5K(팩터당 1.25K). 학습 데이터와 **같은 출처 분포** → [[분포내-우위]].
> - **사람 평가(user study)는 본문에서 찾지 못했다**(HTML 텍스트 검색 기준) — 전 지표 자동 계측.

> [!insight] 📌 Ablation(Table 2)이 보여주는 트레이드오프 — 단계는 공짜가 아니다
> - Stage II **팩터 스와핑 추가**(Exp2→3): ∩-Acc **48→57** ↑ 인데 Motion Order 54→**53**, Trans. Error 0.0654→**0.0671** 로 **오히려 나빠진다**.
> - Stage III **텍스트 단독 학습**(Exp4): ∩-Acc 57→**56**. 혼합 관측(Exp5)에서야 전 지표 회복.
> ⇒ 🎯 **"팩터 제어"와 "시간 예측"은 한 신호로 같이 오르지 않는다** — 저자가 3단계로 쪼갠 이유를 저자 자신의 표가 증명한다. 🔴 초록의 *"consistently better"* 는 최종 구성 기준이다.

> [!warning] 🔴 [[선언된-구현체-공백]] — 레포 이름도, 코드 링크도 비어 있다
> - GitHub API `contents`: **`README.md`(8,069B) + `assets/` 뿐**. 코드·체크포인트·평가 프롬프트 **0**.
> - README 의 Code 배지: **"Code - Coming Soon"**, 링크 대상이 **`[https://github.com/<org>/FAPL](...)` 플레이스홀더**가 그대로 남은 깨진 마크다운이다.
> - README `News`: *"TODO: code, checkpoints, and CineFactor-10K evaluation prompts release."*
> - 레포명 **ShotVerse2.0** ≠ 논문명 FAPL — 이름으로 찾으면 못 찾는다 → [[파생저장소-식별]].
> ⇒ HF `githubRepo` 필드가 채워져 있다는 것은 **레포의 존재만 보증한다.** 생성 2026-10-23T03:18Z(arXiv 다음 날).

## 도메인별 추출 (video-saas 템플릿)

- **기능 벤치마킹**: 내 SaaS 구현 — **불가(코드 없음)**. 단 **설계 원칙은 즉시 이전 가능**: 프롬프트를 `인물/장면/동작/카메라` **4필드 구조화**하고 **한 필드만 바꿔 재생성**하는 편집 UX 는 모델 무관하게 만들 수 있다.
- **크리에이터 인사이트**: 원하는 것 = *"카메라만 바꿔줘, 나머지는 그대로"*. 툴이 주는 것 = 프롬프트 한 단어 바꾸면 인물·배경까지 흔들림. FAPL 의 ∩-Acc(대상 팩터 변경 ∧ 비대상 보존) 가 정확히 이 갭을 재는 지표다.
- **프롬프트 패턴**: 🟢 **필드 라벨·경계를 명시한 구조화 프롬프트**(*"Field labels and boundaries locate the corresponding token spans… giving each factor an explicit address"*). 상용 모델에서도 필드 순서 고정이 일관성에 도움이 되는지 실험할 가치가 있다(미검증).
- **워크플로우**: sparse-to-video(텍스트만) → 팩터 편집 → 멀티샷(샷별 독립 생성 + 공유 인물·장면 레퍼런스). 🔴 멀티샷은 **샷을 독립 생성**하고 레퍼런스로 묶는 방식이다 — 한 번에 긴 영상을 만드는 것이 아니다.
- **디자인 레퍼런스**: 프로젝트 페이지 미열람.
- **경쟁 우위 빈틈**: "MLLM 이 들어있다"를 마케팅하는 통합 영상 모델들에 대해 **"그 MLLM 이 실제로 생성을 조건짓는가"** 를 묻는 질문 자체가 차별점이다.

> [!action] 당장 할 것
> 1. **(중간)** 볼트 영상 프롬프트 템플릿에 **4필드 구조화(character/scene/action/camera) + 단일 필드 변경 재생성** 패턴을 적용해 상용 모델(Kling·Seedance)에서 비대상 보존이 개선되는지 A/B.
> 2. **(낮음)** `Songlin1998/ShotVerse2.0` 코드 공개 감시 — `contents` 에 `README.md` 외 파일이 생기는지.

## 관련 페이지
- [[Tencent]] · [[HKUST-KnowComp]](🔴 HKUST 는 같은 대학이나 **MMLab@HKUST 와 다른 그룹**)
- [[선언된-구현체-공백]] · [[파생저장소-식별]] · [[복합지표-분해]] · [[분포내-우위]] · [[비매칭-비교]]
- [[AI-영상-생성-2026]] · [[Seedance]] · [[Higgsfield]]
- [[OpenGCUA]] — "부품이 실제로 쓰이는가는 배선이 정한다" 동형
- [[WeVisOne-VL]] · [[LayerEditor]] · [[OpenDS-World]] · [[IQuest-Q1]] — 같은 배치
- [[video-saas]]

## 원본
- 출처: https://huggingface.co/papers/2610.30926 (arXiv 2610.30926)
- 열어 본 것: HF papers API · **arXiv HTML v1 전문**(소속·Table 1·2·§4.1·4.2) · GitHub API(repo·contents) · README raw
- 관측: 2026-10-24T09:06Z (18:06 KST)
- 신뢰도: ⭐⭐ (자체 평가셋 · 베이스 대비 비교 · 코드 0)
