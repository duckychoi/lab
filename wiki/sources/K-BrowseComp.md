---
title: K-BrowseComp — 한국어 웹 브라우징 에이전트 벤치마크
type: source
domain: ai-news
tags: [ai-news, hf-paper, benchmark, korean, web-browsing, agent, evaluation]
created: 2026-06-02
updated: 2026-06-02
sources: []
reliability: high
---

# K-BrowseComp: Korean Web Browsing Agent Benchmark

**arxiv**: https://arxiv.org/abs/2606.02404  
**HuggingFace**: https://huggingface.co/papers/2606.02404  
**GitHub**: https://github.com/prometheus-eval/K-BrowseComp  
**신뢰도**: ⭐⭐⭐⭐ (논문 + 실증 벤치마크, MIT 라이선스 공개)

## 핵심 인사이트

> [!insight] 핵심 인사이트
> 한국 맥락 기반 웹 브라우징 에이전트 평가의 첫 종합 벤치마크. 핵심 발견: 한국 모델들(K-EXAONE 10.33%, HyperCLOVAX 2.33%, Kanana 0%)이 글로벌 모델(GPT-5.5 45.67%, DeepSeek-V4-Pro 30%)에 큰 격차로 뒤짐. 원인은 검색량 아닌 **궤적 수준의 상태 유지 실패**.

> [!action] 당장 할 것
> K-BrowseComp 평가셋(400개 문제, MIT) 다운로드. 한국어 웹 에이전트 개발 시 F4(반구조화 파싱), F7(제약조건 추적) 실패 모드 우선 해결.

## 도메인별 추출 (ai-news)

**신뢰도**: ⭐⭐⭐⭐ (300개 수동 검증 + 100개 합성, MIT 공개)  
**즉시 활용**: YES — 벤치마크 코드 + 데이터셋 공개  
**6개월 영향력**: 한국어 에이전트 개발 방향성 제시, 글로벌-한국 모델 격차 가시화  
**대체 관계**: BrowseComp(영어) 한국어 버전

**벤치마크 구성:**
- 400개 문제 (검증 300 + 합성 100)
- 다중 홉: 53.3% / 병렬 분기: 46.7%
- 카테고리: 엔터테인먼트(36%), 교통/지역(16%), 교육(12%) 등

**주요 성능 결과 (Verified 세트):**
- GPT-5.5: 45.67% (1위)
- DeepSeek-V4-Pro: 30.00% / GLM-5.1: 30.67%
- K-EXAONE-236B: 10.33% (한국 모델 최고)
- HyperCLOVAX-SEED-Think-32B: 2.33%
- Kanana-2-30B: 0.00%

**주요 실패 모드 9종 (F0~F8):**
- F4: 반구조화 데이터 파싱 실패 (59개 합성 실패 최다)
- F7: 제약조건 추적 실패 (21개)
- F5: 검색결과 선택 실패

> [!note] 배경 정보
> GLM-5.1(Z.AI/Zhipu)이 30.67%로 DeepSeek-V4-Pro(30.00%)와 동등 수준 달성. 한국 전용 모델들이 글로벌 모델에 비해 도구 호출 안정성, 후검색 상태 유지에서 취약.

> [!warning] 주의 / 신뢰도 낮음
> 단일 검색 백엔드(Perplexity), 10회 호출 예산 제한 — 다른 설정에서 결과 다를 수 있음. Entertainment & Media 36% 집중 — 도메인 편향 존재.

## 관련 페이지
- [[AI-에이전트-프레임워크]]
- [[Zhipu AI]]
- [[DeepSeek-V4-Pro]]
- [[TASTE-agent-benchmark]]

## 원본
- 출처: https://huggingface.co/papers/2606.02404
- 신뢰도: ⭐⭐⭐⭐ (실증 벤치마크, MIT 공개)
