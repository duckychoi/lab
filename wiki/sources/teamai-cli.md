---
title: "Tencent/teamai-cli — 팀 단위 에이전트 하네스 동기화 CLI"
type: source
domain: ai-news
tags: [ai-news, github, agent-harness, skills, mcp, team, tencent]
created: 2026-09-10
updated: 2026-09-10
sources: []
reliability: medium
---

# teamai-cli

> [!insight] 핵심 인사이트
> 에이전트 설정(skills/rules/MCP/docs)을 **개인 dotfile이 아니라 공유 git 레포의 리뷰 대상**으로 끌어올린 도구. 배포 경로가 `push → MR 리뷰·머지 → SessionStart 훅이 pull` 이다.
> → **에이전트 설정에 코드리뷰를 붙인다**는 발상. 스킬이 늘어날수록 "누가 언제 왜 이 룰을 넣었나"가 사라지는 문제를 git으로 푼다.

> [!warning] 🔴 raw의 판정을 볼트가 뒤집었다 — 라이선스
> raw: *"실제 LICENSE 파일은 **Tencent 자체 라이선스**이고 GitHub API는 `NOASSERTION`. **배지를 신뢰하면 안 됨**"*
> **LICENSE 원문 실측(1,418바이트) 결과 이는 틀렸다.** 파일 5행은 그대로 이렇게 쓴다:
> > *"teamai-cli is licensed under **MIT**. teamai-cli does not impose **any additional restrictions** beyond those specified in the license."*
> 이어서 **MIT 전문이 축약 없이 그대로** 실려 있다(`grep -ci MIT` = 4회).
> **실체는 MIT다.** GitHub이 `NOASSERTION`을 반환한 이유는 자체 라이선스여서가 아니라, 파일 **머리에 Tencent 인사말 2줄이 붙어 licensee 자동탐지 정규식이 깨졌기** 때문이다.
> → raw는 **API의 파생 분류를 원문보다 신뢰**했다. 배지가 아니라 **raw가** 틀렸다.

> [!insight] 이번 배치가 만든 새 규칙 — API의 파생 분류는 원문이 아니다
> 볼트는 그동안 *"description은 소스가 아니다"*(09-08) → *"이름도 소스가 아니다"*(09-09) 를 쌓아왔다. 여기에 한 줄이 추가된다:
> **"API가 계산해준 필드도 소스가 아니다."**
> `license.spdx_id` 는 GitHub이 파일을 **추측**한 결과지 파일 자체가 아니다. `NOASSERTION` 은 *"라이선스가 아니다"* 가 아니라 *"내 정규식이 못 읽었다"* 는 뜻이다.
> → [[측정도구-먼저-반증]] 의 메타 레벨 사례: **계측기가 아니라 계측기의 출력 포맷에 속았다.**

> [!note] 지원 범위 — 표기가 균일하지 않다
> README 개요표 기준 **에이전트 11종**: Claude Code · Codex · Cursor · CodeBuddy · WorkBuddy · OpenCode · OpenClaw · Hermes · DeepSeek Harness · Qoder · ZCode.
> **커버리지는 균일하지 않다** — Team Execution 7항목 전체 지원은 **Claude Code · Codex · Cursor · CodeBuddy · Qoder** 뿐이고 **DeepSeek Harness는 skills/docs만**.
> 3층 구조 중 **2층이 beta** — README 59·64·65행에서 `Team Context (beta)` · `Team Improvement (beta)` 확인. 즉 **완성된 층은 Team Execution 하나**.
> 역할(roles)·태그(tags)별 구독 분기 지원.

> [!warning] raw가 맞춘 것 — 숫자 출처 불일치
> README 소개문(14행)은 지원 대상을 6종+"기타"로, 개요표는 11종으로 쓴다. **표를 채택**한 raw의 판단은 타당하다(표가 항목별 커버리지까지 명시하므로 더 구체적인 증거).

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐3,387(실측 2026-09-10, raw 3,377 대비 **+10**) · 포크 214 · 이슈 22 · TypeScript · 생성 2026-04-27 · pushed 2026-09-10. **당일 +556 급상승**. 4개월 된 레포에 Tencent 조직 이름 — 스타는 조직 신뢰에서 온 몫이 크다.
- **즉시 활용**: **조건부 YES.** 나는 이미 스킬을 다수 운용하고 `~/.claude/skills/` 가 비대하다. 다만 **1인 사용자에게 MR 리뷰 루프는 과설계**다. 가져올 것은 도구 자체가 아니라 **"SessionStart 훅이 pull 한다"는 배포 패턴** 하나.
- **6개월 영향력**: 에이전트 설정이 **팀 자산**으로 취급되기 시작하는 신호. 지금은 각자 dotfile이지만, 스킬이 조직 단위로 늘면 버전관리·리뷰·롤백이 필수가 된다.
- **대체 관계**: 내 수동 스킬 복사를 대체 가능. [[에이전트-스킬]] 생태계에서 **배포 계층**을 맡는 도구.
- **허와 실**: 3층 중 2층이 beta이고 11종 중 5종만 완전 지원 — **"Make Every Team AI Native"** 라는 문구 대비 실제 완성도는 낮다. 급상승은 코드 성숙도가 아니라 **Tencent 공개**라는 이벤트다.
- **액션**: 설치하지 말고 **SessionStart 훅 배포 패턴만 읽고 차용**.

> [!action] 당장 할 것
> `.claude/settings.json` 의 SessionStart 훅으로 **스킬 디렉터리를 git pull 하는 1줄**만 실험. 도구 전체 도입은 불필요.

> [!question] 미해결 질문
> Hermes 지원이 표에 있으나 커버리지가 얕다. [[NousResearch]] Hermes 계열과 실제로 연동되는지, 아니면 이름만 올린 것인지 미확인.

## 관련 페이지
- [[Tencent]]
- [[에이전트-스킬]]
- [[측정도구-먼저-반증]]
- [[Claude-Code-워크플로우]]
- [[AI-에이전트-프레임워크]]
- [[PI-Desktop]]
- [[openai-plugins]]

## 원본
- 출처: https://github.com/Tencent/teamai-cli
- 실측(2026-09-10): ⭐**3,387** · 포크 214 · 이슈 22 · pushed 2026-09-10T09:07:49Z · TypeScript · API `NOASSERTION`
- **LICENSE 원문 실측: MIT 전문 수록 — 실체는 MIT** (raw 판정 반증)
- raw 대비 드리프트: 스타 +10(자연 증가) · **라이선스 판정 1건 반증**
- 신뢰도: ⭐⭐ (2/3 층 beta · 커버리지 불균일 · 벤치마크 없음 · 조직 프리미엄)
