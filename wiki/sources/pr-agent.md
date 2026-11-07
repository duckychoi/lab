---
title: "The-PR-Agent/pr-agent — Qodo 레거시를 커뮤니티가 이어받은 3년차 오픈소스 PR 리뷰어. v0.49.0 은 기본 모델 교체·보안 강화"
type: source
domain: ai-news
tags: [ai-news, github-trending, code-review, pull-request, qodo, litellm, github-action, security]
created: 2026-11-07
updated: 2026-11-07
sources: [https://github.com/The-PR-Agent/pr-agent]
reliability: high
---

**GitHub**: [The-PR-Agent/pr-agent](https://github.com/The-PR-Agent/pr-agent) **★15,354 · 포크 2,132 · 오픈이슈 61**(볼트 11-07 실측 · 수집기 11-06 ★15,169 → +185/1일) · MIT · Python · created **2023-07-05** · pushed 2026-11-06T21:17Z · 최신 릴리스 **v0.49.0(10-25)** · v0.48.0(10-16) · v0.47.0(10-02) · python 트렌딩 17위(11-06)

## 핵심 인사이트
> [!insight] 도구 1개 = LLM 1회 호출(약 30초)이라는 절제가 3년을 버틴 이유
> `/review` · `/improve` · `/ask` · `/describe` 가 **각각 LLM 1회 호출**로 끝난다. 큰 PR 은 "PR Compression"으로 압축한다. 다단계 에이전트 루프가 아니라 **단발 호출 + 좋은 프롬프트 + diff 압축**으로 비용·지연을 예측 가능하게 만든 설계다. GitHub Action · CLI(`pip install "pr-agent[github]"`) · GitLab webhook · Bitbucket · Azure DevOps 지원. README 가 *"community-maintained legacy project of Qodo"* 이며 **Qodo 무료 티어와 다르다**고 명시한다.

> [!warning] v0.49.0 업그레이드 시 깨지는 것 (릴리스 노트)
> 1. **기본 모델이 `gpt-6.1-sol`(폴백 `gpt-6-luna`)로 변경** — 이전 모델을 유지하려면 `config.model` 고정 필요(볼트 releases API 확인: v0.49.0 본문에 `gpt-6.1-sol` · `gpt-6-luna` · `polling_repositories` 모두 존재).
> 2. GitHub polling 은 `github.polling_repositories` **허용목록 필수**(빈 값 = 전부 무시).
> 3. Jira `project_keys = []` 의미가 "전체" → "비활성"으로 **반전**.
> 4. **보안 강화**: `litellm.extra_headers` 를 레포 `.pr_agent.toml`·코멘트 인자에서 설정 불가(host-only) · DNS rebinding 차단 · repo-context 경로 탈출 차단 · 자격증명 마스킹 확대. 이 묶음은 **레포 측 설정으로 호스트 자격증명을 빼낼 수 있던 공격면**을 닫은 것으로 읽힌다(볼트 추론 — 사고 공개 문구는 수집기 기준 미확인).
> 5. Docker 이미지 네임스페이스 `codiumai/pr-agent` → `pragent/pr-agent`(0.34.2 이후) 이관.

## 도메인별 추출 (ai-news)
- **신뢰도**: ★15.4k · 3년 4개월 · 릴리스 2주 간격 유지 — 높음.
- **즉시 활용**: YES — 개인 레포에 GitHub Action 으로 붙이면 LLM 키만으로 PR 요약·리뷰 자동화. 단 기본 모델 비용(gpt-6.1-sol) 확인 후 `config.model` 고정 권장.
- **6개월 영향력**: Claude Code `/code-review` 류와 겹친다. 차이는 **CI 상주형**(PR 이벤트마다 자동) vs 로컬 대화형.
- **대체 관계**: [[Claude-Code-워크플로우]] 의 수동 리뷰를 CI 자동 1차 리뷰로 보강.
- **허와 실**: 정량 리뷰 품질 벤치 없음. "30초"는 README 서술값.
- **액션**: 실험 — 테스트 레포 1개에 Action 설치(낮음 우선순위).

## 관련 페이지
- [[Claude-Code-워크플로우]] · [[AI-에이전트-프레임워크]] · [[OpenAI]] (기본 모델 공급자)
- [[agent-switch]] · [[auto-ontology]] (같은 날 GitHub)

## 원본
- 출처: https://github.com/The-PR-Agent/pr-agent
- 확인 범위: GitHub API·releases API 최신 3건(볼트 11-07 · 키워드 존재 확인) · README 는 수집기 기준(상단 약 60행) · v0.48/0.47 본문 미정독 · 실행 0회
- 신뢰도: ⭐⭐⭐ (★15k · 3년 유지 · 활발한 릴리스)
