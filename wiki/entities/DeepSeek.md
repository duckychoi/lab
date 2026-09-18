---
title: DeepSeek — 오픈 웨이트 대형 MoE·저비용 추론 중국 프론티어 랩
type: entity
domain: ai-news
tags: [ai-news, entity, china, frontier-lab, deepseek, moe, open-weights, reasoning]
created: 2026-08-04
updated: 2026-09-18
sources: [DeepSeek-V4-Flash-0731.md, DeepSeek-V4.1-Flash-Paper.md]
reliability: high
---

# DeepSeek

> [!insight] 2026-09-18 추가 — [[DeepSeek-V4.1-Flash-Paper]]: 🔴 **저자 592명. 논문이 모델 카드보다 *적게* 말한다**
> ```
> 볼트 실측 (HF papers API)   업보트 36(1위) · authors 592 · githubRepo 없음
> 배치 논문 5건 저자 수: 592 · 14 · 9 · 9 · 13  → 나머지 4건 합(45)의 13배
> ```
> 🎯 **볼트 판정: 저자 수는 신뢰도 지표가 아니라 *종류* 지표다.** 592명 = **기업 백서**(내부 검증 강함, 외부 재현 불가) · 9~14명 = 연구 논문. 🔴 **둘을 같은 "논문" 채널로 배달하면 근거의 성격 차이가 사라진다.**
> 🔴 **초록에 비교 수치가 0개다** — *"delivers **substantially better** performance"* 라는 정성 서술뿐. **반면 볼트의 [[DeepSeek-V4.1-Flash]] 모델 페이지는 12개 축의 숫자를 갖고 있다**(HLE **36.8 vs 56.3** · TB4.0 **31.2 vs 51.8** 등 **불리한 축까지**).
> 🎯 **그러므로 논문만 읽으면 "전영역 우위"로 오해한다** → **역방향 [[한정어-탈락]]: 카드가 밝힌 약점을 논문 초록이 지운다.**
> 📌 **볼트 규칙 신설**: 같은 대상의 논문과 카드가 둘 다 있으면 **불리한 수치는 카드 쪽에 있을 가능성이 높다.** 요약은 약점을 먼저 버린다.
> ✅ 구조는 볼트 기보유분과 정합 — CED(prefill 8B·decode 16B) · CSA2 + FP4 KV → **890B/token** · SWA Bounded Replay로 **영속 KV 1/8** · 컨텍스트 100만 · 45T 멀티모달 토큰
> 🎯 **같은 배치 [[MiniCPM]] SALA와 직교한다**: V4.1-Flash는 **KV 저장을 줄이고**, SALA는 **어텐션 계산을 바꾼다**. **합성 가능하고, 결합 사례는 볼트에 없다** — 이 배치가 만든 가장 큰 빈칸.
> ✅ [[백필-우회]] 재발 없음 — 수집기가 *"논문↔모델 동일 대상"* 을 스스로 적었다.
 (深度求索)

> [!insight] 핵심 인사이트
> **오픈 웨이트 대형 MoE와 "저비용·고효율 추론"**으로 알려진 중국 프론티어 AI 랩. [[GLM-5.2]]의 [[Zhipu-AI]], Kimi의 [[Moonshot AI]], Qwen의 [[Alibaba]]와 함께 **중국 오픈 웨이트 축**의 핵심 꼭짓점. DeepSeek-V2/V3 계열 MoE와 추론 특화 모델(R1 계열)로 "적은 활성 파라미터·낮은 학습/추론 비용"이라는 효율 노선을 확립해 왔다. 2026-08 시뮬레이션 타임라인에서 **[[DeepSeek-V4-Flash-0731]]**(304B·저지연 Flash 계열)로 "저지연 추론 지향" 신규 릴리스 축을 추가.

> [!note] 포지션
> DeepSeek의 일관된 전략은 "절대 최상단 SOTA"보다 **효율(비용·지연) 대비 성능** — MoE 희소 활성·아키텍처 최적화로 동급 성능을 더 싸게. Flash 계열(저지연)은 이 노선의 서빙 측 연장. [[Moonshot AI]] [[Kimi-K3]](2.8T 최상단 규모)가 *규모*로 프런티어를 밀면, DeepSeek는 *효율*로 채택 저변을 넓히는 대비 구도.

> [!warning] V4-Flash 세부는 시뮬레이션 타임라인 미검증
> 랩(DeepSeek)·효율 노선·오픈 웨이트 MoE 이력은 실체이나, **[[DeepSeek-V4-Flash-0731]]의 구체 스펙·벤치는 볼트 시뮬레이션 타임라인(2026-08)의 raw 자동수집 기반으로 실WebFetch 재현 전** — 수치 인용 시 미검증 병기.

## 관련 페이지
- [[DeepSeek-V4-Flash-0731]] — 304B 저지연 텍스트 생성 모델 (2026-08-04)
- [[Zhipu-AI]] — 중국 오픈 축 동료([[GLM-5.2]])
- [[Moonshot AI]] — 중국 오픈 축 동료([[Kimi-K3]])
- [[Alibaba]] — Qwen, 중국 오픈 축
- [[ai-news]]

## 원본
- 대표 모델(시뮬레이션): https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-0731
- 신뢰도: ⭐⭐⭐ (랩·효율 노선·오픈 MoE 이력은 실체, V4-Flash 세부는 시뮬레이션 타임라인 raw 기반 미검증)
