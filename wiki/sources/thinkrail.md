---
title: "JetBrains/thinkrail — pi 코딩 에이전트를 감싼 경량 에이전틱 IDE. worktree 격리 · SPEC.md 그래프 · 'JetBrains incubator' 배지"
type: source
domain: ai-news
tags: [ai-news, github-trending, agentic-ide, coding-agent, pi, jetbrains, git-worktree, spec-driven, agent-skills]
created: 2026-10-27
updated: 2026-10-27
sources: [https://github.com/JetBrains/thinkrail]
reliability: medium
---

# JetBrains/thinkrail

**GitHub**: https://github.com/JetBrains/thinkrail · 웹 https://thinkrail.ai/
**실측(2026-10-27T09:05Z · GitHub API)**: ★ **3,360**(수집기 3,353 · +7) · fork 179 · 🔴 **open issues 226**(★ 대비 6.7%) · Apache-2.0 · TypeScript · created **2026-07-08**(3.5개월) · pushed 10-27(당일)
**신뢰도**: ⭐⭐ medium (JetBrains 공식 org · 단 README 첫 배지가 **"JetBrains incubator project"** — 정식 제품 아님)

> [!insight] 핵심 인사이트 — **JetBrains 가 자기 IDE 가 아니라 서드파티 에이전트(pi) 위에 새 IDE 를 지었다**
> 엔진은 [[pi-agent-harness]](`@earendil-works/pi-coding-agent` npm — 볼트 09-16 실측 ★106,058). thinkrail 은 그 위에:
> - **격리 워크스페이스** = `git worktree` 단위 브랜치 · 병렬 에이전트 · 머지 후 자동 "Settled shelf" 정리 · PR/CI 상태 연동(`gh` 사용)
> - **Specs as ground truth** — 코드 옆 `SPEC.md` 그래프를 에이전트가 `spec_*` 전용 도구로 읽고·검색하고·유지 ⇒ 세션이 끝나도 의도가 남는다
> - 기존 **Agent Skills 를 제자리에서 읽음**(다른 코딩 에이전트용 스킬 재사용) · 세션별 모델·토큰·비용 실시간 표시
> ⇒ 볼트 위키(CLAUDE.md 스키마 + index.md)가 사람 손으로 하는 일을 IDE 기능으로 만든 형태. 🔴 README 표현 *"building its own capabilities tomorrow"* — **자기 확장 기능은 예정**(수집기 표기 ✅ 정확).

> [!warning] 주의
> - 🔴 **이슈 226 / ★3,360** — 초기 프로젝트 치고 높다(활발한 피드백이거나 미성숙). 분류(버그/기능) 미확인.
> - ⚖️ 오늘 +1,173★(수집기) 는 트렌딩 하루치 — 3.5개월 누적의 1/3이 하루에 들어왔다 ⇒ 지속성 판정은 2주 후.
> - 📌 pi 의 알려진 약점 — 볼트 [[pi-agent-harness]] 제목 그대로 *"권한 모델 부재를 README에 먼저 적는"* 하네스. worktree 격리가 파일 범위는 줄이지만 **셸 권한 문제는 해소하지 않는다**(추정 · 코드 미확인).

## 도메인별 추출 (ai-news)
- **즉시 활용**: 조건부 — pi 를 쓰지 않으면 직접 이득 없음. 단 **"SPEC.md 그래프 + 전용 도구"** 패턴은 Claude Code 에도 이식 가능한 설계 아이디어.
- **6개월 영향력**: IDE 벤더가 자체 에이전트(JetBrains AI/Junie) 와 별도로 **오픈 에이전트 위 경량 IDE** 를 실험 — 하네스와 IDE 의 분리 경향(추정).
- **대체 관계**: [[cindy]](하네스 교체형 클라이언트) · Cursor 류와 같은 층. [[Trial-by-Trace]] 기준으로는 아직 평가 대상 밖.

## 관련 페이지
- [[pi-agent-harness]] · [[에이전트-스킬]] · [[하네스-설계-축]] · [[AI-에이전트-프레임워크]]
- 같은 배치: [[cindy]] · [[ECC]] · [[hallmark]] · [[Trial-by-Trace]]
- [[ai-news]]

## 원본
- README https://raw.githubusercontent.com/JetBrains/thinkrail/HEAD/README.md (볼트 열람 · 앞 5,000자)
- 볼트 실측(2026-10-27T09:05Z UTC): ★3,360 · fork 179 · issues 226 · Apache-2.0
