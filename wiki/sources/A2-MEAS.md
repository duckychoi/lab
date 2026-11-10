---
title: "A2-MEAS — 교정 코드로 실패를 복구하는 체화 멀티에이전트. BEHAVIOR 2026 100과제 Q-score 0.6411, '2.21배'는 초록 스스로 벤치 에디션이 다르다고 밝힌 비교"
type: source
domain: slam-3dgs
tags: [slam-3dgs, hf-paper, vla, embodied, multi-agent, sjtu, behavior, robotwin]
created: 2026-11-10
updated: 2026-11-10
sources: [https://huggingface.co/papers/2611.09124]
reliability: medium
---

**논문**: [2611.09124](https://huggingface.co/papers/2611.09124) *Toward the Era of Agentic Embodied Intelligence* · AutoLab(SJTU) · 업보트 **43** · 코드 [AutoLab-SAI-SJTU/A2MEAS](https://github.com/AutoLab-SAI-SJTU/A2MEAS) ★8(수집 시 1) · Apache-2.0 · 푸시 2026-11-10T01:21Z

## 핵심 인사이트
> [!insight] 실패 복구를 "가중치 재학습"이 아니라 "새 코드 주입"으로 푼다
> 학습된 **교정 코드**(교정 언어 · 공간 증거 · 실행 이력 · 행동 제안)를 MetaBrain 이 학습 감독과 런타임 안내로 준다. 학습 중에는 correction encoder·adapter 가 정책 가중치에 흡수하고, 배포 시에는 **가중치를 동결한 채 새 코드로 적응**한다. 행동 모델 A2-WLA 는 [[VLA]] 정책에 모션 인지 이력 + 잠재 [[월드모델]] 을 더했다.

> [!warning] 수치별 조건 (초록 전문 대조 · 전건 일치)
> - **0.5755 = "2025 우승팀 0.2605 의 2.21배"** — 초록이 직접 *"across different benchmark editions and training configurations"* 라고 단다. 저자가 스스로 붙인 [[비매칭-비교]] 표지이며, 배수는 진전의 크기가 아니다. 또한 0.5755 는 50과제 서브셋 · 온라인 교정 **전** 값.
> - 100과제 전체: Q-score **0.6411** · 과제 성공 **45.40%** — 절반 이상 실패.
> - RoboTwin 2.0: A2-WLA 93.98% → 전체 시스템 95.05%(**+1.07%p**). 교정 계층의 몫은 포화 벤치에서 작게 보인다.
> - 실로봇 12과제 · 5개 가정환경: **57.92% vs π0.5 26.67%**. 시행 횟수는 초록에 없음.
> - 핸드드립 커피: 필터 다루기 두 단계 실패 후 완료율 **14→94% · 8→82%** — 비교 대상은 "A2-WLA 재시도". 특정 두 단계의 값이다.
> - 427.1 samples/s = π0.5 **참조 구현**의 4.03배(동일 HW).

> [!note] 공개 상태
> 초록은 "will release". 레포는 Apache-2.0 · 오늘 푸시가 있으나 볼트는 내용 미열람 — 시스템·모델·학습 스크립트 공개 여부 미확인.

## 도메인별 추출 (slam-3dgs)
- **현재 SOTA**: BEHAVIOR 2026 공개 과제 기준 자기 보고. 리더보드 순위는 초록에 없음.
- **실시간 가능성**: 추론 지연 수치 없음(학습 처리량만).
- **응용 가능성**: "동결 가중치 + 런타임 교정 코드"는 [[국소-수리-원리]] 의 로봇판 — 전체를 다시 하지 않고 실패 지점만 고친다. 오늘 배치 [[PCBRouteAgent]] 도 같은 구조.
- **필수 레퍼런스**: BEHAVIOR 2026 · RoboTwin 2.0 원 벤치 정의(볼트 미보유).

## 관련 페이지
- [[VLA]] · [[임바디드-AI]] · [[월드모델]] · [[국소-수리-원리]] · [[비매칭-비교]] · [[PCBRouteAgent]] · [[mujoco]] · [[Open-HumanScale]]

## 원본
- 출처: https://huggingface.co/papers/2611.09124
- 확인 범위: HF papers API 초록 전문(수치 전건 검출) · GitHub API 메타 · 🔴 본문 · 레포 내용 미열람
- 신뢰도: ⭐⭐ (업보트 43 · ★8 · 자체 측정 · 공개 예정)
