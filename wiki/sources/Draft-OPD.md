---
title: Draft-OPD — On-Policy Distillation로 투기적 디코딩 가속
type: source
domain: ai-news
tags: [ai-news, hf-paper, speculative-decoding, inference, llm, distillation, speed]
created: 2026-06-02
updated: 2026-06-02
sources: []
reliability: medium
---

# Draft-OPD: On-Policy Distillation for Speculative Draft Models

**arxiv**: https://arxiv.org/abs/2605.29343  
**HuggingFace**: https://huggingface.co/papers/2605.29343  
**기관**: Shanghai Jiao Tong University, Shanghai AI Lab, Tsinghua University 등  
**신뢰도**: ⭐⭐⭐ (논문, 유수 기관 공동연구)

## 핵심 인사이트

> [!insight] 핵심 인사이트
> 투기적 디코딩(Speculative Decoding)의 드래프트 모델 훈련 병목 해결. SFT의 "오프라인-추론 불일치" 문제를 On-Policy Distillation(OPD)로 극복 → **EAGLE-3 대비 +23%, DFlash 대비 +13%** 속도 향상. 5× 무손실 가속 달성.

## 도메인별 추출 (ai-news)

**신뢰도**: ⭐⭐⭐ (상해AI연구소 포함 6개 기관 공동, 재현 필요)  
**즉시 활용**: NO — 구현체 공개 여부 미확인, 기술 논문  
**6개월 영향력**: LLM 추론 속도 5× → 로컬 LLM 실용성 대폭 향상 가능  
**대체 관계**: EAGLE-3, DFlash 대비 우월한 드래프트 훈련 방법

**핵심 문제 (SFT의 한계):**
- SFT: 고정된 타겟 모델 생성 궤적으로 학습 → 빠르게 성능 정체
- 원인: "오프라인-추론 불일치" — 학습 분포 ≠ 실제 추론 시 드래프트 분포

**Draft-OPD 해결책:**
- 타겟 보조 롤아웃(target-assisted rollout)으로 안정적 연속 생성
- 검증 노출 오류 위치에서 드래프팅 재실행 (replay)
- 수락/거절 모두에서 타겟 피드백 학습 → 드래프트 유도 오류에 집중 훈련

**결과:**
- 5× 이상 무손실 가속 (thinking 모델)
- EAGLE-3 대비 +23% / DFlash 대비 +13%

> [!note] 배경 정보
> 투기적 디코딩은 대형 LLM 추론 속도를 높이는 현재 가장 실용적인 방법. 드래프트 모델 품질이 핵심 병목인데, 이를 on-policy 방식으로 개선. [[local-llm]] 실배포 시 5× 속도 향상은 게임 체인저.

## 관련 페이지
- [[local-llm]]
- [[AI-에이전트-프레임워크]]

## 원본
- 출처: https://huggingface.co/papers/2605.29343
- 신뢰도: ⭐⭐⭐ (유수 기관 공동, 수치 검증 필요)
