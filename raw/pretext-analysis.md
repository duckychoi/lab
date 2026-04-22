---
title: "Pretext — Multiline Text Measurement & Layout Library"
type: raw-source
tags:
  - library
  - javascript
  - typescript
  - text-layout
  - typography
  - canvas
  - unicode
  - frontend
  - performance
source_path: /home/ducky/Useful_tools/pretext/
ingested: 2026-04-18
---

# Pretext

**순수 JavaScript/TypeScript 멀티라인 텍스트 측정 및 레이아웃 라이브러리.**
빠르고, 정확하며, 모든 언어를 지원. DOM, Canvas, SVG 렌더링 지원.

> "Pretext side-steps the need for DOM measurements (e.g. getBoundingClientRect, offsetHeight), which trigger layout reflow, one of the most expensive operations in the browser."

---

## 기본 정보

| 항목 | 내용 |
|---|---|
| **패키지명** | `@chenglou/pretext` |
| **버전** | 0.0.5 (2026-04-09) |
| **저자** | chenglou (Sebastian Markbage의 text-layout에서 영감) |
| **라이선스** | MIT |
| **저장소** | https://github.com/chenglou/pretext |
| **데모** | https://chenglou.me/pretext/ |
| **런타임** | Bun (개발), 브라우저 + 서버 (사용) |
| **언어** | TypeScript (ESM) |

---

## 핵심 가치

### 문제: DOM 리플로우 비용
브라우저에서 텍스트 높이를 알려면 `getBoundingClientRect()` 등의 DOM 측정이 필요.
이는 **layout reflow**를 유발 — 브라우저에서 가장 비싼 연산 중 하나.

### 해결: DOM 없는 텍스트 측정
Pretext는 자체 텍스트 측정 로직을 구현:
- 브라우저의 폰트 엔진을 ground truth로 사용
- Canvas `measureText`로 세그먼트 폭 측정
- `Intl.Segmenter`로 단어/그래핌 분할
- ==DOM 조작 없이== 순수 연산으로 멀티라인 텍스트 높이 계산

### 지원 언어
- 라틴 계열, CJK (중국어/일본어/한국어), 아랍어, 히브리어
- 태국어, 라오어, 크메르어, 미얀마어 (동남아시아어)
- 이모지, 유니코드 확장 영역
- RTL (Right-to-Left) 텍스트 + Bidirectional

---

## 두 가지 사용 케이스

### 케이스 1: DOM 없이 단락 높이 측정

```ts
import { prepare, layout } from '@chenglou/pretext'

const prepared = prepare('AGI 春天到了. بدأت الرحلة 🚀', '16px Inter')
const { height, lineCount } = layout(prepared, textWidth, 20)
```

- `prepare()`: 1회성 — 텍스트 정규화, 세그먼트 분할, 글루 규칙 적용, canvas 폭 측정
- `layout()`: 핫 패스 — 순수 산술. ==리사이즈 시마다 `layout()`만 재실행==

**활용:**
- 가상 스크롤/오클루전 — 높이 예측으로 정확한 가상화
- 메이슨리 레이아웃, JS 기반 flexbox
- 버튼/라벨 오버플로우 검증 (CI/AI 친화적)
- 텍스트 로드 시 레이아웃 시프트 방지

### 케이스 2: 수동 라인 레이아웃 (Canvas/SVG/WebGL 렌더링)

```ts
import { prepareWithSegments, layoutWithLines } from '@chenglou/pretext'

const prepared = prepareWithSegments('AGI 春天到了. 🚀', '18px "Helvetica Neue"')
const { lines } = layoutWithLines(prepared, 320, 26)
for (let i = 0; i < lines.length; i++) ctx.fillText(lines[i].text, 0, i * 26)
```

**하위 API:**
- `layoutWithLines()` — 고정 폭에서 모든 라인 정보 반환
- `measureLineStats()` / `walkLineRanges()` — 문자열 생성 없이 라인 수/폭만 계산
- `layoutNextLineRange()` — 가변 폭 레이아웃 (이미지 주변 텍스트 흐름 등)
- `materializeLineRange()` — range → 실제 텍스트 문자열 변환

---

## Rich Inline 텍스트 헬퍼

`@chenglou/pretext/rich-inline` — 인라인 전용 리치 텍스트 흐름 헬퍼:

```ts
import { prepareRichInline, walkRichInlineLineRanges } from '@chenglou/pretext/rich-inline'

const prepared = prepareRichInline([
  { text: 'Ship ', font: '500 17px Inter' },
  { text: '@maya', font: '700 12px Inter', break: 'never', extraWidth: 22 },
  { text: "'s rich-note", font: '500 17px Inter' },
])

walkRichInlineLineRanges(prepared, 320, range => {
  // 각 프래그먼트의 itemIndex, text slice, gapBefore, cursors 포함
})
```

**지원:**
- 여러 폰트가 혼합된 인라인 텍스트
- `break: 'never'` — 멘션/칩 등 원자 단위 항목
- `extraWidth` — 패딩/보더 등 호출자 소유 폭
- 브라우저 같은 바운더리 공백 축소

---

## 아키텍처

### 핵심 소스 파일

