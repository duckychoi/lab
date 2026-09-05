---
title: Raw — 인제스트 대기열
updated: 2026-09-05 (대기 13건 — 09-05 자동수집 배치 추가)
---

# Raw 대기열

인제스트할 소스를 여기에 추가한다.
LLM이 처리(ingest) 완료하면 해당 항목을 즉시 삭제한다.

형식:
```
## 소스 제목
- type: url | text | file
- url: https://...
- 메모: (선택사항)
```

---

## 대기 중: **13건** (아래 `2026-09-05 자동수집` 절)

2026-09-04 자동수집 13건(GitHub 5 · HF논문 5 · HF모델 3)은 전량 ingest 완료되어 삭제됐다.
처리 결과는 `log.md` 의 `## [2026-09-04] ingest` 항목 참조.

> ⚠️ **수집기 반영 필요 2건** (자세한 내용은 actionable.md)
> 1. **`gated` 오독** — 09-04 배치에서 pyannote·SAM 3 두 건을 *"게이트라 카드 열람 불가·벤치마크 미확인"* 으로 기록했으나 **둘 다 비인증으로 카드 전문이 열렸다**. `gated` 는 **가중치 다운로드** 게이트이지 카드 열람 게이트가 아니다.
> 2. **증분 필드 폐기** — *"당일 +N"* 표기는 **절대값만 채택** 규칙에 따라 계속 미채택(9회 연속).

---

# 2026-09-05 자동수집 (13건 · 대기 중)

> 수집 시각 2026-09-05 09:00 KST. 전량 GitHub API / HF API 실측 대조.
> ⚠️ HF 모델은 트렌딩 목록 중 **볼트에 전용 소스 페이지가 없는 것**만 다운로드 순으로 채택했다. 최상위 HauhauCS/Qwen3.8-27B-Uncensored-Aggressive-MTP-GGUF(1,463,966 DL)는 `wiki/sources/Qwen3.8-27B-Uncensored-Aggressive-MTP-GGUF.md` 로 **이미 인제스트되어 제외**했고, 차순위 DeepSeek-V4-Flash-Vision-Exp를 채웠다.
> ⚠️ HF 데일리 페이퍼는 09-05분이 **아직 미게시**(API 0건)라 최신 게시분인 **09-04 목록**에서 09-04 배치 인제스트 5건(2609.04199 · 2609.03430 · 2608.26730 · 2609.04196 · 2609.02367)을 제외한 상위 5건을 채택했다.
> ✅ `gated` 규칙 준수: HF 모델 3건 모두 `gated=False` 확인 후 카드 전문 조회, 벤치마크 표 직접 확보(추정·미확인 없음).
> ✅ 증분 필드 미채택 **10회 연속**: "당일 +N" 값은 기록하지 않고 **절대값만** 채택.

## [2026-09-05] 자동수집 | anomalyco/opencode — 오픈소스 AI 코딩 에이전트
- URL: https://github.com/anomalyco/opencode
- 도메인: ai-news
- 스타수: 204,347
- 한줄요약: 터미널 기반 오픈소스 코딩 에이전트(TypeScript, 기본 브랜치 `dev`), npm `opencode-ai`로 배포되며 특정 모델 벤더에 묶이지 않는다.

## [2026-09-05] 자동수집 | github/spec-kit — 명세 주도 개발(SDD) 툴킷
- URL: https://github.com/github/spec-kit
- 도메인: ai-news
- 스타수: 133,541
- 한줄요약: GitHub 공식 레포로, 코딩 에이전트에게 코드를 시키기 전에 **명세를 먼저 확정**시키는 프로세스를 CLI로 강제한다. 특정 에이전트에 비종속(any AI coding agent).

