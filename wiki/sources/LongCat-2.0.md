---
title: LongCat-2.0 — Meituan 1.6T MoE, LongCat Sparse Attention, 1M 컨텍스트
type: source
domain: ai-news
tags: [ai-news, huggingface, model, moe, sparse-attention, long-context, coding-agent]
created: 2026-07-09
updated: 2026-07-09
sources: []
reliability: medium
---

# meituan-longcat/LongCat-2.0 (HF DL 1,107)

**HuggingFace**: https://huggingface.co/meituan-longcat/LongCat-2.0
**다운로드**: 1,107 (2026-07-09) · **likes**: 154 · **제작**: [[Meituan]]
**라이선스**: MIT

> [!insight] 핵심 인사이트
> [[Meituan]]의 **총 1.6T 파라미터 / 토큰당 ~48B 활성 MoE** 초대형 오픈 모델. WebFetch 실측: **LongCat Sparse Attention** + N-gram Embedding 개선, **1M 컨텍스트 학습**, 코딩·에이전트 태스크 강화, **MIT 라이선스**, 그리고 "**AI ASIC 슈퍼팟에서 전량 학습**"을 명시(엔비디아 GPU 밖 학습 인프라 신호). Transformers·vLLM·SGLang 배포 + longcat.ai 챗 제공. 주목점: ①1.6T 초대형을 **MIT로 오픈**한 대담함, ②희소 어텐션으로 1M 컨텍스트를 실용화하려는 방향([[Hierarchical-Sparse-Attention]]·[[MiniMax-Sparse-Attention]] 계보), ③**Claude Code 등 하니스 통합**을 겨냥한 에이전트/코딩 특화. [[Hy3]]·[[DeepSeek-V4-Pro]]와 함께 "오픈 초대형 MoE + 롱컨텍스트 + 에이전트"의 최상단 경쟁.

## 도메인별 추출 (ai-news / local-llm 교차)

- **신뢰도**: ⭐⭐⭐ (HF DL 1,107·likes 154·1.6T/48B·희소어텐션·1M·MIT·ASIC 학습 WebFetch 실측 / 코딩·에이전트 벤치 수치는 원문 미검증 → medium)
- **즉시 활용**: NO(개인) — 1.6T 총 파라미터는 개인·소규모 서버로 구동 불가. 실사용은 API(longcat.ai) 또는 대형 인프라 한정. 48B 활성이라 추론 자체는 상대적 경량.
- **6개월 영향력**: ①오픈 초대형 MoE의 MIT 공개가 가속(가중치 접근성↑), ②**AI ASIC 학습**이 GPU 독점 밖 대안으로 부상, ③희소 어텐션이 1M+ 컨텍스트 실용화의 표준 경로.
- **대체 관계**: 상용 프론티어(코딩) + [[DeepSeek-V4-Pro]]·[[Hy3]] 등 오픈 플래그십과 경쟁. Claude Code 하니스 통합으로 백본 대체 노림.
- **허와 실**: 1.6T·1M·"하니스 통합"은 인상적이나 실사용 접근성은 API/대형 인프라에 갇힘. 코딩·에이전트 우위는 원문 벤치 재현 필요. ASIC 학습 주장은 검증 어려움(모델카드 진술).
- **액션**: longcat.ai에서 코딩 태스크 1건을 무료 시도해 체감 품질만 확인, 로컬 구동은 비현실적이므로 API 비용·컨텍스트 활용도로 평가.

## 관련 페이지
- [[Meituan]] — 제작사
- [[Hy3]] · [[DeepSeek-V4-Pro]] · [[Agents-A1]] — 오픈 MoE·롱컨텍스트·에이전트 경쟁
- [[Hierarchical-Sparse-Attention]] · [[Morphing-Hybrid-Attention]] — 희소/하이브리드 어텐션 계보
- [[에이전트-메모리-레이어]] — 1M 컨텍스트 활용 접점
- [[ai-news]]

## 원본
- 출처: https://huggingface.co/meituan-longcat/LongCat-2.0
- HF DL: 1,107 (2026-07-09), likes 154, MIT
- 아키텍처: 1.6T 총 / ~48B 활성 MoE / LongCat Sparse Attention + N-gram Embedding / 1M 컨텍스트 / AI ASIC 슈퍼팟 학습
- 신뢰도: ⭐⭐⭐ (아키텍처·라이선스 실측 / 코딩·에이전트 벤치 미검증)
