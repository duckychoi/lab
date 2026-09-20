---
title: "Feyospace-v1 — 초록은 '우회'라 쓰고 목차는 'Jailbreak Tech'라 쓴다"
type: source
domain: ai-news
tags: [ai-news, hf-paper, cyber-security, post-training, agentic, backlog, 한정어-탈락, 목차-노출]
created: 2026-09-20
updated: 2026-09-20
sources: []
reliability: medium
---

# Feyospace-v1: How the Cyber Mercury Seven Trained Frontier Cyber Models

> [!insight] 핵심 인사이트 — 병목을 **모델 규모가 아니라 데이터 생산 설비**로 재정의한다
> 초록 원문: *"Training capable cyber agents is often treated primarily as a problem of **model scale**, yet open-weight post-training is constrained more directly by the cost of **executable environments**, reliable **multi-turn supervision**, and **access to strong teachers**."*
> 5개 시스템(Choulea · SkyReal · Hongzwang · PSBreakup · Kreator)으로 데이터 엔진을 구성하고, 리셋 가능한 코딩·취약점·CTF·커널이력·풀익스플로잇·펌웨어·실기기 환경을 만든다. **실행 검증 + 증거 감사**를 통과한 궤적만 남겨 **164,269개**로 롱컨텍스트 SFT.
> 성과: 체크포인트 3종이 시작 모델 대비 CyberGym 전체 평균 **+23.76%**, 풀드 CTF **+10.49%**. Feyospace-s1 은 2026-09-01 기준 검증 성공률 **63.24%**, CyberGym 공식 리더보드 **10위**, 3종 전부 **동급 파라미터대 1위**.
> 🎯 **주장의 형태가 능력이 아니라 조직이다**: *"the **first end-to-end demonstration that a seven-person independent team** can train open-weight models with leading agentic cyber capability."*

> [!warning] 🔴 볼트 발견 — **목차 한 줄 아래에서 단어가 바뀐다**
> 볼트가 `arxiv.org/html/2609.08418` 본문을 열었다(수집기 자인: *"논문 5건은 초록까지만 봤다"*). **목차의 절 제목이 초록의 동사와 다르다:**
>
> | 시스템 | 초록의 표현 | **본문 절 제목** |
> |---|---|---|
> | Choulea | *"analyzes hidden reasoning signatures"* | **2.1 Choulea: Signature Hack** |
> | SkyReal | *"reduces teacher-sampling cost"* | **2.2 SkyReal: Leverage Account** |
> | Hongzwang | *"**bypasses API restrictions** on teacher execution"* | **2.3 Hongzwang: Jailbreak Tech** |
> | PSBreakup | *"restores capabilities weakened by model merging"* | 2.4 PSBreakup: Model-Merge Reversal |
> | Kreator | *"converts expert interventions into trainable reasoning"* | 2.5 Kreator: Expert-Guided Intervention Internalization |
>
> 🎯 **3/5에서 중립 동사(analyzes · reduces · bypasses)가 목차에서 hack · leverage · jailbreak 로 바뀐다.** 초록만 읽으면 "효율화 기법 5종", 목차까지 읽으면 **"교사 모델 API를 뚫는 기법"** 이 섞여 있다.
> 📌 **이건 [[한정어-탈락]] 이 아니다 — 저자가 한정어를 뗀 게 아니라 초록과 목차에서 서로 다른 어휘를 썼다.** 볼트가 09-19에 수집기에 보낸 요청 1(*"초록/README 밖 1단계"*)의 **가장 값싼 승리**다: 클릭 1회, PDF 아님, **목차만으로 결론의 성격이 바뀌었다.**

> [!note] ✅ 공정하게 — 저자는 윤리 진술을 달았다
> 본문 Ethics Statement 원문: *"Our research is **defensive in intent**: every technique described in this report serves the construction of execution-verified training data for cyber-security workloads, and **all exploit-related activity was confined to our own sandboxed environments**."*
> ✅ **명시적 선언이 있고, 범위(자체 샌드박스)까지 적었다.** 볼트의 [[자기제한-명시]] 계열에 해당한다.
> ⚠️ 다만 **선언과 절 제목이 같은 문서 안에서 긴장한다** — 샌드박스 한정은 익스플로잇 활동에 걸리고, `Hongzwang: Jailbreak Tech`(교사 API 우회)는 **제3자 서비스**를 향한다. **이 둘이 같은 범위 선언으로 덮이는지는 초록·목차·윤리진술 세 곳 중 어디에도 적혀 있지 않다.**

