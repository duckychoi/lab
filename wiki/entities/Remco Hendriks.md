---
title: Remco Hendriks
type: entity
domain: local-llm
tags: [local-llm, benchmark, 연구자, 단독저자]
created: 2026-09-13
updated: 2026-09-13
sources: [MetroLLM-Bench.md]
reliability: medium
identifiers: [arXiv:2609.10016, continker/metrollm-bench]
---

# Remco Hendriks

**대표 연구**: [[MetroLLM-Bench]](arXiv:2609.10016 · 업보트 29 · **단독 저자**) · 코드 `continker/metrollm-bench`

> [!insight] 단독 저자가 26개 모델 · 955 케이스를 평가했다
> 6개 실제 지하철 노선망(역 37~414개) · 11개 범주 · 955 케이스 벤치를 구축하고 **6개 벤더 26개 모델**을 평가했다(23개 순위화). Tier1 결정적 채점 14요소 + Tier2 의미품질 8요소로 채점 체계를 분리.
> 🎯 이 배치 HF 논문 5편 중 저자 수가 8·4·**1**·3·3인데, **수치 밀도와 반증 밀도가 가장 높은 것이 단독 저자 논문이다.**

> [!insight] 자기 결과를 스스로 반증하는 서술 습관
> 헤드라인(*"4B 학생이 GPT-5.6 상회"*)을 내면서 **같은 초록 안에** 반증 5개를 적는다:
> 9B·27B는 개선 없음 · PEFT 이득이 2B +7.03 → 27B **-0.91** · 규칙엔진 베이스라인 **84.6** · 종합 1위는 **Muse Glimmer 30B** · 서빙 설정만으로 **2.7점** 이동.
> → **볼트가 매 배치 찾아다니는 "지는 축"을 저자가 먼저 적어 뒀다.** [[자기제한-명시]] 의 논문 판본.

> [!warning] 볼트가 지적하는 잔여 결손
> 그럼에도 **75/25 split(717 학습생성 / 238 홀드아웃)** 문장과 헤드라인을 **나란히 놓지 않았다.** 4B 학생은 이 벤치 자신의 데이터로 학습됐고 GPT-5.6은 아니다 → [[분포내-우위]].
> 📌 **정직한 저자도 배치는 놓친다.** 각 문장이 참인 것과 독자가 올바른 결론에 도달하는 것은 별개다.

> [!note] 실체 확인 범위
> HF API에서 저자 1인·소속 미기재. 코드 레포(`continker/metrollm-bench`) 공개 확인. 개인 이력은 미확인 → **reliability medium**.

## 관련 페이지
- [[MetroLLM-Bench]] · [[분포내-우위]] · [[자기제한-명시]]
- [[측정도구-먼저-반증]] · [[요약자와-판정자-분리]]
