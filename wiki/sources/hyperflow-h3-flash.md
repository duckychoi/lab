---
title: "hyperflow-h3-flash — MiniMax-H3 를 14B·CFG 없는 4~8스텝으로 압축한 영상+스테레오 오디오 생성 (🔴 한국 라이선스 제외)"
type: source
domain: video-saas
tags: [video-saas, video-generation, audio, distillation, gguf, comfyui, license, minimax]
created: 2026-11-12
updated: 2026-11-12
sources: [https://huggingface.co/VideoRebirthAI/hyperflow-h3-flash]
reliability: medium
---

**모델**: [VideoRebirthAI/hyperflow-h3-flash](https://huggingface.co/VideoRebirthAI/hyperflow-h3-flash) · DL **241,579**(30일 = 누적) · likes 225 · `image-text-to-video` · license `other` · created 2026-11-04 (HF models API 볼트 실측) · 카드 raw 321행 · 22,818B

## 핵심 인사이트
> [!insight] 31B → 13.7B, CFG 제거, 6스텝 — 24GB 소비자 GPU 에서 5.2초 영상+오디오가 약 2.5분
> MiniMax-H3(트랜스포머 약 31B) → 13.7B(fl2va) / 13.9B(ref2va), **CFG 없이 4/6/8 스텝**(기본 6), 5.2~15초 · 24fps · 1344×768 + **32kHz 스테레오 오디오 동시 생성**. t2v · 첫/끝 키프레임 · 참조 최대 12개. GGUF Q3_K_M~Q8_0(7.2~15.2GB) · INT8 convrot(약 16GB).
> 카드 표(볼트 행 대조, 236~244행 · 조건: 1344×768 · 6스텝 · 텍스트 인코딩+VAE 포함 E2E · "5.2초 / 15초"):
> - ComfyUI INT8 — RTX 5090 **83 s / 518 s** · 4090 **152 s / 747 s**
> - GGUF Q4_K_M(RAM ≥64GB) — 5090 99 / 575 · 4090 157 / 830 · **3090 315 / 1835**
> - 데이터센터(37·262~265행): 4×B200 **8.7 s** · 1×H200 36 s / 229 s
> - Q4_K_M **9.1GB** · 24/32GB GPU + **시스템 RAM 16GB PC 에서 동작**(40·224행) · **16GB GPU 는 미측정**
> ⇒ 내 4090 로컬 파이프라인에서 오디오 동반 영상이 **실측 조건이 명시된 채로** 가능한 첫 사례 — 단 아래 라이선스 때문에 쓸 수 없다.

> [!warning] 🔴🔴 한국은 라이선스 제외 지역
> 카드 312행: *"**Territory:** Licensed worldwide **excluding the European Union, the United Kingdom, the Republic of Korea, and the United States of America**. Individuals and organizations in those jurisdictions must obtain MiniMax's prior authorization **before downloading**."* — **다운로드 자체**가 사전 승인 대상이다. 원본 H3 LICENSE 10행과 같은 조항(볼트 확인). 이 카드는 그것을 **정직하게 적었다**(같은 날 [[Comfy-Org-MiniMax-H3-Image]] 카드는 생략). MiniMax 공식 제품 아님(수집기 판독). → [[라이선스-지역-제외]]

> [!warning] 품질 수치 0
> 전부 속도·메모리. 원본 대비 화질/음질 손실 벤치 없음. ref2va 의 영상·오디오 참조는 Python INT8 경로만(GGUF/ComfyUI 는 이미지만). Python INT8 오프로드는 시스템 RAM ≥69GiB(fp8 인코더) · 첫 실행 약 90GB 다운로드(139행).

## 도메인별 추출 (video-saas)
- **기능 벤치마킹**: 키프레임 · 참조 12개 · 오디오 동시 생성 — 내 SaaS 의 i2v 단계 후보로 기능 범위는 최상급. **라이선스로 차단**.
- **프롬프트 패턴**: 카드에 CFG 없음 · 6스텝 기본 — 스텝 수만 조절 변수.
- **워크플로우**: ComfyUI INT8(24GB+) / GGUF(소형 GPU · stable-diffusion.cpp) / Python INT8(데이터센터) — 카드 58행 "Decision rule" 이 경로 선택표를 준다(좋은 문서 패턴).
- **경쟁 우위 빈틈**: 한국 사업자는 이 계열을 쓸 수 없다 → 국내 SaaS 는 [[LTX-2.5]] 등 지역 제한 없는 오디오 동반 모델이 대안(라이선스 별도 확인 필요).
- **액션**: 🔴 사용 보류(승인 전).

## 관련 페이지
- [[MiniMax-H3]] · [[MiniMax]] · [[Comfy-Org-MiniMax-H3-Image]] · [[라이선스-지역-제외]] · [[ComfyUI]] · [[LTX-2.5]] · [[AI-영상-생성-2026]]

## 원본
- 출처: https://huggingface.co/VideoRebirthAI/hyperflow-h3-flash
- 확인 범위: HF models API · 카드 raw 행 대조(37·40·58·63~66·139·224·236~244·262~265·312행) · 원본 H3 LICENSE 10행 · 🔴 실행 미확인
- 신뢰도: ⭐⭐ (DL 241,579 · 속도 수치만)
