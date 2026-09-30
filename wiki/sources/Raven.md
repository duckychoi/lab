---
title: "Raven — '하네스의 하네스'가 데일리 1위인데, 초록에 숫자가 한 개도 없다"
type: source
domain: ai-news
tags: [ai-news, hf-paper, arxiv, agent, harness, multi-agent, 하네스-설계-축, 정량근거-부재, 이론적-충분조건]
created: 2026-09-30
updated: 2026-09-30
sources: []
reliability: low
---

# Raven: The Harness of Harnesses for Composable Agentic Intelligence

**HF 논문**: https://huggingface.co/papers/2609.33439 · **arXiv**: 2609.33439
**지표(2026-09-30)**: upvote **254**(수집기 09:04 관측 249 대비 **+5** · 볼트 09:13 실측) · **데일리 1위** · 공개 **2026-09-27**(수집기 일치)
**제목 검증**: arXiv 원문 제목 **완전 일치**

> [!insight] 🎯 핵심 인사이트 — 질문이 *"더 좋은 하네스"* 에서 *"하네스를 만드는 것"* 으로 한 칸 올라갔다
> 초록 원문: *"The central question thus shifts from **how to engineer a stronger harness for one domain** to **how to autonomously construct specialized harnesses, improve them through experience, and orchestrate them across domains**."*
> 📌 **[[하네스-설계-축]] 이 09-18에 열린 뒤 오늘 축 자체가 메타 층을 얻었다.** 그 축의 09-18 4층(SDK 구현 · 자동탐색 · 대조실험 · 학습루프 내재화)은 전부 **하네스를 설계하는 이야기**였다. 이건 **하네스 설계를 자동화하는 이야기**다. 09-19에 볼트가 [[NeoHorse-1-Paper]] 에서 *"하네스 매개 RSI"* 를 확인한 것의 **완성형 주장**에 해당한다.
> 구조(초록 실측): **Host Agent** 가 목표 분해 → 서브태스크를 전문 에이전트에 배정 → 실행 의존성 조정 → 결과 통합. 경험 보존은 **host archive + EverOS**, 그 경험을 재사용 가능한 절차로 노출하는 것이 **Skill Forge**. 단위는 *"each executable **model--harness pair** as a composable unit of intelligence"* — **모델이 아니라 모델·하네스 쌍이 단위**다.
> 🎯 **이 단위 정의가 이 논문의 가장 값나가는 부분이다.** 모델 성능을 모델만으로 말할 수 없다는 것을 **조합 단위 수준에서 형식화**했다. [[측정도구-먼저-반증]] 과 같은 방향이다 — 무엇을 재는지가 먼저다.

> [!warning] 🔴 초록에 정량 수치가 **0개** — 수집기 판정 독립 재확인
> 수집기: *"정량 수치 0개 — significantly outperforms SOTA 만 있고 벤치·수치·기준 모델이 초록에 없다."*
> ✅ **볼트가 arXiv 원문(42,106 바이트)을 직접 열어 재확인했다. 사실이다.** 초록 전문에서 성능 문장은 딱 하나다: *"On complex and long-horizon tasks, Raven **significantly outperforms the state-of-the-art agent systems**, pushing the frontier of composable agentic intelligence."*
> 🔴 **여기에 없는 것 전부**: 벤치마크 이름 · 비교 대상 시스템명 · 수치 · 태스크 수 · 성공률 · 비용. *"complex and long-horizon"* 은 태스크 규정이 아니라 형용사다.
> 🎯 **데일리 1위(upvote 254)가 정량 근거 0개로 달성됐다.** 오늘 논문 5건 중 **upvote 1위이면서 수치 0개**이고, **upvote 5위 [[Omni-IO-Skills]](57)가 수치 최다**다. **upvote와 검증가능성이 역상관**인 관측이 또 나왔다 — 이건 볼트가 [[벤치마크-이미지-봉인]] 계열에서 반복해 본 구조이며, 여기서는 봉인조차 아니다(**애초에 없다**).
> 📌 판정: **reliability low.** 오늘 논문 5건 중 유일한 low다.

> [!note] 확인 가능한 주장 — 이론 쪽은 오히려 명시적이다
> 초록: *"Our theory establishes **sufficient conditions** for such composition to expand reliable task coverage beyond that of the available individual agents **under a shared resource budget**."*
> ✅ **충분조건(sufficient conditions)** 이라고 정확히 썼고, **자원 예산 공유(shared resource budget)** 라는 제약도 붙였다. 필요조건이라고 과장하지 않았고 무한 자원을 가정하지도 않았다 → [[자기제한-명시]] 의 약한 사례.
> ✅ **오픈소스 선언**: *"an open-source multi-agent ecosystem"*. ⬜ **저장소 URL 미확인** — 초록에 링크가 없다(actionable 등록).
> 🎯 **즉 이 논문은 이론은 한정하고 실증은 한정하지 않았다.** 같은 초록 안에서 엄격함의 강도가 두 배로 갈린다.

## 도메인별 추출 (ai-news)

- **신뢰도**: 🔴 **낮음.** upvote 254(데일리 1위) · arXiv 게재 · 오픈소스 선언은 있으나 **정량 근거 0개**. upvote는 관심 지표이고 능력 지표가 아니다.
- **즉시 활용**: 🔴 **NO.** 저장소 URL 미확인 · 수치 미확인 · 구성요소 4종(Host Agent·EverOS·Skill Forge·host archive)의 인터페이스 미확인. **읽을 값은 있고 쓸 값은 아직 없다.**
- **6개월 영향력**: 개념 틀로서는 크다 — *"model--harness pair as composable unit"* 은 볼트가 모델 비교를 기록하는 방식 자체를 바꿀 수 있는 정의다. **구현 영향력은 본문·코드 확인 후 판정.**
- **대체 관계**: 볼트가 추적하는 [[AI-에이전트-프레임워크]] 계열을 **대체하지 않고 위에 얹는다** — 프레임워크를 생성 대상으로 취급한다.
- **허와 실**: 껍데기를 걷으면 **확인된 것 = 구조 설명과 이론 주장**, **미확인 = 전부 성능**. *"significantly outperforms"* 한 문장이 논문의 실증 전체다.
- **액션**: 본문 PDF 열람 → 벤치·수치·저장소 URL 확보(actionable 등록, 우선순위 높음 — 오늘 5건 중 공백이 가장 크다).

## 관련 페이지
- [[하네스-설계-축]] — 이 소스가 메타 층을 추가
- [[Omni-IO-Skills]] — 같은 배치 하네스 논문(수치 최다, upvote 최하 — 대조군)
- [[MaLiang-Harness]] — 같은 배치 하네스 논문(생성 검증 축)
- [[NeoHorse-1-Paper]] — "하네스 매개 RSI" 선행 형식화
- [[에이전트-스킬]] — Skill Forge 연결점
- [[벤치마크-이미지-봉인]] · [[측정도구-먼저-반증]] — 근거 부재 계열
- [[자기제한-명시]] — 충분조건·예산 제약 명시

## 원본
- 출처: https://huggingface.co/papers/2609.33439 · arXiv 2609.33439
- 신뢰도: ⭐ (upvote 254 데일리 1위이나 **정량 수치 0개** — 관심 높고 근거 없음)
- 검증: 2026-09-30 09:13 UTC arXiv 원문 직접 열람(42,106 바이트) — 제목·초록 전문 대조, 수치 0개 **독립 확인**
