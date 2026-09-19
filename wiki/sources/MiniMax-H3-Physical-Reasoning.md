---
title: "MiniMax-H3 물리세계 추론 평가 — 벤더가 0개 낸 숫자를 제3자가 처음 냈다: 41.97%"
type: source
domain: ai-news
tags: [ai-news, video-saas, hf-paper, evaluation, omni-modal, video-generation, audio-video, physical-reasoning, third-party-eval, minimax]
created: 2026-09-19
updated: 2026-09-19
sources: [MiniMax-H3.md]
reliability: low
---

# Can MiniMax-H3 Reason About the Physical World? (arXiv 2609.18323)

> [!insight] 핵심 인사이트 — **벤더 수치 vs 제3자 수치 대조의 결과: 대조할 벤더 수치가 없다**
> 볼트 [[MiniMax-H3]] 페이지는 08-06 이후 **여러 회차 연속**(08-29에 "네 번째 회차", 09-06 재확인) *"모델카드 공개 벤치 0건"* 을 기록했다. 09-19 카드 원문(38,406바이트)을 다시 검색해도 **정량 벤치 표·점수·Elo·승률이 0건**이다(카드의 수치는 스펙뿐 — 33B · 4~15초 · 24FPS · 768p · 11개 언어 등).
> → 🎯 **이 논문의 41.97%는 H3에 대한 볼트 최초의 성능 측정치이자, 유일한 측정치다.** "벤더 주장 대비 몇 점 낮다"가 아니라 **"벤더가 주장하지 않은 영역을 제3자가 처음 쟀다"** 가 정확한 서술이다.
> 📌 그래서 이 수치는 **비교 기준이 없다** — 평가 대상이 H3 **단일 모델**이고 다른 옴니 모델·비디오 모델 결과가 표에 없다. **41.97%가 좋은지 나쁜지는 이 논문만으로 판정할 수 없다**(수집기 🔴 한정 ✅ 유지).

> [!insight] 표 2 전량 — 4시나리오 29하위범주 (사람 평가 성공률, N 가중)
> ```
> MSR 다시점 공간(200)        VDR 영상 의사결정(100)     ADR 오디오 모호성해소(146)   AVIR 시청각 통합(71)
> Deformation   34  41.20    Humans     34  55.88       Vocalizations 16  31.30     Activities 14  57.14
> Cleaning      27  33.30    Cartoons    5  20.00       Alerts        26  23.10     Animation   6  33.33
> Articulation  26  34.60    Animals    11  63.64       Music         16  25.00     Making     21  52.38
> Arrangement   23  47.80    Traffic     9 100.00       Machinery     34  17.60     Animals    10  30.00
> Transport     23  34.80    Physics    10  50.00       Contact       32  21.90     Cues       20  50.00
> Loading       20  50.00    Memory      6  66.67       Nature        22  54.50
> Assembly      20  50.00    Puzzles     6  16.67
> Pouring       12  58.30    Synthetic  19  52.63
> Threading      8  75.00
> Control        7  42.90
> 합계         200  43.50    합계      100  56.00       합계         146  27.40     합계       71  47.89
> ```
> ✅ 볼트 재계산: 87 + 56 + 40 + 34 = **217 / 517 = 41.97%** 일치.
> 🎯 **최저는 오디오 → 기계음(Machinery 17.60%) · 접촉음(Contact 21.90%) · 경보음(Alerts 23.10%)**. H3 카드가 강조하는 축이 *"오디오-영상 동기 생성"* 인데, **소리를 증거로 받아 맞는 사건을 그리는 능력은 5건 중 1건 수준**이다. 🔴 단 이건 **생성 능력이 아니라 오디오 → 사건 추론 능력**이다 — 동기화 품질 자체를 잰 게 아니다.
> 🔴 **작은 N 주의**: Traffic **100%는 9건**, Cartoons 20%는 **5건**, Memory·Puzzles는 **6건**. 하위범주 수치를 개별 인용하면 [[표-부분인용]] 의 표본 축 오류가 된다.

> [!warning] 🔴 저자 스스로 달아 둔 한정 — 수집기 요약에서 빠졌다
> - 시나리오 간 비교 금지: *"since the scenarios differ in data, prompts, and generation targets, the results mainly reflect task-level performance **rather than a direct comparison between video and audio modalities**."* → **"영상이 최고·오디오가 최저"를 "H3는 오디오를 못 쓴다"로 옮기면 저자 한정어를 떨어뜨린 것**이다 → [[한정어-탈락]]
> - 실패 원인 분리 불가: *"A failed output may arise from incorrect input understanding, weak cross-modal integration, or errors during video generation."* 모달리티 제거 등 **통제 실험은 하지 않았다**(향후 과제로만 언급).

