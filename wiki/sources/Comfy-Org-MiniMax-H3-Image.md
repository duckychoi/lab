---
title: "Comfy-Org/MiniMax-H3-Image — MiniMax H3 Image 의 ComfyUI 재패키징 (🔴 한국은 라이선스 제외 지역)"
type: source
domain: video-saas
tags: [video-saas, comfyui, text-to-image, quantization, license, minimax]
created: 2026-11-12
updated: 2026-11-12
sources: [https://huggingface.co/Comfy-Org/MiniMax-H3-Image]
reliability: medium
---

**모델**: [Comfy-Org/MiniMax-H3-Image](https://huggingface.co/Comfy-Org/MiniMax-H3-Image) · DL **351,803**(30일 = 누적) · likes 271 · `text-to-image` · license `other`(minimax-h3-image-community-license-agreement) · created 2026-11-08 (HF models API 볼트 실측 09:05Z)

## 핵심 인사이트
> [!warning] 🔴🔴 한국에서는 사전 승인 없이 쓸 수 없다 — 그런데 이 카드에는 그 말이 없다
> 원본 [MiniMaxAI/MiniMax-H3-Image LICENSE](https://huggingface.co/MiniMaxAI/MiniMax-H3-Image/blob/main/LICENSE)(볼트 직접 조회, 18,208B) 8·10행: *"'Applicable Territory' means worldwide, excluding the Excluded Territories."* · *"'Excluded Territories' means the European Union, the United Kingdom, **the Republic of Korea** and the United States of America."* 22행: 라이선스는 *"Solely within the Applicable Territory"* 에서만 부여된다.
> 이 Comfy-Org 카드 License 절(40~44행)은 *"license agreement is different from the original MiniMax H3 license"* 라고 쓰고 **매출 100만 USD · 제3자 호스팅 조항만 인용**한다. 그러나 **원본 H3 LICENSE 도 같은 4개 지역을 제외한다**(볼트 조회, 17,604B, 10행) — 즉 "다르다"고 강조한 부분 옆에 **두 라이선스가 공유하는 가장 큰 제약(지역 제외)이 빠져 있다.** → [[표-부분인용]] · 🆕 [[라이선스-지역-제외]]
> ⇒ 서울에 있는 이 볼트 사용자에게 이 모델(과 원본·파생 전부)은 **MiniMax 승인 전에는 사용 불가**다. 11-11 actionable *"MiniMax-H3-Image 양자화 경로 시험"* 은 **보류로 전환**한다.

> [!insight] 새 모델이 아니라 폴더 구조 재포장
> 확산 모델 3종(pruned bf16 / int8_convrot / w4a8), 텍스트 인코더(qwen3vl_32b int8_convrot · nvfp4_awq), 프롬프트 보강용 qwen3.5_9b w4a8, VAE fp16, 워크플로 템플릿 2종(t2i · 이미지 편집 — 카드 표 볼트 확인). **품질·속도·양자화 손실 수치 0**. DL 35만은 원본(11-11 볼트 실측 dl30 667)의 **500배 이상** — 사용자는 원본이 아니라 재포장본으로 들어온다([[원본-파생-역전]]).

## 도메인별 추출 (video-saas)
- **기능 벤치마킹**: ComfyUI 워크플로 2종을 내 SaaS 이미지 단계에 붙이는 난이도는 낮다 — **라이선스가 막는다**.
- **크리에이터 인사이트**: 사용자는 양자화 파일 묶음 + 템플릿을 원한다(다운로드가 증명).
- **경쟁 우위 빈틈**: 한국·EU·미국·영국 사용자가 **법적으로 쓸 수 없는** 오픈 가중치 — 이 지역 SaaS 에는 대안 모델이 필요하다.
- **액션**: 🔴 사용 보류. 필요하면 platform.minimax.io 를 통해 승인 신청(원본 LICENSE 23행 *"welcome to contact us about obtaining a license"*).

## 관련 페이지
- [[MiniMax-H3-Image]] · [[MiniMax-H3]] · [[MiniMax]] · [[Comfy-Org]] · [[ComfyUI]] · [[hyperflow-h3-flash]] · [[라이선스-지역-제외]] · [[표-부분인용]] · [[원본-파생-역전]] · [[P-H3-Image-Comfy]]

## 원본
- 출처: https://huggingface.co/Comfy-Org/MiniMax-H3-Image
- 확인 범위: HF models API · 카드 raw(56행 · 3,062B) 전문 · 원본 LICENSE 2종(H3 · H3-Image) 지역 조항 패턴 검색 · 🔴 LICENSE 전문 정독·실행 미확인
- 신뢰도: ⭐⭐ (DL 351,803 · 벤치 0)
