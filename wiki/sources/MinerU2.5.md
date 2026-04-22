---
title: MinerU2.5 — 1.2B 파라미터 고정밀 문서 파싱 VLM
type: source
domain: ai-news
tags: [ai-news, hf-paper, document-parsing, VLM, OCR, pdf, table-extraction, coarse-to-fine]
created: 2026-04-11
updated: 2026-04-11
sources: []
reliability: high
---

# MinerU2.5 (arXiv 2509.22186)

> [!insight] 핵심 인사이트
> 1.2B 파라미터 VLM으로 PDF·수식·표·고해상도 문서 파싱 SOTA 달성. Coarse-to-fine 2단계 전략으로 연산 오버헤드 최소화. 현실적인 크기(1.2B)에서 문서 파싱을 "해결된 문제"로 만든 것이 핵심 — 로컬 배포 가능하면서 수식/표도 인식.

## 핵심 인사이트

> [!action] 당장 할 것
> **높은 우선순위**: PDF → 마크다운 파이프라인에 MinerU2.5 도입 테스트. 현재 [[defuddle]] 또는 pypdf 대체. arXiv/논문 인제스트 자동화에 즉시 활용 가능.

> [!note] 배경 정보
> MinerU 시리즈는 이미 커뮤니티 검증이 많음. 2.5는 VLM 기반으로 전환하며 수식·표 인식 대폭 개선. 1.2B은 GPU 메모리 6-8GB 수준에서 실행 가능 — 실용적 배포 가능.

## 도메인별 추출 (ai-news 템플릿)

- **신뢰도**: ⭐⭐⭐⭐ — HF 논문, MinerU 시리즈 기존 신뢰도 높음
- **즉시 활용**: YES — 현재 wiki 인제스트 파이프라인에 즉시 통합 가능
- **6개월 영향력**: PDF 지식 베이스 구축 자동화 전환점. 수식 포함 학술 자료도 정확히 파싱
- **대체 관계**: Marker, nougat, pdftextract 대체. 수식/표 인식은 기존 대비 명확히 우위
- **허와 실**: "SOTA"는 특정 벤치마크. 복잡한 레이아웃(2단 논문, 차트 혼합)에서 실제 성능 확인 필요
- **액션**: HF 모델 확인 → wiki arXiv 인제스트 파이프라인에 통합 실험

## 관련 페이지

- [[LLM-Wiki]] — 지식 인제스트 파이프라인
- [[문서-파싱]]

## 원본

- 출처: https://arxiv.org/abs/2509.22186
- 신뢰도: ⭐⭐⭐⭐ (HF 검증 논문)
