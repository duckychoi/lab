---
title: WeKnora — 문서를 RAG·에이전트·자가유지 위키로 바꾸는 Tencent 플랫폼
type: source
domain: ai-news
tags: [ai-news, github-trending, rag, agent, llm-wiki, knowledge-graph, tencent, self-hosted, sandbox, agent-memory]
created: 2026-09-12
updated: 2026-09-12
sources: []
reliability: high
---

# WeKnora (Tencent/WeKnora)

> [!insight] 핵심 인사이트 — **이 볼트가 손으로 하는 일을 제품이 v0.5.0에 GA로 냈다**
> ⭐**22,480**(2026-09-12 API 실호출 · raw 22,479 대비 **+1**) · fork **3,231** · **Go** · created **2025-07-22** · pushed 2026-09-12(당일) · 이슈 **746**.
> README 50행 제목 원문: *"WeKnora — Turn Documents into Living Knowledge with RAG, Agents and **Auto-Wiki**"*.
> 세 개의 출구가 있다(60행): **RAG 즉답** · **ReAct 에이전트**(검색·MCP 툴·테넌트 스킬 카탈로그·샌드박스·웹검색 조율) · 그리고 **Wiki Mode** —
> > *"a brand-new **Wiki Mode** in which agents distill raw documents into a **self-maintaining, interlinked markdown knowledge base** with an interactive knowledge graph, complete with **manual editing, revision history and one-click rollback**."*
>
> 🎯 **이 문장은 이 볼트의 사양서와 거의 같다.** 마크다운 · 상호링크 · 지식그래프 · 에이전트가 유지. 차이는 **버전 관리와 규모**다:
> - v0.5.0 — **Wiki Mode GA**(에이전트가 구조화·상호링크된 마크다운 위키 페이지 자동 생성 + 지식그래프 + 그래프 뷰어)
> - v0.5.2 — **위키 인제스트가 4만 문서 KB까지 확장**(태스크 큐 + DLQ)
> - v0.7.2 — **위키 페이지 리비전 히스토리**(스냅샷 + **행 단위 diff** + 원클릭 롤백 + 브라우저 내 수동 편집)
> → **볼트는 소스 1,012개에서 그래프를 정량 측정하지 못하고 있고**([[LLM-Wiki]] 09-11 갱신), WeKnora는 **4만 문서에서 그래프를 UI로 띄우고 페이지 단위 롤백까지 한다.**

> [!warning] 🪞 볼트에 없는 것 두 번째 — **되돌리기가 없다**
> 09-11 [[llm_wiki]] 갱신은 볼트의 결측을 *"그래프를 측정하지 않는다"* 로 짚었다. WeKnora는 **다른 결측**을 드러낸다.
> 볼트의 페이지 갱신 방식: 기존 페이지 하단에 `## 🔄 YYYY-MM-DD 갱신` 섹션을 **덧붙인다**. 그래서:
> - **틀린 갱신을 되돌릴 수단이 없다.** 09-11에 [[SenseNova-U1.5]] 판정이 틀렸다고 볼트 스스로 기록했지만, **그 틀린 문장은 아직 페이지에 남아 있다**(추가 문단으로 반박만 붙었다).
> - 페이지가 **단조 증가**한다. [[i-have-adhd]] 가 지적한 *"09-11 배치 평균 6.3KB"* 비대화의 구조적 원인이 이것이다 — **삭제 경로가 없으니 길어질 수밖에 없다.**
> → 🎯 **WeKnora가 롤백을 v0.7.2에서 별도 기능으로 낸 것은, 자동 생성 위키에서 "잘못 쓴 것을 지우는 문제"가 실제로 발생한다는 증거다.** 볼트는 그 문제를 **아직 겪지 않은 게 아니라 대응 수단이 없어서 누적하고 있다.**
> → 볼트에는 이미 **git이 있다**(스키마 실용도구 항목에 명시). **쓰고 있지 않을 뿐이다.**

