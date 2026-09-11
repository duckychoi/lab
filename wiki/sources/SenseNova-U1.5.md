---
title: "SenseNova-U1.5 — 인코더·VAE 없는 8B-MoT 네이티브 통합 멀티모달 모델"
type: source
domain: ai-news
tags: [ai-news, paper, multimodal, unified-model, encoder-free, vae-free, mot, on-policy-distillation, 4k]
created: 2026-09-11
updated: 2026-09-11
sources: [sensenova-u1.md]
reliability: high
---

# SenseNova-U1.5

> [!insight] 핵심 인사이트 — **인코더도 VAE도 없이** 이해·추론·생성을 한 모델에서
> [[SenseTime]] 의 [[sensenova-u1]] 후속. 정식 제목 *"Towards Native Unified Visual Intelligence"*.
> 구조적 주장: **encoder-free · VAE-free** 아키텍처(8B-MoT)에서 시각 콘텐츠를 **이해하고, 추론하고, 생성**한다.
> - 시각 인터페이스 강화: **공간적으로 일관된 패치 재구성**(spatially coherent patch reconstruction)
> - **최대 4K 네이티브 해상도**까지 학습 확장
> → 🎯 통합 모델의 관례적 구성(비전 인코더 + 확산용 VAE)을 **둘 다 제거**한 것이 이 논문의 축이다. 중간 표현을 없애면 **모듈 경계에서 생기는 정보 손실과 정렬 부담이 사라진다**는 베팅.

> [!note] 사후학습 — 전문가를 따로 키우고 **온폴리시 증류로 합친다**
> 초록 원문: *"we optimize **specialized experts** for visual aesthetics, bilingual text rendering, infographic generation, and image editing, and consolidate their capabilities through **multi-expert on-policy distillation**"*
> → 4개 전문가(미학 · 이중언어 텍스트 렌더링 · 인포그래픽 · 이미지 편집)를 **개별 최적화한 뒤 하나로 증류**.
> → [[온폴리시-증류]] 개념의 **가장 명확한 산업 적용 사례**다. "여러 전문가 → 단일 모델"은 MoE와 다른 경로 — MoE는 전문가를 **남겨두고 라우팅**하고, 이건 전문가를 **지우고 흡수**한다.

> [!insight] 초록이 주장하는 일반화 — 구조적 명세로의 전이
> *"**Despite limited exposure to structured formats** in its generation data, SenseNova-U1.5 **generalizes effectively to long, complex, and structured visual instructions**"*
> → 학습 데이터에 구조화 포맷이 적었는데도 **길고 복잡한 구조적 지시를 수행**한다는 주장. 논문의 해석: *"multimodal understanding can **transfer to visual planning and creation**"*
> → 이해 능력이 **생성 계획 능력으로 전이**된다는 것 — 통합 모델의 존재 이유에 대한 직접적 근거다. 분리 모델에서는 이 전이가 원리상 일어나지 않는다.

> [!warning] 🪞 볼트 과거 예측 점검 — 빗나갔다
> [[sensenova-u1]](2026-05-13) 에서 볼트는 이렇게 적었다:
> > *"NEO-unify 아키텍처 상세 공개 여부 불명확. **SenseTime 특성상 완전 오픈소스 가능성 낮음**"*
>
> U1.5 초록 마지막 문장: *"We **will open-source training code**, including supervised fine-tuning, reinforcement learning, and on-policy distillation."*
> → **학습 코드(SFT·RL·온폴리시 증류)를 공개하겠다고 명시**했다. 볼트의 예측은 **벤더 정체성에서 행동을 추론**한 것이었고, 그건 [[파생표기-함정]] 계보의 또 다른 변형이다 — **"이름(벤더)에서 정책을 추론하지 말 것."**
> → ⚠️ 단 **"will"은 아직 미래형**이다. 예고는 공개가 아니다([[IFM]] 건에서 이미 겪음). **공개 여부를 다음 배치에서 확인**해야 정정이 완료된다.

