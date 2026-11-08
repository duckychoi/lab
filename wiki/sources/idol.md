---
title: "speridlabs/idol — 사진 한 장 → 최대 100만 가우시안 .ply. 피크 VRAM 7.2GB, 비교표 6/7 1위는 개발사 자체 측정"
type: source
domain: slam-3dgs
tags: [slam-3dgs, 3dgs, gaussian-splatting, image-to-3d, hf-model, dit, octree, apache-2.0, 자기보고-수치]
created: 2026-11-08
updated: 2026-11-08
sources: [https://huggingface.co/speridlabs/idol]
reliability: medium
---

**HF**: [speridlabs/idol](https://huggingface.co/speridlabs/idol) · 다운로드 **20,689(30일 = 누적)**(볼트 11-08 API · 수집기 19,139) · ♥**1,222**(수집기 985 → +237/1일) · trendingScore 760(트렌딩 2위권) · Apache-2.0 · created 10-28 · sha `2731c229`

## 핵심 인사이트
> [!insight] 단일 이미지 → 표준 3DGS `.ply` 를 소비자 GPU 에서
> 배경 제거·프레이밍 후 **보이지 않는 면까지** 32,768~**1,048,576**개 가우시안을 표준 3DGS `.ply` 로 출력(카메라 추정 JSON 동반). 구성: DiT 디노이저 **370.6M** + 옥트리 디코더 **50.8M**, 요청 전체 약 **1.80B**(인코더로 게이트된 DINOv3·FLUX.2-dev VAE 사용). **피크 VRAM 7.2GB** — 8GB 소비자 GPU 에서 돈다. 표준 `.ply` 라 기존 3DGS 뷰어/엔진에 그대로 들어간다는 점이 실용적.

> [!warning] 라이선스 연쇄 + 자체 측정
> - 모델 자체는 Apache-2.0 이지만 **DINOv3·FLUX.2-dev 약관 동의가 필요**(게이트) — 상업 사용 시 FLUX.2-dev 비상업 조건을 따로 확인해야 한다.
> - H100 평균(카드 grep 전건 검출): SSIM **0.726** · LPIPS **0.213** · IoU **0.862** · 신규시점 DINOv2 **0.781** · CLIP **0.885** 로 TripoSplat·[[TRELLIS.2|TRELLIS]]·LGM 대비 최고, **PSNR 만 LGM 12.46 > Idol 12.25** — 카드가 "LGM 이 흐릿한데도 PSNR 이 높다"고 해명. 1위 6/7 은 **개발사 자체 측정**. 시간 6.8 s(H100) / 3.4 s(B300, 262,144 가우시안·50스텝) — **조건이 다른 두 수치**를 한 줄에 두지 않는다.

## 도메인별 추출 (slam-3dgs)
- **현재 SOTA**: 오픈 단일이미지→3DGS 중 유력(자체 비교 기준).
- **실시간 가능성**: NO — 요청당 수 초. 오프라인 에셋 생성용.
- **카메라 파이프라인**: 단일 RGB → 카메라 추정 JSON + .ply.
- **응용 가능성**: 영상 SaaS 의 "사진 → 3D 회전 샷" 기능 프로토타입에 직결(7.2GB 로 로컬 가능).
- **필수 레퍼런스**: TRELLIS 와의 독립 비교 필요.

## 관련 페이지
- [[slam-3dgs|3DGS]] · [[AI-3D-생성]] · [[TRELLIS.2]]
- 같은 배치: [[Qwen3.5-4B-GLB-3D-Coder]](코드로 3D, 다른 경로)

## 원본
- 출처: https://huggingface.co/speridlabs/idol
- 확인 범위: HF API expand(볼트 11-08) · 카드 raw 7,274B grep(0.726·0.213·0.862·0.781·0.885·12.46·12.25·7.2GB·6.8s·3.4s·370.6M·50.8M·1.80B·1,048,576 검출) · 추론 0회
- 신뢰도: ⭐⭐ (트렌딩 상위 · 자체 측정)
