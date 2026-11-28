---
title: "OS-Omni — 6개 플랫폼을 하나의 벤치로 잇는 컴퓨터 사용 에이전트 평가 (arXiv 2611.34232)"
type: source
domain: ai-news
tags: [ai-news, paper, computer-use-agent, benchmark, cross-platform, osworld, ios, android]
created: 2026-11-28
updated: 2026-11-28
sources: [https://huggingface.co/papers/2611.34232]
reliability: medium
---

**논문**: arXiv 2611.34232 · 업보트 **109**(수집기 11-28 = 볼트 API 일치) · Touchstone AI · 코드 https://github.com/OS-Copilot/OS-Omni (볼트 API 확인)

## 핵심 인사이트
> [!insight] CUA 평가의 사각지대 — 플랫폼별 점수를 평균 하나로 접으면 극단이 사라진다([[복합지표-분해]])
> Windows · Ubuntu · macOS · iOS · Android · Web 6개 플랫폼에 플랫폼당 48개 + 크로스플랫폼 12개 워크플로우로 CUA를 통합 벤치마킹. 평균으로는 **Claude Opus 5.5 68.5% vs 인간 77.3%** 로 "아직 9%p"처럼 보이지만, 세부는 극단: **Linux에선 인간 초과**, iOS · macOS에선 25p 이상 뒤짐. 남은 약점도 한 종류로 수렴 — 장기 상태 추적(long-horizon state tracking).

> [!warning] 인간 기준선 자체가 플랫폼마다 다르다 — 절대 비교는 조심
> 인간 1작업 평균 **67.54스텝**(OSWorld 15.0과 비교해 참고용 제시). 플랫폼별 인간 성공률이 다르므로 "68.5% vs 77.3%" 격차는 플랫폼 구성 비중에 따라 달라짐 — 모바일(iOS/Android) 과제가 늘어나면 격차는 더 벌어질 것.

## 도메인별 추출 (ai-news)
- **즉시 활용**: NO — 벤치 자체. 단 6플랫폼 × 크로스플랫폼 워크플로우 설계도는 자체 에이전트 테스트 설계 참고.
- **설계 교훈**: 평균 점수 1개가 아니라 **플랫폼별 최악 케이스**를 보고해야 함 — 벤치 리포트 작성 시 패턴으로 차용.
- **6개월 영향력**: [[NightWatch]] 같은 CUA 보정 계층과 짝을 이루는 평가 축 — "CUA 모델 성능 보고 표준" 경쟁이 본격화.
- **액션**: 없음(관찰 — CUA 도입 검토 시 플랫폼별 세부표 확인용).

## 관련 페이지
- [[NightWatch]] · [[복합지표-분해]] · [[하네스-설계-축]] · [[ai-news]]

## 원본
- 출처: https://huggingface.co/papers/2611.34232
- 확인 범위: HF papers API(볼트 11-28 — 업보트 · githubRepo OS-Copilot/OS-Omni 일치) · 본문 수치(6플랫폼 구성 · 인간 스텝 · 플랫폼별 격차 — 수집기 11-28 판독 인용) · 실행 0
- 신뢰도: ⭐⭐⭐ (플랫폼별 세부 공개 · 평균의 한계도 본문에서 명시)
