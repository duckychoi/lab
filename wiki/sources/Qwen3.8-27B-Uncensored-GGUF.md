---
title: JonathanColetti/Qwen3.8-27B-Uncensored-GGUF — 안전 필터 제거 GGUF 재배포판
type: source
domain: ai-news
tags: [ai-news, hf-model, gguf, uncensored, quantization, local-inference, qwen, local-llm, safety]
created: 2026-08-22
updated: 2026-08-22
sources: []
reliability: low
---

# Qwen3.8-27B-Uncensored-GGUF — 파생 생태계가 '양자화'에서 '가드레일 제거'로 분화

**HF 모델**: https://huggingface.co/JonathanColetti/Qwen3.8-27B-Uncensored-GGUF
**지표(2026-08-22 HF API 실호출)**: DL **1,223,422** · 좋아요 **585** · 트렌딩 **5위** · 태스크 `text-generation` · 최종수정 2026-08-16 · 라이선스 apache-2.0
**태그(원문)**: `llama.cpp` `gguf` `uncensored` `qwen3.8` `mtp` `speculative-decoding` `imatrix` `quantized` `en` `zh`
**원본**: [[Qwen3.8-27B]] ([[Alibaba]]) — `base_model:quantized:Qwen/Qwen3.8-27B` 로 계보 명시

> [!insight] 핵심 인사이트 — 파생 축이 "실행 효율"에서 "행동 제약 해제"로 갈라진 첫 정량 신호
> 지금까지 볼트가 추적한 [[Qwen3.8-27B]] 파생은 **실행 환경 최적화** 축이었다 — [[Qwen3.8-27B-GGUF]](CPU/워크스테이션 GGUF)·[[Qwen3.8-27B-FP8]](GPU 서버 FP8). 오늘 상위 트렌딩에 **처음** 올라온 이 재배포판은 축이 다르다: **안전 필터 제거(uncensored)** 그 자체가 배포 사유다. 즉 동일 베이스 위에서 파생 생태계가 **"어디서 돌릴 것인가"에 더해 "무엇을 거부하지 않게 할 것인가"** 로 분화 중이라는 정량 관측.
>
> 기술 태그도 단순 재양자화가 아니다 — `mtp`(multi-token prediction)·`speculative-decoding`·`imatrix`가 함께 붙어 **속도 최적화까지 겸한 패키지**로 배포된다.

> [!warning] raw.md 주장 정정 — "공식 FP8판을 앞섬"은 **사실이 아니다**
> raw 한줄요약은 *"DL 122만으로 공식 FP8판을 앞섬"* 이라 기재했으나, **2026-08-22 HF API 교차 확인 결과 [[Qwen3.8-27B-FP8]]의 DL은 2,306,777** 로 본 모델(1,223,422)의 **약 1.9배**다. 즉 **FP8 > Uncensored**이며 raw의 비교는 뒤집혔다(08-21 시점 FP8 1.94M 값과 비교해도 이미 앞서 있었음). 네 경로의 실제 저변 순위는 **GGUF(6.32M) > FP8(2.31M) > 원본(2.09M) > Uncensored(1.22M)**.
> *([[CLAUDE.md]] 사실확인 원칙 — raw 자동수집 요약의 파생 해석은 절대값 교차확인 후에만 채택)*

> [!warning] 신뢰도 low — 검증 불가 항목이 다수
> ① **제거 방식 미공개** — abliteration인지 파인튜닝인지 초록·카드 수준 정보로 확인 불가. ② **능력 손실 미측정** — 안전 정렬 제거는 통상 일반 능력 저하를 동반하나 벤치 미제시. ③ **라이선스 준수 미검증** — apache-2.0을 표방하나 원본 정책·사용 제한 준수 여부는 별개. ④ 좋아요 **585**로 DL(122만) 대비 **인정 신호가 현저히 낮다**(원본 12,019·GGUF 2,542와 대비) — 다운로드가 곧 승인이 아님.

## 도메인별 추출 (ai-news / 교차: local-llm · safety)

- **신뢰도**: ⭐⭐ — DL·좋아요·태그는 **API 실검증**이나, 모델 자체의 **제작 방식·품질·법적 지위 전량 미검증**. reliability **low** 지정.
- **즉시 활용**: **NO** — 내 용도([[Claude-Code-워크플로우]]·[[video-saas]] 파이프라인·봇)에서 가드레일 제거가 해결하는 문제가 없다. 오히려 프로덕션 경로에 넣을 경우 **출력 책임 리스크**만 늘어난다.
- **6개월 영향력**: **관측 지표로서** 중간 — 모델 자체보다 **"파생 생태계 분화의 계측기"** 로서 가치가 있다. 이 축의 DL이 실행 최적화 축을 실제로 추월하는 날이 오면 로컬 LLM 배포 논의의 전제가 바뀐다(현재는 아직 최하위).
- **대체 관계**: [[Qwen3.8-27B-GGUF]]와 같은 실행 포맷(GGUF)이지만 **목적이 다르므로 대체 아님**. [[Qwen3.6-35B-Uncensored]]·[[Qwen3.6-35B-A3B-Uncensored-Aggressive]] 계보의 연장.
- **허와 실**: "uncensored"는 **능력 향상이 아니라 거부 감소**다. 마케팅적으로 "더 강한 모델"처럼 읽히기 쉬우나 근거가 없고, 통상 정렬 제거는 지시 이행 품질을 함께 떨어뜨린다.
- **액션**: **편입하지 않음.** 트렌딩 순위 추이만 계측 목적으로 관측.

> [!question] 미해결 질문
> 제거 기법은 무엇인가(abliteration/파인튜닝)? 일반 능력 벤치 하락 폭은? DL 122만의 실제 수요층은 누구인가(연구·우회·로컬 롤플레이)?

## 관련 페이지
- [[Qwen3.8-27B]] — 베이스 원본(계보 상류)
- [[Qwen3.8-27B-GGUF]] · [[Qwen3.8-27B-FP8]] — 실행 최적화 축 파생(대비군)
- [[Qwen3.6-35B-Uncensored]] · [[Qwen3.6-35B-A3B-Uncensored-Aggressive]] — 동일 축 선행 사례
- [[AI-Infra-Guard]] — 탈옥·가드레일 평가(방어 축 대응)
- [[local-llm]] · [[ai-news]]

## 원본
- 출처: https://huggingface.co/JonathanColetti/Qwen3.8-27B-Uncensored-GGUF
- 지표: DL 1,223,422 · 좋아요 585 · 트렌딩 5위 · 최종수정 2026-08-16 (2026-08-22 HF API 실호출) — 볼트 첫 편입
- 신뢰도: ⭐⭐ low (수치는 실검증이나 제거 방식·능력 손실·라이선스 준수 전량 미검증 / raw의 "FP8 추월" 주장은 교차확인 결과 오류로 정정)
- 수집: 2026-08-22 아침 자동수집 (HF 모델·트렌딩 5위 신규 진입)
