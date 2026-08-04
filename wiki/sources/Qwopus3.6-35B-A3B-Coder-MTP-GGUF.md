---
title: Qwopus3.6-35B-A3B-Coder-MTP-GGUF — 실행효율 지향 코딩 특화 로컬 MoE
type: source
domain: ai-news
tags: [ai-news, local-llm, qwen, coding, moe, mtp, gguf, agentic]
created: 2026-07-11
updated: 2026-07-11
sources: []
reliability: high
---

# Jackrong/Qwopus3.6-35B-A3B-Coder-MTP-GGUF

> [!insight] 핵심 인사이트
> [[Qwen3.6-35B-A3B]] 기반 **코딩·도구사용 특화 병합 + MTP GGUF**. DL **317,984**. 철학이 명확 — "**더 긴 가시적 추론이 아니라 실행 효율**": 반복 도구 결정·코드 패칭·디버깅 루프를 **thinking-off**로 빠르게. 300케이스 SWE-bench에서 thinking-off·Q5_K_M로 **62.4%**. legit-request 준수(100 vs 70)·멀티턴 오케스트레이션(80 vs 70)에서 thinking-on 대안보다 높음. 35B/~3B 활성 MoE, Q3_K_M 17.2GB~Q8_0 37.8GB.

**HF Model**: https://huggingface.co/Jackrong/Qwopus3.6-35B-A3B-Coder-MTP-GGUF  
**다운로드**: 317,984  
**신뢰도**: ⭐⭐⭐⭐ (모델카드 실측·DL 31.8만·Apache 2.0)

## 도메인별 추출

- **신뢰도**: ⭐⭐⭐⭐ — 모델카드 아키텍처·벤치·DL WebFetch 실측. SWE-bench 62.4%는 자가 300케이스 평가(공식 Verified 아님)
- **즉시 활용**: YES — **로컬 코딩 에이전트 백엔드 직행**. thinking-off로 도구 루프가 빨라 [[Claude-Code-워크플로우]] 스타일 반복 작업에 적합. 소비자 GPU(3B 활성)로 SWE-bench 60%+
- **6개월 영향력**: "**추론을 늘리지 말고 실행을 최적화**"는 [[ThinkingCap-Qwen3.6-27B-GGUF]](추론 토큰 -50%)와 같은 방향 — **롱호라이즌 도구 루프엔 짧고 정확한 실행**이 답이라는 흐름. [[UniClawBench]]가 지적한 프런티어의 롱호라이즌 약점을 로컬에서 겨냥
- **대체 관계**: 범용 [[Qwen3.6-35B-A3B-MTP-GGUF]] 대비 **코딩·에이전트 실행 특화**. thinking-on 모델 대비 멀티턴 준수·오케스트레이션 우위(자가 벤치)
- **Hermes/에이전트 적용**: 로컬 코드 패칭·디버깅 에이전트에 바로. MTP로 응답 지연↓
- **액션**: Q5_K_M로 로컬에 올려 코드 패칭 태스크에서 thinking-off 실행 정확도·속도 검증

> [!action] 당장 할 것
> Qwopus3.6 Q5_K_M를 로컬 코딩 에이전트 백엔드로 올려, thinking-off 모드의 코드 패칭·멀티턴 도구 루프 정확도를 [[Qwen3.6-35B-A3B-MTP-GGUF]] 범용판과 대조한다.

## 관련 페이지
- [[Qwen3.6-35B-A3B]]
- [[Qwen3.6-35B-A3B-MTP-GGUF]]
- [[ThinkingCap-Qwen3.6-27B-GGUF]]
- [[Claude-Code-워크플로우]]
- [[UniClawBench]]

## 원본
- 출처: https://huggingface.co/Jackrong/Qwopus3.6-35B-A3B-Coder-MTP-GGUF
- 신뢰도: ⭐⭐⭐⭐ (모델카드 실측·DL 31.8만)
