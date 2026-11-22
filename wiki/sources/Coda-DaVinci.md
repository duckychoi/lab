---
title: "Coda-DaVinci — 코드로 만든 3D 프록시가 영상 생성을 이끄는 Code2Video (KlingAI Research · 장편 전환 안정성 약점을 초록에 명시)"
type: source
domain: video-saas
tags: [video-saas, paper, code2video, 3d-proxy, multi-agent, kling, physics]
created: 2026-11-22
updated: 2026-11-22
sources: [https://huggingface.co/papers/2611.26595]
reliability: medium
---

**논문**: arXiv 2611.26595 · 업보트 35(볼트 · 수집기 일치) · HF 조직 `KlingTeam`(KlingAI Research) · 저자 23 · 코드 [FrankYang-17/Coda](https://github.com/FrankYang-17/Coda) ★24

## 핵심 인사이트
> [!insight] 프록시는 세밀할수록 좋은 것이 아니다 — 목적에 따라 세밀도를 고른다
> 에이전트가 코드로 3D 프록시(구조 · 동역학)를 만들고 이를 가이드로 영상을 생성하는 Code2Video 를 **블라인드 인간 평가**로 분석: 거친 프록시는 자연스러운 모션에, 중간 세밀도는 일관성에 유리하고, 물리 시뮬레이션과 프록시 정렬 프롬프트가 평균 품질을 올린다. 이를 바탕으로 작업별로 프록시 가이드/직접 생성을 고르고 개체별 모델링 세밀도를 조정하는 멀티에이전트 프레임워크(시각 검사 · 독립 리뷰로 수리).

## 도메인별 추출 (video-saas)
- **기능 벤치마킹**: "프롬프트 → 영상" 사이에 **편집 가능한 중간 표현(코드 · 3D 프록시)** 을 둔다 — 사용자가 결과가 틀렸을 때 프롬프트를 다시 쓰는 대신 프록시를 고칠 수 있는 UX 가능성. 구현 난이도 높음(3D 코드 생성 + 렌더 + 조건부 영상 모델).
- **워크플로우**: 작업 분류 → 프록시 가이드 or 직접 생성 선택 → 개체별 세밀도 → 시각 검사 · 독립 리뷰 → 수리.
- **프롬프트 패턴**: 프록시에 정렬된 프롬프트가 품질을 올린다(초록) — 구도 · 물체 위치를 프록시와 같은 어휘로 서술.
- **경쟁 우위 빈틈**: 🔴 저자가 스스로 적은 한계 — **장편에서 전환 안정성과 장면 설정 준수가 약함**([[자기제한-명시]]). VTR 지시 준수 · R2M 장면 일관성 선두 주장이나 초록 수치 0.

## 관련 페이지
- [[Kling-MLLM-Report]] · [[AI-영상-생성-2026]] · [[월드모델]] · [[자기제한-명시]] · [[3DGS]] · [[video-saas]]

## 원본
- 출처: https://huggingface.co/papers/2611.26595
- 확인 범위: HF papers API(초록 전문 — long · transition 문장 확인 · 조직 · githubRepo) · 🔴 본문 표 미열람
- 신뢰도: ⭐⭐⭐
