---
title: "Incentivizing Self-Learning in LLMs via RL — 교과서를 스스로 읽고 증명하는 BookNavigator"
type: source
domain: ai-news
tags: [ai-news, reinforcement-learning, long-context, self-learning, paper, internlm]
created: 2026-11-16
updated: 2026-11-16
sources: [https://huggingface.co/papers/2610.39671]
reliability: medium
---

**논문**: arXiv 2610.39671 · HF 업보트 37 · 저자 9명(Lingkai Kong … Kai Chen · Wenwei Zhang) · HF 조직 표기 `internlm` · 코드 링크 없음 · HF Daily 11-12 페이지.

## 핵심 인사이트
> [!insight] RAG 의 "찾아서 붙이기"와 다른 축 — "찾아서 배우고 적용하기"
> 낯선 분야 문제는 사실 검색 · 집계가 아니라 **지식 습득과 추론의 결합**이 필요하다는 문제 설정. 과제는 교과서 기반 수학 증명 — 모델이 BookNavigator 인터페이스로 교과서를 탐색 · 학습하고 연습문제 증명을 작성(모범 답안 비공개), 세분화된 보상으로 RL. → [[RAG vs LLM-Wiki]] 질문의 모델 쪽 답: 자료를 "읽는 방법" 자체를 학습시킨다.

## 도메인별 추출 (ai-news)
- **신뢰도**: 초록 수치 있음 · 코드 없음.
- **수치**: [[Intern-S2-Preview]]-35B 전체 증명 정확도 **51.5% → 79.5%**(+28.0%p), 교과서 없는 RL · 고정 검색 베이스라인 상회, 도메인 내 · 외 교과서 모두 개선. 장문맥 전이: BrowseComp-Plus **+1.7%p** · CL-bench **+2.3%p**(베이스 대비).
- **허와 실**: 본 과제 +28%p 와 전이 +2%p 사이의 큰 낙차 — 학습한 것은 대부분 **과제 내** 효과다([[분포내-우위]]). 베이스라인들의 수치는 초록에 없어 "상회" 격차 크기는 미확인.
- **즉시 활용**: NO(학습 방법론). 6개월 영향력: 에이전트가 긴 문서를 탐색하는 [[에이전트-메모리-레이어]] 설계에 "탐색 행동 자체를 보상으로 학습"하는 선택지.
- **액션**: 없음.

## 관련 페이지
- [[Intern-S2-Preview]] · [[InternScience]](소속 관계 미확인) · [[SparseRead]](반대 방향: 덜 읽기) · [[분포내-우위]] · [[하네스형-에이전틱-RL]] · [[RAG vs LLM-Wiki]]

## 원본
- 출처: https://huggingface.co/papers/2610.39671
- 확인 범위: HF papers API 초록 전문 · 저자 · 조직 필드(볼트) · 🔴 본문 미열람 · internlm 과 [[InternScience]] 의 관계 미확인
- 신뢰도: ⭐⭐
