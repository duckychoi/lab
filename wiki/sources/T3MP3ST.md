---
title: "elder-plinius/T3MP3ST — 이미 로그인된 코딩 에이전트를 레드팀 스웜의 두뇌로 재활용. XBOW 104문항 90.1%는 자가 측정"
type: source
domain: ai-news
tags: [ai-news, github-trending, security, red-team, pentest, multi-agent, claude-code, codex, agpl, 자기보고-수치]
created: 2026-11-08
updated: 2026-11-08
sources: [https://github.com/elder-plinius/T3MP3ST]
reliability: medium
---

**GitHub**: [elder-plinius/T3MP3ST](https://github.com/elder-plinius/T3MP3ST) · ★**6,982**(볼트 11-08 09:05Z API · 수집기 11-07 6,963 → +19) · 포크 1,446 · 이슈 16 · **AGPL-3.0** · TypeScript · created 2026-07-02 · 🔴 **pushed 2026-09-08**(두 달 정지)

## 핵심 인사이트
> [!insight] "에이전트를 새로 만들지 않고, 이미 쓰는 에이전트를 공격 도구로 묶는다"
> 브라우저 War Room 또는 CLI에서 **권한 받은 대상**을 자연어로 지정하면 로컬에 로그인된 [[anthropic-claude-code|Claude Code]]·Codex·[[opencode]] 또는 오프라인 모델(Ollama·LM Studio·vLLM)을 두뇌로 다중 에이전트가 recon → exploit → report 를 돈다. 기본값이 **keyless**(API 키 불필요, README 4회 검출). 핵심은 성능이 아니라 **진입 장벽** — 구독 중인 코딩 에이전트가 곧 펜테스트 인력이 된다.

> [!warning] 수치는 자가 측정 + 정지된 레포
> - **XBOW 104문항 pass@1 90.1%**(README 4회 검출) vs XBOW 자기보고 85% — 같은 스위트지만 **측정 주체가 T3MP3ST 자신**이다. `npm run verify-claims` 로 27/27 재계산 가능하다고 적었으나 이는 **"README 수치 = 로그 집계"의 일치**를 보일 뿐 독립 재현이 아니다 → **자가 재계산 ≠ 독립 재현**.
> - README 가 도메인별 성숙도를 스스로 나눈다: 웹앱·CTF·화이트박스 Stable / 스마트컨트랙트 *"재현이지 신규 발견 아님"* / 클라우드·모바일·바이너리 스캐폴딩. **이 자기 한정은 보존해야 한다**([[한정어-탈락]] 방지).
> - pushed 09-08 이후 정지 — 트렌딩(하루 +242)과 개발 활동이 분리돼 있다.

## 도메인별 추출 (ai-news)
- **신뢰도**: ★7K · AGPL · 수치 자가측정 · 독립 검증 0.
- **즉시 활용**: NO — 공격 도구, 승인된 대상이 없으면 쓸 일이 없다. Claude Code 세션 재사용은 기본 **비활성**(도구 권한 누수 우려를 README 가 직접 언급) — 이 설계 판단은 우리 에이전트 운영에도 참고점.
- **6개월 영향력**: "코딩 에이전트 = 범용 실행기"라는 흐름의 보안판. 방어 측에서는 자기 서비스를 이 도구로 셀프 점검하는 용도가 현실적.
- **허와 실**: 90.1%는 웹앱 CTF형 벤치 한정. 실제 침투는 범위·법적 승인이 병목.
- **액션**: 관찰만(star 불필요).

## 관련 페이지
- [[anthropic-claude-code|Claude Code]] · [[opencode]] · [[llm-multi-agent-survey|멀티에이전트]] · [[한정어-탈락]]
- 같은 배치: [[Paradev]](CLI 에이전트 병렬 실행) · [[rivet]]

## 원본
- 출처: https://github.com/elder-plinius/T3MP3ST
- 확인 범위: GitHub API(볼트 11-08) · README raw grep(90.1% · 85% · 27/27 · keyless 검출) · 실행 0회
- 신뢰도: ⭐⭐ (★7K · 수치 자가측정)