## [2026-09-05] 자동수집 | upstash/context7 — LLM용 최신 코드 문서 MCP 서버
- URL: https://github.com/upstash/context7
- 도메인: ai-news
- 스타수: 61,647
- 한줄요약: 라이브러리 문서를 버전별로 끌어와 프롬프트에 주입하는 MCP 서버(기본 브랜치 `master`). 모델의 학습 시점 이후 API 변경으로 인한 환각을 **외부 문서 대조**로 막는 방향.

## [2026-09-05] 자동수집 | cathrynlavery/diagram-design — 코딩 에이전트용 다이어그램 문법 38종
- URL: https://github.com/cathrynlavery/diagram-design
- 도메인: ai-news
- 스타수: 31,255
- 한줄요약: Claude Code·Codex·Pi가 생성할 수 있는 편집형 다이어그램 38종을 **자체 완결 HTML+SVG**로 규정한다(Mermaid 미사용, 정적 출력이 기본). 2.5.10에서 Sankey·fishbone·Wardley map·kanban 등 10종 추가.

## [2026-09-05] 자동수집 | radixark/miles — LLM/VLM 사후학습용 엔터프라이즈 RL 프레임워크
- URL: https://github.com/radixark/miles
- 도메인: ai-news
- 스타수: 2,609
- 한줄요약: slime에서 포크한 대규모 모델 사후학습 전용 RL 프레임워크. 배치 내 최저 스타수지만 GitHub 일간 트렌딩 진입분이며, 기준선 1,000을 상회한다.

## [2026-09-05] 자동수집 | Terminal-Universe: 에이전트 궤적을 실행 가능 환경으로 역복원
- URL: https://huggingface.co/papers/2609.04148
- 도메인: ai-news
- 업보트: 223
- 한줄요약: 축적된 에이전트 궤적의 **툴 실행 이력을 되감아** 파일을 수정 전 상태로 복원, 궤적 1건을 재질의 가능한 환경 1개로 바꾼다. 궤적은 고정된 시연 1회지만 환경은 검증 가능한 과제를 여러 개 다시 뽑아낼 수 있다는 것이 논지.

## [2026-09-05] 자동수집 | LLaDA-Image: 완전 공개 레시피의 6B 이미지 생성기
- URL: https://huggingface.co/papers/2609.03796
- 도메인: ai-news
- 업보트: 204
- 한줄요약: 6B DiT를 처음부터 학습하되 **이미지 단독 사전학습으로 시각 사전지식을 먼저 세우고** 페어 데이터 의존을 낮췄다. Qwen-Image-Bench 종합 **영문 53.53 / 중문 53.38**로 오픈소스 최고, Turbo 증류본은 2~4스텝 추론. 가중치·학습코드·레시피 공개.

## [2026-09-05] 자동수집 | LatentPress: 텍스트도 이미지도 아닌 제3의 컨텍스트 압축
- URL: https://huggingface.co/papers/2609.01507
- 도메인: ai-news
- 업보트: 107
- 한줄요약: 대화 이력을 **동결된 디코더가 입력 임베딩으로 직접 읽는 연속 메모리 토큰**으로 쓴다(추론 시 텍스트 복원 없음). 어댑터만 학습(4.2M~26.2M, 디코더의 ~0.1%). LongMemEval **0.504@7.70배 압축**으로 무압축 원문 0.490을 **상회**, 텍스트 요약 0.184·OCR 0.426~0.312를 크게 앞선다. 쓰기 43ms/대화, 읽기 5~9배 빠름.

## [2026-09-05] 자동수집 | On-Policy Distillation II: 학습 예제 1개로 어디까지 가는가
- URL: https://huggingface.co/papers/2609.04172
- 도메인: ai-news
- 업보트: 72
- 한줄요약: 질의 **단 1개**로 학습해도 수백 스텝 동안 계속 개선되며 전체 데이터 OPD 이득의 대부분을 회수한다. 상태 커버리지 **1개 질의 71.5%(대부분 첫 100스텝 내) → 16개 질의 98.9%**로 전체 데이터와 동급. 결론: OPD는 **데이터 과잉·알고리즘 부족**(data-overfed, algorithm-starved).