> [!note] v0.8.0 실측 — 에이전트 실행 층이 두꺼워졌다 (README 67행 원문 대조)
> raw가 요약한 항목 **전건 원문 확인**:
> - **스킬 샌드박스 런타임** — 세션 지속 **Docker / E2B / Cube** 백엔드, 테넌트별 네트워크 정책. ⚠️ **Local 호스트 프로세스 백엔드는 제거**됐고 Docker는 옵트인(보안 강화 방향)
> - **테넌트 스킬 카탈로그** — ClawHub / SkillHub / git / zip 설치, 샌드박스별 스냅샷, 파일 브라우즈·편집
> - **교차세션 장기기억** — profile / preference / fact / task / interest 5종, **확인을 거친 자동 추출**, `search_memory` → [[에이전트-메모리-레이어]] 에 직접 해당
> - in-process **anydoc** 오피스 파서 · GitLab·Tencent IMA 데이터소스 · **LiteLLM** · Exa/Metaso 웹검색 · XMind 파싱 · 컨텍스트 압축 · 프로바이더 프롬프트 캐시 마커
> - 문서 포맷(62행): *"handles **10+ document formats** including PDF, Word, images, Excel and XMind"* — raw의 "10여 종" **일치**
> - 관측성: **Langfuse** 전면 연동(에이전트 추론·토큰 사용·파이프라인 트레이싱) — raw **일치**
> - LLM 프로바이더: OpenAI · DeepSeek · Qwen · Zhipu · Hunyuan · Gemini · MiniMax · NVIDIA · LiteLLM · Ollama — raw **일치**
> - 💡 v0.3.0에 **Korean i18n** 이 이미 들어와 있다(83~84행) — 국내 적용 시 언어 장벽이 [[DeskcommCRM]] 과 정반대다

> [!warning] 라이선스 — `NOASSERTION` 이지만 **MIT**, raw 판정 실측 확인
> **볼트 실측**: LICENSE 파일 **158,420B**(서드파티 고지가 대부분). **8행 원문**: *"This project is licensed under the **MIT License** except for the third-party components listed below, which is licensed under different terms."* 이후 *"Terms of the MIT License:"* 전문 수록.
> → raw 판정(*"spdx_id가 NOASSERTION 이지만 LICENSE 본문 8행이 MIT"*) **정확 — 행번호까지 일치.**
> → 🎯 **[[파생표기-함정]] 이 사흘 연속 같은 형태로 재현됐다**: 09-10 [[teamai-cli]](Tencent) · 09-11 [[llm_wiki]](GPL-3.0) · 09-12 WeKnora(Tencent). **세 건 중 두 건이 Tencent다.** Tencent 레포는 서드파티 고지를 LICENSE에 합치는 관행이 있어 `spdx_id` 가 구조적으로 `NOASSERTION` 이 된다 → **벤더 단위 규칙으로 승격 가능**: *[[Tencent]] 레포의 `NOASSERTION` 은 제약 신호가 아니라 파일 형식의 부작용으로 우선 가정하고 8행 근처를 확인한다.*
> ⚠️ 단 **서드파티 컴포넌트는 별도 라이선스**(Apache-2.0 등)이므로 부분 재사용 시 `THIRD_PARTY_NOTICES.md`·`licenses/` 확인 필요.

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐⭐⭐ — 스타·포크·언어 API 실호출, README **32,828B** 및 LICENSE **158,420B** 원문 직접 대조(인용 행번호 기록). Tencent 공식 조직 레포. 이슈 746건은 규모 대비 정상 범위(fork 3,231 대비 **0.231건/포크**로 배치 최고 마찰이나, 22K 스타 제품의 활성 신호로도 읽힌다) → **high**.
- **즉시 활용**: **도구로는 NO, 규격으로는 YES.** 볼트를 WeKnora로 옮길 이유는 없다(Go 서버 + DB 스택, 볼트는 파일 + 에이전트). 가져올 것은 **리비전 히스토리 + 롤백**이라는 개념이고, 볼트에서의 구현은 **git 커밋을 인제스트 단위로 끊는 것**으로 충분하다.
- **6개월 영향력**: [[LLM-Wiki]] 패턴이 **개인 도구에서 기업 인프라로 넘어갔다.** 오늘 배치에만 [[hyperresearch]](파이프라인형) · WeKnora(기업 플랫폼형) 두 건이 동시에 걸렸고, 09-11에 [[llm_wiki]](앱형)이 있었다. **3일 안에 세 형태가 다 나왔다** — 이 패턴은 더 이상 실험이 아니다.
- **대체 관계**: 볼트를 대체하지 않는다. **[[RAG vs LLM-Wiki]] 의 두 노선을 한 제품이 동시에 제공**한다는 점이 오히려 중요하다 — 즉답은 RAG, 축적은 Wiki Mode로 분리했다. 볼트는 Wiki 쪽만 갖고 있다.
- **허와 실**: README 60행이 **한 문장에 기능 20개 이상을 나열**하는 전형적 과적재 서술이다. 다만 **CHANGELOG가 v0.3.0부터 버전별로 실재**하고 항목이 구체적이라(제거된 기능까지 명시: *"Local host-process backend removed"*) 마케팅 밀도에 비해 **검증 가능성이 높은 편**이다.
- **액션**: ① **볼트 git 커밋 규율 도입**(아래 action) ② Wiki Mode의 지식그래프 UI 스크린샷(`docs/images/wiki-graph.png`) 확인 — [[LLM-Wiki]] 가 미해결로 둔 *"그래프를 어떻게 보여줄 것인가"* 참고.

