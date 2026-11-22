---
title: "Posterior Matching Distillation (PMD) — 보조 score 네트워크 없이 조건부 분포 전체를 감독하는 확산 증류 (NVIDIA · 4스텝 FID 최고 · 수치는 초록에 없음)"
type: source
domain: ai-news
tags: [ai-news, paper, diffusion-distillation, few-step, sdxl, flux, nvidia]
created: 2026-11-22
updated: 2026-11-22
sources: [https://huggingface.co/papers/2611.26629]
reliability: medium
---

**논문**: arXiv 2611.26629 · 업보트 37(볼트 11-22 · 수집기 35) · 🆕 HF 조직 `nvidia`(볼트 확인 — 수집기 미기재) · 저자 4 · 코드 [yesiltepe-hidir/PMD](https://github.com/yesiltepe-hidir/PMD) ★13

## 핵심 인사이트
> [!insight] 다양성 손실(mode-seeking)을 "posterior 평균 일치"로 우회한다
> reverse-KL 계열 증류의 mode-seeking 문제를 겨냥. 고정된 노이즈 상태에 조건화한 학생 샘플의 지수 가중 평균을 교사 posterior 평균에 맞춘다. 가우시안 손상 하에서 기울인 posterior 평균이 "이동된 입력에서의 교사 1회 평가"가 된다는 점을 이용해 **보조 student-score 네트워크 없이** 조건부 분포 전체를 감독하고, 열린 근방에서의 일치가 posterior 를 유일하게 식별함을 증명. 학습된 타임스텝 격자 안에서는 재학습 없이 임의 스텝 수 샘플링.

> [!warning] 수치와 범위
> 실험은 SDXL · FLUX.2 [klein] 4B. "4스텝 방법 중 FID 최고", 프롬프트 정합 · 지각 품질은 "경쟁적이거나 선두" = 일부 지표는 1위가 아니다. **FID 값 자체는 초록에 없다.** 초록의 "video" 는 도입 문장(증류가 이미지 · 영상 생성을 가속한다)에만 나온다 — 영상 모델 실험이 아니다(볼트 문맥 확인).

## 도메인별 추출 (ai-news)
- **신뢰도**: ⭐⭐⭐ — NVIDIA · 코드 공개 · 이론 보장 주장.
- **즉시 활용**: NO(이미지 증류 연구). 영상 few-step 증류로 옮겨지면 video-saas 관련.
- **6개월 영향력**: 보조 네트워크가 없으면 증류 학습 비용 · 불안정성이 준다 → 커뮤니티 few-step LoRA 제작 문턱 하락 가능.
- **대체 관계**: DMD 계열(분포 매칭 증류)의 대안. [[Jeveration]] 의 1-step 생성과는 다른 축(확산 증류).
- **허와 실**: "최고 FID"에 격차가 붙지 않았다.
- **액션**: 본문 표 확인 대상.

## 관련 페이지
- [[NVIDIA]] · [[Jeveration]] · [[한정어-탈락]] · [[ai-news]]

## 원본
- 출처: https://huggingface.co/papers/2611.26629
- 확인 범위: HF papers API(초록 전문 · 조직 · githubRepo) · 🔴 본문 표 미열람
- 신뢰도: ⭐⭐⭐
