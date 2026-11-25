---
title: "Nemotron — NVIDIA Nemotron 모델 패밀리 학습 레시피 · 배포 쿡북 · 단계(step) CLI 허브"
type: source
domain: ai-news
tags: [ai-news, github, nvidia, training-recipes, rlvr, grpo, nemotron, open-weights]
created: 2026-11-25
updated: 2026-11-25
sources: [https://github.com/NVIDIA-NeMo/Nemotron]
reliability: high
---

**레포**: NVIDIA-NeMo/Nemotron · ★ **2,389**(수집기 11-25 = 볼트 API 11-25 일치) · Jupyter 일간 Trending(당일 +9) · Apache-2.0 · 레포 ID 1069235905 · 생성 2025-10-03 · push 2026-11-23 · 최신 릴리스 v0.2.0(2026-10-15)

## 핵심 인사이트
> [!insight] 가중치 레포가 아니라 "재현 레시피" 허브 — 모델 공개의 다음 단계는 학습 절차 공개
> Nemotron 계열의 **학습 파이프라인 재현 코드** 모음. README 레시피 표: Nemotron 3 Ultra(550B/활성 55B, NVFP4 20T 토큰 사전학습, 1M 컨텍스트 — 레시피는 Pretrain → SFT까지만) · 3 Super(120.6B/12.7B, **21개 보상 환경 RLVR + SWE-RL + RLHF, 비동기 GRPO 1K GPU**) · 3.5 Super(120B/12B VLM) · 3 Nano(31.6B/3.6B) · 3.5 Lightning(30B/3B, MTP) · 3.5 Transcribe(34B/4.3B 음성) · 3 Nano Omni(30B/3B, 4모달) · Embed · Rerank · 3.5 Parse. 그 밖에 `nemotron steps` CLI(데이터 큐레이션 · SDG · 번역 · SFT/PEFT/RL · 변환 · 평가를 YAML로 조립)와 Claude Code 플러그인 `nemotron-customize`(단계 DAG를 계획 · 검증해 YAML 생성). [[파라미터-다중표기]] 다수(550B/55B · 120.6B/12.7B 등).

> [!warning] README가 스스로 밝힌 한계
> **레시피는 공개 데이터 부분집합만 쓰므로 기술보고서 벤치 수치와 결과가 다르다**, 3.5 Super의 SFT · RL 데이터와 에이전트 교사 환경은 **아직 미공개**. README 자체에 벤치 수치 없음.

## 도메인별 추출 (ai-news)
- **실용성**: 수백~수천 GPU급 재현용이라 개인 환경과는 거리가 멀다. 실사용 후보는 **Embed · Rerank 도메인 파인튜닝 레시피** 정도.
- **즉시 활용**: `nemotron-customize` Claude Code 플러그인 — "학습 단계를 에이전트가 DAG로 계획"하는 접근은 워크플로우 관점에서 참고 가능(실행은 안 해봄).
- **액션**: 없음(관찰).

## 관련 페이지
- [[NVIDIA]] · [[파라미터-다중표기]] · [[ai-news]]

## 원본
- 출처: https://github.com/NVIDIA-NeMo/Nemotron
- 확인 범위: README(수집기 11-25) · GitHub API 재확인(볼트 11-25 — ★ · 라이선스 · 레포 ID · 생성일 · push 일치) · 실행 0
- 신뢰도: ⭐⭐⭐ (★2.4천 · NVIDIA 공식 · 단 레시피가 부분집합이라는 자기 한계 명시)
