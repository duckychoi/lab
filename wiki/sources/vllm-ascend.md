---
title: "vllm-ascend — 화웨이 Ascend NPU에서 vLLM을 돌리는 공식 하드웨어 플러그인"
type: source
domain: ai-news
tags: [ai-news, github, vllm, npu, ascend, huawei, serving, hardware-plugin]
created: 2026-11-25
updated: 2026-11-25
sources: [https://github.com/vllm-project/vllm-ascend]
reliability: high
---

**레포**: vllm-project/vllm-ascend · ★ **3,142**(수집기 11-24) → **3,148**(볼트 API 11-25) · Python 일간 Trending(당일 +5) · Apache-2.0 · 생성 2025-01-29 · push 2026-11-25

## 핵심 인사이트
> [!insight] 본체(vLLM)를 고치지 않는 "하드웨어 플러그인" — 플러그인 패턴의 인프라 버전
> vLLM 커뮤니티가 공식으로 만든 레포. vLLM RFC #11162 방식으로 **Ascend NPU 백엔드를 플러그인으로** 붙인다 — vLLM 본체 수정 0. README 기준 Transformer · MoE · 임베딩 · 멀티모달 LLM 지원, 세부는 별도 Support Matrix 문서. 안정판 v0.30.0(2026-10), main은 vLLM v0.33.0 태그를 CI로 추적. [[동결-교정층]] 의 패턴(본체 동결 + 얇은 바깥층)이 **모델이 아니라 서빙 스택**에서도 같은 모양으로 나타난 사례.

> [!warning] 요구 조건이 좁다 — NVIDIA 환경 사용자에게는 무관
> Atlas 800I A2/A3 · 300I Duo · 950PR/950DT 하드웨어, Linux, **Python 3.12 고정**, CANN 9.2.1, PyTorch 2.10.0 + TorchNPU 2.10.0.post7, vLLM은 같은 버전이어야 한다. 벤치마크 · 처리량 수치는 README에 없다.

## 도메인별 추출 (ai-news)
- **실용성**: Ascend 장비를 가진 조직에는 사실상 표준 경로. NVIDIA 환경에는 해당 없음.
- **대체 관계**: [[vllm]] 의 비-NVIDIA 확장 사례 — [[Mooncake]](KV캐시 분리 서빙)와 함께 서빙 인프라 축의 조각.
- **허와 실**: "공식"은 vLLM 커뮤니티 프로젝트라는 뜻이지 화웨이 품질 보증이 아니며, 하드웨어 게이트가 좁아 실 배포 경험은 장비 보유 조직에서만 나온다.
- **액션**: 없음(관찰 — Ascend 장비 없음).

## 관련 페이지
- [[vllm]] · [[Mooncake]] · [[동결-교정층]] · [[ai-news]]

## 원본
- 출처: https://github.com/vllm-project/vllm-ascend
- 확인 범위: README(수집기 11-24) · GitHub API 재확인(볼트 11-25 — ★ · 언어 · 라이선스 · 생성일 · push 일치) · 실행 0
- 신뢰도: ⭐⭐⭐ (★3천+ · vllm-project 산하 공식 플러그인)
