---
title: "Kolibri-1.1 — 독일어 특화 MoE 추론 모델, Overall은 크게 올랐지만 에이전트는 전작보다 후퇴 (Aleph-Alpha)"
type: source
domain: local-llm
tags: [local-llm, model, moe, reasoning, german, long-context, aleph-alpha, gguf]
created: 2026-11-28
updated: 2026-11-28
sources: [https://huggingface.co/Aleph-Alpha/Kolibri-1.1]
reliability: medium
---

**모델**: https://huggingface.co/Aleph-Alpha/Kolibri-1.1 · **다운로드 1,725**(볼트 API 11-28 · 생성 2026-11-20 · 공식 GGUF 별도 레포 44,807 — 베이스 레포보다 GGUF가 26배, [[원본-파생-역전]] 역방향 표본) · **Apache-2.0** · [[Aleph-Alpha]]

## 핵심 인사이트
> [!insight] 유럽(독일) 주권 AI의 실전형 모델 — 75B/3.44B 활성 MoE + 262K 네이티브 컨텍스트
> 독일어/영어 이중 MoE 추론 모델(총 75B · 활성 3.44B), **262K 네이티브(최대 1M)** 컨텍스트, ~77.6GB로 **B200 1장이 최소 요구**. Overall **73.2**(전작 Kolibri 1.0 66.6, +6.6) — 비용은 1k 토큰당 GPU-h **0.72 → 0.21**(약 3.4배 절감). 유럽 GPAI 코드 서명국 제품.

> [!warning] Overall +6.6 뒤에서 에이전트는 오히려 내려갔다([[복합지표-분해]])
> 지는 행 3종: ① **에이전틱 평균 61.0 < 전작 61.8** — 후퇴. ② **Tau3-Bench Banking 38.7→28.6**(−10.1, 전작 대비 큰 폭 하락). ③ Overall도 Qwen3.8 Flash Next 80.1 · GLM-5.3 Flash 80.0에 밀림. 즉 "+6.6 진전"은 범용 지표 위주의 이야기이고, 에이전트 · 도메인 벤치에서는 세대 후퇴가 동시에 일어남. 또한 77.6GB 요구로 "로컬" 범주에 속하긴 하나 소비자 장비에는 사실상 배제.

## 도메인별 추출 (local-llm)
- **즉시 활용**: NO — B200 요구로 로컬 실험 범위 밖. 독일어 프로덕션(유럽 규제 대응) 요건이 생기면 검토.
- **설계 교훈**: 전작 대비 개선 보고에서 **에이전틱 후퇴를 카드에 명시**한 점 — [[자기제한-명시]] 긍정 표본.
- **6개월 영향력**: 유럽 주권 모델 축(프랑스 · 독일 계열)의 성능 경쟁 표본 — "규제 대응 모델이 성능도 잡을 수 있는가"의 시험대.
- **액션**: 없음(관찰 — 유럽어 요건 작업 발생 시 재검토).

## 관련 페이지
- [[Aleph-Alpha]] · [[복합지표-분해]] · [[원본-파생-역전]] · [[자기제한-명시]] · [[지표-창길이]] · [[local-llm]]

## 원본
- 출처: https://huggingface.co/Aleph-Alpha/Kolibri-1.1
- 확인 범위: HF API(볼트 11-28 — DL 1,725 · 생성일 · Apache-2.0 일치) · 벤치 수치(Overall 73.2/66.6 · 에이전틱 61.0/61.8 · Tau3-Bench · 경쟁 모델 점수 — 모델 카드 자기보고, 수집기 11-28 판독 인용) · 실행 0
- 신뢰도: ⭐⭐⭐ (지는 행까지 카드 공개 · B200 요구 등 제한 명시)
