---
title: DeepSWE — 오염을 피해 "창작된" 113개 장기 SWE 과제 벤치마크 (⭐1,604)
type: source
domain: ai-news
tags: [ai-news, github-trending, benchmark, coding-agent, evaluation, contamination, harbor]
created: 2026-09-04
updated: 2026-09-04
sources: []
reliability: high
---

# datacurve-ai/deep-swe — 검증기를 환경 밖으로 뺀 평가

**GitHub**: https://github.com/datacurve-ai/deep-swe
**스타수**: **1,604** (2026-09-04 API 실측 · raw와 **완전 일치**)
**포크 106 · 이슈 72 · 워치 7 · 라이선스 **Apache-2.0** · 생성 2026-05-15 · 최종 push 2026-08-26
**이슈/포크 밀도 0.679 — 볼트 관측 중 이례적으로 높음**

> [!insight] 핵심 인사이트
> 이 벤치마크의 설계는 볼트가 [[검사가능성-공사]]에서 벼려 온 문제의식과 **정확히 같은 곳을 찌른다** — *채점자를 피채점자에게서 떼어내라.* 세 겹으로 구현돼 있다: ① **과제가 원본 창작**(활성 오픈소스 레포 기반, 기존 벤치마크 오염 회피) ② **검증기가 별도 환경**(v1.1부터 에이전트 작업 환경과 채점 환경 분리, 커밋을 패치로 추출해 **깨끗한 컨테이너**에서 채점) ③ **행동 기반 채점**(내부 심볼명·구조 무관, 관측 가능한 동작만 봄). 참조 해답은 `solution/` 에 있지만 **채점에 절대 쓰이지 않고** 리뷰어 오프라인 점검용으로만 존재한다. → [[EarlyEval]]의 *"검사기를 LLM 밖에"* 가 **평가 인프라 층위에서 재현**된 형태.

> [!note] 규모는 작고 호흡은 길다 — SWE-bench 계열과의 차이
> **113개 과제**뿐이다(TypeScript·Go·Python·JavaScript·Rust). 대신 *long-horizon*(장기 호흡)이고 격리 환경 + 프로그램 기반 검증기를 과제마다 갖춘다. **개수를 줄이고 과제당 깊이를 샀다** — 볼트가 반복 관측한 *"개수는 품질을 보증하지 않는다"* 의 **반대편 선택**이며, 이 배치에서 [[prompts-chat]]·[[claude-skills]]의 개수 자랑과 **정면 대비**된다.

## 구조 (README 실측)

**Harbor 태스크 포맷**:
```
task.toml         메타(레포·베이스 커밋·언어·이미지·제한)
instruction.md    에이전트가 보는 프롬프트
environment/      사전 빌드 이미지 재현 Dockerfile
tests/            검증기 진입점 · 비공개 테스트 · 채점 설정
solution/         참조 해답 (에이전트에게 비공개, 채점에 미사용)
```

**검증기 산출물**: `reward.json`(이진 보상+통과 비율) · `ctrf.json`(실패 메시지 포함 기계 판독 리포트) · `test-stdout.txt` · `run.log` · `reports/`

**Pier — Harbor 포크의 존재 이유**: Harbor는 `allow_internet = false` 과제에서 **모든 아웃바운드를 막아** 의존성 설치와 **LLM API 호출까지 차단**된다. Pier는 **에이전트별 네트워크 허용목록**을 추가해 *에이전트에게만* 필요한 통신을 열고 과제 환경은 격리 유지. 여기에 궤적 메타데이터·뷰어·`pier critique run`(궤적 분석)을 더했다. 리더보드 점수는 전부 **Modal 위의 `mini-swe-agent`** 로 산출.

```bash
pier run -p deep-swe/tasks --agent mini-swe-agent --model anthropic/claude-opus-4-8
pier run -p deep-swe/tasks --agent mini-swe-agent --n-tasks 10 --sample-seed 0   # 결정적 부분집합
```
`claude-code`·`codex`·`gemini-cli`·`opencode` 직접 구동도 지원.

> [!warning] 리더보드 점수가 README에 없다
> 레포는 **실행 방법을 완비**했지만 **어떤 모델이 몇 점인지는 이 페이지에 없다**(별도 리더보드 추정). 볼트 규칙상 **점수를 인용할 수 없다** — [[Repo-To-Skill]]의 *"절대 점수 누락"* 미해소 이월과 **같은 결손**이 반복됐다. 또한 **평가 도구를 만든 주체가 데이터 기업(datacurve-ai)** 이라는 점은 이해상충 여지로 남긴다. 이슈 밀도 0.679는 **실사용 마찰이 크다**는 신호일 수 있다(설치·샌드박스 복잡도).

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐⭐⭐⭐ — Apache-2.0·재현 절차 완비·설계 근거 명시. 단 **자체 리더보드 수치 미확인**.
- **즉시 활용**: **부분 YES.** 113과제 전량 실행은 비용이 크지만 `--n-tasks 10 --sample-seed 0` 로 **결정적 10과제 스팟체크**가 가능. 볼트의 *"pass^k 재현성 검증 도입"* actionable([[Thinkingbox]])과 **결합 가능한 첫 실행 가능 도구**다.
- **6개월 영향력**: 오염 회피 + **분리된 검증 환경**이 표준이 되면, 볼트가 인제스트하는 논문들의 자체 보고 점수를 **어떤 조건에서 잰 것인지** 되묻는 기준이 생긴다.
- **대체 관계**: [[SWE-bench-Science]]·[[Long-Horizon-Terminal-Bench]] 와 같은 계열이나, **검증기 환경 분리**는 이쪽이 더 엄격.
- **허와 실**: *"frontier coding agents 측정"* 은 크지만 **113개**다. 커버리지 주장은 절제해서 읽어야 한다.

> [!action] 당장 할 것
> `--n-tasks 10 --sample-seed 0` 로 10과제만 돌려 **동일 시드 2회 반복** — 목적은 모델 순위가 아니라 **같은 시드에서 결과가 재현되는가**다. 재현되지 않으면 이 벤치마크 점수는 인용 불가.

## 관련 페이지
- [[검사가능성-공사]] · [[EarlyEval]] · [[SWE-bench-Science]] · [[Long-Horizon-Terminal-Bench]] · [[FrontierChallenge]] · [[Thinkingbox]] · [[Repo-To-Skill]] · [[AI-에이전트-프레임워크]] · [[BCIT]] · [[Anthropic]] · [[OpenAI]]

## 원본
- 출처: https://github.com/datacurve-ai/deep-swe
- 러너: https://github.com/datacurve-ai/pier · 포맷: https://www.harborframework.com/docs/tasks
- 수집: 2026-09-04 자동수집 (ai-news)
- 검증: README defuddle 원문 + GitHub API 실측 (2026-09-04)
- 신뢰도: ⭐⭐⭐⭐
