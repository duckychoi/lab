---
title: "DavidAU/Qwen3.5-9B-The-Defiant-Fable-…-MTP-GGUF — 9B 다단계 파인튜닝 무검열판 ("7/7 초과" 는 카드 자체 표와 불일치)"
type: source
domain: local-llm
tags: [local-llm, gguf, uncensored, heretic, qwen3.5, 9b, mtp, fine-tune]
created: 2026-11-14
updated: 2026-11-14
sources: [https://huggingface.co/DavidAU/Qwen3.5-9B-The-Defiant-Fable-Uncensored-Heretic-NEO-IMATRIX-MAX-MTP-GGUF]
reliability: medium
---

**모델**: [DavidAU/Qwen3.5-9B-The-Defiant-Fable-Uncensored-Heretic-NEO-IMATRIX-MAX-MTP-GGUF](https://huggingface.co/DavidAU/Qwen3.5-9B-The-Defiant-Fable-Uncensored-Heretic-NEO-IMATRIX-MAX-MTP-GGUF) · dl30 **2,137,747** · 누적 6,085,893 · likes 1,744 · apache-2.0 · created 2026-07-19 · modified 2026-11-10 (HF API 볼트 실측). 수집기 `ai-news` → 볼트 재분류 `local-llm`.

## 핵심 인사이트
> [!insight] 9B 가 원본 9B 보다 객관식 5개 축에서 오른 것은 표에 있다 — 헤드라인은 그보다 크게 말한다
> Qwen3.5-9B 를 [[heretic]] 처리 후 다단계 파인튜닝한 무검열 GGUF(MTP 포함). 카드 표(instruct · mxfp8, 볼트가 카드 raw 86–118행 직접 판독):
> | 모델 | arc/c | arc/e | boolq | hswag | obqa | piqa | wino |
> |---|---|---|---|---|---|---|---|
> | **이 모델** | 0.647 | 0.836 | 0.895 | 0.706 | 0.460 | 0.784 | 0.695 |
> | Qwen3.5-9B 원본 | 0.571 | 0.719 | **0.895** | 0.683 | 0.426 | 0.770 | 0.671 |
> | Qwen3.5-27B | 0.557 | 0.711 | 0.868 | 0.533 | 0.452 | 0.706 | **0.695** |
> | Qwen3.6-35B-A3B | 0.581 | 0.757 | 0.892 | **0.751** | 0.428 | **0.803** | 0.688 |
> | Qwen3.6-27B | 0.647 | 0.803 | 0.910 | 0.773 | 0.450 | 0.806 | 0.742 |
>
> 무검열 지표: KL 0.0793 · 거부 6/100(원본 100/100). MTP GGUF 는 Q4_K_S 에서 일반 약 130 t/s → 185 t/s 초과(수락률 60% · 2토큰 · RTX 5090 · LM Studio — 카드 144행).

> [!warning] "exceeds 7 of 7 benchmarks for Qwen 3.5 9B, Qwen3.5 27B, Qwen3.6 35B-A3B"(카드 49행) — 셋 다 성립하지 않는다
> - vs **Qwen3.5-9B 원본**: BoolQ 0.895 = 0.895(동률) → 6/7. *(수집기는 27B · 35B 만 지적 — 9B 동률은 볼트 추가 발견)*
> - vs **Qwen3.5-27B**: Wino 0.695 = 0.695(동률) → 6/7.
> - vs **Qwen3.6-35B-A3B**: HellaSwag 0.706 < 0.751 · PIQA 0.784 < 0.803 → 5/7.
>
> 과장은 헤드라인에, 반증은 같은 카드의 표에 있다 — [[DavidAU]] 엔티티에 09월부터 기록된 패턴 그대로다([[표-부분인용]]). 과제 7종은 모두 lm-eval 객관식 로그우도 — 추론 · 코딩 능력과 별개이며 자체 측정. 카드 스스로 "27B 를 모든 과제에서 이긴다는 뜻은 아니다"라고 덧붙인다(71행).

## 도메인별 추출 (local-llm)
- **실용성 판단**: 9B · Q4 급이면 소비자 GPU 한 장. MTP 로 속도 이득(카드 수치 · 단일 환경).
- **메모리 아키텍처**: 해당 없음.
- **Hermes 적용**: 보류 — 무검열판을 에이전트 백본으로 쓸 이유가 없고, 도구 호출 · 한국어 성능 근거가 없다.
- **트레이드오프**: 거부 6/100 vs KL 0.0793(원본 대비 분포 변화가 작지 않다).
- **오픈소스 구현체**: GGUF 직접 구동.

## 관련 페이지
- [[DavidAU]] · [[heretic]] · [[표-부분인용]] · [[Qwen3.6-35B-A3B-MTP-GGUF]] · [[Qwen3.8-Flash-Next-GSQ-RCO-abliterated-GGUF]] · [[Qwen]] · [[파생저장소-식별]]

## 원본
- 출처: https://huggingface.co/DavidAU/Qwen3.5-9B-The-Defiant-Fable-Uncensored-Heretic-NEO-IMATRIX-MAX-MTP-GGUF
- 확인 범위: HF API 메타 · 카드 raw(152,867B) 49 · 71 · 86–118 · 144 · 262–263행 직접 판독 · 🔴 실행 미확인
- 신뢰도: ⭐⭐ (dl30 213만 · 자체 측정 · 헤드라인 과장)
