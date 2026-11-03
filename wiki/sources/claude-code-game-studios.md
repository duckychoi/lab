---
title: Donchitos/Claude-Code-Game-Studios
type: source
domain: ai-news
tags: [ai-news, claude-code, game-dev, agent, orchestration, workflow]
created: 2026-04-16
updated: 2026-11-03
sources: []
reliability: medium
---

# Claude Code Game Studios

> [!insight] 핵심 인사이트
> Claude Code를 49개 AI 에이전트·72개 워크플로우로 구성된 완전한 게임 개발 스튜디오로 변환하는 조율(orchestration) 시스템. ⭐10,867(당일 +612). Claude Code 에코시스템 확장의 극단적 사례.

## 핵심 인사이트

**스펙:**
- GitHub ⭐10,867 (당일 +612)
- 내용: 49 에이전트 + 72 워크플로우 + Claude Code 오케스트레이터
- 용도: 게임 개발 전 파이프라인 AI 자동화

> [!note] 배경 정보
> [[claude-code-best-practice]](⭐39K), [[andrej-karpathy-skills]](⭐37K), [[claude-mem]](⭐56K)과 함께 Claude Code 에코시스템이 독자 생태계를 형성하는 또 다른 증거. 이번엔 게임 개발 특화.

**아키텍처 특징:**
- 다중 에이전트 역할 분리: 스토리작가, 레벨디자이너, 코더, QA 등
- Claude Code sub-agent 병렬 실행
- 워크플로우 DAG 기반 의존성 관리

> [!action] 당장 할 것
> 에이전트 오케스트레이션 아키텍처 설계 레퍼런스로 읽기. 게임 외 도메인에 패턴 이식 가능.

## 관련 페이지

- [[Claude-Code-워크플로우]]
- [[AI-에이전트-프레임워크]]
- [[claude-code-best-practice]]
- [[andrej-karpathy-skills]]

## 원본

- 출처: https://github.com/Donchitos/Claude-Code-Game-Studios
- 신뢰도: ⭐⭐ (⭐10,867, 커뮤니티 프로젝트 — 실제 게임 산출물 검증 필요)

## 🔄 2026-11-01 갱신 — **템플릿 제작자가 "문서를 더 쓰면 게임이 나빠졌다"고 측정해 공개했다**

**GitHub API**: ★**31,493**(04-16 10,867에서 2.9배 · 수집기 +5 드리프트) · fork 4,310 · MIT · 푸시 10-19.

> [!insight] 간판 기능의 가치를 스스로 깎은 측정
> 한 브리프로 게임 4개를 엄격도별로 만들어 코드 전 문서 수를 셌다. `minimal` 1개(0분) · `standard` 30개(58분). 전부 실행되고 테스트도 통과했지만, 블라인드 리뷰어 2명과 사람 플레이테스트가 **standard를 최하위**로 뒀다. 결론: 추가 문서 29개는 추적성을 샀을 뿐 더 나은 게임을 사지 않았다. 그래서 **기본값이 `minimal`** 이다. [[superpowers]] 설계문서 생략 건과 같은 축이다 → [[에이전트-스킬]].

> [!warning] 표본과 정정
> - 브리프 1개 · 게임 4개 · 리뷰어 2명의 자체 측정이다. README 표에는 4개 중 2행만 보인다.
> - 스킬 수: 저장소 설명 72 · README 74(수집기 일치). 04-16 "72 워크플로우" 표기는 설명 기준.
> - 🔴 04-16 본 페이지의 "워크플로우 DAG 기반 의존성 관리" · "스토리작가, 레벨디자이너" 예시는 이번 README 확인 범위에서 근거를 다시 찾지 않았다. 신뢰하지 말 것.

- **즉시 활용**: 게임 개발은 NO. 다른 에이전트 템플릿을 도입할 때 **가장 가벼운 단계부터 시작**할 근거로 쓴다.

## 🔄 2026-11-02 갱신 (인제스트 2026-11-02) — ★32,830 · **스킬 수는 실측 74 (설명 72는 낡은 값) · v1.2.0이 "모든 셸 명령 사전 승인"을 걷어냈다**

**GitHub API 실측(11-02 09시대)**: ★**32,830**(수집기 32,828 · +2 드리프트) · fork 4,456 · open_issues 76 · MIT · 언어 Shell ✅ · pushed **2026-10-19**(2주째 푸시 없음) · 최신 릴리스 **v1.2.0(10-19)** "the main path, rebuilt and tested"
- 📈 볼트 마지막 기록 ★31,493(11-01) → **+1,337 / 1일**(수집기 당일 +967과 측정 창이 다름 — 트렌딩 값은 API로 재현 못 함).
- ✅ 수집기 서술 확인: 49 에이전트(README 6·12·57행, `.claude/agents` 디렉터리 **49개** 실측) · Godot 4 / Unity / Unreal Engine 5(98~100행).
- ⚖️ 수집기 오류: **"72 워크플로우 스킬"은 저장소 description 값이다.** README는 74(6·13·104·293행), `.claude/skills` 디렉터리 실측도 **74개**다. 11-01 갱신에서 적은 72/74 불일치가 그대로이고, 실물 기준은 74다.
- ⚖️ 그 밖의 카운트: README 배지 hooks 15 · rules 14. `.claude/rules` 실측 14 ✅ · `.claude/hooks` 항목 **18개**(공용 스크립트 포함 여부는 🔴 미확인이라 불일치로 단정하지 않는다).

