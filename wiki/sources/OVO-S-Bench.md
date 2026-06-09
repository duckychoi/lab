---
title: OVO-S-Bench — 에고센트릭 스트리밍 공간 지능 벤치마크 (InternLM)
type: source
domain: ai-news
tags: [ai-news, hf-paper, spatial-intelligence, benchmark, egocentric, streaming, VLM, embodied-AI]
created: 2026-06-04
updated: 2026-06-04
sources: []
reliability: high
---

# OVO-S-Bench — 연속 에고센트릭 영상 스트림 기반 공간 추론 벤치마크

**논문**: https://huggingface.co/papers/2606.03890  
**저자**: InternLM

## 핵심 인사이트

> [!insight] 핵심 인사이트
> 에고센트릭 연속 영상 스트림 기반 공간 추론 벤치마크(1,680문항). **Gemini-Pro 59.2 vs 인간 86.6** — AI와 인간의 공간 지능 격차가 여전히 크다는 실증. **allocentric mapping**(자신 위치 기준이 아닌 외부 지도 기준 표현)이 최대 병목.

## 도메인별 추출 (ai-news 템플릿)

- **신뢰도**: ⭐⭐⭐⭐ — InternLM, arXiv, HF Papers
- **즉시 활용**: YES (벤치마크로) — VLM의 공간 추론 능력 평가 기준으로 활용
- **6개월 영향력**: 로봇·AR/VR·자율주행에서 공간 지능이 핵심인데, 현재 SOTA가 인간의 68% 수준(59.2/86.6)임을 명확히 함. allocentric mapping 개선이 차세대 VLM의 주요 과제
- **대체 관계**: 기존 정적 이미지 기반 공간 벤치마크 vs DRIFT의 연속 스트리밍 공간 추론
- **허와 실**: "에고센트릭 스트리밍"이 실제 로봇/AR 배포와 얼마나 가까운 시나리오인가?

## 기술 요약

- **1,680문항** 에고센트릭 연속 영상 질문
- **공간 추론 유형**:
  - Egocentric: 자신 기준 방향/거리 추론
  - Allocentric: 외부 지도 기준 위치 표현 ← **최대 병목**
  - Dynamic: 움직이는 물체 추적
- **현재 격차**: Gemini-Pro 59.2 / 인간 86.6

## 관련 페이지

- [[Humanoid-GPT]] — 휴머노이드 로봇 (공간 지능 필요)
- [[LocateAnything-3B]] — 이미지 내 객체 위치 탐색
- [[WildDet3D]] — 3D 객체 탐지

## 원본

- 출처: https://huggingface.co/papers/2606.03890
- arXiv: 2606.03890
- 저자: InternLM
- 신뢰도: ⭐⭐⭐⭐
