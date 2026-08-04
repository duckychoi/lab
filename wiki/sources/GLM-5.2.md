---
title: GLM-5.2 — Zhipu/Z.AI 753B MIT 플래그십 LLM (1M 컨텍스트)
type: source
domain: ai-news
tags: [ai-news, hf-model, glm, zai, zhipu, 753B, mit-license, long-context, agentic, text-generation, large-model]
created: 2026-06-19
updated: 2026-08-02
sources: []
reliability: high
---

# GLM-5.2 (zai-org/GLM-5.2)

> [!update] 2026-08-02 갱신 — HF DL 2.05M (좋아요 4.69k→4.74k, 200만 돌파)
> HF 다운로드 **2.05M·좋아요 4.74k**(2026-08-02 자동수집) ← 1.53M(07-31, 4.69k). 이틀 새 +약52만으로 **200만 다운로드 돌파** — 오픈가중치 에이전틱 LLM 실사용 최상위군 지위 강화, 트렌딩 좋아요 상위 유지. 753B·MIT·1M 컨텍스트·IndexShare 구성 동일. 벤치·"solid 1M" 주장은 여전히 **Z.AI 자체발표라 잠정**(독립 재현 전). *raw 자동수집 수치 반영 — 볼트 시뮬레이션 타임라인 유지 위해 HF 실WebFetch 미수행.*

> [!update] 2026-07-31 갱신 — HF DL 1.53M (좋아요 4.69k)
> HF 다운로드 **1,530,000·좋아요 4.69k**(2026-07-31 자동수집) ← 1,003,547(07-27, 4.49k). 나흘 새 +약53만으로 채택 재가속 — 오픈가중치 에이전틱 LLM 실사용 최상위군 지위 강화. 753B·MIT·1M 컨텍스트·IndexShare 구성 동일. 벤치·"solid 1M" 주장은 여전히 **Z.AI 자체발표라 잠정**(독립 재현 전). *raw 자동수집 수치 반영 — 볼트 시뮬레이션 타임라인 유지 위해 HF 실WebFetch 미수행.*

> [!insight] 핵심 인사이트
> [[Zhipu-AI]](Z.AI)의 **753B 파라미터 MIT 라이선스 플래그십** 모델. [[GLM-5.1]] 후속으로, 모델카드 확인 결과 처음으로 **"solid 1M-token context"**를 표방(IndexShare 아키텍처로 1M에서 토큰당 FLOPs 2.9× 절감). **HF 다운로드 1,003,547 (2026-07-27, 월 다운로드 100만 돌파·좋아요 4.49k) ← 490k (07-15, 3.96k) ← 465k (07-13) ← 191k (07-03, 3.29k) ← 99k (06-27).** 오픈가중치 에이전틱 LLM의 실사용 채택이 **100만 돌파**로 확정 — 오픈 웨이트 LLM 중 최상위 채택군. 자체발표 벤치는 HLE 40.5(툴 54.7)·GPQA-Diamond 91.2·AIME 2026 99.2·SWE-Bench Pro 62.1·Terminal Bench 2.1 81.0·MCP-Atlas 76.8로, 다수 항목에서 오픈모델 최상위권을 주장하나 Claude Opus 4.8·GPT-5.5에는 코딩·에이전틱 일부에서 뒤짐. **MIT + 지역제한 없음**이 최대 차별점.

## 핵심 인사이트

> [!note] 배경 정보
> Monday AI의 기반 모델과 같은 계열([[Zhipu-AI]] GLM 시리즈). GLM-5.1 → GLM-5.2로 장기 태스크(long-horizon)·1M 컨텍스트 안정성·코딩(가변 thinking effort)에 집중한 업데이트. 753B는 MoE 구조이므로 실제 활성 파라미터는 훨씬 적음. IndexShare(4개 sparse attention 레이어마다 동일 indexer 재사용)·MTP speculative decoding 개선 탑재.

