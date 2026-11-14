---
title: "facebook/dinov3-vitl16-pretrain-lvd1689m — DINOv3 ViT-L/16 (7B 증류) 비전 백본 · 1년 지난 모델의 재트렌딩"
type: source
domain: slam-3dgs
tags: [slam-3dgs, vision-backbone, self-supervised, dense-features, depth, segmentation, meta, gated]
created: 2026-11-14
updated: 2026-11-14
sources: [https://huggingface.co/facebook/dinov3-vitl16-pretrain-lvd1689m]
reliability: high
---

**모델**: [facebook/dinov3-vitl16-pretrain-lvd1689m](https://huggingface.co/facebook/dinov3-vitl16-pretrain-lvd1689m) · dl30 **692,241** · 누적 **8,824,385** · likes 2,231 · `gated: manual` · license `dinov3-license` · safetensors 303,129,600 파라미터 · created 2025-08-06 · modified 2025-08-19 · base `facebook/dinov3-vit7b16-pretrain-lvd1689m` · arXiv 2508.10104 (HF API 볼트 실측). 수집기 `ai-news` → 볼트 재분류 `slam-3dgs`(dense feature · 깊이).

## 핵심 인사이트
> [!insight] 파인튜닝 없이 선형 헤드만 — 그리고 한국에서 쓸 수 있다
> LVD-1689M 웹 이미지로 학습한 ViT-7B 를 교사로 증류한 자기지도 ViT-L/16. 백본을 얼린 채 선형 헤드만으로 분류 · 분할 · 깊이를 푼다. 모델 페이지 표(수집기 판독 — 카드가 게이트라 볼트는 raw 를 못 읽었다): ADE20k **54.9 mIoU** · NYU depth 0.352(↓) · DAVIS 79.9 · SPair 61.3 — 7B 교사(ADE20k 55.9 · NYU 0.309) 대비 dense 과제 격차가 작고 SPair 는 오히려 높다(61.3 vs 58.7).
> **라이선스**: 볼트가 GitHub `facebookresearch/dinov3` LICENSE.md(7,503B)를 직접 열었다 — 24행 *"non-exclusive, **worldwide**, non-transferable and royalty-free limited license"*. `korea|territor|exclud` 검색에서 지역 제외 조항 **없음**. 제약은 무역 통제 · 제재 준수와 ITAR · 군사 최종 용도 금지(32 · 36행) → [[라이선스-지역-제외]]의 음성 대조군(같은 규약으로 검사해 통과한 첫 사례).

> [!warning] 신규가 아니다 · 접근은 수동 승인
> 2025-08 공개 모델의 재트렌딩이다(트렌딩 24위). 게이트가 `manual` 이라 이름 · 생년월일 · 소속 등을 제출하고 승인을 기다려야 한다(수집기 판독). 볼트가 확인한 LICENSE 는 GitHub 레포의 것이며 HF 게이트 약관과 문언이 같은지는 미대조.

## 도메인별 추출 (slam-3dgs)
- **현재 SOTA**: 범용 dense feature 백본의 사실상 기준. 수치는 위 표.
- **실시간 가능성**: 3.03억 파라미터 ViT-L/16 — 단일 GPU 실시간 추론 범위(해상도 의존, 수치 미확인).
- **카메라 파이프라인**: RGB → 패치 특징(16px) → 선형 헤드로 깊이 · 분할 · 대응점. SLAM 프런트엔드의 특징 추출 · 루프 클로저 디스크립터 후보.
- **응용 가능성**: 영상 SaaS 쪽에서도 프레임 간 대응(DAVIS 추적 79.9)으로 객체 추적 · 일관성 검사에 쓸 수 있다.
- **필수 레퍼런스**: arXiv 2508.10104 · facebookresearch/dinov3.

## 관련 페이지
- [[Meta]] · [[라이선스-지역-제외]] · [[Open-Vision-Banana]](같은 주 — 생성 모델로 인식을 푸는 반대 경로) · [[3DGS]] · [[slam-3dgs]]

## 원본
- 출처: https://huggingface.co/facebook/dinov3-vitl16-pretrain-lvd1689m
- 확인 범위: HF API 메타 · GitHub LICENSE.md 지역 · 무역 조항 검색 · 🔴 모델 카드는 게이트로 볼트 미열람(벤치 표는 수집기 판독) · 실행 미확인
- 신뢰도: ⭐⭐⭐ (누적 882만 · Meta 공식 · 논문)
