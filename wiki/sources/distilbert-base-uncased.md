---
title: distilbert/distilbert-base-uncased — BERT 증류 경량 인코더
type: source
domain: ai-news
tags: [ai-news, huggingface, model, distillation, bert, encoder, glue, infrastructure, apache-2.0]
created: 2026-09-15
updated: 2026-09-15
sources: []
reliability: high
---

# HF모델: distilbert/distilbert-base-uncased — 증류의 표준 레퍼런스

**URL**: https://huggingface.co/distilbert/distilbert-base-uncased
**지표(2026-09-15 API 실측 · raw 기록과 완전 일치)**: 다운로드 **7,314,069**(30일) · ♥ **1,442** · trendingScore **175**(목록 API) · **DL:♥ = 5,072:1** · **apache-2.0**
생성 **2022-03-02** · 최종수정 **2024-05-06** · `pipeline_tag: fill-mask` · `gated: False`

> [!insight] 핵심 인사이트
> BERT와 **동일 코퍼스**에서 **BERT 자신을 교사로 삼아 자기지도 증류**한 더 작고 빠른 인코더. 추론·다운스트림 태스크 비용을 낮추는 용도.
>
> 🎯 **왜 2026년에도 월 731만인가**: 분류·NER·임베딩 같은 **인코더 태스크는 생성 모델로 대체되지 않았다.** LLM 담론이 디코더에 쏠린 4년 동안 인코더 수요는 조용히 유지됐다. [[bert-base-uncased]]·[[all-MiniLM-L6-v2]] 와 같은 칸.

> [!insight] 벤치마크 (모델카드 GLUE **test**)
> MNLI **82.2** · QQP **88.5** · QNLI **89.2** · SST-2 **91.3** · CoLA **51.3** · STS-B **85.8** · MRPC **87.5** · RTE **59.9**
>
> 🔴 **성립 조건 2건(같은 불릿)**: ① 이 수치는 **GLUE test 세트 기준**이다. ② **BERT-base 대비 상대 비교표가 카드에 없다.** 즉 **"더 작고 빠르다"의 정량 근거는 이 표에 포함되어 있지 않다** — 크기·속도 주장은 카드 본문의 서술이지 표의 수치가 아니다.

> [!warning] 🔴 지는 축 — 8개 중 2개가 50%대
> **CoLA 51.3 · RTE 59.9.** 나머지 6개가 82~91인 것과 대비된다.
> **평균만 인용하면 이 두 축이 가려진다** — 8개 단순평균은 79.5이고, 이 숫자는 CoLA에서 사실상 무작위에 가깝다는 사실을 완전히 덮는다.
> 🔗 [[DataFlex-RL]] 이 같은 배치에서 증명한 것과 정확히 같은 문제다 — **어떤 벤치를 평균에 넣는지가 결론을 만든다.** 여기서는 한 모델 안에서 발생한다.

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐⭐⭐ 4년 · 731만 DL/월 · **apache-2.0 명시** · 카드에 벤치 표 존재 → high
- **즉시 활용**: **YES.** 분류·임베딩 태스크에서 LLM API 호출을 대체할 수 있는 지점이 많다. 비용·지연 모두 자릿수가 다르다.
- **대체 관계**: **LLM을 대체한다** — 반대 방향의 대체다. "모든 NLP를 LLM으로"의 비용 역풍이 오면 돌아올 카드.
- **허와 실**: 카드가 과장하지 않는다. 단 **속도·크기 이득의 수치를 카드에서 찾을 수 없다**는 점은 인용자가 메워야 한다(원논문 참조 필요).

## 관련 페이지
- [[clip-vit-base-patch32]] · [[Llama-3.1-8B-Instruct]] — 같은 배치 3건
- [[bert-base-uncased]] · [[all-MiniLM-L6-v2]] · [[gpt2]] — 상시 인프라 모델 계열
- [[DataFlex-RL]] — 평균이 축을 가리는 문제의 정량 증거
- [[온폴리시-증류]] · [[Switch-KD]] — 증류 계열
- [[ai-news]]

## 원본
- 출처: https://huggingface.co/distilbert/distilbert-base-uncased
- 검증: HF API 실호출(2026-09-15). **DL·♥·생성일·수정일·라이선스 전건 일치(드리프트 0)**
- 신뢰도: ⭐⭐⭐
