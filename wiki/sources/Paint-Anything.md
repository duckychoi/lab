---
title: "Paint-Anything — HEX 색 지정 생성·편집, '+85.3%'의 절대값은 37.02 → 68.58이다"
type: source
domain: ai-news
tags: [ai-news, hf-paper, image-generation, image-editing, color-control, flux, bytedance-seed, 단위-불일치, 게시일-이중화]
created: 2026-09-22
updated: 2026-09-22
sources: []
reliability: medium
---

# Paint-Anything (ByteDance Seed)

> [!insight] 🎯 핵심 인사이트 — **HEX 문자열을 그냥 프롬프트에 쓰면 베이스 모델은 색을 반쯤 잃는다. 학습이 그 간극을 메운다**
> Table 1 원문: CompColor에서 FLUX.2-4B의 색 이름 → **HEX 문자열 치환 시 평균 0.72 → 0.38**(거의 반토막). 파인튜닝 후 HEX 평균 **0.79**, 색 이름 평균도 0.72 → **0.79**.
> 🎯 **"LLM 텍스트 인코더가 HEX를 이해한다"는 전제는 절반만 참이다** — 인코더는 연관을 갖고 있어도 생성기는 그걸 색으로 못 옮긴다. 객체 단위 HEX 감독(Paint-500K)과 **고노이즈 타임스텝에서만 쓰는 순색 앵커**가 그 연결을 만든다.
> 📌 크리에이터 도구 관점([[video-saas]] 교차): 브랜드 컬러 `#RRGGBB` 를 프롬프트에 그대로 넣는 인터페이스는 **학습 없이는 신뢰할 수 없다**는 정량 근거다.

> [!warning] 🔴 **수집기 정정 — "arXiv HTML 미제공"은 v1 기준이다. v2는 HTML이 있다**
> 수집기 raw: *"arXiv HTML 미제공 → 목차 확인 불가"*.
> 🔴 arXiv 제출 이력: **v1 2026-09-17 17:59 UTC · v2 2026-09-20 00:16 UTC**, v2 코멘트 원문 *"**HTML compatibility fixes**; scientific content unchanged"*. 볼트 실측: `arxiv.org/html/2609.20816v1` → **404**, `.../html/2609.20816`(=v2) → **200**.
> 🎯 **수집(09-21) 하루 전에 이미 HTML이 올라와 있었다.** 수집기는 v1 링크를 봤거나 캐시를 봤다 — 확인 불가. → [[게시일-이중화]]: 버전이 바뀌면 *열람 가능성*도 바뀐다.

> [!note] 📌 절대 점수 복원 — 초록의 상대값이 맞다 ✅ (Table 1, 볼트 계산)
> | | FLUX.2-4B 베이스 | + Paint-Anything | Δ | 상대 |
> |---|---|---|---|---|
> | ACBench-T2I Overall | 37.02 | **68.58** | +31.56 | **+85.3%** ✅ |
> | ㄴ Single / Two | 37.45 / 36.60 | 72.67 / 64.49 | +35.2 / +27.9 | |
> | ACBench-Edit | 58.90 | **75.57** | +16.67 | **+28.3%** ✅ |
> | CompColor 평균(색 이름) | 0.72 | 0.79 | | |
> 비교: **FLUX.2-dev(56B) 51.70 / 68.87**, 최강 특화 베이스라인 ColorWave(볼트 재현) 46.54 · ColorBind/Edit 60.38. Z-Image Base에도 같은 레시피 → 33.45 → **53.77**.
> 🔴 수집기 누락: 초록 마지막 문장 *"highest average CompColor score among the compared methods"* — **자체 벤치가 아닌 외부 벤치 주장**이 하나 있었다.

