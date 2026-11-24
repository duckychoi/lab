---
title: "cmHC — Hyper-Connection 잔차 스트림 혼합을 기하적 수축으로 균형 (arXiv 2611.27193 · 새 파라미터 0)"
type: source
domain: ai-news
tags: [ai-news, paper, architecture, hyper-connections, residual-stream, birkhoff-polytope, moe]
created: 2026-11-24
updated: 2026-11-24
sources: [https://huggingface.co/papers/2611.27193]
reliability: medium
---

**논문**: arXiv 2611.27193 · 업보트 **94**(볼트 API 11-24 · 수집기 11-23 54) · 11-23 데일리 1위 · 소속 XingChen-AGI · 코드 https://github.com/Newiz430/cmHC (★0)

## 핵심 인사이트
> [!insight] 믹싱 행렬의 "중간 지대"가 문제다 — 꼭짓점은 under-mixing, 중심은 over-mixing
> mHC(잔차 혼합 행렬을 이중확률 행렬 집합 Birkhoff 다면체에 제약)의 트레이드오프를 이론적으로 경계 짓고: 행렬이 꼭짓점 근처면 스트림들이 사실상 독립(under-mixing), 중심 근처면 스트림 구분이 사라진다(over-mixing). 해법 cmHC = 다면체를 **내부로 수축**시키는 정확한 이중확률 방법 — **새 파라미터 없음**, 얕은 층에만 완만한 수축(K층)을 걸어 over-mixing 을 막는다.

> [!warning] 이기는 것은 "평균 순위"다 — 개별 표에서 지는 행이 있다
> **본문 표 1(nanoGPT, 3회 평균, val loss)**: OpenWebText 에서 cmHC(λ=0.97, K=2) 평균 순위 1.3위 — S 3.4686 vs mHC 3.4775, L 은 K=10 3.1893 vs mHC 3.1920(**차이 0.003–0.01 수준**). 🔴 **불리한 쪽**: FineWeb-Edu S 에선 mHC-lite 3.4660 < cmHC 3.4672, L val 은 KromHC 3.1802 가 최저(cmHC K=2 3.1817) — 평균 순위만 1위(2.8). λ=0.70 전층 수축은 순위 9.0–9.3 으로 악화(수축 강도 민감). 볼트 11-24 본문 HTML 문자열 검증 통과(3.4686 · 3.4775 · 3.4660 · 3.1802 전부 적중).

## 도메인별 추출 (ai-news)
- **규모 실체**: 대규모 실험은 6B-MoE(71.5k step · 149.95B 토큰, mHC 대비 loss −0.002)와 **300B-MoE 는 2k step(33.55B 토큰)만 학습**해 loss 격차 0.0157 — **장기 학습 결과가 아니다**.
- **커널**: Ascend 910C 융합 연산자 지연 감소 44.8%(hidden 2048) → 31.0%(3584) → **24.1%(7168, 차원이 클수록 이득 축소)**. NVIDIA GPU 커널 언급 없음 — 하드웨어 편향 명시.
- **계열 맥락**: [[SimpleHC]](믹싱 제거 단순화, 11-14) · [[xHC]](잔차 연결 일반화, 07-20)에 이어 HC 계열 3번째. 계열의 축: 믹싱을 *제거*(SimpleHC) / *일반화*(xHC) / *제약으로 균형*(cmHC).
- **즉시 활용**: NO — 사전학습 아키텍처 선택 문제. 코드 ★0 — 재현 기대치 낮음.
- **액션**: 없음(관찰).

## 관련 페이지
- [[SimpleHC]] · [[xHC]] · [[ai-news]]

## 원본
- 출처: https://huggingface.co/papers/2611.27193
- 확인 범위: HF papers API(업보트 · 조직 · githubRepo — 볼트 11-24) · 🔴 **본문 HTML 직접 판독** — 표 1 · 3 · 4 · 5 수치 6개 문자열 검출 통과(수집기 11-23 표 판독과 일치) · 코드 레포 미열람 · 실행 0
- 신뢰도: ⭐⭐⭐
