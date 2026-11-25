---
title: "NightWatch — 0.8B 감시 모델로 컴퓨터 사용 에이전트에 연속 지각을 붙이는 플러그인 (arXiv 2611.28947)"
type: source
domain: ai-news
tags: [ai-news, paper, computer-use-agent, watcher, interrupt, latency, plugin, osworld]
created: 2026-11-25
updated: 2026-11-25
sources: [https://huggingface.co/papers/2611.28947]
reliability: medium
---

**논문**: arXiv 2611.28947 · 업보트 **34**(수집기 11-25 = 볼트 API 일치) · 소속 표기 없음 · 저자 5명 · 코드 https://github.com/SuJQ0722/NightWatch (★1 · Apache-2.0)

## 핵심 인사이트
> [!insight] 본체를 한 글자도 고치지 않고 감시층만 얹어 "낡은 화면에 행동하는" 실패를 줄인다
> VLM 에이전트가 스크린샷을 보고 추론하는 사이 화면이 바뀌어 "낡은 상태"에 행동하는 문제를, **10Hz로 화면을 보는 System-1 감시 모델 NightWatch-0.8B**가 추론 중 인터럽트 · 실행 직전 무효화 · 화면 안정 시 깨우기로 보정. **에이전트 모델 · 프롬프트 · 행동공간은 그대로** — [[동결-교정층]] 의 정석적 표본(본체 동결 3중 + 외부 감시층).

> [!warning] 성공률은 표준편차 범위 내 동률 — 실익은 대기 · 헛동작 시간 절감이다
> 표 1(OSWorld-Verified **100과제 부분집합** · 3회): MiMo-V2.6-Flash 성공률 66.3±4.5 → 68.0±3.6(**표준편차 범위 내, 사실상 동률**), 비추론 대기 197.4 → **132.7초(−33%)**, 낭비시간 16.3 → 7.7%, stale 행동 17.4 → 8.3%. DynaCU-Bench(동적 49과제) 39.5 → 44.2%. **지는 행**: Qwen3.8-27B 에이전트는 DynaCU 성공 34.7 = Vanilla 34.7(**개선 0**) / 도메인별(표 8) LibreOffice Impress 54.2 < Vanilla 58.3 · PUSV 64.6, Writer 75.0 < PUSV 87.5, OS 62.5 < Vanilla 70.8 / DynaCU 일시 알림 33.3 < Vanilla 36.7 / API 비용(표 2) MiMo 2.16 > Vanilla 2.10센트.

## 도메인별 추출 (ai-news)
- **즉시 활용**: 화면이 계속 바뀌는 웹 · 대시보드 자동화에서 **대기 시간 −33%** — 성공률이 아니라 속도 · 비용 낭비 감축이 실익. 정적 문서 작업(Writer · Impress)에선 오히려 해례.
- **설계 교훈**: 감시 모델 0.8B를 본체와 분리해 두면 본체 교체·업그레이드와 무관하게 재사용 가능 — 플러그인 구조의 실익.
- **적용 조건**: 동적 화면 과제만. Qwen3.8-27B에서는 개선 0 — 모델-감시 조합 의존성 존재.
- **액션**: 없음(관찰 — 브라우저 자동화 요구 시 재검토).

## 관련 페이지
- [[동결-교정층]] · [[하네스-설계-축]] · [[ai-news]]

## 원본
- 출처: https://huggingface.co/papers/2611.28947
- 확인 범위: HF papers API(볼트 11-25 — 업보트 34 · githubRepo 일치) · 본문 표 1 · 2 · 8 및 지는 행(수집기 11-25 판독) · 실행 0
- 신뢰도: ⭐⭐ (OSWorld는 100과제 부분집합 · 모델 조합 의존성 · ★1 레포)
