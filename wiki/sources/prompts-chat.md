---
title: prompts.chat — 최초의 프롬프트 라이브러리가 셀프호스팅 제품이 된 경로 (⭐169,220)
type: source
domain: ai-news
tags: [ai-news, github-trending, prompt-engineering, dataset, self-hosting, legacy]
created: 2026-09-04
updated: 2026-09-04
sources: []
reliability: high
---

# f/prompts.chat — 3년 9개월 된 레포의 두 번째 삶

**GitHub**: https://github.com/f/prompts.chat (구 *Awesome ChatGPT Prompts*)
**스타수**: **169,220** (2026-09-04 API 실측 · raw 169,219 대비 **+1**)
**포크 21,773 · 이슈 75 · 워치 1,647 · 라이선스 `NOASSERTION`(CC0 계열 추정, API 미해석) · 생성 2022-12-05 · 최종 push 2026-09-04**

> [!insight] 핵심 인사이트
> **2022-12-05 생성** — 볼트가 추적하는 레포 중 가장 오래된 축이다. ChatGPT 공개 5일 뒤에 만들어진 "최초의 프롬프트 라이브러리"가 3년 9개월 뒤에도 **당일 +168**로 살아 있다. 흥미로운 건 생존 **방식**이다: 이 레포는 목록으로 남지 않고 **`npx prompts.chat new` 한 줄로 조직 내부에 사설 프롬프트 라이브러리를 세우는 제품**(Next.js + PostgreSQL + GitHub/Google/Azure AD 인증)으로 바뀌었다. **큐레이션 자산 → 셀프호스팅 인프라** 라는 이 전환은 [[claude-skills]]·[[awesome-claude-skills]] 같은 "awesome 목록형" 자산이 **다음에 갈 곳**을 보여준다.

> [!warning] 🚨 README 배지가 스스로를 **18% 낮춰** 말한다 — 배지 규칙의 두 번째 역방향 사례
> README 자체 표기는 **"⭐143k+ GitHub stars"** 인데 **API 실측은 169,220**이다(**+26,220, +18.3%**). 볼트의 09-02 규칙 *"배지를 근거로 쓰지 않는다"* 는 원래 **과장 방어**용이었으나, 여기서는 배지가 **과소** 표기다([[VoiceStudio]]에 이은 **두 번째 역방향**). → **규칙 정밀화: 배지는 과장/과소 어느 쪽으로도 틀린다. 문제는 방향이 아니라 *갱신되지 않는다*는 것이다.** raw 자동수집 값(169,219)이 README보다 정확했다.

> [!warning] 권위 나열은 근거가 아니다
> README는 Forbes 등재·Harvard/Columbia 인용·**학술 인용 40+**·HF 최다 좋아요 데이터셋·GitHub Staff Pick, 그리고 **Greg Brockman·Wojciech Zaremba(OpenAI 공동창업자)·Clement Delangue(HF CEO)** 의 X 게시물을 나란히 건다. 공교롭게도 이는 [[humanizer]] **패턴 2번 "중요성을 증명하려는 이름 나열"** 의 교과서적 사례다 — **같은 배치의 두 레포가 서로를 반증한다.** 인용 40건은 실재하나, *프롬프트 카탈로그의 품질*이 아니라 *데이터셋으로서의 접근성*을 재는 값에 가깝다.

## 구성 (README 실측)

- **배포 포맷 3종**: `prompts.csv` · `PROMPTS.md` · **HuggingFace 데이터셋 `fka/prompts.chat`** — 목록이 **기계 판독 가능한 데이터셋**으로 동시 배포됨
- **기여 경로**: `prompts.chat/prompts/new` 웹 제출 → 레포로 **자동 동기화** (PR 없이 축적)
- **셀프호스팅**: `npx prompts.chat new my-prompt-library` → 브랜딩·테마·인증·기능 설정 마법사. PostgreSQL 권장(Neon 스폰서)
- **부속물**: 25+장 인터랙티브 프롬프트 엔지니어링 책 · 8~14세 대상 게임형 학습(`prompts.chat/kids`)

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐⭐⭐⭐ — 규모·수명·학술 인용은 실재. 단 **개별 프롬프트의 효과 측정치는 0건**이며, 커뮤니티 자동 동기화 구조상 **품질 게이트가 약하다**.
- **즉시 활용**: **부분 YES.** 프롬프트를 그대로 쓸 일은 적다(볼트는 이미 스킬 체계를 갖췄다). 쓸 만한 건 **셀프호스팅 구조** — 볼트의 `~/.claude/skills/` 21종을 **검색 가능한 사설 라이브러리로 세우는 참조 구현**이 된다.
- **6개월 영향력**: 프롬프트 단위 자산은 **스킬 단위 자산에 흡수되는 중**이다([[anthropics-skills]] `SKILL.md`). 이 레포의 미래는 카탈로그가 아니라 **호스팅 레이어**에 있다.
- **대체 관계**: [[system-prompts-and-models-of-ai-tools]](유출 시스템 프롬프트 아카이브)와 **성격이 반대** — 저쪽은 *관측된 것*, 이쪽은 *제안된 것*. 효과 검증은 양쪽 다 없다.
- **허와 실**: "세계 최대 오픈소스 프롬프트 라이브러리"는 **개수 주장**이다. 볼트의 누적 관측(*[[claude-skills]] 스킬 355개, [[Repo-To-Skill]] 5,000개*)과 같은 함정 — **개수는 품질도 검색가능성도 보증하지 않는다.**

> [!question] 미해결 — 이 배치에서 가장 볼트에 아픈 질문
> 이 레포는 **웹 제출 → 자동 동기화**로 자산을 쌓고, [[CoGR]]이 지적한 *"쌓는 쪽은 찾는 문제를 늦게 발견한다"* 를 **셀프호스팅 검색 UI로 먼저 풀었다.** 볼트는 소스 **935건**을 쌓았고 `queries/` 는 **여전히 0건**이다. → 기존 actionable(*queries 기록 시작*) **우선순위 재확인**.

## 관련 페이지
- [[humanizer]] · [[anthropics-skills]] · [[claude-skills]] · [[awesome-claude-skills]] · [[system-prompts-and-models-of-ai-tools]] · [[Repo-To-Skill]] · [[CoGR]] · [[에이전트-스킬]] · [[LLM-Wiki]] · [[OpenAI]]

## 원본
- 출처: https://github.com/f/prompts.chat
- 데이터셋: https://huggingface.co/datasets/fka/prompts.chat
- 수집: 2026-09-04 자동수집 (ai-news)
- 검증: README defuddle 원문 + GitHub API 실측 (2026-09-04)
- 신뢰도: ⭐⭐⭐⭐
