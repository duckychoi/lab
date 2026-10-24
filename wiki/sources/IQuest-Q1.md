---
title: "IQuest-Q1 — '에이전틱 CLI' 간판의 320B/15B MoE, 그런데 Terminal-Bench 세 판 전부 GLM-5.3-Flash 에 진다"
type: source
domain: ai-news
tags: [ai-news, hf-paper, moe, open-weights, coding-agent, cli, terminal-bench, iquest, muon, mup, 표부분인용, 규약15]
created: 2026-10-24
updated: 2026-10-24
sources: []
reliability: medium
---

# IQuest-Q1: Advancing Foundation Capabilities for Agentic CLI Systems

**arXiv**: 2610.30949 · **HF**: https://huggingface.co/papers/2610.30949
**업보트**: **66** (수집기 66 **일치**) · HF 데일리 10-23 목록 **5위 — 미확정**(규약 ⑮)
**날짜**: `publishedAt` 2026-10-22 · `submittedOnDailyAt` 2026-10-23 · arXiv comments: *"IQuest Report"*
**저자**: HF API **177인** · 본문 바이라인 *"IQuest Research"* (기여자 목록은 §7) · HF org **IQuestLab**
**가중치**: 🟢 `IQuestLab/IQuest-Q1` — **2026-09-28 공개(논문보다 24일 먼저)** · DL **4,318** · ♥149 · **BF16 320.3B**(safetensors 메타) · MTP 헤드 별도(`mtp/`) · **Modified MIT**
**코드 레포**: HF `githubRepo` **없음**
**신뢰도**: ⭐⭐⭐

> [!insight] 핵심 인사이트 — 초록에 숫자 0개, 본문 Table 2 에 30여 개. 그리고 본문 해설은 자기 간판 벤치의 숫자만 뺐다
> 초록은 *"demonstrates capabilities in both coding and general tasks"* 로 끝난다. 볼트가 arXiv HTML(398,833B) Table 2 를 열었다.
> 🔴 **간판이 "Agentic CLI" 인데, CLI 를 직접 재는 Terminal-Bench 세 판에서 오픈 경쟁자 GLM-5.3-Flash 에 전부 진다**:
>
> | 벤치 | **IQuest-Q1** | GLM-5.3-Flash | DS-V4-Flash-0731 | Claude Opus-5 | GPT-5.6 Sol |
> |---|---|---|---|---|---|
> | Terminal-Bench 2.1 | 83.2 | **84.3** | 82.7 | 89.1 | 88.8 |
> | Terminal-Bench 3.0 | 17.9 | **30.0*** | 7.6 | 42.7 | 34.6 |
> | Terminal-Bench 4.0 | 22.7 | **32.8** | 7.0 | 53.9 | 37.3 |
> | IQuest-CLIBench ‡(자체) | **53.7** | 49.5* | 51.5* | 58.2* | 58.5* |
>
> ⇒ 🎯 **이긴 CLI 벤치는 자기 벤치(‡ "proprietary built-in benchmark") 하나다.** 그리고 §5.4 본문 해설은 SWE-Bench Pro 57.5 · DeepSWE 64.6 · NL2Repo 63.0 · PaperBench 86.0 에 숫자를 붙이면서 **Terminal-Bench 는 *"further evaluate long-horizon terminal workflows"* 라고만 적고 숫자를 생략했다** → [[표-부분인용]](저자 산문이 표의 불리한 칸을 건너뛴다) · [[숨김유인-부호]].

> [!insight] 📌 Terminal-Bench 2.1 → 3.0 낙차가 모든 모델에서 거대하다 — 2.1 은 포화됐다
> IQuest 83.2 → **17.9**(−65.3pp) · GLM-5.3-Flash 84.3 → 30.0 · DS-V4-Flash 82.7 → **7.6** · Hy3 71.7 → 3.0.
> ⇒ **2.1 에서 66~89 로 몰려 있던 모델들이 3.0 에서 1.7~42.7 로 흩어진다.** 🎯 **2.1 점수는 더 이상 모델을 구분하지 못한다** — "Terminal-Bench 83" 을 인용하는 마케팅은 포화된 판의 숫자다 → 벤치 포화(같은 판의 판별력 소실).

> [!warning] 🔴 비교표의 * — 경쟁자 점수 다수를 저자가 직접 쟀다
> *"Results with * are from our own testing"* · 하네스는 과제별로 **mini-SWE-agent / BasicAgent / Claude Code / 내부 하네스**가 섞인다 · 런타임 한도 6~12시간. ⇒ 공개값이 없는 칸은 **IQuest 의 하네스·설정으로 잰 경쟁자 점수**다 → [[비매칭-비교]] · [[벤치-개조-재평가]].
> 🔴 프런티어 비교 대상은 **Claude Opus-5**(5.5 아님) · GPT-5.6 Sol — 최신 판과의 격차는 표보다 클 수 있다.
> ⚖️ 오염 대응은 적었다: SWE 계열에서 *"keep only the Git history up to the base commit and use hooks… to block attempts to retrieve existing solutions"*.

