---
title: Program-as-Weights (PAW) — 자연어 퍼지 함수를 로컬 실행 LoRA 어댑터로 컴파일
type: source
domain: ai-news
tags: [ai-news, paper, hf-paper, local-llm, lora, adapter, small-model, compiler, efficiency]
created: 2026-07-03
updated: 2026-07-03
sources: []
reliability: medium
---

# Program-as-Weights (PAW): A Programming Paradigm for Fuzzy Functions

> [!insight] 핵심 인사이트
> HF 업보트 92 (2026-07-03 Paper of the day). 규칙 기반으로 깔끔히 구현하기 어려운 "퍼지 함수"(중요 로그 라인 알림, 깨진 JSON 복구, intent 기반 검색 랭킹 등)를 LLM API 호출 대신 **자연어 명세 → 로컬 실행 가능한 소형 신경망(parameter-efficient adapter)** 으로 컴파일하는 패러다임. 4B 컴파일러가 FuzzyBench(10M 예제, 공개)로 학습되어 frozen 0.6B 인터프리터용 어댑터를 생성 — 0.6B Qwen3 인터프리터가 Qwen3-32B 직접 프롬프팅 성능을 **약 1/50 추론 메모리**로 재현하며 MacBook M3에서 30 tokens/s. 파운데이션 모델을 "입력마다 푸는 solver"에서 "함수 정의당 한 번 호출되는 tool builder"로 재정의. 소형 로컬 모델([[Qwen3-0.6B]])과 [[Code2LoRA]]류 어댑터 자동생성 계열.

## 도메인별 추출 (ai-news)
- **신뢰도**: HF 업보트 92, University of Waterloo, 원문 초록 검증 완료 (defuddle fetch 성공). 데모 사이트·Python 패키지(`programasweights`) 공개 언급.
- **즉시 활용**: MAYBE — 로컬·재현성·비용 이점이 명확하고 `import programasweights as paw` 형태 패키지가 공개되어 있어 실험 진입장벽 낮음. 단 FuzzyBench 범위 밖 태스크 일반화는 검증 필요.
- **6개월 영향력**: 큼. "LLM API 호출을 로컬 소형 어댑터로 대체"라는 방향은 비용·프라이버시·오프라인 요구가 큰 프로덕션에서 강한 pull. 어댑터를 재사용 아티팩트로 캐싱하는 발상은 에이전트 툴 빌딩과 직결.
- **대체 관계**: per-input LLM API 호출(로컬리티·재현성·가격 손실)을 대체/보강. 수동 LoRA 파인튜닝을 자연어 명세 기반 자동 컴파일로 대체.
- **허와 실**: "0.6B가 32B급"은 FuzzyBench 유형 퍼지 함수 한정 — 범용 추론 대체가 아니라 좁은 함수 단위 재현. 컴파일러(4B) 학습 비용·데이터 커버리지가 실제 이득의 전제. 1/50 메모리·30 tok/s는 인터프리터 실행 기준(컴파일 1회 비용 별도).
- **액션**: 실험 — `programasweights` 패키지로 자체 퍼지 함수 1건 컴파일해 로컬 실행 품질/속도 측정.

> [!action] 당장 할 것
> `pip install programasweights` 후 자연어 명세 1건(예: 로그 라인 중요도 분류)을 0.6B 인터프리터로 컴파일해 API 호출 대비 품질·메모리·지연 비교. FuzzyBench 데이터셋 구성 확인.

## 관련 페이지
- [[Code2LoRA]] — 하이퍼네트워크로 태스크별 LoRA 어댑터 동적 생성 (어댑터 자동생성 계열, 강한 인접)
- [[FlashMorph]] — 사전학습 Transformer 효율화(층 선형화) 계열, PAW와 함께 "모델 효율화" 축
- [[CollectionLoRA]] — LoRA 어댑터 관리/조합
- [[Qwen3-0.6B]] — PAW 인터프리터 백본급 소형 모델
- [[온폴리시-증류]] — 대형→소형 지식 이전 관점 비교 대상
- [[에이전트-메모리-레이어]] — 재사용 아티팩트(어댑터) = 함수 단위 메모리로 볼 여지

## 원본
- 출처: https://huggingface.co/papers/2607.02512
- arXiv: 2607.02512
- 소속: University of Waterloo
- HF 업보트: 92 (Paper of the day, 2026-07-03)
- 신뢰도: 원문 초록 검증 완료 (fetch 성공)
