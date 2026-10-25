---
title: "DeepSeek-V4.1-Flash-1017 — 같은 763B 체크포인트의 마이너 업데이트. 11개 벤치 전부 상승, 그러나 표가 20행에서 11행으로 줄었다"
type: source
domain: local-llm
tags: [local-llm, hf-model, deepseek, moe, agent, kv-cache, minor-update, self-reported, harness, 비매칭비교]
created: 2026-10-24
updated: 2026-10-25
sources: [DeepSeek-V4.1-Flash.md, DeepSeek-V4.1-Flash-Paper.md, DeepSeek-V4.1-Flash-1017-GSQ-RCO-GGUF.md]
reliability: medium
---

# DeepSeek-V4.1-Flash-1017

**HF**: https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017
**선행 페이지**: [[DeepSeek-V4.1-Flash]] (원본 · 2026-09-10 공개) · [[DeepSeek-V4.1-Flash-Paper]] (기술 보고서 — 1017 카드도 **같은 PDF** 를 링크)
**실측(2026-10-24T09:06Z · 18:06 KST)**: 다운로드 **57,715**(수집기 일치) · likes **2,636**(수집기 2,635 · +1 드리프트) · trendingScore **2,053** · MIT · `gated: false` · `pipeline_tag` image-text-to-text · createdAt **2026-10-17T02:40Z** · lastModified 10-17T05:46Z
**파라미터**: `safetensors.total` **763,205,315,794** — 🎯 **원본과 정밀도별 수치까지 완전히 동일**(BF16 1,976,441,856 · F32 42,307,282 · F8_E4M3 204,015,223,296 · I8 557,171,343,360) ⇒ **아키텍처 변경 없음, 가중치만 갱신된 체크포인트**다. ("552B 백본 ≠ 763B 체크포인트" 구분은 원본 페이지 [[단위-불일치]] 참조)
**신뢰도**: ⭐⭐ (수치는 전부 **벤더 자기보고** · 독립 재현 없음 · 측정 조건 고지가 원본보다 얇다)

> [!insight] 🏆 핵심 인사이트 — **"원본의 약점 축"이 정확히 고쳐졌다. 그리고 원본의 "강점 축"은 표에서 사라졌다**
> 원본 페이지(09-11/09-14)가 적은 약점은 *"벤치 세대가 최신·고난도로 갈수록 무너진다"* 였다 — TB 4.0 **−20.6**, HLE **−19.5**, ProgramBench **−16.7** (vs Opus).
> 1017 은 바로 그 축에서 가장 크게 올랐다: **TB 4.0 +11.1 · ProgramBench +8.8 · HLE +5.8** ⇒ Opus 대비 격차 **TB 4.0 20.6 → 9.5(54% 축소) · ProgramBench 16.7 → 7.9(53%) · HLE 19.5 → 13.7(30%)**.
> 🔴 **동시에 표가 20행 → 11행으로 줄었다.** 빠진 9행: GPQA · Codeforces · MathArena Apex · **TB 2.1(원본 1위 90.6)** · TB 3.0 · **CyberGym(원본 최고 88.1)** · SEC-Bench Pro · ExploitGym · **HLE w/ tools(원본 1위 63.9)**.
> ⇒ 🎯 **원본의 "1위" 행 3개가 전부 빠졌다.** 개선 서사에 불리해서인지(회귀 은폐), 포화돼서 의미가 없어서인지는 **카드로 구분 불가**다. 확정 가능한 것: **1017 이 그 축에서 원본보다 나은지 나쁜지 볼트는 모른다.** → [[표-부분인용]] · [[선발창-누락]]의 벤치 버전

## 📊 벤치마크 — 카드 표 원문 대조 (자기보고)

