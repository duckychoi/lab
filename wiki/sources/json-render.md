---
title: "json-render — '매번 스키마를 지킨다'의 실체는 사후 검증 + 재프롬프트 도구였다"
type: source
domain: ai-news
tags: [ai-news, github-trending, generative-ui, remotion, zod, structured-output, video-saas, 수집기-정정, 하네스-설계-축]
created: 2026-09-22
updated: 2026-09-22
sources: []
reliability: high
---

# json-render

> [!insight] 🎯 핵심 인사이트 — *"every time"* 은 **라이브러리가 보장하지 않는다**. 라이브러리가 주는 것은 **보장을 만드는 부품**이다
> README 46행: *"**Predictable** - JSON output matches your schema, **every time**"* · 834행: *"output is **always** predictable, constrained to your catalog"*.
> `packages/core/src` 를 직접 읽으면 **제약 디코딩(constrained decoding)은 없다.** 있는 것은 네 가지이고 **전부 호출자가 켜야 한다(opt-in)**:
> 1. `catalog.prompt()` — 카탈로그를 시스템 프롬프트로 변환(**프롬프트 수준 유도**)
> 2. `catalog.jsonSchema({ strict: true })` — OpenAI·Gemini·Anthropic 구조화 출력용 JSON Schema 내보내기. **실제 강제는 모델 제공자 쪽**에서 일어난다. 주석이 한계를 자백한다: *"Record types … **cannot be represented** in strict JSON Schema … the JSON Schema for record entries is **opaque**"* (`schema.ts` 110–122행)
> 3. `catalog.validate(spec)` = `zodSchema.safeParse(spec)` (`schema.ts` 460–461행) + `validateSpec()` 구조 검사(누락 root·끊긴 children·`visible` 오배치 등 13개 코드, `spec-validator.ts`)
> 4. `autoFixSpec()` + `formatSpecIssues()` — **무손실/손실 수리를 구분**하고, 오류를 *"repair prompt sent back to the AI"* 로 포맷한다. 주석: *"Callers with a repair loop should **prefer re-prompting over accepting lossy fixes**, and use the lossy-fixed spec as a **last resort**."*
>
> 🔴 그리고 **기본 `Renderer` 는 검증하지 않는다.** `react/src/renderer.tsx` 에 `safeParse`·`validate` 호출 **0건**. 카탈로그에 없는 타입은 `console.warn("No renderer for component type…")` 후 **`return null`**(675–679행) — **조용히 사라진다.** Remotion 렌더러도 동일(`console.warn("Unknown component…")` → `null`).
> 🎯 즉 README의 *"Guardrailed — AI can only use components in your catalog"* 의 정확한 뜻은 **"AI가 카탈로그 밖을 못 쓴다"가 아니라 "카탈로그 밖은 화면에 안 그려진다"** 다.

> [!warning] 🔴 수집기 판정 — 절반 맞음, 절반 볼트 추가
> ✅ 수집기의 *"보장 방식이 README에 명시되지 않음 … 마케팅 문구로 취급"* 은 **정확했다.** README 839행 전체에 보장 메커니즘 설명이 없다.
> 🎯 **볼트 추가**: 코드 확인 결과 답은 **"사후 검증/수리, 그것도 opt-in"** 이다. *"every time"* 은 [[한정어-탈락]] 의 **저자 자기 탈락형** — 코드 주석은 *"last resort"* · *"opaque"* · *"prefer re-prompting"* 으로 한정하는데, README 헤드라인에서 그 한정이 전부 빠졌다.

> [!note] ✅ `@json-render/remotion` 실재 — 단 **변두리 패키지**다
> - `packages/remotion/src/` 실재(`Renderer.tsx` · `schema.ts` · `catalog.ts` · `ClipWrapper.tsx`). npm `@json-render/remotion` **0.21.0**, 2026-02-05 첫 배포.
> - 표준 카탈로그: 컴포넌트 **10**(TitleCard·ImageSlide·SplitScreen·QuoteCard·StatCard·TypingText·LowerThird·TextOverlay·LogoBug·VideoClip) · 전환 **8** · 효과 **3**(kenBurns·pulse·shake).
> - LLM 출력 형식은 **JSONL 패치**(`{"op":"add","path":"/clips/-",…}`) — 한 줄씩 타임라인을 쌓는다. 클립마다 `ClipErrorBoundary`.
> - ⚠️ `Renderer.tsx` 는 `trackId === "main"` 과 `"overlay"` **두 트랙만 그린다** — 스펙에 다른 트랙 ID를 쓰면 클립이 **말없이 누락**된다.
> - 📌 **npm 월간 다운로드(2026-08-22~09-20)**: `core` **5,057,464** vs `remotion` **3,290** — **0.065%**. 18k 스타의 무게는 웹 UI 쪽에 있고, 영상 렌더러는 **거의 안 쓰인다.**

