---
title: Crafter — 다중 에이전트 과학 논문 그림 자동 생성 시스템
type: source
domain: ai-news
tags: [ai-news, hf-paper, multi-agent, scientific-figure, harness, svg, automation]
created: 2026-06-02
updated: 2026-06-02
sources: []
reliability: medium
---

# Crafter: Multi-Agent Scientific Figure Generation

**arxiv**: https://arxiv.org/abs/2605.30611  
**HuggingFace**: https://huggingface.co/papers/2605.30611  
**신뢰도**: ⭐⭐⭐ (논문, 벤치마크 실증 존재)

## 핵심 인사이트

> [!insight] 핵심 인사이트
> 과학 논문 그림(figure) 생성을 다중 에이전트 하네스로 자동화. 핵심 혁신: "자유 텍스트 누적" 대신 **구조화된 타입화 편집(typed edits)** 사용 → 모순 없는 반복 수정 가능. 기존 최강 대비 PaperBanana-Bench +16.61점, CraftBench +22.20점.

> [!action] 당장 할 것
> Crafter 아키텍처의 harness 패턴(플래너→실행자→비평자→수정자 루프)을 다른 구조화 출력 생성 태스크에 적용 검토. 특히 영상 대본 → 슬라이드 자동화에 활용 가능.

## 도메인별 추출 (ai-news)

**신뢰도**: 논문 + 벤치마크 실증 존재 (CraftBench 279개 샘플)  
**즉시 활용**: NO — 코드 공개 여부 미확인, 비용 높음 ($0.25/도형)  
**6개월 영향력**: 다중 에이전트 구조화 생성 패러다임 확산 가속  
**대체 관계**: PaperBanana(기존 최강) 대비 22점 향상

**5개 협력 에이전트:**
1. **Intent Reasoner**: 입력 → 초기 명세 생성
2. **Plan Generator**: K개 후보 시각 계획 제안
3. **Image-Gen Backend**: 래스터 렌더링 (Nano Banana 2)
4. **Critic**: 6개 축 진단 (내용 정확도, 레이아웃, 가독성, 미학 등)
5. **Convergence Judge**: 수용/계속/복귀 결정

**핵심 메커니즘:**
- 다양성 주도 계획 탐색 (K개 후보): +8.56점
- 구조화된 수정 계층 (typed edits): +8.90점 (가장 큰 기여)
- 검증-수정 루프: +5.48점

**CraftEditor** (래스터→SVG 변환): 8.04/10 vs 경쟁사 6.91/10

**비용:**
- $0.25/도형 (vs PaperBanana $0.11)
- CraftEditor: $0.85/변환

> [!note] 배경 정보
> "Typed edits" 개념이 핵심 — 자유 텍스트로 수정 지시가 쌓이면 "제목 확대" + "공백 감소"가 충돌. 구조화된 편집 명세로 이 문제 해결. 이 패턴은 영상 편집, UI 자동화 등 타 도메인에도 적용 가능.

## 관련 페이지
- [[AI-에이전트-프레임워크]]
- [[After-Effects-MCP]]

## 원본
- 출처: https://huggingface.co/papers/2605.30611
- 신뢰도: ⭐⭐⭐ (논문, 벤치마크 실증)
