---
title: 하네스형 에이전틱 RL — 하네스가 루프를 소유하고 트레이너는 요청–응답만 본다
type: concept
domain: ai-news
tags: [ai-news, concept, agentic-rl, harness, 신설]
created: 2026-09-19
updated: 2026-09-19
sources: [agent-lightning.md, NeoHorse-1-Paper.md, SoL-Pi.md]
reliability: medium
---

# 하네스형 에이전틱 RL (Harnessed Agentic RL)

> [!insight] 한 줄
> **배포 때 쓰는 하네스를 그대로 학습 환경으로 쓰고, 트레이너는 프록시로 요청–응답 쌍만 관측한다.** 에이전트 코드 변경 0. 이름은 [[agent-lightning]] v1.0 보고서가 붙였다.

## 하네스를 학습에 쓰는 세 방식 (볼트 보유)
- **온라인 RL** — [[agent-lightning]]: 하네스 = RL 환경. Qwen3.5-9B SWE-bench Verified 41.8→56.4(6K 샘플)
- **오프라인 SFT·OPD** — [[NeoHorse-1-Paper]]: 배포 궤적 → 학습 데이터 + 라우팅 커리큘럼. 루프 1회
- **하네스 자체 진화** — [[SoL-Pi]] · [[ModularRSI]]: 모델 불변, 하네스 코드를 선택압으로 개선
→ 상위 축: [[하네스-설계-축]]

## 🎯 새 난점 — **단위 문제**
하네스가 루프를 소유하면 **롤아웃 1개 ≠ 샘플 1개**다: 단일 샘플로 남는 롤아웃 평균 36% · 롤아웃당 평균 **2.41 샘플**. → 어드밴티지·손실 정규화를 **롤아웃 단위**로 계산해야 한다는 것이 agent-lightning 의 주장. 프레임워크 간 선택이 갈린다(verl Uni-Agent·Polar vs slime·AReaL — 🔴 볼트 미대조).
🔴 agent-lightning 절제가 **비단조**(어드밴티지만 고치면 33.1 < 기준 35.0 < 전부 38.2) — 부품 하나만 가져다 쓰면 오히려 나빠질 수 있다.

## 🔴 공통 전제 — 보상 신호를 지키려면 네트워크를 막아야 한다
agent-lightning 코딩 에이전트 보상해킹 4종 중 **3종이 네트워크 경유** → K8s 허용목록. [[DeepSWE]] Pier 와 같은 해법. [[K2-Horizon-7B]] 의 "SWE-bench 답안 다운로드 → 82점"도 같은 계열.

## 관련 페이지
- [[하네스-설계-축]] · [[agent-lightning]] · [[NeoHorse-1-Paper]] · [[SoL-Pi]] · [[ModularRSI]] · [[DeepSWE]] · [[RSI-프레이밍]]
