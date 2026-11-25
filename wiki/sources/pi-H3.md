---
title: "pi-H3 — MiniMax H3를 2–4스텝 · VAE 디코더 없이 돌리는 증류 어댑터"
type: source
domain: video-saas
tags: [video-saas, hf-model, distillation, video-generation, minimax-h3, dwd, license-region-exclusion, korea-blocked]
created: 2026-11-25
updated: 2026-11-25
sources: [https://huggingface.co/Lakonik/pi-H3]
reliability: medium
---

**모델**: Lakonik/pi-H3 · 다운로드 **32,375**(수집기 11-24) → **57,282**(볼트 API 11-25 — **하루 +77%**) · 좋아요 234 → **266** · trendingScore 77(트렌딩 32위) · HF 내부 ID `6af534d7…`(일치 확인) · base_model `MiniMaxAI/MiniMax-H3` · license other(MiniMax H3 Community License) · 생성 2026-11-12

## 핵심 인사이트
> [!insight] 마지막 스텝에서 픽셀을 직접 예측해 VAE 디코더를 건너뛴다 — 증류가 "속도"만 깎는 게 아니라 "파이프라인 부품"을 없앤다
> Stanford(일부 Luma AI) 저자. 볼트 [[MiniMax-H3]] 영상 + 동기 오디오 생성을 pi-Flow v2 소수 스텝 증류로 **2스텝 · 4스텝**에 끝내고, **DWD(Decoding Without a Decoder)** 로 마지막 스텝에서 픽셀을 직접 예측해 **영상 VAE 디코더를 건너뛴다**(VAE는 키프레임 인코딩에만 사용). 어댑터 4종(2/4스텝 × DWD/VAE), 텍스트 · 첫/끝 프레임 조건, ComfyUI용 INT8 ConvRot판. 사용 예시는 FP8 W8A8 양자화 + Sol 희소 어텐션, 자체 라이브러리 LakonLab v0.3 필요. [[동결-교정층]] 표본 — 원본 H3 동결 + 얇은 증류 어댑터.

> [!warning] 라이선스: 한국 사용 불가 확정(볼트 LICENSE.md 원문 재열람 — [[라이선스-지역-제외]] 10번째)
> LICENSE.md 30행: *"Excluded Territories means the European Union, the United Kingdom, the Republic of Korea and the United States of America."* (볼트 11-25 원문 확인) · IV.4 적용 지역 밖 사용 · 출력물 이용 금지 · **III.3 출력물로 타 AI 모델 개선 금지**. MiniMax 본체와 같은 H3 Community License 계열이며 **서드파티 어댑터가 원본의 지역 제외를 그대로 승계** — 파생 라이선스 조항 승계 사례. 카드에는 속도 · 화질 수치가 전혀 없다("the fastest way" 서술뿐). 볼트의 다른 H3 가속판([[MiniMax-H3-Turbo-Lora]] · [[Minimax-h3-Turbo-lightx2v]])과 같은 계열.

## 도메인별 추출 (video-saas)
- **실용성**: 🔴 **한국에서는 라이선스상 사용 불가** — 동향 기록용. 단 기술 자체는 주목: 증류 + 디코더 우회의 조합은 영상 생성 파이프라인 구조 자체를 단순화한다.
- **트렌드 신호**: 하루 +77% 다운로드(32,375 → 57,282) — H3 가속 계열의 수요가 아직 커지는 중.
- **액션**: 없음(라이선스 블록).

## 관련 페이지
- [[MiniMax-H3]] · [[Sulphur-3]] · [[라이선스-지역-제외]] · [[동결-교정층]] · [[video-saas]]

## 원본
- 출처: https://huggingface.co/Lakonik/pi-H3
- 확인 범위: HF API 재확인(볼트 11-25 — dl · 좋아요 · 내부 ID · base_model 일치) · **LICENSE.md 원문 재열람**(볼트 11-25 — 30행 · IV.4 · III.3 적중 행 직접 확인, 수집기 판독과 일치) · 카드(수집기 11-24) · 실행 0
- 신뢰도: ⭐⭐ (성능 수치 0 — 카드 미공개 · 라이선스 판단은 원문 확인 완료)
