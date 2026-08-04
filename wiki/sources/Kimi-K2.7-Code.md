---
title: Kimi K2.7 Code — Moonshot 1.1T 코드 특화 멀티모달 모델
type: source
domain: ai-news
tags: [ai-news, coding-model, multimodal, moe, moonshot, kimi, code-generation]
created: 2026-06-14
updated: 2026-06-18
sources: []
reliability: medium
---

# moonshotai/Kimi-K2.7-Code

> [!insight] 핵심 인사이트
> Moonshot AI의 1.1T 파라미터 코드 특화 멀티모달 모델. 다운로드 173,000 (2026-06-17). 이미지+텍스트를 받아 코드를 생성 — UI 스크린샷 → 코드, 다이어그램 → 구현 등 **비주얼 기반 코딩** 시나리오에 특화. 1.1T의 거대한 총 파라미터 수(MoE 구조)로 코드 품질 극대화 시도.

**HuggingFace**: https://huggingface.co/moonshotai/Kimi-K2.7-Code  
**다운로드**: 173,000 (2026-06-17; 이전 56,800 2026-06-15)  
**신뢰도**: ⭐⭐⭐ (Moonshot 공식, 신규 출시)

## 도메인별 추출

- **신뢰도**: Moonshot AI(Kimi 시리즈, 중국 top-tier AI 기업) 공식 — 신뢰도 중상. 다운로드 1,690은 초기 수치
- **즉시 활용**: 조건부 YES — 로컬 실행 시 1.1T MoE 구조로 하드웨어 요구사항이 높을 것. API 제공 여부 확인 필요
- **6개월 영향력**: 이미지+코드 통합 멀티모달 코딩 에이전트 시대 본격화. [[agentsview]] 같은 도구로 성능 비교 분석 가능
- **대체 관계**: Claude Sonnet(비전+코딩), GPT-4o Code Interpreter 대비 오픈 웨이트. [[Gemma-4-31B]] 대비 코드 특화
- **허와 실**: 1.1T 총 파라미터는 MoE 희소 활성화 — 실제 활성 파라미터는 훨씬 적음. 코드 벤치마크(HumanEval, SWE-Bench) 수치 아직 미확인

> [!warning] 주의 / 신뢰도 낮음
> 다운로드 1,690은 신규 출시 초기 수치. 실제 코드 생성 품질은 독립 벤치마크 결과 확인 후 판단 필요.

> [!question] 미해결 질문
> SWE-Bench/HumanEval 벤치마크 점수는? API 서비스 제공 여부? 실제 활성 파라미터 수?

## 관련 페이지
- [[Gemma-4-31B]]
- [[GLM-5.1]]
- [[AI-에이전트-프레임워크]]
- [[agentsview]]

## 원본
- 출처: https://huggingface.co/moonshotai/Kimi-K2.7-Code
- 다운로드: 173,000 (2026-06-17) ← 56,800 (2026-06-15) ← 1,690 (2026-06-14)
- 신뢰도: ⭐⭐⭐ (Moonshot 공식, 빠른 성장 확인)
