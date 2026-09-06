---
title: anthropics/skills — Agent Skills 명세 원본 저장소 (⭐173,849)
type: source
domain: ai-news
tags: [ai-news, github-trending, agent-skills, anthropic, spec, claude-code, plugins]
created: 2026-09-04
updated: 2026-09-06
sources: []
reliability: high
---

# anthropics/skills — 스킬 생태계의 명세 원본

**GitHub**: https://github.com/anthropics/skills
**스타수**: **173,849** (2026-09-04 API 실측 · raw 표기 173,845 대비 **+4**)
**포크 20,615 · 이슈 1,212 · 워치 1,119 · 생성 2025-09-22 · 최종 push 2026-09-03**
**라이선스**: ⚠️ **레포 레벨 라이선스 없음(API `license: null`)** — 하위 폴더별로 갈림

> [!insight] 핵심 인사이트
> 볼트가 **21개 스킬 레포**를 추적하는 동안 정작 빠져 있던 **명세의 원본**이다. 그런데 이 레포의 진짜 포지션은 README 첫 줄이 스스로 밝힌다 — *"이 저장소는 Anthropic의 **구현체**이고, Agent Skills **표준**은 [agentskills.io](http://agentskills.io) 를 보라."* **표준과 구현을 분리해 선언**한 것이다. 즉 벤더가 스펙을 자기 레포에 가두지 않고 밖으로 뺐다. [[agentskills]]·[[claude-skills]]·[[vercel-skills]]·[[google-skills]] 로 이어지는 크로스벤더 확산이 **우연이 아니라 설계**였음을 뒤늦게 확인한 셈이다.

> [!warning] 라이선스가 하나가 아니다 — 이 레포의 가장 실무적인 함정
> API의 레포 레벨 `license`는 **null**이다. README가 층을 나눠 밝힌다:
> - **다수 스킬**: Apache 2.0 (오픈소스)
> - **`skills/docx` · `skills/pdf` · `skills/pptx` · `skills/xlsx`**: **source-available, *not* open source** — Claude의 문서 기능을 실제로 구동하는 프로덕션 코드를 "레퍼런스로 공유"한 것
>
> **⭐173K짜리 레포를 "오픈소스"로 뭉뚱그리면 틀린다.** [[VoiceStudio]]의 2층 라이선스(앱 AGPL / 모델 각자)와 **같은 계열**이며, 볼트의 *"오픈 가중치 ≠ 오픈 시스템"*([[MiniMax-H3]]) 축이 **코드 쪽에서 재현**된 사례다.

> [!note] 레포 자신이 붙인 면책 — 서술 정직성 상위
> *"이 스킬들은 **시연·교육 목적**이다. Claude에서 실제로 제공되는 동작은 여기 구현과 **다를 수 있다**. 중요한 작업에 의존하기 전 반드시 자체 환경에서 테스트하라."*
> → 벤더 공식 레포가 **자기 구현과 자사 제품 동작의 불일치 가능성을 먼저 밝혔다.** [[VoiceStudio]]의 *"646 언어, 단 실제 커버리지는 엔진에 달림"* 과 같은 **주장 약화형 정직성**. 볼트의 *"배지를 근거로 쓰지 않는다"* 규칙이 이번에도 **역방향**으로 걸린다.

## 구조 (README 실측)

- **`./skills`** — 창작·디자인 / 개발·기술 / 엔터프라이즈·커뮤니케이션 / 문서 스킬 예제
- **`./spec`** — Agent Skills **명세**
- **`./template`** — 스킬 템플릿
- 각 스킬은 `SKILL.md` 하나에 지시문 + 메타데이터를 담은 **자기완결 폴더**

배포 경로가 **플러그인 마켓플레이스**로 정식화돼 있다:
```
/plugin marketplace add anthropics/skills
/plugin install document-skills@anthropic-agent-skills
/plugin install example-skills@anthropic-agent-skills
```

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐⭐⭐⭐⭐ — **볼트 추적 레포 중 최상위권 스타(173,849)**, 벤더 공식, 명세 보유. 단 라이선스는 단일하지 않음.
- **즉시 활용**: **YES.** 이 볼트의 `/wiki` 스킬을 포함해 `~/.claude/skills/` 전체가 이 명세를 따른다. `./spec` 을 읽어 **현재 볼트 스킬들이 명세를 어긋나게 쓰고 있는지** 대조할 수 있다 — 지금까지 볼트는 [[agent-skills]]·[[awesome-claude-skills]] 등 **파생물만** 봤고 원본 스펙을 대조한 적이 없다.
- **6개월 영향력**: 스킬이 **폴더 = 배포 단위**로 굳으면, 볼트의 인제스트 파이프라인 자체를 스킬로 패키징해 재사용·공유할 수 있다. `template/` 이 그 출발점.
- **대체 관계**: 대체가 아니라 **상위 규격**. [[claude-skills]](alirezarezvani, ⭐20,831)·[[mattpocock-skills]]·[[superpowers]] 는 전부 이 스펙의 소비자다. **볼트는 5개월간 소비자만 보고 생산자를 안 봤다.**
- **허와 실**: 스타 수가 곧 스킬 품질은 아니다 — 173K는 **Claude Code 사용자 기반의 크기**를 재는 값에 가깝다. 실제 검증 대상은 `./spec` 의 엄밀성이다.

> [!action] 당장 할 것
> `./spec` 원문을 받아 이 볼트의 `/wiki` `SKILL.md` 와 **필드 단위 대조**. 특히 트리거 조건·메타데이터 스키마가 명세와 맞는지 확인. 문서 스킬 4종(`docx`/`pdf`/`pptx`/`xlsx`)은 **라이선스가 다르므로 복사·재배포 금지**, 열람만.

> [!question] 미해결
> `agentskills.io` 의 표준과 이 레포 `./spec` 이 **버전이 같은가.** 표준을 밖에 뒀다는 선언은 좋지만, 둘이 갈라지면 크로스벤더 호환의 근거가 무너진다. **다음 회차 확인 대상.**

---
## 📊 2026-09-06 재관측 (GitHub API 실측)
⭐ **174,699** · fork **20,684** · 오픈이슈 **1,210** · **라이선스 `None`(레포 레벨 null 재확인)**
raw 09-06 수집값 ⭐174,695와 일치. 09-04 기록 ⭐173,849 → **+850**.
> [!warning] ⚠️ 09-04에 기록한 라이선스 함정이 **API로 재확인**됐다
> 레포 레벨 라이선스가 **여전히 `null`** 이다. ⭐17만을 "오픈소스"로 뭉뚱그리면 틀린다는 기존 경고 유지 — 문서스킬 4종(`docx`/`pdf`/`pptx`/`xlsx`)은 **source-available**.
> 미해소 이월 항목(*`./spec`과 agentskills.io 표준의 버전 일치 여부*)은 **여전히 미확인**.

## 관련 페이지
- [[Anthropic]] · [[에이전트-스킬]] · [[agentskills]] · [[claude-skills]] · [[awesome-claude-skills]] · [[mattpocock-skills]] · [[vercel-skills]] · [[google-skills]] · [[superpowers]] · [[ponytail]] · [[humanizer]] · [[Repo-To-Skill]] · [[claude-obsidian]] · [[LLM-Wiki]]

## 원본
- 출처: https://github.com/anthropics/skills
- 수집: 2026-09-04 자동수집 (ai-news)
- 검증: README defuddle 원문 + GitHub API 실측 (2026-09-04)
- 신뢰도: ⭐⭐⭐⭐⭐
