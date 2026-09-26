---
title: "AEWM — 판별기 이득 +10.6이 실제 과제에서 +3.2~6.7로 줄어드는 과정을 논문이 스스로 보여준다"
type: source
domain: ai-news
tags: [ai-news, local-llm, world-model, llm-agent, state-revision, rejection-sampling, 요약자와-판정자-분리, 수확체감-변곡점]
created: 2026-09-26
updated: 2026-09-26
sources: []
reliability: high
---

# Agent-Editing World Model (AEWM)

> [!insight] 핵심 인사이트 — **세계모델이 환경이 아니라 과제 상태를 모델링한다**
> 문제 제기가 날카롭다: 기존 언어 세계모델은 **툴 응답을 재구성**하는데, *"reconstructing **high-entropy, execution-dependent** tool responses offers **limited value when real feedback is available**."*
> 🎯 **실제 실행이 가능한데 왜 응답을 흉내내는가** — 툴을 진짜 돌릴 수 있는 에이전트 환경에서 관측 예측은 낭비다. AEWM은 대신 **추론·행동이 과제 진행을 어떻게 바꾸는지**를 모델링한다.
> 두 번째 문제: **task-state contamination** — *"unsupported assumptions and outdated plans persist in history and distort subsequent decisions."* 📌 **낡은 계획이 히스토리에 남아 이후 결정을 오염시킨다**는 지적은 [[에이전트-메모리-레이어]] 의 *"압축이 아니라 이중화"* 논의와 정반대 방향이다 — 저쪽은 **보존**을 처방하고 이쪽은 **편집**을 처방한다. 🎯 **같은 축의 반대 극이 한 주 안에 나왔다.**

> [!insight] 🎯 비평이 아니라 상태를 바꾼다
> 구성: **Action Judge**(결정을 **Critical / Exploratory / Noisy** 3분류) + **State Revision**(같은 관측 이력에서 잡음 연속을 편집) → **EditAct** 로 실제 실행과 결합.
> 결정적 문장: *"**directly changing the state underlying subsequent decisions rather than merely providing critiques.**"*
> 📌 볼트가 09-17·09-24에 쌓은 *"다른 에이전트를 감독하는 층"*([[Octop]] 권한 게이트 · [[oh-my-hermes]] 증거 게이트 · [[security-audit-skill]] 스키마 게이트)은 전부 **막거나 표시하는** 게이트였다. AEWM은 **고쳐 쓴다** — 감독 계층의 새 양식이다.
> 🎯 그리고 3분류가 [[검사가능성-공사]] 와 같은 형식이다 — [[Cloudflare]] 의 `needs_validation`, [[oh-my-hermes]] 의 `reported done` 처럼 **중간 상태에 이름을 준다**(`Exploratory` = 결정적이지도 잡음도 아닌 칸). **세 번째 생태계의 3값화.**

