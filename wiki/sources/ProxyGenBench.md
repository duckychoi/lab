---
title: "ProxyGenBench — 영상 생성 모델의 프록시 충실도와 최종 품질이 순위를 뒤집는다는 것을 잰 벤치 (arXiv 2611.34457)"
type: source
domain: ai-news
tags: [ai-news, paper, benchmark, video-generation, seedance, kling, wan, minimax-h3, rank-inversion]
created: 2026-11-28
updated: 2026-11-28
sources: [https://huggingface.co/papers/2611.34457]
reliability: medium
---

**논문**: arXiv 2611.34457 · 업보트 **36**(수집기 11-28 = 볼트 API 일치) · Tencent · 코드 https://github.com/2kxx/ProxyGenBench (볼트 API 확인)

## 핵심 인사이트
> [!insight] Strict 순위와 Joint 순위가 뒤집힌다 — 중간 프록시 점수로 모델을 고르면 최종 품질을 놓친다([[복합지표-분해]] 본배치의 중심 표본)
> Preserve(원소 유지) · Complete(완성도) · Bind(결합) 체크리스트 3축으로 60 장면 · 312 케이스 채점. **오디오 참조 없는 Strict** 순위: Seedance-2.5 0.450 · Kling-4.0 0.425 · Wan-3.0 0.399 · Seedance-2.0 0.375 · MiniMax-H3 0.344. 그런데 **Joint(3축 동시 충족)는 7.2~17.4%** 대에 머물고 **최고는 Strict 4위 Seedance-2.0(17.4%)** — 1위가 아니라. 게다가 **프록시(디테일 유지)가 좋을수록 Complete가 나빠지는** 음의 관계 — 트레이드오프가 노이즈가 아니라 구조적.

> [!warning] 채점자 일치율 92.9%는 자기보고 — 체크리스트 채점의 재현성은 미검증
> 그레이더-인간 일치 92.9%는 논문 저자 보고. 체크리스트 벤치의 전형적 약점(채점 기준 경계선 케이스)에 대한 외부 검증 없음.

## 도메인별 추출 (ai-news)
- **즉시 활용**: 영상 생성 모델 선정 시 프록시 벤치 순위(Strict)만 보지 말고 Joint 지표 확인 — Seedance-2.5가 프록시 1위여도 결합 품질은 Seedance-2.0이 이김.
- **설계 교훈**: "중간 지표 최적화 ↔ 최종 품질" 역전을 명시적으로 잰 벤치 설계 — 자체 평가 파이프라인 설계 시 3축 체크리스트 패턴 차용 가능.
- **경쟁 우위 빈틈**: [[MiniMax-H3]] 가 5개 중 최하위(0.344) — H3 계열 선택 시 결합 정확성 리스크 인지([[Minimax-h3-Turbo-Fusion]] · [[Minimax-h3-Turbo-lightx2v]] 계열 파생물 평가에도 적용).
- **액션**: 없음(관찰 — 영상 모델 벤치 재검토 시 Joint 지표 우선).

## 관련 페이지
- [[복합지표-분해]] · [[MiniMax-H3]] · [[Minimax-h3-Turbo-lightx2v]] · [[Tencent]] · [[ai-news]]

## 원본
- 출처: https://huggingface.co/papers/2611.34457
- 확인 범위: HF papers API(볼트 11-28 — 업보트 · githubRepo 2kxx/ProxyGenBench 일치) · 본문 수치(Strict 5모델 · Joint 7.2~17.4% · 역전 · 음의 관계 · 일치율 92.9% — 수집기 11-28 판독 인용) · 실행 0
- 신뢰도: ⭐⭐⭐ (역전을 주 결과로 명시 · 채점 일치율은 자기보고)
