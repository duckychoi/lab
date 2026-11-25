---
title: "sam2 — 이미지 · 영상 프롬프트 분할 SAM 2/2.1 공식 코드"
type: source
domain: video-saas
tags: [video-saas, github, segmentation, video-tracking, sam2, meta, baseline-resurfacing]
created: 2026-11-25
updated: 2026-11-25
sources: [https://github.com/facebookresearch/sam2]
reliability: high
---

**레포**: facebookresearch/sam2 · ★ **20,217**(수집기 11-24) → **20,228**(볼트 API 11-25) · Jupyter 일간 Trending(당일 +5) · Apache-2.0 · 생성 2024-07-29 · push 2026-05-30 — [[기준선-재부상]] 사례

## 핵심 인사이트
> [!insight] 이미지를 1프레임 영상으로 취급한다 — SAM 2의 설계가 SAM 3 이전 표준인 이유
> 이미지를 1프레임 영상으로 보고 **스트리밍 메모리**를 둔 트랜스포머로 클릭 · 박스 · 마스크 프롬프트 기반 분할을 영상 전체로 추적. 2024-12 업데이트로 `vos_optimized=True` 시 전체 모델 torch.compile, 추적 중 새 객체 추가(객체별 독립 추론) 지원. [[sam3]] 의 이전 세대이며 **텍스트 프롬프트 분할이 필요하면 SAM 3 쪽** — 프롬프트 방식이 바뀌면서 같은 계열이 두 세대로 나뉜 지점이 이 페이지의 핵심 기록.

> [!note] SAM 2.1 공식 수치(README 표 · 열 귀속 확인, 수집기 11-24)
> tiny 38.9M · 91.2 FPS · SA-V test J&F **76.5** / small 46M · 84.8 FPS · 76.6 / base+ 80.8M · 64.1 FPS · 78.2 / large 224.4M · 39.5 FPS · **79.5** (MOSE val 71.8→74.6, LVOS v2 77.3→80.6). SAM 2→2.1에서 SA-V는 전 크기 +1.5–3.5 상승, 단 **large의 MOSE val은 74.6 그대로**, base+ LVOS v2는 75.8→78.2. 설치 시 nvcc로 CUDA 확장 빌드가 필요하나 실패해도 대부분 결과엔 영향 없다고 README가 명시.

## 도메인별 추출 (video-saas)
- **실용성**: 영상 객체 마스킹(배경 제거 · 리타깃) 파이프라인의 **검증된 기본값** — FPS 수치까지 공개되어 하드웨어 계획이 가능하다.
- **크리에이터 인사이트**: 자동 마스킹은 "검출 정확도"보다 "추적 일관성(객체 누락 · 아이덴티티 스위치)"이 실사용 품질을 결정 — SA-V J&F가 그 지표.
- **액션**: 없음(관찰 — [[sam3]] 보유로 충분).

## 관련 페이지
- [[sam3]] · [[Meta]] · [[기준선-재부상]] · [[video-saas]]

## 원본
- 출처: https://github.com/facebookresearch/sam2
- 확인 범위: README 표(수집기 11-24 — 열 귀속 확인) · GitHub API 재확인(볼트 11-25 — ★ · 라이선스 · 생성일 · push 일치) · 실행 0
- 신뢰도: ⭐⭐⭐ (★2만 · Meta 공식 · 표 수치는 README 기준)
