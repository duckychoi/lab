---
title: Agents-A1 — 35B MoE 에이전트 모델(262K 컨텍스트)
type: source
domain: ai-news
tags: [ai-news, huggingface, agent, moe, open-model, long-context]
created: 2026-07-08
updated: 2026-07-08
sources: []
reliability: medium
---

# InternScience/Agents-A1 (HF DL 14.7k)

**HuggingFace**: https://huggingface.co/InternScience/Agents-A1
**다운로드**: 14.7k (2026-07-08) · **제작**: [[InternScience]]
**아키텍처**: 35B MoE · 컨텍스트 262K

> [!warning] 벤치 수치 미검증
> IFEval 94.82 · GAIA 96.04 · Seal-0 56.36 등은 자동수집(모델카드 추정) 수치로 원문 벤치 재현 미확인. DL 수치와 아키텍처 개요만 채택.

> [!insight] 핵심 인사이트
> **에이전트 태스크에 특화된 35B MoE 오픈 모델**(262K 롱컨텍스트). 자동수집 요약은 IFEval 94.82·GAIA 96.04·Seal-0 56.36으로 **GPT-5.5·[[DeepSeek-V4-Pro]]와 경쟁**한다고 주장. 주목점은 절대 성능보다 "**에이전트 실행에 맞춰 튜닝된 오픈 MoE**"라는 포지셔닝 — [[Ornith-1.0-35B]]·[[Qwen3.6-35B-A3B]] 같은 35B급 오픈 에이전트 모델 경쟁이 심화됨을 보여준다. GAIA(에이전트 벤치) 상위 주장은 "리더보드 점수 ≠ 실제 에이전트 신뢰성"([[Beyond-Static-Leaderboards]] 원칙)으로 걸러 봐야 함.

## 도메인별 추출 (ai-news / local-llm 교차)

- **신뢰도**: ⭐⭐⭐ (HF DL 14.7k / 벤치 수치 원문 미검증 → medium)
- **즉시 활용**: 후보 — 35B MoE + 262K 컨텍스트면 로컬/서버에서 에이전트 백본으로 시험 가치. 단 MoE 활성 파라미터·GGUF 양자화 유무·VRAM 요건 확인 필요.
- **6개월 영향력**: 오픈 에이전트 모델이 "지시이행(IFEval)·도구사용(GAIA)"에 특화되며 굳어짐. 프론티어 API 대비 실행가능 경량이 실수요라는 7월 흐름 연장.
- **대체 관계**: 상용 에이전트 API를 오픈 로컬로 대체 시도. [[Ornith-1.0-35B]]·[[Qwen3.6-35B-A3B]]와 직접 경쟁.
- **허와 실**: GAIA 96.04는 매우 높은 수치 — 평가 셋업·오염 여부 검증 없이는 과신 금물.
- **액션**: GGUF 양자화판 나오면 로컬에서 에이전트 태스크 1건 실측, Ornith-35B와 도구사용 신뢰성 비교.

## 관련 페이지
- [[InternScience]] — 제작 기관
- [[Ornith-1.0-35B]] · [[Qwen3.6-35B-A3B]] — 35B급 오픈 에이전트 경쟁 모델
- [[DeepSeek-V4-Pro]] — 비교 대상 플래그십
- [[Beyond-Static-Leaderboards]] — 벤치 신뢰성 원칙
- [[ai-news]]

## 원본
- 출처: https://huggingface.co/InternScience/Agents-A1
- HF 다운로드: 14.7k (2026-07-08) / 35B MoE · 262K 컨텍스트
- 신뢰도: ⭐⭐⭐ (DL 실측 / 벤치 원문 미검증)
