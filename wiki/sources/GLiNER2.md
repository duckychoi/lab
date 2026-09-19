---
title: "GLiNER2 (레포) — 스키마 하나로 5종 정보추출. 그러나 레포는 모델이 아니라 아키텍처 2종·체크포인트 9종의 컨테이너다"
type: source
domain: ai-news
tags: [ai-news, github-trending, information-extraction, ner, relation-extraction, encoder, deberta, cpu-inference, fastino, 컨테이너, 중복판정]
created: 2026-09-19
updated: 2026-09-19
sources: [gliner2.5-multi-v1.md]
reliability: medium
---

# fastino-ai/GLiNER2 (레포)

> [!insight] 핵심 인사이트 — **로더가 아키텍처 경계를 가른다. "GLiNER2"라는 이름은 이제 두 개의 서로 다른 물건을 가리킨다**
> README 첫 화면이 스스로 밝힌다: *"Two extraction architectures share one public API"* —
> - **`span`** (`GLiNER2` / `SpanExtractor`) — 고정폭 스팬 그리드. *"legacy checkpoints and specialty fine-tunes (GLiGuard, PII)"*
> - **`boundary`** (`BoundaryExtractor`, **GLiNER2.5**) — 시작·끝 희소 페어링, *"any span length within the encoded window"*
>
> 🔴 **그리고 클래스 이름이 아키텍처 이름과 어긋난다**: *"`GLiNER2.from_pretrained(...)` remains span-only and will **not** load GLiNER2.5 boundary checkpoints."* → **`GLiNER2` 클래스로는 GLiNER2.5를 못 읽는다.** 반드시 `AutoExtractor` 를 써야 한다.
> 🎯 **실무 함의**: 블로그·튜토리얼·기존 코드의 `GLiNER2.from_pretrained("fastino/...")` 를 그대로 복사하면 **2.5 체크포인트에서 깨진다.** 레포 이름·패키지 이름·클래스 이름이 전부 `GLiNER2` 인데 최신 모델은 그 클래스로 안 열린다 — 이게 이 레포의 가장 실용적인 사실이다.

> [!warning] ⚖️ 컨테이너 규약 적용 — **이 페이지는 [[gliner2.5-multi-v1]] 의 수치를 복제하지 않는다**
> 이 레포는 [[컨테이너-중복]] 의 두 번째 사례다(첫 사례 [[MiniCPM]]): **레포 1 ⊃ 아키텍처 2 ⊃ 체크포인트 9.** 볼트 규약(09-18 확정)에 따라:
> - 여기엔 **컨테이너 고유 사실**만 적는다 — 아키텍처 2종 · 로더 제약 · 체크포인트 목록 · 설치 프로파일 · 벤치 부재 구조
> - **다운로드·♥·카드 한계(청크 경계 등)·가중치 크기 정정은 [[gliner2.5-multi-v1]] 에만** 있다 → 그쪽을 보라
> - **★1,977 은 컨테이너 지표**다. 9개 체크포인트 중 어느 것의 지표도 아니다.
> ✅ **수집기가 이 관계를 자진신고했다** — 09-18에 볼트가 *"교차유형 중복은 자진신고가 유일한 탐지 경로"* 라고 판정한 뒤 **첫 배치에서 규약을 그대로 적용**했다.

## 컨테이너 구성 — 체크포인트 9종 (README `## 📦 Available Models` 원문 대조)

| 계열 | 체크포인트 | 파라미터 | 인코더 | 언어 |
|---|---|---|---|---|
| GLiNER2 (span) | `gliner2-base-v1` | 205M | DeBERTa-v3-base | English |
| | `gliner2-large-v1` | 340M | DeBERTa-v3-large | English |
| | `gliner2-multi-v1` | ~205M | mDeBERTa-v3-base | Multilingual |
| GLiNER2.5 (boundary) | `gliner2.5-small-v1` | 74M | DeBERTa-v3-xsmall | English |
| | `gliner2.5-base-v1` | 194M | DeBERTa-v3-base | English |
| | **[[gliner2.5-multi-v1]]** | → 구성원 페이지 | → 구성원 페이지 | Multilingual |
| Safety/PII (span 파인튠) | `gliguard-LLMGuardrails-300M` | ~300M | — | — |
| | `gliner2-privacy-filter-PII-multi` | 205M | — | 다국어 PII 42 엔티티 타입 |
| | `GLiNER2-Guardrails-PII-Multi` | 205M | — | — |

(표 전체 전사 — 3개 하위표 9행을 한 표로 합쳤다. 볼트 페이지가 있는 구성원의 값은 규약 2에 따라 여기 복제하지 않고 링크로 대체했다. 나머지 수치는 README 기재값이며 볼트가 각 체크포인트 API로 재측정하지 않았다. 볼트 페이지가 있는 구성원은 **[[gliner2.5-multi-v1]] 1개**뿐.)

