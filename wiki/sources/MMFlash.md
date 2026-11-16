---
title: "MMFlash — VLM 용 블록 확산 드래프터 투기적 디코딩 (시각 의존 토큰 가중, 최대 3.58×)"
type: source
domain: local-llm
tags: [local-llm, speculative-decoding, vlm, inference, paper]
created: 2026-11-16
updated: 2026-11-16
sources: [https://huggingface.co/papers/2611.18482]
reliability: medium
---

**논문**: arXiv 2611.18482 · 업보트 25 · HF 조직 NationalUniversityofSingapore · 코드 [fscdc/MMFlash](https://github.com/fscdc/MMFlash) ★13.

## 핵심 인사이트
> [!insight] 드래프터가 틀리는 곳은 "이미지를 봐야 아는 토큰"이다
> 시각 입력 유무에 따른 다음 토큰 분포 KL 로 **토큰별 시각 의존도**를 정의 → 수용률이 의존도 최하위 사분위 **46% → 최상위 22%**, 멀티모달 학습 후에도 격차 유지. 그래서 드래프터가 못 맞히는 시각 의존 토큰에 학습 가중치를 높이고, 긴 영상 입력엔 희소 어텐션. [[dflash]] 계열(블록 단위 확산 드래프터)을 VLM 으로 확장.

## 도메인별 추출 (local-llm)
- **실용성 판단**: 무손실 **최대 3.58×**, EAGLE-3 대비 최대 +195.4% · DFlash 대비 최대 +17.1%.
- **트레이드오프**: 평균 가속 · 대상 VLM · 하드웨어는 초록에 없음 — 전부 "up to" → [[천장-기준선]].
- **Hermes 적용**: 로컬 VLM 서빙(llama.cpp/vLLM) 에 드래프터가 붙을 때까지는 NO.
- **오픈소스 구현체**: 코드 ★13.

## 관련 페이지
- [[dflash]] · [[천장-기준선]] · [[SteerDistill]](같은 배치 · 추론 효율) · [[local-llm]]

## 원본
- 출처: https://huggingface.co/papers/2611.18482
- 확인 범위: HF papers API 초록 전문 · 코드 링크(볼트) · 🔴 본문 미열람
- 신뢰도: ⭐⭐
