---
title: "xtools-at/DeepSeek-V4-Pro-Qwen3.5-9B-UNCENSORED-heretic — DeepSeek-V4-Pro 증류 9B 의 검열 제거판. 카드의 벤치는 전부 원본(Jackrong) 수치이고 이 레포가 잰 것은 거부 3/100·KL 0.0422 뿐"
type: source
domain: local-llm
tags: [local-llm, hf-model, distillation, uncensored, heretic, qwen3.5, deepseek, 파생저장소]
created: 2026-11-10
updated: 2026-11-10
sources: [https://huggingface.co/xtools-at/DeepSeek-V4-Pro-Qwen3.5-9B-UNCENSORED-heretic]
reliability: low
---

**HF**: https://huggingface.co/xtools-at/DeepSeek-V4-Pro-Qwen3.5-9B-UNCENSORED-heretic · 다운로드(30일) **11,755** = 누적 11,755 · ♥**1,092** · trendingScore **864** · Apache-2.0 · base `Jackrong/DeepSeek-V4-Pro-Qwen3.5-9B` · `pipeline_tag: text-generation` · 생성 2026-10-30 · 수정 2026-11-08 (HF API 2026-11-10 09:06Z · 수집기 ♥1,091 · 863 대비 +1 드리프트)

## 핵심 인사이트
> [!insight] 벤치 표는 물려받고, 벤치 대상은 바뀌었다
> 원본([[DeepSeek-V4-Pro]] "Max Effect" 응답 약 25만 건으로 Qwen3.5-9B 를 SFT → GSPO 로 가벼운 RL)의 카드 내용이 그대로 복사돼 있다. 이 레포가 직접 잰 것은 [[heretic]] 지표 — **거부 3/100(원본 100/100) · KL 0.0422**(카드 52~53행 볼트 확인) — 뿐이다. **검열 제거 후 가중치로 GSM8K·MMLU-Pro 를 다시 잰 값은 없다.** KL 0.0422 는 같은 날 [[DavidAU-Qwen3.8-27B-TURBO]] 의 Stage 2(0.0025)보다 17배 크다.

> [!warning] 원본 수치의 조건 (카드 대조)
> - **GSM8K 94.50%** = NVFP4 · vLLM · **4회 평균**(141~142 · 165행). 비교 열 DeepSeek-V4-Pro 92.60% · MiMo-V2.5-Pro 99.60% 는 수집기 판독대로 외부 인용치 — **학생이 교사를 넘었다는 그림은 측정 조건이 다른 숫자끼리의 비교**([[비매칭-비교]]).
> - **MMLU-Pro 3과목 평균 90.53% vs Qwen3.5-9B 89.60%(+0.93p)** — 과목당 500문항, 모델당 1,500문항. 1,500문항에서 0.93p 는 약 14문항 차이다(볼트 산술).
> - 정답당 추론 토큰 **3,157 vs 4,938(36.1% 절감)** · "대문자 한 글자만" 형식 준수 97.2% vs 37.3% — 볼트는 3,157 · 4,938 · 36.1% 를 카드에서 검출, 97.2/37.3 은 수집기 판독 기준.
> - **코딩 데이터 0건인데 코딩·툴콜 소폭 개선** — 카드 스스로 "post-training tests indicated a small improvement" 수준의 서술이고 코드 벤치는 없다.

> [!note] 채택 신호의 모양
> ♥1,092 대 30일 다운로드 11,755 = 좋아요 1개당 10.8회. 같은 날 [[DavidAU-Qwen3.8-27B-TURBO]] 는 548회다. 트렌딩 2위는 **관심**이 만든 순위이고 사용량은 아직 작다(생성 11일).

## 도메인별 추출 (local-llm)
- **실용성**: 9B 수학·STEM 추론기. 토큰 효율 주장은 원본 기준. 태그에 `ko` 가 있으나 한국어 평가는 카드에 없음.
- **트레이드오프**: 안전 정렬 제거 → 서비스 투입 부적합. 품질 영향은 KL 한 숫자로만 제시.
- **Hermes 적용**: NO(검열 제거판). 원본 Jackrong 9B/4B 는 수학 라우팅 후보일 수 있으나 볼트 미조회.
- **오픈소스 구현체**: 가중치 공개(safetensors).

## 관련 페이지
- [[DeepSeek-V4-Pro]] · [[heretic]] · [[Qwen3.5-Claude-Distilled]] · [[DavidAU-Qwen3.8-27B-TURBO]] · [[파생저장소-식별]] · [[비매칭-비교]] · [[TwIL-8B]]

## 원본
- 출처: https://huggingface.co/xtools-at/DeepSeek-V4-Pro-Qwen3.5-9B-UNCENSORED-heretic
- 확인 범위: HF API(expand) + 카드 raw 38,579B 표본 대조 · 🔴 원본 Jackrong 레포 미조회 · 추론 미실행
- 신뢰도: ⭐ (dl30 11,755 · 재측정 벤치 0 · 검열 제거 파생)
