---
title: OpenGCUA — 컴퓨터 사용 에이전트 오픈스택 (코드 실행을 1급 수단으로)
type: source
domain: ai-news
tags: [ai-news, computer-use, agent, osworld, open-stack, code-execution, harness, 벤치마크외부축]
created: 2026-10-17
updated: 2026-10-17
sources: []
reliability: high
---

# OpenGCUA: Toward a Fully Open Stack for Generalist Computer Use

**arXiv**: 2610.22200 · **HF**: https://huggingface.co/papers/2610.22200
**upvote**: **315** (HF 데일리페이퍼 10-16 목록 3위 · 수집기 수치와 일치)
**저자**: 15인 · published 2026-10-15
**코드**: https://github.com/Tongyi-MAI/OpenGCUA · **프로젝트**: https://tongyi-mai.github.io/OpenGCUA/
**신뢰도**: ⭐⭐⭐

> [!insight] 핵심 인사이트 — **GUI 를 벗어난 것이 아니라, 하네스가 쥐던 판단을 모델에 넘겼다**
> 저자 정의: GCUA = *"a system in which **the model chooses how to observe, act, and organize its work** across visual and programmatic interfaces"*.
> 두 축이 분리돼 있다:
> 1. **코드 실행을 1급 수단으로** — *"it lets intermediate results determine subsequent operations"* ⇒ 중간 결과가 다음 조작을 결정한다(GUI 클릭 시퀀스는 이걸 못 한다).
> 2. 🏆 **harness-to-model decision transfer** — *"moving selected observations and task-state decisions **from fixed harness rules to the model**"*.
> ⇒ 🎯 **에이전트 성능 개선이 모델 교체가 아니라 "하네스가 뭘 결정하고 있었나"의 재배분에서 나온다**는 주장이다. 이것이 이 논문의 이전 가능한 부분이다.

## 측정 (초록 전문 교차검증 완료)

- **OSWorld-v2**: 전체 구성이 **평가 8개 모델 전부에서 태스크 점수 상승**(GPT-6 Astra · Claude Opus 5 포함)
- **평균 partial score +19.6점**
- **태스크당 스텝 평균 −53.0%** (GUI-only 배치 실행 대비)
- 공개물: 구현·프롬프트 · **8개 모델 전원의 평가 트래젝터리** · 실기기 하네스 예비판 · 크로스디바이스 SDK

> [!warning] 🔴 저자가 벤치마크 밖의 축을 직접 적었다 — 실기기 효율 19.4배 격차
> *"Across four real macOS tasks under our real-device harness, selected **Qwen3.8-Max** runs use **19.4 times** as many reported reasoning tokens as **GPT-6 Astra**, highlighting substantial differences between models in real-device execution efficiency."*
> ⇒ 🏆 **OSWorld-v2 점수는 8/8 올랐다고 적은 바로 그 논문이, 실기기에서는 모델 간 19.4배 토큰 격차가 있다고 적었다.**
> ⇒ ⚖️ **같은 점수를 내는 두 모델의 비용이 19.4배 다르면 벤치마크 점수는 선택 근거가 못 된다.** 저자 서술: *"The harness addresses real-device challenges **not fully captured by benchmarks**."*
> 🔴 단 n=4 태스크 · *"selected runs"* 이고 전수 측정이 아니다 — 방향은 믿을 만하고 배수는 아니다.

## 도메인별 추출 (ai-news 템플릿)

- **신뢰도**: ⭐⭐⭐ — upvote 315 · 저자 15인 · **githubRepo + projectPage 둘 다 실존**(규약 ⑩ 통과) · 트래젝터리 공개 = 재현 경로 있음
- **즉시 활용**: **부분 YES** — "코드 실행을 1급 수단으로" 와 "하네스 결정을 모델로 이전"은 **내 에이전트 설계에 코드 변경 없이 적용 가능한 설계 원칙**이다. 🔴 스택 자체는 컴퓨터 사용(데스크톱 조작) 전용이라 볼트 워크플로우와 직접 겹치지 않는다.
- **6개월 영향력**: *"frontier implementations, such as GPT-6 Astra's computer-use system, remain largely **closed**"* ⇒ 폐쇄 스택의 설계를 체계적으로 연구할 수 없던 상태를 깨려는 시도. 성공 여부는 **트래젝터리 공개가 재현으로 이어지는지**에 달렸다.
- **대체 관계**: GUI-only 에이전트 하네스(고정 규칙형)를 대체. 스텝 −53.0% 는 **같은 일을 절반의 조작으로** 한다는 뜻이다.
- **허와 실**: 🔴 **절대 점수표가 초록에 없다** — *"+19.6 points"* 는 증분이고 기준 점수가 없다. ⚖️ 단 트래젝터리를 공개했으므로 **"미공시"가 아니라 "초록에 없음"** 이다 → 레포/프로젝트 페이지에 표가 있을 수 있다(미확인, 아래 question).
- **액션**: `Tongyi-MAI/OpenGCUA` 의 `contents/` 1회 조회로 절대 점수표 존재 여부 확정(규약 ⑨) · 우선순위 중간.

> [!question] 미해결
> ① 절대 점수표 미확인 — 레포·프로젝트 페이지 **미열람**(규약 ⑨/⑫ 미적용, 금일 이월).
> ② **19.4배가 어느 방향으로 유리한지 불명** — 토큰을 더 쓴 Qwen3.8-Max 가 그 태스크를 더 잘 풀었는지 초록에 없다. 비용만 비교하면 결론이 뒤집힐 수 있다.

## 관련 페이지
- [[하네스-설계-경험칙]]
- [[벤치마크-외부축]]
- [[복합지표-분해]]
- [[AI-에이전트-프레임워크]]
- [[FDE-Gym]] ← 같은 10-16 목록 · **"벤치마크가 잡지 못하는 축"을 저자가 직접 분해**한 동형 사례
- [[MJev-Spatial]]

## 원본
- 출처: https://huggingface.co/papers/2610.22200 (arXiv 2610.22200)
- 열어 본 것: HF papers API(초록 전문 · upvote · githubRepo · projectPage). 🔴 arXiv API 는 금일 3건 전부 **빈 응답**이라 HF API 로 대체(메타규약 적용 — 같은 자원의 다른 표현 1회).
- 관측: 2026-10-17T09:12Z (18:12 KST)
- 신뢰도: ⭐⭐⭐
