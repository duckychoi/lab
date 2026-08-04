---
title: AREX — 재귀적 자기개선 딥리서치 에이전트
type: source
domain: ai-news
tags: [ai-news, hf-paper, deep-research, agent, self-improvement, moe, verification]
created: 2026-07-25
updated: 2026-07-25
sources: []
reliability: medium
---

# AREX (Towards a Recursively Self-Improving Agent for Deep Research)

> [!insight] 핵심 인사이트
> HF Daily ↑122. 딥리서치의 근본 비대칭 — **"모든 제약을 동시에 만족하는 답을 찾기는 비싸지만, 후보 답을 제약별로 쪼개 검증하기는 훨씬 싸다"** — 를 아키텍처로 만든 프레임워크. **내부 루프**(증거수집→잠정답변→상태유지)와 **외부 루프**(제약별 감사→미해결 클레임 식별→표적 추가조사)를 교대 실행하고, 상호작용 이력을 **외부 모델 없이 스스로 압축**(검증된 증거·미해결 제약만 보존)한다. 이 위키의 무인 자동수집 파이프가 정확히 "수집→잠정정리→검증→재조사" 루프라, AREX의 discovery-verification 분리는 **직접 참고할 설계 원리**.

> [!note] 배경 정보
> 두 구현체: **AREX-Turbo**(Dense 4B, Qwen3.5-4B 백본)·**AREX-Base**(122B 총/10B 활성 MoE). "작은 검증기를 여러 번 돌려 큰 탐색을 대체"하는 [[SearchOS-V1]]·[[에이전트-메모리-레이어]] 계열과 문제의식 공유 — 특히 "컨텍스트를 압축된 improvement state로 유지"는 장기세션 메모리 하네스([[jcode]] 시맨틱 메모리)와 맞닿는다.

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐⭐ — HF 초록 WebFetch 실확인(discovery-verification 비대칭·이중 루프·자기압축 구조 구체 확인). 단 미래형 ID(2607.21461)·원문 미검증·자체 벤치라 medium.
- **즉시 활용**: MAYBE — 구현체(4B/122B) 공개 여부 미확인이나, **"제약별 검증기로 답을 감사"하는 외부 루프 패턴**은 지금 위키 인제스트에 개념 이식 가능(수집 후 "이 주장 검증됐나?"를 제약 체크리스트로 자동화).
- **6개월 영향력**: 딥리서치 에이전트가 "한 번에 완벽한 답" 대신 **"싸게 검증하며 재귀 개선"**으로 수렴하면, 무인 리서치의 정확도·비용 곡선이 개선. BrowseComp·GAIA·HLE(w/Tools) 우위 주장.
- **대체 관계**: [[SearchOS-V1]](다중에이전트 팬아웃)·[[deer-flow]]류 딥리서치 하네스에 **자기감사 외부 루프**를 더하는 보강 방향.
- **허와 실**: "동급 대비 우위·더 큰 활성 파라미터 모델과도 경쟁력"은 자체 리포트. 122B-A10B 실제 공개·재현 전까지 벤치는 잠정.
- **액션**: 원문/구현 공개 시 외부 루프(제약별 검증)를 위키 인제스트 검증 단계에 프로토타입 이식 검토 → actionable 등록.

## 관련 페이지
- [[SearchOS-V1]]
- [[에이전트-메모리-레이어]]
- [[jcode]]
- [[DataFlow-Harness]]
- [[ai-news]]

## 원본
- 출처: https://huggingface.co/papers/2607.21461
- HF Daily Papers: ↑122
- 구현체: AREX-Turbo(Dense 4B, Qwen3.5-4B) / AREX-Base(122B 총·10B 활성 MoE)
- 벤치(자체): BrowseComp · WideSearch · DeepSearchQA · HLE(w/Tools) · GAIA · xbench-DeepSearch 우위 주장
- 신뢰도: ⭐⭐ (초록 WebFetch 실확인, 미래형 ID·원문·재현 미검증 medium)
