---
title: "pyannote"
type: entity
domain: ai-news
tags: [ai-news, entity, org, speech, diarization, vad]
created: 2026-11-25
updated: 2026-11-25
sources: [pyannote-segmentation-3.0.md, pyannote-community-1.md, pyannote-speaker-diarization.md]
reliability: high
---

## 개요
HF 조직 `pyannote`. 화자 분할 · VAD · 발화 분리의 표준 오픈소스 축. 비즈니스 모델: 오픈 모델(자동 승인 게이트) + 유료 pyannoteAI(카드 상단 전환 권유). 볼트 소스 3건:
- [[pyannote-community-1]] — 커뮤니티 파이프라인 v1
- [[pyannote-speaker-diarization]] — 화자 분리 파이프라인
- [[pyannote-segmentation-3.0]] — 10초 청크 화자 분할 부품(30일 dl 439만 · 2023-09 모델) — 파이프라인의 내부 부품이자 VAD · 겹침발화 검출 단독 용도

## 관찰
- segmentation-3.0의 30일 439만 다운로드는 파이프라인 의존 수요 — **오픈 부품 + 유료 상위 서비스** 구조가 다운로드 규모를 만든 사례([[기준선-재부상]]).
- 볼트의 /down-analysis · /reat-voice 체인이 간접 사용 중일 가능성(미검증).

## 관련 페이지
- [[pyannote-segmentation-3.0]] · [[pyannote-community-1]] · [[pyannote-speaker-diarization]] · [[ai-news]]