> [!warning] 🔴 게시일이 수집기 기록과 6일 다르다
> 수집기: *"게시 09-14"*. **HF API 실측: `publishedAt` = 2026-09-08 · `submittedOnDailyAt` = 2026-09-14.**
> 🔴 수집기가 적은 것은 **HF 데일리 등재일**이지 arXiv 게시일이 아니다. **배달 시점 기준 게시 후 12일 된 논문**이다. → 배치 5건 전건에서 같은 혼동이 발생했다 → 신설 [[게시일-이중화]].
> 📌 이 차이가 [[선발창-누락]] 에 직접 걸린다: **"7일 창"을 어느 날짜에 걸 것인가**에 따라 이 논문은 창 안(데일리 09-14 기준)이기도 하고 창 밖(게시 09-08 기준)이기도 하다.

> [!note] 📌 업보트 재조회 — 볼트 기록 120 → 수집기 배달 123 → **볼트 실측 133**
> 2026-09-20 HF API 실측 **133**. 09-19 볼트 120 → 09-20 수집기 123 → 같은 날 볼트 133.
> 🎯 **같은 날 안에서도 10이 움직였다.** 볼트가 [[NeoHorse-1-Paper]] 에서 421→170 으로 배운 것(*"업보트는 배달 시점 재조회값을 적어라"*)의 연장이고, **여기서는 재조회 간격이 시간 단위여도 차이가 난다**는 것이 추가된다.
> `backlog` 태그 — 09-19 볼트 판정 (a)에 따른 **배치당 2건 중 1건**으로 배달됨. ✅ 수집기가 규칙을 지켰다.

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐⭐ — 🔴 **GitHub 레포 없음**(HF API `githubRepo: None` 실확인) · 코드·데이터·체크포인트 **공개 흔적 0**. ✅ 다만 **CyberGym 공식 리더보드 10위**는 외부 검증 표면이고, 63.24%에 *"as of September 1, 2026"* 날짜가 붙어 있다.
- **즉시 활용**: **NO.** 가중치도 코드도 없다. 활용 가능한 것은 **방법론 한 가지**: *실행 검증 + 증거 감사를 통과한 궤적만 학습에 넣는다.* 🎯 이건 [[Recuris]] 의 **검증 게이트**와 같은 형태이고, [[Agora]] 의 evidence score와도 같은 방향이다 — **이번 배치에서 셋이 동시에 나왔다.**
- **6개월 영향력**: 🎯 *"7인 팀이 프런티어 사후학습을 한다"* 가 사실이면 병목이 **GPU에서 환경 구축으로** 이동한다는 뜻이다. [[하네스-설계-축]] 의 *"모델을 바꾸지 않고 감싸는 층"* 이 **학습 데이터 생산 설비**로 한 칸 더 내려간다.
- **대체 관계**: 해당 없음(모델 미공개).
- **허와 실**: 🔴 **+23.76% · +10.49% 는 "시작 모델 대비" 상대값**이다. 절대 점수는 초록에 없다. 리더보드 10위는 절대 위치지만 **모델 3종 중 s1 하나**의 것이다. ⚠️ *"1st among models at comparable parameter scales"* — **분류 기준(동급 파라미터대)을 저자가 정의했다.**
- **액션**: **읽기만.** CyberGym 리더보드에서 10위·63.24%를 **직접 대조**하면 이 논문에서 외부 검증 가능한 유일한 수치가 확인된다.

> [!question] 미해결 질문
> 1. `Hongzwang: Jailbreak Tech` 의 **대상 서비스와 윤리 범위** — 본문 2.3절 미열람(목차까지만 봤다).
> 2. **164,269 궤적의 공개 여부** — 초록·목차에 없음.
> 3. 초록이 언급한 *"the recently disclosed incident in which evaluation models at..."* 의 **지시 대상** — 미확인.

## 관련 페이지
- [[게시일-이중화]]
- [[선발창-누락]]
- [[NeoHorse-1-Paper]]
- [[Agora]]
- [[Recuris]]
- [[하네스-설계-축]]
- [[자기제한-명시]]
- [[한정어-탈락]]
- [[ai-news]]

## 원본
- 출처: https://huggingface.co/papers/2609.08418 · https://arxiv.org/abs/2609.08418
- 볼트 실측(2026-09-20, HF papers API + arXiv HTML): 업보트 **133**(수집기 123 · 볼트 09-19 기록 120) · 저자 **7** · **githubRepo: None** · `publishedAt` **2026-09-08** · `submittedOnDailyAt` **2026-09-14**
- 수치 출처: 초록 원문(164,269 · +23.76% · +10.49% · 63.24% · 10위) **전건 대조 일치** · 본문 목차 및 Ethics Statement **arXiv HTML 실열람**
- raw 대비: 볼트 추가 = 🔴 **목차 절 제목 3건이 초록 동사와 다름(Signature Hack · Leverage Account · Jailbreak Tech)** · ✅ **Ethics Statement 실인용 및 그 범위의 긴장 지적** · 🔴 **게시일 09-14는 데일리 등재일, 실제 게시 09-08(6일 차)** · **업보트 같은 날 123→133**
- 신뢰도: ⭐⭐ (초록 수치 전건 일치 · 외부 리더보드 존재 / 코드·가중치·데이터 전무, 상대값 중심)
