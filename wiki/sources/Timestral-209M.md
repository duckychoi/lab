---
title: "mistralai/Timestral-209M — 3개 리더보드 1위 주장, 그러나 2위와의 차이는 0.5%이고 123M 과는 0.001이다. 라이선스는 'MIT'가 아니라 월매출 2천만 달러 상한"
type: source
domain: ai-news
tags: [ai-news, hf-model, time-series, forecasting, foundation-model, zero-shot, mistral, gift-eval, fev-bench, chronos, timesfm, license, 시계열]
created: 2026-10-26
updated: 2026-10-26
sources: [https://huggingface.co/mistralai/Timestral-209M]
reliability: medium
---

# mistralai/Timestral-209M

**HF**: https://huggingface.co/mistralai/Timestral-209M · 제작 Mistral AI(볼트 기존 페이지 [[Mistral-Medium-3.5-128B]] 와 같은 조직) · 코드 https://github.com/mistralai/timestral (★**886** · fork 71 · **Apache-2.0** · 2026-10-15 생성)
**실측(2026-10-26T09:08Z · HF API)**: downloads(30일) **9,765** = all-time **9,765**(수집기 일치 · 드리프트 0) · likes **379** · createdAt **2026-10-14** · `library_name: timestral` · `pipeline_tag: time-series-forecasting` · `license: other` · 파일 6개
**도메인**: `ai-news` — 볼트의 시계열 계보([[시계열-예측-파운데이션-모델]] · [[TimesFM]] · [[timesfm-3.0-pytorch]] · [[Kronos]])가 전부 `ai-news` 이고, `local-llm` 템플릿(Hermes 적용·메모리 아키텍처)은 언어모델·에이전트용이라 질문이 성립하지 않는다. CPU 추론 가능(카드) 이라는 점만 local-llm 과 겹친다.
**신뢰도**: ⭐⭐⭐ (대형 벤더 · 공개 리더보드 3종 명시 · 재현 코드 공개 / 단 `model-index` 전부 `verified: False` · 기술보고서 *"coming soon"*)

> [!insight] 🏆 핵심 인사이트 ① — **이 개념 페이지가 2회 이월한 "TimesFM-3 벤치 수치"가 경쟁사 카드에서 처음 들어왔다**
> Timestral 카드 비교표(텍스트 · 이미지 봉인 아님 ✅):
>
> | 벤치 | 지표 | **Timestral-209M** | t0-gamma | TimesFM-3 | Toto-2.0-2.5B | Chronos-2 |
> |---|---|--:|--:|--:|--:|--:|
> | GIFT-Eval | MASE↓ | **0.658** | 0.661 | 0.667 | 0.696 | 0.698 |
> | | CRPS↓ | **0.446** | 0.452 | 0.456 | 0.476 | 0.485 |
> | TIME | MASE↓ | **0.626** | 0.637 | 0.640 | 0.642 | 0.662 |
> | | CRPS↓ | **0.522** | 0.534 | 0.536 | 0.539 | 0.556 |
> | fev-bench | SQL skill↑ | **50.39** | 49.42 | 48.99 | 44.42 | 47.28 |
> | | MASE skill↑ | **39.49** | 37.99 | 37.82 | 32.54 | 35.50 |
>
> ⇒ 수집기 수치 6개 **전부 일치**. 🎯 **경쟁 모델과 비교한다**(수집기 요청 확인): t0-gamma · TimesFM-3 · Toto-2.0-2.5B · Chronos-2. **Moirai 는 표에 없다.**
> ⚖️ 단 **TimesFM-3 수치는 Google 이 아니라 Mistral 이 적은 것**이다 — 출처가 리더보드라고만 적혀 있고 셀별 측정 주체는 불명 → [[비매칭-비교]] 주의. 볼트는 리더보드 원값을 **열람하지 않았다.**

> [!insight] 🏆 핵심 인사이트 ② — **"SOTA"의 마진이 사이즈 사다리의 마진보다 작다**
> - 2위 대비: GIFT-Eval MASE **0.003(0.5%)** · CRPS 0.006(1.3%) · TIME MASE 0.011(1.7%) · fev SQL +0.97p. **CI·시드 분산 미보고.**
> - 🔴 **패밀리 내부**: 123M → 209M 은 GIFT MASE **0.659 → 0.658(0.001)** · fev SQL 50.18 → 50.39 — **파라미터 1.7배에 차이 0.1~0.2%**. 123M 만으로 이미 t0-gamma(0.661) 를 앞선다.
> - 28M(GIFT MASE 0.678)은 TimesFM-3(0.667)·Chronos-2(0.698) 사이 ⇒ 🎯 **실무 선택은 209M 이 아니라 123M 또는 28M** — [[시계열-예측-파운데이션-모델]] 의 *"작게 만들어 어디에나 꽂는다"* 를 Mistral 자신의 표가 뒷받침한다.
> ⇒ "SOTA"는 순위로는 참이지만 **차이가 구별 가능한지는 카드로 판정 불가.** [[유의성-자기제한]] 부재.

> [!warning] 🔴 "Modified MIT" 는 MIT 가 아니다 (LICENSE 전문 실측 1,695B)
> 조항 2: *"You are not authorized to exercise any rights under this license if the **global consolidated monthly revenue** of your company (or that of your employer) **exceeds $20 million** … for the preceding month."* — **파생·결합 저작물에도 적용**, 초과 시 Mistral 상업 라이선스(재량) 필요.
> ⇒ **월 2천만 달러(연 약 2.4억 달러) 미만 조직은 사실상 MIT 와 동일하게 상업 이용 가능.** 개인·소규모 SaaS 에는 제약 아님.
> 📌 **2층 라이선스 함정의 반대 부호 사례**: [[timesfm-3.0-pytorch]] 는 코드 Apache-2.0 / 가중치 **비상업**이었고, Timestral 은 코드 **Apache-2.0** / 가중치 **매출상한부 MIT**. 같은 개념 페이지의 라이선스 표에 TimesFM(🔴)·Timestral(🟡)·Chronos-2(🟢 apache-2.0 실측) 3칸이 채워진다.
> `license: other` 필드만 보면 이 차이가 안 보인다 → [[파생표기-함정]].

> [!warning] 기타 주의
> - **채택 규모 격차**: 같은 계수 규칙(`timestral`·`chronos-forecasting` 둘 다 `model-libraries.ts` 에 countDownloads 미지정 ⇒ 기본 `config.json` 1회 — 볼트 확인)에서 `amazon/chronos-2` 30일 **13,395,742**(all-time 1.9억) · `google/timesfm-3.0-pytorch` 30일 **867,414** ↔ Timestral 4종 합 **24,972**. 공개 12일차이므로 사용량 판정은 보류(볼트 규칙 *"최소 2주, 전 세대와의 상대비"*).
> - 패밀리 실측: 5M **5,401**(♥74) · 28M **6,540**(♥40) · 123M **3,266**(♥42) · 209M **9,765**(♥379).
> - 수집기의 *"trending 18"* 순위는 API 로 검증 불가(API 는 `trendingScore` **224** 만 제공).
> - 21 분위수 · 컨텍스트 32,768 · 호라이즌 1,024 · 24층/768차원 · 패치 32 — **config.json 과 일치**(`context_length` 32768 · `d_model` 768 · `block_schedule` 24개 · `quantile_knots` 21개). 수집기 클레임 전부 확인. 추가 확인: 24층 중 **6개가 time_variate(변량 어텐션)**, 나머지 18개는 time 전용.

## 도메인별 추출 (ai-news)
- **신뢰도**: HF dl 9,765 · ♥379 · GitHub ★886 · 논문 **없음**(기술보고서 예정) · 벤치는 공개 리더보드 3종이나 `verified: False`.
- **즉시 활용**: **YES(조건부)** — `pip install git+https://github.com/mistralai/timestral.git` + CPU 추론. 다변량·공변량(과거 전용/미래 기지)·결측(NaN) 지원이라 SaaS 지표(MAU·매출) 예측에 바로 대입 가능. 사용자는 매출 상한 미만이므로 라이선스 장애 없음.
- **6개월 영향력**: 시계열 FM 시장에 **LLM 벤더(Mistral)가 진입** — 지금까지 볼트 계보는 Google(TimesFM)·Amazon(Chronos)·개인(Kronos). 벤더 경쟁으로 상업 허용 라이선스가 표준화될 가능성(추정).
- **대체 관계**: [[timesfm-3.0-pytorch]](비상업) 를 **상업 용도에서 대체**하는 첫 후보. Chronos-2(Apache-2.0)와는 라이선스 동급 · 표상 정확도 우위(0.658 vs 0.698).
- **허와 실**: "SOTA" = 순위상 참 · 마진은 0.5~1.7% 로 구별 가능성 미확인 · 209M 의 추가 이득은 123M 대비 거의 0.
- **액션**: 자체 지표 1개(예: 일별 영상 조회수)로 Timestral-28M/123M vs Chronos-2 백테스트(MASE) — 코드 실행은 별도 승인 후.

## 관련 페이지
- [[시계열-예측-파운데이션-모델]] · [[TimesFM]] · [[timesfm-3.0-pytorch]] · [[Kronos]]
- [[Mistral-Medium-3.5-128B]] — 같은 제작사 · [[Google]] · [[Amazon]] · [[Salesforce]](GIFT-Eval 주관)
- [[비매칭-비교]] · [[유의성-자기제한]] · [[파생표기-함정]] · [[계수기-배수]]
- [[ai-news]] · [[local-llm]]

## 원본
- 출처: https://huggingface.co/mistralai/Timestral-209M · LICENSE https://huggingface.co/mistralai/Timestral-209M/blob/main/LICENSE · 블로그 https://mistral.ai/news/timestral/ (HTTP 200 · 본문 미열람)
- 볼트 실측(2026-10-26T09:08Z UTC): dl 30d **9,765** / all-time **9,765** / likes **379**
- 신뢰도: ⭐⭐⭐ (HF 다운로드 9,765 · 대형 벤더 · 공개 리더보드 · 자기보고 미검증)