> [!warning] 업보트 1,580 → 78 — 20배 하락을 어떻게 읽나
> [[sensenova-u1]] 은 업보트 **1,580**, U1.5는 **78**이다. 성능이 떨어졌다고 볼 근거는 없다. 가능한 해석:
> - U1이 **"통합 모델"이라는 개념 자체의 신규성**으로 주목받았고, U1.5는 **같은 방향의 개선판**이라 신규성 프리미엄이 없다
> - 저자 **65명**(U1 대비 대폭 증가) = 대형 엔지니어링 프로젝트화 → 연구적 놀라움보다 제품화 단계
> → 🎯 **업보트는 성능 지표가 아니라 신규성 지표다.** 볼트가 업보트를 신뢰도 신호로 쓸 때 이 구분이 필요하다 — 같은 배치 [[DeepSeek-V4.1-Flash]] 의 "다운로드 6 vs ♥1,578" 과 같은 종류의 함정.

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐⭐⭐ — 업보트 **78** · 저자 **65명** · 2026-09-10. **초록 원문 전건 대조 완료.** reliability **high**(수치 주장이 적고 구조 서술 중심이라 검증 범위가 초록에 한정).
- **즉시 활용**: **NO(아직).** 가중치·코드 미공개. 다만 **온폴리시 증류로 전문가 통합**은 내가 [[reat-script]]·영상 파이프라인에서 **여러 특화 프롬프트를 하나로 합칠 때** 참고할 구조.
- **6개월 영향력**: encoder-free·VAE-free가 재현되면 **멀티모달 스택이 단순해진다.** 지금 파이프라인에 붙는 인코더·VAE 의존이 사라지면 로컬 배포 난이도가 내려간다.
- **대체 관계**: [[sensenova-u1]] 의 후속. 동시에 [[MiniMax-H3]]·통합 멀티모달 축의 경쟁자.
- **허와 실**: 초록에 **정량 벤치 수치가 거의 없다**("largely advances", "improving" 등 정성 서술). 4K·8B-MoT·4전문가는 사실이나 **성능 우위는 이 초록만으로 검증 불가**. 이 점이 U1(업보트 1,580) 대비 신중해야 할 이유.
- **액션**: 학습 코드 공개 여부를 **다음 배치에서 확인**(actionable 등록) — 볼트 예측 정정의 완결 조건.

> [!question] 미해결 질문
> **"encoder-free"의 정확한 의미**가 초록에서 확정되지 않는다. 픽셀을 직접 토큰화하는가, 아니면 학습된 패치 임베딩이 있는데 그걸 인코더라 부르지 않는 것인가? **패치 재구성이 있다는 서술과 인코더가 없다는 서술의 관계**가 본문 없이는 모호하다.

## 관련 페이지
- [[sensenova-u1]]
- [[SenseTime]]
- [[온폴리시-증류]]
- [[파생표기-함정]]
- [[단위-불일치]]
- [[DeepSeek-V4.1-Flash]]
- [[MiniMax-H3]]
- [[IFM]]

## 원본
- 출처: https://huggingface.co/papers/2609.11929
- 실측(2026-09-11): 업보트 **78**(raw 일치) · 저자 **65명**(일치) · published **2026-09-10**(일치) · 정식 제목 *"SenseNova-U1.5: Towards Native Unified Visual Intelligence"*
- **초록 원문 대조**: encoder-free·VAE-free·8B-MoT **확인** · spatially coherent patch reconstruction **확인** · native resolutions up to 4K **확인** · 4전문가(aesthetics/bilingual text rendering/infographic/image editing) + multi-expert on-policy distillation **확인** · "limited exposure to structured formats ... generalizes effectively" **확인** · **"We will open-source training code"** 확인
- raw 대비: **전건 일치.** 볼트 추가 = 🪞**볼트의 U1 예측(오픈소스 가능성 낮음) 빗나감 기록** · **업보트 1,580→78 = 신규성 지표지 성능 지표 아님** · 정량 수치 부재 지적
- 신뢰도: ⭐⭐⭐ (초록 서술은 정확 / **성능 우위는 미검증** — 코드·가중치 공개 전까지 판정 유보)
