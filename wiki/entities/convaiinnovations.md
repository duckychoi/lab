---
title: "convaiinnovations — System-1 결정 모델 제공자"
type: entity
domain: ai-news
tags: [entity, organization, huggingface, decision-model, calibration, local-llm]
created: 2026-10-10
updated: 2026-10-10
sources: [laya.md]
reliability: medium
---

# convaiinnovations

**HuggingFace**: https://huggingface.co/convaiinnovations

> [!insight] 핵심
> [[laya]] 의 제공 조직. **생성하지 않는 비자기회귀 System-1 결정 모델**을 만든다 — 텍스트 생성 대신 **캘리브레이션된 확률이 붙은 타입 answer** 를 단일 순방향 패스로 반환한다.
> 🎯 **볼트 수집 조직 중 "생성형이 아닌 것을 의도적으로 만드는" 첫 사례다.** 기존 수집은 생성 모델 제공자(Qwen·Lightricks)와 양자화 조직(ISTA-DASLab·prism-ml)에 쏠려 있었다.

> [!insight] 🏆 자기 실패 수치를 카드에 적는 조직이다
> [[laya]] 카드가 **크메르어 정확도 0.000 · 확신도 0.952** 를 적고 *"확신도 게이팅으로는 구제할 수 없다"* 고 명시한다.
> ⇒ 📌 **금일(2026-10-10) 배치에서 자기 실패 수치를 적은 유일한 소스**이고, 볼트 [[측정도구-먼저-반증]] · [[캘리브레이션-붕괴]] 의 최강 사례다.
> 🏆 **외부 독립 측정 출처를 링크로 명시**한다(경쟁 모델 TypeSafe Jev 의 p50 지연 236~276ms 를 자기 측정이 아니라 **외부 2곳 인용**으로 적는다) ⇒ 이 조직은 **비교 수치의 출처를 분리하는 규율**을 가지고 있다.

> [!note] 확인된 것
> - [[laya]]: created **2026-09-18** · lastModified 2026-10-03 · **Apache-2.0** · `safetensors` **421,293,830** 파라미터
> - 다운로드 **41,468**(30일 = 전체누적 동일 · 생성 22일차) · likes **5,441** · HF trending **11위**
> - 체크포인트 3종 운영: 영어 ModernBERT-large · 다국어 mmBERT-base 322M · typed-decisions ModernBERT-large 421M
> - 배포가 **`pip install laya`** 이고 GPU·API키·계정이 **전부 불필요**하다 ⇒ 🎯 **볼트 금일 ★최우선 actionable**
> - 학습법 **RLCD**(엄격 적정 채점규칙에 대한 강화학습)를 자칭 — **정의·구현 미확인**

> [!warning] 🔴 미확인
> 조직 실체(기업/연구소/개인 여부) · 구성원 · 자금 출처 · **다른 저장소 보유 여부 전부 미조회.** HF org 페이지 **미열람.**
> 🔴 이름이 *"Conv AI Innovations"* 로 읽히나 **회사 실존·소속 국가 미확인** — 지어내지 않는다.
> 🔴 **RLCD 가 자체 명명인지 기존 기법인지 미확정.**

## 관련 페이지
- [[laya]] — 주 산출물
- [[캘리브레이션-붕괴]] — 신설 계기를 제공
- [[측정도구-먼저-반증]] · [[유의성-자기제한]]
- [[SearchJev]] — 같은 범주의 논문 쪽(EvoScientist)
- [[local-llm]] · [[ai-news]]

## 원본
- 대표 산출물: [[laya]] (HF 다운로드 41,468 · likes 5,441 · trending 11위)
- 신뢰도: ⭐⭐⭐ (산출물 메타는 실측 · **조직 실체 미확인**)