## 다른 칸 (Table 2 발췌)
- 코딩: SWE-bench Multilingual **80.3** · SWE-Bench Pro 57.5 (GLM-5.3-Flash 59.4*) · NL2Repo 63.0 · CyberGym 84.5 · SkillsBench 74.1 · LiveCodeBench v6 89.7
- 일반: GPQA Diamond 93.3 · HLE 39.2 / w/ tools 55.7 · BrowseComp **85.5** · WideSearch 81.8 · Toolathlon-Verified 75.0 · MCP-Atlas 78.4 · **HealthBench Professional 33.4**(GLM-5.3-Flash 47.1*)
- 볼트 집계 — **코딩 13칸 vs GLM-5.3-Flash: 8승 5패**, 5패 중 3패가 Terminal-Bench 전부.

> [!note] 학습 레시피 (초록 + §2)
> Stable SplitNorm + **Muon**(임베딩 등 제외 전 파라미터) + **μP**(폭·깊이 스케일 규칙으로 최적 LR 전이) · 2단계 커리큘럼(2단계에서 코드 비중 ↑) · SWA 3 : FA 1 하이브리드 어텐션(처음·끝 2층 FA) · MTP 2층 · 후학습 **SFT + 도메인 RL + MOPD**(멀티 스캐폴드) · 모델 머징. → [[온폴리시-증류]] 계열(MOPD).

> [!warning] 177인 · 숫자 없는 초록 — 무엇을 뜻하나
> 저자 수는 **조직 규모의 신호이지 결과의 신호가 아니다.** 같은 org 의 이전 공개물(IQuest-Coder-V1 계열 · 2025-12~2026-02, 40B Loop-Instruct DL 2,176)과 비교하면 이번은 **가중치 선공개 → 24일 뒤 보고서** 순서다 ⇒ 논문은 **이미 배포된 모델의 사후 기술서**에 가깝다. HF 업보트 66(배치 최하)은 **모델 DL 4,318 과 비동행** → [[스타-근거-비동행]].

## 도메인별 추출 (ai-news 템플릿)

- **신뢰도**: ⭐⭐⭐ — 가중치 실존(320.3B BF16 · 190 파일) · 표 30여 칸 · 🔴 자체 벤치 1 · 경쟁자 자체측정 다수 · 코드 레포 없음.
- **즉시 활용**: **NO(로컬)** — 15B 활성이라 디코딩은 빠르겠으나 **메모리는 320B 전체**가 필요: BF16 ≈ **640GB**(볼트 계산 320.3B×2B). 커뮤니티 양자화가 이미 있다: `Baekpica/IQuest-Q1-Mixed-Quant-GGUF` DL **1,001** · `xhxlb/IQuest-Q1-GGUF` 856 · `xhxlb/IQuest-Q1-FP8` 36 (파생 합계 1,893 = 원본의 44%) → [[원본-파생-역전]] 감시 후보. 4bit 로도 ~160GB+ 추정(미실측) — 단일 소비자 GPU 범위 밖.
- **6개월 영향력**: 낮음~중간. 같은 체급 오픈 MoE([[GLM-5.3-Flash]] 321B MIT · [[Hy3]] 295B/21B · [[MiniMax-M3]])와 **동급 군집**이고, CLI 특화 주장은 공개 터미널 벤치로 뒷받침되지 않는다.
- **대체 관계**: 볼트 코딩 에이전트 백엔드 후보로서 GLM-5.3-Flash 를 **대체할 근거 없음**(Terminal-Bench 3패 · 라이선스는 GLM 이 MIT, IQuest 는 **상업 사용 시 UI 에 "IQuest-Q1" 표기 의무** Modified MIT).
- **허와 실**: 레시피(Muon+μP 안정성 마진, SWA 하이브리드)는 실제 기술 기여일 수 있다. **"Agentic CLI" 는 간판이고, 근거는 자체 CLIBench 다.**
- **액션**: 지금 할 것 없음. 커뮤니티 GGUF DL 이 원본을 넘는지만 감시(낮음).

## 관련 페이지
- [[GLM-5.3-Flash]] · [[Hy3]] · [[MiniMax-M3]] · [[DeepSeek-V4-Flash-0731]] — 비교표 오픈 경쟁자
- [[Zhipu-AI]] · [[Tencent]] · [[MiniMax]] · [[DeepSeek]] · [[Anthropic]] · [[OpenAI]]
- [[표-부분인용]] · [[숨김유인-부호]] · [[비매칭-비교]] · [[벤치-개조-재평가]] · [[스타-근거-비동행]] · [[원본-파생-역전]] · [[온폴리시-증류]] · [[간판-지체]](반대 방향: 간판이 본문보다 **높다**)
- [[Long-Horizon-Terminal-Bench]] · [[SWE-Bench-Pro-Verified]]
- [[WeVisOne-VL]] · [[FAPL]] · [[OpenDS-World]] · [[LayerEditor]] — 같은 배치
- [[ai-news]] · [[local-llm]]

## 원본
- 출처: https://huggingface.co/papers/2610.30949 (arXiv 2610.30949)
- 열어 본 것: HF papers API · **arXiv HTML v1 전문**(Table 1·2 · §5.2~5.4 · Limitations) · arXiv abs comments · HF models API(원본 + 파생 검색) · HF LICENSE 본문
- 관측: 2026-10-24T09:06Z (18:06 KST)
- 신뢰도: ⭐⭐⭐
