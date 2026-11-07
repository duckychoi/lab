---
title: "VFlash — 궤적·박스를 프리미티브 단위로 한 번에 디코딩. '약 25배'는 3D 점 예측에서 정확도를 내준 결과"
type: source
domain: slam-3dgs
tags: [slam-3dgs, robotics, vla, visual-planning, trajectory, speculative-decoding, nvidia, hf-paper]
created: 2026-11-07
updated: 2026-11-07
sources: [https://huggingface.co/papers/2611.08449]
reliability: medium
---

**HF**: upvote **96**(볼트 11-07 재조회 · 수집기 11-06 관측 54 · 11-06 목록 1위) · NVIDIA · 저자 19명 · arXiv 2611.08449 · `githubRepo` **None(코드 미공개)**

## 핵심 인사이트
> [!insight] 토큰 일치를 요구하지 않는 드래프트 — "구조적으로 유효하면 수용"
> 로봇·자율주행 VLM 은 점·박스·궤적을 좌표 토큰 하나씩 자기회귀로 낸다. VFlash 는 **경량 drafter 가 프리미티브 전체를 1 forward 로 예측**하고, 투기적 디코딩과 달리 **타깃 AR 모델의 토큰열 재현(target-token agreement)을 요구하지 않는다** — 구조적으로 유효하면 그대로 쓴다. 그래서 속도 상한이 수용률에 묶이지 않는다. 대가는 "타깃과 같은 답"이라는 보장이 사라진다는 것이다.

> [!warning] 속도 25배가 나온 표에서 정확도는 타깃보다 나쁘다 (볼트 본문 대조)
> - **Table 5(PointMotionBench)** HOT3D: MolmoMotion-AR `ADE ↓` **0.109** · `PWT ↑` **0.444** vs VFlash **0.122** · **0.391**(볼트 행 직접 확인). 본문: *"Its ADE ranks second on HOT3D and WorldTrack, behind AR … although WorldTrack FDE increases by 15% and PWT is 7–12% lower across the three datasets."*
> - 같은 표에서 DAVIS ADE/FDE 는 27%/19% 개선 — **데이터셋별로 엇갈린다**.
> - 속도 "약 25배" = **H100 1장 · 배치 1 · 단일 롤아웃**, VFlash 3.21 s vs AR 79.8 s(HOT3D) 등 24.8/23.5/26.4배(부록 F.3). 초록도 속도를 *"Preliminary"* 로 한정한다(볼트 본문 grep 1건).
> - "consistently reduces errors"는 **2D·3D 로봇 궤적** 과제(Table 4: AgiBot ADE 0.130→0.041 · SR@5 0.456→0.739)에 한정된다 → [[한정어-탈락]] · [[배수-조건분산]].

## 도메인별 추출 (slam-3dgs)
- **현재 SOTA**: Table 6 MolmoSpaces `Avg.` Baseline 62.6 → VFlash 70.2(같은 WAM, 텍스트 인코더만 교체). 단 `Close` 열은 PrimeR0 81.3 · Cosmos3-Nano-Policy 79.1 · WALL-OSS-0.5 78.5 가 VFlash 77.0 보다 높다(수집기 기준).
- **실시간 가능성**: 단일 롤아웃 3~4 s(H100) — 실시간 제어 루프(수십 ms)에는 아직 멀다. "AR 대비 25배"가 의미 있는 것은 계획(planning) 단계.
- **응용 가능성**: 휴머노이드/로봇 VLA 의 계획 출력 지연 단축 아이디어로 [[VLA]] 계열과 연결. 코드 미공개라 재현 불가.
- **필수 레퍼런스**: Table 4~6 + 부록 F.3.

## 관련 페이지
- [[VLA]] · [[임바디드-AI]] · [[NVIDIA]] · [[월드모델]]
- [[한정어-탈락]] · [[배수-조건분산]] · [[표-부분인용]]
- 같은 날 논문: [[BestRand]] · [[Harness-S]] · [[TailSteer]] · [[WeLM-Image]]

## 원본
- 출처: https://huggingface.co/papers/2611.08449 · https://arxiv.org/html/2611.08449v1
- 확인 범위: HF papers API(볼트 11-07) · arXiv HTML 전문 텍스트 grep — 수집기 인용 12개 수치 전부 검출 · Table 5 HOT3D 행 · "15%" 문단 볼트 직접 확인 · Table 6 `Close` 열 경쟁 행은 수집기 기준 · 실행 0회
- 신뢰도: ⭐⭐ (NVIDIA · 코드 없음 · 속도는 Preliminary)
