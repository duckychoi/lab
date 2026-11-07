---
title: "WeLM-Image — 위챗 단일 GPU 배포 MoT-MoE 통합 생성·편집 모델. '오픈 1위' 3관왕 중 하나는 Turbo 변형의 몫"
type: source
domain: video-saas
tags: [video-saas, image-generation, image-editing, mixture-of-transformers, moe, wechat, tencent, hf-paper, meanflow]
created: 2026-11-07
updated: 2026-11-07
sources: [https://huggingface.co/papers/2611.07392]
reliability: low
---

**HF**: upvote **39**(볼트 11-07 · 수집기 25 · 11-06 5위) · HF 조직 표기 None(본문상 WeChat) · 저자 16명 · arXiv 2611.07392 · `githubRepo` **None** · 수집기 기준 arXiv HTML 내 가중치·코드 링크 0건 → **공개 여부 미확인**

## 핵심 인사이트
> [!insight] "저장 31.7B · 활성 5.4B"를 한 GPU 에 — 서비스용 통합 모델의 설계
> 텍스트·참조 이미지·타깃 latent 를 한 인터리브 시퀀스로 처리하는 **Mixture-of-Transformers**(이해/생성 경로 독립 가중치 + 공유 어텐션)에 경로별 MoE 를 얹어 **저장 31.7B · 타깃 latent 토큰당 생성 활성 약 5.4B**. 생성·편집을 루브릭/체크리스트 보상으로 따로 최적화한 뒤 **noise-aware on-policy 증류로 합치고**, MeanFlow few-step 증류로 Turbo 를 만든다. 네이티브 1.5K. **Turbo 4.98 s = 1024² · H20 1장 · guidance-free 8스텝**(볼트 본문 검출).

> [!warning] 초록 "오픈 1위(PRISM·Qwen-Image-Bench·UnicBench)"의 분해 (볼트 Table 5 행 직접 확인)
> - **Qwen-Image-Bench**: 기본 WeLM-Image **54.155 < ERNIE-Image-Turbo-PE 55.309**. 오픈 1위는 **WeLM-Image-Turbo-8step 55.992** 다 — 같은 이름 아래 다른 변형이 1위를 가져갔다 → [[동일대상-분리오판]].
> - PRISM 7.555(오픈 1위 · Boogu-Image-0.1-Base 7.500) · UnicBench 8.992(오픈 1위)는 기본 모델 값.
> - 편집: GEdit 8.381 < HunyuanImage-3.0-Instruct-Distil-CoT 8.385 · ImgEdit 4.581 < FireRed-Image-Edit-1.1 4.616.
> - 폐쇄 GPT-Image-2 는 PRISM 8.039 · Qwen-Image-Bench 63.165 · UnicBench 9.079 로 전부 앞선다. `WeGenBench`·`WeGenEditBench` 는 **자사 명칭 벤치** → [[벤치마크-외부축]].

## 도메인별 추출 (video-saas)
- **기능 벤치마킹**: 생성·편집 단일 모델 + 단일 GPU 배포는 이미지 SaaS 의 서빙 비용 구조에 유리. 그러나 **가중치 공개 미확인** → 지금은 구현 레퍼런스(설계 문서)로만 가치.
- **경쟁 우위 빈틈**: 오픈 상위권이지만 GPT-Image-2 와 Qwen-Image-Bench 에서 7점 이상 격차.
- **프롬프트 패턴**: 루브릭/체크리스트 보상 — 생성 품질 QA 를 체크리스트로 쪼개는 방식은 [[scenario-skills]] 의 quality-gate 와 같은 결.

## 관련 페이지
- [[Tencent]] · [[AI-영상-생성-2026]] · [[온폴리시-증류]] · [[Qwen]]
- [[동일대상-분리오판]] · [[벤치마크-외부축]] · [[한정어-탈락]]
- 같은 날 논문: [[VFlash]] · [[BestRand]] · [[Harness-S]] · [[TailSteer]]

## 원본
- 출처: https://huggingface.co/papers/2611.07392 · https://arxiv.org/html/2611.07392v1
- 확인 범위: HF API · arXiv HTML 전문 grep(수집기 인용 11개 수치 전부 검출) · Table 5 ERNIE 행 볼트 직접 확인 · 가중치 공개 여부는 수집기 기준 · 실행 0회
- 신뢰도: ⭐ (코드·가중치 미확인 · 자사 벤치 병기)
