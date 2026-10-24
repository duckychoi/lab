---
title: "OpenDS-World — '모델 39.0% > 인간 21.1%'는 1회 시도끼리 비교다. 인간 5명 중 1명이라도 맞힌 비율은 57.5%다"
type: source
domain: ai-news
tags: [ai-news, hf-paper, benchmark, deep-search, web-agent, live-web, 인간대조, llm-judge, 비매칭비교, 규약15]
created: 2026-10-24
updated: 2026-10-24
sources: []
reliability: high
---

# Deep Search in Real-World Web Environments (OpenDS / OpenDS-World)

**arXiv**: 2610.30181 · **HF**: https://huggingface.co/papers/2610.30181
**업보트**: **152** (수집기 152 **일치**) · HF 데일리 10-23 목록 **3위 — 미확정**(규약 ⑮)
**날짜**: `publishedAt` **2026-10-19** · `submittedOnDailyAt` 2026-10-23 → [[게시일-이중화]] **4일**
**저자**: 25인 · HF `organization` **없음**
**코드**: https://github.com/Yu-xm/OpenDS (★23 · Apache-2.0 · Python · `src/` `toolbox/` `evaluation.yaml` 실존 · 레포 생성 2026-08-17 = arXiv 2개월 전)
**신뢰도**: ⭐⭐⭐⭐

> [!insight] 핵심 인사이트 — 초록의 "모델 > 인간"은 조건이 다른 두 숫자의 병치다
> 초록: *"The best-performing model achieves **39.0%** accuracy, while human evaluation across **1,000 independent attempts** yields **21.1%**."*
> 볼트가 arXiv HTML(485,435B) §2.3 을 열어 조건을 맞췄다:
>
> | 조건 | 인간 | 모델 |
> |---|---|---|
> | 시도 단위 | 50명 · 과제당 **5명** · 1인 20과제 (총 1,000시도) | 모델당 과제당 **1회**(200시도) |
> | 시간 | **제한 없음** · *"voluntarily terminates"* · 평균 **38.8분/시도** | **3,600초** + **100 tool call** |
> | 도구 | 일반 브라우저 · **LLM 도구 금지** | 검색(텍스트·이미지·영상) + GUI + 영상 프레임·자막 추출 |
> | 채점 | **사람이 수작업 확인** | **LLM 판정자 Qwen3.8-27B**(의미 동치) |
>
> 🏆 **같은 데이터의 과제 단위 집계**: 5명 중 **1명 이상 정답 115/200 = 57.5%**. ⇒ 🎯 **"인간 집단"은 최고 모델(39.0%)을 18.5pp 앞선다**(🔴 이쪽은 반대로 5인 vs 1회 비대칭 — 공정한 짝은 12모델 합집합인데 본문에서 못 찾았다). 21.1% 는 *"무작위 한 사람의 한 번 시도"* 이고, 39.0% 는 *"최고 모델의 한 번 시도"* 다.
> ⚖️ 그리고 **12개 모델 평균은 25.0%** (볼트 계산: Table 1 Overall 합 300.0 ÷ 12) — 인간 1회 시도 21.1% 는 **평균 모델과 비슷한 수준**이다. "모델이 인간을 넘었다"는 **최고 모델 1개**의 이야기다.
> → [[비매칭-비교]] · 신설 [[인간-기준선-조건]].

> [!warning] 🔴 채점자가 다르다 — 인간은 사람이, 모델은 27B 모델이 채점했다
> *"All final answers submitted by the solvers are **manually checked**"* vs *"We use **Qwen3.8-27B** as the LLM judge"*. ⇒ **두 정확도는 서로 다른 계측기로 잰 값이다.** LLM 판정자가 관대하면 모델 쪽이, 엄격하면 인간 쪽이 유리하다 — 방향은 본문에서 판정 불가(판정자–사람 일치도 미열람) → [[측정도구-먼저-반증]] · [[요약자와-판정자-분리]].
> 🔴 추가: *"if any issue that affects normal solving is identified, the corresponding instance is recorded and jointly reviewed and **revised after the testing is completed**"* ⇒ **인간은 수정 전 문항을, 모델은 수정 후 문항을 풀었을 수 있다.** 수정 건수는 미확인.

> [!insight] 🏆 난이도 등급이 "인간 정답자 수"로 정의돼 있다 — 그래서 High 등급은 인간 0% 가 정의상 고정이다
> Low(2~5명 정답) **54** · Medium(정확히 1명) **61** · High(0명) **85** 과제. 볼트 검산: 1+25+17+11 = 54 ✅.
> **High 85과제(인간 전원 실패)에서**: Gemini 3.8 Flash **28.24%**(24) · Claude Opus 5.5 25.88%(22) · GPT-6 Astra 24.71%(21).
> ⇒ 🎯 **진짜로 "인간이 못 한 것을 모델이 한" 증거는 이 85과제 중 약 1/4이다.** 이것이 초록의 39.0 vs 21.1 보다 훨씬 강하고 정직한 주장인데, 초록에는 없다 → [[표-부분인용]](이번엔 초록이 **더 약한** 버전을 골랐다).
> ⚖️ 역으로 **Low 등급(인간 2명+ 정답)에서도 최고 모델은 59.26%** — 인간 다수가 푼 문제의 40%를 놓친다. **능력 축이 다르다**는 [[HyperBrowseComp]] 결론(동점·다른 문항)과 같은 방향.

## 모델 결과 (Table 1 Overall · 200과제)
GPT-6 Astra **39.0** · Claude Opus 5.5 **38.0** · Gemini 3.8 Flash 36.5 · Claude Fable 5.1 33.5 · GPT-5.6 Sol 28.0 · Qwen3.8-Max 25.5 · GLM-5.3-Flash 23.5 · DeepSeek-V4.1-Flash 20.5 · Kimi K3 17.5 · GLM-5.3(T) 13.5 · DeepSeek-V4-Pro(T) 12.5 · Qwen3.8-Flash 12.0 · (T)=텍스트 전용

