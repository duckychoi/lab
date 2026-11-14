---
title: "Open Vision Banana — 이미지 생성기를 범용 인식 모델로 바꾸는 완전 공개 레시피 (Cityscapes 73.9 mIoU · arXiv 2611.15844)"
type: source
domain: slam-3dgs
tags: [slam-3dgs, generative-perception, segmentation, depth, open-recipe, test-time-scaling]
created: 2026-11-14
updated: 2026-11-14
sources: [https://huggingface.co/papers/2611.15844]
reliability: medium
---

**논문**: [arXiv 2611.15844](https://huggingface.co/papers/2611.15844) *Open Vision Banana: A Fully Open Recipe for Generative Visual Perception* · 업보트 **32** · 저자 7명(Arpit Jadon · Valentinos Pariza … **Yuki M. Asano**) · 발행 2026-11-11 · 코드 OpenVisionBanana/OpenVisionBanana ★14 · 프로젝트 openvisionbanana.github.io (HF papers API 볼트 실측 — 수집기와 일치). 수집기 `ai-news` → 볼트 재분류 `slam-3dgs`(분할 · 깊이).

## 핵심 인사이트
> [!insight] 비공개 방법을 공개 재현하면서, 진 곳을 이긴 곳과 같은 문단에 적었다
> Vision Banana 는 비전 과제를 "조건부 이미지 편집"으로 푼다 — 단 데이터 · 가중치 · 코드 · 구현 세부가 비공개. OVB 는 4B · 9B 오픈 웨이트 생성 모델 + 공개 데이터 210만~380만 쌍으로 재현:
> - ✅ Cityscapes 제로샷 **73.9 vs 69.9 mIoU**(Vision Banana 보고치 상회) · affine-invariant 깊이는 SOTA 급.
> - ⚖️ 비-제로샷 변형: 참조 · 추론 분할은 Vision Banana 대비 **5점 이내 열세**, **인스턴스 분할은 더 크게 뒤짐**.
> - 원래의 이미지 편집 능력은 대체로 유지.
>
> **Legend ensembling**(테스트 시점 스케일링): 여러 클래스-색 범례로 분할한 뒤 다수결 — 불안정한 색-클래스 결합을 교정해 재학습 없이 mIoU **최대 +8.7(Cityscapes) · +15.0(COCO-Object)**.
> **설계 선택이 상호작용한다**: 색 인코딩 · 프롬프트 · 파라미터 적응 · 과제 균형 — *"individually helpful choices can hurt when combined"*. 개별 ablation 의 합으로 최종 구성을 정하면 안 된다는 경고다.

> [!warning] 읽는 법
> 73.9 vs 69.9 의 상대값은 **보고치**(재실행 아님). "+8.7 · +15.0"은 "최대"다. 공개 범위(데이터 파이프라인 · 학습/평가 코드 · 중간/ablation 체크포인트)는 초록 주장이며 볼트는 레포를 열지 않았다.

## 도메인별 추출 (slam-3dgs)
- **현재 SOTA**: 깊이는 "SOTA 급"(수치 본문), 분할은 과제별로 갈린다.
- **실시간 가능성**: 낮음 — 4B/9B 생성 모델 추론 + legend ensembling 은 여러 번 추론.
- **카메라 파이프라인**: RGB → (편집 프롬프트) → 분할/깊이 "이미지". 판별 백본([[dinov3-vitl16]] + 선형 헤드)과 반대 경로.
- **응용 가능성**: 오프라인 주석 생성기(의사 라벨)로는 후보. 영상 SaaS 쪽에서는 "편집 모델 하나로 마스크 · 깊이까지" 얻는 구성.
- **필수 레퍼런스**: 프로젝트 페이지 · 코드.

## 관련 페이지
- [[dinov3-vitl16]] · [[자기제한-명시]] · [[한정어-탈락]] · [[Marigold-V2]] · [[slam-3dgs]]

## 원본
- 출처: https://huggingface.co/papers/2611.15844
- 확인 범위: HF papers API 초록 전문 · 저자 · 🔴 본문 · 코드 · 체크포인트 미확인
- 신뢰도: ⭐⭐ (업보트 32 · 코드 공개 · 불리한 결과 명시)
