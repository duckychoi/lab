---
title: "EDGAR — 가우시안 헤드 아바타의 흐림·늘어짐·떨림을 1-step 디퓨전으로 고친 뒤 아바타에 다시 굽는다. 추론 시 디퓨전 0회"
type: source
domain: slam-3dgs
tags: [slam-3dgs, 3dgs, gaussian-avatar, hf-paper, one-step-diffusion, mixture-of-experts, kaist, refinement]
created: 2026-11-09
updated: 2026-11-09
sources: [https://huggingface.co/papers/2611.07909]
reliability: medium
---

**논문**: [2611.07909](https://huggingface.co/papers/2611.07909) · KAIST · 업보트 16(볼트 11-09 · 수집기 14) · 코드 [kwanyun/edgar-code](https://github.com/kwanyun/edgar-code) ★23 · 프로젝트 https://kwanyun.github.io/edgar/

## 핵심 인사이트
> [!insight] 후처리 디퓨전을 "매 프레임 필터"가 아니라 "한 번 쓰고 굽는 교사"로
> 실패 사례를 시뮬레이션한 트리플렛 데이터 **EDGAR-SET**(열화 렌더·정답·참조) → Sapiens 정체성 특징 주입 **1-step 디퓨전 + 열화 유형/강도별 MoE** → 보정된 다시점 렌더를 의사 타깃으로 **원래 [[3DGS]] 아바타를 재최적화**. 최종 렌더는 실시간 3DGS 그대로.

> [!warning] 정량 수치 없음(초록) — 3 복원법 × 3 설정에서 원본·SDEdit 류 대비 개선이라는 서술뿐. 초록 스스로 *"recoverable appearance artifacts"* 의 **유용한 작동 영역**이라고 한정한다([[한정어-탈락]] 주의 — 기하 붕괴는 범위 밖일 수 있음).

## 도메인별 추출 (slam-3dgs)
- **실시간 가능성**: YES(재최적화 후 일반 가우시안 렌더) — 보정 비용은 오프라인 1회
- **카메라 파이프라인**: 단안 영상/이미지 기반 헤드 아바타 출력이 입력
- **응용 가능성**: 단안 아바타 품질 보정 → 영상 SaaS 의 디지털 휴먼·립싱크 소스 품질 개선
- **필수 레퍼런스**: 중간 — 코드 공개

## 관련 페이지
- [[3DGS]] · [[idol]](11-08 단일 이미지→3DGS) · [[한정어-탈락]]

## 원본
- 출처: https://huggingface.co/papers/2611.07909
- 확인 범위: HF papers API 초록(볼트 재조회)
- 신뢰도: ⭐⭐
