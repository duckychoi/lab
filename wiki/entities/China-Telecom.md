---
title: China Telecom — TeleChat·Xing 계열, Ascend 학습
type: entity
domain: local-llm
tags: [local-llm, ai-news, entity, ascend, mindspore, china, 신설]
created: 2026-09-19
updated: 2026-09-19
sources: [Xing4.0-29B-A4B.md]
reliability: medium
---

# China Telecom (중국전신)

> [!insight] 핵심 — **국산 연산(Ascend NPU) + 국산 프레임워크(MindSpore)** 로 학습하는 것이 정체성
> [[Xing4.0-29B-A4B]](구 TeleChat, 09-16): 29B-A4B MoE(MLA+mHC+MTP), 카드 개발사 "China Telecom Artificial Intelligence Technology Co., Ltd."(中电信人工智能科技有限公司).
> 전작 **TeleChat3-MoE**(arXiv 2512.24157, 저자 54): 105B~1T+ 를 *"end-to-end on Ascend NPU cluster"* 로 학습.

> [!warning] 🔴 "첫 모델" 주장은 한정어가 전부다
> 영문 *"the first model **of this scale**…"* / 중문 *"**国内首个**…**百亿参数**…**面向复杂工程任务**"* — 두 언어의 한정어가 다르고, **전작이 이미 더 큰 모델을 Ascend로 학습**했다 → [[한정어-탈락]]
> 🔴 TeleChat3 README 는 中国电信人工智能研究院(TeleAI) 로 표기 — 두 법인의 관계 **미확인**.

## 산출물
- [[Xing4.0-29B-A4B]] · TeleChat3-MoE(볼트 미보유)
- 배포: HF · ModelScope · Modelers

## 관련 페이지
- [[Xing4.0-29B-A4B]]
- [[한정어-탈락]]

## 원본
- https://huggingface.co/XingChen-AGI (멤버 10 · 팔로워 101 · 미인증)
- 신뢰도: ⭐⭐ (카드·README 원문 · 법인 관계 미확인)
