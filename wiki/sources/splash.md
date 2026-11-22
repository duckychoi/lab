---
title: "incoai/splash — Apple silicon 전용 로컬 추론 엔진 (DFlash 2 투기적 디코딩 · llama.cpp 대비 2.5–5.3× · 지원 모델 고정 목록)"
type: source
domain: local-llm
tags: [local-llm, github-trending, apple-silicon, metal, speculative-decoding, inference-engine, openai-compatible]
created: 2026-11-22
updated: 2026-11-22
sources: [https://github.com/incoai/splash]
reliability: medium
---

**GitHub**: ★2,613(볼트 API 11-22 · 수집기 일치) · C++ · Apache-2.0 · 생성 2026-09-18 · push 2026-11-17

## 핵심 인사이트
> [!insight] 배수는 비교 상대에 따라 1.3× 에서 5.3× 까지 달라진다 — README 에 표가 둘 있다
> Mac 한 대에서 OpenAI(Chat/Responses/Completions) · Anthropic Messages 호환 서버를 띄우는 엔진. DFlash 2 투기적 디코딩(모델별 draft 자동 선택), 전용 Metal 커널, 프리픽스 캐시 재사용, 동시 요청 자동 배칭, 비전 · 툴콜 · JSON Schema. `splash claude / codex / opencode` 로 코딩 에이전트를 바로 붙인다.

## 도메인별 추출 (local-llm)
- **실용성 판단**: **M3 이상 + macOS 26.4 이상**(README 18행 볼트 확인) · 지원 모델 고정(Qwen3.8-27B · Qwen3.6-35B-A3B · Ornith-1.5-122B · Qwen3.8-Flash-Next · Flint) · 전체 BF16/F16 GGUF 거부. 그 외 환경은 해당 없음.
- **트레이드오프 — 🆕 볼트가 README 표를 직접 판독(수집기는 "열별 기기 구성 미확인")**:
  - 표 1(차순위 엔진 대비 · **M5 Pro 16코어 GPU 48GB** · SPEED-Bench 코딩 프롬프트 · HTTP): decode 35B-A3B 210 tok/s(1.7×) · 27B 74(2.0×) · Flash-Next 95(1.3×). 32K prefill 2,011(1.3×) · 363(1.2×) · 1,312(1.3×). 캐시된 TTFT 123ms(6.6×) · 282ms(7.3×) · 171ms(212×). 4동시 합산 357(2.0×) · 170(3.9×) · 171(2.4×). Flash-Next 열만 M5 Pro 20코어 64GB, 비교 상대는 Strata.
  - 표 2(**같은 Unsloth UD-Q4_K_M 가중치로 llama.cpp 와 직접 비교**): 27B 는 llama.cpp 16/17 · MTP 27/20 vs Splash **74/92** tok/s(M5 Pro / M3 Max) = 4.5–5.3×(MTP 대비 2.7–4.6×). 35B-A3B 는 69/66 vs **175/209** = 2.5–3.2×.
  - 정합성: Splash vs llama.cpp 다음 토큰 일치 99.30–99.45%(27B) · 97.83–98.14%(35B-A3B) — llama.cpp 자체의 CPU vs GPU 일치(97.8% · 96.5–96.9%)와 같은 수준이라는 비교까지 실었다.
- **Hermes 적용**: 서버가 Mac 이 아니면 NO.
- **오픈소스 구현체**: 본 레포(GGUF 커널에 llama.cpp MIT 코드 포함).

> [!warning] 단서
> 전부 README 자체 측정. 표 1 의 "차순위 엔진"이 무엇인지는 README 본문에 이름이 없다(docs/performance.md 미열람). 수집기가 인용한 "1.3–2.0배"는 표 1, 더 큰 배수는 표 2 — 둘을 섞어 "최대 5.3배"로만 전하면 [[배수-조건분산]] 이다.

## 관련 페이지
- [[MMFlash]] (투기적 디코딩) · [[omlx]] · [[jan]] · [[Qwen3.8-27B]] · [[Qwen3.8-Flash-Next]] · [[unsloth]] · [[배수-조건분산]] · [[local-llm]]

## 원본
- 출처: https://github.com/incoai/splash
- 확인 범위: GitHub API · README 원문(9,127B) 138–175행 표 2개 직접 판독 · 🔴 docs/performance.md 미열람 · 실행 0(볼트 환경은 Mac 아님)
- 신뢰도: ⭐⭐⭐
