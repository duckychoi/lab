---
title: OpenResearch — 하네스 무관 병렬 리서치 에이전트 워크스페이스 (alphaXiv · Rust)
type: source
domain: ai-news
tags: [ai-news, github-trending, research-agent, local-first, rust, harness-agnostic, alphaxiv]
created: 2026-09-12
updated: 2026-09-12
sources: []
reliability: high
---

# OpenResearch (alphaXiv/OpenResearch)

> [!insight] 핵심 인사이트 — 모델이 아니라 **하네스까지 교체 가능한 층**
> ⭐**1,469**(2026-09-12 API 실호출 · raw 1,468 대비 **+1**) · fork **105** · **Rust** · **MIT** · created **2026-06-07** · pushed 2026-09-12(당일) · 이슈 9.
> README 5행 자기규정: *"The **local-first workspace** for research agents and autoresearch."*
> 🎯 raw는 *"모델 종류를 가리지 않고"* 라고 요약했지만 **원문은 한 칸 더 나간다**(50행): *"Use **Claude Code, Codex, OpenCode, or Cursor**, with the **harness and model** selected per session."*
> → **모델만이 아니라 코딩 에이전트 하네스 자체를 세션 단위로 갈아끼운다.** 이건 [[에이전트축-분기]] 가 추적해 온 축 — *"누가 지능을 갖느냐"가 아니라 "누가 실행 껍데기를 소유하느냐"* — 의 최신 지점이다. [[OpenClaude]](임의 LLM 백엔드를 한 터미널로) 와 같은 계열이되, **저쪽은 모델을 추상화했고 이쪽은 하네스를 추상화했다.**
> 컴퓨트도 같은 방식이다(51·63행): 로컬 · 자체 인프라 · 관리형 컴퓨트, 그리고 **동일한 커밋 스냅샷이 로컬 / SSH / Slurm 어디서든 실행**된다.

> [!warning] 🔴 **raw의 "초기 단계" 판정은 원문의 한정 범위를 넘었다**
> raw 기록: *"README가 자체적으로 **'support is still in beta'** 라고 적을 만큼 **초기 단계**."*
> **볼트 원문 실측 — README 31~35행 전문:**
> > *"**On Windows**, install from [Releases] and read [the Windows notes] first — **Git for Windows is required**, and support is still in beta."*
>
> → 🎯 **`beta` 의 주어는 제품이 아니라 「Windows 지원」이다.** 플랫폼 한정 단서를 제품 성숙도 판정으로 확대했다.
> → 반대 근거도 있다: **당일 푸시**, 이슈 **9건**(fork 105 대비 0.086), `curl | sh` 원라인 설치 + `orx up` 으로 `127.0.0.1:4791` 로컬 대시보드가 즉시 뜬다 — **초기 단계 서술과 정합하지 않는다.**
> → 이 실패는 [[한정어-탈락]] 의 **거울상**이다. hyperresearch에서는 raw가 **한정어를 빠뜨려 주장을 강하게** 만들었고(리더보드 1위), 여기서는 **한정어를 빠뜨려 주장을 약하게** 만들었다(제품이 베타). **방향은 반대인데 기전은 같다 — 조건절을 떼고 본문만 옮겼다.**
> → 볼트에 주는 교훈: 한정어 탈락은 *"과장"의 문제가 아니다.* 과소평가도 똑같이 만든다. 그래서 **"이 도구는 과장하고 있는가"만 묻는 검사로는 안 잡힌다.**

> [!note] 배경 — 만든 곳이 [[alphaXiv]] 라는 사실이 정보다
> alphaXiv는 **arXiv 논문 위에 토론·리뷰 층을 얹는 서비스**다. 즉 리서치 에이전트를 **논문 유통을 실제로 운영해 본 팀**이 만들었다.
> 그리고 언어가 **Rust** 다 — 같은 배치 [[llm_wiki]](Rust 백엔드) 와 함께, **로컬 우선 에이전트 도구가 Python을 벗어나는 흐름**의 두 번째 사례. 기동 비용·단일 바이너리 배포가 로컬 우선 설계와 직결된다.

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐⭐⭐ — 수치·라이선스·언어·푸시일 API 실호출, README 4,135B **전문 대조**(문제의 33~35행 포함). 조직([[alphaXiv]])이 실재하는 공개 서비스라 출처 추적 가능 → **high**.
- **즉시 활용**: **부분 YES.** 지금 내 작업은 Claude Code 단일 하네스라 "하네스 교체"의 실익이 당장은 없다. 다만 **`orx up` 로컬 대시보드로 병렬 리서치 세션을 관리하는 형태**는 볼트 인제스트가 매 배치 13건을 순차 처리하는 현 방식과 대비된다 — **병렬화 참고 대상**.
- **6개월 영향력**: 하네스가 교체 가능해지면 **특정 CLI에 대한 락인이 약해진다.** 볼트·스킬 자산이 Claude Code에 묶여 있는 만큼, 이 층이 표준화되는지는 실질적 이해관계가 있다.
- **대체 관계**: [[OpenClaude]](모델 추상화) 와 상보. 같은 배치 [[hyperresearch]] 와는 **경쟁이 아니라 다른 층** — hyperresearch는 Claude Code *안의* 스킬 파이프라인이고, OpenResearch는 *그 바깥의* 워크스페이스다. 실제로 OpenResearch 위에서 hyperresearch를 돌리는 조합이 성립한다.
- **허와 실**: 걷어낼 마케팅이 **거의 없다** — README 4KB에 형용사보다 명령어가 많다. 대신 **성능·품질 주장도 없다**(벤치마크 0건). 즉 *"무엇을 하는가"* 는 명확하고 *"얼마나 잘하는가"* 는 미측정.
- **액션**: `docs/local-models.md` 확인 — LM Studio / oMLX / Ollama 연결 경로가 [[local-llm]] 도메인 자산(GGUF 모델들)과 이어지는지.

## 관련 페이지
- [[alphaXiv]]
- [[hyperresearch]]
- [[OpenClaude]]
- [[에이전트축-분기]]
- [[한정어-탈락]]
- [[llm_wiki]]
- [[local-llm]]
- [[ai-news]]

## 원본
- 출처: https://github.com/alphaXiv/OpenResearch
- GitHub API 실호출(2026-09-12): ⭐**1,469** · fork **105** · **Rust** · **MIT** · created 2026-06-07 · pushed **2026-09-12(당일)** · open_issues 9 · topics 없음
- README 원문 실측: **4,135B**, 인용 행번호 5 · 30 · 31~35 · 38 · 50 · 51 · 63
- raw 대비: 스타 **+1 드리프트** / 🔴 **한정 범위 확대**(Windows 지원 베타 → 제품 초기 단계)
- 신뢰도: ⭐⭐⭐ (기능·메타 실측 / 품질 주장은 원문에 부재)
