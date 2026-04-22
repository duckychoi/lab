---
title: 갓대희 블로그 핵심 정리 모음
date: 2026-04-10
tags:
  - AI
  - MCP
  - Ollama
  - Playwright
  - Figma
  - Supabase
  - Skills
  - 로컬LLM
---

# 갓대희 블로그 핵심 정리 모음

> [!abstract] TL;DR
> **갓대희 블로그(goddaehee.tistory.com)** 7편의 AI 관련 글을 읽기 쉽게 시각적으로 정리한 노트입니다. 각 글의 ==핵심 내용==, 비교표, 실전 팁을 한눈에 파악할 수 있도록 구성했습니다.

---

## 1. Ollama — 로컬 LLM 환경 구축

> [!tip] 한줄 요약
> **ChatGPT 같은 AI를 내 PC에서 직접 돌릴 수 있게 해주는 오픈소스 도구**

### Ollama가 뭔가요?

Ollama는 로컬 환경(내 컴퓨터)에서 대규모 언어 모델(LLM)을 쉽게 실행할 수 있게 해주는 ==오픈소스 도구==입니다. 쉽게 말해서 **ChatGPT 같은 AI를 내 PC에서 직접 돌릴 수 있게 해주는 프로그램**이라고 보면 됩니다.

인터넷 연결 없이도, 인프라 지식 없이도 개인 PC에서 곧바로 ChatGPT 유사 AI 챗 기능을 체험할 수 있도록 설계되어 있습니다.

### 왜 Ollama를 선택해야 하나?

갓대희님은 로컬 LLM 도구가 여러 개(LM Studio, GPT4All, Text generation web UI 등) 있는데도 ==Ollama를 첫 번째 선택지==로 꼽았습니다. 그 이유는 다음과 같습니다.

| 장점 | 설명 |
|------|------|
| **설치가 진짜 쉽다** | 인스톨러 다운받고 더블클릭하면 끝. 복잡한 CUDA 설정 불필요 |
| **CLI가 직관적** | Docker 쓰듯이 `pull`, `run` 명령어로 모델 관리 |
| **API가 표준적** | OpenAI API 형식이라 기존 코드를 그대로 재활용 가능 |
| **리소스 효율적** | 메모리 사용량이 다른 도구보다 적음 |
| **활발한 커뮤니티** | GitHub Stars 148,000개, 지속적인 업데이트 |

### 핵심 특징

| 특징 | 설명 |
|------|------|
| **로컬 실행** | 인터넷 연결 없이도 AI 모델 사용 가능 |
| **쉬운 설치** | 복잡한 CUDA 설정 없이 간단 설치 |
| **다양한 모델** | Llama 3.2, Mistral, DeepSeek-R1, Gemma3 등 최신 모델 지원 |
| **API 제공** | OpenAI API와 ==호환되는 REST API== |
| **멀티모달** | 텍스트뿐만 아니라 이미지 입력도 가능 |
| **Tool Calling** | 함수 호출 기능으로 AI Agent 구축 가능 |

### 내 PC에서 돌릴 수 있을까? — 시스템 요구사항

Ollama를 설치하기 전에 ==내 컴퓨터가 감당할 수 있는지== 확인해야 합니다. 생각보다 요구사항이 높지 않습니다.

| 모델 크기 | 최소 RAM | 권장 RAM | 속도 |
|-----------|----------|----------|------|
| 7B (소형) | 8GB | 16GB | 빠름 |
| 13B (중형) | 16GB | 32GB | 보통 |
| 33B+ (대형) | 32GB | 64GB | 느림 |

### 어떤 모델을 선택해야 하나요?

용도에 따라 추천하는 모델이 다릅니다. 처음 시작한다면 ==가볍고 빠른 Llama3.2==가 좋습니다.

| 모델 | 파라미터 | 크기 | 추천 용도 |
|------|----------|------|-----------|
| **Llama3.2** | 3B | 2GB | ==처음 시작==, 범용 챗봇/QA 테스트용 |
| **Gemma3** | 4B/12B/27B | 3.3~17GB | 고효율 언어모델, 구글 생태계 최적화 |
| **DeepSeek-R1** | 7B~32B | 4GB+ | 복잡한 reasoning, function-calling (32B 권장) |
| **Phi-4** | 14B | ~9.1GB | 멀티태스크, 수학/추론 우수 |
| **Codellama** | 7B | ~3.8GB | ==코딩 전용== — 코드 생성/디버깅 특화 |
| **Llama3.3** | 70B | ~43GB | 뛰어난 언어 이해력 (64GB+ RAM 필요) |

### 설치 & 실행 방법

#### Windows 설치 (가장 간단)

