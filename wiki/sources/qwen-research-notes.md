---
title: "Qwen Novel View Synthesis — Research Notes"
type: source
tags:
  - computer-vision
  - image-generation
  - qwen
  - research-note
created: 2026-04-10
updated: 2026-04-17
source_file: Research.md
author: Claude (Claude Code 대화에서 생성)
cssclasses:
  - wide-page
---

# Qwen Novel View Synthesis — Research Notes

> [!abstract] Source Summary
> Qwen-Image-Edit이 단일 이미지에서 새 시점을 생성하는 방법 —
> 실제 3D mesh 없이 ==diffusion prior==와 텍스트 조건으로.

| Field | Value |
|---|---|
| **Source File** | `Research.md` (vault root) |
| **Origin** | Claude Code 대화에서 생성된 연구 분석 |
| **Ingested** | 2026-04-10 |

---

## Key Findings

### 1. Diffusion Prior-based NVS

> [!insight]
> Qwen-Image-Edit은 공식적으로 20B MMDiT 기반 이미지 생성/편집 모델.
> "뒷면 복원"이 아니라 **"가장 그럴듯한 뒷면 이미지를 새로 샘플링"**하는 것.

학습 중 축적된 시각적 사전지식:
> "이런 앞면이면 옆면/뒷면은 대체로 이렇게 생긴다"

### 2. Identity Consistency

이중 인코딩으로 원본 정체성 유지:
- **Qwen2.5-VL** → semantic control (무엇인지)
- **VAE Encoder** → visual appearance control (어떻게 생겼는지)

T2I + TI2I + I2I reconstruction 동시 훈련으로 latent 공간 정렬.

### 3. View-conditioned Editing

시점 변화 = 조건부 편집 조건.
슬라이더 값 → 텍스트 프롬프트 변환:
```python
prompt = f"Rotate the camera {angle} degrees..."
# "bird's-eye view", "close-up", "back view" 등
```

LoRA 역할: "시점 토큰 → 일관된 뷰 변화" 매핑을 더 잘 학습.

### 4. Limitations

> [!limitation]
> - 비대칭 제품, 뒷면 로고/텍스트, 숨겨진 구조 → 추정 오류 가능
> - Single-view NVS는 잘 하지만 ==strict 3D consistency==는 보장 안 됨

---

## Reference Links

| Resource | URL |
|---|---|
| Qwen-Image-Edit Blog | `qwenlm.github.io/blog/qwen-image-edit/` |
| Technical Report | `huggingface.co/papers/2508.02324` |
| Qwen-Image-Edit-2509 Notes | GitHub `QwenLM/Qwen-Image` |
| HF Space (linoyts) | `spaces/linoyts/Qwen-Image-Edit-Angles` |
| ComfyUI Node | `jtydhr88/ComfyUI-qwenmultiangle` |

---

## Derived Pages

- [[concepts/novel-view-synthesis]] — NVS 개념 일반화
- [[entities/qwen-image]] — Qwen-Image 모델 상세

---

## Related Pages

- [[domains/ai-ml]] — AI/ML 도메인 종합
