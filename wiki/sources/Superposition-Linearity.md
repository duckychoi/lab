---
title: "Superposition Linearity — 선형성은 학습으로 생기지 않고 학습할수록 사라진다"
type: source
domain: local-llm
tags: [local-llm, ai-news, interpretability, transformer, superposition, decoding, 검사가능성-후퇴]
created: 2026-09-26
updated: 2026-09-26
sources: []
reliability: low
---

# Your Transformer Can Hold Two Thoughts at Once

> [!insight] 핵심 인사이트 — **창발의 반대 방향**
> 두 개의 서로 다른 텍스트 스트림 입력을 **선형 결합**하면 출력이 각 next-token 분포의 **중첩(superposition)** 으로 나온다 — 이를 **Superposition Linearity Hypothesis** 라 명명한다.
> 🎯 **반직관 지점이 논문의 값이다**: *"superposition is an **intrinsic property of the Transformer architecture** rather than an emergent consequence of training; in fact, we observe that it tends to **diminish as pretraining progresses**."*
> 📌 볼트가 쌓아 온 대부분의 관측은 *"학습하면 능력이 생긴다"* 방향이다. 이 논문은 **구조가 이미 갖고 있던 성질을 학습이 깎아낸다**고 말한다. 사실이라면 [[월드모델]]·창발 논의 전반에 **"창발인가 잔존인가"** 라는 구분선이 하나 더 생긴다.
> 실용 귀결: 경량 파인튜닝으로 선형성을 상당 부분 **복원**할 수 있고, guided decoding 으로 **단일 forward pass에서 일관된 두 개의 연속 생성**을 분리해 낸다.

> [!warning] 🔴 초록에 정량 수치가 **0개** — 대조 불가
> 볼트가 초록 전문을 토큰 단위로 검사했다: **숫자 토큰 0개.** *"significantly reducing the divergence"* · *"substantially restored"* · *"tends to diminish"* — **전부 방향어이고 값이 없다.**
> 🔴 따라서 다음을 **하나도 말할 수 없다**: 중첩 오차가 얼마인지 · 사전학습 단계별로 얼마나 감소하는지 · 복원율이 몇 %인지 · 두 생성의 품질 저하가 얼마인지.
> 📌 09-24 [[Spatial-Interactor]]·[[RewardVerse]] 에 이어 **수치 0개 논문 3번째**이고, 볼트 *"미대조 논문"* 누적은 [[BPO]] 포함 **5건**이 된다. reliability **low**.
> ⚠️ 부속 GitHub **없음**(HF API `githubRepo: None` — 이건 수집기 누락이 아니라 실제 부재다).

## 도메인별 추출 (local-llm)

- **실용성 판단**: ⬜ **현재로선 아니다.** guided decoding 으로 1패스 2생성이 되면 **추론 비용이 실질 절반**이 될 수 있어 파급이 크지만, **속도·품질 수치가 0개**라 이득을 추정할 근거가 없다. 구현체도 없다.
- **메모리 아키텍처**: 직접 해당 없음. 단 *"한 forward pass가 두 맥락을 동시에 유지한다"* 는 결과는 **KV 재사용·배치 병합** 설계에 시사점이 있다 — 두 대화를 물리적으로 겹쳐 돌리는 방식이 이론적으로 정당화될 여지.
- **Hermes 적용**: **NO(현시점).** 파인튜닝으로 선형성을 복원해야 하고, 복원 비용·효과가 미제시다. [[hermes-agent]] 는 API 모델 기반이라 **개입 지점 자체가 없다.**
- **트레이드오프**: ⬜ **전부 미상.** 유일하게 말할 수 있는 정성 트레이드오프는 *"사전학습을 더 할수록 이 성질이 나빠진다"* 는 것 — 즉 **최신·고성능 모델일수록 이 기법이 덜 먹힐 가능성**이다. 이건 실용성에 불리한 방향이다.
- **오픈소스 구현체**: **없음.**

> [!question] 미해결 질문
> *"diminish as pretraining progresses"* 가 모델 규모와 어떻게 얽히는가? 규모↑와 학습량↑이 분리되지 않으면 *"큰 모델일수록 안 된다"* 인지 *"많이 배운 모델일수록 안 된다"* 인지 구분되지 않는다. **초록만으로는 판별 불가.**

## 관련 페이지
- [[검사가능성-후퇴]] · [[한정어-탈락]] · [[측정도구-먼저-반증]]
- [[Mamba4]] · [[월드모델]] · [[hermes-agent]]

## 원본
- 출처: https://huggingface.co/papers/2609.29845 (arXiv 2609.29845)
- 실측(2026-09-26 HF API): upvote **58**(수집기와 **완전일치**) · `publishedAt` **2026-09-24** · 저자 **9명** · githubRepo **없음**
- 수집기 대조: upvote·제목 일치 · *"정량 수치 0개"* 판정 **볼트 독립 확인 — 정확**
- 확인 범위: **초록 전문(숫자 토큰 0개 확인).** 🔴 본문 미열람
- 신뢰도: ⭐⭐ **low** — 주장은 흥미로우나 **초록 단계에서 대조할 값이 하나도 없다**
