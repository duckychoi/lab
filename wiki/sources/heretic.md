---
title: p-e-w/heretic — 언어모델 검열 자동 제거(abliteration) 툴
type: source
domain: ai-news
tags: [ai-news, github-trending, local-llm, abliteration, uncensoring, safety, open-weights]
created: 2026-07-14
updated: 2026-07-14
sources: []
reliability: high
---

# p-e-w/heretic (GitHub ⭐26,261)

**GitHub**: https://github.com/p-e-w/heretic
**스타수**: 26,261 (2026-07-14 기준, 당일 +79) · **도메인**: ai-news

> [!insight] 핵심 인사이트
> **오픈웨이트 LLM의 "거부(refusal) 방향"을 자동으로 탐지·제거해 abliteration(검열 해제)을 무인화하는 도구.** 기존 abliteration은 거부 벡터를 사람이 손으로 찾아 활성화 공간에서 빼내는 수작업이었는데, heretic은 이 과정을 자동화해 **가중치 편집만으로** 모델이 거부하도록 학습된 응답을 풀어낸다. 로컬·오픈모델을 다루는 [[local-llm]] 진영에서 "모델 커스터마이징의 하한선"을 낮추는 도구로, [[NousResearch|Hermes]]류 언센서드 파인튜닝과 목적은 같으나 **재학습 없이 후처리로** 달성한다는 점이 다르다.

> [!warning] 오남용 주의 · 신뢰도
> 이 도구는 **안전장치 제거 기술**이다. 연구·레드팀·개인 실험 맥락에서만 다루고, 공개 서비스에 얹은 배포는 법적·윤리적 책임이 따른다. abliteration은 거부만 제거할 뿐 **모델의 실제 지식·능력을 늘리지 않으며**, 종종 일반 성능 저하(품질 열화)를 동반한다 — "검열만 풀리고 똑똑해지지는 않음". 마케팅 걷어낸 실체는 "가중치 방향 편집 자동화 유틸".

## 도메인별 추출 (ai-news / local-llm)

- **신뢰도**: ⭐⭐⭐⭐ (⭐26,261·당일 +79, 자동수집 수치 기반. 실사용은 미실측)
- **즉시 활용**: NO — 내 워크플로우(down-analysis·reat-*)는 검열이 병목이 아님. 다만 [[Qwen3.6-40B-Deckard-Heretic]] 같은 커뮤니티 병합·언센서드 계보를 이해하는 배경지식.
- **6개월 영향력**: 오픈모델 파생 생태계(HF의 -Heretic·-Uncensored 접미사 붙은 머지들)의 **공급원**. 로컬 모델 다양성↑, 동시에 안전 규제 논의 가열.
- **대체 관계**: 수작업 abliteration 노트북·언센서드 파인튜닝의 일부를 대체(재학습 불필요).
- **허와 실**: "검열 완전 제거"는 과장 — 강한 거부는 부분적으로만 풀리고 성능 손실 트레이드오프 존재.

## 관련 페이지
- [[Qwen3.6-40B-Deckard-Heretic]] — 이름에 Heretic이 붙은 커뮤니티 병합 모델(직접적 연관은 미확인, 명명 계보 추정)
- [[NousResearch]] — 언센서드/파인튜닝 노선 엔티티
- [[local-llm]] — 로컬·오픈모델 도메인
- [[destructive_command_guard]] — 반대 축(에이전트 안전 강화) 대조

## 원본
- 출처: https://github.com/p-e-w/heretic
- 신뢰도: ⭐⭐⭐⭐ (GitHub ⭐26,261, 자동수집)