| 벤치 | 원본 카드(09-10) | **1017 카드의 "V4.1-Flash" 열** | **1017** | Δ | Opus 5 | 1017 vs Opus |
|---|--:|--:|--:|--:|--:|--:|
| HLE w/o tools | 36.8 (39.1†) | 36.8 (39.1†) | **42.6 (44.0†)** | +5.8 | 56.3 | 🔴 −13.7 |
| Terminal-Bench 4.0 | 31.2 | 31.2 | **42.3** | +11.1 | 51.8 | 🔴 −9.5 |
| DeepSWE v1.1 | 74.2 | 74.2 | **77.0** | +2.8 | 74.0 | ✅ +3.0 |
| ProgramBench | 20.3 | 20.3 | **29.1** | +8.8 | 37.0 | 🔴 −7.9 |
| NL2Repo-Bench | 🔴 **64.0** | 🔴 **65.4** | **68.2** | +2.8 (또는 +4.2) | 75.3 | 🔴 −7.1 |
| Automation-Bench | 54.8 | 54.8 | **60.5** | +5.7 | 50.3 | ✅ +10.2 |
| Agents' Last Exam | 31.8 | 31.8 | **35.4** | +3.6 | 28.6 | ✅ +6.8 |
| Apex Bench v1.1 | 🔴 (없음 — "MathArena Apex 65.6") | 64.6 | **72.1** | +7.5 | 65.8 | ✅ +6.3 |
| Chartography w/tools | 78.9 | 78.9 | **83.0** | +4.1 | 84.0 | −1.0 |
| BabyVision w/tools | 89.6 | 89.6 | **92.5** | +2.9 | 94.1 | −1.6 |
| ZeroBench-main w/tools | 49.0 | 49.0 | **51.0** | +2.0 | 52.0 | −1.0 (GPT-5.6 Sol 53.0) |

✅ **수집기 수치 전건 일치**(TB 4.0 31.2→42.3 · DeepSWE 74.2→77.0 · ProgramBench 20.3→29.1 · HLE 36.8→42.6 · Apex 64.6→72.1 · Opus HLE 56.3 / TB 51.8 / ProgramBench 37.0 / DeepSWE 74.0 / Automation 50.3).
⚖️ **정직한 집계**: 11개 중 **Opus 5 를 넘는 것 4개**(DeepSWE · Automation · ALE · Apex), **지는 것 7개**(HLE · TB 4.0 · ProgramBench · NL2Repo · 시각 3종). 시각 3종은 1~1.6점 차로 사실상 근접. **텍스트 고난도 4종(HLE·TB4·ProgramBench·NL2Repo)은 여전히 7~14점 열세**다.
경쟁사 열(Opus 5 · GPT-5.6 Sol · [[Kimi-K3]] · [[GLM-5.3]])의 값은 **원본 카드와 숫자가 전부 같다** ⇒ **재측정이 아니라 복사**다(같은 날 재측정했다는 근거 없음).

> [!warning] 🔴 **TB 4.0 +11.1 은 하네스가 바뀐 비교일 수 있다** → [[비매칭-비교]]
> - **원본 카드**: *"For code agent benchmarks (Terminal-Bench 2.1/3.0/4.0, …), the model is evaluated with the Minimal mode of **DeepSeek Harness**"*
> - **1017 카드**: *"We use the **Claude Code harness** for Terminal-Bench 4.0"*
> - 그런데 1017 표의 기준 열 31.2 는 **원본 카드 값과 동일**하다 ⇒ **기준값은 DSH Minimal, 신규값은 Claude Code 하네스**일 가능성이 있다. 1017 카드는 기준 열을 Claude Code 로 재측정했다고 **밝히지 않는다**.
> - 방향 참고: 원본 카드의 스캐폴드 비교표에서 TB **2.1** 은 Claude Code **88.0** < DSH Minimal **90.6** — 즉 원본 모델에겐 Claude Code 가 **불리한** 하네스였다. ⇒ 하네스 교체가 이득을 **부풀렸다고 단정할 수는 없다**(오히려 반대일 수 있다). 확정 가능한 것은 **"같은 조건 비교인지 모른다"** 까지.
> - DeepSWE 는 양쪽 모두 **mini-SWE 하네스** 명시 ⇒ **+2.8 은 동일 하네스 비교로 볼 수 있는 유일한 에이전트 행**이다.

> [!warning] 🔴 **같은 모델의 같은 벤치 값이 두 카드에서 다르다** → [[문서내-값충돌]] (문서 간 변형)
> - **NL2Repo-Bench**: 원본 카드 **64.0** ↔ 1017 카드의 "DS-V4.1-Flash" 열 **65.4**. 정정 고지 없음. ⇒ 1017 의 상승폭은 **+2.8 또는 +4.2** — 어느 쪽인지 인용 불가.
> - **Apex**: 원본 카드는 *"MathArena Apex"* 65.6(K3 도 65.6 · Opus "—"), 1017 카드는 *"Apex Bench v1.1"* 64.6(K3 **47.8** · Opus 65.8). K3 값이 65.6 → 47.8 로 다르다 ⇒ **이름이 비슷한 다른 벤치**로 판단한다(추정). ⇒ 🔴 **"Apex 64.6→72.1" 의 기준 64.6 은 원본 카드에 없는 수치**다 — 원본 공개 시점의 주장이 아니라 1017 과 함께 새로 나온 측정이다.