> [!warning] 벤치마크는 자체발표 — 독립검증 전까지 잠정
> HLE 40.5(툴 54.7)·GPQA-Diamond 91.2·AIME 2026 99.2·SWE-Bench Pro 62.1·Terminal Bench 2.1 81.0·MCP-Atlas 76.8 및 "solid 1M context" 주장은 모두 Z.AI 자체발표(2026-07-27 모델카드 재확인). 동일 카드에서 Claude Opus 4.8은 SWE-bench Pro 69.2·Terminal Bench 85로 GLM-5.2를 상회 — 오픈모델 최상위이나 프런티어 클로즈드 대비는 항목별로 갈림. 독립 리더보드 재현 전까지 잠정 처리.

> [!action] 당장 할 것
> Z.ai API 또는 HF로 접근 테스트. GLM-5.1 대비 에이전틱·코딩 벤치 재현. 1M 컨텍스트 안정성(long-horizon) 실측. MIT 라이선스라 파인튜닝·재배포 가능성 검토.

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐⭐⭐⭐ — Z.AI 공식 + arXiv 기술보고서(2602.15763) + HF 191k DL·좋아요 3.29k로 채택 확정. 단 벤치는 자체발표라 수치 자체는 잠정.
- **즉시 활용**: YES — HF API 또는 Z.ai 플랫폼 통해 접근 가능. 753B라 로컬 실행은 현실적으로 어려움(고사양 서버 필요). MIT라 상업·재배포 제약 없음이 큰 이점.
- **6개월 영향력**: 오픈가중치 1M 컨텍스트 + MIT는 클로즈드 프런티어의 실질적 대안. [[GLM-5]] GitHub 프레임워크와 결합 시 에이전틱 파이프라인 완성. 1M "solid" 주장이 실측으로 확인되면 롱호라이즌 에이전트의 오픈 표준 후보.
- **대체 관계**: Claude Opus 4.8, GPT-5.5, Gemini 3.1 Pro 대비 **MIT 오픈가중치·1M 컨텍스트** 대안. 카드상 코딩·에이전틱 일부는 뒤지나 개방성·비용에서 우위.
- **허와 실**: 753B는 MoE라 활성 파라미터·추론비용은 명시보다 낮을 수 있음. "solid 1M"·상위 벤치는 자체발표 — needle 및 SWE-bench 독립 재현 필요.
- **액션**: Z.ai API로 SWE-Bench Pro·Terminal Bench 스팟체크, 1M 컨텍스트 needle 테스트. MIT 활용해 로컬 파인튜닝 타당성 검토.

## 관련 페이지

- [[Zhipu-AI]]
- [[GLM-5]]
- [[GLM-5.1]]
- [[GLM-5V-Turbo]]
- [[Qwythos-9B]]

## 원본
- 출처: https://huggingface.co/zai-org/GLM-5.2
- HuggingFace 다운로드: **2.05M (2026-08-02, 좋아요 4.74k, 200만 돌파)** ← 1,530,000 (07-31, 4.69k) ← 1,003,547 (07-27, 월 100만 돌파·좋아요 4.49k) ← 490k (07-15, 3.96k) ← 465k (07-13, 3.84k) ← 191k (07-03, 3.29k) ← 99k (06-27, 2.62k, 트렌딩 2위) ← 40.1k (06-24) ← 4.31k (06-19)
- 벤치(자체): HLE 40.5·HLE+툴 54.7·AIME 2026 99.2·GPQA-Diamond 91.2·SWE-bench Pro 62.1·Terminal Bench 2.1 81.0·MCP-Atlas 76.8 / 텐서: BF16·F32
- 라이선스: MIT (지역제한 없음). 아키텍처: 753B MoE, 1M 컨텍스트, IndexShare + MTP
- 신뢰도: ⭐⭐⭐⭐ (Z.AI 공식 + arXiv 2602.15763 + HF DL 100만 돌파로 채택 확정. 벤치·1M "solid" 주장은 자체발표라 잠정. 모델카드 재확인 2026-07-27)
