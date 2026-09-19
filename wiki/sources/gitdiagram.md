---
title: "GitDiagram — 레포를 아키텍처 다이어그램으로. 검증은 '경로가 존재하나'까지이고, 틀린 경로의 노드는 링크만 떼고 남는다"
type: source
domain: ai-news
tags: [ai-news, github-trending, tool, code-understanding, architecture-diagram, mermaid, llm-validation, vercel, workflow]
created: 2026-09-19
updated: 2026-09-19
sources: []
reliability: medium
---

# GitDiagram (ahmedkhaleel2004/gitdiagram)

> [!insight] 핵심 인사이트 — **"LLM 출력을 그대로 렌더하지 않는다"는 설계는 맞다. 단 검증이 지키는 것은 *구조*이지 *정확성*이 아니다**
> 파이프라인: 레포 트리 + README + **크기 제한된 소스 발췌** → LLM이 **그룹·노드·엣지·경로를 가진 엄격한 그래프(JSON)** 출력 → 서버가 검증 → **결정론적 컴파일러가 Mermaid로 변환**(LLM이 Mermaid 문법을 직접 쓰지 않는다) → 브라우저가 SVG 재정화 + GitHub 링크 허용목록 재적용.
> 🎯 **이 "LLM은 AST만, 문법은 컴파일러가"라는 분리는 그대로 가져다 쓸 만한 패턴이다** — 문법 오류로 인한 렌더 실패를 모델 품질과 분리한다.
> 🔴 **그러나 볼트가 코드(`src/server/generate/graph.ts`, `graph-planner.ts`)를 읽은 결과 README 서술과 동작이 한 군데 다르다**:
> - README: *"validates identifiers, graph connectivity, limits, and **every linked path** against the actual repository. **Invalid output is retried** with focused feedback."*
> - 코드: 검증 이슈가 **전부 `missing_repository_path` 뿐이면 재시도하지 않는다.** `stripUnknownNodePaths()` 가 해당 노드의 **경로만 null로 지우고 노드는 다이어그램에 남긴다.** 주석 원문: *"Unresolvable paths only cost a node its GitHub link, so repair them in place. **Only structural problems are worth another model call.**"*
> → 🎯 **LLM이 존재하지 않는 파일을 가리키며 지어낸 컴포넌트는 "링크 없는 노드"로 살아남는다.** 재시도 대상은 중복 ID·미정의 그룹 등 **구조 오류뿐**이다. "환각 방어"는 **링크 환각 방어**이지 **컴포넌트 환각 방어가 아니다.** 비용 합리적인 설계지만, 사용자는 "링크 없는 노드 = 검증 안 된 노드"라는 사실을 UI에서 알 수 없다(UI 표시 여부 미확인).

> [!warning] 🔴 정정 — "GPT-5.6 Luna **1회 호출**"은 **기본 경로의 최소값**이다
> README 원문: *"one GPT-5.6 Luna request at medium reasoning … additional Luna calls are reserved for **structural repairs** or **one recovery after an 18-second slow request**."* 코드 상수 `ARCHITECTURE_SLOW_RETRY_MS = 18_000` ✅.
> 또한 **사용자 키 · 명시적 모델 지정 · OpenRouter** 는 *"retain the **two-stage** pipeline"*(설명 → 그래프 2단). → 1회 호출은 **관리형(managed) OpenAI 경로 한정**이다.
> ✅ 나머지 일치: medium reasoning · Fast 모드 `service_tier: "priority"` · Vercel 300초 · *"Output token estimates reserve quota but **do not cap** provider output"* — 코드 주석도 *"Provider requests **deliberately omit** `max_output_tokens`"* 로 확인(견적 상수: 설명 8,000 / 그래프 6,000 토큰).

## 도메인별 추출 (ai-news)

- **신뢰도**: GitHub **★16,579** · 포크 1,261 · MIT · `open_issues_count` 40 = 이슈 23 + PR 17 · **오늘(09-19) 커밋 3건** — 활발. 논문·평가 없음, **생성 품질 수치 0개**(수집기 ✅). 개인 개발자 프로젝트 + 스폰서 슬롯 운영. → reliability **medium**(★와 코드 품질은 높으나 산출물 정확도 근거 없음).
- **즉시 활용**: 🎯 **YES — 이 볼트의 인제스트 작업에 바로 쓴다.** 트렌딩 레포를 인제스트할 때 URL의 `github.com` → `gitdiagram.com` 치환(README: *"replace `hub` with `diagram`"*)만으로 구조도를 얻는다. 🔴 **단 다이어그램을 인용 근거로 쓰지 말고 "어디를 읽을지" 지도로만 쓴다** — 위 인사이트대로 노드의 정확성은 보증되지 않는다.
- **6개월 영향력**: **낮~중.** 코드 이해 도구로는 에이전트(Claude Code가 직접 레포를 읽는 것)가 더 깊다. 가치는 **"0초 진입"** — 설치·키 없이 공개 레포에 즉시 작동.
- **대체 관계**: README가 영감원으로 밝힌 **Gitingest**(레포 → LLM용 텍스트 덤프)의 **시각화 버전**. 볼트가 레포를 읽을 때 쓰는 `curl` + 트리 조회를 대체하진 않고 **앞단 개요**를 강화한다.
- **허와 실**: 🔴 **"any public or private GitHub repository … in seconds"** 의 실제 입력 예산(코드 `repository-context.ts` 상수):
  ```
  트리 문자열   ≤ 24,000자   (초과분 경로는 프롬프트에서 제외, treeTruncated 플래그)
  README        ≤ 8,500자    (잘라서 "[README excerpt ends here.]")
  소스 발췌     ≤ 12개 파일 · 합계 ≤ 48,000자 · 파일당 원본 ≤ 512,000바이트
  거부 조건     GitHub API 트리 응답이 truncated면 즉시 거부
                → 오류문 "Repository is too large (>195k tokens)"
  ```
  🎯 **대형 모노레포는 거부되고, 중형 레포는 "일부만 보고" 그린다.** 수집기의 *"대형 모노레포는 안 된다"* 판정 ✅ — 볼트가 거부 조건의 실제 트리거(GitHub API `truncated` 플래그)와 **중형 레포의 부분 가시성**을 추가 확인. 🔴 오류문의 ">195k tokens"는 **실제 판정 기준(GitHub 트리 절단)과 다른 단위의 설명**이다.
