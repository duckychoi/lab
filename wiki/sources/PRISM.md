---
title: PRISM — SFT→RL 사이 분포 정렬 멀티모달 강화학습
type: source
domain: ai-news
tags: [ai-news, rl, multimodal, alignment, distillation, sft, rlvr]
created: 2026-05-07
updated: 2026-05-07
sources: []
reliability: medium
---

# PRISM: Pre-alignment via Black-Box On-Policy Distillation for Multimodal RL

> [!insight] 핵심 인사이트
> SFT(지도학습 파인튜닝)와 RL(강화학습) 사이에 **분포 정렬 단계(pre-alignment)** 를 삽입해 멀티모달 RLVR 성능을 향상. 4B 모델 +4.4p, 8B 모델 +6.0p 성능 개선. "SFT → RL 갭"이 학습 비효율의 주요 원인임을 실증.

**HuggingFace**: https://huggingface.co/papers/2604.28123  
**업보트**: 30 (2026-05-06 기준)  
**신뢰도**: ⭐⭐⭐

## 도메인별 추출

- **신뢰도**: 업보트 30, arXiv 논문 — 중간 수준. 벤치마크 재현 필요
- **즉시 활용**: 직접 적용보다 훈련 파이프라인 설계 시 참고. SFT 후 RL 적용 시 분포 정렬 단계 추가 검토
- **6개월 영향력**: 멀티모달 RL 훈련 표준 파이프라인에 pre-alignment 단계가 포함될 가능성
- **대체 관계**: [[Near-Future-Policy-Optimization]], [[Accelerating-RL-Post-Training]] 등 RL 후훈련 개선 연구 클러스터
- **허와 실**: 블랙박스 온-폴리시 증류 방식 — 교사 모델 접근 없이 가능하다는 장점. 실제 배포 환경에서의 일반화 검증 필요

> [!note] 배경 정보
> RLVR(Reinforcement Learning from Verifiable Rewards) — 검증 가능한 보상 신호로 LLM을 강화학습. 수학·코딩 등 정답이 명확한 태스크에 효과적.

## 관련 페이지
- [[HeavySkill]]
- [[Near-Future-Policy-Optimization]]
- [[Reward-Hacking-Large-Models]]

## 원본
- 출처: https://huggingface.co/papers/2604.28123
- 신뢰도: ⭐⭐⭐ (업보트 30)
