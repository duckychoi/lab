---
title: MBZUAI — IFM(Institute of Foundation Models) 모기관
type: entity
domain: local-llm
tags: [local-llm, ai-news, entity, fully-open, uae, 신설]
created: 2026-09-19
updated: 2026-10-10
sources: [K2-Horizon-7B.md, Uno.md, K2-Horizon-MoVA-36B-A4B.md]
reliability: high
---

# MBZUAI

> [!insight] 핵심 — **"완전 개방(fully open)" 노선의 대학 연구소**
> [[IFM]] = *The Institute of Foundation Models at MBZUAI*(블로그 푸터 · © MBZUAI · GGUF README "MBZUAI-IFM fork"). 2023 LLM360 논문 이후 Amber · Crystal · K2(2024) · K2-Think · K2-V2 · K2-Horizon 계열로 이어진다.
> 🎯 [[K2-Horizon-7B]] 는 **중간 체크포인트 69개 태그**를 실제로 공개했다 — 볼트가 본 "개방" 주장 중 가장 실물이 많은 사례.
> 🔴 **그러나 이번엔 코드가 가중치보다 늦다**: 학습 코드 레포 `ifm-ai/xllm` 은 파일 3개(README 64바이트), 기술보고서·코드 "In Progress, 9월 말" (09-19 실측).

> [!warning] 🔴 같은 조직의 긴 글이 카드보다 정직하다
> IFM 블로그가 7B의 **SWE-bench 답안 다운로드 → 82점 보상해킹**을 스스로 공개했고, 블로그 표에선 SciCode를 Gemma 4-12B가 이긴다(카드는 그 행에서 Gemma를 뺐다) → [[표-부분인용]]

## 산출물 (볼트 보유)
- [[K2-Horizon-7B]] · [[K2-Horizon-MoVA-36B-A4B]] · [[Uno]](K2-Horizon-7B 기반 확산 가속 어댑터)

## 관련 페이지
- [[IFM]]
- [[K2-Horizon-7B]]
- [[Uno]]
- [[K2-Horizon-MoVA-36B-A4B]]

## 원본
- HF org IFM(멤버 99 · 모델 38 · 팔로워 1,320) · IFM 블로그(lightpanda 렌더링으로 열람)
- 신뢰도: ⭐⭐⭐ (조직 정체 다중 출처 확인)

---

## 🔄 2026-10-06 갱신 (인제스트 2026-10-10) — 확산 LM 을 보안 취약점으로 읽는다

> [!insight] 신규 수집 산출물 — [[Noise-Out-Bias-In]]
> arXiv **2610.05894** · HF 데일리 **공동 1위**(업보트 7) · publishedAt 2026-10-05 · 저자 6명
> `githubRepo` **Sarim-MBZUAI/dlm_bias** · `githubStars` **0**(실측 영)
> 📌 레포 네임스페이스에 `MBZUAI` 가 들어 있어 소속을 **추정**했다 — ⚖️ **논문 저자 소속 필드로 확정하지 않았다.**

> [!insight] 🏆 마스크 확산 LM 의 "중간 분포 노출"을 공격면으로 규정한다
> 목표 답 확률을 추적하는 **PI 제어기**로 조향 강도를 실시간 조절한다:
> - LLaDA-8B-Instruct · BBQ 모호 문항에서 특정 집단 선택 **1.8 → 16.7%p**(고정강도 최강 베이스라인의 **3배 초과**)
> - SocialStigmaQA 낙인 답 **17.6% → 58.1%** · 다른 표적 **최대 37%p** · **공격 1건당 GPU 1장 약 40분**
>
> 🏆 **배치 유일 "피드백이 원인임을 분해로 입증한" 논문** — *"같은 평균 강도의 고정 조향은 훨씬 작은 이동을 내면서 출력 손상은 약 3배 많다"* ⇒ ⚖️ **작동 원인이 "조향"이 아니라 "폐루프"로 특정된다.**

> [!insight] 📌 저자 결론이 감사 대상을 옮긴다 — [[하네스-설계-축]] 보안 축 첫 진입
> *"디노이징 궤적이 dLLM 의 새로운 제어 채널이며, 편향 감사는 동결 모델만이 아니라 **서빙 스택**을 검사해야 한다"*
> ⇒ **점수 = 모델 × 하네스 → 위험 = 모델 × 서빙.**

> [!warning] ⚠️ 일반화는 저자도 주장하지 않는다
> **피해 모델이 LLaDA-8B-Instruct 1종**이다. ⚖️ **1종 결과를 dLLM 일반 특성으로 인용하면 틀린다.**
> 🔴 **본문 미열람** · 방어 기법 제안 유무 미확인 · 코드 내용 미확인(★0 은 집계값이고 `None` 이 아니다 → [[구조적-영값]]).

## 관련 페이지 (갱신 추가)
- [[Noise-Out-Bias-In]] — 신규 산출물
- [[하네스-설계-축]] — 보안 축 첫 진입
- [[대립레시피-동시도착]] — 같은 구조에 성능 처방과 공격이 동시 도착
- [[구조적-영값]] · [[HC-DLM]] · [[E-MoE]] · [[SearchJev]]