> [!warning] ⚠️ **"4B"는 4B가 아니다 — 그리고 만점 허용오차가 넓다**
> 1. 본문 각주 원문: *"The '4B' and '9B' suffixes refer to the **DiT parameter count**; the Total params. column reports the total parameter count, **including the bundled Qwen3 text encoder**."* → 표의 FLUX.2-4B는 **8B**. §4.3 헤드라인 *"an **8B** model outperform a **56B** model"* 은 총 파라미터 기준이다. 저자가 직접 밝혔으므로 기만은 아니나, 이름(4B)과 비교 단위(8B)가 다르다 → [[단위-불일치]].
> 2. 점수식(식 5): 채널 평균 **MAE ≤ 16 이면 100점**, 64 이상 0점. **"24비트 임의 색"을 말하지만 채점은 채널당 ±16/255(≈6%)까지 정답**으로 친다. 저자 설명: *"allowing natural appearance variation"*(그림자·조명). 합리적 설계지만 **"정확한 HEX 재현"으로 읽으면 과대**다 → [[한정어-탈락]] 주의.
> 3. **ACBench는 저자 자체 제작**(T2I 1,000 + Edit 500). ✅ 보완: 외부 프로토콜 2종(CompColor 공식 평가기 무수정, GenColorBench NCU 34.00 → **57.89**)도 돌렸다.

> [!note] ✅ 불리한 수치도 적었다
> - **객체 로컬라이즈 실패율 Paint-Anything 5.50%(33/600) — 비교 모델 중 최고**(FLUX.2-4B 4.17%). 실패 제외 시 68.58 → 70.93, 순위 불변.
> - 사용자 연구(15명×80프롬프트=1,200판정): 색 선호 55% / 동률 32% / 패 13%. 그러나 **화질은 승 22% / 동률 58% / 패 20%** — **색은 좋아지고 화질은 그대로**. 원문: *"do not establish per-sample metric-human agreement or image-quality equivalence."*
> - 학습/평가 분리(부록 L): 정규화 후 프롬프트 **완전일치 0건**. 단 **정확 문자열 일치만** 검사.

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐⭐ — ByteDance Seed 기술보고서(29쪽) · 업보트 30 · 저자 5. 🔴 **코드·가중치·데이터·프로젝트 페이지 없음**(HF API `githubRepo`·`projectPage` null, 본문에도 공개 약속 문장 없음) → 재현 불가.
- **즉시 활용**: **NO** — 가중치 미공개. 방법론만 가져갈 수 있다(순색 앵커를 고노이즈 구간에만 섞는 트릭, 4 GPU·4,000 스텝·배치 72·lr 2e-5).
- **6개월 영향력**: 브랜드 컬러 지정이 "프롬프트 한 줄"이 되는 방향. FLUX.2-klein 계열 LoRA로 누군가 재현할 가능성이 높다.
- **대체 관계**: ColorBind·ColorPeel·ColorWave 류 전용 파이프라인을 **프롬프트 네이티브 인터페이스**로 대체하는 주장.
- **허와 실**: 실 = 절대 +31.6점(T2I)·외부 벤치 2종 동반. 허 = "4B"(실제 8B), "정확한 HEX"(실제 ±16 허용).
- **액션**: 없음(가중치 대기).

> [!question] 미해결 질문
> 1. 가중치·Paint-500K 공개 계획 — 논문에 언급 없음.
> 2. MAE 허용오차를 8로 좁히면 격차가 유지되나? — 부록 H에 대안 통계가 있으나 볼트 미전사.

## 관련 페이지
- [[ByteDance]]
- [[단위-불일치]]
- [[한정어-탈락]]
- [[게시일-이중화]]
- [[video-saas]]
- [[ai-news]]

## 원본
- 출처: https://huggingface.co/papers/2609.20816 · https://arxiv.org/abs/2609.20816 · HTML https://arxiv.org/html/2609.20816v2
- 볼트 실측(2026-09-22): HF 업보트 **30**(수집기 23) · 저자 5 · org ByteDance-Seed · publishedAt 09-17 · 데일리 09-21 · githubRepo/projectPage **null** · arXiv v1 09-17 / **v2 09-20(HTML 추가)**
- 수치 출처: arXiv HTML v2 — §4.1~4.3 · Table 1 · 부록 H(Table 9)·K·L · NCU(Table 4)
- raw 대비: 🔴 **"HTML 미제공" 정정(v2 존재)** · ✅ +85.3%/+28.3% 절대값 복원(37.02→68.58, 58.90→75.57) · 🔴 CompColor 외부 벤치 주장 누락 · ⚠️ 4B=8B 총파라미터 · ⚠️ MAE≤16 만점 · ✅ 코드/가중치 없음 확인
- 신뢰도: ⭐⭐ (1차 기술보고서·외부 벤치 병행·불리한 수치 공개 / 가중치·코드·데이터 미공개, 핵심 벤치 자체 제작)