📌 **README 자체 추천**: *"Prefer `gliner2.5-base-v1` for English and `gliner2.5-multi-v1` for multilingual."* — 영어면 multi가 아니라 base다.

## 도메인별 추출 (ai-news)

- **신뢰도**: ★**1,977** · fork 181 · open_issues **55**(=2.78%, 이 필드는 열린 PR 포함) · Apache-2.0 · 생성 2025-07-07 · 최근 push 2026-09-18 (GitHub API `stargazers_count`·`forks_count`·`open_issues_count`·`created_at`·`pushed_at`, 2026-09-19 조회). 출처 논문 arXiv:2507.18546 (EMNLP 2025 System Demonstrations, README 인용 블록 기재). → **medium**: 논문은 있으나 **레포의 현행 주력(2.5 boundary)에 대한 품질 수치는 어디에도 없다**(아래).
- **즉시 활용**: **YES (조건부)** — `pip install "gliner2[local]"` 로 로컬 CPU 추론. LLM 호출 없이 엔티티·분류·관계·레코드를 **한 번의 forward pass**로 뽑으므로, 대량 문서 전처리(예: 이 볼트의 인제스트 대상 텍스트에서 인물·기업·모델명 자동 태깅)에 **LLM 대비 비용 0**으로 붙일 수 있다. 단 한국어는 [[gliner2.5-multi-v1]] 의 언어 검증 이슈를 먼저 볼 것.
- **6개월 영향력**: "스키마 선언 → 로컬 인코더 추출" 패턴이 LLM 기반 JSON 추출의 **저비용 1차 필터**로 자리잡을 가능성. 논문 표 4 기준 라벨 수가 늘어도 지연이 거의 안 늘어난다(아래) — 라벨 수십 개짜리 분류기에서 의미가 크다.
- **대체 관계**: spaCy NER · 제로샷 NLI 분류기(`deberta-v3-*-zeroshot`) · 소형 LLM JSON 추출을 **하나로 묶는다.** GPT-4o 급 품질은 아니다(논문 스스로 *"GPT-4o leads across all tasks"*).
- **허와 실**: 아래 별도 섹션.
- **액션**: star · 한국어 문장 10개로 `gliner2.5-multi-v1` 실측(→ [[gliner2.5-multi-v1]] action).

## 허와 실 — "벤치 0개"의 정확한 위치

> [!warning] 🔴 README 1,360행에 **품질** 수치는 0개다. 그러나 "수치 0개"는 채널마다 뜻이 다르다
> - **README**: 성능 비교표 없음 ✅(수집기 일치). 수치는 LoRA 절(*"Adapters are ~2-10 MB vs ~450 MB"* · *"2-3x faster than full fine-tuning"*)뿐 — 둘 다 근거 미제시.
> - **논문 초록**: *"**competitive** performance across diverse IE tasks"* — 정성 서술 ✅(수집기 일치)
> - 🎯 **논문 본문에는 수치가 있다** — 단, **2025년 span 체크포인트(205M, 영어) 기준**이다. 수집기는 초록만 읽었다.
>
> **논문 본문(arXiv html 2507.18546) 수치 — 표 3 전체(CrossNER 제로샷 F1)**:
> ```
>              GPT-4o   GLiNER-M   GLiNER2
> AI           0.547    0.518      0.526
> Literature   0.561    0.597      0.564
> Music        0.736    0.694      0.632
> Politics     0.632    0.686      0.679
> Science      0.518    0.581      0.547
> Average      0.599    0.615      0.590
> ```
> 🔴 **본문 서술 오류 발견**: 본문은 *"achieves higher scores in **AI (0.526 vs. 0.547)** and Literature"* 라고 적는다. **0.526 < 0.547 — AI에서는 GPT-4o보다 낮다.** 표와 서술이 불일치한다. 또 평균은 **전문 NER 모델 GLiNER-M(0.615)에도 진다.**
> **표 4 전체(CPU 지연 ms, 분류 라벨 수별)**:
> ```
> #Labels   GPT-4o   DeBERTa   GLiClass   GLiNER2
> 5         358      1714      137        130
> 10        382      3404      131        132
> 20        425      6758      140        163
> 50        463      16897     190        208
> Speedup   1.00×    0.10×     2.75×      2.62×
> ```
> 🎯 **이 표가 진짜 셀링 포인트다** — DeBERTa 제로샷은 라벨마다 forward pass를 반복해 **선형으로** 느려지고(50라벨 16.9초), GLiNER2는 한 번에 처리해 **130→208ms**. 단 🔴 GPT-4o는 **API 왕복 지연**(네트워크 포함)이고 나머지는 CPU 로컬 — **측정 조건이 다른 비교**다([[단위-불일치]]).
>
> 📌 **결론**: 이 수치들은 **GLiNER2.5(boundary)에 대해 아무것도 말하지 않는다.** 2.5 계열의 품질 수치는 README·카드·논문 어디에도 없다. `benchmarks/`·`bench/`·`benchmark_statistical.py` 는 전부 **속도** 측정 스크립트다.

