---
title: Qwen-Drive-1.0 — 자율주행용 비전-언어 파운데이션 모델 (검사 가능한 3D 인터페이스)
type: source
domain: ai-news
tags: [ai-news, hf-daily-paper, autonomous-driving, vlm, bev, multimodal, no-numbers, 정정됨]
created: 2026-09-02
updated: 2026-09-13
sources: []
reliability: high
---

# Qwen-Drive-1.0: An Initial Step towards a Vision-Language Foundation Model for Autonomous Driving

**arXiv**: 2609.00111 · **HF**: https://huggingface.co/papers/2609.00111
**지표(2026-09-02)**: 업보트 **76**(데일리 **1위**) · 저자 **16인** · 공개 **2026-08-31** — HF API 실호출 + **초록 원문 대조**
**드리프트**: raw 75 vs API **76**(+1) → API값 채택
**벤더 추정**: 명칭 기준 [[Alibaba]] Qwen 계열(초록에 소속 미기재 → **미확정**)

> [!insight] 핵심 인사이트 — BEV 헤드를 성능 부품이 아니라 **관측 창**으로 쓴다
> 설계의 특이점은 "무엇을 붙였나"가 아니라 **"왜 붙였나"** 에 있다. 사전학습 VLM 아키텍처를 **그대로 유지한 채**(*retains the architecture*) 3D 인지·VQA·모션 플래닝을 한 프레임에 통합하고, 외부 **BEV(조감도) 인지 헤드**가 3D 객체탐지·시맨틱 점유예측·BEV 맵 분할을 **동시에** 수행한다.
> 그런데 초록은 이 헤드의 역할을 이렇게 규정한다 — *"It serves as a **probe** of the 3D information accessible from the shared representations and provides an **explicit, inspectable interface** to 3D scene structure."* **탐침(probe)** 이고 **검사 가능한 인터페이스**다.
> 즉 이 헤드는 주행 성능을 올리는 모듈이라기보다 **"공유 표현 안에 3D 정보가 실제로 들어 있는가"를 밖에서 볼 수 있게 만드는 장치**다. 블랙박스 VLM에 **계기판을 다는 설계**이며, 자율주행처럼 실패가 치명적인 도메인에서 *"모델이 무엇을 알고 있는지 확인할 수 있어야 한다"* 는 요구에 대한 구조적 응답이다.

> [!insight] 이 배치의 숨은 축 — **"내부 상태를 밖에서 검사 가능하게 만들기"**
> 같은 배치 3편이 서로 참조 없이 같은 방향을 향한다.
> - **Qwen-Drive**: 공유 표현 → BEV 헤드라는 *inspectable interface*
> - [[Safin-1]]: 메모리를 *"수동적 기록"* 에서 **라우팅되는 상태 인터페이스**로 재정의
> - [[UI-Venus-2]]: 보상 신뢰성을 위해 **트레이스/샘플 단위 평가자**를 학습 축으로 승격
>
> 공통 명제: **모델이 잘하는지 묻기 전에, 모델이 무엇을 들고 있는지 볼 수 있어야 한다.** 이는 08-31에 세운 [[국소-수리-원리]]의 **전제 조건**에 해당한다 — 그 원리는 *"틀어진 지점을 찾을 수 있어야"* 성립한다고 이미 단서를 달았고, 이번 배치는 **그 "찾을 수 있게 만드는" 층을 각자 짓고 있다.**

> [!warning] ⚠️ 성능 주장 검증 불가 — 데일리 1위인데 수치가 0개다
> 초록의 결과 서술은 두 문장뿐이다: *"Experiments demonstrate **strong** 3D perception and driving scene understanding while **largely preserving** general vision-language capability"* · *"further show **highly competitive** motion-planning performance."*
> **strong · largely · highly competitive — 전부 형용사이고 숫자가 하나도 없다.** open-loop / pseudo-closed-loop / closed-loop **3종 평가를 했다고는 밝히지만**, 벤치마크명·절대 점수·비교 대상이 **전량 미기재**다.
> 미기재 항목: 모델 크기 · 베이스 VLM 버전 · 데이터 규모 · nuScenes/NAVSIM 등 벤치명 · 비교 모델 · 가중치·코드 공개 여부 · 소속 기관.
> **업보트 76으로 데일리 1위인데 검증 가능한 수치가 0개**라는 점을 기록해 둔다. 순위는 관심의 지표이지 근거의 지표가 아니다 — 볼트가 반복 확인해 온 명제의 또 한 사례.

