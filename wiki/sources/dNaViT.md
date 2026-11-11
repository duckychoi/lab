---
title: "dNaViT — 고정 인코더 위 residual modulation + grouped product quantization 으로 만든 네이티브 해상도 이산 비전 토크나이저 (초록 수치 0)"
type: source
domain: ai-news
tags: [ai-news, hf-paper, vision-tokenizer, discrete-tokens, multimodal, meituan]
created: 2026-11-11
updated: 2026-11-11
sources: [https://huggingface.co/papers/2611.12426]
reliability: low
---

**논문**: [2611.12426](https://huggingface.co/papers/2611.12426) · [[Meituan]] LongCat(HF org `meituan-longcat`) · 업보트 **28**(11-11 Daily Papers 1위, 수집기) · 코드 링크 없음(HF papers API `githubRepo: null`)

## 핵심 인사이트
> [!insight] "비전도 언어처럼 이산 토큰으로"의 부품
> 고정된 사전학습 인코더에 가벼운 residual modulation 과 이중 목적(의미·재구성)을 얹고, **grouped product quantization** 으로 공간 시퀀스 길이를 늘리지 않은 채 이산 용량을 키운다. 하나의 이산 코드로 이해·생성·편집을 모두 처리하는 것이 목표(초록 전문 일치).

> [!warning] 초록에 수치가 없다
> 근거는 *"12개 이해 벤치 · 4개 생성 벤치 · 1개 편집 벤치에서 과제별 베이스라인과 동등하거나 상회(matches or exceeds)"* 라는 정성 문장뿐이다. "동등"과 "상회"가 몇 대 몇인지, 베이스라인이 무엇인지 초록으로는 알 수 없다. 업보트 1위는 수치가 아니라 주제가 만든 순위다.

## 도메인별 추출 (ai-news)
- **신뢰도**: 업보트 28 · 코드 없음 · 초록 수치 0 → `low`.
- **즉시 활용**: NO — 코드·가중치 미공개.
- **6개월 영향력**: 통합 멀티모달(이해+생성) 모델의 토크나이저 선택지. 영상 생성 쪽으로 번지면 [[video-saas]] 에 영향.
- **허와 실**: 본문 표를 보기 전에는 판단 불가.
- **액션**: 없음(코드 공개 시 재확인).

## 관련 페이지
- [[Meituan]] · [[LongCat-2.0]] · [[MiniMax-H3-Image]](같은 날 입고된 생성 모델)

## 원본
- 출처: https://huggingface.co/papers/2611.12426
- 확인 범위: HF papers API 초록 전문 · 🔴 본문 미열람
- 신뢰도: ⭐ (업보트 28 · 코드 없음)
