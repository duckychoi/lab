---
title: OpenBMB
type: entity
domain: local-llm
tags: [local-llm, edge-ai, slm, openbmb, on-device, minicpm]
created: 2026-07-10
updated: 2026-09-10
sources: [MiniCPM5-2B.md, MiniCPM5-1B.md, MiniCPM-V-4.6.md]
reliability: high
---

# OpenBMB

> [!insight] 핵심 인사이트
> **온디바이스/엣지용 소형 LLM(SLM)에 특화된 오픈 연구·개발 조직**으로, 이 위키에서는 **MiniCPM 시리즈**의 제작사로 등장한다. ①**[[MiniCPM5-1B]]**(1.08B, 131K 컨텍스트, think/fast 2모드, 도구호출, RL+OPD로 수학·코드 +16점) — "1B급 오픈 SOTA"를 표방하는 순수 텍스트 SLM, ②**[[MiniCPM-V-4.6]]** — 동급 스케일 멀티모달 VLM. OpenBMB의 일관된 노선은 "**작게 만들되 도구 사용·추론까지 넣어 실제 온디바이스에서 쓸모 있게**" — BF16/GGUF/MLX 다포맷과 FlagOS 다칩 지원으로 CPU·스마트폰·임베디드 배포를 겨냥. 내 [[에이전트-메모리-레이어]]·경량 에이전트 백엔드 후보 공급원.


> [!insight] 2026-09-10 — [[MiniCPM5-2B]]: **밀집 2B가 4B급 5종을 평균에서 상회**
> MiniCPM5 계열 2번째. 카드 평균 **53.9** 로 2B급 3종(33.2/28.0/24.6)뿐 아니라 **4B급 5종 전부**(51.1/42.7/32.6/31.2/28.4)를 앞선다. **SWE-bench Verified 46.4**(차상위 36.8) · **NoLiMa 68.1**(차상위 43.5, 나머지는 0.5~17.1로 붕괴) · GAIA Text-103 **88.7**.
> **OpenBMB 노선이 [[MiniCPM5-1B]] 에서 한 단계 확장됐다** — "작게 만들되 도구·추론을 넣는다"에 **코퍼스 전면 공개**가 더해졌다(Ultra-FineWeb·UltraX·UltraData 계열 + 후학습 SFT 400B 토큰 · SFT→RL→OPD 3단계). 배포 백엔드 **9종**.
> 🎯 **[[K2-Horizon-MoVA-36B-A4B]] 와 결정적 대비**: K2는 코드·체크포인트가 *"예고(coming)"* 였고 OpenBMB는 **학습 코퍼스를 실제로 냈다**. 같은 "오픈"이라도 등급이 다르다.
> ⚠️ **약점을 숨기지 않되 약점은 분명하다** — 일반지식·**지시이행 열위**(IFEval 86.7 vs LFM2.5-**2.6B** 93.4 — **더 작은 모델에도 진다**), SWE-bench **Pro** 14.4 vs 28.2.
> 🔴 **볼트 추가 발견**: 카드 각주는 *"† 만 Artificial Analysis 공식, 나머지 전부 내부 재현"* 인데 — **† 항목(제3자 측정)에서는 대체로 진다**(GPQA-D 70.2 vs 77.1 · Terminal-Bench 8.6 vs 25.8). **이기는 축은 자체측정, 지는 축은 제3자 측정**이라는 상관이 보인다 → [[측정도구-먼저-반증]]

## 관련 소스
- [[MiniCPM5-2B]] — 밀집 2B, 4B급 5종을 평균 상회, 코퍼스 공개 *(2026-09-10 신규)*
- [[MiniCPM5-1B]] — 1.08B 온디바이스 SLM (131K, think/fast, RL+OPD) *(2026-07-10 갱신)*
- [[MiniCPM-V-4.6]] — 동급 멀티모달 VLM

## 관련 페이지
- [[에이전트-메모리-레이어]] — 경량 로컬 에이전트 백엔드 후보
- [[온폴리시-증류]] — MiniCPM5 학습에 쓰인 OPD 흐름
- [[Qwen3.6-27B]] — 오픈 멀티모달 계열(스케일 대극)
- [[local-llm]] · [[ai-news]]

## 원본
- 조직: OpenBMB (온디바이스 SLM 오픈 개발)
- 대표 산출물: [[MiniCPM5-1B]], [[MiniCPM-V-4.6]] (MiniCPM 시리즈)
- 신뢰도: ⭐⭐⭐⭐ (다운로드 수십만+ 지속, 다포맷 오픈 배포)
