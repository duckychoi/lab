---
title: SenseTime (商汤)
type: entity
domain: ai-news
tags: [ai-news, company, china, multimodal, unified-model]
created: 2026-09-11
updated: 2026-09-11
sources: [sensenova-u1.md, SenseNova-U1.5.md]
reliability: high
---

# SenseTime (商汤)

> [!insight] 한 줄
> 중국 컴퓨터비전·멀티모달 대기업. SenseNova 시리즈로 **이해·생성 통합 멀티모달 모델** 노선을 2개 세대 연속 밀고 있다 — [[sensenova-u1]](2026-05, NEO-unify) → [[SenseNova-U1.5]](2026-09, encoder-free·VAE-free 8B-MoT).

> [!insight] 기술 노선 — **중간 표현을 계속 지운다**
> - U1(2026-05): NEO-unify로 이해·생성을 단일 모델에 통합
> - U1.5(2026-09): **비전 인코더도 VAE도 제거**, 공간 일관 패치 재구성 + 최대 4K 네이티브 해상도
> → 세대 간 방향이 일관된다: **모듈 경계를 없애는 쪽.** 통합 모델 진영에서 가장 급진적인 축.
> - 사후학습은 반대로 **분화 후 통합**: 미학·이중언어 텍스트 렌더링·인포그래픽·이미지 편집 **4전문가 개별 최적화 → 멀티전문가 온폴리시 증류**로 흡수 → [[온폴리시-증류]]

> [!warning] 🪞 볼트 예측 정정 — "오픈소스 가능성 낮음"은 빗나갔다
> [[sensenova-u1]](2026-05-13)에서 볼트는 *"**SenseTime 특성상 완전 오픈소스 가능성 낮음**"* 이라 적었다.
> U1.5 초록: *"We **will open-source training code**, including supervised fine-tuning, reinforcement learning, and on-policy distillation."*
> → **벤더 정체성에서 정책을 추론한 것**이 빗나갔다. [[파생표기-함정]] 계보의 변형 — *"이름(벤더)에서 행동을 추론하지 말 것."*
> → ⚠️ 단 **"will"은 미래형**이다. 예고는 공개가 아니다([[IFM]] 선례). **다음 배치에서 실제 공개 확인 필요** — 그때까지 정정은 미완결.

> [!note] 주목도 변화
> HF 업보트 [[sensenova-u1]] **1,580** → [[SenseNova-U1.5]] **78**(저자 65명). 성능 하락이 아니라 **신규성 프리미엄 소멸 + 제품화 단계 진입**으로 읽는 것이 타당하다. **업보트는 신규성 지표지 성능 지표가 아니다.**

## 관련 페이지
- [[sensenova-u1]]
- [[SenseNova-U1.5]]
- [[온폴리시-증류]]
- [[파생표기-함정]]
- [[MiniMax]]
- [[Alibaba]]
- [[IFM]]

## 원본
- 출처: https://huggingface.co/papers/2609.11929 (HF API 실호출 2026-09-11) · https://huggingface.co/papers/2605.12500
- 신뢰도: ⭐⭐⭐⭐ (기업 실체 명확 · 논문 2세대 추적 / 코드 공개는 **예고 단계**)
