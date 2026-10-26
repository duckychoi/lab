---
title: "sandbox-runtime (srt) — Claude Code용으로 만든 컨테이너 없는 OS 샌드박스. '윈도우 미지원'은 틀렸고(알파 지원), README 절반이 '이 설정을 켜면 격리가 깨진다'는 경고다"
type: source
domain: ai-news
tags: [ai-news, github-trending, sandbox, agent-security, bubblewrap, seatbelt, network-proxy, claude-code, research-preview]
created: 2026-10-26
updated: 2026-10-26
sources: [https://github.com/anthropics/sandbox-runtime]
reliability: high
---

# anthropics/sandbox-runtime — ★6,647 · TypeScript · Apache-2.0 · Beta Research Preview

> [!insight] 핵심 인사이트 — **"에이전트 권한"을 프롬프트가 아니라 OS가 강제하는 1차 구현체를 벤더가 직접 공개했다**
> `srt "<명령>"` 한 줄로 임의 프로세스(에이전트 bash·로컬 MCP 서버·`npm install`)에 **파일시스템 allow/deny + 도메인 allowlist 네트워크(기본 전면 차단)** 를 건다. macOS는 동적 Seatbelt 프로필(`sandbox-exec`), Linux는 `bubblewrap` + 네트워크 네임스페이스, 트래픽은 호스트의 HTTP/SOCKS5 프록시로만 나간다. README가 스스로 *"developed for Claude Code"* 라고 밝히므로 [[Claude-Code-워크플로우]]의 샌드박스 동작을 이해하는 원전이다.
> 더 중요한 것은 **위협모델을 적었다는 점**이다. [[OpenShell]]이 "샌드박스"를 내놓고 위협모델을 적지 않았던 것과 대조적으로, srt README 156 KB 중 상당 부분이 Security Limitations·Known limitations·옵션별 *"Security warning"* 이다(도메인 프론팅 우회, `github.com` 같은 광역 허용의 유출 위험, docker.sock 허용 = 호스트 탈출, `allowAppleEvents`는 *"removes code-execution isolation"*). → [[자기제한-명시]]의 모범 사례.

> [!warning] 수집기 요약 교정
> - 🔴 **"no Windows" — 틀림.** README Platform Support: *"**Windows**: Alpha — uses a bundled `srt-win.exe` helper"* + 별도 `## Windows (alpha)` 절(전용 `srt-sandbox` 로컬 계정, WFP egress 펜스, 1회 UAC 승격 `windows-install`, 사용자 프로필 읽기 grant). 알파라는 한정어를 붙여 "지원(알파)"이 정확.
> - "research preview" → 원문은 **"Beta Research Preview"**, *"APIs and configuration formats may evolve."*
> - Linux 네트워크 격리는 `HTTP_PROXY` 등 **환경변수 의존** — 이를 무시하는 프로그램은 (우회가 아니라) 접속 불가가 된다고 README가 명시. `enableWeakerNestedSandbox`(Docker 내부용)는 *"considerably weakens security"*.
> - 설치 위치 함정: 프로젝트 `node_modules/`에 설치하고 프로젝트를 쓰기 허용하면 샌드박스 안의 명령이 srt 자신을 덮어써 **다음 실행이 비샌드박스**가 된다(README 명시). 전역 설치 권장.

## 도메인별 추출 (ai-news)

- **신뢰도**: ★6,647 · fork 587 · open issues **303**(★ 대비 높음 = 실사용 마찰 신호) · created 2025-10-20(1년) · pushed 2026-10-25 · [[Anthropic]] 공식 · 논문 없음이나 구현 세부·한계가 문서화됨.
- **즉시 활용**: **YES(Linux)** — 볼트 서버는 Linux. `bubblewrap` 설치 후 `srt --settings <json> <명령>`으로 크론 리서치 에이전트·미검증 MCP 서버·다운로드한 레포 스크립트를 `allowedDomains` 최소화 상태로 감쌀 수 있다. "다운로드 코드 실행 금지" 원칙을 *실행이 필요할 때* 완화하는 유일한 근거 있는 수단.
- **6개월 영향력**: 높음 — 에이전트 하네스마다 제각각이던 "권한 프롬프트"가 OS 강제 샌드박스로 수렴하는 기준 구현. 라이브러리 API(`wrapWithSandbox`, 위반 attribution, `--control-fd` 실행 중 설정 갱신, `srt proxy` 외부 decider)는 다른 하네스가 임베드하라고 만든 모양.
- **대체 관계**: Docker 컨테이너 격리를 **경량 대체**(컨테이너 불필요). [[OpenShell]](NVIDIA, Rust)·[[openai-codex]]의 자체 샌드박스와 같은 층. [[하네스-설계-축]]의 "실행 격리" 축.
- **허와 실**: 실 = 도메인 단위 egress 통제 + 자격증명 마스킹(`credentials` mask, TLS 종료 필요) + 해석 주소 검사(허용 도메인이 루프백·메타데이터 IP로 리졸브되면 차단). 허 = 트래픽 내용은 기본적으로 검사 안 함(TLS 종료는 experimental), 광역 도메인 허용 시 유출 가능, 윈도우는 알파.
- **액션**: **설치·실험** — 전역 `npm install -g @anthropic-ai/sandbox-runtime` → 테스트 디렉터리에서 `srt "curl example.com"`(차단 확인) → 크론 에이전트 1개를 감싸 위반 로그 관찰.

## 관련 페이지
- [[Anthropic]] · [[Claude-Code-워크플로우]] · [[하네스-설계-축]] · [[자기제한-명시]]
- 같은 층: [[OpenShell]] · [[openai-codex]]
- 같은 배치: [[experiential]] · [[claude-seo]] · [[gstack]] · [[infinite-canvas]]
- [[ai-news]]

## 원본
- 출처: https://github.com/anthropics/sandbox-runtime · README raw 156,873 B
- 볼트 실측(GitHub API, 2026-10-26T09:07Z): ★6,647(수집기 일치) · fork 587 · open issues 303 · Apache-2.0 · TypeScript · created 2025-10-20 · pushed 2026-10-25T22:32Z
- 신뢰도: ⭐⭐⭐ (벤더 공식 · 한계 자기명시 · ★는 상대적으로 낮음)
