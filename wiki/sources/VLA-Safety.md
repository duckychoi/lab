---
title: VLA Safety — 비전-언어-행동 시스템 위협·방어 종합 조사
type: source
domain: ai-news
tags: [ai-news, hf-paper, vla, safety, survey, robotics, defense, threat-analysis]
created: 2026-04-28
updated: 2026-04-28
sources: []
reliability: medium
---

# Vision-Language-Action Safety (HF arXiv 2604.23775, upvotes: 35)

> [!insight] 핵심 인사이트
> VLA(Vision-Language-Action) 시스템 — 즉, 보고·판단하고·행동하는 로봇/에이전트 AI — 의 안전성 위협을 체계적으로 분류. 적대적 입력, 분포 이탈, 물리 세계 결과의 비가역성 등 일반 LLM 안전과 다른 VLA 특유의 위험을 다룸. [[ASGuard]](jailbreak 방어)와 함께 AI 안전 클러스터 형성.

**HuggingFace**: https://huggingface.co/papers/2604.23775  
**upvotes**: 35 (2026-04-28 기준)  
**신뢰도**: ⭐⭐⭐ — arXiv 서베이, upvotes 35

## 핵심 인사이트

> [!note] 배경 정보
> VLA 시스템은 텍스트·이미지 입력을 받아 물리 세계의 행동(로봇 팔 제어, 자율주행 등)을 출력. 오작동이 디지털 오류가 아니라 물리적 피해로 이어지므로 일반 LLM 안전과 완전히 다른 위험 프로파일. 위협·도전·평가·방어 4개 축으로 현황 정리.

> [!action] 당장 할 것
> [[HY-Embodied]]·[[HiVLA]]·[[UniT-Humanoid-Policy]] 등 로봇 AI 연구 시 이 서베이를 안전성 체크리스트로 활용. 로봇 에이전트 설계 시 물리적 비가역성 고려 방어 레이어 추가.

> [!question] 미해결 질문
> 현재 VLA 방어 메커니즘 중 실배포 수준으로 성숙한 것은? [[ASGuard]]와의 호환성?

## 도메인별 추출 (ai-news 템플릿)

- **신뢰도**: ⭐⭐⭐ — 서베이 논문, upvotes 35
- **즉시 활용**: 참조용 YES — 로봇 AI 프로젝트 안전 설계에 체크리스트로 즉시 사용 가능
- **6개월 영향력**: 로봇·자율주행·VLA 에이전트가 실세계 진출할수록 이 분야의 중요성 폭발적 증가
- **대체 관계**: [[ASGuard]](LLM jailbreak 방어), [[Reward-Hacking-Large-Models]](RL 안전) — 안전 클러스터 내 보완 관계
- **허와 실**: 서베이 논문의 특성상 새로운 방어법 제시보다 기존 연구 정리에 가까울 수 있음
- **액션**: 서베이 목차 확인 → VLA 프로젝트 안전 체크리스트 작성 → 핵심 위협 유형 docs 작성

## 관련 페이지

- [[HY-Embodied]]
- [[HiVLA]]
- [[UniT-Humanoid-Policy]]
- [[ASGuard]]
- [[Reward-Hacking-Large-Models]]
- [[slam-3dgs]]
- [[ReVSI]]

## 원본

- 출처: https://huggingface.co/papers/2604.23775
- 신뢰도: ⭐⭐⭐