> [!insight] 🎯 볼트 운영자의 [[reat]] 파이프라인과의 대조 — **모양은 같고, 검증을 두는 곳이 다르다**
> 수집기 *"구조가 같다(스키마 → LLM JSON → Remotion 컴포지션)"* ✅ 맞다. 볼트가 로컬 사본(`/tmp/skill-json`, package `new-video-gen`, 최종 커밋 2026-03-31 — **최신판과 다를 수 있음**)과 `reat-layout` 스킬 문서를 대조한 결과:
>
> | 항목 | json-render | reat (`reat-layout` + `StackRenderer`) |
> |---|---|---|
> | 카탈로그 | zod `defineCatalog` | `NODE_REGISTRY` + `docs/node-catalog.md`(산문) |
> | LLM 산출물 검증 | `validate()`(zod) + `validateSpec()` — **코드** | 스킬 문서 784행 **"검증" 체크리스트 12항**(타입 존재·id 유일·enterAt 범위·형제 간격 30프레임·깊이 ≤6…) — **LLM 자기점검** |
> | 저장 API | — | `stack-root/route.ts`: `as { stack_root: StackNode }` 캐스팅 + **존재 여부만** 검사 |
> | 수리 | `autoFixSpec`(무손실/손실 구분) + `formatSpecIssues` → 재프롬프트 | 후처리 스크립트 4종(`sync-enterAt` · `optimize-layout` · `pad-sparse-scenes` · `fix-all-enterAt-gaps`) — **레이아웃 보정**이지 스키마 수리 아님 |
> | 미등록 타입 | `console.warn` + **`null`(보이지 않음)** | 빨간 **`Unknown: {type}`** 박스(**보임**) |
>
> 🎯 **양쪽 다 "매번"은 보장하지 않는다.** json-render가 앞선 것은 **검증을 코드로 두고 재프롬프트 문자열까지 만들어 주는 것**, reat가 앞선 것은 **실패를 화면에 드러내는 것**이다([[검사가능성-공사]]). reat의 체크리스트 12항 중 상당수(타입·id·enterAt 범위·깊이)는 zod `refine` 으로 **그대로 코드화 가능**하다.

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐⭐⭐ — ★18,011 · [[Vercel]] Labs(Organization) · Apache-2.0 · `core` 월 505만 다운로드. 🔴 단 버전 **0.21.0(1.0 이전)** 이고 헤드라인 *"every time"* 은 코드가 뒷받침하지 않는다.
- **즉시 활용**: **YES(부품 차용)** — 프레임워크 전체를 들이기보다 `validateSpec` + `autoFixSpec(lossy:false)` + `formatSpecIssues` 의 **3단 패턴**을 reat의 stack_root에 이식하는 것이 즉효. Remotion 렌더러 자체는 컴포넌트 10종·2트랙 한정이라 reat(`NODE_REGISTRY` 렌더러 27종 · 노드 36+)보다 **좁다** — 교체 대상 아님.
- **6개월 영향력**: "LLM이 JSON을 내고 렌더러가 그린다"가 웹·PDF·이메일·터미널·3D·영상에 **같은 계약**으로 퍼졌다(README 패키지 표 29개). 🎯 **카탈로그가 곧 프롬프트이고 곧 검증기**라는 단일 원천 설계가 표준화된다 — reat의 `node-catalog.md`(산문)와 `NODE_REGISTRY`(코드)가 **이원화**된 것과 대비된다.
- **대체 관계**: [[hyperframes]](HTML→영상)과 같은 층의 대안. reat를 **대체하지 않고 강화**한다(검증 계층).
- **허와 실**: 실(實) = 스트리밍 패치 렌더(SpecStream) · 무손실/손실 수리 구분 · 구조화 출력용 strict 스키마. 허(虛) = *"every time"* · *"always"* · *"AI can only use"* — **셋 다 opt-in 도구의 존재를 기본 동작처럼 말한다.**
- **액션**: 아래.

> [!action] 당장 할 것
> reat `stack_root` 용 zod 스키마 1개를 쓰고(`NODE_REGISTRY` 키 = `z.enum`, 체크리스트 12항 중 기계 판정 가능한 것을 `refine` 으로), `reat-layout` 5단계 뒤에 **validate → 오류 문자열 재프롬프트(최대 N회, 무손실 수리 우선) → 최후에 손실 수리** 루프를 붙인다. 정지 조건은 [[국소-수리-원리]] · [[EASEL]] 과 동일하게 둔다.

## 관련 페이지
- [[Remotion]] · [[스키마-준수-보장]]  *(09-22 연결)*
- [[Vercel]]
- [[vercel-skills]]
- [[reat]]
- [[hyperframes]]
- [[하네스-설계-축]]
- [[한정어-탈락]]
- [[검사가능성-공사]]
- [[국소-수리-원리]]
- [[EASEL]]
- [[video-saas]]
- [[ai-news]]

## 원본
- 출처: https://github.com/vercel-labs/json-render (homepage json-render.dev)
- 볼트 실측(2026-09-22, GitHub API): ★**18,011**(raw 17,685 → +326) · fork **940**(raw 929) · **Apache-2.0** · TypeScript · owner **Organization** · open issues **109**(raw 완전일치) · created 2026-01-14T17:22:39Z · pushed 2026-09-21T22:01:04Z · topics **0개**
- npm(2026-09-22): `@json-render/core` 0.21.0, 월 5,057,464 · `@json-render/remotion` 0.21.0, 월 3,290
- 수치 출처: README 전문 839행 · `packages/core/src/{schema,spec-validator}.ts` · `packages/react/src/renderer.tsx` · `packages/remotion/src/{components/Renderer,schema,catalog}.ts(x)` 원문 실열람 · reat 비교는 로컬 사본 + `/home/ducky/.claude/skills/reat-layout/SKILL.md`
- raw 대비: 볼트 추가 = 🎯 **"every time" 보장 방식 확정(제약 디코딩 없음 · opt-in 사후 검증 + 재프롬프트)** · 🔴 **기본 Renderer 무검증 · 미등록 타입 조용히 누락** · ⚠️ **Remotion 렌더러 2트랙 한정 · 다운로드 0.065%** · 🎯 **reat와 검증 위치 대조표**
- 신뢰도: ⭐⭐⭐ (Vercel Labs · 대량 실사용 · 코드 공개 / 1.0 이전 · 헤드라인 과장)
