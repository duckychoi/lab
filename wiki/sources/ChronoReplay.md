---
title: "ChronoReplay (LINs lab) — 공간 VLM의 'interface lock-in': 한 응답 형식만 후학습하면 그 형식에만 이득이 몰린다. 시간순 재생+계열 균형으로 3벤치 동시 상승"
type: source
domain: ai-news
tags: [ai-news, hf-paper, spatial-intelligence, streaming, VLM, post-training, egocentric, slam-3dgs, qwen3-vl]
created: 2026-10-28
updated: 2026-10-28
sources: [https://huggingface.co/papers/2610.34283, https://github.com/yihaohu0118/ChronoReplay]
reliability: medium
---

# ChronoReplay: One Answer Interface Is Not Enough for Streaming Spatial Intelligence

**HF**: https://huggingface.co/papers/2610.34283 · published **2026-10-25** · **LINs lab**(Yihao Hu · Yitong Lin 외 · 저자 11) · upvote **131**(수집기 일치 · 데일리 1위)
**코드**: https://github.com/yihaohu0118/ChronoReplay — ★7(수집기 일치) · license **없음**(🔴 README: *"The authors have not yet selected a project-wide license. No project-wide open-source license is granted"*) · 파인튜닝 가중치 **미포함**(*"Supply a local checkpoint"*) · 점수 파일·예측 미동봉
**신뢰도**: ⭐⭐ medium
> [!note] 이름 충돌 없음 — [[ChronoVision]](2608.05631, 잠재 상태 재구성 시간추론)과 **별개 논문**이다.

> [!insight] 핵심 인사이트 — 감독이 "무엇을 구분하도록 강제하는가"가 전이를 결정한다
> 좌/우 판단으로 학습하면 미터 단위 변위를 보존할 필요가 없고, 거리 추정으로 학습하면 범주 관계가 비어 있게 된다. 그래서 응답 형식 하나로 후학습하면 이득이 그 형식에 갇힌다(**interface lock-in**). 해법은 이질적인 공간 감독을 **시간순 에피소드로 재생**하고, **원래 형식 타깃을 유지**하며, **계열(family)별로 손실을 균형** 맞추는 것이다.
> README 수치(Qwen3-VL-8B 공식 대비, 같은 causal observation access): OVO-S **48.98→53.89(+4.91)** · OST **50.52→63.93(+13.41)** · UCS **45.33→52.77(+7.44)**.
> 추론 시 adaptive frame selection만으로 OVO-S **57.98**(평균 80.50프레임, 기존 128). 학습 효과와 **분리 보고**한다. → [[자기제한-명시]]의 좋은 사례다.

> [!warning] 주의
> - ⚖️ "highest three-benchmark mean" 뒤에는 **"among the supervision settings compared here"**라는 한정어가 붙어 있다. 외부 SOTA와 비교한 것이 아니라 자체 감독 설정끼리의 비교다. 수집기는 이 한정어를 옮기지 않았다(→ [[한정어-탈락]]).
> - 🎲 시간순 재생의 순수 효과(shifted-order 대조 대비 **≈+2.41 OST**)는 **시드 2개**뿐이다. 수집기도 "시드 2개"를 적었다(✅).
> - 📉 초록은 "answer serialization이 OST와 UCS 사이에서 이득을 **재분배**한다"고 적는다. 한 벤치가 오르면 다른 벤치가 내려가는 트레이드오프가 대조군 안에 있다는 뜻이다. 수집기 요약에는 빠졌다.
> - 🔒 가중치가 없고 라이선스도 없어서 **재현하려면 직접 학습해야 하고, 상업 이용 권리는 없다.**

## 도메인별 추출 (ai-news · slam-3dgs 접점)
- **slam-3dgs 연결**: 스트리밍 SLAM과 로봇 공간 질의는 "누적된 관측 이력 위에서 범주·거리·시간 답을 모두 내야 하는" 문제다. [[OVO-S-Bench]](에고센트릭 스트림, allocentric mapping이 병목)를 이 논문이 직접 개선 대상으로 삼았다. → [[VLA]] 학습 데이터 설계에도 "형식 하나만 쓰는 SFT"를 피하라는 교훈이 된다.
- **재사용 가능한 레시피**: ① 감독 계열별 정규화 손실 ② 원래 형식 타깃 유지(하나의 포맷으로 통일하지 않음) ③ 시간순 에피소드 구성 ④ 추론 시 프레임 선택은 별도 레버로 둔다.
- 비교 계보: [[OpenSpatial]] · [[SpatialWorld]] · [[Reinforcing-Dual-Path-Spatial-VLM]] · [[Latent-Spatial-Memory]] · [[StreamArena]]

## 관련 페이지
- [[OVO-S-Bench]] · [[ChronoVision]](이름만 유사) · [[VLA]] · [[임바디드-AI]]
- [[한정어-탈락]] · [[자기제한-명시]] · [[Qwen]]
- 같은 배치(10-28): [[The-Trinity]] · [[PDRVLA]] · [[Hy-Nomas]] · [[Rollback]]
- [[ai-news]] · [[slam-3dgs]]

## 원본
- https://huggingface.co/papers/2610.34283 · https://github.com/yihaohu0118/ChronoReplay
- 볼트 실측(2026-10-28): HF upvote 131 · 저자 11 · ★7 · license null · 레포 생성 2026-10-20 · README 30~49·99·114행
