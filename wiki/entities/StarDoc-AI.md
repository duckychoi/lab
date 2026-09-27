---
title: StarDoc-AI — TeleOCR 제작 조직 (구 NaviDC-OCR)
type: entity
domain: local-llm
tags: [local-llm, ai-news, ocr, 문서파싱, vlm, 정규명-우선-중복검사]
created: 2026-09-27
updated: 2026-09-27
sources: [TeleOCR.md]
reliability: low
---

# StarDoc-AI

> [!note] 볼트가 확인한 것만
> HuggingFace 조직 `StarDoc-AI` 로 **[[TeleOCR]]** 를 배포한다 — **약 1.42B**(실측) 경량 문서파싱 VLM, **Apache-2.0**.
> **2026-09-10 에 `NaviDC-OCR` → `TeleOCR` 로 개명**했다 → [[정규명-우선-중복검사]] 사례.
> 부속 GitHub **`caipeng328/TeleOCR`** · 기술보고서 **arXiv 2608.12898**.
> 🎯 **공개 성향이 있다**: Apache-2.0 + 기술보고서 + 코드 레포를 모두 갖췄고, **Dr.DocBench 수치가 대회 공식 순위가 아니라 자체 평가임을 카드에 명시**한다 → [[자기제한-명시]].

> [!warning] 🔴 조직 실체 미확인
> ⚠️ 모델명 접두어 `Tele` 와 조직명 `StarDoc` 이 **통신사 계열**([[China-Telecom]] 등)을 암시할 수 있으나 **볼트가 확인하지 않았다.** 🔴 **이름만 보고 소속을 추정해 적지 않는다** — 09-24 `NOASSERTION` 교훈(도구·표기의 한계를 세계의 속성으로 읽지 말라)의 같은 계열이다.
> ⬜ 회사 규모·국가·자금 미조사. 부속 GitHub 소유자가 개인 계정(`caipeng328`)인 점은 **소규모 팀 또는 연구자 주도**를 시사하나 역시 추정이다.
> → actionable: HF org 페이지 + 부속 GitHub 조직 정보 조회.

## 관련 페이지
- [[TeleOCR]] — 배포 모델
- [[China-Telecom]] — **추정 연관, 미확정**
- [[정규명-우선-중복검사]] · [[자기제한-명시]] · [[단위-불일치]]
- [[Docling-Project]] · [[PageIndex]] — 문서 파싱 인접 조직·도구

## 원본
- 출처: https://huggingface.co/StarDoc-AI
- 신뢰도: ⭐ (**모델 1건 기준** — 조직 실체·소속 미확인)
