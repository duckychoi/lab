---
title: DeepSeek-V4-Flash-Vision-Exp — DeepSeek-V4 계열 첫 멀티모달 실험 모델
type: source
domain: ai-news
tags: [ai-news, hf-model, deepseek, multimodal, vlm, agent-benchmark, mit]
created: 2026-09-06
updated: 2026-09-06
sources: []
reliability: medium
---

# deepseek-ai/DeepSeek-V4-Flash-Vision-Exp

**HF 모델**: https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-Vision-Exp
**지표(2026-09-06 API 실측)**: 다운로드 **209,191** · 좋아요 **698** · `gated=False` · 생성 2026-08-31 · 최종수정 2026-09-01 · **MIT** · pipeline **image-text-to-text**
**raw 수집값(09-05)**: DL 133,024 · 좋아요 628 → **DL +76,167(+57.3%)** — 배치 증가율 2위
**벤더**: [[DeepSeek]]

> [!insight] 핵심 인사이트 — **텍스트를 잃지 않고 멀티모달을 얻었다는 것이 주장의 핵심**
> V4-Flash 아키텍처에 시각 모듈을 얹어 **연속 학습**한 계열 첫 멀티모달 실험 모델이다. 전작 **V4-Flash-0731 대비**:
> - **ApexBench Pass@1 26.2 → 36.5** (+10.3, **+39%**)
> - **Agents' Last Exam 25.2 → 27.3**
>
> 멀티모달 능력을 붙이면서 **텍스트 에이전트 성능을 유지**했다는 게 이 카드의 판매점이다. 통상 시각 모듈 추가는 텍스트 능력을 갉아먹으므로, 사실이면 의미 있는 결과다.

> [!insight] **Opus-4.8 대비 승패가 축마다 갈린다 — 이 표의 가장 유용한 부분**
> - **이긴다**: Agents' Last Exam **27.3 vs 25.7** · ZeroBench Pass@5 **35.0 vs 34.0**
> - **크게 진다**: NL2Repo **57.7 vs 69.7**(-12.0) · DSBench-Hard **63.6 vs 71.7**(-8.1)
> - **비슷**: DeepSWE **59.3 vs 58.0**
>
> 패턴이 읽힌다 — **에이전트 시험·시각 추론에서는 대등하거나 앞서고, 레포 규모 코드 생성·데이터사이언스 난제에서는 크게 뒤진다.** 즉 *"에이전트 성능"* 을 한 덩어리로 말하면 안 된다는 사례다. [[Qwen3.8-27B]]가 SWE-bench Pro에서는 이기고 HLE·Terminal Bench에서 지는 것과 **같은 형태의 분열**이다.
> ⚠️ **볼트에 축적되는 규칙**: 벤더 표에서 승리 항목만 뽑아 인용하면 반드시 틀린다. **이 배치 두 모델 모두 승패가 갈렸다.**

> [!insight] **MIT 라이선스 · gated=False**
> 209,191 DL / 698 좋아요. 실험 모델(`-Exp`)임에도 **MIT**로 나왔다 — [[DeepSeek]]의 일관된 노선이고, [[MiniMax-H3]]의 커뮤니티 라이선스나 [[Qwen3.8-Flash-Next-GGUF]]의 `other`와 대비된다.

> [!warning] ⚠️ **자체 공표 표이며 제3자 재현이 없다**
> 볼트 반복 규칙 그대로 적용. 덧붙여:
> - 모델명에 **`-Exp`(experimental)** 가 명시돼 있다 — **벤더 스스로 실험 단계임을 표시**했다. 프로덕션 인용 부적절.
> - **크기·활성 파라미터·컨텍스트 길이가 카드 메타에서 확인되지 않았다.** V4-Flash 계열(304B MoE)을 상속한다면 로컬 배포는 불가능한 규모다 — **확인 전까지 "돌려볼 수 있다"고 가정하지 않는다.**

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐⭐⭐ medium — HF API 실측(DL·좋아요·MIT·gated=False 확인). 성능은 벤더 자체 표.
- **즉시 활용**: **NO(로컬).** V4-Flash 계열 규모를 상속하면 개인 하드웨어 밖이다. **API 경로가 있다면 YES** — Agents' Last Exam에서 Opus-4.8을 앞선다는 주장은 검증할 가치가 있다.
- **6개월 영향력**: **중간~높음.** [[DeepSeek]]가 멀티모달 축에 진입했다는 사실 자체가 오픈 웨이트 지형을 바꾼다. MIT라는 점이 파급을 키운다.
- **대체 관계**: 폐쇄형 멀티모달 에이전트(Opus·GPT 계열)의 **부분 대체 후보**. 단 NL2Repo -12.0이 보여주듯 **전면 대체는 아니다.**
- **허와 실**: 실은 **MIT·전작 대비 +39%·승패가 솔직히 적힌 표**. 허는 **`-Exp` 딱지와 제3자 재현 부재**.
- **액션**: **모델 크기·컨텍스트 사양 확인**(중간) — 로컬 가능 여부를 가르는 단일 변수. Agents' Last Exam 정의 확인(낮음).

> [!question] 미해결 질문
> - **파라미터 규모와 활성 파라미터** — 이 배치 모델 6건 중 **유일하게 규모를 모른다.**
> - **NL2Repo에서 -12.0인 이유** — 시각 모듈 추가의 대가인가, 아니면 원래 약점인가. 전작 대비 NL2Repo 수치가 없어 판정 불가.
> - **`-Exp`가 정식 릴리스로 이어지는가.**

## 관련 페이지
- [[DeepSeek]] — 벤더 엔티티
- [[DeepSeek-V4-Flash]] — 계열 원본
- [[Qwen3.8-27B]] — **승패가 축마다 갈리는 같은 패턴**의 대비 사례
- [[MiniMax-H3]] — 옴니모달 경쟁 축(라이선스 노선은 정반대)
- [[검사가능성-공사]] — 벤더 자체 표의 한계라는 축

## 원본
- 출처: https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-Vision-Exp
- 신뢰도: ⭐⭐⭐ (HF API 2026-09-06 실측 · 벤더 자체 표 · 규모 미확인)
