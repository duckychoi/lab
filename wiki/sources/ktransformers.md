---
title: ktransformers — CPU+GPU 이기종 초대형 LLM 추론·파인튜닝 프레임워크
type: source
domain: ai-news
tags: [ai-news, github-trending, local-llm, inference-optimization, moe, heterogeneous, quantization]
created: 2026-07-20
updated: 2026-07-20
sources: []
reliability: high
---

# ktransformers (kvcache-ai/ktransformers)

> [!insight] 핵심 인사이트
> ⭐**18,544 (2026-07-20, 당일 +360)**. 칭화대 MADSys Lab + 커뮤니티가 만든 **CPU+GPU 이기종(heterogeneous) 추론·파인튜닝 프레임워크**. 핵심은 "GPU VRAM에 다 못 올리는 초대형 MoE를 CPU 커널로 오프로딩해 소비자 하드웨어에서 돌린다" — Intel AMX/AVX INT4/INT8 최적화 커널 + NUMA-aware 메모리 관리로 DeepSeek-V3/R1·Qwen3·GLM-5·Kimi-K2.5 같은 프런티어 MoE를 4×RTX4090급에서 구동/SFT(LLaMA-Factory 연동). 이 위키의 로컬 추론 축에 **"CPU 오프로딩(MoE 전문가를 CPU로)"** 을 명확히 추가한다 — [[airllm]](레이어 스와핑=메모리↔시간 교환)이 "한 레이어씩 GPU"라면, ktransformers는 "MoE 전문가 가중치를 CPU RAM에 두고 AMX로 계산"하는 다른 벡터. 둘 다 "VRAM 부족을 시간/CPU로 메꾼다"는 같은 철학의 서로 다른 구현.

> [!note] 배경 정보
> 로컬 대형 구동의 4대 축을 이 소스가 명확히 한다: ①양자화 비트폭([[Bonsai-27B]] 삼진 1.71bit·[[Qwen3.6-27B-NVFP4]] 4bit) ②KV 재사용([[LMCache]]) ③레이어 스와핑([[airllm]]) ④**MoE CPU 오프로딩(ktransformers)**. ①이 "가중치를 작게", ③④가 "가중치는 그대로 두고 배치를 바꿔서" 접근한다는 게 갈림. 특히 MoE는 토큰당 일부 전문가만 활성화되므로 "안 쓰는 전문가는 CPU에 둔다"가 구조적으로 잘 맞는다.

## 도메인별 추출 (ai-news / local-llm 교차)

- **신뢰도**: ⭐⭐⭐ — ⭐1.85만 + 칭화대 MADSys Lab 산학 프로젝트로 실재성·기술 신뢰도 확고. "3.7 it/s DeepSeek-V3 on 4×4090" 등 성능 수치는 자체 리포트(원문 벤치 재현 미실측). raw 수치(당일 +360)는 WebFetch 확인(⭐18.5k 일치).
- **즉시 활용**: MAYBE — 내 무인 크론·[[reat-*]] 스택은 API/소형모델 중심이라 초대형 MoE 로컬 구동 필요성은 낮음. 다만 **GLM-5/Kimi-K2.5급을 자체 하드웨어에서 돌려야 할 때** 1순위 후보. Intel AMX(사파이어래피즈+) 있으면 효과 큼, 없으면 이득 제한.
- **6개월 영향력**: "프런티어 MoE = 클라우드 전용"이라는 전제를 흔든다. 양자화(비트폭 축소)와 **직교하는** "구조적 오프로딩" 축이 굳으면, 로컬 대형 구동이 GPU 개수가 아니라 CPU RAM 용량 문제로 이동.
- **대체 관계**: llama.cpp의 CPU 추론을 MoE·이기종·파인튜닝까지 확장한 상위 대안. [[airllm]](레이어 스와핑)·[[LMCache]](KV)와는 경쟁이 아니라 조합 가능한 다른 레이어.
- **허와 실**: "4GB VRAM에 671B"류 극단 클레임([[airllm]])과 달리 ktransformers는 "여러 GPU + 큰 CPU RAM"을 전제한 현실적 오프로딩 — 대신 하드웨어 요구(AMX CPU·수백GB RAM)가 실질 진입장벽. "소비자 하드웨어"는 상대적 표현.
- **액션**: star + AMX 지원 CPU 유무 확인. GLM-5/Kimi-K2.5 로컬 구동이 필요해지는 시점에 kt-kernel 추론 속도 실측.

## 관련 페이지
- [[airllm]]
- [[LMCache]]
- [[Bonsai-27B]]
- [[Qwen3.6-27B-NVFP4]]
- [[local-llm]]
- [[ai-news]]

## 원본
- 출처: https://github.com/kvcache-ai/ktransformers
- GitHub: ⭐18,544 (2026-07-20, 당일 +360) — raw 자동수집 + WebFetch 확인(⭐18.5k)
- 개발: 칭화대 MADSys Lab + 커뮤니티
- 신뢰도: ⭐⭐⭐ (대형·산학 프로젝트, 실재 확고 / 성능 수치는 자체 리포트 미재현)