> [!note] 권한 측면 (수집기 누락)
> - v1.2.0 노트: *"no skill pre-approves every shell command any more"* — **이전 버전에는 모든 셸 명령을 사전 승인하는 스킬이 있었다**는 뜻이다. 1.2.0 미만 템플릿을 복사해 쓰고 있다면 갱신 대상.
> - 현재 `.claude/settings.json`: `defaultMode: default` · allow는 `dir`, `pytest` 정도 · deny에 `rm -rf` 변형·`git push --force`·`git reset --hard`·`git clean -f` 류를 길게 나열. 문자열 패턴 차단이라 우회 가능성은 남는다(볼트 판단).
> - v1.2.0은 큰 설계 문서 통째 읽기를 막는 read guard를 추가했다 — 토큰 비용 관리 장치.

- 기본 rigor `minimal`(README 220·224행) 유지 — 11-01 갱신의 "문서를 더 쓰면 게임이 나빠졌다" 측정과 일관.

## 🔄 2026-11-03 갱신 (인제스트 2026-11-03) — ★34,011 · **실측 에이전트 49·스킬 74 재확인(설명 72 그대로) · 15일 무푸시에 하루 +1,181**

**GitHub API 실측(11-03 09시대)**: ★**34,011**(수집기 34,005 · +6) · fork **4,556**(수집기 4,555) · open_issues **92** · MIT ✅ · Shell ✅ · pushed **2026-10-19T02:43Z**(HEAD `05ad7c8` "Release 1.2.0", 이후 커밋 0) · 최신 릴리스 **v1.2.0(10-19)** — 신규 릴리스 없음 · description 여전히 *"49 AI agents, 72 workflow skills"*
- 📈 볼트 마지막 기록 ★32,830 · fork 4,456 · open_issues 76(11-02) → **★ +1,181 · fork +100 · open_issues +16 / 1일.** 04-16(★10,867) 대비 3.1배.
- ✅ **카운트 재측정**(측정 경로: `api.github.com/repos/Donchitos/Claude-Code-Game-Studios/git/trees/HEAD?recursive=1`, 782 항목 · `truncated: false`):
  - `.claude/agents/*.md` = **49** ✅(설명·README 일치)
  - `.claude/skills/` 직속 하위 디렉터리 = **74**, 그중 `SKILL.md` 보유 **74** ✅ — README 6·104·293행 "74 skills" 일치, description "72"는 낡은 값(11-01·11-02 볼트 판정 유지).
  - `.claude/rules/` = **14** ✅(배지 일치) · `.claude/hooks/` 항목 = **18**(배지 15 — 공용 스크립트 포함 여부 🔴 미확인, 11-02와 동일).
  - ⇒ 수집기 "에이전트 49 일치 · 스킬 +2" ✅ 정확하고 측정 경로까지 명시했다.
- ✅ 수집기 서술 확인: v1.2.0 = 스토리 스킬 헬퍼 스크립트 중심 재작성 · 대용량 설계문서 전체읽기 차단 가드 · Godot 4.7/UE 5.8 레퍼런스. 🔴 품질·완성도 측정값 0건 — 단 볼트 11-01 기록대로 **README에 rigor별 게임 4개 비교(문서 많을수록 최하위)라는 자체 측정이 있다.** 수집기의 "측정값 0건"은 "외부·정량 벤치 0건"으로 좁혀 읽어야 한다(🟡 경미한 과잉 일반화).
- ⚖️ 수집기 누락: v1.2.0의 **"no skill pre-approves every shell command any more"**(권한 축소) — 11-02 볼트가 기록, 수집기 요약에는 없음.

> [!insight] 코드가 멈춘 템플릿이 하루 +1천씩 오른다
> 마지막 커밋 15일 전, 릴리스 없음, open_issues는 하루 +16. 관심 지표(★·fork·이슈)가 전부 상승하는데 저장소 내용은 10-19에서 고정이다. 이 성장은 **변경이 아니라 노출(트렌딩 체류) 효과**로 읽힌다 — 3일 연속 트렌딩(11-01·11-02·11-03). description 72 → 실측 74 불일치가 15일째 방치되는 것도 같은 신호다 → [[메타데이터-부재-추론]] · [[스타-근거-비동행]].

- **수집기 평가**: 이번 배치 5건 중 가장 정확(카운트·경로 일치). 감점은 "측정값 0건"의 범위 과잉 하나.
- **즉시 활용**: 변동 없음 — 다른 에이전트 템플릿 도입 시 `minimal` 단계부터 시작하는 근거로만 쓴다 → [[에이전트-스킬]] · [[superpowers]].
