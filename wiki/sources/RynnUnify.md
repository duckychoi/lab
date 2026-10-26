---
title: "RynnUnify — Cosmos3 MoT(8B 추론기 + 8B 확산 생성기) 위에 세운 16B 통합 임바디드 모델. '+9.75 over Cosmos 3 Nano' 는 자기 베이스 대비·자체 벤치 수치"
type: source
domain: slam-3dgs
tags: [slam-3dgs, robotics, embodied-ai, unified-multimodal, world-action-model, visual-planning, vla, alibaba-damo, cosmos3, hf-paper]
created: 2026-10-26
updated: 2026-10-26
sources: [2610.32965]
reliability: medium
---

# RynnUnify: Towards Unified Embodied Brain (HF 2610.32965)

**HF**: https://huggingface.co/papers/2610.32965 · org **DAMO Academy**(Alibaba) · 저자 **23명**(Minghao Zhu · Bohan Hou · Kun Xiang 외) · published 2026-10-23 · 코드 `alibaba-damo-academy/RynnUnify`
**실측(2026-10-26 09:08 UTC)**: upvote **28**(수집기 일치) · ★**15**(HF 메타 7 → 증가 중) · 레포 생성 10-25 · push 10-26 · Apache-2.0(코드) / VisualPlan 은 OpenMDW-1.1 · **HF 가중치 3종 존재**: `RynnUnify-Base`(dl 30) · `-Agentic-Reasoner`(dl 41) · `-WAM-RoboCasa`(dl 31), 모두 2026-10-22 생성
**도메인 판정**: **`slam-3dgs`** — 실로봇(Astribot S1) 제어 · 카메라 입력 월드-액션 모델. 볼트가 [[FRED]] 를 같은 기준으로 재분류한 선례를 따름.
**신뢰도**: ⭐⭐⭐ (가중치·코드 실재 / 핵심 비교가 자기 베이스·자체 벤치)

> [!insight] 핵심 인사이트 — **"Cosmos 3 Nano 대비 +9.75" 는 경쟁 비교가 아니라 파인튜닝 이득이다**
> 본문: *"a 16B unified embodied model built upon the Mixture-of-Transformers (MoT) architecture of **Cosmos3**, comprising an 8B autoregressive reasoner and an 8B diffusion generator"* · *"We retain the autoregressive reasoner of Cosmos3 without architectural modifications"*. README 모델 표: `RynnUnify-Base | Base Model: **Cosmos3 Nano**`.
> 🎯 ⇒ 초록의 *"improves the Rynn-VP overall score by 9.75 points over Cosmos 3 Nano"* 는 **자기 출발점 대비 · 저자 신설 벤치(Rynn-VP) 위**의 개선. 임바디드 데이터로 학습하면 오르는 것이 기대값이다 — [[비매칭-비교]] 는 아니지만 "타 모델을 이겼다"로 읽으면 안 된다. [[Cosmos-3]] 페이지 관점에선 **NVIDIA 오픈 월드모델이 중국 연구소의 임바디드 FM 베이스로 채택된 첫 볼트 사례**다.

> [!warning] 수치 성격 정리 (수집기 대비)
> - **Rynn-VP +9.75점**: 절대 점수차 · 비교 대상 = 자기 베이스 · 자체 벤치.
> - **Rynn-GEU +6.0점**: 대조군 = *"direct reasoning"* = **같은 모델의 에이전틱 확장 유무** (자기 ablation). 역시 자체 벤치.
> - **RoboCasa365 51.5%**: 🔴 **한정어 복원** — 원문 *"on **20 selected** composite RoboCasa365 tasks"*. 수집기 요약은 "selected" 를 떨어뜨렸다([[한정어-탈락]]). 365개 중 선별 20개 · 선별 기준과 경쟁군 수치는 HTML 변환본이 잘려 확인 못함.
> - **실로봇 46.7%**: *"average success across three real-robot tasks"* · 과제당 시행 수(분모) 미확인 ⇒ 46.7 = 7/15 형태일 수 있음(추정). [[임계-의존-성공률]] 주의.
> - "highest average embodied understanding score **among the evaluated unified multimodal models**" — 비교 범위가 통합 모델(UMM)로 한정. 전문 VLM 대비는 아님.
> - arXiv HTML 이 데이터 표 중간에서 잘려 있음(LaTeXML 변환 실패) — 본문 표는 PDF(`RynnUnify.pdf` 레포 동봉) 미열람.

## 도메인별 추출 (slam-3dgs)
- **현재 SOTA**: 통합 UMM 중 임바디드 이해 평균 1위(자체 집계) · RoboCasa365 선별 20과제 51.5% · Astribot S1 실로봇 3과제 평균 46.7%. 공개 경쟁 수치와 직접 대조 불가.
- **실시간 가능성**: 미기재. 16B(8B AR + 8B 확산) 구조에 비디오 예측을 추론 중에 선택적으로 호출 — 30fps 류 제어와는 거리가 멂. 확산 생성기를 매 스텝 돌리지 않으려는 설계가 "selectively use video predictions"(RL 로 언제 상상할지 학습).
- **카메라 파이프라인**: 다중 클립 비디오-언어 인터리브 입력 · VAE 호환 4n+1 프레임 · 3D RoPE + 프레임레이트 변조 유지(Cosmos3 상속). WAM 확장은 latent planning + video-action 공동학습.
- **응용 가능성**: "언제 미래를 상상해서 추론에 쓸지"를 RL 로 배우는 **에이전틱 월드모델 사용** — [[월드모델]] 을 도구처럼 호출하는 패턴. [[FRED]](단일 디노이징 스텝으로 비용 절감)와 같은 문제(확산 월드모델 비용)를 다른 방식으로 푼다: FRED 는 스텝을 줄이고, RynnUnify 는 호출 빈도를 줄인다.
- **필수 레퍼런스**: [[Cosmos-3]](베이스) · [[RynnBrain-1.1]](같은 "Rynn" 계열 임바디드 FM — 동일 조직 여부는 볼트 미확인) · [[FRED]] · [[LaLa-World]].

> [!question] 미해결
> RoboCasa365 20과제 선별 기준 · 경쟁 WAM 수치 · 실로봇 시행 수. PDF 표 확인 필요.

## 관련 페이지
- [[Cosmos-3]] · [[NVIDIA]] · [[Alibaba]]
- [[RynnBrain-1.1]] · [[FRED]] · [[LaLa-World]] · [[BadWAM]] · [[Physical-RSI]]
- [[VLA]] · [[임바디드-AI]] · [[월드모델]] · [[Diffusion-월드모델]]
- [[한정어-탈락]] · [[임계-의존-성공률]] · [[비매칭-비교]]
- 같은 배치: [[HiSTEVE]] · [[UserArena]] · [[RSIHub]] · [[Omni-Woodpecker]]
- [[slam-3dgs]]

## 원본
- 출처: https://huggingface.co/papers/2610.32965 · https://github.com/alibaba-damo-academy/RynnUnify · https://huggingface.co/collections/Alibaba-DAMO-Academy/rynnunify
- 볼트 실측: upvote 28 · ★15 · HF 모델 3종 dl 30/41/31 (2026-10-26 09:08 UTC)
- 신뢰도: ⭐⭐⭐ (가중치·코드 실재 / 자기 베이스·자체 벤치 비교 · 선별 과제)
