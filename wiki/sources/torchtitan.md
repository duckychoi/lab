---
title: "pytorch/torchtitan — PyTorch 공식 대규모 사전학습 → SFT → RL 단일 스택 (TitanRL · 비트 단위 재현)"
type: source
domain: ai-news
tags: [ai-news, github, training-infrastructure, pytorch, fsdp, moe, distributed-training]
created: 2026-11-24
updated: 2026-11-24
sources: [https://github.com/pytorch/torchtitan]
reliability: medium
---

**GitHub**: ★5,968(볼트 API 11-24 · 수집기 11-23 5,954) · 당일 +10(Python Trending) · Python · BSD-3-Clause · 생성 2023-12-13 · HEAD `692c9bb5b2`(수집기 11-23, 볼트 확인 시점 push 11-24 09:08Z — 활발) · ICLR 2025 논문

## 핵심 인사이트
> [!insight] 설정은 플래그가 아니라 "config를 반환하는 Python 함수(recipe)" — 샤딩을 모델이 선언한다
> 모델이 샤딩 방식을 선언하면 FSDP2 · TP · PP · CP · EP 를 `DeviceMesh`/DTensor 로 N차원 조합하는 PyTorch 네이티브 학습 플랫폼. 2026-08 추가 **TitanRL**: 학습기와 vLLM 생성에 **같은 모델 정의 · 커널**을 쓰고 **비트 단위 재현 가능한 batch-invariant 모드** 지원. MXFP8/NVFP4 저정밀, Dist-MoE, CUDA graph. 지원 모델: Llama 3(1B–405B) · Qwen3/3.5/3.6/3.8(최대 2.4T-A95B) · DeepSeek V3/V4 · gpt-oss · Kimi K2.7/K3 · Muse Glimmer/Spark-Open(816B-A42B) · FLUX.

> [!warning] "검증된 recipe"는 일부뿐 · 성능 수치 0
> 검증된 recipe 가 있는 것은 일부(llama3_8b/70b · qwen3_14b · deepseek_v3_671b · muse 계열 · flux)이고 **나머지는 CI 디버그 설정 통과만**이다. README 에 MFU · 처리량 성능 수치 없음. PyTorch nightly 필수(활발한 개발 중 명시), AMD 는 별도 포크.

## 도메인별 추출 (ai-news)
- **실용성**: 단일 GPU 디버그(`NGPU=1 ./run_train.sh`)는 바로 돌아가지만 본 용도는 멀티노드 클러스터 — 개인 로컬 환경 직접 효용 낮음, **학습 인프라 동향 파악용**.
- **동향 신호**: 2026년 오픈 학습 스택의 표준 방향이 "샤딩 선언은 모델이, 조합은 프레임워크가"로 수렴. TitanRL 의 **학습-생성 커널 공유 + batch-invariant 재현**은 RL 후학습 파이프라인의 재현성 요구가 인프라 기능으로 흡수되고 있다는 신호.
- **지원 모델 목록 자체가 정보**: Qwen3.8(2.4T-A95B) · Kimi K2.7/K3 · Muse 816B-A42B — 2026년 말 프런티어 오픈 모델의 크기 · 활성 스케일 확인창([[파라미터-다중표기]]).
- **액션**: 없음(관찰).

## 관련 페이지
- [[PyTorch]] · [[Mooncake]] · [[latent-MoE]] · [[ai-news]]

## 원본
- 출처: https://github.com/pytorch/torchtitan
- 확인 범위: GitHub API(스타 · 언어 · 라이선스 · 생성일 · push — 볼트 11-24) · README 내용은 수집기 11-23 판독 · 실행 0
- 신뢰도: ⭐⭐⭐
