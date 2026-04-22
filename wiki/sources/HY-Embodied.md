---
title: HY-Embodied-0.5 — 실세계 로봇용 소형 임베디드 파운데이션 모델
type: source
domain: ai-news
tags: [ai-news, hf-paper, embodied-ai, robotics, foundation-model, edge-ai, physical-environment]
created: 2026-04-10
updated: 2026-04-10
sources: []
reliability: medium
---

# HY-Embodied-0.5: Embodied Foundation Models for Real-World Agents

> [!insight] 핵심 인사이트
> 물리 환경 인식·행동을 위한 소형(0.5B급) 임베디드 AI 모델. 실세계 로봇에 직접 탑재 가능 크기로 줄이면서 환경 추론 능력 유지. [[slam-3dgs]] 도메인과 직결 — 로봇이 "보고 이해하고 행동"하는 파이프라인의 핵심 컴포넌트.

## 핵심 인사이트

> [!note] 배경 정보
> arXiv: 2604.07430. "HY" = Hunyuan (Tencent). 0.5B 파라미터급 경량 모델로 에지 디바이스 배포 초점.

> [!question] 미해결 질문
> 3DGS/SLAM 파이프라인과 연동 방법? 입력 형식(RGB-D? 단안 카메라?)? 실시간 처리 가능?

## 도메인별 추출 (ai-news 템플릿)

- **신뢰도**: ⭐⭐ — Tencent 연구 그룹, arXiv 논문. 실물 테스트 미확인
- **즉시 활용**: NO — 로봇 하드웨어 없으면 직접 활용 어려움
- **6개월 영향력**: 임베디드 AI + 로봇 통합 트렌드 가속. slam-3dgs 도메인에 영향
- **대체 관계**: 기존 로봇 비전 파이프라인(SLAM + 별도 추론) 통합 대체 후보
- **액션**: slam-3dgs 도메인 탐구 시 참조 논문으로 보관

## 관련 페이지

- [[slam-3dgs]]
- [[local-llm]]

## 원본

- 출처: https://huggingface.co/papers/2604.07430
- arXiv: 2604.07430
- 신뢰도: ⭐⭐
