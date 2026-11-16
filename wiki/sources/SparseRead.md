---
title: "SparseRead (Read Less, Solve More) — 에이전트의 과잉 읽기를 막는 읽기 제어 계층"
type: source
domain: local-llm
tags: [local-llm, agent-memory, token-efficiency, context, paper]
created: 2026-11-16
updated: 2026-11-16
sources: [https://huggingface.co/papers/2608.22237]
reliability: medium
---

**논문**: arXiv 2608.22237 · HF 업보트 23 · 저자 8명(Zedong Liu … Dingwen Tao · Guangming Tan) · HF 조직 표기 `ict-cas` · 코드 [Liuzedooong/SparseReading](https://github.com/Liuzedooong/SparseReading) ★**83**(볼트 11-16 · 수집기 63).

## 핵심 인사이트
> [!insight] 컨텍스트 압축을 모델이 아니라 "읽기 인터페이스"에서 한다
> 웹페이지 · 문서 · 레포 · 도구 응답을 통째로 노출하는 읽기 인터페이스가 토큰 · 지연을 늘리고 증거를 희석한다. SparseRead 는 **에이전트 모델을 건드리지 않는** 제어 계층: ① Read Intent Protocol(정보 필요 · 소스 커버리지 추적) ② Adaptive Reader Backends(증거 찾는 방식 선택) ③ Budgeted Read Gate(에피소드당 원문 노출 누적 상한 + 전체 보기 폴백). → [[에이전트-메모리-레이어]] 의 입력단 버전.

## 도메인별 추출 (local-llm)
- **실용성 판단**: [[Anthropic]] Claude Opus 5 포함 6개 모델 × 5개 시나리오에서 **총 토큰 최대 −92.9% · 시간 최대 −89.0%**, **97% 설정에서 품질 유지 또는 향상**. 3개 에이전트 프레임워크에 통합.
- **트레이드오프**: 웹 딥서치에선 토큰 **−31.0~43.0%** · 시간 −23.0~37.0% — 헤드라인 −92.9% 는 최선 시나리오. 3% 설정은 품질 하락(초록이 그 크기는 적지 않음).
- **Hermes 적용**: 개념은 즉시 적용 가능 — 도구 응답을 전부 컨텍스트에 붓지 말고 **에피소드 노출 예산 + 필요 시 전체 보기** 규칙. 로컬 소형 모델일수록 컨텍스트가 비싸 효과가 크다.
- **오픈소스 구현체**: 코드 공개(★83).

> [!warning] 헤드라인 = 최선 사례
> "최대" 수치와 딥서치 구간 수치의 차이(−92.9% vs −31~43%)가 크다 → [[천장-기준선]] · [[배수-조건분산]].

## 관련 페이지
- [[에이전트-메모리-레이어]] · [[에이전트-웹접근]] · [[BookNavigator-Self-Learning]](반대 방향: 더 깊이 읽기) · [[배수-조건분산]] · [[천장-기준선]] · [[local-llm]]

## 원본
- 출처: https://huggingface.co/papers/2608.22237
- 확인 범위: HF papers API 초록 전문 · 저자 · 코드 링크 · 스타(볼트) · 🔴 본문 · 코드 미열람
- 신뢰도: ⭐⭐⭐ (초록 수치 · 코드 공개 · 실사용 모델 포함 평가)
