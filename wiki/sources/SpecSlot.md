---
title: "SpecSlot — 토큰을 역할로 나눠 세부와 전역 통신 비용을 분리한 픽셀 공간 생성"
type: source
domain: ai-news
tags: [ai-news, image-generation, pixel-space, tokenization]
created: 2026-11-01
updated: 2026-11-01
sources: [https://huggingface.co/papers/2610.40647]
reliability: medium
---

**HF**: published 2026-10-29 · upvote 36 · 저자 5 · arXiv 2610.40647 · 코드 [JiongfanYang/SpecSlot](https://github.com/JiongfanYang/SpecSlot)

## 핵심 인사이트
> [!insight] 세부를 늘려도 전역 시퀀스를 늘리지 않는다
> 앵커마다 슬롯을 두고 DCT 대역을 나눈 뒤, 저주파 슬롯만 전역 어텐션에 참여시킨다. 512 해상도에서도 전역 시퀀스가 288토큰에 머문다. "토큰 수 = 세부 = 비용"의 결합을 푸는 설계다.

> [!warning] 격차를 함께 봐야 한다
> - ImageNet-256: FLOPs 대조군(JiT-CM) 대비 **+0.09**에 그치고(FID 6.59 대 6.68), 최강 JiT-B/8(4.34)에는 **2.25 뒤진다**.
> - ImageNet-512: 대조군 대비 2.84 개선, JiT-B/16에 0.69 뒤지며 비용 38.2% 절감.
> - 저자도 두 작동점만으로는 512 쪽 이득의 **원인을 분리하지 못한다**고 적었다.

- **텍스트→이미지**: DPG-Bench 62.21 대 JiT-B/8 61.15(전방 연산 40.6% 절감) · 🔴 GenEval은 26.99 대 29.78로 **뒤진다**(수집기 · 초록 미언급, Table 2).

## 도메인별 추출
- **즉시 활용**: NO(ImageNet 학습 연구 단계). **6개월 영향력**: 잠재 공간 없는 생성 모델의 고해상도 비용을 낮추는 설계 후보다.
- **대체 관계**: VAE 잠재 확산의 대안인 픽셀 공간 계열(JiT)의 효율 개선. 현행 도구를 대체하지는 않는다.

## 관련 페이지
- [[AI-영상-생성-2026]] · [[Dynamic-Band-Splitting]] · [[천장-기준선]] · [[한정어-탈락]]

## 원본
- 출처: https://huggingface.co/papers/2610.40647
- 확인 범위: HF `api/papers` · arXiv HTML 본문 · 🔴 코드 실행 0회 · 수치는 전부 저자 보고
- 신뢰도: ⭐⭐⭐ (코드 공개 · 격차 자체 공개 · 볼트 재현 없음)
