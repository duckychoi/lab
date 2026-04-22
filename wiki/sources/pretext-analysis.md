---
title: "Pretext — Text Measurement & Layout Library"
type: source
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
created: 2026-04-18
updated: 2026-04-18
source_path: /home/ducky/Useful_tools/pretext/
author: chenglou
cssclasses:
  - wide-page
---

# Pretext — Text Measurement & Layout Library

> [!abstract] Source Summary
> 순수 JS/TS 멀티라인 텍스트 측정/레이아웃 라이브러리.
> ==DOM 리플로우 없이== 텍스트 높이를 예측하고, Canvas/SVG/WebGL로 수동 렌더링 지원.

| Field | Value |
|---|---|
| **Package** | `@chenglou/pretext` |
| **Version** | 0.0.5 |
| **Author** | chenglou |
| **License** | MIT |
| **Repo** | https://github.com/chenglou/pretext |
| **Demo** | https://chenglou.me/pretext/ |
| **Ingested** | 2026-04-18 |

---

## Core Problem & Solution

> [!insight] Why Pretext?
> 브라우저에서 `getBoundingClientRect()`로 텍스트 높이를 측정하면 **layout reflow** 발생.
> 이것은 브라우저에서 가장 비싼 연산 중 하나.
>
> Pretext는 ==DOM 조작 없이== 순수 산술로 멀티라인 높이를 계산.

### How
- Canvas `measureText` → 세그먼트 폭 측정
- `Intl.Segmenter` → 단어/그래핌 분할
- 자체 텍스트 측정 로직 (브라우저 폰트 엔진을 ground truth로)

---

## Two Use Cases

### 1. Height Prediction (No DOM)

```ts
import { prepare, layout } from '@chenglou/pretext'
const prepared = prepare('AGI 春天到了. 🚀', '16px Inter')
const { height, lineCount } = layout(prepared, textWidth, 20)
```

- `prepare()` — 1회성 전처리 (리사이즈 시 재실행 불필요)
- `layout()` — 핫 패스, 순수 산술

### 2. Manual Line Layout (Canvas/SVG/WebGL)

```ts
import { prepareWithSegments, layoutWithLines } from '@chenglou/pretext'
const { lines } = layoutWithLines(prepared, 320, 26)
```

하위 API: `walkLineRanges()`, `measureLineStats()`, `layoutNextLineRange()`, `materializeLineRange()`

---

## Rich Inline Helper

`@chenglou/pretext/rich-inline` — 혼합 폰트, 멘션/칩, 바운더리 공백 축소:

```ts
const prepared = prepareRichInline([
  { text: 'Ship ', font: '500 17px Inter' },
  { text: '@maya', font: '700 12px Inter', break: 'never', extraWidth: 22 },
])
```

---

## Architecture

| File | Role |
|---|---|
| `src/layout.ts` | Core — `layout()` fast & allocation-light |
| `src/analysis.ts` | Text analysis — normalization, segmentation, glue rules |
| `src/measurement.ts` | Canvas measurement, cache, emoji correction |
| `src/line-break.ts` | Line-walking core shared by rich APIs |
| `src/bidi.ts` | Bidirectional text metadata |
| `src/rich-inline.ts` | Rich inline text flow helper |

8가지 내부 세그먼트 타입: 일반 텍스트, 축소 공백, 보존 공백, 탭, NBSP 글루, ZWSP, 소프트 하이픈, 하드 브레이크.

---

## Supported Languages

라틴, CJK, 아랍어, 히브리어, 태국어, 라오어, 크메르어, 미얀마어, 이모지, 유니코드 확장.

---

## CSS Support

| CSS | Status |
|---|---|
| `white-space: normal` / `pre-wrap` | Supported |
| `word-break: normal` / `keep-all` | Supported |
| `overflow-wrap: break-word` | Supported |
| `break-all`, `strict`, `loose`, `anywhere` | Not supported |

---

## Practical Use Cases

1. **Virtual scrolling** — 리스트 아이템 높이 예측으로 부드러운 스크롤
2. **Chat apps** — 메시지 버블 높이 미리 계산, 레이아웃 시프트 제로
3. **Canvas editors** — Figma/Excalidraw 스타일 텍스트 레이아웃
4. **Image text flow** — `layoutNextLineRange()`로 가변 폭 대응
5. **CI/AI testing** — 브라우저 없이 UI 텍스트 오버플로우 자동 검증
6. **SVG/WebGL rendering** — DOM 없는 환경에서 정확한 텍스트 레이아웃

---

## Caveats

> [!warning]
> - `system-ui` 폰트는 macOS에서 정확도 불안정
> - 전체 CSS 텍스트 엔진이 아님 — 일반적인 앱 텍스트 타겟
> - 아랍어 fine-width 영역에서 미세 차이 존재

---

## Demos

| Demo | Description |
|---|---|
| `bubbles` | Shrinkwrap 버블 — 비구체화 라인 레인지 워커 |
| `dynamic-layout` | 2단 편집 레이아웃 + 장애물 인식 리플로우 |
| `markdown-chat` | 리치 채팅 가상화 스트레스 테스트 |
| `rich-note` | 인라인 리치 노트 — rich-inline 도그푸딩 |

---

## Version Timeline

| Version | Date | Key Change |
|---|---|---|
| 0.0.0 | 2026-03-26 | Initial release |
| 0.0.2 | 2026-03-28 | `pre-wrap` mode |
| 0.0.3 | 2026-03-29 | ESM npm publish |
| 0.0.5 | 2026-04-09 | Rich line helpers, `keep-all`, rich-inline |

---

## Related Pages

- [[domains/vibe-coding]] — AI 코딩 도구, 프론트엔드 라이브러리
