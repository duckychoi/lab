---
title: "Game2Player — 빌더 에이전트가 웹게임을 검증 가능한 과제로 개조, 플레이어가 풀며 데이터 수집 (PlayerBench 14.3 → 31.2%)"
type: source
domain: slam-3dgs
tags: [slam-3dgs, vla, game-agent, embodied, data-generation, paper]
created: 2026-11-19
updated: 2026-11-19
sources: [https://huggingface.co/papers/2611.24154]
reliability: medium
---

**논문**: arXiv 2611.24154 · 업보트 21(볼트 · 수집기 20) · UIUC · 코드 [game2player/Game2Player](https://github.com/game2player/Game2Player) (🆕 볼트 확인 — 수집기 미기재)

## 핵심 인사이트
> [!insight] "개선을 식별 가능하게" 만드는 쪽에 투자했다 — 상태 기반 성공 판정
> Builder 에이전트가 기존 웹게임을 개조해 **내부 상태를 노출**하고 상태 기반 진척 지표 · 성공 판정이 있는 과제를 정의 → Coding Player · VLM Player 가 풀며 문제를 Builder 에 보고 → 수리. 플레이가 곧 **환경 검증 + 학습 데이터**. 같은 날 [[Resolution-Hypothesis]] 의 처방("진짜 개선을 검출 가능하게")과 같은 방향이다.

## 도메인별 추출 (slam-3dgs)
- **현재 SOTA (초록 · 볼트 대조)**: 검증 게임 568 · 과제 3,436 · 궤적 15.7K(307시간), 50게임 홀드아웃 PlayerBench. 진척 가중 SFT 의 Game2Player-9B: PlayerBench **14.3 → 31.2%**, 외부 GameWorld **30.0 → 53.1%**.
- **실시간 가능성**: 해당 없음(웹게임 · 턴 단위 여부 미확인).
- **응용 가능성**: 사람 플레이 수집 없이 검증 가능한 궤적 데이터를 만드는 경로 — 로봇 시뮬 과제 자동 생성과 같은 구조.

> [!warning] 단서
> ① PlayerBench 는 같은 파이프라인이 만든 홀드아웃 — [[분포내-우위]] 성격, 외부 GameWorld 가 더 의미 있다 ② 절대 수준은 여전히 절반 안팎 ③ [[Gamer]](11-16)와 달리 실시간 키보드 · 마우스 조작이 아니다.

## 관련 페이지
- [[Gamer]] · [[VLA]] · [[임바디드-AI]] · [[UIUC]] · [[분포내-우위]] · [[Resolution-Hypothesis]]

## 원본
- 출처: https://huggingface.co/papers/2611.24154
- 확인 범위: HF papers API(초록 전문 · 업보트 · 조직 · githubRepo) · 🔴 본문 표 미열람
- 신뢰도: ⭐⭐⭐
