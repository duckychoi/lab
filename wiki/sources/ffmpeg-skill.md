---
title: "kajisho5/ffmpeg-skill — 코딩 에이전트용 로컬 FFmpeg 영상 편집 스킬 (42개 도구 · MCP)"
type: source
domain: video-saas
tags: [video-saas, github-trending, ffmpeg, agent-skill, mcp, 영상자동화]
created: 2026-11-16
updated: 2026-11-16
sources: [https://github.com/kajisho5/ffmpeg-skill]
reliability: medium
---

**레포**: [kajisho5/ffmpeg-skill](https://github.com/kajisho5/ffmpeg-skill) · ★**6,093**(볼트 11-16 실측) · fork 539 · Python · MIT · repo id 1356077516 · 생성 2026-09-03. API description: *"Local video editor for coding agents: 42 FFmpeg tools with a machine-readable c…"*.

## 핵심 인사이트
> [!insight] probe → 무손실 우선 편집 → 재probe 검증 — 에이전트가 영상을 "보지 않고" 망치는 길을 막는다
> 모든 작업은 `probe.py` 실측(fps · 해상도 · 색 · 오디오 레이아웃)에서 시작, **셸 문자열 · 호출자 필터그래프를 받지 않는** 타입 지정 스크립트, 실행 후 재probe 해 목적지 규격과 대조, 화면이 바뀌면 컨택트 시트로 확인. 모든 도구에 `--dry-run` · `--plan FILE`(README 199행). MCP `input_schema` 는 CLI `argparse` 에서 런타임 파생 — 어긋나면 CI 실패 → [[스키마-준수-보장]].

> [!note] 자기 채점 — 정직성 신호
> 저자 본인의 포지션 페이퍼(Zenodo)가 *"scores ffmpeg-skill itself as only partially conformant"*(README 97행 · 볼트 확인) → [[자기제한-명시]].

## 도메인별 추출 (video-saas)
- **기능 벤치마킹**: 컷 · 카라오케 자막 · 9:16 리프레임 · 무음 제거 · 라우드니스(−14 LUFS) · 플랫폼 내보내기 — 쇼츠 후처리 체인과 거의 1:1. Python 표준 라이브러리만 · 클라우드 · 키 불필요, Parakeet/whisper 있으면 전사(수집기).
- **워크플로**: [[Remotion]] 렌더 출력 → ffmpeg-skill 로 리프레임 · 라우드니스 정규화 · 플랫폼 규격 검증.
- **경쟁 우위 빈틈**: "결과 재probe 후 규격 대조"는 볼트 영상 파이프라인에 없는 단계.
- **액션**: 설치 시험 1회(actionable).

## 관련 페이지
- [[에이전트-스킬]] · [[스키마-준수-보장]] · [[자기제한-명시]] · [[Remotion]] · [[SkillEvaluator]] · [[AI-영상-생성-2026]]

## 원본
- 출처: https://github.com/kajisho5/ffmpeg-skill
- 확인 범위: GitHub API 메타 · README 97 · 199행(볼트) · 🔴 도구 목록 · 의존성 서술은 수집기 판독 · 실행 미확인
- 신뢰도: ⭐⭐⭐ (★6,093 · 로컬 전용 · 측정 0)
