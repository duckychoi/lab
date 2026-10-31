---
title: "LOWN (Look Only When Needed) — 확산 VLM 디코딩에서 이미지를 필요할 때만 처리"
type: source
domain: local-llm
tags: [ai-news, local-llm, diffusion-llm, vlm, inference-efficiency]
created: 2026-10-31
updated: 2026-10-31
sources: [https://huggingface.co/papers/2610.36671]
reliability: medium
---

**HF**: published 2026-10-27 · upvote 94 · 저자 4(Donghyeon Cho · Eunho Yang 외) · arXiv 2610.36671

## 핵심 인사이트
> [!insight] 임계값 튜닝 없는 "일치하면 재사용" 규칙으로 FLOPs 65% 절감
> LLaDA-V 디코딩에서 이미지를 빼도 결정이 바뀌는 스텝은 평균 22.8%. 그러나 **MMBench 7.9% ~ DocVQA 43.8%** 로 5.5배 벌어진다. 고정 스케줄이 안 되는 이유이자, 평균값만 옮기면 안 되는 이유다.

> [!warning] 평균 뒤에 숨은 것
> ① 99.6%는 **10개 벤치 평균** 유지율이고, 비교 우위는 동일 FLOPs 조건에서 **10개 중 8개** 벤치다. ② 저자 Limitations: 재사용 토큰이 앵커가 낡을수록 새 FULL 예측과 달라지고, **차트·문서 판독에서 절감이 작으며**, 응답별 비용을 디코딩 전에 정할 수 없다. 지연 상한이 필요한 서빙에는 그대로 맞지 않는다. ③ 벤치 대상은 LLaDA 계열 확산 VLM에 한정된다.

## 도메인별 추출
- **실용성 판단**: 확산 LM 서빙을 실제로 할 때만 의미가 있다. 볼트 스택(자기회귀 GGUF)에 직접 적용은 NO.
- **트레이드오프**: FLOPs 35.3% ↔ 점수 99.6%(평균) · KV 캐시와 결합 시 5.6~7.0배 빠른 디코딩(저자 보고).
- **이식 가능한 아이디어**: "저렴한 경로 예측 ≈ 직전 비싼 예측이면 비싼 경로 생략" — 자기회귀 멀티모달 추론이나 에이전트 도구 호출 생략 판단에 빌릴 수 있는 패턴. 🔴 볼트 가설이며 검증 없음.

## 관련 페이지
- [[DTCA]] · [[한정어-탈락]] · [[local-llm]]

## 원본
- 출처: https://huggingface.co/papers/2610.36671 · 코드 https://github.com/hyeon9698/LOWN (★12 · 라이선스 필드 없음 · 볼트 실측) · https://hyeon9698.github.io/LOWN/
- 확인 범위: HF `api/papers` · arXiv HTML 본문 열람(2026-10-31) · 🔴 코드 실행 0회 · 수치는 전부 저자 보고
- 신뢰도: ⭐⭐ (저자 자기 측정 · 볼트 재현 없음)
