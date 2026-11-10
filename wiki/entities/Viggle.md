---
title: Viggle — Qwen-Image 증류 LoRA 를 내놓은 제작사
type: entity
domain: video-saas
tags: [video-saas, ai-news, 증류, lora, 이미지생성]
created: 2026-09-27
updated: 2026-11-10
sources: [Qwen-Image-2.1-viggle-turbo.md]
reliability: low
---

# Viggle

> [!note] 볼트가 확인한 것만
> HuggingFace 조직 `Viggle` 로 **[[Qwen-Image-2.1-viggle-turbo]]** 를 배포한다 — [[Qwen-Image-2.1]] 을 Distribution Matching Distillation 으로 증류한 **few-step LoRA 어댑터**(40패스 → 6패스).
> 🎯 **모델카드 품질이 볼트 관측 기준 상위다** — 3지표에 **측정 정의를 함께 적고**(intra-prompt DINOv2 patch distance 평균비 · 이미지 중심 수평 이동량), 한계 3건을 자기신고하고, ComfyUI 포팅이 *"mostly vibe-coded"* 임을 **직접 밝힌다** → [[자기제한-명시]].

> [!warning] 🔴 조직 실체는 미확인이다
> ⬜ 회사 규모·국가·자금·다른 제품 **전부 미조사.** 볼트가 아는 것은 **이 HF 조직이 이 모델을 냈다**는 것뿐이다.
> ⚠️ *"Viggle"* 이라는 이름의 AI 영상·캐릭터 애니메이션 서비스가 별개로 존재할 가능성이 있으나 **볼트가 동일 조직임을 확인하지 않았다** — **추정으로 연결하지 않는다.**
> → actionable: 조직 실체 조회(HF org 페이지 · 자체 사이트).

## 관련 페이지
- [[Qwen-Image-2.1-viggle-turbo]] — 배포 모델
- [[Qwen-Image-2.1]] · [[Alibaba]] — 베이스 모델과 그 제작사
- [[원본-파생-역전]] — 이 조직의 파생이 원본을 2.52배 역전
- [[자기제한-명시]] · [[바이브코딩]] · [[온폴리시-증류]]

## 원본
- 출처: https://huggingface.co/Viggle
- 신뢰도: ⭐ (**모델 1건 기준의 조직 판정** — 조직 실체 미조사)

## 🔄 2026-11-10 갱신 — 두 번째 모델 [[Viggle-Remake]] (영상 편집 LoRA + MCP 에이전트)
- 이미지 증류 LoRA([[Qwen-Image-2.1-viggle-turbo]]) 1건뿐이던 조직에 **영상 편집 모델**이 추가됐다: [[MiniMax-H3]] 위 rank-256 LoRA 2종(swap · edit) + 컷 단위 MCP 에이전트. dl30 97,356 · ♥246(HF API 11-10).
- 조직 판정 근거가 모델 1건 → 2건. 둘 다 **남의 베이스 위 LoRA** 라는 점은 같다. 카드가 "모델 안에 안전장치 없음 · 동의 검증 불가"를 직접 적는다.
- 조직 실체(회사 · 인력)는 여전히 미조사.
