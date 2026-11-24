---
title: "kvcache-ai/Mooncake — Kimi 서빙용 KV캐시 중심 분리(PD disaggregation) 인프라 · FAST'25 Best Paper"
type: source
domain: ai-news
tags: [ai-news, github, serving-infrastructure, kv-cache, pd-disaggregation, rdma, moe, kimi]
created: 2026-11-24
updated: 2026-11-24
sources: [https://github.com/kvcache-ai/Mooncake]
reliability: medium
---

**GitHub**: ★7,120(볼트 API 11-24 · 수집기 11-23 7,114) · 당일 +6(C++ Trending) · C++ · Apache-2.0 · 생성 2024-06-25 · HEAD `19542b6a3e`(수집기 11-23) · open issues 1,110(PR 포함, 수집기) · FAST'25 Best Paper

## 핵심 인사이트
> [!insight] prefill · decode를 떼어놓고, 놀고 있는 CPU · DRAM · SSD를 KV캐시 풀로 쓴다
> [[Moonshot AI]](Kimi) 서빙 플랫폼. 구성 3층: ① **Transfer Engine** — RDMA 멀티 NIC 대역폭 집적 · 토폴로지 인지 경로 선택 · 장애 우회(TCP · RDMA · AWS EFA · NVLink · CXL · Ascend) ② **Mooncake Store** — 분산 KV캐시 · 모델 가중치 저장(DRAM/SSD 다층 · 복제 · 고정 정책) ③ **Mooncake EP/PG** — 장애 rank 우회 MoE expert-parallel(DeepEP 호환 API). SGLang · vLLM · TensorRT-LLM · LMDeploy · LMCache 에 커넥터로 통합.

> [!warning] 수치는 전부 자체 · 파트너 발표 기준
> 실워크로드 SLO 준수하며 처리 요청 **+75%**(Kimi) · Transfer Engine 40GB 전송 **87GB/s(4×200Gbps RoCE) · 190GB/s(8×400Gbps)** = TCP 대비 2.4배 · 4.6배 · Kimi K2 128×H200 에서 prefill 224k · decode 288k tok/s · SGLang RL 가중치 갱신 53s → 7.2s(1T 파라미터). 🔴 **소비자 하드웨어 수치는 없다** — 데이터센터 RDMA 환경 전제.

## 도메인별 추출 (ai-news)
- **실용성**: 로컬 1–2 GPU 사용자에게 직접 쓸 일은 거의 없음 — vLLM/SGLang 의 PD 분리 · KV 공유 기능의 **밑단을 이해하는 참고용**. 이 기능들이 "어디서 왔는가"의 원점.
- **동향 신호**: KV캐시가 임시 상태에서 **분산 스토리지 계층**(복제 · 고정 · 다층 계층화)으로 승격. [[torchtitan]] 이 학습 쪽이라면 이쪽은 서빙 쪽 — 같은 배치의 인프라 2건([[torchtitan]] · Mooncake)은 "모델 밖 계층이 비용을 결정"([[하네스-설계-축]]의 데이터센터 버전).
- **선발 성격**: ★7,120 · 당일 +6 — 급상승이 아니라 성숙 인프라 기록분(수집기 스스로 명시).
- **액션**: 없음(관찰).

## 관련 페이지
- [[Moonshot AI]] · [[Kimi-K3]] · [[torchtitan]] · [[하네스-설계-축]] · [[ai-news]]

## 원본
- 출처: https://github.com/kvcache-ai/Mooncake
- 확인 범위: GitHub API(스타 · 언어 · 라이선스 · 생성일 — 볼트 11-24) · README 수치는 수집기 11-23 판독(볼트 문자열 검증 미실시) · 실행 0
- 신뢰도: ⭐⭐⭐