- **액션**: 설치 불필요. 🎯 **다음 트렌딩 레포 인제스트 1건에서 gitdiagram 결과를 README·트리와 대조해 "링크 없는 노드" 비율을 한 번 센다** — 이게 이 도구의 실제 환각률 대리지표다.

### 스택·운영 — 참고용
- Next.js 16 App Router · React 19 · Vercel(Bun 런타임, **유일한 라이브 런타임**) · Cloudflare R2(아티팩트) · Upstash Redis(쿼터·취소·락) · PostHog
- *"There is **no** separate FastAPI implementation, Postgres database, or Neon runtime"* — 과거 구조를 걷어냈다고 README가 명시(이전 구조는 볼트 미확인).
- 성공 결과는 R2에 **레포 키로 캐시** → 재방문 시 모델 호출 없음. 🔴 **캐시 무효화 조건(레포가 바뀌면?)은 README에 없다**(미확인).
- 비공개 레포: 브라우저에 fine-grained PAT 입력, 별도 R2 네임스페이스.

> [!action] 당장 할 것
> **볼트의 GitHub 인제스트 체크리스트에 "gitdiagram.com/<owner>/<repo> 로 구조 개요 확인(지도 용도, 인용 금지)"을 선택 단계로 제안한다.** 🎯 비용 0 · 설치 0. 이 배치의 [[marin]] 처럼 README가 `docs/` 하위 문서에 수치를 숨기는 레포에서, **어느 디렉터리를 열어야 하는지** 찾는 시간을 줄인다.

> [!question] 미해결 질문
> - 검증에 쓰는 `fileTreeLookup` 이 **전체 트리**로 만들어지는가, **24,000자로 잘린 프롬프트 트리**로 만들어지는가? 후자면 실존하지만 잘려나간 파일을 가리킨 올바른 노드도 링크를 잃는다(호출부 미열람 — 미확인).
> - "링크 없는 노드"가 UI에서 구분 표시되는가?
> - 생성 품질에 대한 **어떤 평가**(사람 평가·정답 다이어그램 대조)도 README·트리에 없다. `*.test.ts` 는 컴파일러 계약·쿼터·SSE 등 **시스템 정확성** 테스트다(파일명 기준, 내용 미열람).

## 관련 페이지
- [[Vercel]]
- [[Cloudflare]]
- [[OpenAI]]
- [[Claude-Code-워크플로우]]
- [[검사가능성-공사]]
- [[요약자와-판정자-분리]]
- [[한정어-탈락]]
- [[agent-lightning]]
- [[marin]]
- [[tradingview-mcp]]

## 원본
- 출처: https://github.com/ahmedkhaleel2004/gitdiagram · 서비스 https://gitdiagram.com
- 볼트 실측(2026-09-19, GitHub API): `stargazers_count` **16,579**(수집기 16,577 — 조회 시차) · `forks_count` 1,261 · `open_issues_count` **40** ✅ = 이슈 23 + PR 17 · `created_at` 2024-12-15 ✅ · `pushed_at` 2026-09-19T08:22 · `license` MIT ✅ · 트렌딩 전체 데일리 `152 stars today` ✅ · 트리 blob 288개(`truncated: false`)
- 코드 열람(HEAD, 2026-09-19): `src/server/generate/graph.ts`(496행) · `graph-planner.ts` · `repository-context.ts` · `source-excerpt.ts` · `generation-policy.ts` · `github.ts`
- 수집기 대조: README 106행 ✅ · 트리·README·bounded 발췌 ✅ · 결정론적 컴파일러 ✅ · medium reasoning · priority 티어 ✅ · 300초 ✅ · "do not cap" ✅ · 대형 입력 사전 거부 ✅ · 🔴 "1회 호출" → 관리형 기본 경로 최소값(수리·지연복구 추가 호출, 타 경로는 2단) · 🔴 "검증 실패 시 재시도" → **경로 오류만이면 재시도 없이 링크 제거 후 수용**(코드 확인)
- 신뢰도: ⭐⭐ (★ 높고 코드·테스트 체계 양호 · 🔴 출력 정확도 평가 0 · README 서술이 코드보다 강함)
