---
title: XHToken — Spark 계열 소형 모델 개발사
type: entity
domain: local-llm
tags: [entity, model-publisher, slm, ascend, china, open-weights]
created: 2026-09-09
updated: 2026-09-09
sources: [Spark-X2.5-4B.md]
reliability: medium
---

# XHToken

> [!note] 정체
> **Spark-X2.5** 계열(4B · 1.7B) 소형 범용 언어모델을 Apache-2.0으로 공개한 곳. 볼트 최초 수집 **2026-09-09**([[Spark-X2.5-4B]] 경유, 수집 시점 **HF 트렌딩 1위**).

## 확인된 사실 (모델 카드 실측)

- **모델**: [[Spark-X2.5-4B]], Spark-X2.5-1.7B (+ 각 Base 버전). Apache-2.0.
- **학습 인프라**: **화웨이 Ascend 클러스터**. 사전학습 약 **20조 토큰**.
- **하드웨어 지향**: NVIDIA 외 **Huawei · Hygon · HOUMO.AI** 지원 명시 → **중국 국산 가속기 생태계** 대응.
- **후처리 기법**: 도메인별 교사 정책을 만든 뒤 **MOPD**로 단일 배포 모델에 통합.
- **채널**: Slack · Discord · YouTube(@SparkLLM) · dev.to · Bluesky · X · Zhihu · WeChat — **영어권과 중국어권 채널을 동시 운영**.

> [!question] 미확인
> 법인 실체·소속·자금 배경을 볼트가 확인하지 않았다. 모델 카드에 조직 소개가 없고, `XHToken` 이라는 HF 조직명 외 공식 사이트를 확인하지 못했다. **회사 규모·국적을 단정하지 말 것**(Ascend 사용과 Zhihu/WeChat 채널은 중국 연관을 시사하나 증거로 확정하기엔 약하다).

## 관련 페이지
- [[Spark-X2.5-4B]]
- [[에이전트축-분기]]
- [[Alibaba]]
- [[Zhipu-AI]]
