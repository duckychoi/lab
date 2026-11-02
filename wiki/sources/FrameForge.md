---
title: "FrameForge — 조건과 목표 사이의 '가상 시간 간격'을 골라 영상 모델로 이미지 생성·편집"
type: source
domain: ai-news
tags: [ai-news, image-generation, image-editing, video-foundation-model, lora, mixture-of-experts, video-saas]
created: 2026-11-02
updated: 2026-11-02
sources: [https://huggingface.co/papers/2610.36545]
reliability: medium
---

**HF**: published 2026-10-27 · upvote 22 · Yijing Lin · Zhendong Mao · Mengqi Huang · Yuxin Wang · Yongdong Zhang (HF 조직 FrameX-AI) · arXiv 2610.36545 · 코드 [Lyne1/FrameForge](https://github.com/Lyne1/FrameForge) (★3 · Python · 추론 코드) · LoRA 가중치 `lyneeeeeeeee/FrameForge` 공개

## 핵심 인사이트
> [!insight] 조건→목표 거리는 작업마다 다르고, 디노이징 도중에도 바뀐다
> 조건 이미지와 목표 이미지를 영상의 두 프레임으로 놓되, 그 **시간 간격을 고정하지 않는다**. MoTE는 짧은·중간·긴 간격 temporal RoPE 전문가 3개 중 하나를 라우터로 고른다. CoTR은 조건과 목표 사이에 잠재 중간 프레임을 끼우고 병목 어텐션 마스크로 정보가 그 경로를 지나게 만든다. 라우팅 분석에서 canny→이미지는 긴 간격을 고르고, 편집은 디노이징 후반으로 갈수록 짧은 간격으로 이동했다. HunyuanVideo1.5에 LoRA(182M 파라미터)만 붙였고, A800 2장으로 약 6일 학습했다.

> [!warning] "superior performance"의 실제 폭과 FID 역전
> - **DreamBench 종합 O 0.739** vs 차순위 **ChronoEdit 0.729** → **+0.010** (본문의 "1.37%"는 상대값). SC는 ChronoEdit(0.757)보다 **낮고**, PQ는 EasyControl(0.839)·IP-Adapter(0.824)·OminiControl(0.816)보다 낮다. 채점은 GPT-4o 기반 VIEScore다.
> - **COCO canny**: SSIM 0.447로 1위(EasyControl 0.417 대비 상대 +7.2%). 하지만 **FID 23.47은 6개 중 5위**다(ControlNet 20.42 · OmniGen 22.51 · EasyControl 22.82 · DRA-Ctrl 23.27). 저자는 "FID는 백본 통계 영향을 받는다"고 해명했다. CLIP-T 0.323은 ControlNet과 같다.
> - **GEdit 종합 G-O 6.12**: 오픈소스 중 1위다(ChronoEdit 5.08). 하지만 비공개 모델(GPT-4o 8.01 · Gemini 2.5 7.89 · Seedream 4.0 7.81)과는 거리가 멀다. G-PQ 6.52는 ICEdit·UniWorld·ChronoEdit보다 낮다. "GPT-4o에 근접"은 **Motion Change 한 범주**(6.84 vs 7.81)에 대한 말이다.
> - 학습·평가 해상도가 512×512이고, 비교 대상들의 베이스 모델이 SD1.5부터 Wan2.1-14B까지 제각각이다.

> [!warning] 한계 · 배포 조건
> 한계 절이 없다. 추론 시간도 보고하지 않았다(50 디노이징 스텝 기준 라우팅 분석만 있음). 레포는 HunyuanVideo 1.5 파생이라 **Tencent Hunyuan Community License**를 따르고, README상 게이트된 **FLUX.1-Redux-dev** 접근이 필요하다. 학습 코드 포함 여부는 확인하지 않았다(최상위 파일 목록만 봄).

## 도메인별 추출 (ai-news)
- **신뢰도**: 논문 + 추론 코드 + LoRA 가중치 공개 · ★3 · 볼트 재현 없음.
- **즉시 활용**: 조건부. 하나의 LoRA로 피사체 생성·canny·편집을 처리하는 통합 모델로 실험해 볼 수 있다. 다만 HunyuanVideo1.5 백본과 FLUX Redux 게이트를 풀어야 한다.
- **6개월 영향력**: "영상 모델을 이미지 편집기로 쓴다"는 흐름(ChronoEdit, DRA-Ctrl, RealGeneral)에서, 프레임 간격 자체를 학습 변수로 삼은 사례다. 동작·자세 변경 편집이 강점이다.
- **대체 관계**: 작업별 LoRA를 하나의 공유 LoRA로 대체한다. 단 어블레이션에서 MoTE·CoTR 없는 공유 LoRA는 편집이 4.94로 작업별 LoRA(5.99)보다 나빴다.
- **허와 실**: 우위는 SSIM과 오픈소스 편집 G-O에서 뚜렷하다. 피사체 생성 우위는 0.01이고, FID에서는 열세다.
- **액션**: 동작 변경 편집이 필요한 video-saas 작업이 생기면 그때 시험한다.

## 관련 페이지
- [[AI-영상-생성-2026]] · [[Diffusion-월드모델]]
- [[한정어-탈락]] ("GPT-4o 근접" = Motion Change 한 범주) · [[표-부분인용]] (FID 열세 생략) · [[비매칭-비교]] (백본 상이) · [[선언된-구현체-공백]]

## 원본
- 출처: https://huggingface.co/papers/2610.36545
- 확인 범위: HF `api/papers` · arXiv HTML 본문(표 1~5, 8, 4장) · GitHub API(★3 · 라이선스 NOASSERTION · 최상위 파일) · README · HF 모델 API(LoRA 파일 존재 확인) · 🔴 학습 코드 포함 여부 미확인 · 코드 실행 0회
- 신뢰도: ⭐⭐ (소속은 HF 조직 FrameX-AI 표기뿐, 본문 소속 각주는 추출하지 못함 · 가중치 공개)
