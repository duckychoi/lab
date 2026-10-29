---
title: "Falcon — 입술 영상으로 목표 화자만 실시간 분리하는 경량 인과 모델 + 현실형 벤치 RealSSA. AV-TFGridNet 대비 파라미터 −91.9%·연산 1/20.2·GPU 지연 1/11.1. 🔴 SOTA 목록에 실녹음셋은 없다"
type: source
domain: ai-news
tags: [ai-news, hf-paper, speech-separation, audio-visual, target-speaker-extraction, streaming, edge-ai, benchmark, tsinghua]
created: 2026-10-29
updated: 2026-10-29
sources: [https://huggingface.co/papers/2610.32749]
reliability: medium
---

# Falcon: Efficient Streaming Audio-Visual Target Speaker Extraction for Real-World Acoustic Scenes

**HF**: https://huggingface.co/papers/2610.32749 · published **2026-10-23** · Wendi Sang · Kai Li · Yifan Li · Jianqiang Huang · Xiaolin Hu(저자 5) · upvote **144**(수집기 일치)
**코드**: https://github.com/JusperLee/Falcon (HF `githubStars` **13**) · 데모 cslikai.cn/Falcon
**신뢰도**: ⭐⭐⭐ medium(효율 수치 구체적 · 코드·데모 공개 · 실녹음 평가셋 존재)

> [!insight] 핵심 인사이트 — "가벼운 분리기를 여러 번 부르는" 경량화는 절약분을 도로 까먹는다
> 초록이 짚은 두 간극: ① 기존 벤치는 화자 2명 고정이라 근거리/원거리 간섭·잔향·돌발 소음이 없다 ② 고성능 인과 구조는 엣지에 너무 무겁고, 경량 대안은 **작은 분리기를 반복 호출**해서 용량을 되찾으려다 절약을 상쇄한다.
> Falcon 의 답: 분리기가 **인코더-디코더 1패스**로 다중 스케일 시간-주파수 분리를 끝낸다. 인코더 공간 **화자 대조 손실**은 근거리 누설을 줄이면서 **추론 비용 0**이고 다른 백본에도 이식된다.
> 수치: 인과 AV-TFGridNet 대비 **파라미터 −91.9% · 연산 20.2배↓ · GPU 지연 11.1배↓**.
> 🎯 볼트 관점: "학습 시에만 드는 비용으로 추론 품질을 사는" 패턴(대조 손실 · 추론 0비용)은 [[온폴리시-증류]] 류와 같은 축 — 엣지 배포용 모델 설계의 정석.

> [!warning] 🔴 주의 — 수집기 요약에서 빠진 한정 조건
> - 🔴 **SOTA 주장 목록에 RealSSA-Real(실녹음 평가셋)이 없다.** 초록: *"state-of-the-art extraction quality on RealSSA-Sim, LRS2-2Mix, LRS3-2Mix, and VoxCeleb2-2Mix"* — 시뮬레이션 1 + 기존 2화자 혼합 3. 저자가 직접 만든 실녹음셋에서의 순위는 초록에 없다 ⇒ "현실형"이라는 셀링포인트의 핵심 셀이 비어 있다. 수집기는 "실녹음 평가셋도 있음"만 적고 SOTA 목록에서 빠졌다는 점은 적지 않았다 → [[한정어-탈락]] · [[분포내-우위]].
> - 📐 효율 비교 대상은 **인과 AV-TFGridNet 1개**(무거운 쪽)다. 다른 경량 인과 모델 대비 효율은 초록에 없다 → [[비매칭-비교]].
> - 절대 지연(ms)·디바이스 종류는 초록에 없다 — "GPU 지연 1/11.1"은 상대값.
> - RealSSA-Sim 은 저자 제작 벤치 → [[벤치마크-외부축]] 관점에서 자작 벤치 1위는 할인.

## 도메인별 추출 (ai-news · local-llm 접점)
- **신뢰도**: 논문 + 코드(★13) + 데모 + 실녹음 평가셋 공개
- **즉시 활용**: △ — 화상회의·현장 녹음 정리에서 "카메라에 잡힌 화자만" 분리하는 용도. 코드가 있으니 데모 확인은 가능.
- **6개월 영향력**: 엣지 AV 분리 표준 벤치 후보(RealSSA). 근거리 1~5명 + 원거리 10~15명 설정은 기존 2Mix 보다 훨씬 현실적이다.
- **video-saas 접점**: 촬영 소스에서 출연자 음성만 깨끗하게 분리 → 자막·더빙 파이프라인 전처리. 입술이 보여야 하므로 정면 인터뷰형 영상에 한정.
- **허와 실**: 효율 수치는 강하다. "현실 장면" 성능은 실녹음 셀 확인 전까지 미확정.
- **액션**: 본문에서 RealSSA-Real 표 확인(무비용) → SOTA 여부 확정.

## 관련 페이지
- [[온폴리시-증류]] · [[한정어-탈락]] · [[분포내-우위]] · [[비매칭-비교]] · [[벤치마크-외부축]]
- 같은 배치(10-29): [[DTCA]] · [[Sensorimotor-Alignment]] · [[OmniShowcase]] · [[TAO-Agentic-Serving]]
- [[ai-news]] · [[local-llm]]

## 원본
- https://huggingface.co/papers/2610.32749 (초록) · https://cslikai.cn/Falcon/
- 볼트 실측(2026-10-29T09:06Z, HF `api/papers`): upvote 144 · 저자 5 · githubRepo JusperLee/Falcon · githubStars 13 — 수집기 수치 일치 · 🔴 실녹음셋 SOTA 부재 미기재
- 신뢰도: ⭐⭐⭐