> [!note] 제목이 스스로 낮춘 기대치
> 제목에 **"An Initial Step"** 이 들어 있다. 같은 배치 [[Safin-1]]도 *"only an initial architectural exploration"* 이라 적었다. **13건 중 2건이 제목·본문에서 스스로 "초기 단계"라고 밝힌다** — 과장이 기본값인 환경에서 이 자기 제한은 오히려 신뢰를 높이는 신호로 읽는다. 다만 그것이 **성능 수치 부재를 정당화하지는 않는다.**

## 도메인별 추출 (ai-news)

- **신뢰도**: **high**(문헌 실재·주장 내용) / **성능은 판단 불가**. 이 등급은 *논문이 존재하고 초록이 이렇게 적혀 있다*에 대한 것이다.
- **즉시 활용**: **아니오**(자율주행은 내 도메인 밖). 단 **"탐침으로서의 보조 헤드"** 설계는 이식 가능한 아이디어 — 내부 표현을 검사 가능한 출력으로 뽑는 패턴.
- **6개월 영향력**: **미지수**. 수치가 없어 위치를 매길 수 없다. 본문에 표가 있을 가능성이 높으므로 **초록만으로 기각하지 않고 보류**([[DART-SD]] 때 세운 처리 방침 적용).
- **대체 관계**: 모듈형 자율주행 스택(인지→예측→계획 분리)을 **단일 VLM + 탐침 헤드로 통합**하려는 시도.
- **허와 실**: 걷어내면 = **"사전학습 VLM을 건드리지 않고 BEV 헤드와 플래닝 전문가를 얹고, 단계적 학습으로 일반 능력을 보존했다"**. 구조 설명은 구체적이고, 성능 서술만 비어 있다.
- **액션**: [[actionable]]에 **"본문 확인 대기"** 등재(수치 확보 시 재평가).

## 관련 페이지
- [[Safin-1]] · [[UI-Venus-2]] — 같은 배치 "검사 가능성" 축
- [[국소-수리-원리]] — 이 축이 그 원리의 **전제 조건**을 짓는다
- [[Alibaba]] — 명칭 기준 추정 벤더(미확정)
- [[ai-news]]

---

> [!warning] 🔴 **2026-09-13 정정 — 이 페이지의 "검증 불가" 판정은 틀렸다**
> 아래 `> [!warning] ⚠️ 성능 주장 검증 불가` 콜아웃의 **핵심 주장을 취소한다.**
>
> **취소되는 문장**: *"데일리 1위인데 검증 가능한 수치가 0개"* · *"미기재 항목: 모델 크기 · 베이스 VLM 버전 · 벤치명 · 비교 모델 · 가중치·코드 공개 여부 · 소속 기관"*
>
> **사유**: 가중치 레포 `Qwen/Qwen-Drive-1.0-4B` 가 **2026-08-27에 이미 생성**되어 있었다. 이 페이지를 쓴 **09-02보다 6일 앞선다.** 그 모델 카드에는 **22개 벤치 × 15개 비교모델 표**가 있고, 위에 "미기재"로 열거한 **7개 항목이 전부 들어 있다.**
> - 모델 크기 **4.54B**(safetensors 실측) · 베이스 **Qwen3.5-4B** · 소속 **[[Alibaba]] Qwen 확정**(`Qwen/` 조직) · 가중치 **Apache-2.0 공개** · 벤치 NAVSIM·WOD-E2E·PAI-AV·AlpaSim·LingoQA 등
>
> → **자료가 없었던 게 아니라 볼트가 찾지 않았다.** "초록에 없다"를 "저자가 내지 않았다"로 번역한 것이 오류의 정체다.
> → 실측 결과는 **[[Qwen-Drive-1.0-4B]]** 로. 규칙은 **[[짝-아티팩트-조회]]** 로 신설했다.
>
> ✅ **유지되는 판정**: *"업보트 76 데일리 1위"* 와 *"초록 자체에 수치가 없다"* 는 **사실이다**. 틀린 것은 거기서 *"검증 불가"* 로 건너뛴 부분이다.

> [!insight] 🎯 그리고 초록의 한 주장은 이제 **반증됐다**
> 초록: *"while **largely preserving** general vision-language capability"*
> 모델 카드 표 실측 — **일반 VLM 15개 과제 중 10개에서 베이스 Qwen3.5-4B보다 낮다**(CountQA -4.2 · RefSpatial -3.7 · MMMU-Pro std -2.2 · MMBench -1.6 ...).
> *"largely preserving"* 은 거짓은 아니나(대부분 1~2점대) **방향은 일관된 하락**이다. 상세는 [[Qwen-Drive-1.0-4B]].