> [!warning] 측정 조건 고지가 원본보다 얇다
> 원본 카드: *"All instruct results … use the maximum effort setting (`reasoning_effort=100`)… `temperature=1.0, top_p=0.95`"* + 컨텍스트 길이(1M / 512k) + 스캐폴드별 표.
> 1017 카드: **reasoning_effort 언급 없음** · 평가 샘플링 언급 없음 · 권장 샘플링만 `temperature 1.0 · top_p **1.0** · context 1M · max_tokens ≥256K`(원본 평가 top_p 0.95 와 다름).
> *"reduces task execution time and output length … advancing the performance–cost Pareto frontier"* — 🔴 **시간·출력 길이·비용 수치 0건.** 파레토 주장의 근거가 카드에 없다. (기술 보고서 링크는 원본 V4.1 PDF 그대로 — 1017 전용 보고서 없음)

## 도메인별 추출 (local-llm)

- **실용성 판단**: 원본과 동일 — **763B 체크포인트(48 샤드) · 로컬 불가 · API/대형 클러스터용.** 볼트 `local-llm` 분류는 원본 페이지와 같은 이유(KV 압축 아키텍처 학습 가치)로 유지. 1017 은 아키텍처 변경이 없으므로 **KV 890B/token 주장도 그대로 승계**(새로 측정된 것은 아님).
- **메모리 아키텍처**: 변경 없음(CED + CSA2 + FP4 KV — [[DeepSeek-V4.1-Flash]] · [[DeepSeek-V4.1-Flash-Paper]]). 🎯 **같은 KV 예산에서 장기 과제 점수가 오른 것** = 원본 페이지 미해결 질문 *"TB 2.1→4.0 붕괴가 컨텍스트 압축 때문인가, 학습 데이터 때문인가"* 에 대한 **간접 증거**: 압축 구조는 그대로인데 TB 4.0 이 +11.1 ⇒ **붕괴의 상당 부분은 압축의 구조적 한계가 아니라 사후학습으로 고칠 수 있는 것**이었다(단 하네스 교체 변수가 섞여 있어 **확정 아님**).
- **Hermes 적용**: 직접 불가(크기). 판단 기준만 갱신 — DeepSeek API 를 쓸 경우 **1017 이 장기 에이전트 과제에서 원본보다 낫다는 자기보고**가 있다. 단 원본이 1위였던 TB 2.1·CyberGym·HLE w/tools 에서의 1017 성능은 **미공개**.
- **트레이드오프**: 파레토 주장은 **수치 없음**. 확인된 트레이드오프는 원본 페이지의 것(KV 890B/token ↔ 고난도 열세)뿐이고, 1017 은 그 열세를 **반쯤** 줄였다는 자기보고.
- **오픈소스 구현체**: MIT · Jinja chat template **없음**(원본과 동일 — `encoding/encoding.py` 참조 구현 + [deepseek-recipe](https://github.com/deepseek-ai/deepseek-recipe) Rust/Python 라이브러리) ⇒ 🔴 **llama.cpp·vLLM 기본 chat template 경로로 바로 못 돈다** — 서빙 시 인코딩 계층을 직접 붙여야 한다. → [[선언된-구현체-공백]]의 경량판(구현체는 있으나 표준 경로 밖)

## 📈 다운로드 — 원본과 비교

| 레포 | 관측 | 다운로드 | likes | 비고 |
|---|---|--:|--:|---|
| [[DeepSeek-V4.1-Flash]] | 09-11 (볼트) | 6 | 1,583 | 공개 당일 |
| 〃 | 09-14 (볼트) | 244,457 | 2,303 | 공개 +4일 |
| 〃 | **10-24 (볼트)** | **1,478,503** (30일) / **2,078,447** (전체) | 4,717 | 전체 기준 09-14 대비 **×8.50** · trendingScore 117 |
| **1017** | **10-24 (볼트)** | **57,715** | 2,636 | 공개 **+7.3일** · trendingScore 2,053 |

- 🎯 **1017 은 공개 7일 차에 원본의 4일 차(244,457)의 약 24%** 다. 원본 30일치의 **3.9%**. ⇒ **"트렌딩 1위"(trendingScore 2,053 vs 원본 117)인데 실사용 흡수는 원본에 훨씬 못 미친다.** 해석 후보(미검증): ① 763B 를 이미 받은 사용자가 **마이너 업데이트를 다시 받을 유인이 약함** ② 원본 레포가 계속 기본 경로로 쓰임. → [[상대속도-가림]](트렌딩은 속도, 다운로드는 누적)
- 원본 09-14 규칙 *"공개 72시간 내 다운로드는 지표가 아니다 · ♥/dl 비율은 +7일 이후"* — 1017 은 **+7.3일로 조건 충족**: dl/♥ = **21.9 : 1**(원본 +4일 시점 106 : 1). ⇒ ♥ 대비 실사용이 원본보다 **약 5배 얇다**.
- 🔴 원본 레포 `lastModified` 가 **2026-10-16T09:27Z** 로 바뀌어 있다(09-14 볼트 기록은 09-10). 1017 공개 전날 원본 레포에 무엇이 바뀌었는지 **미확인**.

> [!question] 미해결
> ① 1017 표의 "DS-V4.1-Flash" 기준 열이 **Claude Code 하네스로 재측정된 값인가, 원본 DSH Minimal 값의 복사인가**(31.2 동일 → 복사 의심)
> ② NL2Repo **64.0 vs 65.4** — 어느 쪽이 정정값인가
> ③ 빠진 9행(특히 TB 2.1 · CyberGym · HLE w/tools)에서 1017 이 **회귀했는가**
> ④ "실행 시간·출력 길이 감소"의 수치 — 카드·보고서 모두 없음
> ⑤ 원본 레포 10-16 수정 내용
> ⑥ 1017 평가의 `reasoning_effort` 설정

> [!action] 액션 후보
> - (중간) DeepSeek API 를 쓰는 워크로드가 있다면 **장기 에이전트 과제 1개를 원본 vs 1017 로 직접 A/B** — 카드가 숨긴 TB 2.1 류(짧은 터미널 과제)도 함께 넣어 **회귀 여부 확인**
> - (낮음) ①·② 를 HF Community 탭(Discussions)에서 확인 — 다음 재수집 시

## 관련 페이지
- [[DeepSeek-V4.1-Flash]] ← 원본 (벤치 약점 분석 · 552B↔763B)
- [[DeepSeek-V4.1-Flash-Paper]] ← 기술 보고서 (1017 도 같은 PDF 링크)
- [[DeepSeek]] · [[DeepSeek-V4-Flash]] · [[DeepSeek-V4-Pro]] · [[DeepSeek-V4-Flash-0731]]
- [[Kimi-K3]] · [[GLM-5.3]] · [[Anthropic]] ← 비교 열의 경쟁 모델
- [[DeepSWE]] · [[Long-Horizon-Terminal-Bench]]
- [[비매칭-비교]] · [[문서내-값충돌]] · [[표-부분인용]] · [[하네스-설계-축]] · [[단위-불일치]] · [[상대속도-가림]] · [[선언된-구현체-공백]] · [[에이전트축-분기]]

## 원본
- 출처: https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017
- 열어 본 것: HF API `?expand[]=downloads,downloadsAllTime,likes,createdAt,lastModified,gated,safetensors` (1017 · 원본) · `raw/main/README.md` (1017 · 5,231 B / 원본 · 13,110 B — 둘 다 HTTP 200) · `tree/main` (48 샤드 · `encoding/` · `inference/`)
- 관측: 2026-10-24T09:06Z (18:06 KST)
- 신뢰도: ⭐⭐ (전 수치 자기보고 · 하네스·기준값 불일치 2건 · 표 축소)

## 🔄 2026-10-25 — 파생본 도착
- [[DeepSeek-V4.1-Flash-1017-GSQ-RCO-GGUF]] — 생성 6일 만에 ISTA 양자화(IQ2_XXS 2.00bpw 가 AIME25·GPQA-D·LCB v6 기준선 100.0% 주장 · AIME 는 기준선 만점 → [[천장-기준선]]) · 🔴 카드 TBD 6건
