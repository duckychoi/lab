---
title: "OmniShowcase — 다시점 참조 이미지로 '안 보이던 면'까지 3D 일관된 피사체 영상(360° 궤도 포함). 표면 노멀맵 턴테이블을 조건으로 넣는다. 🔴 영상 품질은 'competitive'(SOTA 아님) · 학습셋은 3D 에셋 렌더"
type: source
domain: video-saas
tags: [video-saas, ai-news, hf-paper, subject-to-video, multi-view, 3d-consistency, normal-map, product-video, 360-orbit]
created: 2026-10-29
updated: 2026-10-29
sources: [https://huggingface.co/papers/2610.35684]
reliability: medium
---

# OmniShowcase: Omnidirectional Subject-Consistent Video Generation from Multi-View Images

**HF**: https://huggingface.co/papers/2610.35684 · published **2026-10-26** · Junyeong Ahn · Geonwoo Kim · Kinam Kim · Gihwi Kim · Hoonjin Jung · Hyojin Jang 외(저자 7) · upvote **28**(수집기 27 · +1 드리프트)
**코드**: 🆕 https://github.com/justin4ai/OmniShowcase (HF `githubStars` **4**) · 프로젝트 페이지 justin4ai.github.io/OmniShowcase — 🔴 **수집기는 코드 레포를 적지 않았다**
**신뢰도**: ⭐⭐ medium(초록 수치 0개 · 코드·평가셋 공개)

> [!insight] 핵심 인사이트 — 다시점 참조를 주는 것만으로는 부족하다, 그 시점들을 잇는 3D 구조를 명시해야 한다
> 단일 참조 S2V 는 카메라가 돌면 안 보이던 면을 지어내야 한다. 최근 방법들은 참조를 여러 장으로 늘렸지만 **시점 간 3D 구조를 명시하지 않고**, 학습 데이터도 시점 변화가 같은 3D 피사체를 유지한다는 보장이 없다.
> OmniShowcase 의 두 부품: ① 피사체 기하가 이끄는 카메라 궤적(360° 궤도 포함)으로 **학습 영상을 자동 합성** ② 참조 뷰에서 재구성한 **표면 노멀맵 턴테이블**을 조건으로 투입 — 생성 프레임과 **시간 정렬이 필요 없다**.
> 데이터: **Showcase-4K**(카메라 모션 12종 × 궤적 설정 88개, 3D 에셋 기반) · 평가셋 **ShowcaseBench**(소스 메시·카메라 파라미터 포함).
> 🎯 [[video-saas]] 관점: 상품 360° 쇼케이스는 커머스 영상의 정형 포맷이다. 사진 몇 장 → 회전 영상이 3D 일관성을 지키면 촬영 세팅(턴테이블)을 대체한다.

> [!warning] 🔴 주의 — 수집기 요약에서 빠진 것
> - 🔴 **영상 품질·모션은 SOTA 가 아니다**: 초록 *"state-of-the-art subject identity and 3D consistency while maintaining **competitive** video quality and motion"* — 1위는 정체성·3D 일관성 2축뿐이고 화질·모션은 "경쟁력 있는" 수준. 수집기는 "주장: 피사체 정체성과 3D 일관성 SOTA"로 적어 **틀리진 않았지만** 화질 쪽 양보를 적지 않았다 → [[한정어-탈락]].
> - 🔴 **학습 코퍼스는 3D 에셋 렌더 영상이다**(*"a corpus of 3D-asset-based videos"*). 실사 상품 사진 → 영상 전이 성능은 초록에서 확인되지 않는다 → [[분포내-우위]]. ShowcaseBench 도 메시 렌더 기반이라 **평가도 같은 분포**다.
> - 초록에 정량 수치 0개(수집기 기재 ✅).
> - 코드 레포 존재 미기재(수집기 누락 · HF `githubRepo` 필드에 있음).

## 도메인별 추출 (video-saas)
- **기능 벤치마킹**: 내 SaaS 에 "상품 사진 3~4장 → 360° 회전 영상" 기능을 넣는다면 — 노멀맵 재구성(다시점 → 메시/노멀) + 조건부 영상 모델. 난이도 높음(3D 재구성 단계 필요) · 코드 공개 여부에 따라 달라짐.
- **크리에이터 갭**: 기존 S2V 는 뒷면을 지어낸다 → 상품 영상에서 치명적(로고·라벨이 바뀜). 3D 일관성이 셀링포인트인 이유.
- **프롬프트 패턴**: 해당 없음(조건 = 노멀맵 턴테이블).
- **경쟁 우위 빈틈**: 실사 상품 사진 입력에서도 일관성이 유지되는지가 상용화 관건 — 논문이 답하지 않은 부분이 곧 차별화 지점.
- 비교: [[AI-3D-생성]] · [[AI-영상-생성-2026]] · [[Diffusion-월드모델]]

## 관련 페이지
- [[video-saas]] · [[AI-영상-생성-2026]] · [[AI-3D-생성]] · [[한정어-탈락]] · [[분포내-우위]]
- 같은 배치(10-29): [[DTCA]] · [[Falcon-AVTSE]] · [[Sensorimotor-Alignment]] · [[TAO-Agentic-Serving]] · [[LTX-2.5]]
- [[ai-news]]

## 원본
- https://huggingface.co/papers/2610.35684 (초록) · https://justin4ai.github.io/OmniShowcase
- 볼트 실측(2026-10-29T09:06Z, HF `api/papers`): upvote 28 · 저자 7 · githubRepo justin4ai/OmniShowcase · githubStars 4 — 🔴 수집기 코드 레포 누락 · 화질 'competitive' 한정 미기재
- 신뢰도: ⭐⭐
