---
title: asgeirtj/system_prompts_leaks
type: source
domain: ai-news
tags: [ai-news, prompt-engineering, system-prompt, github-trending, reference]
created: 2026-07-05
updated: 2026-07-05
sources: [system_prompts_leaks.md]
reliability: medium
---

# asgeirtj/system_prompts_leaks

> [!update] 2026-09-14 갱신 — ⭐**66,373**(71일 **+17,148 · +34.8%**) · 🔴 중복 재배달 · **페이지 대폭 보강**
> **GitHub API 실호출(2026-09-14)**: ⭐**66,373**(raw 66,368 대비 **+5**) · fork **10,833**(raw 일치) · 이슈 **56** · **CC0-1.0**(일치) · 언어 **JavaScript** · created 2025-05-03(일치) · **pushed 2026-09-13**
> 🔴 **신규 아님.** 이 페이지는 **2026-07-05 생성**(당시 ⭐49,225). raw가 *"볼트 미보유"* 로 오판 → [[백필-우회]]
> ⚠️ **볼트 자기 점검**: 이 페이지는 71일간 갱신되지 않은 **40줄짜리 최소 페이지**였다. 그 사이 ⭐가 **+34.8%** 늘었다. **갱신 주기가 없는 페이지는 조용히 낡는다.**
>
> 📌 **새로 확인된 것 — 최근 추가분에 날짜가 붙는다**(GitHub description 실확인)
> description 원문: *"Extracted system prompts from **Anthropic - Claude Fable 5.1, Opus 5, Claude Design, Claude Code**. **OpenAI - ChatGPT GPT-6-Astra, Codex**. **Google - Gemini 3.8 Flash, 3.1 Pro, Antigravity**"*
> raw 보고 날짜: ChatGPT Work Codex(local)·Gemini 3.8 Flash **2026-09-13** · Claude Code headless(Fable 5.1) **2026-09-05** · Codex GPT-6-Astra **2026-09-04**. **pushed 2026-09-13 이 09-13 추가분과 일치**한다.
>
> 🔴 **raw가 가져온 핵심 한정어 — 채택한다**: *"verbatim(원문 그대로)"* 주장을 **레포 내부에서 검증할 수단이 없다.** 항목별 **추출 방법·캡처 시점 로그가 없어** 진위는 전적으로 외부 인용에 의존한다(워싱턴포스트 2026-05-11 인터랙티브 · CEPS AI World 2026-07-10 대시보드).
> 🎯 **⭐66k를 기능 성숙도로 읽으면 안 된다 — 이건 코드가 아니라 문서 아카이브다.** 별은 *"이 코드가 잘 돈다"* 가 아니라 *"이 자료가 궁금하다"* 를 센다. **같은 지표가 레포 종류에 따라 다른 것을 측정한다.** → [[측정도구-먼저-반증]] · [[단위-불일치]]
> ⚠️ `reliability: medium` 유지 — 검증 경로 부재가 해소되지 않았다.

Anthropic·OpenAI·Google·xAI 등 주요 LLM 서비스의 시스템 프롬프트 추출본 모음. 프롬프트 엔지니어링 리버스 참고용 레퍼런스.

## 핵심 인사이트

> [!insight] "프론티어 서비스의 프롬프트 설계를 역공학"
> 상용 챗 서비스가 실제로 어떻게 톤·안전장치·도구사용을 지시하는지 원문 수준으로 관찰 가능. [[system-prompts-and-models-of-ai-tools]]와 짝을 이루는 참고 자산으로, 내 봇/에이전트 프롬프트 설계 시 "검증된 프레이징"을 빌려올 수 있다.

> [!warning] 신뢰도 / 저작권 주의
> "추출본(leak)"은 버전·정확성이 보장되지 않으며 시점에 따라 낡는다. 그대로 복붙 시 서비스 약관·저작권 이슈 소지. 설계 패턴 참고용으로만 활용.

## 도메인별 추출 (ai-news)

- **신뢰도**: GitHub ⭐49,225 (+471/일). 콘텐츠 자체는 비공식 추출이라 medium.
- **즉시 활용**: 부분 YES — 프롬프트 구조(역할 정의, 거절 처리, 도구 지시) 패턴을 내 에이전트에 참고.
- **6개월 영향력**: 프롬프트 설계 관행의 상향 평준화. "무엇을 지시해야 하는가"의 공용 레퍼런스화.
- **대체 관계**: 대체 아님 — [[system-prompts-and-models-of-ai-tools]] 보완.
- **허와 실**: 마케팅 없음. 다만 정확성·최신성 미보장.
- **액션**: 거절/안전/도구지시 섹션만 발췌해 패턴 노트화.

## 관련 페이지
- [[system-prompts-and-models-of-ai-tools]]
- [[Claude-Code-워크플로우]]
- [[agent-skills]]

## 원본
- 출처: https://github.com/asgeirtj/system_prompts_leaks
- 신뢰도: ⭐⭐ (GitHub ⭐49,225 / 콘텐츠는 비공식 추출)
