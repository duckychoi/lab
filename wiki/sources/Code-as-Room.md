---
title: Code-as-Room — 에이전트 코드 합성으로 탑다운 이미지 기반 3D 방 생성
type: source
domain: ai-news
tags: [ai-news, slam-3dgs, 3d-generation, code-synthesis, agent, interior-ai]
created: 2026-05-19
updated: 2026-05-19
sources: []
reliability: medium
---

# Code-as-Room — 에이전트 코드 합성으로 탑다운 이미지 기반 3D 방 생성

## 핵심 인사이트

> [!insight] 핵심 인사이트
> 탑다운(조감도) 이미지를 입력으로 받아 에이전트가 코드를 합성해 3D 방(인테리어)을 자동 생성. "코드로 3D 장면 표현"이라는 독특한 접근 — 3D 자산 직접 생성이 아닌 절차적 코드 합성으로 구조화된 3D 공간 표현. [[Map2World]](세그멘테이션 맵 기반 3D)와 유사한 방향에서 코드 에이전트 결합.

## 도메인별 추출 (ai-news / slam-3dgs 교차)

- **신뢰도**: HF 업보트 24 (2026-05-19), arXiv 2605.18451, 학술 논문
- **즉시 활용**: NO — 데모/코드 공개 여부 확인 필요. 인테리어 설계 자동화 연구 방향 참조
- **6개월 영향력**: [[Map2World]]·[[anyrecon]]·[[GlobalSplat]]과 함께 "입력 이미지 → 3D 공간" 파이프라인 경쟁 심화. 에이전트 코드 합성이 3D 생성에 결합되는 첫 사례 중 하나
- **대체 관계**: [[Meshy]]·[[Tripo]] 같은 3D 자산 생성 도구 대비 방·공간 특화. 인테리어 AI 특수 목적
- **허와 실**: 탑다운 이미지만으로 정확한 3D 공간 복원이 가능한지(깊이·비율 추정) 검증 필요

## 관련 페이지

- [[Map2World]] — 세그멘테이션 맵 조건 3D 월드 생성
- [[anyrecon]] — 비디오 디퓨전 임의 시점 3D 재구성
- [[GlobalSplat]] — 전역 장면 토큰 3DGS 재구성
- [[AI-3D-생성]] — 3D 생성 AI 전체 지형도

## 원본

- 출처: https://huggingface.co/papers/2605.18451
- 신뢰도: ⭐⭐ (업보트 24, arXiv 2605.18451, 2026-05-19)