## [2026-09-05] 자동수집 | Minima: Gated DeltaNet이 4비트를 견디는 이유 (NVFP4 W4A4)
- URL: https://huggingface.co/papers/2609.04098
- 도메인: ai-news
- 업보트: 72
- 한줄요약: 하이브리드 27B(GDN 48층+어텐션 16층)에서 그동안 8/16비트로 남겨두던 GDN 게이트까지 포함해 **선형층 496개 전부를 NVFP4 W4A4**로 내렸는데 BF16과 시드 노이즈 내 동등(5과제 평균 **-0.52**), 최소 용량 **17.5 GiB**, 프리필 **+14~19%**. "재귀에서 오차가 누적된다"는 통념과 반대로 게이트 투영이 **가장 덜 민감**했고(GEMM 오차 ~11% → 출력 오차 ~2%), 32K 구간에서 주입 노이즈가 평탄하게 유지된다.

## [2026-09-05] 자동수집 | unsloth/Qwen3.8-Flash-Next-GGUF
- URL: https://huggingface.co/unsloth/Qwen3.8-Flash-Next-GGUF
- 도메인: ai-news
- 다운로드수: 702,251 (좋아요 791, 생성 2026-08-26, gated=False)
- 한줄요약: Qwen3.8-Flash-Next의 Unsloth Dynamic 3.0 GGUF 양자화 재배포, MTP로 추론 1.3~1.7배 가속. ⚠️ 카드에 **자체 벤치마크 표 없음** — "타 양자화보다 정확도 우수"는 문서 링크만 있고 이 카드에 수치 미제시. 라이선스 `qwen-community-1.0`(other).

## [2026-09-05] 자동수집 | ISTA-DASLab/Qwen3.8-27B-GSQ-RCO-GGUF
- URL: https://huggingface.co/ISTA-DASLab/Qwen3.8-27B-GSQ-RCO-GGUF
- 도메인: ai-news
- 다운로드수: 206,575 (좋아요 327, 생성 2026-08-28, gated=False)
- 한줄요약: GSQ(arXiv 2604.18556)·RCO(arXiv 2605.00649) 기반 **비균일 혼합정밀 양자화**. IQ3_S(3.50bpw·11.8GB, **4.6배 축소**)가 AIME25 **100.00**과 LiveCodeBench v6 **85.71**로 BF16과 동일, GPQA-D만 89.39(BF16 89.90)로 0.51 뒤진다. 동일 파일 크기(8.4GB)에서 Unsloth UD-IQ2_S 대비 AIME25 **+10.00**·GPQA-D +8.59·LCB +4.57. Apache-2.0. ⭐배치 유일의 **제3자 대조 벤치마크 표** 보유.
## [2026-09-05] 자동수집 | deepseek-ai/DeepSeek-V4-Flash-Vision-Exp
- URL: https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-Vision-Exp
- 도메인: ai-news
- 다운로드수: 133,024 (좋아요 628, 생성 2026-08-31, gated=False, MIT)
- 한줄요약: DeepSeek-V4 계열 **첫 멀티모달 실험 모델** — V4-Flash 아키텍처에 시각 모듈을 얹어 연속 학습했다. 텍스트 에이전트 성능을 유지한 채 멀티모달 에이전트가 크게 올랐다: ApexBench Pass@1 **26.2→36.5**, Agents' Last Exam **25.2→27.3**(전작 V4-Flash-0731 대비). Opus-4.8 대비로는 Agents' Last Exam 27.3 vs 25.7·ZeroBench Pass@5 35.0 vs 34.0으로 **앞서고**, NL2Repo 57.7 vs 69.7·DSBench-Hard 63.6 vs 71.7로는 크게 뒤진다. DeepSWE 59.3 vs 58.0. ⚠️ 자체 공표 표이며 제3자 재현 없음.

