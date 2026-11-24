---
title: "NoPeWorld — 인터랙티브 영상 월드모델의 물체 관통 방지: 동결 DiT 은닉 상태로 위험 행동 교체 (arXiv 2611.27963)"
type: source
domain: video-saas
tags: [video-saas, paper, world-model, navigation, safety, frozen-backbone, probe-head]
created: 2026-11-24
updated: 2026-11-24
sources: [https://huggingface.co/papers/2611.27963]
reliability: medium
---

**논문**: arXiv 2611.27963 · 업보트 **56**(볼트 API 11-24 · 수집기 11-23 39) · 11-23 데일리 2위 · 소속 The Hong Kong Polytechnic University(PolyUHK) · 코드 https://github.com/yuhangdai427/NoPeWorld (★3) · 벤치 · 가중치 공개 명시

## 핵심 인사이트
> [!insight] 재학습 없이, 은닉 상태 하나만 읽어 위험한 행동을 갈아끼운다
> 키 입력으로 걷는 영상 월드모델이 벽 · 장애물을 뚫는 문제. NoPeBench(Unreal Engine 정답 경로 기준)로 오픈 모델 6종을 평가하니 **어느 것도 관통을 막지 못한다**. 그런데 **동결 DiT 의 은닉 상태만으로 "이 행동이 관통할지"를 예측할 수 있음**을 발견 → 작은 예측 헤드를 얹어 위험 행동을 원래 의도에 가장 가까운 안전 행동으로 교체. 초록 수치: 6개 모델 평균 물리 위반율 **74% → 16%**. 오픈 도메인 이미지 · 3인칭 · 움직이는 장애물로 제로샷 일반화 주장. [[동결-교정층]] (신설)의 대표 표본.

> [!warning] 원래 위반율이 낮은 모델에서는 오히려 하락
> **본문 표 4의 불리한 행**: ① WorldPlay2 — Raw 54.6 · 텍스트 프롬프트 60.5 인데 NoPeWorld 52.1(Coll) · 50.7(Pred)로 **오히려 하락**(원래 위반율 11%로 낮은 모델) ② Hy-Nomas 는 적용 후에도 영상 위반 40–45%(Raw 95%) ③ HY-WorldPlay 에서 외부 깊이 베이스라인이 위반 0%로 NoPeWorld(15–21%)보다 낮다(대신 SIS 진행도는 NoPeWorld 우세). LingBot-World 2.0 경로당 추가 비용은 표 5 별도(원본 53.7s/경로).

## 도메인별 추출 (video-saas)
- **신뢰도**: ⭐⭐⭐ — 코드 · 벤치 · 가중치 공개 명시 · 6모델 전수 평가. ★3 미성숙 레포.
- **즉시 활용**: NO — 월드모델 · 게임 생성 연구용. 일반 영상 생성(SaaS 생성 파이프라인)에는 직접 해당 없음.
- **6개월 영향력**: 인터랙티브 월드모델(게임형)이 상품화되면 "관통 검사"는 필수 QA 항목이 된다. 동결 본체 + 검사 헤드 구조는 [[월드모델]] 품질 보증의 표준 후보.
- **액션**: 없음(관찰).

## 관련 페이지
- [[월드모델]] · [[Diffusion-월드모델]] · [[동결-교정층]] · [[video-saas]]

## 원본
- 출처: https://huggingface.co/papers/2611.27963
- 확인 범위: HF papers API(업보트 · 조직 · githubRepo — 볼트 11-24) · 본문 표 4 수치는 수집기 11-23 판독(볼트 HTML 검증 미실시 — 표본 검증은 cmHC · Clover 로 대체) · 실행 0
- 신뢰도: ⭐⭐⭐