| 파일 | 역할 |
|---|---|
| `src/layout.ts` | 코어 라이브러리 — `layout()` 빠르고 할당 가볍게 유지 |
| `src/analysis.ts` | 정규화, 세그먼테이션, 글루 규칙 — `prepare()`의 텍스트 분석 단계 |
| `src/measurement.ts` | Canvas 측정, 세그먼트 메트릭스 캐시, 이모지 보정 |
| `src/line-break.ts` | 라인 워킹 코어 — 리치 API와 핫 패스 라인 카운터 공유 |
| `src/bidi.ts` | Bidirectional 텍스트 메타데이터 헬퍼 |
| `src/rich-inline.ts` | 리치 인라인 전용 헬퍼 |

### 내부 세그먼트 모델

8가지 이상의 브레이크 종류 구분:
1. 일반 텍스트
2. 축소 가능 공백 (collapsible spaces)
3. 보존 공백 (preserved spaces)
4. 탭
5. 비축소 글루 (NBSP / NNBSP / WJ)
6. 제로폭 브레이크 기회 (ZWSP)
7. 소프트 하이픈
8. 하드 브레이크

### 캐시 구조

```
Map<font, Map<segment, metrics>>
```
- 텍스트 전체 공유, `clearCache()`로 초기화 가능
- 폭은 현재 하나의 캐시된 팩트; 그래핌 폭 등은 지연 로딩

---

## 지원 CSS 동작

| CSS 속성 | 지원 |
|---|---|
| `white-space: normal` | 기본 |
| `white-space: pre-wrap` | `{ whiteSpace: 'pre-wrap' }` 옵션 |
| `word-break: normal` | 기본 |
| `word-break: keep-all` | `{ wordBreak: 'keep-all' }` 옵션 (CJK/한글) |
| `overflow-wrap: break-word` | 좁은 폭에서 그래핌 경계 단위로 단어 내 브레이크 |
| `line-break: auto` | 지원 |
| `tab-size: 8` | 기본 브라우저 스타일 |

**미지원:** `break-all`, `strict`, `loose`, `anywhere`

---

## 정확도 검증 시스템

### 브라우저 정확도 스냅샷
- `accuracy/chrome.json` / `safari.json` / `firefox.json`
- 4 폰트 × 8 사이즈 × 8 폭 × 30 텍스트 = **7,680** 케이스 per 브라우저
- 라인 핏 허용오차: Chromium/Gecko = `0.005`, Safari/WebKit = `1/64`

### 장문 코퍼스 테스트
- `corpora/chrome-step10.json` / `safari-step10.json`
- 스텝 10 폭 스윕으로 다국어 장문 테스트
- 태국어, 크메르어, 라오어, 미얀마어, 아랍어, 일본어, 중국어 등

### 벤치마크
- `benchmarks/chrome.json` / `safari.json`
- Chrome이 메인 퍼포먼스 베이스라인

---

## 데모

| 데모 | 설명 |
|---|---|
| `pages/demos/bubbles.ts` | 버블 shrinkwrap — 비구체화 라인 레인지 워커 사용 |
| `pages/demos/dynamic-layout.ts` | 2단 편집 레이아웃 — 장애물 인식 타이틀 라우팅, 라이브 리플로우 |
| `pages/demos/markdown-chat.ts` | 리치 채팅 가상화 — 준비된 템플릿 + 수동 블록 레이아웃 스트레스 테스트 |
| `pages/demos/rich-note.ts` | 인라인 리치 노트 — rich-inline 헬퍼 도그푸딩 |

---

## 개발 명령어

```bash
bun install                  # 의존성 설치
bun start                    # 개발 서버 (localhost:3000)
bun run check                # 타입체크 + 린트
bun run accuracy-check       # 브라우저 정확도 검증
bun run corpus-check         # 코퍼스 테스트
bun run benchmark-check      # 퍼포먼스 벤치마크
bun run build:package        # dist/ 빌드
```

---

## 버전 히스토리 요약

| 버전 | 날짜 | 주요 변경 |
|---|---|---|
| 0.0.0 | 2026-03-26 | 최초 공개 — `prepare()`, `layout()`, 리치 API |
| 0.0.1 | 2026-03-27 | Safari 라인 브레이킹 개선 |
| 0.0.2 | 2026-03-28 | `pre-wrap` 모드 추가 |
| 0.0.3 | 2026-03-29 | npm ESM 빌드 배포 |
| 0.0.4 | 2026-04-02 | 정렬 비교 데모, 상태 대시보드 |
| 0.0.5 | 2026-04-09 | 리치 라인 헬퍼, `keep-all`, rich-inline 모듈, 마크다운 채팅 데모 |

---

## 실용 활용 시나리오

1. **가상 스크롤**: 리스트의 각 아이템 높이를 DOM 없이 예측 → 부드러운 무한 스크롤
2. **채팅/메시지 앱**: 메시지 버블 높이 미리 계산 → 레이아웃 시프트 제로
3. **캔버스 기반 에디터**: Figma/Excalidraw 같은 툴에서 텍스트 레이아웃
4. **이미지 주변 텍스트 흐름**: `layoutNextLineRange()`로 가변 폭 대응
5. **CI/AI 테스트**: 브라우저 없이 UI 텍스트 오버플로우 자동 검증
6. **SVG/WebGL 렌더링**: DOM이 없는 환경에서도 정확한 텍스트 레이아웃

---

## 주의사항

- `system-ui` 폰트는 macOS에서 canvas와 DOM이 다른 폰트를 로드할 수 있어 ==정확도 불안정==
- 전체 CSS 텍스트 엔진이 아님 — 일반적인 앱 텍스트 설정 타겟
- 라인 핏 허용오차는 브라우저별로 다름
- 아랍어 fine-width 영역에서 미세한 정확도 차이 존재
