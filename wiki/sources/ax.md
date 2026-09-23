---
title: "ax (google/ax) — 에이전트를 쿠버네티스처럼 선언하는 오케스트레이터, 그런데 실행 기반은 '구글 공식 아님' 레포다"
type: source
domain: ai-news
tags: [ai-news, github, 에이전트-오케스트레이션, 샌드박스, kubernetes, go, 자기제한-명시, 하네스-설계-축]
created: 2026-09-23
updated: 2026-09-23
sources: []
reliability: medium
---

# ax — 선언형 에이전트 오케스트레이션 런타임

> [!insight] 핵심 인사이트 — **에이전트 운영을 "앱 배포 문제"로 재정의했다**
> 에이전트 프레임워크 대부분은 *에이전트를 어떻게 만드는가*(툴·메모리·플래닝)를 다룬다. `ax` 는 그 층을 건드리지 않고 **이미 만들어진 에이전트를 클러스터에서 어떻게 돌리는가**만 맡는다. `ax.io/v1alpha1` YAML 매니페스트 → 샌드박스·워크스페이스·네트워크 펜싱이 붙어 실행.
> 🎯 프리미티브가 4개뿐이라는 게 설계 주장이다 — **Task**(격리 실행 + CPU/메모리 제한) · **Workspace**(Git·MCP·스킬 사전 배선) · **Gateway**(아웃바운드 호스트 허용목록) · **Model**(플랫폼 LLM 설정). 여기에 `ax suspend/resume` · `ax ssh`.
> 📌 [[하네스-설계-축]] 관점: 이것은 **에이전트 축이 아니라 인프라 축**의 물건이다. [[에이전트축-분기]] 가 실행 계층까지 내려온 사례.

> [!warning] 🔴 성능 주장은 전부 목표 진술 — **측정치 0개**
> *"billions of autonomous agent workloads"* · *"billions of tasks per cluster"* 는 README **13행의 소개 문장**이며 벤치 표·처리량·지연시간 수치가 **하나도 없다.**
> ✅ 볼트 확인 범위: **README 185행 전문** — 숫자를 포함한 행 28개는 전부 포트·버전·YAML 예시값이고, `benchmark`/`throughput`/`latency`/`qps` 키워드는 **13행 소개 문장 외 0건**.
> 🔴 README 자체 경고: *stable release 전 major breaking changes 도입 예정.* 알파(`v1alpha1`)를 API 그룹 이름에 박아 둔 것과 일관된다 → [[자기제한-명시]].

> [!insight] 🎯 이 항목의 진짜 뉴스 — **구글 레포가 "구글 공식 아님" 레포에 의존한다**
> README 13행: *"It runs on top of [Agent Substrate](https://github.com/agent-substrate/substrate) for sandboxed execution."* 72행에서는 배포 전제로 **Agent Substrate Control API 도달 가능성**(기본 `api.ate-system.svc.cluster.local:443`)을 요구한다.
> 그런데 그 [[substrate]] 는 자기 README에 ***"공식 지원 Google 제품 아님 · Google OSS VRP 대상 아님"*** 을 명시한다.
> 🎯 **`google/` 네임스페이스의 신뢰도가 의존 사슬 한 칸 아래에서 끊긴다.** 레포 소유자로 신뢰도를 추정하는 휴리스틱의 반례 — 볼트 [[파생저장소-식별]] 이 *파생 방향*에서 본 문제를 **의존 방향**에서 다시 만난 셈이다.
> ⬜ 두 레포의 조직적 관계(같은 팀인지, Substrate가 곧 구글로 편입되는지)는 **미확인**.

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐ 8,140 (**당일 +2,305 — 이번 배치 최대 급상승**) · fork 376 · Go · Apache-2.0 · 생성 2026-03-30 · 오픈이슈 36. ✅ 볼트 실측(09-23 09:2x) ★**8,143** — 수집기 8,140과 3 차이(시차).
- **즉시 활용**: **NO.** 쿠버네티스 클러스터 + 별도 Substrate Control API가 전제다. 단일 머신 워크플로에는 과하다.
- **6개월 영향력**: 에이전트가 **"프로세스"가 아니라 "워크로드"로 다뤄지는 전환**의 대표 사례가 될 수 있다. `suspend/resume` 이 일급 동사인 게 신호 — 에이전트를 **중단 가능한 장기 작업**으로 본다.
- **대체 관계**: 대체하지 않는다. 기존 에이전트 프레임워크 **아래에 깔리는** 층.
- **허와 실**: 프리미티브 4개·YAML·펜싱은 실체. **규모 주장(billions)은 전부 허** — 근거 0.
- **액션**: ⭐ star + 관찰. 벤치 수치가 올라오면 재평가.

## 관련 페이지
- [[substrate]] — 실행 기반. 이 항목의 핵심 연결
- [[Google]] · [[Google-Labs]]
- [[에이전트축-분기]] · [[하네스-설계-축]] · [[자기제한-명시]] · [[파생저장소-식별]]

## 원본
- 출처: https://github.com/google/ax
- 확인 범위: README **185행 전문** · GitHub API 실측 1회
- 신뢰도: ⭐⭐ (구현 실체 확인 · **성능 주장 근거 0**)
