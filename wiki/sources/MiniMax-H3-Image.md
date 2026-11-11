---
title: "MiniMax-H3-Image — 16MP 네이티브 · 6스텝 증류 오픈 웨이트 이미지 생성/편집 모델 (33.1B DiT · 카드에 정량 벤치 없음 · 가중치 합계 130GB 이상)"
type: source
domain: video-saas
tags: [video-saas, hf-model, image-generation, image-editing, dit, minimax, open-weights]
created: 2026-11-11
updated: 2026-11-11
sources: [https://huggingface.co/MiniMaxAI/MiniMax-H3-Image]
reliability: medium
---

**모델**: [MiniMaxAI/MiniMax-H3-Image](https://huggingface.co/MiniMaxAI/MiniMax-H3-Image) · dl30 **667** · likes **545** · created 2026-11-03 · pipeline `text-to-image` · 라이선스 `other`(minimax-h3-image-community-license-agreement) · base `MiniMaxAI/MiniMax-H3` (HF models API 볼트 실측)

## 핵심 인사이트
> [!insight] 영상 모델의 뼈대에서 오디오 분기를 떼어 낸 이미지 모델
> [[MiniMax-H3]] 아키텍처에서 오디오 분기를 제거한 **33.1B dense 단일 스트림 DiT**(카드 115행). 업스케일러 없이 **약 16MP**(1:1 기준 4096×4096)를 직접 생성하고 **6 스텝(6 NFE)** 으로 증류됐다(카드 67·69행). 텍스트→이미지와 다중 참조 편집(최대 16장, 수집기)을 한 체크포인트로 처리.

> [!warning] 좋아요 545 · 다운로드 667 · 벤치 0
> - 카드에 **정량 벤치 표가 없다.** "strongest" 서술(90행)은 수치 근거 없이 나온다(볼트 패턴 검색: FID·GenEval·DPG 표 미검출 — 유일한 'FID' 일치는 예시 이미지 설명문 안의 단어였다).
> - 좋아요(545)가 다운로드(667)와 거의 같다 — 받아서 돌려 본 사람보다 관심 표시가 많은 단계. [[DeepSeek-V4-Pro-Qwen3.5-9B-UNCENSORED-heretic]] 에서 본 "관심이 만든 트렌딩"과 같은 모양이다.
> - 용량: DiT 66.28GB(카드 126행) + 텍스트 인코더 66.7GB + VAE 2.34GB(+ 선택 프롬프트 확장기 17.9GB) — 수집기 집계, 볼트는 66.28 · 17.9 만 직접 검출.
> - 비표준 커뮤니티 라이선스(카드 362~363행 링크) — 상업 이용 조건 전문 미열람.

## 도메인별 추출 (video-saas)
- **기능 벤치마킹**: 고해상도 썸네일·키프레임 생성기로 쓸 수 있으나 원본 가중치는 단일 소비자 GPU 범위를 넘는다. 볼트가 11-09 에 기록한 [[P-H3-Image-Comfy]](PrunaAI 양자화 · 피크 21GB)가 현실적인 경로일 수 있다 — 단 그 모델이 이 체크포인트의 파생인지는 볼트 미확인.
- **크리에이터 인사이트**: 16MP 직접 출력은 업스케일 단계를 없앤다. 품질 근거는 카드 예시 이미지뿐.
- **프롬프트 패턴**: 카드는 16MP 부근 해상도에서 최상 결과라고 안내(226행).
- **워크플로우**: SGLang · vLLM-Omni · diffusers · ComfyUI 지원(수집기).
- **경쟁 우위 빈틈**: 오픈 웨이트 16MP + 다중 참조 편집 조합은 드물다. 검증은 아직 없다.

## 관련 페이지
- [[MiniMax]] · [[MiniMax-H3]] · [[P-H3-Image-Comfy]] · [[Viggle-Remake]] · [[dNaViT]]

## 원본
- 출처: https://huggingface.co/MiniMaxAI/MiniMax-H3-Image
- 확인 범위: HF models API · 카드 raw(23,132B) 패턴 검색 · 🔴 카드 전문 정독 아님 · 라이선스 전문 · 실행 미확인
- 신뢰도: ⭐⭐ (dl30 667 · likes 545 · 벤치 없음)
