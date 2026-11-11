---
title: "Ripple-65B-Preview — 12T 토큰 스크래치 사전학습 65B dense 모델: Terminal-Bench 2.1 80.5(자체 측정)로 501B·816B 모델과 나란히, GPQA 는 비교군 최하"
type: source
domain: local-llm
tags: [local-llm, hf-model, dense-transformer, agentic-coding, long-context, ricursive]
created: 2026-11-11
updated: 2026-11-11
sources: [https://huggingface.co/ricursiveAI/Ripple-65B-Preview]
reliability: medium
---

**모델**: [ricursiveAI/Ripple-65B-Preview](https://huggingface.co/ricursiveAI/Ripple-65B-Preview) · dl30 **6,480** · likes **490** · created 2026-11-04 · Apache-2.0 · 파라미터 **64.78B**(safetensors 64,782,689,360) (HF models API 볼트 실측)

## 핵심 인사이트
> [!insight] 작은 팀이 dense 65B 로 에이전트 코딩 한 축만 맞췄다
> Olmo 3 기준선에서 출발해 처음부터 **12T 토큰** 사전학습(카드 23·53행), 최대 컨텍스트 1,048,576 토큰. 카드 표에서 Terminal-Bench 2.1 **80.5** 는 Reflection Beam 501B(80.1) · Muse Spark Open 816B(76.4)와 같은 줄에 선다. 2×B200 · batch 8 에서 250 tok/s(카드 51행), MFU 40%(39행).

> [!warning] 80.5 옆에 붙어 있는 것들
> - 표의 행 이름 자체가 **"Terminal-Bench 2.1 (self-reported)"** 다(카드 110행). 카드는 에이전트 벤치 재현이 어렵고 결과가 *best-effort* 비교라고 적었다(89행). 하네스가 항목별로 다르다는 것은 수집기 판독.
> - 같은 표에서 **GPQA Diamond 85.2 는 비교 5개 모델 중 최하**(87.0 · 87.2 · 89.0 · 90.6), **SWE-bench Verified 76.5 는 5개 중 4위**(최고 81.6), MMLU-Pro 84.2 도 상위 3개(86.8~87.9)보다 낮다(카드 102~113행 볼트 확인). 강점은 Terminal-Bench · SWE-bench Pro(61.42, 2위) 쪽에 몰려 있다 → 헤드라인 한 행으로 전체를 대표시키면 [[표-부분인용]].
> - 이탤릭 = 자체 측정, 그 외 = 공식치 혼합(카드 표기 · 수집기) — 열마다 측정 주체가 다르다.
> - Preview · 경량 후학습 단계(수집기).

## 도메인별 추출 (local-llm)
- **실용성 판단**: 65B dense BF16 은 가중치만 약 130GB(64.78B × 2바이트, 볼트 계산). NVFP4 변형으로 DGX Spark 급에 올린다는 것은 카드 주장(수집기) — 볼트 미확인.
- **메모리 아키텍처**: 해당 없음(모델). 1M 컨텍스트는 외부 메모리 없이 긴 세션을 버티는 쪽의 접근 — 같은 날 [[billion-context]] 는 반대로 100K 창 + 압축을 택했다.
- **Hermes 적용**: NO — 로컬 소비자 하드웨어 범위 밖.
- **트레이드오프**: 에이전트 코딩 강점 ↔ 지식·과학 문항 열세(위 표).
- **오픈소스 구현체**: 가중치 Apache-2.0 공개.

## 관련 페이지
- [[Qwen3.8-27B]] · [[Arete-27B]] · [[Kimi-K3.1-Pro]] · [[billion-context]] · [[표-부분인용]]

## 원본
- 출처: https://huggingface.co/ricursiveAI/Ripple-65B-Preview
- 확인 범위: HF models API · 카드 raw(12,403B) 표 행 대조 · 🔴 카드 전문 정독 아님 · 실행 0건
- 신뢰도: ⭐⭐ (dl30 6,480 · 핵심 수치 자체 측정)