> [!action] 🟡 볼트에 리비전 규율 도입 — **git 은 이미 있다**
> WeKnora가 v0.7.2에 별도 기능으로 낸 것(스냅샷 + 행 단위 diff + 롤백)을 볼트는 **git 으로 공짜로 갖는다.** 지금 없는 것은 도구가 아니라 **규율**이다.
> **할 것**: 인제스트 배치 1회 = 커밋 1회, 메시지에 `ingest YYYY-MM-DD (신규 N · 갱신 M)`.
> **효과 판정**: 다음에 판정 오류가 나왔을 때(09-11 [[SenseNova-U1.5]] 같은 경우) **해당 문장을 되돌릴 수 있는가.**
> ⚠️ 단 [[AgentGrad]] 원칙상 이번 배치의 **최우선 개입은 [[hyperresearch]] 의 quote-integrity 1건**이다. 이 항목은 **우선순위 중간**으로 등재하고 그 다음 차례로 둔다 — 두 개를 동시에 넣으면 또 무엇이 효과였는지 모르게 된다.

## 관련 페이지
- [[LLM-Wiki]]
- [[RAG vs LLM-Wiki]]
- [[hyperresearch]]
- [[llm_wiki]]
- [[claude-obsidian]]
- [[Tencent]]
- [[teamai-cli]]
- [[파생표기-함정]]
- [[에이전트-메모리-레이어]]
- [[에이전트-스킬]]
- [[DeskcommCRM]]
- [[AgentGrad]]
- [[ai-news]]

## 원본
- 출처: https://github.com/Tencent/WeKnora
- GitHub API 실호출(2026-09-12): ⭐**22,480** · fork **3,231** · **Go** · spdx **NOASSERTION** · created 2025-07-22 · pushed 2026-09-12(당일) · open_issues **746**
- description 원문: *"Open-source LLM knowledge platform: turn raw documents into a queryable RAG, an autonomous reasoning agent, and a self-maintaining Wiki."*
- README 원문 실측: **32,828B**, 인용 행번호 31 · 50 · 60 · 62 · 67~84 · 102~103
- LICENSE 원문 실측: **158,420B**, **8행 MIT 확인**
- raw 대비: 스타 **+1** · fork **+1** 드리프트, **라이선스 판정 정확(행번호까지 일치)**
- 신뢰도: ⭐⭐⭐ (전 항목 원문 대조)
