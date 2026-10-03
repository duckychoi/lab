---
title: University of Illinois Urbana-Champaign (UIUC)
type: entity
domain: local-llm
tags: [entity, 대학, 연구기관, diffusion-lm, usa]
created: 2026-10-03
updated: 2026-10-03
sources: [HC-DLM.md]
reliability: high
---

# University of Illinois Urbana-Champaign (UIUC)

> [!insight] 볼트 유입 경로
> **2026-10-03 배치 [[HC-DLM]] 논문의 제1 소속**으로 볼트에 처음 등록. HF 논문 API `organization` 값은 **`UIUC-CS`**(fullname: *University of Illinois at Urbana-Champaign*).

## 볼트 관측 사항

- **[[HC-DLM]]** (2610.02193 · 2026-10-01 · upvote 70) — 저자 **Hui Ren · Zihan Li · Chang Liu · Alexander Schwing**(UIUC) + **Huidong Liu**([[Amazon]]).
  - 🏆 **Alexander Schwing** — UIUC 교수. 볼트에 처음 등장하는 연구자.
  - ✅ **비교 설계가 오늘 배치 최고 수준**이었다: 베이스라인 CCDD 를 **6M 파라미터로 재현 + 백본 교체**해 공정 비교하고, **파라미터 정의(샘플링 시점 생성 파라미터, 토큰 임베딩 제외)까지 명시** → [[비매칭-비교]] 모범 사례.
  - 🔴 **그러나 초록이 Sudoku Easy split 패배를 뭉갰다**(본문은 `94.65 vs. 94.21` 로 인정) → [[표-부분인용]].
  - 🔴 **공개 레포 `rhfeiyang/HC-DLM` 에 코드가 없다**(★52 · `languages` 비어 있음) → [[선언된-구현체-공백]] **활력형 공백**.

> [!warning] 🔴 `organization` 필드가 공동 소속을 숨긴다
> HF API 는 **`UIUC-CS` 단일**로 보고하지만 PDF 실측 소속은 **UIUC + Amazon.com, Inc. 2개 기관**이다.
> ⇒ 📌 같은 배치 [[Sharpening-Tax]] 에서 같은 현상이 더 크게 확인됐다([[Meta]] 단일 보고 ↔ 실제 4기관). ⚖️ **`organization` 은 제1저자 소속만 반영한다. 소속 목록으로 쓰면 안 된다.**

## 관련 페이지
- [[HC-DLM]] · [[Amazon]]
- [[선언된-구현체-공백]] · [[비매칭-비교]] · [[표-부분인용]]
- [[local-llm]]

## 원본
- HF 논문 API `organization.name = UIUC-CS`
- PDF 실측: `arXiv:2610.02193v1` 저자 각주 1
- 신뢰도: ⭐⭐⭐⭐⭐ (PDF 1차 문서 확인)
