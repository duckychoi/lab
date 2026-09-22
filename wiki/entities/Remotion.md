---
title: Remotion
type: entity
domain: video-saas
tags: [video-saas, remotion, react, 영상자동화, rendering, 본체-누락]
created: 2026-09-22
updated: 2026-09-22
sources: [json-render.md, hyperframes.md, video-shotcraft.md, stitch-skills.md, openai-plugins.md, Programmable-World-Model.md, MoneyPrinterTurbo.md]
reliability: medium
---

# Remotion

React 컴포넌트를 **프레임 단위로 렌더해 영상(mp4)을 만드는** 프레임워크. 사용자의 [[reat]] 영상 파이프라인(`/reat-render` · Scene DSL → TSX)의 **렌더 엔진**이다.

> [!insight] 🎯 볼트가 이 페이지 없이 **13개 페이지**에서 Remotion을 언급해 왔다
> 2026-09-22 grep 실측: sources 9 · entities 2 · domains 2 에서 언급, **엔티티 페이지 0**. [[browser-use]]·[[HuggingFace]]·[[mem0]] 에 이은 **본체 누락 4번째** — 이번 것은 **사용자 자신의 스택**이라는 점이 다르다.
> 볼트에 쌓인 Remotion 관련 언급을 한 곳에 모으면 **한 가지 방향**이 보인다: 벤더들이 Remotion을 **에이전트가 쓰는 출력 타깃**으로 편입하고 있다.
> - [[openai-plugins]] — 플러그인 예제에 `remotion` 포함
> - [[stitch-skills]]([[Google-Labs]]) — Build 플러그인에 Remotion 영상 생성
> - [[video-shotcraft]] — Remotion 제품영상 에이전트 스킬 157 레시피
> - [[json-render]]([[Vercel]] Labs) — `@json-render/remotion` 렌더러(0.21.0, 컴포넌트 10종)
> - 대체재: [[hyperframes]](HTML/GSAP, React 없음)

> [!warning] 🔴 "편입"은 채택과 다르다
> [[json-render]] npm 월 다운로드: core **5,057,464** vs remotion 렌더러 **3,290**(**0.065%**) — 2026-09-22 서브에이전트 실측. **벤더가 Remotion 타깃을 만들었다는 것과 그것이 쓰인다는 것은 별개다.** 볼트는 Remotion 본체의 다운로드·라이선스 조건을 **직접 조회하지 않았다**(⬜ 미검증).

## 사용자 파이프라인과의 관계
- [[reat]] = 자막(SRT) → beats → scene-plan → Scene DSL → **Remotion 컴포지션** → mp4
- [[json-render]] 와 **구조가 같다**(스키마 → LLM JSON → 렌더러). 차이와 이식 가능한 부분은 [[스키마-준수-보장]] 참조.
- [[Programmable-World-Model]] 의 해석: beats/scene-plan = 프로그램, **Remotion = 결정적 컴파일러**, 비디오 모델 = 렌더러.

## 관련 페이지
- [[json-render]] · [[hyperframes]] · [[video-shotcraft]] · [[stitch-skills]] · [[openai-plugins]] · [[Programmable-World-Model]] · [[MoneyPrinterTurbo]] · [[video-use]] · [[Pascal-Editor]]
- [[스키마-준수-보장]]
- [[video-saas]]
