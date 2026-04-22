---
title: Novel View Synthesis (NVS)
type: concept
tags:
  - computer-vision
  - image-generation
  - 3d
  - diffusion-model
created: 2026-04-10
updated: 2026-04-17
sources:
  - qwen-research-notes
cssclasses:
  - wide-page
---

# Novel View Synthesis (NVS)

> [!definition] Definition
> 단일 이미지(또는 소수 이미지)를 입력으로 받아 **보이지 않던 시점**의 이미지를 생성하는 기술.
> 실제 3D 메쉬 없이 모델의 학습된 "시각적 사전지식"으로 그럴듯한 뷰를 생성.

Related Model: [[entities/qwen-image]]

---

## How It Works

> [!architecture] Diffusion Prior Approach (Qwen-Image-Edit)
> ```
> 입력 이미지
>   + 시점 조건 (텍스트 프롬프트 토큰)
>   + Identity 보존 (이중 인코딩)
>      ↓
> Diffusion denoising
>      ↓
> 새 시점 이미지 생성
> ```

실제 3D mesh를 추출해서 렌더링하는 게 아니라,
"이런 앞면이면 뒷면은 대체로 이렇게 생긴다"는 ==통계적 사전지식==으로 수렴.

### View Conditioning

Qwen-Image-Edit은 슬라이더 값 → 텍스트 토큰 변환:
- `Rotate the camera 90 degrees to the right`
- `bird's-eye view`
- `back view`
- `close-up`

즉, **시점 변화 = 조건부 이미지 편집**.

---

## Identity Consistency

> [!architecture] Dual Encoding (Qwen)
> | Encoder | Input | Role |
> |---|---|---|
> | Qwen2.5-VL | 원본 이미지 | Semantic control (무엇인가) |
> | VAE Encoder | 원본 이미지 | Visual appearance control (어떻게 생겼나) |

"이 물체가 무엇인지"는 유지, "현재 보이지 않는 면"만 새로 생성.

---

## Limitations

> [!limitation] Known Failure Cases
> | Case | Reason | Result |
> |---|---|---|
> | 비대칭 제품 | 훈련 데이터에 희소 | 뒷면 잘못 추정 |
> | 뒷면 로고/텍스트 | 앞면에서 추론 불가 | 임의 생성 또는 생략 |
> | 숨겨진 구조 | 단순 hallucination | 그럴듯하지만 틀릴 수 있음 |
> | 독특한 손상/장식 | 맥락 부족 | 평균적 외관으로 수렴 |

**Bottom line:** single-view NVS는 잘 하지만, ==strict 3D consistency는 보장 안 됨==.

---

## Approach Comparison

| Approach | Method | Pros | Cons |
|---|---|---|---|
| **Diffusion prior** (Qwen) | 텍스트 조건 + diffusion | 유연함, 자연스러운 출력 | 3D 불일치 가능 |
| **NeRF** | 실제 3D 표현 학습 | 기하학적 정확성 | 다수 이미지 필요 |
| **3D Gaussian Splatting** | 포인트 클라우드 렌더링 | 빠른 렌더링 | 다수 이미지 필요 |
| **Zero-1-to-3** | 상대 카메라 각도 조건 | 단일 이미지 가능 | 디테일 손실 |

---

## Open Questions

> [!open-question]
> - Qwen-Image의 3D consistency 한계를 LoRA fine-tuning으로 극복 가능한가?
> - 특정 카테고리(예: 특정 제품 라인)에 특화 훈련하면 비대칭 물체 처리가 나아지는가?
> - ComfyUI multi-angle 노드 + 여러 시점 앙상블로 일관성을 높일 수 있는가?

---

## Related Pages

- [[entities/qwen-image]] — Qwen-Image-Edit 모델 상세
- [[domains/ai-ml]] — AI/ML 도메인 종합
- [[sources/qwen-research-notes]] — 원본 연구 노트
