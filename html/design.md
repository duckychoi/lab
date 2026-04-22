# Fix Log HTML — Design & Style Guide

다른 coding agent가 동일한 스타일의 fix log / 기술 문서 HTML을 작성할 수 있도록 정리한 가이드.

---

## 1. 문서의 목적과 철학

이 HTML 포맷은 **"debugging 과정을 다른 사람(또는 에이전트)이 재현할 수 있게"** 기록하는 것이 목적이다.

핵심 원칙:
- **원인 → 증거 → 수정 → 검증** 순서를 지킨다. 결론만 쓰지 않는다.
- 코드 diff, 로그 출력, 명령어는 **그대로 붙여넣는다**. 요약하지 않는다.
- 독자가 "왜?"를 묻기 전에 먼저 설명한다.
- 에이전트가 읽어도 따라 할 수 있을 만큼 구체적으로 쓴다.

---

## 2. 전체 문서 구조

```
container (max-width: 860px)
├── page-nav          ← 여러 페이지가 있을 때 상단 탭 버튼
├── page#p1           ← 첫 번째 페이지
│   ├── header        ← badge + h1 + 부제
│   ├── timeline      ← 수정 단계들 (accordion)
│   │   └── step × N  ← 각 단계 카드
│   ├── result-banner ← 하단 핵심 요약
│   └── guide-section ← 에이전트용 상세 재현 가이드 (선택)
└── page#p2           ← 두 번째 페이지 (독립 주제)
    ├── header
    ├── timeline
    └── result-banner
```

페이지가 하나면 `page-nav`와 `page` 래퍼는 생략하고 바로 `header → timeline → result-banner`를 쓴다.

---

## 3. 색상 시스템 (CSS 변수)

```css
:root {
  --bg:       #0f0f13;   /* 최하단 배경 */
  --surface:  #1a1a24;   /* 카드 배경 */
  --surface2: #22222f;   /* 내부 중첩 배경 */
  --border:   #2e2e42;   /* 기본 테두리 */
  --accent:   #7c6af7;   /* 주요 강조색 (보라) */
  --accent2:  #4fc3f7;   /* 보조 강조색 (하늘) */
  --accent3:  #81c784;   /* 성공/OK (초록) */
  --warn:     #ffb74d;   /* 경고 (주황) */
  --danger:   #ef5350;   /* 오류/문제 (빨강) */
  --text:     #e0e0f0;   /* 본문 텍스트 */
  --text-dim: #8888aa;   /* 보조 텍스트 */
  --code-bg:  #12121a;   /* 코드 블록 배경 */
}
```

