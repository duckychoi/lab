---
title: "WorkFactory — 전문 업무 11만 건을 실행 가능한 학습 환경으로 만드는 프레임워크"
type: source
domain: ai-news
tags: [ai-news, local-llm, agent-training, qwen, gdpval]
created: 2026-11-01
updated: 2026-11-01
sources: [https://huggingface.co/papers/2610.37161]
reliability: medium
---

**HF**: published 2026-10-27 · upvote 36 · 저자 13 · arXiv 2610.37161 · 코드 [IQuestLab/WorkFactory](https://github.com/IQuestLab/WorkFactory)

## 핵심 인사이트
> [!insight] 환경 결함이 궤적 품질을 망친다는 진단
> 필요한 정보의 의존성과 위치를 그래프로 계획하고, 프로브 실행으로 결함을 찾아 고친 뒤에야 교사에게 넘긴다. 전제는 다 주되 중간 결과는 주지 않는 경계가 핵심이다. 612개 직업에 112,686개 과제다.

> [!warning] 879 → 1565는 측정법이 다른 두 값의 비교다
> 표에서 **879는 공식 v2.1 Elo**(별표)이고 **1565는 로컬 2앵커 추정치**다. 판정자는 Gemini 3.1 Pro Preview이고, 보정 노드에 베이스 모델 자신이 들어간다. 저자는 부트스트랩 구간이 "방법 형식 오차를 포함하지 않는다"고 적었다. 공식 값끼리 비교한 +686이 아니다. 수집기 요약은 이 구분을 옮기지 않았다.

- **교사 천장**: 교사 GLM-5.3이 1646(공식), WorkPilot-27B는 1612(로컬)로 34점 아래다. 교사를 넘었다는 주장은 없다.
- **수확 체감**: 35B-A3B에서 첫 5K 과제가 +447, 75K→110K는 **+13**이다. 30K에서 이득의 88%(27B는 94%)를 얻는다. 🎯 작은 데이터로 시작해도 된다는 뜻이다.
- **텍스트 전용**: 교사가 텍스트만 지원해 학습·평가 모두 비전 없이 진행했다.
- **기타 벤치**: JobBench 28.91→62.35 · Workspace-Bench 47.12→56.53 · OmegaUse-OfficeVal 7.14→21.18.

## 도메인별 추출
- **신뢰도**: 데이터·모델 공개 표방 · 볼트 미실행.
- **즉시 활용**: 부분 YES. 학습 없이도 "프로브 실행으로 환경을 고친다"는 절차는 에이전트 평가셋 제작에 이식할 수 있다.
- **Hermes 적용**: 소형 모델 파인튜닝 후보이지만, Elo는 로컬 추정이고 볼트에서 돌려 보지 않았다.

## 관련 페이지
- [[Qwen]] · [[Zhipu-AI]] · [[A-RSI]] · [[Trial-by-Trace]] · [[Trajectory2Gym]] · [[DeepSeek-V4.1-Flash-1017]] · [[한정어-탈락]]

## 원본
- 출처: https://huggingface.co/papers/2610.37161
- 확인 범위: HF `api/papers` · arXiv HTML 본문 · 🔴 Table 11 구간 값은 수식 표기라 추출하지 못했다 · 코드 실행 0회
- 신뢰도: ⭐⭐ (로컬 Elo 추정 · 볼트 재현 없음)
