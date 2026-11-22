---
title: "sensenova/SenseNova-Loop-9B-GGUF — 루프형 9B 멀티모달 모델 GGUF (추론 환산 약 14.6B · 256K 컨텍스트에 약 15GiB 주장 · NL2Repo 는 Qwen3.8-27B 에 열세)"
type: source
domain: local-llm
tags: [local-llm, hf-model, gguf, looped-layers, multimodal, long-context, sensetime, apache-2.0]
created: 2026-11-22
updated: 2026-11-22
sources: [https://huggingface.co/sensenova/SenseNova-Loop-9B-GGUF]
reliability: medium
---

**HF**: dl30 68,559 · 좋아요 131(볼트 API 11-22 · 수집기 130) · 생성 2026-11-18 · 내부 ID `6afd49ef…` · apache-2.0 · base_model `sensenova/SenseNova-Loop-9B`

## 핵심 인사이트
> [!insight] 같은 날 두 번째 루프형 — "9B" 는 저장 크기이고 연산은 14.6B 급이다
> 32개 물리 디코더층 중 4–27층 블록을 가중치 공유로 2회 반복해 56층 연산(약 9B · **추론 환산 약 14.6B**), 2-stream mHC 잔차, 선형/전체 어텐션 4층 주기 하이브리드, 컨텍스트 512K, 텍스트 + 이미지 → 텍스트. [[Inkling-2-Mini-GGUF]] (12층 × 3회)와 같은 날 도착 → [[파라미터-다중표기]].

## 도메인별 추출 (local-llm)
- **실용성 판단**: 4비트 가중치 + 8비트 KV 캐시로 256K 컨텍스트 멀티모달 추론 시 **약 15GiB GPU 메모리**(카드 주장) — 16GB 급 GPU 장문맥 후보. `custom_code` 필요.
- **트레이드오프 (카드 수치 · 볼트 11개 값 문자열 검출)**: Preview → 정식 AutomationBench 14.33 → 36.67 · Terminal-Bench 2.1 40.45 → 59.55 · GAIA 37.86 → 69.90 · BIRD 72.34. [[Qwen3.8-27B]] 대비 AutomationBench 동률(36.67) · AIDABench 65.31 vs 65.01 · 🔴 **NL2Repo 41.36 vs 44.60 열세**.
- **Hermes 적용**: 🟡 장문맥 에이전트 · 웹/SVG 생성용 소형 후보. 속도는 9B 가 아니라 14.6B 급으로 예상해야 한다.
- **메모리 아키텍처**: 512K 컨텍스트에 의존(외부 메모리 아님).
- **오픈소스 구현체**: GGUF(커스텀 코드 경로).

> [!warning] 단서
> - Preview 대비 큰 폭 상승(GAIA +32)은 **자기 이전 버전 대비**다. 타 모델 대비는 동률 · 근소 · 열세가 섞여 있다.
> - 벤치가 GGUF 에서 측정됐는지 원본에서 측정됐는지는 수집기 요약에 없다 — 미확인.
> - 볼트 확인은 문자열 존재까지.

## 관련 페이지
- [[SenseTime]] · [[Inkling-2-Mini-GGUF]] · [[파라미터-다중표기]] · [[Qwen3.8-27B]] · [[배포출처-봉인]] · [[local-llm]]

## 원본
- 출처: https://huggingface.co/sensenova/SenseNova-Loop-9B-GGUF
- 확인 범위: HF models API · 카드 README 원문(17,855B) 수치 11개 문자열 검출 · 🔴 표 열 귀속 · 측정 대상(GGUF/원본) 미확인 · 실행 0
- 신뢰도: ⭐⭐⭐
