---
title: "P²-MOPD — 다중 교사 온폴리시 증류에 '학생+전문가 파라미터 선형결합'을 학습 가능한 사전지식으로 넣어 절반 스텝에 MOPD 최종치를 넘는다(1.7B 94.7% vs 80.9%)"
type: source
domain: local-llm
tags: [local-llm, hf-paper, distillation, on-policy, task-arithmetic, stepfun]
created: 2026-11-10
updated: 2026-11-10
sources: [https://huggingface.co/papers/2611.03953]
reliability: medium
---

**논문**: [2611.03953](https://huggingface.co/papers/2611.03953) · StepFun · 업보트 **48** · 코드 [SinuoWang/P2-MOPD](https://github.com/SinuoWang/P2-MOPD) ★3 · 생성·푸시 2026-11-05 · `language: null` · license 없음

## 핵심 인사이트
> [!insight] 병합(merge)과 증류(distill)를 같은 손실 아래 한 모델로 본다
> task arithmetic 은 동결된 학생·전문가 파라미터의 span 안에 갇힌다. P²-MOPD 는 그 선형결합을 미분 가능한 하나의 모델로 보고 **혼합 계수와 학생 가중치를 같은 온폴리시 증류 목적으로 동시 최적화**한다. 학생이 계속 학습되므로 전문가는 "사전지식" 역할만 한다. 4개 도메인 × 1.7B·4B, 같은 초기화에서 MOPD 의 **최종 평균 회복률을 절반 스텝에 돌파**, 종료 시 1.7B **94.7% vs 80.9%**(초록 전문 일치).

> [!warning] 초록이 말하지 않은 것
> - **4B 최종 수치 · 도메인 이름 · 도메인별 회복률**이 초록에 없다. "balanced"의 근거(최저 도메인 값)는 본문.
> - 비교는 "same initialization"이라 조건은 맞췄다고 명시 — 이 점은 좋다. 다만 [[DN-MOPD]] 처럼 MOPD 자체를 고친 변형과의 비교는 초록에 없다.
> - 레포는 `language: null` · 생성 당일 푸시 1회 — 코드가 실제로 들어 있는지 볼트 미확인([[선언된-구현체-공백]] 후보, 추정).

## 도메인별 추출 (local-llm)
- **실용성**: 소형(1.7B·4B) 학생에 여러 전문가를 합치는 레시피. 전문가와 학생의 **구조가 같아야** 파라미터 선형결합이 성립한다(구조상 전제, 볼트 추론).
- **트레이드오프**: 학습 중 전문가 가중치를 메모리에 함께 올려야 하는 비용은 초록에 없음.
- **Hermes 적용**: NO — 학습 기법. 로컬 소형 모델을 직접 증류할 때만.
- **오픈소스 구현체**: 미확인(레포 존재만 확인).

## 관련 페이지
- [[온폴리시-증류]] · [[DN-MOPD]] · [[UI-MOPD]] · [[선언된-구현체-공백]]

## 원본
- 출처: https://huggingface.co/papers/2611.03953
- 확인 범위: HF papers API 초록 전문 · GitHub API 메타 · 🔴 본문 · 레포 내용 미열람
- 신뢰도: ⭐⭐ (업보트 48 · ★3)
