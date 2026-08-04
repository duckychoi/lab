---
title: allenai/olmocr — PDF·이미지를 LLM 학습용 텍스트로 선형화하는 OCR 툴킷
type: source
domain: ai-news
tags: [ai-news, github-trending, ocr, document-parsing, vlm, dataset, allenai]
created: 2026-07-02
updated: 2026-07-02
sources: []
reliability: high
---

# olmocr (allenai/olmocr)

> [!insight] 핵심 인사이트
> ⭐18,454 (2026-07-02, 당일 +334). [[Allen Institute for AI (AI2)]]가 만든 **문서→클린 텍스트/마크다운 변환 OCR 툴킷**으로, 핵심은 단순 글자 인식이 아니라 **LLM 학습 데이터셋용 "선형화(linearization)"** 다. 7B 비전-언어 모델(VLM)을 백본으로 수식·표·손글씨·다단 레이아웃을 처리하고 헤더/푸터를 자동 제거해 *기계 판독 가능한 순서*로 재배열한다. 비용은 **100만 페이지당 200달러 미만**을 표방하고 `olmOCR-Bench` 벤치까지 함께 공개, **Apache 2.0**. [[MinerU]]·[[Unlimited-OCR]]와 같은 "문서→LLM 입력" 계보의 대표 오픈소스로, AI2라는 신뢰 출처가 붙어 신뢰도가 높다.

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐⭐⭐ — AI2 공식 + ⭐18.4K + 자체 벤치(olmOCR-Bench) 공개 + Apache 2.0. 문서 파싱 도메인에서 [[MinerU]]와 함께 가장 검증된 축.
- **즉시 활용**: YES — 이 위키의 [[wiki]] 인제스트 파이프라인에서 **PDF/스캔 문서를 마크다운으로 정제하는 전처리 게이트**로 바로 투입 가능. `defuddle`가 웹 HTML을 담당한다면 olmocr는 PDF·이미지 소스를 담당하는 대칭축.
- **6개월 영향력**: 높음 — "PDF를 LLM에 넣기 전 정제"가 표준 단계로 굳는 흐름. 100만 페이지 $200 미만이면 대량 문서 코퍼스 구축의 진입장벽이 크게 낮아짐.
- **대체 관계**: 상용 OCR(문서 AI) API를 로컬 GPU/Docker 배포로 대체. [[MinerU]](2.5 VLM 엔진)와 직접 경쟁·보완 관계.
- **허와 실**: "$200/100만 페이지"는 배치·GPU 조건에 의존하는 추정치. 손글씨·복잡 표 정확도는 문서 종류별 편차가 크므로 내 실제 문서로 검증 필요.
- **액션**: [[wiki]] 인제스트에 PDF 소스가 들어올 때 olmocr vs [[MinerU]] 정확도·속도 대조 → 우세한 쪽을 표준 PDF 게이트로 채택.

> [!action] 당장 할 것
> raw.md에 PDF/스캔 소스가 등장하면 olmocr로 마크다운 변환 후 인제스트하는 경로를 [[MinerU]]와 비교 테스트.

## 관련 페이지
- [[MinerU]]
- [[Unlimited-OCR]]
- [[Allen Institute for AI (AI2)]]
- [[wiki]]
- [[ai-news]]

## 원본
- 출처: https://github.com/allenai/olmocr
- 스타: ⭐18,454 (2026-07-02, 당일 +334)
- 라이선스: Apache 2.0 · 백본: 7B VLM · 벤치: olmOCR-Bench
- 신뢰도: ⭐⭐⭐ (AI2 공식 + 벤치 공개 + 실사용 검증층)