**색상 사용 규칙:**
- 문제/오류 설명 → `--danger` (#ef5350) 계열
- 수정/해결/OK → `--accent3` (#81c784) 계열
- 근거/이유 설명 → `--accent2` (#4fc3f7) 계열
- 핵심 강조 → `--accent` (#7c6af7)
- 경고/주의 → `--warn` (#ffb74d)

---

## 4. 컴포넌트별 HTML 패턴

### 4-1. Header

```html
<header>
  <div class="badge">Fix Log · 2026-04-10</div>
  <h1>문서 제목</h1>
  <p>한 줄 부제 — <code style="color:var(--accent2)">명령어</code> 포함 가능</p>
</header>
```

- `badge`: 날짜, 문서 유형, 버전 등 메타 정보. 그라디언트 pill.
- `h1`: 그라디언트 텍스트 (`#c4b5fd → --accent2`).
- `p`: `--text-dim` 색상의 짧은 설명.

---

### 4-2. Timeline + Step (accordion)

타임라인은 **왼쪽 세로선 + 번호 dot + 클릭 시 펼쳐지는 카드** 구조.

```html
<div class="timeline">
  <div class="step" onclick="toggle(this)">
    <div class="step-dot">1</div>          <!-- 또는 class="blue/green/orange" -->
    <div class="step-card">

      <!-- 항상 보이는 헤더 -->
      <div class="step-header">
        <div>
          <div class="step-title">단계 제목 — 핵심을 한 줄로</div>
          <div class="chips">
            <span class="chip purple">태그1</span>
            <span class="chip blue">태그2</span>
          </div>
        </div>
        <div style="display:flex;align-items:center;gap:.5rem">
          <span class="step-file">path/to/file</span>  <!-- 선택 -->
          <span class="chevron">▼</span>
        </div>
      </div>

      <!-- 클릭 시 펼쳐지는 본문 -->
      <div class="step-body">
        <!-- 박스들 조합 -->
      </div>

    </div>
  </div>
</div>
```

**step-dot 색상:**
| class | 색 | 용도 |
|---|---|---|
| (없음) | `--accent` 보라 | 일반 단계 |
| `blue` | `--accent2` 하늘 | 진단/확인 단계 |
| `green` | `--accent3` 초록 | 수정/완료 단계 |
| `orange` | `--warn` 주황 | 분석/주의 단계 |

**chip 색상:**
```html
<span class="chip purple">핵심 수정</span>
<span class="chip blue">진단</span>
<span class="chip green">완료</span>
```

---

### 4-3. 본문 박스 3종

step-body 안에서 **문제 → 수정 → 이유** 순서로 배치한다.

```html
<!-- 문제 설명 (빨강 왼쪽 border) -->
<div class="problem-box">
  <div class="label">문제</div>
  구체적인 증상. <strong>강조</strong>와 <code>명령어</code> 포함.
</div>

<!-- 수정/결과 설명 (초록 왼쪽 border) -->
<div class="fix-box">
  <div class="label">효과</div>
  수정 후 어떻게 달라지는지.
</div>

<!-- 이유/원리 설명 (하늘 왼쪽 border) -->
<div class="reason-box">
  <div class="label">왜?</div>
  내부 동작 원리, 로드 순서, 메커니즘.
</div>
```

추가로 `warn-box` (주황)와 `info-box` (보라)도 있다:

```html
<div class="warn-box">주의사항 — 부작용 가능성 등</div>
<div class="info-box">참고 정보 — 배경 지식, 설계 이유</div>
```

---

### 4-4. Diff 블록

실제 파일 변경 내용을 표시할 때.

```html
<div class="diff">
  <div class="diff-header">파일명 또는 설명</div>
  <div class="diff-line ctx"> 변경 없는 컨텍스트 줄</div>
  <div class="diff-line removed">-  삭제된 줄</div>
  <div class="diff-line added">+  추가된 줄</div>
</div>
```

- `ctx`: 회색. 변경 전후 맥락.
- `removed`: 빨간 배경. `-` 로 시작.
- `added`: 초록 배경. `+` 로 시작.

---

### 4-5. Code 블록 (copy 버튼 포함)

```html
<div class="code-block">
  <button class="copy-btn" onclick="copyCode(this)">copy</button>
  <span class="comment"># 주석</span>
  <span class="key">VARIABLE_NAME</span>=<span class="val">value</span>
  <span class="str">"문자열"</span>
  <span class="hl">강조할 줄</span>
  일반 텍스트
</div>
```

**span 클래스:**
| class | 색 | 용도 |
|---|---|---|
| `.comment` | `#555577` 어두운 회색 | `#` 주석 |
| `.key` | `#c4b5fd` 연보라 | 변수명, JSON 키 |
| `.val` | `#a5d6a7` 연초록 | 값, boolean |
| `.str` | `#80cbc4` 청록 | 문자열 |
| `.hl` | `#ffcc80` 연주황 | 강조할 명령/값 |

`white-space: pre`이므로 들여쓰기를 그대로 보존한다. copy 버튼 클릭 시 `copy → copied!` 로 1.5초간 바뀐다.

---

### 4-6. Flow Diagram

원인 체인, 데이터 흐름, before/after를 텍스트로 표현할 때.

```html
<div class="flow">
<span class="fl-dim"># 주석/설명</span>
<span class="fl-key">변수명</span> <span class="fl-arrow">=</span> <span class="fl-bad">잘못된 값</span>
<span class="fl-arrow">↓</span> 다음 단계
<span class="fl-good">올바른 결과</span>
</div>
```

**span 클래스:**
| class | 색 | 용도 |
|---|---|---|
| `.fl-bad` | `#ef9a9a` 연빨강 | 잘못된 값, 오류 경로 |
| `.fl-good` | `#a5d6a7` 연초록 | 올바른 값, 성공 경로 |
| `.fl-dim` | `--text-dim` | 주석, 보조 설명 |
| `.fl-key` | `#ffcc80` 연주황 | 변수명, 키워드 |
| `.fl-arrow` | `#7c6af7` 보라 | `→`, `↓`, `=` |

`line-height: 2`로 여유 있게 배치한다.

---

### 4-7. Diag Grid (2열 비교)

정상 vs 비정상, Before vs After를 나란히 비교할 때.

```html
<div class="diag-grid">
  <div class="diag-card">
    <div class="diag-label" style="color:var(--danger)">비정상</div>
    <code>명령어 출력</code>
    <code>또 다른 줄</code>
    <div class="diag-note">설명</div>
  </div>
  <div class="diag-card">
    <div class="diag-label" style="color:var(--accent3)">정상</div>
    <code>기대 출력</code>
    <div class="diag-note">설명</div>
  </div>
</div>
```

---

### 4-8. Shell Flow (인라인 흐름 표시)

짧은 단계 흐름을 한 줄로 표현할 때.

```html
<div class="shell-flow">
  <span class="shell-node accent">--login 플래그</span>
  <span class="shell-arrow">→</span>
  <span class="shell-node">/etc/profile</span>
  <span class="shell-arrow">→</span>
  <span class="shell-node green">~/.bashrc 로드</span>
</div>
```

---

### 4-9. Result Banner (하단 요약)

각 페이지 맨 아래. 핵심 원인과 해결책을 한 단락으로.

```html
<div class="result-banner">
  <div class="result-icon">⚡</div>   <!-- 또는 🔑 🛠 🔍 등 -->
  <div class="result-text">
    <h3>핵심 요약</h3>
    <p>원인과 해결책을 2-3문장으로. <code>기술 용어</code>는 코드 태그 사용.</p>
  </div>
</div>
```

---

### 4-10. Page Nav (다중 페이지)

독립된 주제를 별도 페이지로 분리할 때. 상단 고정.

```html
<nav class="page-nav">
  <button class="page-btn active" onclick="showPage('p1', this)">① 첫 번째 주제</button>
  <button class="page-btn" onclick="showPage('p2', this)">② 두 번째 주제</button>
</nav>

<div class="page active" id="p1"> ... </div>
<div class="page" id="p2"> ... </div>
```

---

### 4-11. Guide Section (에이전트용 재현 가이드)

1페이지 하단에 추가하는 선택적 섹션. 다른 에이전트가 동일 문제를 만났을 때 따라 할 수 있도록.

```html
<div class="guide-section">
  <div class="section-title">Agent Reproduction Guide</div>
  <div class="section-sub">한 줄 설명</div>

  <div class="guide-card">
    <h3><span class="num">0</span> 단계 제목</h3>
    <p>설명</p>
    <!-- tab-bar, code-block, checklist, diag-grid 등 조합 -->
  </div>
</div>
```

guide-card 내부 `num` 색상:
- 기본 숫자 → `var(--accent)` 보라
- `class="blue"` → `var(--accent2)` 하늘
- `class="green"` → `var(--accent3)` 초록
- `class="orange"` → `var(--warn)` 주황

---

## 5. JavaScript (3개 함수)

```js
// 페이지 전환
function showPage(id, btn) {
  document.querySelectorAll('.page').forEach(p => p.classList.remove('active'));
  document.querySelectorAll('.page-btn').forEach(b => b.classList.remove('active'));
  document.getElementById(id).classList.add('active');
  btn.classList.add('active');
  window.scrollTo({ top: 0, behavior: 'smooth' });
}

// step accordion
function toggle(stepEl) {
  const body = stepEl.querySelector('.step-body');
  const isOpen = body.classList.contains('open');
  document.querySelectorAll('.step-body.open').forEach(b => {
    b.classList.remove('open');
    b.closest('.step').classList.remove('open');
  });
  if (!isOpen) {
    body.classList.add('open');
    stepEl.classList.add('open');
  }
}

// copy 버튼
function copyCode(btn) {
  const block = btn.closest('.code-block');
  const text = block.innerText.replace(/^copy\n/, '').trim();
  navigator.clipboard.writeText(text).then(() => {
    const orig = btn.textContent;
    btn.textContent = 'copied!';
    setTimeout(() => btn.textContent = orig, 1500);
  });
}
```

---

## 6. 설명 스타일 가이드

### 단계 제목 작성법

```
좋음: "Shell 교체 — sh → bash + login 플래그"
좋음: "원인 분석 — Snap 격리로 인한 XDG 경로 오염"
나쁨: "문제 해결"
나쁨: "수정 완료"
```

형식: `[동작/분류] — [구체적 내용]`
대시(`—`) 앞뒤는 공백. 파일명, 명령어, 경로는 구체적으로.

### problem-box 작성법

```
좋음: "기본 프로파일이 /bin/sh에 args 없음 → sh는 .bashrc를 로드하지 않아
       PATH가 불완전. opencode·claude 명령 미인식."

나쁨: "명령어가 안 됩니다."
```

- `→` 로 원인-결과를 연결한다.
- 구체적인 파일명, 변수명, 오류 메시지를 포함한다.
- `<code>` 태그로 기술 용어를 마킹한다.

### fix-box / reason-box 작성법

fix-box = "수정 후 어떻게 동작하는가"
reason-box = "왜 그 수정이 효과가 있는가"

두 개를 항상 세트로 쓴다. reason 없이 fix만 쓰면 에이전트가 변형 상황에 적용 못한다.

### flow diagram 작성법

```
원인 A
  ↓ 결과 1
  ↓ 결과 2 (나쁜 값은 fl-bad, 좋은 값은 fl-good)
  ↓ 최종 증상

──────── (구분선)
수정 후
  ↓ 달라지는 지점
  ↓ 올바른 결과
```

before/after를 한 다이어그램 안에 `──────` 구분선으로 함께 넣는다.

### checklist 작성법

```html
<ul class="checklist">
  <li>구체적인 확인 항목. <code>실행할 명령</code> 포함.</li>
  <li>조건이 있으면 조건도 명시. 없으면 생략.</li>
</ul>
```

추상적인 항목 금지. 에이전트가 그대로 실행할 수 있어야 한다.

---

## 7. 페이지 구성 판단 기준

| 상황 | 구성 |
|---|---|
| 단일 문제, 수정 3개 이하 | 페이지 1개, timeline만 |
| 단일 문제, 수정 많음 | 페이지 1개 + guide-section |
| 독립된 두 문제 | 페이지 2개 (page-nav) |
| 에이전트가 재현해야 함 | guide-section 필수 추가 |

guide-section 내부 카드 순서:
1. 문제 상황 파악 (언제 이 가이드가 필요한가)
2. 사전 확인 (Step 0)
3. 수정 단계들 (Step 1, 2, ...)
4. 검증 체크리스트
5. 트러블슈팅 FAQ

---

## 8. 완성 체크리스트

문서를 작성한 후 아래를 확인한다.

- [ ] 모든 step에 problem-box가 있는가 (왜 이 수정이 필요한지 설명)
- [ ] diff 블록이 실제 변경 내용과 일치하는가
- [ ] code-block에 copy 버튼이 달려 있는가
- [ ] flow diagram에서 bad/good 색상이 의미에 맞게 사용됐는가
- [ ] result-banner가 각 페이지 하단에 있는가
- [ ] guide-section의 코드 블록은 복사해서 바로 실행 가능한가
- [ ] 트러블슈팅 FAQ에 "수정 후에도 안 될 때" 항목이 있는가
