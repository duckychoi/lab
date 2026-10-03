---
title: Amazon (Amazon.com, Inc.)
type: entity
domain: local-llm
tags: [entity, 기업, 빅테크, diffusion-lm, usa]
created: 2026-10-03
updated: 2026-10-03
sources: [HC-DLM.md]
reliability: high
---

# Amazon (Amazon.com, Inc.)

> [!insight] 볼트 유입 경로 — **API 가 아니라 PDF 가 찾아냈다**
> **2026-10-03 배치 [[HC-DLM]]** 의 공동 소속. 🔴 **HF 논문 API `organization` 은 `UIUC-CS` 만 보고했고 Amazon 은 나타나지 않았다.** 볼트가 PDF 를 열어 저자 각주를 읽고서야 발견했다.
> ⇒ 📌 **이 엔티티의 존재 자체가 "API 단일 필드가 소속을 숨긴다"의 증거다** → [[복합지표-분해]].

## 볼트 관측 사항

- **[[HC-DLM]]** (2610.02193) — **Huidong Liu** (Amazon.com, Inc.), 공저자 4명은 [[UIUC]].
  - 🎯 **산학 공동 연구**이고 Amazon 쪽 기여 범위는 논문에 명시되지 않는다.
  - 🔴 **Amazon 자원(컴퓨트/데이터) 사용 여부 미확인** — 감사(acknowledgement) 절 미열람.

> [!question] 미해결 질문
> - Amazon 의 이 연구 참여가 **제품 방향(Bedrock·Titan 등)과 연결되는지** 미확인.
> - 볼트에 Amazon 관련 소스가 이 1건뿐이다. **AWS/Bedrock 쪽 소스가 수집기 선발창에 들어온 적이 없다** → 📌 [[선발창-누락]] 후보 영역.

## 관련 페이지
- [[HC-DLM]] · [[UIUC]]
- [[복합지표-분해]] · [[선발창-누락]]
- [[local-llm]]

## 원본
- PDF 실측: `arXiv:2610.02193v1` 저자 각주 2 — *"2Amazon.com, Inc."*
- 신뢰도: ⭐⭐⭐⭐⭐ (PDF 1차 문서 확인) / 🔴 참여 범위는 미확인
