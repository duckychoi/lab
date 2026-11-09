---
title: "PrunaAI/P-H3-Image-Comfy — MiniMax-H3 계열 8MP·8스텝 이미지 생성/편집의 ComfyUI 파일. w4a8 로 피크 21GB, 품질 벤치는 0건"
type: source
domain: video-saas
tags: [video-saas, hf-model, text-to-image, image-editing, comfyui, quantization, int8, w4a8, pruna, minimax]
created: 2026-11-09
updated: 2026-11-09
sources: [https://huggingface.co/PrunaAI/P-H3-Image-Comfy]
reliability: medium
---

**HF**: [PrunaAI/P-H3-Image-Comfy](https://huggingface.co/PrunaAI/P-H3-Image-Comfy) · dl30 **625,136**(볼트 11-09 API · 수집기 505,526 → **+119,610/1일**) · ♥258 · trending 223 · license **minimax-h3-community-license-agreement** · base `PrunaAI/p-h3-image`(quantized) · created 2026-10-28

## 핵심 인사이트
> [!insight] 143GB 원본 계열을 소비자 GPU 범위(피크 21GB)로 내리는 정밀도 혼용 묶음
> P-H3-Image(카드 기준 33.1B 트랜스포머 + 4B 텍스트 인코더 + VAE + Qwen3.5-9B 기반 프롬프트 업샘플러) → bf16 55GB/피크 56GB · int8 30/31GB · **w4a8(+int8 VAE) 20/21GB**. CFG·네거티브 없이 **8스텝 8MP**, 입력 이미지 최대 8장 편집. 양자화 = 그룹 하다마드 회전 후 INT8/4bit 코드북, 캘리브레이션 불필요, Ampere+·RDNA3/4.

> [!warning] 수치는 속도·메모리뿐 — 품질 벤치 0건
> L40S 48GB 2048² 생성 w4a8 **6.3초 vs bf16 19초** — 단 bf16 은 그 GPU 에서 **오프로딩이 발생**한 조건이라 3배 차의 상당분이 메모리 부족 효과다([[비매칭-비교]]). 품질은 정성 설명(int8 ≈ bf16 픽셀 단위, w4a8 은 세부·구도가 가끔 바뀜). ComfyUI 지원은 **master(nightly)** 브랜치만, 프롬프트 업샘플러 별도 6.7~19.3GB. 33.1B 는 Comfy 카드에 없고 원본 카드 값(수집기 판독).

## 도메인별 추출 (video-saas)
- **기능 벤치마킹**: 24GB GPU 1장으로 8MP 썸네일·키프레임 생성 + 다중 이미지 편집(캐릭터·제품 일관성) → 영상 파이프라인의 스타트 프레임 생성기로 적합
- **워크플로우**: ComfyUI nightly + 파일 선택(Pick your files 표) + 업샘플러 유무 결정
- **경쟁 우위 빈틈**: 라이선스가 MiniMax-H3 커뮤니티 라이선스 — 상업 조건 확인 선행
- **다운로드 하루 +12만** = 이번 배치 최대 채택 신호

## 관련 페이지
- [[MiniMax-H3]] · [[MiniMax]] · [[ComfyUI]] · [[Comfy-Org]] · [[WeLM-Image]](11-07 이미지 생성) · [[비매칭-비교]]

## 원본
- 출처: https://huggingface.co/PrunaAI/P-H3-Image-Comfy
- 확인 범위: HF API(볼트 11-09) · Comfy 카드 raw grep(6.3 · 56 · 21 · 143 · Ampere · RDNA · nightly 검출)
- 신뢰도: ⭐⭐⭐ (dl 62만 · 품질 미측정)