## 🔴 이 평가 자체의 약점 — 본문·레포에서 확인
1. **어떤 H3를 돌렸는지 적혀 있지 않다.** 오픈 가중치 로컬 실행인지, **H3-Context-IR(전처리)·2K 재생성이 붙은 공식 API**인지 본문에 없다(`API|Context-IR|768|2K` 0히트). 볼트 [[MiniMax-H3]] 페이지가 확인했듯 카드는 Context-IR을 *"critical to the quality of the final output"* 이라 하고 **오픈 릴리스에서 뺐다.** 🎯 **어느 쪽이냐에 따라 41.97%의 의미가 달라진다** — 오픈 가중치라면 "공식 시스템보다 낮게 잰 값", API라면 "공식 시스템 값".
2. **평가자 간 일치도가 없다** — 전문가 3명이 독립 평가 후 *"cross-check"* 했다고만 적었다. κ 등 **일치도 수치 0건**. 인스턴스당 생성 횟수·시드도 미기재.
3. **데이터가 아직 없다** — README TODO: *"Open-source the evaluation dataset — TODO"*. HF 데이터셋 `gulucaptain/MiniMax-H3-Reason` 은 **수동 승인 게이트**이고 카드 원문: *"Actual evaluation inputs and prompts **have not yet been populated** here."* → **재현 불가.**
4. **레포와 논문이 MSR 입력을 다르게 적는다** — 논문: *"Given K images … captured from different viewpoints"*(다시점). README·데이터셋 카드: MSR = **"Single image" / "One image"**. 🔴 볼트는 어느 쪽이 맞는지 판정 불가.
5. **인스턴스 검증 문장이 모호하다** — *"Each condition-prompt pair is verified to support the intended inference through video generation **for MiniMax-H3**."* H3로 돌려 보고 쌍을 다듬었다는 뜻이면 **평가셋이 H3에 맞춰졌을 가능성**이 있다(볼트 해석, 확인 불가).
6. **입력 일부를 경쟁사 생성기로 만들었다** — 합성 영상 **[[Seedance]] 2.0**([[ByteDance]]) · 합성 음성 ChatGPT Voice. 저자 소속에는 **[[Tencent]]**(교신 포함)가 있고 다시점 데이터 출처에 **Hy-Embodied-0.5-VLA-Data**(Tencent)가 있다. 🎯 **MiniMax와는 독립이지만 경쟁 영상 벤더가 없는 평가는 아니다.** 편향 증거는 없다 — 기록만 한다.

## 벤더 ↔ 제3자 대조표 (볼트 작성)
| 항목 | 벤더(MiniMax 모델카드, 09-19 실측) | 제3자(이 논문) |
|---|---|---|
| 정량 성능 | **0건** | 517건 사람 평가 · SR 41.97% |
| 멀티모달 입력 | 이미지 ≤9 · 영상 ≤3 · 오디오 ≤3(합 ≤15초, 파일 ≤12) — **지원 범위** | 지원 ≠ 활용: *"accepting multiple modalities is not equivalent to reasoning across them"* |
| 오디오 | 32kHz 스테레오 동기 생성 · 11개 언어 대사 | 오디오 → 사건 추론 **27.40%**(최저 시나리오) |
| 물리성 | 주장 없음 | 실패 유형 4종: 증거 접지 오류 · 사건 미실현 · **물리/형상 위반** · 시간 상태 불일치 |
| 품질 핵심 모듈 | Context-IR **오픈 미포함**(API) | 어느 경로로 돌렸는지 **미기재** |
🎯 **두 문서는 서로 다른 질문에 답한다** — 벤더는 "무엇을 받을 수 있나", 제3자는 "받은 것을 쓰나". 볼트가 [[MiniMax-H3]] 에서 반복한 *"다운로드는 품질 근거가 아니다"* 에 **처음으로 반대편 증거(측정치)** 가 생겼다.

## 도메인별 추출 (ai-news · 교차 video-saas)
- **신뢰도**: HF 업보트 **66** · 저자 **13명**(NUS 다수 · Fudan · Tencent; Shuicheng Yan 등) · org 필드 None · GitHub `gulucaptain/MiniMax-H3-Reason` **★21**(파일 37개 = README·개요 이미지·**성공 사례 영상/미리보기**) · 데이터셋 미공개. 🔴 **일치도 없음 · 재현 불가 · 실행 경로 미기재 · 단일 모델** → reliability **low**. (방향성 — "지원 ≠ 활용" — 은 설득력 있다.)
- **즉시 활용**: 🎯 **YES (video-saas) — 평가 설계를 가져온다.** "프롬프트에서 핵심 정보를 빼고 입력 모달리티에 분산시킨다"는 **암묵 프롬프트(implicit prompt)** 설계는 내 [[video-saas]] 파이프라인에서 **레퍼런스 입력을 실제로 쓰는지** 점검하는 테스트로 그대로 쓸 수 있다(예: 오디오 참조를 넣고 프롬프트에는 사건을 적지 않기).
- **6개월 영향력**: **중간.** 옴니 생성 모델 평가가 "시킨 걸 그리나(VBench류)"에서 **"뭘 그려야 할지 추론하나"** 로 옮겨가는 초기 사례. 저자가 DeepSeek 기반 **자동 평가 파이프라인**을 예고했다(README) — 나오면 다른 모델 비교가 가능해진다.
- **대체 관계**: VBench·WorldModelBench·VideoPhy를 대체하지 않고 **입력 축(T+I+A+V, 암묵 프롬프트)** 을 보완한다(표 1).
- **허와 실**: ✅ 실: 벤더 외 첫 정량치 · 저자 스스로 시나리오 간 비교 금지 한정 · 실패 사례 공개. ❌ 허: "H3의 물리 추론 수준"으로 읽기엔 **비교 대상 0 · 경로 미기재 · 데이터 미공개**.
- **액션**: 🎯 **H3 채택 판단 시 이 41.97%를 "상한 미상의 단일 측정"으로만 인용**하고, 데이터셋이 채워지면 재방문.

