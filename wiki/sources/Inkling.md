---
title: Inkling (thinkingmachines) — 975B/41B 멀티모달 MoE (텍스트·이미지·오디오 입력)
type: source
domain: ai-news
tags: [ai-news, hf-model, moe, multimodal, frontier, benchmark, text-generation]
created: 2026-07-18
updated: 2026-07-25
sources: []
reliability: low
---

# Inkling (thinkingmachines/Inkling)

> [!update] 2026-07-25 갱신 — DL 31,575·좋아요 1,552 (관심 상승, 정체는 여전히 미검증)
> HF 다운로드 **31,575 / 좋아요 1,552**(2026-07-25) ← 12,456 / 996(07-18). 일주일 새 다운로드 2.5배·좋아요 +556로 관심은 뚜렷이 상승. 그러나 **업로더 "thinkingmachines"의 실체(Thinking Machines Lab 공식 여부)·프론티어급 자체벤치 출처·가중치 공개 범위는 여전히 미검증** — 관심 상승이 곧 검증은 아니므로 reliability **low 유지**. 라이선스는 raw에서 Apache-2.0로 수집됐으나 모델카드 원문 미실측이라 인용 시 재확인 필요. 규명 전 벤치 인용 금지.

> [!insight] 핵심 인사이트
> **텍스트·이미지·오디오 입력 → 텍스트 출력** 멀티모달 MoE. 총 **975B / 활성 41B**(256 전문가 중 6개 라우팅)로, raw 벤치는 **SWE-Bench Verified 77.6% · AIME 2026 97.1% · GPQA Diamond 87.2%** — 사실이라면 프론티어급 오픈(?) 모델. 업로더 "thinkingmachines"는 Thinking Machines Lab(전 OpenAI CTO Mira Murati 창업) 연상 명칭이나 **HF 계정 실체·가중치 공개 범위 자동수집 단계 미확인**. 좋아요 996 대비 다운로드 12,456로 **관심 대비 실사용은 초기** — 대형 MoE라 로컬 구동 장벽이 높기 때문으로 추정.

> [!warning] 신뢰도 low — 강한 클레임·출처 미검증
> ①업로더가 실제 Thinking Machines Lab 공식인지 **미확인**(이름 연상만으로 단정 금지 — [[Qwen3.6-40B-Deckard-Heretic]]의 "Claude-4.6-Opus" 오인 명명 전례 참고). ②SWE-Bench 77.6%·AIME 97.1% 등 **프론티어급 수치는 자체 리포트일 가능성**이 크고 독립 재현 없음. ③975B 총 파라미터는 소비자 하드웨어로 **로컬 구동 불가**에 가까움 — "오픈 가중치"인지 데모/게이트인지 모델카드 확인 필수. 수치·정체 규명 전까지 인용 금지.

## 도메인별 추출 (ai-news / local-llm 교차)

- **신뢰도**: ⭐⭐ 미만 — DL 12,456·좋아요 996만 확정. 벤치·업로더 정체·라이선스 전부 미검증.
- **즉시 활용**: NO — 975B MoE는 로컬 불가, API/데모 존재 여부도 불명. 현시점 관측 대상.
- **6개월 영향력**: (사실이라면) 멀티모달 프론티어 MoE의 오픈 배포가 [[GLM-5.2]]·[[LongCat-2.0]] 계보를 잇는 사건이나, **정체 확인이 선행 조건**.
- **메모리 아키텍처**: 256중 6전문가 라우팅 = 활성 41B. [[Qwen3.6-35B-A3B-MTP-GGUF]]·[[LongCat-2.0]]과 같은 sparse MoE 계열이나 규모가 한 자릿수 크다.
- **대체 관계**: 확인 시 [[GLM-5.2]](오픈 플래그십)·[[LongCat-2.0]](1.6T MoE)와 같은 대형 오픈 MoE 경쟁군. 미확인이면 편입 보류.
- **허와 실**: "유명 랩 연상 이름 + 프론티어 벤치 + 낮은 다운로드"는 전형적 **미검증 하이프 패턴**. 모델카드에서 업로더 신원·벤치 출처·가중치 공개 여부부터 규명.
- **액션**: 모델카드/커밋 이력 확인 → Thinking Machines Lab 공식 여부·라이선스·벤치 출처 규명. 규명 전 인용·추천 금지.

## 관련 페이지
- [[GLM-5.2]]
- [[LongCat-2.0]]
- [[Qwen3.6-35B-A3B-MTP-GGUF]]
- [[Qwen3.6-40B-Deckard-Heretic]]
- [[local-llm]]
- [[ai-news]]

## 원본
- 출처: https://huggingface.co/thinkingmachines/Inkling
- HuggingFace 다운로드 31,575 / 좋아요 1,552 (2026-07-25, HF API 실측) ← 12,456 / 996 (07-18)
- raw 수집 태그: image-text-to-text·audio-text-to-text, Apache-2.0(모델카드 원문 미실측)
- 신뢰도: ⭐⭐ 미만 (다운로드·좋아요만 확정, 업로더 정체·벤치 출처·가중치 공개 범위 전부 미검증, reliability low)
