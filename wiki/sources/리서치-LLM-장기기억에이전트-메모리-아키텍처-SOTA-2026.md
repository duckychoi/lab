---
title: "[리서치] LLM 장기기억·에이전트 메모리 아키텍처 SOTA (2026)"
created: 2026-10-18
updated: 2026-10-18
author: research-agent
origin: cron-research-agent
tags: [research-agent, ai-news]
---
웹검색으로 2026년 LLM 장기기억 및 에이전트 메모리 아키텍처의 최신 동향을 조사하겠습니다.
이제 한국어로 최신 동향을 정리하겠습니다.

## LLM 장기기억·에이전트 메모리 아키텍처 SOTA (2026)

**핵심 3줄**
- 
LLM 에이전트의 장기기억은 큐레이션된 워킹 뷰, 비정렬 저장소에 대한 검색, 계층화된 메모리 제어의 세 가지 아키텍처 계통으로 진화

- 
명시적이고 지속적인 메모리 메커니즘이 추론 이후로 적응적으로 진화하며 모델의 능력 확장에 직교 방향의 경로 제공

- 
AgeMem은 저장, 검색, 업데이트, 요약, 폐기라는 5가지 메모리 작업을 에이전트 정책 내 호출 가능한 도구로 강화학습 최적화


**상세**
- **아키텍처 3가지 패턴**: 
①모놀리식 컨텍스트(프롬프트 내 모든 메모리, 투명하지만 용량 제한), ②컨텍스트+검색 저장소(워킹 메모리/장기 기록 분리), ③계층화된 메모리+학습된 제어(컨텍스트, 구조화된 DB, 벡터 저장소, 콜드 아카이브 티어)


- **주요 2026년 연구 성과**:
  - 
LLM 에이전트를 위한 적응형 메모리 구조

  - 
감쇠 기반 활성화를 통한 자가적응 에이전트 메모리 제어(Oblivion)

  - 
속성 기반 밀집 보상을 통한 장기기억 구축(MemBuilder)

  - 
자동연구를 통한 자가진화 메모리 아키텍처(EvolveMem)


- **벤치마크 성과**: 
SuperMemory가 LongMemEval에서 ~85%에서 ~99%로 상향, 모든 공개 벤치마크 메모리 시스템 상회
; 
TeleMem: Mem0 대비 19% 높은 정확도, 43% 감소한 토큰, 2.1배 빠른 속도


- **프로덕션 시스템**: 
EverOS v1.0.0은 Cases와 Skills를 메모리 1급 객체로 취급하며 에이전트가 자신의 작업 학습 내용 검색 가능
; 
Mem0(LLM 기반 사실 추출), Zep/Graphiti(시간 기반 지식 그래프), Letta(계층화 메모리+자가편집)


- **멀티모달 & 실시간**: 
WorldMemArena는 행동-환경 상호작용을 통해 멀티모달 에이전트 메모리 평가
; 
3D 가우시안 스플래팅을 지속적 공간 메모리로 활용한 제로샷 구현 탐색


- **보안 & 거버넌스**: 
LLM 에이전트 장기기억의 보안 공격, 방어, 거버넌스 전 생명주기 조사
; 
독 허가권으로 중독 공격 방어(비-가단형)


**💡 인사이트/시사점**
- 메모리가 스케일링과 동등한 아키텍처 차원으로 부상하면서 지속적 파라미터 업데이트와 학습된 제어 정책이 표준화됨. 단순 벡터 검색에서 그래프 기반, 시간적 타당성, 자가진화 메커니즘으로 급속 진화 중.
- 프로덕션에서는 계층화 구조(컨텍스트/구조화 DB/벡터/아카이브)와 에이전트가 주도하는 메모리 정책 최적화(RL 기반)가 주류. 벤치마크 경쟁이 치열해지면서 신뢰성 있는 평가(LoCoMo, LongMemEval) 체계 정립 중요성 증가.

**출처**
- MemChain: Learning Interpretable Memory Traces — https://arxiv.org/pdf/2607.24097
- Mi-Memory: A Lifecycle Memory Framework — https://arxiv.org/pdf/2607.18975
- Always-On Agents Survey — https://arxiv.org/pdf/2606.30306
- Memory for Autonomous LLM Agents — https://arxiv.org/html/2603.07670v1
- Ground Truth First: Longitudinal Evaluation — https://arxiv.org/pdf/2607.21962
- LycheeMemory V2 — https://arxiv.org/pdf/2608.12990
- EverMind AI Blog (2026 베스트 메모리 시스템) — https://evermind.ai/blogs/top-ai-memory-systems-benchmarked-in-2026
- Awesome Agent Evolution (GitHub) — https://github.com/EvoMap/awesome-agent-evolution
- Memory for Large Language Models Survey — https://arxiv.org/pdf/2607.25380