1. [공식 사이트](https://ollama.com/download)에서 다운로드
2. `OllamaSetup.exe` 실행하고 설치
3. 설치 완료 후 재부팅
4. PowerShell에서 `ollama --version` 으로 정상 설치 확인

#### macOS / Linux 설치

```bash
# macOS (Homebrew)
brew install ollama

# Linux (공식 스크립트)
curl -fsSL https://ollama.ai/install.sh | sh
```

#### 모델 다운로드 & 실행

```bash
# 모델 다운로드 (예: gemma3 4B)
ollama pull gemma3:4b

# 대화형 모드로 실행
ollama run gemma3:4b

# API 서버 시작 (기본 포트 11434)
ollama serve
```

### API로 활용하기 — Python 연동 예시

CLI로만 쓰기엔 아쉬우니까 ==REST API==로 연동해서 써볼 수 있습니다. Ollama는 OpenAI API와 호환되는 REST API를 제공합니다.

```python
import requests
import json

def ask_ollama(prompt, model="llama3.2"):
    url = "http://localhost:11434/api/generate"
    data = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }
    response = requests.post(url, json=data)
    if response.status_code == 200:
        return response.json()["response"]
    else:
        return f"Error: {response.status_code}"

# 사용 예시
answer = ask_ollama("React Hook의 장점을 설명해줘")
print(answer)
```

### Tool Calling으로 AI Agent 만들기

2025년에 추가된 ==Tool Calling 기능==을 사용하면 AI가 직접 함수를 호출할 수 있습니다. 예를 들어 "서울 날씨 어때?"라고 물으면 AI가 날씨 API를 직접 호출해서 답변하는 식입니다.

```python
# Tool 정의 (날씨 정보 함수)
tools = [{
    "type": "function",
    "function": {
        "name": "get_weather",
        "description": "특정 도시의 날씨 정보를 가져옵니다",
        "parameters": {
            "type": "object",
            "properties": {
                "city": {
                    "type": "string",
                    "description": "날씨를 알고 싶은 도시 이름"
                }
            },
            "required": ["city"]
        }
    }
}]

# Ollama API에 Tool 전달
response = requests.post("http://localhost:11434/api/chat", json={
    "model": "llama3.1",
    "messages": [{"role": "user", "content": "서울 날씨 어때?"}],
    "tools": tools
})
```

### Open WebUI — 웹에서 ChatGPT처럼 사용하기

웹 브라우저에서 ==ChatGPT처럼 사용==할 수 있는 Open WebUI도 Docker로 설치 가능합니다.

```bash
docker run -d --network=host \
  -v open-webui:/app/backend/data \
  --name open-webui \
  --restart always \
  ghcr.io/open-webui/open-webui:main
```

> [!success] 갓대희님의 정리
> - **생각보다 쉽다**: 복잡한 ML 환경 설정 없이도 몇 분 만에 로컬 LLM 환경 구축 가능
> - **비용 효율적**: 한 번 설치하면 클라우드 API 비용 없이 무제한 사용
> - **개인정보 보호**: 모든 데이터가 로컬에서 처리되어 프라이버시 걱정 없음
> - **확장성**: REST API로 다양한 애플리케이션과 쉽게 통합 가능

> [!warning] 주의
> GPU 없어도 CPU만으로 충분히 사용 가능하지만 ==응답 속도가 GPU 대비 느립니다==. ChatGPT와 완전히 같은 수준은 아니지만, 일반적인 질답이나 코딩 도움 정도는 충분히 사용할 만합니다.

> [!faq]- Q: 인터넷 연결 없이도 사용할 수 있나요?
> 예! 모델을 한 번 다운로드하면 오프라인에서도 완전히 작동합니다. 데이터가 외부로 전송되지 않아 보안도 뛰어납니다.

---

## 2. Agent Skill 오픈 표준 (SKILL.md)

> [!tip] 한줄 요약
> **SKILL.md 하나로 Claude, Cursor, Copilot, Gemini ==모든 AI 에이전트==에서 재사용 가능한 오픈 표준**

### Agent Skill이 뭔가요?

AI 도구를 새로 바꿀 때마다 이런 생각 해본 적 없나요? ==**"Claude Code에서 공들여 만든 커스텀 설정, Cursor로 넘어가면 다시 처음부터 만들어야 하나?"**==

Agent Skill은 바로 이 문제를 해결합니다. ==SKILL.md 파일 형식==을 따르는 모든 스킬은 표준을 지원하는 어떤 AI 에이전트에서도 작동합니다. 한 번 만들어두면 Claude Code에서도, Cursor에서도, GitHub Copilot에서도 그대로 쓸 수 있습니다.

### 핵심 오해 깨기

> [!danger] 흔한 오해 3가지
> 1. "Claude Code에서만 쓸 수 있겠지" → ==아니다. Cursor, Copilot, Gemini CLI에서도 된다==
> 2. "Anthropic이 만든 거면 Claude에 최적화되어 있겠지" → ==표준을 오픈했기 때문에 어디서나 동일하게 동작한다==
> 3. "직접 만들기 어렵겠지" → ==SKILL.md 하나로 5분이면 만든다==

### 오픈 표준의 탄생 배경

Anthropic이 2025년 12월에 씨앗을 심었고, Vercel이 CLI를 만들었으며, 커뮤니티가 스킬을 만들어 가는 ==크로스플랫폼 오픈 표준==입니다.

| 시점 | 내용 |
|------|------|
| **2025-12-16** | agentskills/agentskills 저장소 첫 커밋 |
| **2025-12-18** | 오픈 표준으로 공개 — agentskills.io 론칭 |
| **이후** | Vercel Labs가 skills.sh 디렉토리 사이트 + npx skills CLI 제작. Cursor, GitHub Copilot, Gemini CLI 등 순차 지원 |
| **2026-03 현재** | ==32개 이상의 AI 에이전트/IDE가 공식 지원== |

### SKILL.md 파일 구조

스킬 하나는 하나의 디렉토리로 구성됩니다. ==필수 파일은 SKILL.md 뿐==이고 나머지는 모두 선택입니다.

```
my-skill/
├── SKILL.md          ← 필수. 스킬의 전부가 여기에
├── scripts/          ← 선택. 스킬이 사용할 스크립트/도구
│   ├── setup.sh
│   └── validate.py
├── references/       ← 선택. 참고 문서, 예시 파일
│   ├── example.md
│   └── patterns.md
└── assets/           ← 선택. 이미지, 기타 리소스
```

### SKILL.md Frontmatter 필드

SKILL.md는 파일 상단의 ==YAML frontmatter==와 그 아래의 ==Markdown 본문==으로 구성됩니다.

```yaml
---
name: my-awesome-skill          # 필수. 최대 64자. 소문자+숫자+하이픈만
description: |                  # 필수. 최대 1024자
  이 스킬은 무엇을 하는지 한 문단으로 설명한다.
  언제 호출되어야 하는지도 여기에 적는다.
license: MIT                    # 선택
compatibility: |                # 선택. 지원 플랫폼, 버전 제약 등
  Claude Code 1.0+, Cursor 0.40+
metadata:                       # 선택. 임의 키-값 쌍
  version: 1.2.0
  author: your-name
  tags: [productivity, frontend]
---
```

### Progressive Disclosure 3단계 — 왜 필요한가?

에이전트가 ==모든 스킬의 전체 내용을 한꺼번에 로딩==하면 컨텍스트 윈도우가 금방 채워집니다. 그래서 ==3단계에 걸쳐 필요한 만큼만 로딩==하는 방식을 씁니다.

| 단계 | 로딩 내용 | 토큰 비용 | 역할 | 언제? |
|------|-----------|-----------|------|-------|
| **Tier 1** | name + description만 | ~50-100 | "이 스킬 쓸까?" 판단 | 세션 시작 시 자동 |
| **Tier 2** | SKILL.md 전체 본문 | ~5,000 이하 | 실제 수행 지침 | 스킬 활성화 시 |
| **Tier 3** | scripts/references/assets | 온디맨드 | 보조 리소스 | 필요할 때만 |

> [!info] 실전 팁
> **description**은 "언제 나를 써야 하는지"를 명확하게 써야 합니다. Tier 1에서 에이전트가 이 텍스트만 보고 스킬 활성화 여부를 결정하기 때문입니다.
> 예: "코드 리뷰 요청, PR 피드백, 코드 개선 제안 시 활성화"처럼 ==구체적인 트리거 조건==을 포함하세요.

### 플랫폼별 설치 경로

각 플랫폼마다 스킬을 읽어오는 경로가 다릅니다. ==크로스플랫폼 표준 경로인 `~/.agents/skills/`==에 저장하고 각 에이전트 경로에 심볼릭 링크를 거는 것이 가장 실용적입니다.

| 플랫폼 | 전역 경로 | 프로젝트 경로 |
|--------|-----------|---------------|
| **Claude Code** | `~/.claude/skills/` | `.claude/skills/` |
| **Codex CLI** | `~/.agents/skills/` | `.agents/skills/` |
| **Gemini CLI** | `~/.gemini/skills/` | `.agents/skills/` |
| **Cursor** | `~/.cursor/skills/` | `.cursor/skills/` |
| **GitHub Copilot** | `~/.copilot/skills/` | `.copilot/skills/` |
| **==크로스플랫폼 표준==** | `~/.agents/skills/` | `.agents/skills/` |

```bash
# 표준 경로에 스킬 보관
mkdir -p ~/.agents/skills/my-skill

# 각 에이전트별로 심볼릭 링크 연결
ln -s ~/.agents/skills/my-skill ~/.claude/skills/my-skill
ln -s ~/.agents/skills/my-skill ~/.cursor/skills/my-skill
```

### 주목할 스킬 6가지 — 각 스킬이 뭘 해주나?

#### 1. Frontend Design — "AI 티" 없애기

AI가 생성한 UI를 보면 금방 알아볼 수 있습니다. ==Inter 폰트, 파란색 그라디언트, 카드 UI의 과다 사용==... Frontend Design 스킬은 이런 패턴을 명시적으로 ==금지==하고 독창적인 디자인을 유도합니다.

- **금지 폰트**: Inter, Roboto, Arial, Space Grotesk 등
- **금지 색상**: 흰 배경 위 보라색 그라디언트
- **선택 가능한 방향**: brutalist, retro-futuristic, editorial/magazine, soft/pastel 등 10가지+

#### 2. Planning with Files — 파일 기반 작업 계획

Manus가 사용하는 방식에서 영감을 받은 스킬입니다. ==핵심 아이디어: Context Window = RAM, Filesystem = Disk==. AI가 작업 계획과 진행 상황을 파일에 저장해두면, 컨텍스트가 초기화되더라도 파일을 읽어 이어서 작업을 계속할 수 있습니다.

- `task_plan.md`: 전체 작업 계획
- `findings.md`: 조사/리서치 결과 누적
- `progress.md`: 진행 상황 추적

#### 3. Superpowers — 7단계 개발 워크플로우

==brainstorming부터 최종 마무리까지 7단계==를 구조화하는 올인원 스킬입니다.

```
1. brainstorming → 아이디어 발산
2. git-worktrees → 병렬 개발
3. writing-plans → 구현 계획 수립
4. executing-plans → 계획 실행
5. TDD → 테스트 주도 개발
6. code-review → 코드 품질 검토
7. finishing → 최종 점검
```

#### 4. Humanizer — AI 문체 제거기

AI가 작성한 글에는 특유의 패턴이 있습니다. Humanizer는 이 패턴들을 구체적으로 정의하고 ==제거==합니다.

- 과도한 의미 부여 (중요성·레거시 강조)
- 마케팅 문구 같은 홍보성 표현
- "전문가들에 따르면" 같은 출처 불명 표현
- em dash(—) 남용
- "delve into", "tapestry" 같은 AI 특유 단어

#### 5. MCP Builder — MCP 서버 개발 가이드

MCP(Model Context Protocol) 서버를 ==설계→구현→테스트→배포== 4단계로 안내합니다.

#### 6. Superpowers-Chrome — 브라우저 자동화

Chrome DevTools Protocol을 사용해 AI 에이전트가 ==실제 Chrome 브라우저를 제어==할 수 있게 해줍니다.

| 스킬 | 기능 | GitHub Stars |
|------|------|--------------|
| **Frontend Design** | AI 티 없애기, 독창적 UI 유도 | 94,479 |
| **Planning with Files** | 파일 기반 작업 계획 (Manus 스타일) | 16,151 |
| **Superpowers** | 7단계 개발 워크플로우 올인원 | 86,879 |
| **Humanizer** | AI 문체 패턴 제거 | 9,423 |
| **MCP Builder** | MCP 서버 개발 4단계 가이드 | 94,479 |
| **Superpowers-Chrome** | Chrome 브라우저 자동화 | 204 |

### 스킬 직접 만들기 — 5분이면 충분

```bash
# 1단계: 디렉토리 만들기
mkdir -p ~/.agents/skills/commit-helper

# 2단계: SKILL.md 작성 (name, description 두 필드면 최소 완성)
```

```markdown
---
name: commit-helper
description: |
  Git 커밋 메시지를 작성할 때 활성화된다.
  Conventional Commits 형식, 한국어 작성.
  트리거: "커밋", "commit message" 요청 시
---

# Commit Helper

## 형식
<type>(<scope>): <subject>

## 타입 정의
- feat: 새 기능 / fix: 버그 수정 / docs: 문서 변경
- refactor: 리팩터링 / test: 테스트 / chore: 기타
```

```bash
# 3단계: 에이전트 재시작하면 바로 인식됨
```

### 스킬 찾는 곳 3가지

| 곳 | 설명 | URL |
|----|------|-----|
| **skills.sh** | Vercel이 만든 공식 디렉토리 + CLI | [skills.sh](https://skills.sh) |
| **anthropics/skills** | Anthropic 공식 스킬 저장소 (94,479 Stars) | [GitHub](https://github.com/anthropics/skills) |
| **agentskills.io** | 표준 공식 문서 (32개+ 플랫폼 목록) | [agentskills.io](https://agentskills.io) |

```bash
# 스킬 검색
npx skills find frontend

# 스킬 설치
npx skills add anthropics/skills --skill frontend-design

# 설치된 스킬 목록
npx skills list
```

### 팀에서 스킬 공유하기

팀 전체가 같은 코드 리뷰 기준을 써야 한다면, ==프로젝트 레포에 `.agents/skills/` 디렉토리를 만들고 git에 커밋==하면 됩니다.

```
my-project/
├── src/
├── .agents/
│   └── skills/
│       ├── code-review/    ← 팀 코드 리뷰 기준
│       ├── commit-style/   ← 커밋 메시지 컨벤션
│       └── test-guide/     ← 테스트 작성 가이드
└── README.md
```

팀원이 레포를 클론하거나 pull 받으면 ==자동으로 동기화==됩니다. 어떤 에이전트를 쓰든 동일한 기준이 적용됩니다.

> [!success] 핵심 정리
> - **한 번 만들면 어디서나**: Claude, Cursor, Copilot, Gemini 등 32개+ 플랫폼에서 동일하게 작동
> - **5분이면 만든다**: name과 description 두 필드만 채우면 최소 스킬 완성
> - **팀 공유는 .agents/skills/**: 프로젝트 루트에 넣고 git 커밋하면 팀 전체 자동 동기화

> [!warning] 흔한 함정 4가지
> 1. SKILL.md 본문이 ==5,000 토큰 초과== → 토큰 낭비. 긴 내용은 references/로 분리
> 2. ==description이 모호== → 엉뚱한 타이밍에 활성화. 구체적 트리거 조건 필수
> 3. ==name에 언더스코어/대문자== 사용 → 표준 위반. 소문자+하이픈만 허용
> 4. ==플랫폼별 경로 혼란== → `~/.agents/skills/`에 두고 심볼릭 링크 활용

---

## 3. Playwright MCP — 브라우저 자동화

> [!tip] 한줄 요약
> **자연어로 브라우저를 조종하는 MCP 서버. 접근성 트리(Accessibility Tree) 기반으로 빠르고 정확**

### Playwright MCP가 뭔가요?

Playwright는 Microsoft가 만든 브라우저 자동화 라이브러리입니다. 기존에는 개발자가 직접 JavaScript/TypeScript 코드를 작성해 브라우저를 제어했는데, ==**Playwright MCP**는 Claude 같은 AI 모델이 자연어 명령으로 Playwright를 직접 조작==할 수 있게 해줍니다.

예를 들어 **"GitHub에 접속해서 내 레포지토리 목록을 확인해줘"** 라고 말하면 Claude가 실제로 브라우저를 열고 해당 작업을 수행합니다.

### 접근성 트리(Accessibility Tree)가 뭔가요?

Playwright MCP의 핵심은 ==스크린샷이 아닌 접근성 트리==를 통해 페이지를 이해한다는 것입니다. 접근성 트리는 웹 페이지의 구조적 정보(버튼, 링크, 입력창 등)를 ==텍스트 형태==로 표현한 것입니다.

스크린샷 방식은 이미지를 분석해야 해서 ==느리고 토큰 소모가 크지만==, 접근성 트리 방식은 ==구조화된 텍스트를 바로 처리==하므로 훨씬 빠르고 정확합니다. 시각적으로 숨겨진 요소나 동적으로 생성된 콘텐츠도 정확히 파악할 수 있습니다.

### 설치 방법

```bash
# 기본 설치
claude mcp add playwright npx '@playwright/mcp@latest'

# 헤드리스 모드 (브라우저 창이 보이지 않음)
claude mcp add playwright npx '@playwright/mcp@latest' --headless
```

> [!info] 자연어로도 설치 가능
> Claude Code에 **"Playwright mcp 설치해줘"** 라고 말하면 알아서 설치해줍니다.

### Snapshot vs Vision — 두 가지 동작 모드

| 구분 | Snapshot 모드 (기본) | Vision 모드 |
|------|---------------------|-------------|
| **동작 방식** | 접근성 트리 분석 | 스크린샷 + X/Y 좌표 |
| **속도** | ==빠름== | 느림 |
| **토큰 소모** | ==적음== | 많음 (이미지 포함) |
| **Canvas/WebGL** | 제한적 | ==적합== |
| **활성화** | 기본값 | `--caps vision` 플래그 |

대부분의 경우 기본값인 ==Snapshot 모드로 충분==합니다. Canvas 기반 앱이나 시각적 판단이 필요한 경우에만 Vision 모드를 고려하세요.

### 핵심 Tool 정리

#### 가장 많이 쓰는 Tool TOP 3

1. **`browser_navigate`** — URL로 이동. ==모든 자동화의 시작점==
2. **`browser_snapshot`** — 접근성 트리로 현재 페이지 구조를 파악. ==Snapshot 모드의 핵심==
3. **`browser_click` / `browser_type`** — 요소 클릭 & 텍스트 입력

#### 전체 Tool 카테고리

| 카테고리 | Tool | 설명 |
|----------|------|------|
| **네비게이션** | `browser_navigate` | URL로 이동 |
| | `browser_navigate_back` | 뒤로 가기 |
| | `browser_tab_new/close` | 탭 관리 |
| **상호작용** | `browser_click` | 요소 클릭 (ref 기반) |
| | `browser_type` | 텍스트 입력 |
| | `browser_press_key` | 키보드 입력 (Enter, Tab 등) |
| | `browser_select_option` | 드롭다운 선택 |
| | `browser_hover` | 마우스 호버 |
| **캡처** | `browser_snapshot` | 접근성 트리 스냅샷 |
| | `browser_take_screenshot` | 스크린샷 |
| | `browser_pdf_save` | PDF 저장 |

### 실전 활용 예시

#### 예시 1: 웹사이트 스크린샷 + 분석

```
사용자: "https://github.com/microsoft/playwright-mcp 에 접속해서 
       README의 주요 내용을 요약해줘"

Claude 내부 동작:
1. browser_navigate → 페이지 접속
2. browser_snapshot → 접근성 트리로 페이지 구조 파악
3. browser_take_screenshot → 스크린샷 캡처
4. 결과 분석 후 요약 응답
```

#### 예시 2: 로그인 플로우 테스트

```
사용자: "localhost:3000/login에서 test@example.com / password123으로 
       로그인하고 성공 여부를 확인해줘"

Claude 내부 동작:
1. browser_navigate → 로그인 페이지 접속
2. browser_snapshot → 이메일 입력칸(ref=e3), 비밀번호(ref=e5), 
                      로그인 버튼(ref=e7) 확인
3. browser_type(ref=e3, "test@example.com") → 이메일 입력
4. browser_type(ref=e5, "password123") → 비밀번호 입력
5. browser_click(ref=e7) → 로그인 버튼 클릭
6. browser_snapshot → /dashboard로 이동 확인 → "로그인 성공"
```

> [!info] ref가 뭔가요?
> `browser_snapshot`이 반환하는 접근성 트리에는 각 요소에 ==ref 값==이 부여됩니다 (예: e3, e5, e7). Claude가 이 ref 값으로 어떤 버튼을 클릭할지 식별합니다. ==개발자가 CSS 셀렉터를 직접 지정할 필요가 없습니다.==

### Playwright MCP vs CLI vs codegen — 3가지 방법 비교

| 방법 | 장점 | 단점 | 추천 상황 |
|------|------|------|-----------|
| **MCP** | 자연어 요청으로 즉시 실행, 대화형 피드백 | 재현성 낮음, 토큰 비용 | 탐색적 테스트, 일회성 자동화 |
| **codegen** | 조작이 코드로 자동 변환 | 생성 코드 수정 필요 | 테스트 코드 초안 작성 |
| **CLI 직접** | 완전한 제어, 완벽한 재현성 | API 학습 필요 | CI/CD, 정형화된 E2E |

> [!tip] 갓대희님 추천 — 실전 3단계 조합
> 1. **MCP**로 "이 플로우 되나?" ==빠르게 탐색== 및 검증
> 2. **codegen**(`npx playwright codegen`)으로 검증된 플로우를 ==테스트 코드로 변환==
> 3. **CLI**로 ==CI/CD 파이프라인에 통합==

---

## 4. Playwright CLI vs MCP — 심층 비교

> [!tip] 한줄 요약
> ==playwright-cli가 기능적 상위 호환==이지만, Vision 모드와 Claude Desktop 지원은 MCP만 가능

### 비교 대상 정리

갓대희님은 ==Microsoft가 별도로 제공하는 playwright-cli==가 MCP의 기능적 상위 호환에 가깝다고 분석했습니다. 다만 MCP만이 줄 수 있는 ==고유한 가치도 분명히 존재==한다고 합니다.

| 구분 | Playwright MCP | playwright-cli |
|------|---------------|----------------|
| **정의** | `@playwright/mcp` MCP 서버 | `@playwright/cli` 에이전트용 CLI |
| **설치** | 별도 MCP 서버 설치 필요 | `npm install -g @playwright/cli` |
| **호출** | MCP 프로토콜 Tool 호출 | `playwright-cli [command]` |
| **환경** | Claude Code, ==Claude Desktop== | Claude Code (Bash) |

> [!warning] 주의
> `playwright-cli`는 `npx playwright`와 ==다른 도구==입니다. `npx playwright`는 테스트 실행용(`npx playwright test`)이고, `playwright-cli`는 에이전트 전용 CLI입니다.

### 전체 기능 비교

| 기능 | MCP | CLI | 우위 |
|------|-----|-----|------|
| 도구 수 | ~22개 (opt-in 35+) | ==50+== | CLI |
| Claude Desktop | ==지원== | 미지원 | MCP |
| 토큰 효율 | 많이 소모 | ==적게 소모== | CLI |
| Vision/Canvas/WebGL | ==지원== | 미지원 | MCP |
| 네트워크 모킹 | 미지원 | ==지원== | CLI |
| 쿠키 관리 | 미지원 | ==지원== | CLI |
| 세션 저장/불러오기 | 정적만 | ==동적 가능== | CLI |
| 구간별 트레이싱 | 세션 전체만 | ==구간별 가능== | CLI |
| 테스트 코드 생성 | 미지원 | ==지원== | CLI |

### 왜 CLI가 토큰을 더 적게 쓸까?

이것이 ==비용과 직결==되는 중요한 차이입니다.

```
MCP 방식:
  접근성 트리/스크린샷 → LLM context에 직접 삽입 → 수천 토큰 소모

CLI 방식:
  결과를 파일에 저장 → 경로만 반환 → 수십 토큰 소모
```

MCP는 `tools/call` 응답으로 접근성 스냅샷(수천 토큰)이나 스크린샷(base64 이미지)을 ==LLM context window에 직접 삽입==합니다. 반면 playwright-cli는 결과를 파일로 저장하고 ==경로 한 줄만 반환==하므로 컨텍스트 소모가 최소화됩니다.

### MCP만 가능한 것 (대체 불가능)

1. **Vision 모드** — Canvas, WebGL, PDF 뷰어 등 ==접근성 트리가 없는 UI==를 조작할 때 유일한 선택지
2. **Claude Desktop 호환** — Claude Desktop에서 브라우저 자동화를 쓰려면 ==MCP가 유일한 방법==

### playwright-cli만 가능한 것

| 기능 | 설명 |
|------|------|
| `route` / `unroute` | API 응답 가로채서 테스트용 데이터로 교체 |
| `cookie-set/list/delete` | 쿠키 직접 설정/관리 |
| `state-save` / `state-load` | 로그인 상태를 파일로 저장/복원 |
| `tracing-start/stop` | ==원하는 구간만== 트레이싱 기록 |
| `-s=name` | 네임드 세션으로 ==여러 사용자 동시 테스트== |
| `npx playwright codegen` | 브라우저 조작을 테스트 코드로 자동 변환 |

### 상황별 선택 가이드

| 상황 | 추천 | 이유 |
|------|------|------|
| E2E 테스트 자동화 | ==CLI== | 네트워크 모킹, 세션 관리 필요 |
| 웹 스크래핑 반복 작업 | ==CLI== | 토큰 효율 우위, 비용 절감 |
| Canvas/WebGL 시각 검증 | ==MCP== | Vision 모드가 유일한 선택지 |
| Claude Desktop에서 사용 | ==MCP== | Bash 실행 불가 환경 |
| CI/CD 파이프라인 | ==CLI== | 별도 MCP 프로세스 관리 불필요 |

> [!success] 갓대희님의 최종 결론
> **"Skills + CLI 조합을 기본으로, MCP는 Vision 모드가 필요할 때 보조 도구로"**
>
> Claude Code의 내장 Playwright Skills와 CLI를 조합하면 ==MCP의 기능적 상위 호환==이 됩니다. 다만 Vision 모드와 Claude Desktop은 ==MCP만이 제공할 수 있는 고유 가치==입니다.

---

## 5. Figma MCP — 디자인을 코드로 변환

> [!tip] 한줄 요약
> **Figma 디자인 파일의 메타데이터를 AI가 직접 읽어서 코드 생성. 스크린샷보다 ==정확==**

### Figma MCP가 뭔가요?

디자이너와 개발자의 협업에서 ==가장 큰 병목==은 "디자인을 코드로 변환하는 작업"입니다. 기존에는 디자이너가 스크린샷을 캡처해서 전달하거나, Figma Dev Mode에서 수치를 하나씩 확인해가며 코드를 작성했습니다.

Figma MCP를 사용하면 ==Claude에게 "이 Figma 프레임 링크를 보고 React 컴포넌트를 만들어줘"== 라고 말하는 것만으로 AI가 실제 디자인의 레이아웃, 색상, 타이포그래피, 간격 등 ==정확한 수치==를 읽어서 코드를 생성합니다.

### 왜 스크린샷보다 나은가?

스크린샷을 보고 AI가 코드를 생성하면 ==**"버튼 패딩이 12px인지 16px인지"** 정확히 알 수 없습니다==. 하지만 Figma MCP는 ==구조화된 메타데이터==를 통해 정확한 수치, 폰트 이름, 색상 hex 값, 자동 레이아웃 설정 등을 전달합니다. 픽셀 퍼펙트 구현이 훨씬 쉬워집니다.

### 설치 방법

```bash
claude mcp add --transport http figma https://mcp.figma.com/mcp
```

> [!info] 인증 방식
> Figma MCP는 PAT가 아닌 ==OAuth 인증==을 사용합니다. 설치 후 Claude Code에서 `/mcp` → Figma → Authenticate를 누르면 브라우저가 열리면서 자동 로그인됩니다.

### 원격 서버 vs 데스크탑 서버

| 구분 | 원격 서버 | 데스크탑 서버 |
|------|-----------|---------------|
| **서버 위치** | Figma 호스팅 (mcp.figma.com) | 로컬 (Figma 데스크탑 앱) |
| **Figma 앱 필요** | 불필요 (웹 브라우저 OK) | 필요 (데스크탑 앱 실행 중) |
| **플랜 요건** | ==모든 플랜 (무료 포함)== | Dev 또는 Full 시트 (유료) |
| **Starter 제한** | ==월 6회 Tool 호출== | 해당 없음 |

### 핵심 Tool 13개 — 어떤 순서로 쓰나?

```
1. get_design_context → 상세 메타데이터 획득 (가장 핵심!)
2. get_metadata → 고수준 노드 맵 (응답이 너무 클 때)
3. get_screenshot → 시각적 참조 이미지 확보
4. get_variable_defs → 디자인 토큰 (색상, 간격, 타이포그래피)
5. → 이 정보를 바탕으로 코드 생성 시작
```

**Figma URL 구조 이해하기**

```
https://www.figma.com/design/[파일키]/[파일명]?node-id=[노드ID]

예시: https://www.figma.com/design/AbCdEfGhIjKl/MyDesign?node-id=1%3A234
                                         ^^^^^^^^^^^^                  ^^^^^
                                         파일 키                       노드 ID (1:234)
```

### 양방향 워크플로우 — Code ↔ Figma

Figma MCP는 ==단방향이 아닙니다==. 두 방향 모두 가능합니다.

| 방향 | Tool | 설명 |
|------|------|------|
| **Figma → Code** | `get_design_context` | Figma 프레임을 React/Vue 코드로 변환 |
| **Code → Figma** | `generate_figma_design` | 웹페이지를 ==편집 가능한 Figma 레이어==로 역변환 |

```
Code → Figma → Code 선순환:
1. 이미 만든 웹사이트를 generate_figma_design으로 Figma에 역캡처
2. 캡처된 Figma 파일을 get_design_context로 읽어 코드 개선
3. 프로젝트 전반의 디자인 일관성 유지
```

### 실전 활용 예시

#### Figma 프레임 → React 컴포넌트

```
사용자: "이 Figma 프레임을 보고 React + Tailwind CSS 컴포넌트를 만들어줘"
       (Figma URL 전달)

Claude 내부 동작:
1. get_design_context → 배경색(#6366f1), padding(12px/4px), 
   그림자, 폰트 정보 등 메타데이터 획득
2. 프로젝트 스타일에 맞게 적응 (폰트 교체 등)
3. Badge.tsx 컴포넌트 코드 생성
```

#### 디자인 토큰 → CSS 변수 추출

```
사용자: "이 Figma 파일에서 색상 변수와 타이포그래피를 CSS 변수로 변환해줘"

Claude 내부 동작:
1. get_variable_defs → Figma Variables 조회
2. 없으면 get_design_context로 실제 사용된 값 추출
3. CSS 커스텀 프로퍼티(:root) 파일 생성
```

> [!warning] Starter 플랜 주의
> `generate_figma_design` 캡처 ==1회에 약 4회 Tool 호출==이 소모됩니다 (whoami 1회 + generate_figma_design 약 3회). ==월 6회 한도의 67%가 한 번의 캡처에 소진==됩니다. 적극 활용하려면 유료 플랜이 필요합니다.

### Figma MCP vs Dev Mode vs REST API

| 방법 | 특징 | 인증 | 추천 상황 |
|------|------|------|-----------|
| **Figma MCP** | 자연어로 디자인 분석 및 코드 변환 | OAuth | AI 코딩 워크플로우 |
| **Figma Dev Mode** | 브라우저에서 즉시 수치 확인 | Figma 로그인 | 빠른 단발성 수치 확인 |
| **Figma REST API** | 완전한 프로그래밍 제어 | PAT | 자동화 스크립트, CI/CD |

> [!success] 갓대희님의 추천
> - Figma 디자인을 React/Vue 코드로 자주 변환하는 ==프론트엔드 개발자==
> - 디자이너와의 ==Handoff 비용을 줄이고 싶은 팀==
> - ==코드를 먼저 개발하고 나중에 Figma 자산을 정리하고 싶은 분== (generate_figma_design 역캡처)

---

## 6. Supabase MCP — 자연어로 DB 관리

> [!tip] 한줄 요약
> **자연어로 PostgreSQL 스키마 설계, SQL 실행, RLS 설정까지 ==자동 처리==**

### Supabase MCP가 뭔가요?

보통 Supabase 작업은 ==대시보드 SQL Editor에서 직접 쿼리를 실행==하거나, ==supabase CLI로 마이그레이션을 관리==하는 방식으로 이루어집니다. Supabase MCP를 쓰면 ==Claude Code 대화창에서 "users 테이블에 created_at 컬럼 추가해줘"== 라고 하면 마이그레이션까지 자동으로 적용해줍니다.

### 특별한 이유 — DDL과 DML 분리

그냥 SQL을 실행하는 것만이 아니라, ==**스키마 변경은 apply_migration으로, 데이터 조회는 execute_sql로 구분**==해줍니다. 이렇게 DDL과 DML이 분리되어 있어서 ==실수로 스키마를 날려먹을 위험이 줄어듭니다==.

### 설치 & 인증

```bash
# 설치
claude mcp add --transport http supabase https://mcp.supabase.com/mcp

# 설치 후 반드시 Claude Code 재시작 → /mcp → Supabase → Authenticate
```

> [!warning] 설치 직후 "Failed to connect"가 정상
> MCP 서버를 등록한 직후에는 ==OAuth 인증이 아직 완료되지 않았기 때문==에 연결 실패 상태입니다. ==Claude Code를 반드시 재시작==해야 인증 플로우가 트리거됩니다.

**OAuth가 안 될 때 — PAT 방식으로 전환**

```bash
# PAT 발급: Supabase 대시보드 → 프로필 → Account → Access Tokens
claude mcp remove supabase
claude mcp add --transport http supabase \
  "https://mcp.supabase.com/mcp?project_ref=YOUR_PROJECT_REF" \
  --header "Authorization: Bearer YOUR_SUPABASE_PAT"
```

### 32개 Tool 중 실무에서 가장 많이 쓰는 3개

| Tool | 용도 | 설명 |
|------|------|------|
| **`execute_sql`** | SELECT/INSERT/UPDATE/DELETE | ==DML 작업==은 거의 다 여기로. "어떤 데이터 보여줘"라고 하면 결국 이 tool이 호출 |
| **`apply_migration`** | CREATE/ALTER TABLE 등 | ==스키마 변경==을 마이그레이션 이력에 자동 기록. 테이블 생성/수정/인덱스 추가 핵심 |
| **`list_tables`** | 현재 스키마 파악 | Claude가 SQL을 제대로 짜려면 ==먼저 이걸 호출==해서 테이블 구조를 봐야 함 |

> [!important] DDL vs DML 분리 원칙
> - **`apply_migration`** → CREATE TABLE, ALTER TABLE, CREATE INDEX 등 ==DDL== (마이그레이션 이력에 기록됨)
> - **`execute_sql`** → SELECT, INSERT, UPDATE, DELETE 등 ==DML== (이력에 기록되지 않음)
>
> 이 구분 덕분에 ==실수로 스키마를 날려먹을 위험이 줄어듭니다==.

### 8개 Tool 그룹 전체

| 그룹 | Tool 예시 | 설명 |
|------|-----------|------|
| **Database** | execute_sql, apply_migration, list_tables | SQL 실행, 마이그레이션, 테이블 조회 |
| **Debugging** | get_logs, get_advisors | 로그 조회, ==보안/성능 어드바이저== |
| **Development** | generate_typescript_types, get_project_url | 타입 생성, API URL 조회 |
| **Edge Functions** | list/deploy_edge_function | 서버리스 함수 관리 |
| **Project Management** | create/list/pause/restore_project | 프로젝트 관리 |
| **Branching** | create/merge/delete_branch | Preview Branch (실험적) |
| **Storage** | list_storage_buckets | 스토리지 (기본 비활성화) |

### 실전 활용 예시

#### 예시 1: 자연어로 DB 스키마 설계

```
사용자: "블로그 서비스 만들건데 users, posts, comments, tags 테이블이 필요해.
       posts와 tags는 다대다 관계고, RLS도 설정해줘."

Claude 내부 동작:
1. list_tables → 현재 테이블 없음 확인
2. apply_migration → users, posts, comments, tags, post_tags 5개 테이블 생성
3. RLS 정책까지 자동 적용 (인증된 사용자만 자기 데이터 CRUD)

소요 시간: 약 30초 (대화 1회)
→ CLI로 했으면 약 5분 (SQL 직접 작성 + 테스트)
```

#### 예시 2: 자연어로 SQL 쿼리 실행 & 분석

```
사용자: "거래량 급증률이 가장 높은 종목 Top 5를 보여줘"

Claude 내부 동작:
1. list_tables → 테이블 구조 파악
2. execute_sql → SELECT ... FROM intraday_top50_members ORDER BY surge_rate DESC LIMIT 5
3. 결과를 표 형태로 정리 + 인사이트 제공

"대한해운이 surge_rate 875.74로 압도적 1위. 해운 섹터에 수급이 몰린 것으로 보입니다."
```

#### 예시 3: 보안 점검

```
사용자: "현재 DB의 보안 취약점을 점검해줘"

Claude 내부 동작:
1. get_advisors → 보안/성능 어드바이저 결과 획득
2. execute_sql → 상세 확인
3. 수정 SQL 자동 생성
4. apply_migration → 수정 적용

→ 전체 과정이 하나의 대화 흐름에서 자동 처리
```

### Read-only 모드 — 프로덕션 DB 필수

프로덕션 DB에 MCP를 연결할 때는 ==반드시 read_only 모드==를 사용해야 합니다.

```
URL에 ?read_only=true 추가
→ execute_sql은 SELECT만 허용
→ apply_migration, create_project 등 모든 변경 tool 비활성화
```

> [!danger] 보안 — 반드시 지켜야 할 것
> - ==RLS가 적용되지 않는 관리자 수준 권한==으로 실행됨. 테이블에 RLS를 걸어놔도 MCP로 쿼리하면 모든 행이 다 보임
> - 프로덕션 DB는 ==반드시 `read_only=true`==. 부득이하게 접근해야 하는 경우에만 차선책으로 사용
> - execute_sql 결과가 ==전부 LLM context window에 들어감== → `LIMIT` 필수, 집계 쿼리 권장
> - 대량 데이터 분석은 ==CLI + psql==을 사용

> [!faq]- execute_sql이 토큰을 많이 먹는 이유?
> MCP의 execute_sql 결과는 ==전부 LLM의 context window에 들어갑니다==. 수천 행짜리 결과를 몇 번 반복하면 토큰이 순식간에 날아갑니다.
>
> **해결책:**
> 1. `LIMIT` 꼭 붙이기: `SELECT * FROM users LIMIT 20`
> 2. 집계 쿼리 사용: `COUNT`, `AVG`, `GROUP BY`
> 3. 대량 작업은 CLI + psql 사용

---

## 7. Supabase CLI vs MCP — 심층 비교

> [!tip] 한줄 요약
> **MCP로 스키마 설계/쿼리, CLI로 로컬 개발/배포 — ==상호보완이 정답==**

### 비교 대상 정리

| 구분 | Supabase MCP | supabase CLI |
|------|-------------|--------------|
| **정의** | AI 에이전트 기반 DB 관리 | 프로젝트 라이프사이클 관리 도구 |
| **설치** | `claude mcp add` (원클릭) | `brew install supabase/tap/supabase` |
| **인증** | OAuth / PAT | `supabase login` |
| **호출** | MCP Tool (자연어) | `supabase [command]` (Bash) |
| **주요 역할** | ==스키마 설계, 쿼리, 보안 점검== | ==로컬 개발, 마이그레이션, CI/CD== |

### 한눈에 보는 선택 가이드

| 작업 | 추천 | 이유 |
|------|------|------|
| 스키마 설계/변경 | ==MCP== | AI가 기존 스키마 이해 & SQL 자동 생성 |
| 데이터 조회/분석 | ==MCP== | 자연어로 복잡한 쿼리 요청 가능 |
| 로컬 개발 환경 | ==CLI== | `supabase start`로 Docker 기반 전체 스택 구동 |
| 마이그레이션 관리 | ==CLI== | diff, squash, test 등 파이프라인 기능 |
| 보안 점검 | ==MCP== | get_advisors + execute_sql 조합 |
| CI/CD 배포 | ==CLI== | 비대화형 자동화에 적합 |
| 타입 생성 | ==동등== | 양쪽 모두 가능 |

### CLI만 할 수 있는 것 — 로컬 개발의 핵심

`supabase start` ==한 줄이면== Docker로 PostgreSQL, Auth, Storage, Realtime, Studio까지 로컬에서 전부 띄울 수 있습니다. ==이건 MCP로는 절대 할 수 없는 영역==입니다.

| 서비스 | 기본 포트 | 설명 |
|--------|-----------|------|
| **API Gateway** | 54321 | REST/GraphQL 엔드포인트 |
| **PostgreSQL** | 54322 | 로컬 DB |
| **Studio** | 54323 | 브라우저 기반 DB 관리 GUI |
| **Mailpit** | 54324 | 이메일 테스트 서버 |

CLI 전용 기능 요약:

| 기능 | 명령어 | 설명 |
|------|--------|------|
| 로컬 전체 스택 | `supabase start` | Docker 기반 전체 구동 |
| 스키마 차이 감지 | `supabase db diff` | 로컬/원격 간 차이 자동 감지 |
| pgTAP 테스트 | `supabase test db` | DB 단위 테스트 |
| 마이그레이션 압축 | `supabase migration squash` | 여러 마이그레이션을 하나로 |
| 성능 분석 | `supabase inspect db` | ==13개 서브커맨드== (bloat, locks, outliers 등) |
| Edge Function 로컬 실행 | `supabase functions serve` | 로컬에서 함수 개발/테스트 |
| CI/CD 통합 | `supabase db push` | GitHub Actions 등에서 자동 배포 |

### MCP만 할 수 있는 것

| 기능 | 설명 |
|------|------|
| ==AI가 SQL 자동 작성== | LLM이 스키마를 읽고 SQL 생성 후 apply_migration까지 자동 |
| `get_advisors` | 보안/성능 어드바이저 |
| `get_logs` | API/DB/Edge Functions/Auth 로그 통합 조회 |
| `search_docs` | Supabase 공식 문서 검색 (할루시네이션 감소) |
| `read_only` 모드 | URL 파라미터로 쓰기 차단 |
| Claude Desktop 지원 | GUI 앱에서 직접 DB 관리 |

### 시나리오별 비교 — 어떤 게 더 좋을까?

#### 시나리오 1: 새 테이블 설계 → ==MCP 유리==

```
MCP: 자연어로 요청 → list_tables → SQL 자동 생성 → apply_migration → RLS까지
     소요 시간: 약 30초

CLI: supabase migration new → SQL 직접 작성 → db reset 테스트 → db push
     소요 시간: 약 5분
```

#### 시나리오 2: 로컬 개발 환경 → ==CLI만 가능==

```
MCP: 불가능 (로컬 스택 구동 불가)

CLI: supabase init → supabase start → Docker 전체 스택 구동
     소요 시간: 약 2분
```

#### 시나리오 3: 보안 점검 → ==MCP 유리==

```
MCP: "보안 점검해줘" → get_advisors → execute_sql → 수정 SQL → apply_migration
     → 전체 과정이 하나의 대화에서 자동 처리

CLI: supabase db lint (Postgres 린트만) → 수동 분석 → 직접 SQL 작성
     → 보안 어드바이저 기능 없음
```

#### 시나리오 4: 프로덕션 배포 → ==CLI 유리==

```
MCP: 대화형이라 CI/CD 통합 어려움

CLI: GitHub Actions에서 supabase db push로 자동 배포 가능
```

### 추천 조합 워크플로우

갓대희님은 ==MCP와 CLI를 같이 쓸 때가 제일 편하다고== 합니다.

**조합 1: MCP로 설계 → CLI로 타입 생성**

```
1. MCP list_tables로 기존 스키마 확인
2. 자연어로 테이블 설계 요청 → MCP apply_migration
3. CLI: supabase gen types --lang typescript > src/types/supabase.ts
```

**조합 2: CLI로 로컬 개발 → MCP로 원격 점검**

```
1. CLI: supabase start → 로컬 스택 구동
2. CLI: 로컬에서 개발 & 마이그레이션 테스트
3. MCP: get_advisors → 원격 DB 보안/성능 점검
4. MCP: get_logs → 배포 후 에러 로그 확인
```

**조합 3: MCP로 데이터 분석 → CLI로 자동화**

```
1. MCP: execute_sql로 데이터 탐색
2. MCP: apply_migration으로 필요한 인덱스 추가
3. CLI: supabase db diff → 변경사항 확인
4. CLI: supabase db push → 원격 적용
```

> [!success] 갓대희님의 최종 결론
> **"CLI로 `supabase start` → 로컬 개발 → MCP로 원격 DB 스키마 설계/점검 → CLI로 `db push` 배포"**
>
> MCP는 ==탐색·설계·분석==에 쓰고, CLI는 ==로컬 테스트·빌드·배포==에 쓰면 됩니다. ==둘 다 쓰는 게 맞습니다.==

> [!warning] CLI 사용 시 자주 겪는 문제들
> - `supabase login`이 ==non-TTY 환경에서 실패== → 별도 터미널에서 실행
> - `supabase inspect db`는 ==linked 프로젝트에서만 동작== → 먼저 `supabase link`
> - `table-sizes`는 deprecated → ==`table-stats` 사용==
> - macOS에서 `psql` 미설치 → `brew install libpq` 후 PATH 추가

---

## 전체 요약 — 한눈에 보기

| 주제 | 핵심 도구 | 한줄 포인트 |
|------|-----------|------------|
| **로컬 LLM** | Ollama | 내 PC에서 ChatGPT급 AI 무료로 돌리기. 설치 쉽고 API도 제공 |
| **Agent Skills** | SKILL.md | 한 번 만들면 32개+ AI 에이전트에서 재사용. 5분이면 만든다 |
| **브라우저 자동화** | Playwright MCP | 자연어로 브라우저 조종. 접근성 트리 기반으로 빠르고 정확 |
| **브라우저 심층비교** | Playwright CLI | CLI가 기능 상위호환이지만 Vision 모드는 MCP만. Skills+CLI 조합이 최강 |
| **디자인→코드** | Figma MCP | 디자인 메타데이터로 픽셀퍼펙트 코드 생성. 양방향(Code↔Figma) 가능 |
| **DB 관리** | Supabase MCP | 자연어로 스키마 설계 & SQL 실행. DDL/DML 분리로 안전 |
| **DB 심층비교** | Supabase CLI | 로컬 전체 스택 + CI/CD 배포. MCP와 상호보완이 정답 |

> [!quote] 출처
> 모든 내용은 [갓대희의 작은공간](https://goddaehee.tistory.com) 블로그에서 발췌하여 정리했습니다.
> - [Ollama 설치 및 기초 사용방법 (feat 로컬 LLM 환경 구축해보기)](https://goddaehee.tistory.com/381)
> - [Agent Skill 오픈 표준 — SKILL.md 하나로 모든 AI 에이전트에서 쓰는 방법](https://goddaehee.tistory.com/553)
> - [Supabase CLI와 MCP 비교 분석 해보기](https://goddaehee.tistory.com/551)
> - [Supabase MCP 설치 및 사용방법 — 자연어로 PostgreSQL을 다루는 법](https://goddaehee.tistory.com/549)
> - [Figma MCP 설치 및 사용방법 — 자연어로 Figma를 조작하는 법](https://goddaehee.tistory.com/545)
> - [Playwright CLI와 MCP 비교 분석 해보기](https://goddaehee.tistory.com/539)
> - [Playwright MCP 설치 및 사용방법 — 자연어로 브라우저를 조종한다](https://goddaehee.tistory.com/538)