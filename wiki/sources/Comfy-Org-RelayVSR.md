---
title: "Comfy-Org/RelayVSR — 스트리밍 영상 초해상 RelayVSR(4×·2×)의 ComfyUI 재포장"
type: source
domain: video-saas
tags: [video-saas, super-resolution, comfyui, upscale, wan, huggingface]
created: 2026-11-16
updated: 2026-11-16
sources: [https://huggingface.co/Comfy-Org/RelayVSR]
reliability: medium
---

**모델**: [Comfy-Org/RelayVSR](https://huggingface.co/Comfy-Org/RelayVSR) · 다운로드 **182,094**(볼트 11-16 · 수집기 162,037) · 좋아요 270 · apache-2.0 · 생성 2026-11-05 · base `kopper/RelayVSR` + `lightx2v/RelayVSR_X2` · 파일: `relayvsr_x4_int8_convrot` · `relayvsr_x2_lightx2v_int8_convrot` + flash VAE x2/x4 fp32.

## 핵심 인사이트
> [!insight] 큰 생성 모델은 "희소 참조 프레임"만, 나머지는 경량 네트워크
> 원본 kopper/RelayVSR(arXiv 2609.37850): Wan2.2-TI2V-5B 개조 모델이 희소 참조 프레임을 만들고 경량 VSR 네트워크(`flash.safetensors`)가 전 프레임을 처리하는 스트리밍 4× 초해상. 확산 업스케일러의 비용 문제를 **분업**으로 푼다.

## 도메인별 추출 (video-saas)
- **기능 벤치마킹 (속도 · lightx2v 카드 43–66행 · 볼트 확인)**: H100 80GB 1장, 1024×768 · 243프레임 → 2048×1536.
  - RelayVSR X2(LightX2V) **5.348초 = 45.44 FPS**
  - FlashVSR+ Turbo 54.024초 (4.50 FPS) · SeedVR2-3B 352.820초 (0.69 FPS)
  - 수집기 판독: SwiftVR(LightX2V) 6.399초 · Open-H3-Regenerate-2K 785.0초 · 원본 RelayVSR 4× 26.3초(LightX2V 19.3초)
- **프롬프트 패턴**: 없음(입력 영상만). 2× 워크플로 링크 제공.
- **워크플로**: [[MiniMax-H3]] 등 생성 영상 → RelayVSR 2× → 최종 출력. ComfyUI 에서 바로 시험 가능.

> [!warning] 속도만 있고 화질은 없다
> ① 위 속도는 **LightX2V 런타임 · 원본 가중치** 기준 — ComfyUI int8 재포장본 측정이 아니다. ② Comfy-Org 카드(40행) · lightx2v 카드 모두 **PSNR/SSIM/LPIPS grep 0건**(볼트 확인) — "플리커 억제"는 비교 영상으로만. ③ 측정 1회(워밍업 후). → [[벤치마크-외부축]].

> [!note] 라이선스 — 지역 제외 없음
> kopper/RelayVSR LICENSE = Apache-2.0 원문(11,358B · `territor|korea|exclud` 3건은 전부 Apache 본문의 "excluding" — 지역 조항 아님 · 볼트 확인). lightx2v/RelayVSR_X2 메타 license 필드 없음. [[라이선스-지역-제외]] 음성 대조군.

## 관련 페이지
- [[Comfy-Org]] · [[MiniMax-H3]] · [[Veyra-NRVideo]](재생 단계 초해상) · [[MiniMax-H3-Character-Swap-LoRA]](같은 배치) · [[라이선스-지역-제외]] · [[AI-영상-생성-2026]] · [[파생저장소-식별]]

## 원본
- 출처: https://huggingface.co/Comfy-Org/RelayVSR · https://huggingface.co/kopper/RelayVSR · https://huggingface.co/lightx2v/RelayVSR_X2
- 확인 범위: HF models API 3건 메타 · Comfy 카드 화질 지표 grep · lightx2v 카드 속도 표 행 · kopper LICENSE 원문(볼트) · 🔴 실행 미확인 · 화질 미측정
- 신뢰도: ⭐⭐⭐ (DL 18만 · Apache · 속도 표 공개)
