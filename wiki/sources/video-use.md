---
title: browser-use/video-use — 코딩 에이전트로 영상을 편집하는 도구
type: source
domain: ai-news
tags: [ai-news, github-trending, video-editing, ai-agent, video-saas, automation, claude-code]
created: 2026-06-30
updated: 2026-09-02
sources: []
reliability: high
---

# video-use (browser-use/video-use)

> [!update] 2026-09-02 갱신 — ⭐14,077(2026-07-03) → **23,275**(+**9,198**·약 1.65배) · ⚠️**푸시 08-30 = 3일 정체**
> **61일 만의 재관측.** 일평균 약 **+151**. 포크 **2,830** · 이슈 **81** · MIT · 푸시 **2026-08-30**.
> **이슈/포크 0.0286**(81/2,830)로 **이번 배치 GitHub 5건 중 2위**([[OpenMAIC]] 0.0459 다음). 볼트 규칙대로 밀도로 읽으면 **실제로 돌려보다 막히는 사람이 상대적으로 많다** — 영상 편집은 산출물이 눈에 보이므로 실패가 곧바로 이슈로 보고되는 유형이다. [[academic-research-skills]](0.0053)·[[minimind]](0.0079) 같은 프롬프트/교육 자산과 **정반대 성격**이며, 이 대비가 **"이슈 밀도는 도메인 특성을 먼저 반영한다"** 는 것을 보여준다 — 레포 간 밀도 비교 시 주의할 점으로 기록.
> 아키텍처 판정은 유지된다: **LLM이 영상을 보지 않고 읽는다** — ElevenLabs Scribe로 단어 단위 타임스탬프·화자 분리를 뽑아 `takes_packed.md`로 만들고 그것을 근거로 편집한다.
> 같은 배치 [[OpenClaude]]와 나란히 놓으면 **"코딩 에이전트 하네스를 특정 도메인에 태운다"** 는 같은 패턴의 두 갈래다 — video-use는 *도메인 이식*(웹→영상), OpenClaude는 *백엔드 이식*(Claude→임의 LLM). 전자는 MIT로 깨끗하고, 후자는 배포 권한을 자체 부인한다.
> ⚠️ 지원 편집 연산 범위·실패율·처리 시간 등 **능력 경계 수치는 여전히 미검증**.
> **지표(2026-09-02)**: ⭐**23,275** · 포크 **2,830** · 이슈 **81** · Python · **MIT** · 생성 2026-04-12 · 푸시 2026-08-30 — GitHub REST 실호출. raw 23,271 대비 **+4**.

> [!insight] 핵심 인사이트
> ⭐14,077 (2026-07-03, 당일 +554) ← ⭐12,888 (07-01). **"Claude Code로 영상을 편집한다"** — 원본 푸티지를 폴더에 넣고 에이전트와 대화하면 `final.mp4`가 나온다. 핵심은 *LLM이 영상을 보지 않고 읽는다*는 설계: ElevenLabs Scribe로 단어 단위 타임스탬프·화자 분리·오디오 이벤트를 뽑아 `takes_packed.md`(~12KB)로 만들고, 이를 근거로 필러 단어(`umm`,`uh`) 제거·컷·색보정·자막·30ms 오디오 페이드·애니메이션 오버레이(HyperFrames/Remotion/Manim/PIL)를 수행한다. 만든 곳이 [[browser-use]](웹 자동화 에이전트로 유명한 조직)라는 점이 핵심 — "에이전트가 브라우저를 조작하듯 타임라인을 조작한다"는 동일 패턴의 도메인 확장. [[OpenMontage]] 계보에 합류하며, 같은 배치의 [[superpowers]]·[[agency-agents]]와 마찬가지로 *코딩 에이전트를 특정 도메인 작업에 태우는* 흐름의 영상판이다.

## 도메인별 추출 (ai-news / video-saas)

- **신뢰도**: ⭐⭐⭐⭐ — ⭐14K + 3일 연속 유입 + [[browser-use]]라는 검증된 조직 출처. "LLM은 영상을 읽는다(transcript 기반)"는 아키텍처가 구체적이라 실용성 기대치 높음. 100% 오픈소스.
- **즉시 활용**: MAYBE — Claude Code/Codex에 스킬 등록 + ffmpeg + ElevenLabs API 키 필요. 내 [[video-saas]] 워크플로에 "자연어 → 편집 명령" 레이어 레퍼런스로 유용. [[reat-render]]/[[reat-slides]] 파이프라인에 편집 지시 에이전트를 얹는 구조 참고 가능.
- **6개월 영향력**: 높음 — 영상 편집이 "타임라인 수작업"에서 "에이전트에게 지시"로 이동하는 신호. 특히 **transcript(단어 타임스탬프) 기반 컷**은 토킹헤드·튜토리얼 편집에서 실효성이 크다. [[OpenMontage]]·[[After-Effects-MCP]]와 함께 편집 자동화 에이전트 카테고리를 굳힘.
- **대체 관계**: 기존 NLE(Premiere/Resolve) 대체가 아니라 그 위에 자연어 지시 레이어를 얹는 보강. 컷·자막·색보정 등 반복 노동을 자동화. [[After-Effects-MCP]](AE 자동화)와 용처가 겹친다.
- **허와 실**: transcript 기반이라 **음성 없는 순수 비주얼 편집·미세 타이밍·창의적 몽타주**는 약할 수 있다. 단어 경계 컷·필러 제거·자막은 강하지만 "감각적 편집"은 여전히 사람 몫. 자기 평가(self-evaluate) 루프가 있으나 최종 품질은 검증 필요.
- **액션**: star + `takes_packed.md`·`timeline_view` 등 "영상을 텍스트로 읽는" 구조 분석 → 내 영상 파이프라인의 자동 컷·자막 단계 설계에 이식.

> [!action] 당장 할 것
> 짧은 토킹헤드 클립으로 설치·시험 → transcript 기반 필러 제거·컷 품질 체감하고, 자연어 지시가 어떤 편집 프리미티브(컷/자막/색보정/전환)로 분해되는지 매핑 방식 파악. [[OpenMontage]]·[[After-Effects-MCP]]와 추상화 레이어 비교.

## 관련 페이지
- [[browser-use]]
- [[OpenMontage]]
- [[After-Effects-MCP]]
- [[video-saas]]
- [[AI-영상-생성-2026]]
- [[superpowers]]
- [[agency-agents]]
- [[caveman]]
- [[바이브코딩]]

## 원본
- 출처: https://github.com/browser-use/video-use
- 스타: ⭐14,077 (2026-07-03, 당일 +554) ← ⭐12,888 (07-01, +721) ← ⭐12,216 (06-30)
- 신뢰도: ⭐⭐⭐⭐ (검증된 browser-use 조직 출처 + 3일 연속 유입, transcript 기반 아키텍처 구체적)