> [!warning] 🔴 "100% local"과 기본 설치의 긴장
> *"🛡️ Privacy: 100% local processing, zero external dependencies"* 라고 적으면서, **기본 `pip install gliner2` 는 torch 없이 클라우드 API 클라이언트(`GLiNER2API`, `PIONEER_API_KEY`)를 설치한다.** 로컬 추론은 `[local]` extra를 붙여야 한다.
> 🎯 **로컬은 가능하지만 기본값은 아니다.** 민감 데이터용이라면 `[local]` 설치 + API 키 미설정을 확인해야 한다. → [[한정어-탈락]] 의 변형: "100% local"의 성립 조건(`[local]` 프로파일)이 기능 목록과 다른 절에 있다.

## 수집기 대조

- ✅ 원문 대조 일치: ★1,977 · Apache-2.0 · 생성 2025-07-07 · open_issues 55(2.78%) · README 1,360행 · 아키텍처 2종 · `GLiNER2.from_pretrained()` 2.5 로드 불가 · 체크포인트 9종 · 인코더 74M~340M · 논문 초록 *"competitive"*
- ⚠️ 부분 정정: *"`benchmarks/` 는 FlashDeBERTa 속도 측정 스크립트뿐"* → `benchmarks/` 에는 `benchmark_batching.py`·`benchmark_flashdeberta.py` **2개**, 루트에 `benchmark_statistical.py`, 별도 `bench/`(`bench_boundary_head.py` + `results/` JSON 2개, CPU·fp32·iters 2 마이크로벤치)가 있다. **결론(품질 벤치 없음)은 유지.**
- ⚠️ 보강: *"벤치마크 수치 0개"* 는 **README 한정**으로 참. 논문 본문엔 v1 span 수치가 있다(위).
- 미확인: *"당일 +35 · Python 데일리 트렌딩"* — 2026-09-19 조회 시 Python 데일리 트렌딩 페이지에서 이 레포를 찾지 못했다(시점 차 가능). 튜토리얼 16개 미열람(수집기와 동일).

> [!action] 당장 할 것
> 1. **코드에서 `GLiNER2.from_pretrained` 를 `AutoExtractor.from_pretrained` 로 통일**하는 것을 기본 습관으로 — 2.5 체크포인트 호환.
> 2. 볼트 인제스트 전처리용 **엔티티 자동 태깅 PoC**: `gliner2.5-base-v1`(영어 원문) 로 raw.md 항목에서 `organization`·`model`·`benchmark` 추출 → wikilink 후보 생성. LLM 호출 0. (우선순위 중간)

> [!question] 미해결 질문
> - **GLiNER2.5 boundary가 span 대비 품질이 나은가?** 저자 측 수치 0. `docs/gliner2_5_boundary_architecture.md`(설계 노트) 미열람 — 거기에 내부 평가가 있는지 확인 필요.
> - 논문 표 3의 **서술 오류(AI 0.526 vs 0.547 "higher")** 가 arXiv v2 이상에서 정정됐는지 미확인.
> - span 파인튠(GLiGuard·PII)이 **2.5 boundary로 재학습될 계획**이 있는가? 현재 안전 계열은 전부 레거시 span.

## 관련 페이지
- [[gliner2.5-multi-v1]] — 이 컨테이너의 구성원 (볼트 유일)
- [[컨테이너-중복]] — 두 번째 사례
- [[MiniCPM]] — 첫 사례 (레포 1 ⊃ 모델 4계열)
- [[파생저장소-식별]]
- [[단위-불일치]] — 표 4의 API vs 로컬 지연 비교
- [[한정어-탈락]]
- [[자기제한-명시]] — "주장 있음 + 근거 없음" 쪽
- [[Fastino]] *(신설 제안)*
- [[Microsoft]] — DeBERTa-v3 / mDeBERTa-v3 인코더 원저
- [[ai-news]]

## 원본
- 출처: https://github.com/fastino-ai/GLiNER2 (README HEAD, 2026-09-19 조회)
- 논문: https://arxiv.org/abs/2507.18546 (본문 html 열람)
- 측정: GitHub API `stargazers_count` 1,977 · `forks_count` 181 · `open_issues_count` 55 · `pushed_at` 2026-09-18T12:17:46Z · `created_at` 2025-07-07T15:54:16Z · `license` Apache-2.0 (2026-09-19)
- 신뢰도: ⭐⭐⭐ (★1,977 · 논문 있음 · 현행 2.5 계열 품질 수치 없음)