> [!insight] 🔴 감쇠를 논문이 수치로 드러낸다 — 오늘 5건 중 유일
> - Action Judge 벤치: **macro-F1 70.5%**, 최강 프런티어 베이스라인 대비 **+10.6점**
> - 6개 벤치 × 3개 백본에서 EditAct: 평균 **+3.2 ~ +6.7점**
> - AEWM-RFT(검증 궤적 rejection sampling FT): Self-RFT 대비 **+2.2 ~ +2.6점**(온라인 안내 없이)
>
> 🎯 **+10.6 → +3.2~6.7 → +2.2~2.6 의 3단 감쇠가 한 초록 안에 있다.** 판별기에서 얻은 이득의 **약 30~63%만 과제 성능으로 흐르고**, 오프라인 증류로는 다시 그 절반쯤이 남는다.
> 📌 **이걸 숨기지 않은 것이 이 논문의 신뢰도다.** 보통은 +10.6만 헤드라인에 쓴다. [[수확체감-변곡점]] 에 **"중간 지표 → 최종 지표 전달률"** 축을 추가할 사례이고, 볼트가 09-17에 [[DeepSeek-R1]] 에서 배운 *"부분인용은 인용 범위 안에서 사실이다"* 의 **저자 측 예방 조치**다.
> 학습 영역: Search · Terminal · **Software Engineering** 3영역 mid-training + SFT.

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐⭐⭐⭐ — 초록 수치 밀도가 **오늘 5건 중 최고**(6개 수치 토큰, 전건 볼트 대조 일치). 부속 GitHub `RUCAIBox/Agent-Editing-World-Model` ★**4** 실재(🔴 수집기 미기재 — 09-24 요청 3 재위반 3/3). RUCAIBox는 중국인민대 AI Box 연구실 계열로 보이나 ⬜ **초록·API로 소속 미확정**.
- **즉시 활용**: **NO(현시점)** — 학습(mid-training + SFT)이 필요하고 가중치 공개 여부가 초록에 없다. ★4 레포는 코드 공개 초기 단계로 보인다. 🎯 **단 Action Judge 3분류는 프롬프트 수준으로 즉시 모방 가능**하다 — 에이전트 턴마다 직전 결정을 Critical/Exploratory/Noisy로 라벨링시키는 것만으로도 효과 일부를 볼 여지.
- **6개월 영향력**: 높음 — *"세계모델 = 환경 시뮬레이터"* 라는 정의를 *"세계모델 = 과제 상태 편집기"* 로 밀어내는 재정의다. 09-17 관측(*"논문 5건 중 4건이 먼저 이름을 붙인다"*)의 또 한 사례이며, 여기서는 **이름이 아니라 정의를 바꾼다.**
- **대체 관계**: [[oh-my-hermes]] 증거 게이트·[[Octop]] 권한 게이트를 **대체하지 않고 다음 단계로 잇는다**(표시 → 차단 → **수정**).
- **허와 실**: 🔴 걷어낼 것은 **+10.6** 이다. 그건 **자기 벤치(Action Judge)** 값이고 실제 과제 이득은 **+3.2~6.7**이다. 🎯 다만 **저자가 둘 다 적었으므로 이건 과장이 아니라 투명성**이다 — 걷어내는 일을 독자가 아니라 저자가 미리 했다.
- **액션**: ⬜ `RUCAIBox/Agent-Editing-World-Model` 레포 열람(가중치·데이터 공개 범위 확인) · ⬜ Action Judge 3분류를 [[hermes-agent]] 턴 로깅에 프롬프트로 시험 적용.

> [!question] 미해결 질문
> State Revision 이 **틀린 편집**을 했을 때 복구 경로가 있는가? 히스토리를 직접 고치는 설계는 **오편집이 누적되면 되돌릴 근거 자체가 사라진다** — 초록은 이 실패 모드를 언급하지 않는다.

## 관련 페이지
- [[월드모델]] · [[에이전트-메모리-레이어]] · [[검사가능성-공사]] · [[수확체감-변곡점]]
- [[oh-my-hermes]] · [[Octop]] · [[security-audit-skill]] · [[요약자와-판정자-분리]] · [[표-부분인용]]

## 원본
- 출처: https://huggingface.co/papers/2609.28416 (arXiv 2609.28416)
- 실측(2026-09-26 HF API): upvote **13**(수집기와 **완전일치**) · `publishedAt` **2026-09-23** · 저자 **9명** · githubRepo `RUCAIBox/Agent-Editing-World-Model` ★**4**
- 수집기 대조: 초록 수치 **6/6 축자 일치**(70.5 · +10.6 · +3.2–6.7 · +2.2–2.6) · 3분류 명칭 일치 · 🔴 **부속 GitHub 미기재**
- 확인 범위: **초록 전문.** 🔴 본문·부속 레포 미열람 · 🔴 RUCAIBox 소속 미확정
- 신뢰도: ⭐⭐⭐⭐ **high** — 수치 밀도 최고 · **자기 이득의 감쇠를 스스로 공개**
