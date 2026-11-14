---
title: "Ropedia Xperience 2 — 3D 스캔 1,589개 + 1인칭 녹화 4,230개(131시간)를 묶은 물리 AI 데이터셋 (arXiv 2611.17060)"
type: source
domain: slam-3dgs
tags: [slam-3dgs, embodied-ai, dataset, 3d-scan, egocentric, simulation, retargeting]
created: 2026-11-14
updated: 2026-11-14
sources: [https://huggingface.co/papers/2611.17060]
reliability: medium
---

**논문**: [arXiv 2611.17060](https://huggingface.co/papers/2611.17060) *Ropedia Xperience 2: A Gold Standard for Scaling Physical AI Environments and Behaviors* · 업보트 **26** · 저자 21명(Hao Li · Fangzhou Hong · Zhaoxi Chen … **Ziwei Liu**) · 발행 2026-11-12 · 코드 Ropedia/Ropedia-Xperience-2 ★16 (HF papers API 볼트 실측 — 수집기와 일치). 수집기 `ai-news` → 볼트 재분류 `slam-3dgs`(3D 스캔 · 임바디드).

## 핵심 인사이트
> [!insight] 스케일링 법칙을 묻기 전에, 무엇을 스케일할지부터 — "환경 × 행동"을 한 번의 캡처로
> 초록 첫 문장: *"Large foundation models such as GPT-6 Astra and Claude Fable 5.1 have recently been shown to control robots directly from visual observations. They nevertheless remain brittle on long-horizon, contact-rich tasks."* (수집기 요약에는 없던 전제 — 같은 주 [[Embodied-First-Exam]] 의 Standard 34% 와 같은 방향의 진단).
> 필요한 자원 두 가지: 과제 수행을 감독하는 **사람 행동 시연**, 정책을 굴려 평가 · 개선할 **상호작용 환경**. 공개물:
> - 미터 스케일 3D 스캔 **1,589개**
> - 74개 과제 1인칭 녹화 **4,230개 · 131시간**
>
> 각 캡처의 재가공: 스캔 장면 → **물리 상호작용 가능한 시뮬레이션 환경** · 사람 동작 → **전신 로봇 궤적 리타깃** · 가상 원격조작 + 자동 장기 궤적 생성으로 로봇 행동 추가.

> [!warning] "Gold Standard"는 제목의 자기 호칭
> 이 데이터로 학습한 정책의 성능, 환경 수 · 행동 수에 따른 스케일링 곡선은 초록에 **없다** — *"laying a data foundation for establishing scaling laws"*(토대 단계). 스캔 → 시뮬 변환의 물리 충실도, 리타깃 성공률도 본문 확인 필요.

## 도메인별 추출 (slam-3dgs)
- **현재 SOTA**: 해당 없음(데이터셋). 규모 수치만 확정.
- **실시간 가능성**: 해당 없음.
- **카메라 파이프라인**: 미터 스케일 3D 스캔 + 1인칭(egocentric) 영상. 스캔 장비 · 표현(메시/가우시안)은 초록에 없다.
- **응용 가능성**: 실내 3D 스캔 1,589개는 [[3DGS]] · SLAM 평가용 장면 풀로 쓸 수 있는지 라이선스 확인 가치가 있다.
- **필수 레퍼런스**: 레포 Ropedia/Ropedia-Xperience-2.

## 관련 페이지
- [[임바디드-AI]] · [[Embodied-First-Exam]] · [[Open-HumanScale]] · [[VLA]] · [[3DGS]] · [[slam-3dgs]]

## 원본
- 출처: https://huggingface.co/papers/2611.17060
- 확인 범위: HF papers API 초록 전문 · 저자 · 🔴 본문 · 데이터 라이선스 · 포맷 미확인
- 신뢰도: ⭐⭐ (업보트 26 · 규모 수치 명시 · 정책 성능 0)