> [!insight] 📌 비용 축 — 1위와 2위의 차이는 1pp, 예산 소진율은 9pp
> - **예산 한계 도달률**: Claude Opus 5.5 **16.5%** · GPT-5.6 Sol 22.0% · GPT-6 Astra 25.5% … Qwen3.8-Flash **81.5%** · DeepSeek-V4.1-Flash 78.0%.
> - GPT-6 Astra 51.05 call · **18.66분**/과제 vs GPT-5.6 Sol 52.42 call · **8.99분** — 같은 호출 수, 2배 시간.
> - 총 토큰(M): GPT-6 Astra **187** · Claude Opus 5.5 339 · Gemini 3.8 Flash **976** (1위 대비 5.2배 토큰으로 −2.5pp).
> ⇒ 🎯 **저예산 모델의 낮은 점수 상당분은 "못 찾음"이 아니라 "예산 소진 후 강제 종료"다.** 1시간·100콜 한도를 바꾸면 순위가 바뀔 수 있다 → [[임계-의존-성공률]] · [[하네스-설계-축]].

## 도메인별 추출 (ai-news 템플릿)

- **신뢰도**: ⭐⭐⭐⭐ — 업보트 152 · 25인 · **코드 실존**(Apache-2.0, `src/`·`toolbox/`·평가 yaml) · 인간 1,000시도(646시간) 실측 · 과제당 787 증거 엔트리·42 포맷·7 접근유형 주석. 🔴 감점: 판정자 비대칭.
- **즉시 활용**: **부분 YES** — 볼트의 웹 읽기 경로([[Agent-Reach]] · `mark-clean` 스킬)를 재는 척도로 쓸 수 있다. 특히 *"67.0% 링크 탐색 · 60.0% 아티팩트 전송(다운로드 후 검사) · 47.5% 시간 색인(영상 내 위치)"* — **텍스트 추출만 하는 경로는 과제 절반 이상에서 구조적으로 실패한다**는 예측이 가능하다.
- **6개월 영향력**: 딥서치 평가가 **정적 코퍼스 → 라이브 웹**으로 이동. 🔴 단 라이브 웹은 **시간이 지나면 정답 경로가 썩는다**(페이지 삭제·변경). 저자는 **입력 영상만 아카이브**했다(*"videos… are archived and distributed with the benchmark"*) — 웹 증거 쪽 부패 대응은 미확인.
- **대체 관계**: [[DeepSearch-World]](결정론적 환경 420K QA) 의 반대편 — 그쪽은 재현성을, 이쪽은 현실성을 택했다. [[HyperBrowseComp]] · [[DR3-Eval]] · [[K-BrowseComp]] 와 같은 계열.
- **허와 실**: 마케팅 문장(*"모델이 인간을 넘었다"*)을 걷어내면 → **최고 모델 1회 39.0% < 인간 5인 집단 57.5%**, 그리고 **인간 전원 실패 과제의 약 25%를 상위 모델이 푼다.** 둘 다 사실이고, 후자가 이 논문의 진짜 결과다.
- **액션**: 아래.

> [!action] 당장 할 것
> 1. **(중간)** `Yu-xm/OpenDS` 의 과제 샘플 몇 개를 볼트 웹 읽기 경로로 돌려 **"아티팩트 전송·시간 색인" 유형에서 실패하는지** 확인 — 볼트 도구 한계를 수치화하는 가장 싼 방법.
> 2. **(낮음)** 부록 C.4 판정 프롬프트 + 판정자–사람 일치도 존재 여부 확인(미열람).

> [!question] 미해결
> - 인간 참여자 50명의 **자격·배경**: 감사 목록에 이름만 있고, 본문 검색으로 전문성 기준을 **찾지 못했다**. [[HyperBrowseComp]] 는 주석자 자격(플랫폼 테스트 90점 초과)을 적었다.
> - 12개 모델 **합집합 정답률**(모델 "집단")은 본문에서 찾지 못했다 — 인간 집단 57.5% 와 짝 비교가 되려면 이 값이 필요하다.

## 관련 페이지
- [[인간-기준선-조건]] 🆕 · [[비매칭-비교]] · [[측정도구-먼저-반증]] · [[요약자와-판정자-분리]] · [[표-부분인용]] · [[임계-의존-성공률]] · [[하네스-설계-축]] · [[에이전트-웹접근]] · [[게시일-이중화]]
- [[HyperBrowseComp]] · [[RoTA-Bench]] — 인간 기준선 동형 사례
- [[DeepSearch-World]] · [[DR3-Eval]] · [[K-BrowseComp]] · [[SearchJev]]
- [[OpenAI]] · [[Anthropic]] · [[Google]] · [[Qwen]] · [[DeepSeek]] · [[Moonshot AI]] · [[Zhipu-AI]] — 평가 대상 벤더
- [[Qwen3.8-27B]] — 판정자로 쓰인 모델
- [[WeVisOne-VL]] · [[FAPL]] · [[LayerEditor]] · [[IQuest-Q1]] — 같은 배치
- [[ai-news]]

## 원본
- 출처: https://huggingface.co/papers/2610.30181 (arXiv 2610.30181)
- 열어 본 것: HF papers API · **arXiv HTML v1 전문**(§2.3 인간 평가 · Table 1 · §3.3 비용 · §3.6 예산 · 판정 설정) · GitHub API(repo·contents·license)
- 관측: 2026-10-24T09:06Z (18:06 KST)
- 신뢰도: ⭐⭐⭐⭐
