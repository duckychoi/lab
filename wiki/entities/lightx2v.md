---
title: lightx2v
type: entity
domain: video-saas
tags: [entity, org, lora, turbo, distillation, video-generation, lightning]
created: 2026-11-28
updated: 2026-11-28
sources: [Minimax-h3-Turbo-lightx2v.md, Minimax-H3-Turbo-Fusion.md]
reliability: medium
---

## 개요
HF 조직 `lightx2v`(재현 레포는 GitHub `ModelTC` — 09-04 페이지 실측) — **볼트 조직 실측(11-28 · HF API)**: 공개 모델 **54개**. "Lightning/Turbo" 계열 증류·가속 LoRA 전문 배포자로, Wan · Qwen-Image · MiniMax-H3 등 주요 오픈 영상/이미지 모델의 가속층을 나란히 출시한다.

## 볼트 추적 모델 (볼트 실측 2026-11-28)
- [[Minimax-h3-Turbo-lightx2v]] — DL **1,824,393** · ♥1,252 (09-04 실측 1,117,509 대비 **+706,884 / 약 85일 ≈ 일평균 +8,316**)
- [[Minimax-H3-Turbo-Fusion]] — DL **22,131** · ♥115 · created 2026-11-24 (신규 · 3-LoRA 가중합 단일 퓨전)
- Qwen-Image-Edit-2511-Lightning — DL 905,736 · ♥553 (볼트 미인제스트)
- Wan2.2-Distill-Loras — DL 132,337 · ♥296 (볼트 미인제스트)

## 관찰
- **증류 가속층이 이 조직의 본업** — 베이스 모델당 4/8스텝 구성을 표준 출하. 09-04 판정("파생 가속층은 표준 배포 구성품")의 11-28 재확인.
- **정량 벤치를 카드에 두지 않는 경향** — 09-04(Turbo · 가속/품질 수치 미공개)와 11-28(Fusion · 스펙트럼 에너지만 제시 + "지각 품질 점수 아님" 면책) 두 건 모두. "속도를 파는 조직"의 일관된 포지션 — 채택 시 자체 A/B 필수.
- 퓨전물은 **비공식 커뮤니티 파생**이며 베이스(H3) 라이선스가 `other`라 결과물 사용 조건은 베이스 조항이 지배(09-04 경고 이월).

## 관련 페이지
- [[Minimax-h3-Turbo-lightx2v]] · [[Minimax-H3-Turbo-Fusion]] · [[MiniMax-H3]] · [[자기제한-명시]] · [[video-saas]]