> [!warning] 수집기 대조
> - ✅ 원문 대조 일치: 업보트 66 · 공개 09-16 · githubStars 21 · 저자 13 · 4시나리오 설명 · 517건 · 41.97% · VDR 56.00% · ADR 27.40% · 제3자(MiniMax 소속 저자 0명 — 볼트 확인) · 단일 모델 한정 · 볼트 기보유 `MiniMaxAI/MiniMax-H3` `downloads` **4,449,605**(09-19 실측 일치).
> - 🔴 보강: ① 수집기가 뺀 **저자 한정**(시나리오 간 차이는 모달리티 비교가 아님) ② **실행 경로(오픈 vs API·Context-IR) 미기재** ③ 데이터셋 미공개 · 일치도 없음 ④ 저자 소속에 **Tencent** 포함.
> - 📌 볼트 내부 주의: `MiniMaxAI/MiniMax-H3` 의 `downloads` 는 **30일 창** 값이라 09-06 실측 4,986,349 → 09-19 4,449,605로 **줄었다**(누적 아님). 좋아요는 4,943 → **5,476**(누적). Comfy-Org 재패키지 `downloads` **20,277,946** · ♥1,920(09-19).

> [!action] 당장 할 것
> 1. **[[MiniMax-H3]] 페이지에 "첫 제3자 정량치" callout 추가**(오케스트레이터 반영 대상) — 41.97% + 실행 경로 미기재 경고를 함께
> 2. **video-saas 레퍼런스 활용 점검 테스트 1건 설계** — 암묵 프롬프트 + 오디오 참조로 "입력을 실제로 쓰는지" 확인(낮음)
> 3. `gulucaptain/MiniMax-H3-Reason` 데이터셋 채워짐 여부 추적(다음 달)

> [!question] 미해결 질문
> - 공식 API(Context-IR + 2K)로 돌렸나, 오픈 가중치로 돌렸나?
> - 같은 517건을 다른 옴니/비디오 모델(Seedance 2.0 등)에 돌리면? — 입력 일부를 Seedance로 만들었으므로 **그 모델에는 유리할 수 있다**
> - 3명 평가자의 일치도는?
> - MSR 입력은 다시점(K장)인가 단일 이미지인가?

## 관련 페이지
- [[MiniMax-H3]] — 벤더 쪽 기록(카드 벤치 0건 반복 확인)
- [[MiniMax]]
- [[MiniMax-H3-Turbo-Lora]]
- [[Seedance]] · [[ByteDance]] — 평가 입력 합성에 사용된 경쟁 생성기
- [[Tencent]] — 저자 소속
- [[월드모델]]
- [[PhysBrain-1.5]] — 같은 배치, "물리세계"를 **이해 모델** 쪽에서 자체 평가
- [[측정도구-먼저-반증]] — 기존 벤치가 "시킨 걸 그리나"만 잰다는 지적
- [[한정어-탈락]]
- [[표-부분인용]]
- [[video-saas]]

## 원본
- 출처: https://huggingface.co/papers/2609.18323 · 본문 https://arxiv.org/html/2609.18323
- 레포: https://github.com/gulucaptain/MiniMax-H3-Reason · 데이터셋(게이트·미충전): https://huggingface.co/datasets/gulucaptain/MiniMax-H3-Reason
- 볼트 실측(2026-09-19): HF papers API `upvotes` 66 · `githubStars` 21 · `authors` 13 · `organization` None · `publishedAt` 2026-09-16 · `linkedDatasets` [] / GitHub API `stargazers_count` 21 · `forks_count` 0 · `open_issues_count` 1 · `created_at` 2026-09-11 · `pushed_at` 2026-09-19 · license None · 파일 37 / HF datasets API `downloads` 19 · `likes` 3 · `gated` manual / HF models API `MiniMaxAI/MiniMax-H3` `downloads` 4,449,605 · `likes` 5,476 · `lastModified` 2026-08-13 · license other · `Comfy-Org/MiniMax-H3` `downloads` 20,277,946 · `likes` 1,920 / 모델카드 원문 정량 벤치 검색 0건 / arXiv HTML 본문 전문 읽음(표 1·2, §3.3·4.1·4.5)
- 신뢰도: ⭐ (벤더 외 유일 측정 · 🔴 비교 모델 0 · 실행 경로 미기재 · 일치도 없음 · 데이터 미공개)
