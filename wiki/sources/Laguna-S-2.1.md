---
title: Laguna-S-2.1 — poolside의 에이전틱 코딩용 118B MoE(활성 8B)
type: source
domain: ai-news
tags: [ai-news, hf-model, coding-agent, moe, long-context, swe-bench, local-llm]
created: 2026-07-22
updated: 2026-07-29
sources: []
reliability: medium
---

# Laguna-S-2.1 (poolside/Laguna-S-2.1)

> [!insight] 핵심 인사이트
> HF 다운로드 **67,286(월간, 3,056→67,286 약 22배 급증)·좋아요 805(266→805)** — 2026-07-29 갱신. 초기 신생에서 실사용 채택이 크게 붙은 상태. 갱신 벤치에 **SWE Atlas 46.2%·Toolathlon Verified 49.7%** 추가 확인. [[poolside]]의 **에이전틱 코딩 특화** 오픈웨이트 모델 — **118B 총 파라미터·활성 ~8B MoE**(256 라우팅 top-10 + 1 공유 전문가, 48층 글로벌+슬라이딩윈도 어텐션), **1M 토큰 컨텍스트**, 네이티브 추론(도구 호출 사이 interleaved thinking·요청별 제어). 벤치는 **SWE-bench Multilingual 78.5%·Terminal-Bench 2.1 70.2%·SWE-Bench Pro(공개) 59.4%·Deep SWE 40.4%**. FP8·NVFP4·INT4·GGUF 양자화 변종 제공, OpenMDW-1.1 오픈 라이선스(상용 허용). "활성 8B로 대형급 코딩 벤치"를 노린 **MoE 효율 코더** — [[Inkling]](975B MoE·SWE 77.6%)·[[Agents-A1]] 계보에서 **1M 컨텍스트 + 코딩 SOTA 지향** 항을 채운다.

> [!warning] 신뢰도 medium — 벤치 자체 리포트·다운로드 초기
> 118B/8B·1M·78.5% 등은 **모델카드 WebFetch로 확인**했으나 전부 **배포자 자체 벤치**로 독립 재현 전. 월 3,056 다운로드는 신생 초기 수준이라 실사용 검증 부족. SWE-bench Multilingual 78.5%는 [[Inkling]]류 프론티어 클레임과 유사하므로 액면가 신뢰 금지 — 실측 필요.

## 도메인별 추출 (ai-news / local-llm 교차)

- **신뢰도**: ⭐⭐ — 모델카드 WebFetch 실확인(스펙·벤치 구체 수치 확보), 단 자체 벤치·다운로드 초기. reliability medium.
- **즉시 활용**: 조건부 — 활성 ~8B라 로컬 추론 부담은 27B급 수준이나 **총 118B 가중치 로딩**이 관건. GGUF/INT4로 소비자 하드웨어 구동 여부가 실용성 분수령. 1M 컨텍스트는 대형 레포 코딩에 매력.
- **6개월 영향력**: "에이전틱 코딩 전용 오픈 MoE"가 [[Qwen3.6-27B]]·[[Inkling]] 사이에서 **1M 컨텍스트 + interleaved thinking**으로 차별화하면, 로컬 코딩 에이전트 백본 선택지 확대.
- **대체 관계**: [[Qwen3.6-27B]]·[[Agents-A1]]·[[Inkling]]의 코딩 백본 대안. [[OmniRoute]]류 게이트웨이에 붙여 비용 최적 라우팅 후보.
- **허와 실**: 78.5% SWE-ML은 대형 상용 근접 클레임 — 자체 벤치이므로 실제 에이전트 루프에서의 도구 사용·디버깅 실력은 별개.
- **액션**: GGUF 변종을 받아 실제 SWE 태스크(버그 수정 1~2건)로 [[Qwen3.6-27B]]·상용 대비 코딩 실력·1M 컨텍스트 활용도 스팟체크.

## 관련 페이지
- [[poolside]]
- [[Inkling]]
- [[Agents-A1]]
- [[Qwen3.6-27B]]
- [[OmniRoute]]
- [[local-llm]]
- [[ai-news]]

## 원본
- 출처: https://huggingface.co/poolside/Laguna-S-2.1
- HuggingFace: 다운로드 67,286(월간, 3,056→67,286)·좋아요 805(266→805) — 2026-07-29 WebFetch 실측 갱신
- 스펙: 118B 총/활성 ~8B MoE(256 top-10 + 1 공유, 48층), 1M 컨텍스트, 네이티브 interleaved 추론, FP8/NVFP4/INT4/GGUF, OpenMDW-1.1
- 벤치(자체): SWE-bench Multilingual 78.5% · Terminal-Bench 2.1 70.2% · SWE-Bench Pro(공개) 59.4% · Deep SWE 40.4% · SWE Atlas 46.2% · Toolathlon Verified 49.7%
- 신뢰도: ⭐⭐ (모델카드 검증, 벤치 자체 리포트·독립 재현 전)
