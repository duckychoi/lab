---
title: "Learning the Task or Learning the Verifier? — 체화 자기개선 에이전트의 판정 기준 노출(CE) 점검"
type: source
domain: slam-3dgs
tags: [slam-3dgs, robotics, embodied, benchmark, verifier-overfitting, paper]
created: 2026-11-16
updated: 2026-11-16
sources: [https://huggingface.co/papers/2611.08318]
reliability: medium
---

**논문**: arXiv 2611.08318 · HF 업보트 21 · 저자 13명(Wenbo Huang … Shukai Gong · **Daquan Zhou**) · HF 조직 `DAGroup-PKU` · 코드 링크 없음 · HF Daily 11-13 페이지.

## 핵심 인사이트
> [!insight] 높아진 점수가 과제를 배운 건지, 채점기를 배운 건지
> 로봇 시뮬 벤치의 성공 판정 기준은 원래 **모방학습 정책 검증용**으로 쓰여서 언어 지시보다 더 많이 요구하는 경우가 많다. 최근 자기개선 체화 코딩 에이전트 연구 다수가 이 기준을 에이전트에 노출(Criteria Exposure, CE)한다. 통제 실험 결과: CE 하에선 주어진 기준의 성공률이 빨리 오르지만 **지시를 벗어나지 않는 범위에서 기준을 살짝 바꾸면 우위가 사라지고**, CE 하에서 만든 스킬은 과제 간 전이가 나쁘다. 대안: 지시 충실형(instruction-faithful) 기준. → [[분포내-우위]] · [[벤치-개조-재평가]] 의 로봇판.

## 도메인별 추출 (slam-3dgs)
- **현재 SOTA**: 해당 없음 — 이 논문은 SOTA 주장들의 **측정 타당성**을 겨냥한다.
- **응용 가능성**: 로봇 · 체화 에이전트 논문을 읽을 때 "에이전트가 성공 판정 코드를 볼 수 있었나"를 첫 질문으로 둘 근거.
- **필수 레퍼런스**: YES(평가 방법론) — 다만 초록에 정량 수치 0건. 어떤 벤치 · 어떤 선행 연구가 CE 를 썼는지는 본문 확인 필요.

> [!question] 미해결
> 우위가 "사라진다"의 크기, 기준 변경의 구체 형태, 지시 충실형 기준이 기존 순위를 어떻게 바꾸는지 — 본문 미열람.

## 관련 페이지
- [[DAGroup-PKU]](3번째 논문 · 마지막 저자 Daquan Zhou 동일) · [[PhysLoop]] · [[G-STAR]] · [[임바디드-AI]] · [[분포내-우위]] · [[벤치-개조-재평가]] · [[요약자와-판정자-분리]] · [[VLA]]

## 원본
- 출처: https://huggingface.co/papers/2611.08318
- 확인 범위: HF papers API 초록 전문 · 저자 13명 · 조직 필드(볼트) · 🔴 본문 미열람
- 신뢰도: ⭐⭐ (수치 0 · 방법론 논문)
