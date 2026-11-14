---
title: DAGroup-PKU
type: entity
domain: video-saas
tags: [entity, research-group, pku, image-generation, video-generation]
created: 2026-11-14
updated: 2026-11-14
sources: [G-STAR.md, PhysLoop.md]
reliability: medium
---

# DAGroup-PKU

> [!insight] 한 줄
> GitHub 조직 `DAGroup-PKU`. 2026-11-13 HF 데일리 페이퍼 상위 10편 중 **2편**([[PhysLoop]] 3위 · [[G-STAR]] 4위)이 이 조직 레포를 코드로 걸었고, 두 논문의 마지막 저자가 모두 **Daquan Zhou** 다(HF papers API 저자 목록 볼트 확인).

## 소스
- [[G-STAR]](arXiv 2611.13004 · 42 up · 코드 ★25) — 그룹 크기를 압축률 제곱으로 키워 32×/64× 압축 이산 AR 이미지 생성 · 1024px 2.5초(H200) · 기존 이산 AR 대비 20×.
- [[PhysLoop]](arXiv 2611.16748 · 44 up · 코드 ★34) — LLM 물리 지식을 하네스로 묶어 영상 생성 모델의 학습 영상 구축 · 국소 수리 · 영상 10만 개 공개.

## 관찰
- 두 논문 모두 **생성 모델의 효율/데이터** 쪽이고, 초록에 벤치 점수를 적지 않는다(G-STAR "competitive" · PhysLoop 수치 0) — 헤드라인은 속도(20×) · 규모(10만)다.
- 🔴 조직명의 "PKU"가 북경대 소속을 뜻하는지, 저자 소속이 무엇인지는 볼트 미확인(HF API `organization` 필드는 조회하지 않았다 — [[복합지표-분해]]의 경고대로 그 필드만으로 소속을 단정하지 않는다).

## 관련 페이지
- [[G-STAR]] · [[PhysLoop]] · [[AI-영상-생성-2026]] · [[video-saas]]
