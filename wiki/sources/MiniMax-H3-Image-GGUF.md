---
title: "Abiray/MiniMax-H3-Image-GGUF — MiniMax-H3-Image(프루닝판) GGUF 양자화 (🔴 한국 제외 라이선스)"
type: source
domain: video-saas
tags: [video-saas, minimax, gguf, image-generation, license, comfyui]
created: 2026-11-16
updated: 2026-11-16
sources: [https://huggingface.co/Abiray/MiniMax-H3-Image-GGUF]
reliability: low
---

**모델**: [Abiray/MiniMax-H3-Image-GGUF](https://huggingface.co/Abiray/MiniMax-H3-Image-GGUF) · 다운로드 127,803 · 좋아요 248 · license `other`(minimax-h3-image-community-license-agreement) · base MiniMaxAI/MiniMax-H3-Image · 생성 2026-11-10.

## 핵심 인사이트
> [!insight] 33.1B 이미지 DiT 를 16GB VRAM 으로 — 단 한국에서는 쓸 수 없다
> [[Comfy-Org-MiniMax-H3-Image]] 의 구조적 프루닝 BF16 에서 직접 변환: Q2_K 6.88GB · Q3_K_M 8.91GB · **Q4_K_M 11.60GB**(16GB VRAM 권장) · Q5_K_M 14.10GB. 입력 패치화기 · 6스텝 출력 헤드 · AdaLN 기저는 FP32 유지, `pdd_sigmas` 메타로 stock ComfyUI-GGUF 로더에서 바로 로드. 별도로 24채널 VAE + Qwen3-VL-32B 텍스트 인코더(Q4_K_M 14.6GB 등) 필요(수집기).

> [!warning] 🔴 라이선스 — 원본과 바이트 동일, 한국 제외 (볼트 확인)
> 레포 LICENSE 18,208B 가 MiniMaxAI/MiniMax-H3-Image LICENSE 와 **`cmp` 동일**. 10행 Excluded Territories = EU · 영국 · **대한민국** · 미국 → [[라이선스-지역-제외]] 파생 6번째(이미지 계열 2번째). 수집기가 요약에 명시.

> [!warning] "거의 무손실"의 근거 0건 (README 60–61행 · 볼트 확인)
> *"Near-lossless visual quality"*(Q4_K_M) · *"Indistinguishable from full BF16"*(Q5_K_M) — 카드 전체에 PSNR · SSIM · FID · CLIP 점수 0건. 샘플 6장은 Q4_K_M 결과물(수집기) → 같은 배치의 "측정된 것 ≠ 쓰이는 것" 축의 극단: **측정 자체가 없다**.

## 도메인별 추출 (video-saas)
- **기능 벤치마킹**: 이미지 생성 6스텝. 기술적으로는 로컬 고품질 이미지 생성의 좋은 경로.
- **액션**: H3 계열 보류 목록에 추가.

## 관련 페이지
- [[MiniMax-H3-Image]] · [[Comfy-Org-MiniMax-H3-Image]] · [[MiniMax]] · [[라이선스-지역-제외]] · [[MiniMax-H3-Character-Swap-LoRA]] · [[원본-파생-역전]]

## 원본
- 출처: https://huggingface.co/Abiray/MiniMax-H3-Image-GGUF
- 확인 범위: HF models API 메타 · LICENSE 원문 grep + 원본 cmp · README 품질 지표 grep · 60–61행(볼트) · 🔴 파일 크기 · FP32 유지 층 · 의존 파일은 수집기 판독
- 신뢰도: ⭐ low (한국 사용 불가 · 품질 측정 0)
