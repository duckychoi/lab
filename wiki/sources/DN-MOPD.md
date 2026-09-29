---
title: "DN-MOPD — 누가 가르치느냐를 정해도, 얼마나 세게 가르치느냐를 안 정하면 합쳐지지 않는다"
type: source
domain: ai-news
tags: [ai-news, local-llm, hf-paper, 증류, on-policy-distillation, multi-teacher, qwen, 자기제한-명시, 대조군-설계]
created: 2026-09-29
updated: 2026-09-29
sources: []
reliability: high
---

# DN-MOPD — Beyond Teacher Assignment: Domain-Normalized Multi-Teacher On-Policy Distillation

> [!insight] 핵심 인사이트 — **라우팅은 "누가"만 정하고 "얼마나 세게"를 비워 둔다. 그 빈칸이 실패의 원인이었다**
> 초록 축자: *"This routing decides **which specialist teaches, but not how strongly its feedback moves the shared student**."*
> 🔴 **먼저 기존 방법의 실패를 보고한다**: *"we find that MOPD's student **does not beat one taught by the best single specialist** and gains little of the mathematics specialist's advantage."* — **여러 전문가를 합쳤는데 최고 단일 전문가보다 못하다.** 합성의 목적 자체가 무너진 상태에서 출발한다.
> 🎯 **원인을 분산으로 특정한다**: *"instruction-following feedback is **several times more spread out** than mathematics feedback and **dominates the student's updates**."* → 처방은 **도메인별 측정 분산으로 재척도**(rescale by measured spread).
> 📌 **이 논문의 형태가 [[측정도구-먼저-반증]] 과 같다** — 성능을 올리기 전에 **기존 방법이 왜 실패하는지를 먼저 계측**했고, 그 계측값(분산)이 그대로 처방이 됐다.

> [!insight] 🏆 **대조군이 자기 기여를 깎는다 — [[자기제한-명시]] 의 교과서 사례**
> 초록 축자 2건:
> ① *"Controls with fixed domain weights show that the gain comes mainly from **turning down instruction-following feedback rather than turning up mathematics alone**"* → **이득의 정체는 강화가 아니라 감쇠다.** 이름은 "정규화"지만 실제로 한 일은 **시끄러운 교사 입 막기**다.
> ② 🔴 *"and that **fixed weights close to those DN-MOPD measures perform comparably**."* → **측정해서 구한 가중치가, 그 근처 고정 가중치보다 낫지 않다.** 즉 **"측정한다"는 기여 부분은 성능으로 정당화되지 않는다** — 남는 이점은 튜닝 없이 자동으로 그 값에 도달한다는 것뿐이다.
> 📌 **저자가 자기 방법의 상한을 직접 적었다.** 볼트가 [[자기제한-명시]] 로 모아 온 사례군 중 **가장 깔끔하게 "우리 기여의 절반은 불필요할 수 있다"를 밝힌 축**이다.

> [!note] 실험 규모 — 일반화 근거가 초록 안에 있다
> - 백본: **Qwen3.5 계열 3개 크기**(*"In Qwen3.5 models at three sizes"*) → [[Qwen]] 패밀리
> - 검증 폭: **6개 공개 벤치 × 3 랜덤시드 × 2 답변길이 제한**, *"improves the average score over MOPD **at every size**"*
> - 🎯 **시드 3개와 길이제한 2종을 명시한 것이 드물다** — 단일 시드 보고가 관행인 영역에서 [[검사가능성-공사]] 쪽에 선다.

## 도메인별 추출 (ai-news / local-llm 교차)

- **신뢰도**: HF 데일리 **업보트 60**(볼트 09-29 09:08 실측 · 수집기 58 → **+2 드리프트**) · arXiv 2609.35347 · 게재 2026-09-28. **초록 전문 판독 성공, 손상 없음.** 🔴 **본문·코드·체크포인트 미확인** — 수치는 전부 저자 자기보고.
- **즉시 활용**: 🟡 **직접은 아니다.** 볼트는 증류 파이프라인을 운영하지 않는다. **다만 원리는 즉시 쓸 수 있다** — 여러 신호원을 하나로 합칠 때(예: 여러 평가자 점수 합산) **신호별 분산을 재지 않고 평균 내면 시끄러운 쪽이 결과를 지배한다.** [[요약자와-판정자-분리]] 와 같은 층의 이야기다.
- **6개월 영향력**: 멀티 티처 증류에서 **라우팅 연구 → 가중 연구로 축이 옮겨갈 근거**를 줬다. [[온폴리시-증류]] 계열에 *"어느 교사"* 다음 질문이 생겼다.
- **대체 관계**: MOPD 를 대체하는 것이 아니라 **한 줄 덧붙이는** 형태(라우팅 유지, 스케일만 추가). 채택 장벽이 낮다.
- **허와 실**: 🔴 **마케팅을 걷어낼 필요가 거의 없다** — 저자가 먼저 걷어냈다(고정 가중치 대조군). **실제 능력은 "MOPD 평균을 전 조건에서 넘음"이고, "고정 가중치보다 낫다"는 주장하지 않는다.**

> [!action] 당장 할 것
> 볼트 자체 적용 후보: **수집기 배달 항목 점수화 시 지표별 분산 정규화**(★ 증분 · 업보트 · 다운로드는 분산 규모가 서로 수십 배 다르다 — 지금은 사실상 ★ 증분이 지배한다). 우선순위 낮음, 원리 차용만.

## 관련 페이지
- [[온폴리시-증류]] · [[자기제한-명시]] · [[측정도구-먼저-반증]] · [[검사가능성-공사]] · [[요약자와-판정자-분리]]
- [[Qwen]] · [[분포내-우위]] · [[비매칭-비교]]
- 같은 배치: [[TraceDance]] · [[Post-Training-Behavioral-Shadows]] · [[YuE2]] · [[HexaAnything]]

## 원본
- 출처: https://huggingface.co/papers/2609.35347 · arXiv **2609.35347**
- 실측(2026-09-29 09:08 UTC · HF papers API): 제목·업보트 **60**·게재일 **2026-09-28** 확인 · **초록 전문 정상 수신**(손상 0)
- 수집기 대조: 업보트 58→60(**+2**) · 인용 내용 **전부 일치**, 🎯 **수집기가 누락한 것 2건** — ① 백본이 **Qwen3.5 3개 크기**라는 사실 ② **고정 가중치 대조군이 동등 성능**이라는 자기제한
- 확인 범위: 초록 전문. 🔴 본문·부록·코드 미열람 · 🔴 미실행
- 신뢰도: ⭐⭐⭐⭐ **high** — API 실검증 + 초록 무손상 + 저자 자기제한 명시. (제3자 재현 부재로 최상위는 아님)
