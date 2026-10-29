---
title: "TAO — GPU 추론과 CPU 도구 호출이 번갈아 도는 에이전트 서빙 스케줄러. 도구 복귀 임박도·감쇠형 KV 캐시 이득·토큰 점유를 하나의 가치함수로 묶고 DP 로 승인·배치를 함께 결정. 지연 최대 −26.8% · TTFT 최대 −36.3% · 코드 미공개"
type: source
domain: local-llm
tags: [local-llm, ai-news, hf-paper, agentic-serving, scheduling, kv-cache, inference-serving, tool-use]
created: 2026-10-29
updated: 2026-10-29
sources: [https://huggingface.co/papers/2610.37230]
reliability: low
---

# TAO: Tool-Aware Joint Scheduling for LLM-Based Agentic Serving

**HF**: https://huggingface.co/papers/2610.37230 · published **2026-10-27** · Shuhuai Li · Shengdong Ye · Dongdong Ge · **Yinyu Ye** · Jianghao Lin(저자 5) · upvote **3**(수집기 2 · +1 드리프트)
**코드**: 없음(HF `githubRepo` null · 수집기 일치)
**신뢰도**: ⭐ low(코드 없음 · 관심도 최저 · 수치는 "최대" 값)

> [!insight] 핵심 인사이트 — 에이전트 서빙의 낭비는 "도구가 아직 안 돌아온 세션"에 GPU 자리를 주는 데서 생긴다
> 기존 서빙은 ① 서비스 평가에서 **도구 반환 준비 여부**를 무시하고 ② GPU 승인·배치를 휴리스틱으로 정한다. TAO 는 **가까운 시일 내 도구 복귀 가능성 + 노드별 KV 캐시 이득(시간 감쇠) + 토큰 점유량**을 하나의 가치 인터페이스로 합치고, 용량 제약 하에서 동적계획법으로 대기 세션을 **함께** 고르고 배치한다.
> 🎯 [[local-llm]] 관점: 로컬에서 에이전트 여러 개를 한 GPU 에 돌릴 때(예: [[thinkrail]] 류 병렬 에이전트) 같은 문제가 소규모로 생긴다 — 도구 실행 중인 세션의 KV 를 붙잡아 둘지 내보낼지. "KV 캐시 이득은 시간에 따라 감쇠한다"는 모델링은 단일 노드에서도 쓸 수 있는 직관이다.

> [!warning] 주의
> - 📐 **"최선 기준선"은 지표마다 다르다**: 초록 *"relative to the best evaluated state-of-the-art baseline **for each metric**"* — 지연·TTFT·처리량 각각 가장 강한 기준선과 비교했다. 즉 세 수치가 **같은 기준선 대비가 아니다.** 수집기는 "최선 기준선 대비"로 적어 이 조건을 축약했다 → [[한정어-탈락]].
> - "최대(up to)" × 12개 설정 — 12개 중 가장 좋은 셀 값. 평균·중앙값 없음 → [[배수-조건분산]].
> - 코드 미공개 · upvote 3 ⇒ 독립 재현 경로 없음(수집기가 "관심도 낮음"을 명시 ✅).
> - 🆕 저자에 **Yinyu Ye**(최적화·운영연구 분야 저명 연구자 — 볼트 일반 지식, 동명이인 여부 미확인)가 있다. DP 기반 공동 결정이라는 OR 색채와 일치.

## 도메인별 추출 (local-llm)
- **실용성 판단**: 클러스터 서빙(GPU 다수 + 분산 CPU 도구) 전제 — 개인 로컬 환경에 직접 이식 대상은 아님.
- **메모리 아키텍처**: KV 캐시 — 노드 친화도(cache credit) + 시간 감쇠.
- **Hermes 적용**: 당장 NO. ChinameBot 이 도구 호출 대기 중 KV 를 유지할지 판단하는 휴리스틱의 설계 참고로만.
- **트레이드오프**: 지연 −26.8% / TTFT −36.3% / 처리량 +29.5% (전부 "최대" · 지표별 다른 기준선).
- **오픈소스 구현체**: 없음.

## 관련 페이지
- [[local-llm]] · [[한정어-탈락]] · [[배수-조건분산]] · [[하네스-설계-축]]
- KV 캐시 관련: [[AttentionSink]] · [[DeepSeek-V4.1-Flash]]
- 같은 배치(10-29): [[DTCA]] · [[Falcon-AVTSE]] · [[Sensorimotor-Alignment]] · [[OmniShowcase]] · [[thinkrail]]
- [[ai-news]]

## 원본
- https://huggingface.co/papers/2610.37230 (초록)
- 볼트 실측(2026-10-29T09:06Z, HF `api/papers`): upvote 3 · 저자 5 · githubRepo null — 수집기 일치 · 🔴 "지표별 기준선" 조건 축약
- 신뢰도: ⭐
