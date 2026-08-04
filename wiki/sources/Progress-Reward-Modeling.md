---
title: Progress Reward Modeling for Robotic Learning — 진행도 리워드 서베이
type: source
domain: ai-news
tags: [ai-news, hf-paper, robotics, reward-modeling, rl, survey, embodied-ai]
created: 2026-07-28
updated: 2026-07-28
sources: []
reliability: medium
---

# Progress Reward Modeling for Robotic Learning: A Survey (논문 2607.21655)

> [!insight] 핵심 인사이트
> 로봇 학습에서 **진행도(progress) 기반 리워드 모델링**을 통합 정리한 종합 서베이. HF 논문 2607.21655·업보트 **53**. 저자 Keliang Wu 외 10인, **Northwestern·CMU·UW-Madison·UCSB·UIUC** 다기관. 핵심 프레이밍: 기존 리워드가 **최종 성공(terminal success)** 신호에만 의존해 롱호라이즌 태스크에서 학습 신호가 희소한 문제를, **"현재 관측을 진행 중인 긴 태스크의 전개 위에 위치시키는"** 진행도 추정으로 촘촘히 채운다. 세 관점으로 분야 조직화 — **①인터페이스**(진행도 모델이 무엇을 받고 어떤 신호를 내는가), **②구성 방법**(진행도 리워드를 어떻게 만드는가), **③데이터·평가**(품질 검증). 네 구성 패러다임: 동결 파운데이션 모델·시간/상대 학습·지시튜닝 예측·프로그램적 리워드 생성. 07-25 [[K12-KGraph]]·07-27 [[Skill-Self-Play]]가 "학습 신호를 구조화"한 계보의 **로보틱스판** — 리워드 자체를 진행도로 밀도화.

> [!warning] 서베이 · 미래형 ID
> 초록·프레임워크를 WebFetch로 확인. 서베이 특성상 신규 실험·벤치가 아닌 **문헌 정리**라 원저작 성능은 각 인용 논문에 귀속. 논문 ID(2607.21655)가 미래형이라 원문 재현 전 medium.

## 도메인별 추출 (ai-news / slam-3dgs·로보틱스 교차)

- **신뢰도**: ⭐⭐ — 초록·4패러다임 WebFetch 실확인, 서베이·미래형 ID로 medium. 개별 기법 성능은 원논문 검증 대상.
- **즉시 활용**: NO(간접) — 물리 로봇 직접 응용은 내 워크로드 밖이나, **"희소한 최종 보상을 진행도로 조밀화"**는 에이전트 RL([[Molt]]·[[Skill-Self-Play]])·롱호라이즌 태스크 평가에 이식 가능한 발상.
- **6개월 영향력**: 임보디드/에이전트 RL에서 리워드 설계가 "성공/실패 이진"에서 **진행도 밀도 신호**로 이동하는 흐름의 지형도. 진행도 모델을 리워드로 쓰는 표준화가 진행되면 롱호라이즌 학습 진입장벽 하락.
- **대체 관계**: 최종 성공 리워드·수작업 shaping 대비 **학습된 진행도 신호**. VLA·임보디드 트래킹([[ReferTrack]])의 학습 신호 하부 이론과 연결.
- **허와 실**: 서베이라 자체 신규성보다 **분류·프레임워크 제공**이 가치. 네 패러다임 중 실전 효용은 도메인·로봇 종류별 편차 큼.
- **액션**: "진행도=조밀 리워드" 프레이밍을 내 에이전트 태스크(롱호라이즌 스케줄·멀티스텝 위키 인제스트)의 중간 진척 평가 지표 설계에 참고.

## 관련 페이지
- [[ReferTrack]]
- [[Molt]]
- [[Skill-Self-Play]]
- [[온폴리시-증류]]
- [[ai-news]]

## 원본
- 출처: https://huggingface.co/papers/2607.21655 — 업보트 53
- 저자: Keliang Wu·Haoran Lu·Anbang Liu 외 (Northwestern·CMU·UW-Madison·UCSB·UIUC)
- 핵심: 진행도 리워드 3관점(인터페이스·구성·데이터/평가), 4패러다임(동결 파운데이션·시간/상대 학습·지시튜닝 예측·프로그램적 생성)
- 신뢰도: ⭐⭐ (초록·프레임워크 실확인, 서베이·미래형 ID·재현 전 medium)
