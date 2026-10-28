---
title: "Rollback (AgiBot World) — 월드모델을 '되감기 가능한 환경'으로: 결정 시점에서 분기·대조해 행동 단위 감독을 만든다. 실로봇 3과제 1위, 8시간 만에 인간 평균 추월(2과제)"
type: source
domain: ai-news
tags: [ai-news, hf-paper, world-model, robot-rl, counterfactual, real-robot, lora, agibot, ge-sim, slam-3dgs]
created: 2026-10-28
updated: 2026-10-28
sources: [https://huggingface.co/papers/2610.36068, https://arxiv.org/html/2610.36068]
reliability: medium
---

# Rollback: Experience Backtracking in World Models for Policy Improvement

**HF**: https://huggingface.co/papers/2610.36068 · published **2026-10-26** · **AgiBot World**(Jiayi Luo · Yang Zhang 외 · 저자 16) · upvote **48**(수집기 일치)
**코드**: 없음(HF `githubRepo` null · 수집기 일치)
**신뢰도**: ⭐⭐ medium(실로봇 수치 있음 · 코드 없음)

> [!insight] 핵심 인사이트 — 물리 환경에는 없고 월드모델에만 있는 능력은 '되감기'다
> 기존 월드모델 RL은 월드모델을 앞으로만 굴리는 대리 환경으로 썼다. Rollback은 **핵심 결정 시점으로 되감아 → 다른 행동으로 분기 → 결과를 대조**해서 성공을 개별 결정에 귀속시킨다. 상상을 중요한 순간에 집중시키고, **별도의 가치모델 없이** 행동 단위 감독을 만든다.
> 시스템: 분산 월드모델 탐색 + 비동기 실로봇 실행. 실제 전이 데이터가 경량 **LoRA**로 월드모델 동역학을 계속 보정한다(**test-time physics grounding**). 월드모델은 **GE-Sim 2.0**에서 초기화했고, 로봇은 양팔 16차원 행동을 30Hz로 제어한다.
> 결과(arXiv Table 1): Block Extraction **69.33%** · Ball Tossing **40.00%** · Tabletop Curling **64.44%**. 평균 기준으로 SFT +17.63 · RECAP +13.71 · RISE w/ GE-Sim2 +11.21%p다. 🎯 같은 월드모델 위에서 **되감기만 추가한 효과(+11.21)가 실세계 RL(+3.92)과 전방 롤아웃(+2.49)을 합친 것보다 크다.**

> [!warning] 주의
> - 📐 **"최강 베이스라인" = RISE w/ GE-Sim2이고, 저자가 직접 재현한 것이다**(*"our reproduction of RISE on the same world model without backtracking"*). 같은 월드모델로 맞춘 공정한 대조이긴 하지만, 원 저자 구현이 아니다 → [[비매칭-비교]]. 모든 방법이 같은 초기화, 약 8시간, 로봇 1대, 비슷한 수의 H200을 썼다.
> - 🎲 평가 규모: 과제당 초기 위치 6곳(Curling은 9곳) × 위치당 15회(Block은 25회). 시드 반복이나 분산은 보지 못했다.
> - 👥 **"인간 추월"은 3명 평균 기준이다**: Ball Tossing 인간 31.48% → Rollback 6시간에 33.33%, 8시간에 40.00% · Curling 인간 58.39% → 4시간에 추월, 8시간에 64.44%. 추월한 것은 2과제뿐이다(Block Extraction에는 인간 비교가 없다). → [[인간-기준선-조건]]
> - 📊 절대 성공률은 아직 낮다. Ball Tossing 40%는 10번 중 6번 실패한다는 뜻이다.
> - 수집기 요약은 +10.67/+11.11/+11.85를 정확히 옮겼다. 다만 **인간 추월 결과(초록 마지막 문장)를 빠뜨렸고**, 최강 베이스라인이 **자체 재현**이라는 점과 절대 성공률도 적지 않았다.

## 도메인별 추출 (ai-news · slam-3dgs 접점)
- **왜 중요한가**: [[월드모델]]을 **반사실 엔진**으로 쓰는 첫 실로봇 실증 사례다. 같은 배치의 [[PDRVLA]](월드모델 = 표현 교사)와 짝을 이룬다. 10-28 하루에 월드모델 용도 3가지가 나란히 나왔다: 교사([[PDRVLA]]) · 반사실 환경(Rollback) · 인터랙티브 생성기([[Hy-Nomas]]). → [[대립레시피-동시도착]]
- **slam-3dgs 연결**: "실제 전이로 시뮬레이터를 LoRA 보정"하는 방식은 SLAM의 온라인 맵 보정과 같은 구조다(실측이 모델을 계속 고친다). 손으로 만든 물리 시뮬레이터에는 없는 성질이다.
- 비교: [[FRED]] · [[LaLa-World]] · [[World-Action-Models-Survey]] · [[Physical-RSI]](실세계↔모델 자기강화 루프) · [[VLA-Corrector]]

## 관련 페이지
- [[월드모델]] · [[VLA]] · [[임바디드-AI]] · [[비매칭-비교]] · [[인간-기준선-조건]] · [[대립레시피-동시도착]]
- 같은 배치(10-28): [[PDRVLA]] · [[Hy-Nomas]] · [[ChronoReplay]] · [[The-Trinity]]
- [[ai-news]] · [[slam-3dgs]]

## 원본
- https://huggingface.co/papers/2610.36068 · https://arxiv.org/html/2610.36068 (§6.1·6.2·6.6)
- 볼트 실측(2026-10-28): upvote 48 · 저자 16 · githubRepo null
