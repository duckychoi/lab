---
title: "Duo v1 — 지각하면서 동시에 응답하는 전이중 "Reciprocal World Model" 기술 보고서 (arXiv 2611.15131)"
type: source
domain: video-saas
tags: [video-saas, full-duplex, audio-video-generation, world-model, realtime, technical-report]
created: 2026-11-14
updated: 2026-11-14
sources: [https://huggingface.co/papers/2611.15131]
reliability: low
---

**논문**: [arXiv 2611.15131](https://huggingface.co/papers/2611.15131) *Duo: A Reciprocal World Model for Full-Duplex Interaction* · 업보트 **38**(수집기: 25) · 저자 20명(Hengyuan Cao · Biao Gong … Zhenzhong Lan) · 발행 2026-11-11 (HF papers API 볼트 실측). 수집기 `ai-news` → 볼트 재분류 `video-saas`(실시간 시청각 생성).

> [!note] 수집기 "코드 링크 없음" — 지금은 있다
> HF papers API `githubRepo` = `inclusionAI/Duo`. GitHub API: ★38 · Apache-2.0 · created 2026-11-06(볼트 실측 11-14). 수집 시점(11-13)에 링크가 없었을 수 있다 — 오류 확정이 아니라 시점 차이일 가능성. 레포 내용(가중치 포함 여부)은 미열람.

## 핵심 인사이트
> [!insight] 영상 생성 모델에게 "지시를 이해"시키는 대신 "대화에 참여"시킨다
> Reciprocal World Model(RWM): 지능과 물리 현실을 월드의 동등한 구성요소로 본다. 기존 월드모델은 물리 쪽만 시뮬레이션하고 추론·결정은 외부 제어로 남긴다는 문제 제기.
> - **Intent**(자기회귀): 연속 상호작용 추론과 **참여 결정**(언제 말하고 언제 끼어드는가).
> - **Realization**: 일관된 시청각 행동 생성.
> - 두 모듈을 청크 단위 공통 타임라인으로 동기화, 미래 입력을 막는 어텐션 마스크, 자기 생성 이력으로 학습하는 **dual rollout distillation**(분포 이동 완화).
> 실시간 오디오 · 비디오 · 텍스트를 계속 지각하며 끼어들기를 포함한 전이중 대화, 실물 보여주기 · 가상 장면 수정 · 시청각 게임.

> [!warning] 정량 평가 전무 · 예고성 보고서
> 초록에 벤치 · 지연시간 · 해상도 · 하드웨어 수치가 없다. *"The release of Duo v1 makes our first step, with the next version coming soon."* reliability `low`.
> "월드모델"이라는 말이 같은 날 [[BirdDreams]](주행 장면 예측)와 전혀 다른 대상을 가리킨다 — [[월드모델]] 용어 범위가 넓어지는 사례.

## 도메인별 추출 (video-saas)
- **기능 벤치마킹**: 실시간 아바타 대화(끼어들기 포함). 구현 난이도 최상 — 재현 근거 없음.
- **크리에이터 인사이트**: "프롬프트 → 클립"이 아니라 "말로 장면을 고친다"는 상호작용 형식.
- **경쟁 우위 빈틈**: 지연시간이 공개되면 그때 판단.
- **프롬프트 패턴 / 워크플로우 / 디자인 레퍼런스**: 해당 없음.

## 관련 페이지
- [[월드모델]] · [[BirdDreams]] · [[AI-영상-생성-2026]] · [[HeyGen]] · [[video-saas]]

## 원본
- 출처: https://huggingface.co/papers/2611.15131
- 확인 범위: HF papers API 초록 전문 · 저자 · GitHub API(inclusionAI/Duo 메타) · 🔴 본문 · 레포 내용 미열람
- 신뢰도: ⭐ (수치 0 · 예고성)
