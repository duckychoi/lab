---
title: LPM 1.0 — 영상 기반 캐릭터 퍼포먼스 모델
type: source
domain: video-saas
tags: [video-saas, character-animation, performance-capture, diffusion, video-generation, motion]
created: 2026-04-12
updated: 2026-04-12
sources: []
reliability: medium
---

# LPM 1.0: Video-based Character Performance Model

> [!insight] 핵심 인사이트
> 영상에서 캐릭터 퍼포먼스를 캡처·재연하는 대규모 모델 연구. HF 업보트 194. 25명 이상 대규모 저자 — 학계·산업계 공동 대형 프로젝트. [[Higgsfield]]의 캐릭터 애니메이션 기능과 직접 경쟁/보완 관계.

## 핵심 인사이트

> [!note] 배경 정보
> arXiv 2604.07823. "Character Performance Model"은 배우의 동작·표정·발화를 종합 캡처하는 모델을 의미. 실사 영상 입력 → 디지털 캐릭터 구동 파이프라인. 게임·영화 VFX·버추얼 인플루언서 제작에 직결.

> [!warning] 주의 / 신뢰도 낮음
> 논문 단계. 오픈소스 코드·모델 공개 여부 불분명. HF 업보트 194는 중간 수준 — 검증 후 평가 필요.

> [!question] 미해결 질문
> 오픈소스 가중치 공개 예정인가? [[Higgsfield]] @캐릭터 시스템과 어떻게 다른가? 실시간 동작 가능한가?

## 도메인별 추출 (video-saas 템플릿)

- **기능 벤치마킹**: 캐릭터 퍼포먼스 캡처→재연. Higgsfield의 캐릭터 일관성 유지와 다른 접근 — 동작 전송 특화
- **크리에이터 인사이트**: 버추얼 유튜버·SNS 캐릭터 제작 자동화 수요와 직결
- **프롬프트 패턴**: 입력 영상 + 타겟 캐릭터 → 퍼포먼스 전송 (추정)
- **워크플로우**: 퍼포먼스 캡처 → 디지털 캐릭터 구동 end-to-end
- **디자인 레퍼런스**: 상세 UI 미공개
- **경쟁 우위 빈틈**: 소형 크리에이터 접근 가능한 오픈소스 퍼포먼스 캡처 부재

## 관련 페이지

- [[Higgsfield]] — 캐릭터 시스템 경쟁/보완
- [[Higgsfield-벤치마킹]] — 실제 UI 분석
- [[AI-영상-생성-2026]] — 전체 영상 AI 지형도
- [[Seedance]] — VFX 특화 영상 AI

## 원본

- 출처: https://huggingface.co/papers/2604.07823
- HF 업보트: 194 (2026-04-12 기준)
- 신뢰도: ⭐⭐⭐
