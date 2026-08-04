---
title: Hy3 (Hunyuan Hy3) — Tencent 295B/21B MoE 에이전트·롱컨텍스트
type: source
domain: ai-news
tags: [ai-news, huggingface, model, moe, long-context, agent, tencent]
created: 2026-07-09
updated: 2026-07-13
sources: []
reliability: medium
---

# tencent/Hy3 (HF DL 9,163)

**HuggingFace**: https://huggingface.co/tencent/Hy3
**다운로드**: 9,163 (2026-07-13) ← 5,572 (07-09) · **likes**: 579 · **제작**: [[Tencent]] (Hy Team)
**라이선스**: Apache 2.0 · **정밀도**: BF16

> [!insight] 핵심 인사이트
> [[Tencent]] Hunyuan 계열의 **295B 총 / 21B 활성 MoE(192 전문가 중 top-8), 256K 컨텍스트** 오픈 모델. WebFetch 실측으로 raw 요약(활성 21B·192e top-8·256K)이 정확히 확인되고 **총 파라미터 295B·Apache 2.0·BF16**이 추가 확정. 추론·에이전트·롱컨텍스트 강화가 목표이며, FP8 양자화판(Hy3-FP8) + vLLM/SGLang(스펙 디코딩 포함) 배포. raw의 "SWE-Bench Verified에서 스캐폴딩(Cline·KiloCode 등) 간 정확도 편차 4% 이내" 주장이 사실이면 **하니스에 덜 민감한 에이전트 모델** — [[Beyond-Static-Leaderboards]]가 지적한 "스캐폴딩에 따라 점수 요동" 문제를 정면으로 완화한다는 셀링포인트. [[Agents-A1]]·[[DeepSeek-V4-Pro]]와 오픈 에이전트/롱컨텍스트 경쟁의 새 참전.

## 도메인별 추출 (ai-news / local-llm 교차)

- **신뢰도**: ⭐⭐⭐ (HF DL 5,572·likes 579·아키텍처(295B/21B·192e·256K)·Apache 2.0 WebFetch 실측 / SWE-Bench 편차 4% 등 벤치 주장은 원문 미검증 → medium)
- **즉시 활용**: 후보(서버) — 21B 활성이라 추론 비용은 중형이나 295B 총 파라미터로 VRAM/디스크 부담 큼. FP8·vLLM/SGLang 지원은 실배포 친화적.
- **6개월 영향력**: 오픈 MoE가 "스캐폴딩 견고성(하니스 편차 최소화)"을 셀링포인트로 내세우는 흐름. 에이전트 백본 선택 기준이 raw 점수 → 하니스 안정성으로 확장.
- **대체 관계**: 상용 에이전트 API + [[DeepSeek-V4-Pro]]·[[Agents-A1]] 등 오픈 플래그십과 경쟁.
- **허와 실**: "스캐폴딩 간 4% 이내"는 매력적이나 원문 벤치 재현 없이는 과신 금물. 295B 총 파라미터는 로컬 개인 환경엔 사실상 서버급.
- **액션**: FP8판 확보 가능 시 vLLM으로 에이전트 도구사용 1건 실측, 서로 다른 하니스(예: 2종)에서 정확도 편차를 직접 측정해 "4% 이내" 주장 검증.

## 관련 페이지
- [[Tencent]] — 제작사 (같은 날 TencentDB-Agent-Memory도 배출)
- [[Agents-A1]] · [[DeepSeek-V4-Pro]] · [[LongCat-2.0]] — 오픈 MoE·롱컨텍스트 경쟁
- [[Beyond-Static-Leaderboards]] — 스캐폴딩 편차 문제 원칙
- [[에이전트-메모리-레이어]] — 256K 롱컨텍스트 활용 접점
- [[ai-news]]

## 원본
- 출처: https://huggingface.co/tencent/Hy3
- HF DL: 9,163 (2026-07-13) ← 5,572 (2026-07-09), likes 579, Apache 2.0, BF16
- 아키텍처: 295B 총 / 21B 활성 MoE(192e top-8) / 256K 컨텍스트 / FP8판·vLLM·SGLang
- 신뢰도: ⭐⭐⭐ (DL·아키텍처·라이선스 실측 / SWE-Bench 편차 주장 미검증)
