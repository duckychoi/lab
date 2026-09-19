---
title: Fastino — GLiNER2 계열 정보추출 모델 공급자
type: entity
domain: ai-news
tags: [ai-news, entity, information-extraction, encoder, 신설]
created: 2026-09-19
updated: 2026-09-19
sources: [GLiNER2.md, gliner2.5-multi-v1.md]
reliability: medium
---

# Fastino

> [!insight] 핵심 — **작은 인코더로 스키마 기반 정보추출을 로컬에서** 돌리는 쪽에 베팅한 회사
> GitHub `fastino-ai`(레포 [[GLiNER2]] ★1,977) + HF org `fastino`(체크포인트 9종: span 계열 6 · boundary 계열 3). 대표 모델 [[gliner2.5-multi-v1]](30일 DL 183,555).
> 🎯 오픈 가중치와 **상용 API(`GLiNER2API`/Pioneer)·파인튠 서비스**를 함께 운영한다 — 🔴 기본 `pip install gliner2` 가 클라우드 API 클라이언트를 설치하고, 로컬 실행은 `[local]` extra가 필요하다.

> [!warning] 🔴 문서와 실물의 차이 (09-19 볼트 실측)
> - 카드 "~594MB FP16" ↔ 실물 safetensors **F32 1.15GB** → [[파생표기-함정]]
> - `GLiNER2.from_pretrained()` 로는 2.5(boundary) 체크포인트를 **못 연다** — `AutoExtractor` 필요
> - 2.5 계열 **품질 벤치 0개**. 원 논문(EMNLP 2025 Demo, Zaratiana 외 5명)은 v1 span 205M 수치만 있다

## 산출물
- [[GLiNER2]] — 레포(컨테이너) · [[컨테이너-중복]] 사례 2
- [[gliner2.5-multi-v1]] — 287M 다국어 boundary 모델

## 관련 페이지
- [[GLiNER2]]
- [[gliner2.5-multi-v1]]
- [[컨테이너-중복]]
- [[파생표기-함정]]

## 원본
- https://github.com/fastino-ai/GLiNER2 · https://huggingface.co/fastino
- 신뢰도: ⭐⭐ (API 실측 · 🔴 2.5 품질 수치 부재)
