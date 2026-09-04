---
title: SAM 3 — 텍스트로 "개념 전체"를 분할하는 프롬프터블 세그멘테이션 (DL 2,081,577)
type: source
domain: video-saas
tags: [ai-news, hf-model, segmentation, meta, sam, video, open-vocabulary, transformers]
created: 2026-09-04
updated: 2026-09-04
sources: []
reliability: high
---

# facebook/sam3 — 이미지에서 영상으로, 클릭에서 문장으로

**HuggingFace**: https://huggingface.co/facebook/sam3
**다운로드(30일)**: **2,081,577** — raw 자동수집 값과 **완전 일치**
**좋아요 2,894 · 라이선스 `other` · 게이트 `manual` · 생성 2025-11-07**
**코드**: https://github.com/facebookresearch/sam3 · **데모**: HF Space `akhaliq/sam3`

> [!warning] 🚨 raw 주장 정정 — 여기서도 게이팅은 카드를 막지 않았다
> raw는 *"게이트(manual) 모델이라 카드 열람에 승인 필요, **벤치마크 수치는 미확인**"* 이라 적었다. **틀렸다.** 카드 전문(26KB)과 **SA-CO 벤치마크 수치를 비인증으로 확보**했다. [[pyannote-community-1]]과 **같은 배치에서 같은 오류가 2건** — 우연이 아니라 **수집기의 체계적 결함**이다. → **`gated` 필드를 "카드 열람 불가"로 해석하지 말 것.**

> [!insight] 핵심 인사이트 — SAM 2와의 결정적 차이는 "전부"다
> SAM 2까지는 **점·박스·마스크로 *그 객체 하나*를 분할**했다. SAM 3는 **짧은 텍스트 구절이나 예시(exemplar)로 지정한 개방 어휘 개념의 *모든 인스턴스를 남김없이* 분할**한다(**PCS**, Promptable Concept Segmentation). *"ear"* 라고 쓰면 이미지 안의 **귀를 전부** 찾는다. 이 전환은 **"어떤 것을 고르는 도구" → "무엇이 몇 개 있는지 세는 도구"** 로의 성격 변경이다. 자동화 파이프라인에서 결정적인데, **사람이 클릭할 필요가 사라지기 때문**이다.

## 수치 (카드 원문)

- **SA-CO 벤치마크에서 인간 성능의 75~80% 달성**
- SA-CO는 **270,000개 고유 개념** 포함 — **기존 벤치마크의 50배 이상**
- 이미지 + **비디오**(`build_sam3_video_predictor`) 모두 지원, 프레임 임의 지점에서 텍스트 프롬프트로 세션 시작
- **🤗 Transformers 정식 통합**: `Sam3Model` · `Sam3Processor` — `from_pretrained("facebook/sam3")` 한 줄
- 프롬프트 종류: **텍스트 / 단일 박스 / 다중 박스(양성·음성 라벨로 개념 정교화) / 점 / 마스크 / 예시 이미지**

> [!note] "인간의 75~80%"라는 표현이 드물게 정직하다
> 대부분의 모델 카드는 *"SOTA 달성"* 을 쓴다. Meta는 **인간 대비 비율**로 적었다 — 즉 **아직 사람에 못 미친다는 걸 수치로 명시**했다. 볼트가 [[EarlyEval]]·[[VoiceStudio]]·[[anthropics-skills]]에서 관측한 **주장 약화형 정직성**의 또 다른 사례이며, 이 배치에서만 **네 번째**다. 다만 **SA-CO는 Meta 자체 제작 벤치마크**이므로, *"기존의 50배"* 는 **자사 벤치마크의 규모 주장**이라는 점은 감안해야 한다.

## 도메인별 추출 (video-saas 교차 slam-3dgs)

- **기능 벤치마킹**: **텍스트로 영상 객체를 지정→추적→마스크**가 한 모델로 된다. 영상 자동화에서 이건 **로토스코핑(rotoscoping) 자동화**를 뜻한다 — 배경 교체·객체 제거·선택적 색보정이 **클릭 없이** 가능해진다. 난이도는 낮은 편(Transformers 통합 완료), 필요 스택은 PyTorch + GPU.
- **크리에이터 인사이트**: 편집자가 가장 시간을 쓰는 반복 작업이 **마스킹**이다. *"모든 인스턴스"* 를 세는 능력은 **"화면 속 사람 전부 흐리게"** 같은 요청을 1회 프롬프트로 만든다.
- **워크플로우**: 프레임 0에서 텍스트 프롬프트 → 세션 유지 → 전 프레임 마스크. 조립형 파이프라인에 **후처리 단계로 끼워 넣기 쉽다**(생성 모델 교체 불필요).
- **디자인 레퍼런스**: 카드가 마스크 오버레이 헬퍼(`matplotlib rainbow` 컬러맵, alpha 0.5 합성)까지 제공 — 시각화 코드 그대로 재사용 가능.
- **경쟁 우위 빈틈**: 상용 영상 툴의 자동 마스킹은 대개 **폐쇄 어휘**(사람·하늘·배경 등 고정 클래스)다. **270K 개방 어휘**는 *"빨간 우산만"* 같은 지시를 가능하게 한다.
- **slam-3dgs 교차**: [[Puffin-World]]가 깊이·기하를 생성하고 SAM 3가 **의미 분할**을 붙이면, **의미가 붙은 3D 재구성**으로 간다. 볼트의 [[X2SAM]]·[[4D-Human-Scene-Reconstruction]] 축과 직결.

> [!warning] 라이선스가 `other` 이고 게이트가 `manual` 이다
> 가중치를 실제로 받으려면 **수동 승인**이 필요하고 라이선스는 `other`(Meta 자체 조항). **상업적 사용 조건을 반드시 원문 확인해야 한다** — [[anthropics-skills]]의 source-available 문서 스킬과 같은 함정이다. 카드 열람이 자유롭다고 **사용이 자유로운 게 아니다**. 이 둘을 혼동하지 말 것.

> [!action] 당장 할 것
> HF Space `akhaliq/sam3` 에서 **볼트 실제 작업 영상 1클립**으로 텍스트 프롬프트 마스킹 스팟체크(가중치 승인 없이 가능). 확인할 것은 화질이 아니라 **①"모든 인스턴스" 주장이 실제로 성립하는가 ②프레임 간 마스크가 튀지 않는가**. 통과하면 `/down-analysis` 파이프라인의 **시각 분석 단계 보강 후보**로 승격, 그때 라이선스 원문을 확인한다.

## 관련 페이지
- [[Meta]] · [[X2SAM]] · [[Puffin-World]] · [[TCR]] · [[4D-Human-Scene-Reconstruction]] · [[4DAnyone]] · [[pyannote-community-1]] · [[AI-영상-생성-2026]] · [[Higgsfield-벤치마킹]] · [[PyTorch]] · [[임바디드-AI]] · [[AI-3D-생성]]

## 원본
- 출처: https://huggingface.co/facebook/sam3
- 코드: https://github.com/facebookresearch/sam3
- 수집: 2026-09-04 자동수집 (raw 도메인 ai-news → **video-saas 재분류**: 영상 마스킹 파이프라인 부품)
- 검증: 모델 카드 defuddle 원문 + HF API 실측 (2026-09-04) — **raw의 "미확인" 주장 반증**
- 신뢰도: ⭐⭐⭐⭐⭐
