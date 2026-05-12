---
title: WindowsWorld — 실무 다중앱 GUI 에이전트 벤치마크
type: source
domain: ai-news
tags: [ai-news, gui-agent, benchmark, windows, cross-application, evaluation]
created: 2026-05-07
updated: 2026-05-07
sources: []
reliability: medium
---

# WindowsWorld: Cross-Application GUI Agent Benchmark

> [!insight] 핵심 인사이트
> 실무 다중 앱 GUI 에이전트 벤치마크. **최고 성능 모델도 멀티앱 태스크 성공률 21% 미만** — GUI 에이전트가 단일 앱에서는 그럭저럭 작동하지만 실무처럼 여러 앱을 오가는 태스크에서 여전히 매우 취약함을 명확히 드러냄.

**HuggingFace**: https://huggingface.co/papers/2604.27776  
**업보트**: 9 (2026-05-06 기준)  
**신뢰도**: ⭐⭐⭐

## 도메인별 추출

- **신뢰도**: 업보트 9, 벤치마크 논문 — 방법론 검증 필요. Windows 실환경 기반이므로 재현 어려움
- **즉시 활용**: 직접 활용보다 "GUI 에이전트 능력 현실 파악"에 쓸 것. 21% 성공률 = 현재 GUI 에이전트 신뢰 수준 상한선
- **6개월 영향력**: 멀티앱 GUI 에이전트 연구 가속 기대. [[ClawBench]], [[WindowsWorld]], [[Claw-Eval-Live]] 등 GUI 에이전트 평가 인프라 경쟁
- **허와 실**: Windows 전용 벤치마크 — Linux/Mac 환경과 전이 가능성 미확인
- **에이전트 설계 시사점**: 실무 GUI 자동화 에이전트 구축 시 멀티앱 전환 처리가 가장 어려운 부분

> [!note] 배경 정보
> Cross-Application 태스크 예시: Word에서 내용 복사 → Excel에 붙여넣기 → 이메일 발송 등 여러 앱을 순차적으로 조작하는 작업.

## 관련 페이지
- [[ClawBench]]
- [[Claw-Eval-Live]]
- [[VLAA-GUI]]
- [[Step-level-Optimization]]

## 원본
- 출처: https://huggingface.co/papers/2604.27776
- 신뢰도: ⭐⭐⭐ (업보트 9)
