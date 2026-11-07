---
title: "TailSteer — 디노이징 궤적 끝단만 보정해 멀티턴 편집 드리프트를 줄인다. 지시수행 손실은 백본마다 부호가 다르다"
type: source
domain: video-saas
tags: [video-saas, image-editing, multi-turn, drift, flux, on-policy, mmlab-cuhk, hf-paper]
created: 2026-11-07
updated: 2026-11-07
sources: [https://huggingface.co/papers/2611.06741]
reliability: medium
---

**HF**: upvote **37**(볼트 11-07 · 수집기 27 · 11-06 4위) · MMLab-CUHK · 저자 9명 · arXiv 2611.06741 · 코드 [Lyricccco/tailsteer](https://github.com/Lyricccco/tailsteer) **★42 · Apache-2.0**(볼트 11-07 · 수집기 ★25 · HF 캐시 3)

## 핵심 인사이트
> [!insight] 초반 동역학은 그대로, 꼬리(tail)에서만 보존 보정
> 편집 결과를 다음 턴 입력으로 재사용하면 시각 드리프트가 쌓인다. TailSteer 는 **초기 디노이징 동역학은 베이스와 같게 두고 궤적 끝 근처에만 보존 보정을 집중**한다. 보정은 편집기 **자신의 on-policy 롤아웃**에서, 바뀌지 않은 원본 영역을 기준으로 학습한다 — **정답 편집쌍 큐레이션 불필요**. FLUX·SenseNova·Qwen 계열에 적용. [[온폴리시-증류]] 계열의 "최종단 학습".

> [!warning] 🔴 수집기 "트레이드오프"는 FLUX.2 Klein 한 백본의 사실이다 (볼트 Table 2 전 백본 대조)
> | 백본 (Table 2) | `SR@5 (%) ↑` MSE-Bench 베이스 → TailSteer | `PSNR@10 ↑` 베이스 → TailSteer |
> |---|---|---|
> | FLUX.2 [Klein] Base 9B | 40.00 → **33.00**(k_s=46) · 32.00(43) · 41.00(48) | 13.85 → **19.96**(46) |
> | SenseNova U1.5-8B MoT | 50.00 → **54.00 / 55.00 / 55.00**(37/42/47) | 11.23 → 18.22 |
> | Qwen Image-2.1 | 42.00 → 38.00 / **44.00** / 38.00(24/30/35) | 16.93 → 18.38 |
>
> - 수집기가 적은 FLUX.2 Klein k_s=46 값(SR@5 40→33 · IF@3 32.69→30.24 · PSNR@10 13.85→19.96 · SSIM 0.289→0.621 · LPIPS 0.524→0.290)은 **볼트 행 직접 확인으로 정확**하다.
> - 그러나 수집기가 "미대조"로 남긴 **SenseNova 행은 SR@5 가 +4~+5 오른다** — 보존과 지시수행이 같이 좋아진다. Qwen 은 k_s 에 따라 ±. 따라서 **"보존↑·지시수행↓ 트레이드오프"는 일반 법칙이 아니라 백본·k_s 의존**이다 → [[표-부분인용]].
> - 같은 표 비교 기법 FreqEdit·VAE-LFA 도 FLUX.2 Klein 에서 SR@5 33.00 이다 — FLUX.2 Klein 에서 보존 기법 전반이 지시수행을 깎는 경향.
> - "GPT-Image-2.5 보다 낫다"는 **단일 정성 예시**(테이블 색 보존) 서술이다. Table 2 의 GPT-Image-2.5-Sunburst(API) 행은 SR@5 48.45 · PSNR@10 18.55.

## 도메인별 추출 (video-saas)
- **기능 벤치마킹**: "같은 이미지를 여러 번 고치면 망가진다"는 편집 SaaS 의 실사용 불만에 직접 대응. 오픈 가중치 편집기(FLUX.2 Klein · Qwen-Image-2.1)에 붙는 사후 학습이라 자체 서빙 시 적용 가능.
- **크리에이터 인사이트**: 15~20턴 반복 편집 시 배경·소품 보존이 핵심 — 쇼츠 썸네일·캐릭터 시트 반복 수정 워크플로에 해당.
- **프롬프트 패턴**: 해당 없음(학습 기법). 조향 시작 스텝 `k_s` 가 보존/지시수행 균형 손잡이.
- **경쟁 우위 빈틈**: 상용 API(GPT-Image-2.5)는 PSNR@10 18.55 로 TailSteer-FLUX(19.96)와 비슷 — 오픈 모델 + TailSteer 로 반복 편집 보존을 상용 수준에 맞출 여지.

## 관련 페이지
- [[온폴리시-증류]] · [[AI-영상-생성-2026]] · [[Black-Forest-Labs]] · [[SenseTime]] · [[Qwen]]
- [[표-부분인용]] · [[한정어-탈락]] · [[MoviEdit]] (편집 일관성 계열)
- 같은 날 논문: [[VFlash]] · [[BestRand]] · [[Harness-S]] · [[WeLM-Image]]

## 원본
- 출처: https://huggingface.co/papers/2611.06741 · https://arxiv.org/html/2611.06741v1 · https://github.com/Lyricccco/tailsteer
- 확인 범위: HF API · arXiv HTML Table 1·2 텍스트 파싱 — **FLUX.2 Klein · SenseNova · Qwen 3개 백본 행 전부 볼트 직접 대조** · GitHub API · 실행 0회
- 신뢰도: ⭐⭐ (MMLab-CUHK · 코드 공개)
