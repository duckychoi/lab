# Wiki Log

시간순 기록. `grep "^## \[" log.md | tail -10` 으로 최근 항목 확인 가능.

---

## [2026-06-09] ingest | GitHub Trending + HF 자동수집 (2026-06-09 일괄)
- 도메인: ai-news (주)
- 처리 항목: 총 13개 (GitHub Trending 5 + HF 논문 5 + HF 모델 3)
- 추가 페이지: 10개 | 업데이트 페이지: 3개
  - sources 신규 (10): turbovec, Agent-Reach, google-skills, SWE-Explore, On-Policy-Distillation, Latent-Spatial-Memory, SpatialWorld, CoVEBench, gemma-4-12b-it-GGUF, gemma-4-12B-it
  - sources 스탯 업데이트 (3): last30days-skill(⭐23,614→35,739 +3,558), supervision(⭐39,051→42,596 +1,288), HRM-Text-1B(90K→133K DL)
  - index.md 업데이트 (total_pages: 459→469, total_sources: 444→454)
  - raw.md 전량 삭제 완료
- 핵심 인사이트: google/skills(Google 공식 에이전트 스킬 레지스트리) 등장으로 스킬 생태계가 빅테크 공식 채널로 확장 — Microsoft·Vercel·Google 모두 공식 스킬 배포 단계 진입. SWE-Explore가 "코딩 에이전트 탐색 능력"을 벤치마크화 — GitNexus 같은 코드 지식 그래프 도구의 학술적 근거 마련. gemma-4-12b-it GGUF(660K DL)가 Gemma-4 12B 로컬 실행 표준으로 빠르게 자리잡는 중.
- canvas 업데이트: NO
- actionable 추가: NO

---

## [2026-06-09] wiki-check | 대기 항목 없음
- 대기 항목 없음

---

## [2026-06-08] ingest | 자동수집 배치 처리 (2026-06-08)
- 도메인: ai-news (전체)
- 처리 항목: 총 13개 (신규 페이지 6개 + 업데이트 7개)
- 핵심 인사이트: hermes-agent ⭐187K — 4월 ⭐87K에서 2개월간 +115% 폭증, 에이전트 프레임워크 수요 가속. supervision +957 급등은 CV 파이프라인 표준화 수요. AnchorWorld(Kling Team)는 영상 AI→체현 AI 세계 시뮬레이션으로 영역 확장 신호. Gemma-4-12B DL 315K→554K(+75%), GGUF 458K→645K(+41%) — 12B급 로컬 멀티모달 수요 가파른 상승.
- canvas 업데이트: NO
- actionable 추가: NO

**신규 소스 페이지 생성 (6개)**
- khoj (⭐34,997) — 자체 호스팅 AI 세컨드 브레인, 개인 문서·웹 통합 RAG, 오프라인 지원
- UnEmbedding-Matrix-Feature-Lens (arXiv 2606.07502, ↑49) — 임베딩 언임베딩 행렬 피처 렌즈 발견
- MMAE (arXiv 2606.07229, ↑33) — 38인 공동 멀티태스크 오디오 편집 벤치마크
- SoCRATES (arXiv 2606.05563, ↑29) — LLM 사회인지 중재 능력 자동 평가 프레임워크
- AnchorWorld (arXiv 2606.07326, ↑21) — Kling Team 에고센트릭 체현 AI 세계 시뮬레이터
- Direct-3D-Aware-Object-Insertion (arXiv 2606.06601, ↑19) — 분해된 시각 프록시로 3D 인식 객체 삽입

**업데이트 (7개)**
- hermes-agent: ⭐184,000 → ⭐187,000 (+1,112 오늘)
- MemPalace: ⭐54,472 → ⭐54,700 (+452 오늘), LongMemEval R@5 96.6% 클레임 검증 대기
- VibeVoice: ⭐48,582 → ⭐48,700 (+275 오늘)
- supervision: ⭐39,051 → ⭐41,844 (+957 오늘, 급등)
- Gemma-4-12B-GGUF: DL 458,000 → 645,000 (+40.8%)
- Gemma-4-12B: DL 315,000 → 554,000 (+75.9%)
- LocateAnything-3B: DL 111,000 → 122,000 (+9.9%)

---

## [2026-06-07] ingest | 자동수집 배치 처리 (2026-06-07)
- 도메인: ai-news (전체)
- 처리 항목: 총 13개 중 신규 5개 처리 (신규 페이지 4개 + 업데이트 1개 + 이미 처리됨 8개 raw 삭제)
- 핵심 인사이트: CopilotKit +631 최고 급등 — 에이전트 인프라 경쟁이 백엔드 실행에서 프론트엔드 UI 통합 단계로 이동. MemPalace ⭐54K "벤치마크 1위" 클레임은 검증 전까지 신뢰도 중간. openai/whisper ⭐10만 돌파로 ASR 사실상 표준 확인.
- canvas 업데이트: NO
- actionable 추가: NO

**신규 소스 페이지 생성 (4개)**
- openai-whisper (⭐101,966) — OpenAI 범용 ASR, 100개 언어, 약지도 학습 기반 사실상 표준
- PaddleOCR (⭐81,113, +433) — Baidu 경량 OCR, LLM 파이프라인 연동 최적화
- MemPalace (⭐54,472, +446) — 오픈소스 에이전트 장기 기억 시스템, "벤치마크 1위" 클레임 요검증
- CopilotKit (⭐33,451, +631) — React 프론트엔드 AI 에이전트·생성형 UI 통합, AG-UI 프로토콜

**업데이트 (1개)**
- VibeVoice: ⭐45,909 → ⭐48,582

**이미 처리됨 → raw 삭제만 (8개)**
- Code2LoRA, ArcANE, TIDE, AdaPlanBench, VideoKR (2026-06-06 배치에서 처리 완료)
- Gemma-4-12B-GGUF, Gemma-4-12B, LocateAnything-3B (2026-06-06 배치에서 처리 완료)

**concepts 업데이트**
- [[에이전트-메모리-레이어]]: MemPalace 독립 메모리 시스템 섹션 추가

---

## [2026-06-06] ingest | 자동수집 배치 처리 (2026-06-06)
- 도메인: ai-news (전체)
- 처리 항목: 총 12개 (신규 페이지 8개 + 업데이트 4개)
- 핵심 인사이트: hermes-agent ⭐147K→⭐184K (+25% 3주), headroom ⭐7,772→⭐15,000 (+93% 3일) — 에이전트 프레임워크와 토큰 압축이 이번 사이클 양대 폭발 성장 영역. Gemma-4-12B DL 315K+GGUF DL 458K는 중간 크기 멀티모달 로컬 실행 수요 확인.
- canvas 업데이트: NO
- actionable 추가: NO

**신규 소스 페이지 생성 (8개)**
- open-notebook (⭐26,200) — Google NotebookLM 오픈소스 대체재, 18개 AI 제공사, 로컬 팟캐스트 생성
- Code2LoRA (arXiv 2606.06492, ↑56) — Waterloo대, 하이퍼네트워크 기반 코드 LM LoRA 어댑터 동적 생성
- ArcANE (arXiv 2606.05553, ↑42) — 서울대, 롤플레잉 에이전트 캐릭터 일관성 상황 적절성 벤치마크
- TIDE (arXiv 2606.04743, ↑36) — KAIST AI, 템플릿 기반 다수 문제 선제적 발굴 프레임워크
- AdaPlanBench (arXiv 2606.05622, ↑35) — UIUC, LLM 에이전트 적응적 계획 능력 평가 벤치마크
- VideoKR (arXiv 2606.05259, ↑33) — Yale대, 지식·추론 집약적 영상 이해 방법론
- Gemma-4-12B-GGUF (HF DL 458,000) — unsloth Gemma 4 12B GGUF 양자화, 로컬 추론
- Gemma-4-12B (HF DL 315,000) — Google 12B Any-to-Any 멀티모달 인스트럭션 튜닝

**업데이트 (4개)**
- hermes-agent: ⭐147,666 → ⭐184,000 (+25%, 내용 갱신)
- headroom: ⭐7,772 → ⭐15,000 (+93% 단 3일)
- LocateAnything-3B: HF DL 78,925 → 111,000
- Cosmos-3: GitHub 링크 추가 (⭐9,500)

---

## [2026-06-04] ingest | 자동수집 배치 처리 (2026-06-03 ~ 2026-06-04)
- 도메인: ai-news (전체)
- 처리 항목: 총 24개 (신규 페이지 14개 + 업데이트 10개)
- 핵심 인사이트: headroom 토큰 60~95% 압축 + Cosmos 3 NVIDIA 옴니모달 월드 모델 RoboArena 1위 — 비용 최적화(압축·라우팅)와 로봇 AI 월드 모델이 이번 사이클의 두 축
- canvas 업데이트: NO
- actionable 추가: NO

**신규 소스 페이지 생성 (14개)**
- headroom (⭐7,772) — LLM 토큰 60~95% 압축, Library·Proxy·MCP Server
- TrOPD (arXiv 2606.01249) — Samsung Research, 신뢰 구간 온폴리시 증류 불안정성 해결
- Humanoid-GPT (arXiv 2606.03985) — 20억 프레임 GPT형 트랜스포머 휴머노이드 전신 제어, 제로샷 일반화
- MultiDomain-RL-Interference (arXiv 2606.02398) — 멀티도메인 RL 간섭 저차원 충돌 서브스페이스 규명, 수학 57.66→66.04
- PF-OPSD (arXiv 2606.03603) — Tencent, 월드 모델+LLM 구체 추론, VRQABench +10.6%
- AutoMedBench (arXiv 2606.01961) — UC Santa Cruz, 의료 AI 에이전트 5단계 파이프라인 평가
- activepieces (⭐22,557) — AI 에이전트+MCP 서버+워크플로 통합, ~400개 MCP 지원
- manifest-mnfst (⭐6,786) — AI 에이전트 비용/성능 자동 모델 라우팅
- datahub (⭐12,034) — AI 파이프라인 데이터 카탈로그·계보 추적
- Cosmos-3 (arXiv 2606.02800) — NVIDIA 옴니모달 월드 모델, RoboArena 1위, 291인 저자
- DRIFT (arXiv 2606.02060) — NJU, 딥리서치 에이전트 궤적 오류 구간 탐지 +30%p
- OVO-S-Bench (arXiv 2606.03890) — InternLM, 에고센트릭 스트리밍 공간 추론, Gemini 59.2 vs 인간 86.6
- Qwen-Image-Flash (arXiv 2606.03746) — Alibaba, 데이터 레시피 재설계 고속 증류 T2I
- M3Eval (arXiv 2606.05008) — PKU, 인지심리학 기반 MLLM 메모리 평가

**업데이트 (10개)**
- everything-claude-code: ⭐199,631 → 204,673
- hermes-webui: ⭐11,945 → 12,806
- VoxCPM: ⭐24,625 → 25,364
- supermemory: ⭐24,250 → 24,863
- LocateAnything-3B: HF DL 35,800 → 78,925
- LFM2.5-8B: HF DL 37,900 → 60,171 (+성능 수치 추가)
- MiniCPM5-1B: HF DL 45,700 → 68,494 (+학습 방법 추가)
- FunASR: updated 날짜 갱신
- n8n: updated 날짜 갱신
- Qwen3.6-35B-Uncensored: HF DL 2,646,756 (updated 날짜 갱신)

---

## [2026-06-03] wiki | 대기 항목 없음

## [2026-06-01] ingest | 자동수집 배치 처리 (2026-05-31 + 2026-06-01)
- 도메인: ai-news (전체)
- 처리 항목: 총 24개 (신규 페이지 9개 + 업데이트 15개)
- 핵심 인사이트: DeepSeek-V4-Pro HF 다운로드 3.14M→5.89M (2주 만에 88% 증가), everything-claude-code ⭐178K→199K — AI 코딩 에이전트 에코시스템 폭발적 성장 중
- canvas 업데이트: NO
- actionable 추가: NO

**신규 소스 페이지 생성 (9개)**
- liteparse (⭐8,081) — LlamaIndex Rust 기반 고속 로컬 문서 파서, RAG 전처리 특화
- train-llm-from-scratch (⭐3,310) — LLM 처음부터 구현 교육용 가이드
- anthropic-claude-code (⭐129,171) — Anthropic 공식 Claude Code CLI 원천 레포
- project-nomad (⭐27,876) — 오프라인 AI 자급자족 컴퓨터 시스템
- COLLEAGUE-SKILL (HF ↑50) — Shanghai AI Lab 에이전트 스킬 자동 생성
- Representation-Forcing (HF ↑35) — ByteDance Seed 통합 멀티모달 표현 병목 해소
- LongTraceRL (HF ↑28) — Tsinghua KEG 검색 궤적 기반 장문 추론 RL
- SwanVoice (HF ↑25) — ByteDance 모놀로그·다이얼로그 장문 제로샷 TTS
- Function2Scene (HF ↑23) — 기능 사양→3D 실내 씬 자동 생성

**업데이트 (15개)**
- MoneyPrinterTurbo: ⭐67,925→72,712
- markitdown: ⭐128,337→133,359
- VoxCPM: ⭐17,274→23,009
- everything-claude-code (ECC): ⭐193,173→199,631
- AgentDoG: HF ↑97→116
- Qwen-VLA: updated 날짜 갱신
- OmniRetrieval: updated 날짜 갱신
- CollectionLoRA: updated 날짜 갱신
- minWM: updated 날짜 갱신
- DeepSeek-V4-Pro: HF 3.14M→5.89M DL, likes 4,000→4,470
- Qwen3.6-27B: HF 2.45M→5.06M DL, likes 764→1,540
- DeepSeek-V4-Flash: HF 281K→3.48M DL
- LocateAnything-3B: HF 18,300→35,800 DL
- MiniCPM5-1B: HF 28,800→45,700 DL
- LFM2.5-8B: HF 8,850→37,900 DL

---

## [2026-05-29] ingest | GitHub Trending + HF 논문·모델 자동수집 (2026-05-28 ~ 05-29)
- 도메인: ai-news (전체)
- 처리 항목: 총 22개 (신규 19개 + 업데이트 6개)

**신규 소스 페이지 생성 (19개)**

GitHub Trending (2026-05-28):
- milvus (⭐44,495) — 클라우드 네이티브 벡터 DB, RAG 인프라 표준
- Megatron-LM (⭐16,474) — NVIDIA 3D 병렬화 LLM 분산 학습 프레임워크
- FunASR (⭐16,381) — 170배 실시간 ASR + 50개 언어 + 화자분리, OpenAI 호환
- giskard-oss (⭐5,398) — LLM 에이전트 평가·테스트, 환각·편향·취약성 자동 탐지

HF Daily Papers (2026-05-28):
- ProRL (업보트 65) — 능동적 추천 정류 정책 그래디언트 RL, Fudan
- AEPO (업보트 60) — 멀티모달 에이전트 탐색적 정책 최적화, NVIDIA
- PixelsToWords (업보트 48) — 픽셀→텍스트 직접 처리 네이티브 단일 비전 모델
- GammaWorld (업보트 46) — 다중 에이전트 생성적 세계 모델링 (N>2명), NVIDIA
- SelfImprovingLMs (업보트 37) — 양방향 진화적 탐색 LLM 자기 개선, Harvard

HF Trending Models (2026-05-28):
- MiniCPM5-1B (15,600 DL) — OpenBMB 1B 초소형 텍스트 생성, 엣지 최적화
- LongCat-Video-Avatar (좋아요 352) — 미투안 비디오 아바타 생성 v1.5

GitHub Trending (2026-05-29):
- MoneyPrinterTurbo (⭐67,925, +4,698) — AI 쇼트폼 영상 완전 자동화, 당일 최다 상승
- taste-skill (⭐27,221, +2,234) — AI 코드 생성 진부함 억제 에이전트 스킬 파일

HF Daily Papers (2026-05-29):
- AgentDoG (업보트 71) — AI 에이전트 안전·보안 경량 정렬 프레임워크, Shanghai AI Lab
- OmniRetrieval (업보트 45) — 이종 지식 소스 통합 단일 검색, KAIST AI
- CollectionLoRA (업보트 34) — 50 시각효과 → 1 LoRA 다중 교사 증류
- minWM (업보트 27) — 실시간 인터랙티브 비디오 월드 모델 풀스택 OSS
- GenClaw (업보트 21) — 코드 기반 에이전트 이미지 생성 파이프라인 제어, Tencent

HF Trending Models (2026-05-29):
- LFM2.5-8B (8,850 DL) — Liquid AI 8B MoE (활성 1B), 19시간 만에 트렌딩
- LocateAnything-3B (7,860 DL) — NVIDIA 자연어 쿼리 객체 위치 탐색 VLM

**기존 소스 스탯 업데이트 (6개)**
- flash-attention: ⭐23,304 → **23,951**
- Lance: DL 1,910 → **2,510**, 좋아요 943, 트렌딩 1위 달성 (출시 3시간)
- superpowers: ⭐193,260 → **211,716** (+1,730 당일)
- markitdown: ⭐103,007 → **128,337** (+1,410 당일)
- Understand-Anything: ⭐33,131 → **43,637** (+3,776 당일)
- DeepSeek-V4-Pro: HF DL 4.67M → **5.84M**

- canvas 업데이트: NO
- actionable 추가: YES (MoneyPrinterTurbo 영상 자동화 테스트, LocateAnything-3B GUI 에이전트 통합, FunASR 한국어 ASR 테스트, giskard-oss RAG 파이프라인 품질 검증)

**핵심 인사이트**: MoneyPrinterTurbo (⭐67,925, +4,698 당일)가 영상 자동화 오픈소스 레퍼런스로 급부상 — 내 video-saas 파이프라인의 기능 갭 분석 시급. Lance가 출시 3시간 만에 HF 트렌딩 1위로 ByteDance의 멀티모달 통합 전략 가속화 신호.

## [2026-05-28] ingest | 대기 항목 없음

## [2026-05-26] ingest | GitHub Trending + HF 논문·모델 자동수집 (2026-05-26)
- 도메인: ai-news (전체)
- 처리 항목: 총 13개

**GitHub Trending 스탯 업데이트 (5개)**
- everything-claude-code (affaan-m/ECC): ⭐178,846 → **193,173** (+2,025 당일) — Claude Code 에이전트 하네스 지속 성장
- Understand-Anything: ⭐23,045 → **33,131** (+5,604 당일) — 코드베이스 지식 그래프 수요 폭증, 오늘 트렌딩 최대 증가
- andrej-karpathy-skills: ⭐150,477 → **155,977** (+2,749 당일) — CLAUDE.md 표준화 지속 관심
- ai-engineering-from-scratch: ⭐14,302 → **19,554** (+3,154 당일) — AI 엔지니어링 커리큘럼 수요 급등
- Kronos: ⭐25,895 → **26,251** (+245 당일) — 금융 AI 지속 관심 (안정적)

**HF 모델 스탯 업데이트 (2개)**
- Hy-MT2-1.8B: 5,550 → **7,470 DL** — Tencent 번역 모델 채택 증가
- Lance: 438 → **1,910 DL** — ByteDance 멀티모달 모델 초기 성장

**HF 논문 신규 (5개)**
- DVAO (업보트 68) — 다중 보상 RL 분산 적응 어드밴티지 최적화, 멀티리워드 RLVR 안정화
- Macaron-A2UI (업보트 51) — 개인 에이전트 사용자 맥락 기반 생성형 UI 동적 생성
- Foundation Protocol (업보트 50) — AI 에이전트 사회 협력·조율 분산형 프로토콜 레이어
- WBench (업보트 44) — 인터랙티브 비디오 월드 모델 멀티턴 추론·예측 벤치마크
- ParaVT (업보트 28) — 에이전트 비디오 RL 도구 사전 편향 해결

**HF 모델 신규 (1개)**
- Hy-MT2-30B-A3B (2,090 DL) — Tencent 30B MoE (활성 3B) 고품질 번역 서버 배포용

- 추가 페이지: 6개 신규 소스 (DVAO, Macaron-A2UI, Foundation-Protocol, WBench, ParaVT, Hy-MT2-30B-A3B)
- 업데이트 페이지: 7개 스탯 업데이트 + index.md (378 pages, 363 sources)
- 핵심 인사이트: Understand-Anything이 하루 +5,604로 오늘 최대 증가 — 코드베이스를 에이전트가 탐색 가능한 지식 그래프로 변환하는 수요가 실제 트렌드임을 확인. Foundation Protocol + Macaron-A2UI는 모두 "에이전트가 수동 설정이 아닌 맥락을 읽고 동적으로 결정"하는 방향 — 에이전트 자율성 레이어 연구가 2026-05 핵심 주제로 수렴 중.
- canvas 업데이트: NO
- actionable 추가: NO

---

## [2026-05-25] ingest | GitHub Trending + HF 논문·모델 자동수집 (2026-05-24~25)
- 도메인: ai-news (전체)
- 처리 항목: 총 24개 (2026-05-24: 13개 + 2026-05-25: 11개)

**GitHub Trending 스탯 업데이트 (4개)**
- andrej-karpathy-skills: ⭐12,083 → **150,477** (+3,507 당일) — 약 6주 만에 12배 폭발적 성장, CLAUDE.md 커뮤니티 표준화 신호
- codegraph: ⭐3,787 → **20,572** (+2,456 당일) — 1주 만에 5배 급등, AI 코딩 에이전트 코드 그래프 수요 폭증
- multica: ⭐8,427 → **32,822** (+585 당일) — 매니지드 에이전트 플랫폼 안정적 성장
- Kronos: ⭐24,981 → **25,895** — 금융 AI 지속 관심

**GitHub Trending 신규 (5개)**
- Understand-Anything (⭐23,045, +2,299) — 코드베이스 인터랙티브 지식 그래프, Claude/Copilot 공식 연동
- claude-plugins-official (⭐26,877, +2,193) — Anthropic 공식 Claude Code 플러그인 디렉토리
- ai-engineering-from-scratch (⭐14,302, +1,521) — AI 엔지니어링 실무 커리큘럼
- knowledge-work-plugins (⭐14,447, +550) — Anthropic 공식 지식 노동자용 플러그인
- Anthropic-Cybersecurity-Skills (⭐8,709, +930) — 사이버보안 스킬 라이브러리 (커뮤니티, 비공식)

**HF 논문 신규 (10개)**
- DelTA (업보트 191) — RLVR 토큰 그래디언트 재가중, Qwen3 수학 벤치마크 향상
- TransitLM (업보트 167) — 대중교통 경로 1300만건 데이터셋 + LLM 경로 생성
- MLLM-personality-bias (업보트 160) — MLLM 외모 편견 측정 벤치마크
- pi-Bench (업보트 90) — 능동적(proactive) 개인 비서 에이전트 평가
- Full-Attention-to-Sparse (업보트 84) — 100스텝 이내 Sparse Attention 전환
- Lens-Microsoft (업보트 81) — T2I 훈련 효율 재설계
- See-What-I-Mean (업보트 80) — Alibaba 비디오 세밀 객체 이해
- SkillOpt (업보트 75) — Microsoft 에이전트 스킬 자율 진화
- Cross-Layer-Routing-DiT (업보트 61) — DiT 레이어 간 라우팅 개선
- StepAudio-2.5 (업보트 29) — 오디오 AI 기술 보고서

**HF 모델 스탯 업데이트 (3개)**
- Gemma-4-31B: 9.89M → 10.4M DL
- DeepSeek-V4-Pro: 3.44M → 4.67M DL
- Qwen3.6-27B: 3.68M → 4.24M DL

**HF 모델 신규 (3개)**
- HRM-Text-1B (90,000 DL, 트렌딩) — SapientInc 1B 경량 추론
- Marlin-2B (7,290 DL) — 소형 비디오 이해 멀티모달
- Hy-MT2-1.8B (5,550 DL) — Tencent 번역 특화 경량

- 추가 페이지: 18개 신규 소스
- 업데이트 페이지: 7개 스탯 업데이트 + index.md (372 pages, 357 sources)
- 핵심 인사이트: andrej-karpathy-skills의 12K→150K 급등은 CLAUDE.md 기반 에이전트 행동 표준화가 커뮤니티 핵심 관심사임을 확인. Anthropic이 claude-plugins-official + knowledge-work-plugins 두 개의 공식 플러그인 레포를 동시에 운용 — 개발자 vs 지식 노동자 시장 동시 공략. SkillOpt(MS), pi-Bench, Full-Attention-to-Sparse 등 에이전트 자율성·효율성 연구 집중은 다음 경쟁 축이 "얼마나 잘 하는가"→"얼마나 스스로 개선하는가"로 이동하는 신호.
- canvas 업데이트: NO
- actionable 추가: NO

## [2026-05-24] wiki 점검 — 대기 항목 없음

## [2026-05-23] wiki 점검 — 대기 항목 없음

## [2026-05-20] ingest | GitHub Trending + HF 논문·모델 자동수집 (2026-05-20)
- 도메인: ai-news (전체)
- 처리 항목: 총 13개

**GitHub Trending 스탯 업데이트 (5개)**
- ai-agents-for-beginners: ⭐62,967 → 64,744 (+818 오늘)
- CLI-Anything: ⭐37,137 → 38,098 (+1,038 오늘)
- openhuman: ⭐14,939 → 22,625 (+3,973 오늘, 역대 최대 일일 급등)
- agentmemory: ⭐9,289 → 14,564 (+1,609 오늘)
- academic-research-skills: ⭐13,041 → 14,811 (+3,164 오늘)

**HF 논문 신규 (5개)**
- OpenComputer (arXiv 2605.19769, 업보트 43) — Computer-Use 에이전트 검증 가능한 소프트웨어 환경
- GoLongRL (arXiv 2605.19577, 업보트 40) — 멀티태스크 정렬 유지 긴 컨텍스트 RL
- WhenVisionSpeaksForSound (arXiv 2605.16403, 업보트 39) — 시각→오디오 크로스모달 학습
- AutoResearchClaw (arXiv 2605.20025, 업보트 35) — 인간-AI 협업 자기강화 자율 연구
- EnvFactory (arXiv 2605.18703, 업보트 35) — 환경 합성+RL로 도구 사용 에이전트 확장

**HF 모델 스탯 업데이트 (3개)**
- Sulphur-2-base: 1.11M → 1.16M DL
- MiniCPM-V-4.6: 28.6K → 166K DL (폭발적 급증 6배)
- Lance: 업보트 51 → DL 438 (지표 전환)

- 추가 페이지: 5개 신규 소스 (OpenComputer, GoLongRL, WhenVisionSpeaksForSound, AutoResearchClaw, EnvFactory)
- 업데이트 페이지: 8개 스탯 업데이트 + ai-news.md(도메인) + index.md
- 핵심 인사이트: openhuman(⭐22K, +3.97K/day)의 급등은 로컬 프라이버시 AI 에이전트 수요 임계점 도달 신호. MiniCPM-V-4.6 다운로드 6배 급증은 1B 소형 VLM의 실용성을 시장이 인정한 것. 에이전트 평가 인프라(OpenComputer, EnvFactory) 연구 집중은 "에이전트 품질 측정" 문제가 다음 병목임을 시사
- canvas 업데이트: NO
- actionable 추가: NO

---

## [2026-05-19] ingest | GitHub Trending + HF 논문·모델 자동수집 (2026-05-18~19 일괄)
- 도메인: ai-news (전체)
- 처리 항목: 총 26개 (2026-05-18: 13개 + 2026-05-19: 13개)

**2026-05-18 처리 (13개)**
- GitHub Trending 스탯 업데이트 (4개): openhuman (⭐9,634→14,939), scientific-agent-skills (⭐23,434→24,065), Open-Generative-AI (⭐7,902→15,492), ai-agents-for-beginners (⭐58,091→62,967)
- GitHub Trending 신규 (1개): codegraph (⭐3,787, +857, AI 코딩 에이전트 코드 지식 그래프)
- HF 논문 신규 (5개): CiteVQA (업보트 76), MMSkills (69), PhysBrain (52), DexJoCo (39), FashionChameleon (38)
- HF 모델 스탯 업데이트 (3개): Gemma-4-31B (9.12M→9.89M DL), Qwen3.6-35B-A3B (3.86M→5.61M DL), DeepSeek-V4-Pro (3.14M→3.44M DL)

**2026-05-19 처리 (13개)**
- GitHub Trending 스탯 업데이트 (1개): supertonic (⭐6,270→8,556)
- GitHub Trending 신규 (4개): academic-research-skills (⭐13,041), tech-leads-agent-skills (⭐4,231), CLI-Anything (⭐37,137), 12-factor-agents (⭐20,892)
- HF 논문 신규 (5개): LongLive-2.0 (업보트 78), Lance (51), AI-for-Auto-Research (40), KVPO (33), Code-as-Room (24)
- HF 모델 스탯 업데이트 (3개): Qwen3.6-27B (2.45M→3.68M DL), DeepSeek-V4-Flash (281K→2M DL), Sulphur-2-base (875K→1.11M DL)

- 추가 페이지: 15개 신규 소스 (codegraph, CiteVQA, MMSkills, PhysBrain, DexJoCo, FashionChameleon, academic-research-skills, tech-leads-agent-skills, CLI-Anything, 12-factor-agents, LongLive-2.0, Lance, AI-for-Auto-Research, KVPO, Code-as-Room)
- 업데이트 페이지: 11개 (스탯 업데이트) + ai-news.md(도메인) + index.md
- 핵심 인사이트: CLI-Anything(⭐37K) — HKUDS가 "모든 CLI를 에이전트 네이티브화" 하는 프레임워크 공개. chrome-devtools-mcp + n8n-mcp + CLI-Anything = 에이전트 도구 접근 3대 인프라 완성. DeepSeek-V4-Flash 7배 다운로드 급증(281K→2M)은 "속도 > 크기" 실무 선호 재확인
- canvas 업데이트: NO
- actionable 추가: NO

---

## [2026-05-18] wiki check
- 대기 항목 없음

---

## [2026-05-17] ingest | GitHub Trending + HF 논문·모델 자동수집 (2026-05-16~17 일괄)
- 도메인: ai-news (전체)
- 처리 항목: 총 22개 (2026-05-16: 13개 + 2026-05-17: 9개)
  - **2026-05-16 처리**
    - GitHub Trending 스탯 업데이트 (4개): mattpocock-skills (⭐46,841→85,662, **+38,821!**), superpowers (⭐174,963→193,260), RuView (⭐49,992→57,762), openhuman (⭐8,220→9,634)
    - GitHub Trending 신규 (1개): supertonic (Supertone/Krafton, ONNX TTS, ⭐6,270)
    - HF 논문 신규 (1개): Causal Forcing++ (arXiv 2605.15141, 실시간 인터랙티브 영상 생성)
    - HF 논문 이미 처리 (4개): olympiad-reasoning, self-distilled-agentic-rl, MemLens, SANA-WM → 중복 skip
    - HF 모델 스탯 업데이트 (3개): MiniCPM-V-4.6 (22,500→28,600 DL), Sulphur-2-base (784K→875K DL), HiDream-O1-Image (11,700→13,600 DL)
  - **2026-05-17 처리**
    - GitHub Trending 스탯 업데이트 (1개): scientific-agent-skills (⭐22,037→23,434)
    - HF 논문 신규 (4개): darwin-family (2605.14386), llm-multi-agent-survey (2605.14892), WildClawBench (2605.10912), stale-llm-memory (2605.06527)
    - HF 논문 이미 처리 (1개): MemEye → 중복 skip
    - HF 모델 신규 (1개): qwen36-27b-mtp-gguf (185K DL)
    - HF 모델 스탯 업데이트 (1개): DeepSeek-V4-Pro (1.34M→3.14M DL, likes 4,000)
    - supertonic HF 모델 정보 추가: supertonic-3 (20,200 DL, 331 likes)
- 추가 페이지: 7개 | 업데이트 페이지: 11개
  - sources 신규 (7): supertonic, causal-forcing-plus-plus, darwin-family, llm-multi-agent-survey, WildClawBench, stale-llm-memory, qwen36-27b-mtp-gguf
  - sources 스탯 업데이트 (11): mattpocock-skills, superpowers, RuView, openhuman, MiniCPM-V-4.6, Sulphur-2-base, HiDream-O1-Image, scientific-agent-skills, DeepSeek-V4-Pro, supertonic(HF 추가), MemEye(날짜 확인)
- index.md 업데이트: total_pages 323→330, total_sources 308→315
- raw.md 전량 삭제 완료
- 핵심 인사이트:
  1. **mattpocock-skills ⭐46,841→85,662(+86%)**: 약 2.5주 만에 거의 2배 — Claude Code 에이전트 스킬 생태계의 폭발적 성장세 재확인. [[superpowers]](⭐193,260)·[[agent-skills]] 등과 함께 "스킬 레지스트리" 시장 급팽창 중
  2. **STALE 논문 등장**: 에이전트 메모리 연구의 새 방향 — 기억 저장·검색을 넘어 "기억의 신선도 자기인식"으로 진화. [[cognee]]·[[agentmemory]] 등 현재 메모리 시스템의 다음 기능 로드맵 예측 가능
  3. **Qwen3.6-27B-MTP-GGUF 185K DL > Qwen3.6-27B-GGUF 131K DL**: MTP(Multi-Token Prediction) 방식이 로컬 추론 속도 문제의 해결책으로 커뮤니티에서 빠르게 채택 중
- canvas 업데이트: NO
- actionable 추가: NO

---

## [2026-05-15] ingest | GitHub Trending + HF 논문·모델 자동수집 (2026-05-15 일괄)
- 도메인: ai-news (전체)
- 처리 항목: 총 13개 (GitHub Trending 5 + HF 논문 5 + HF 모델 3)
  - **GitHub Trending 신규 (1개)**
    - supervision (roboflow ⭐39,051 +83, YOLO·Transformers·MMDetection 모델 출력 통합 CV 파이프라인)
  - **GitHub Trending 스탯 업데이트 (4개)**
    - Kronos (⭐21,524→⭐24,981 +363, 금융 시계열 파운데이션 모델)
    - scientific-agent-skills (⭐21,394→⭐22,037 +643, 과학·공학·금융 에이전트 스킬)
    - agentmemory (⭐8,382→⭐9,289 +1,879, AI 에이전트 영속 메모리)
    - openhuman (⭐6,774→⭐8,220 +3,329, Rust 로컬 AI 에이전트)
  - **HF 논문 신규 (5개)**
    - olympiad-reasoning (arXiv 2605.13301, 업보트 104 — 단순 스케일링 수학 올림피아드 금메달)
    - self-distilled-agentic-rl (arXiv 2605.15155, 업보트 48 — 에이전트 RL 자기 증류)
    - MemEye (arXiv 2605.15128, 업보트 46 — 멀티모달 에이전트 시각 메모리 평가)
    - SANA-WM (arXiv 2605.15178, 업보트 41 — NVIDIA 선형 확산 트랜스포머 월드 모델링)
    - MemLens (arXiv 2605.14906, 업보트 38 — NVIDIA VLM 장기 멀티모달 메모리 벤치마크)
  - **HF 모델 신규 (1개)**
    - HiDream-O1-Image (HiDream-ai 9B I2I, 11,700 DL, 트렌딩 3위)
  - **HF 모델 스탯 업데이트 (2개)**
    - Sulphur-2-base (627K→784K DL, +25%, 트렌딩 점수 943)
    - MiniCPM-V-4.6 (16,800→22,500 DL, 트렌딩 점수 540)
  - **index.md 업데이트**: total_pages: 316→323, total_sources: 301→308
  - **raw.md 전량 삭제 완료**
- 추가 페이지: 7개 | 업데이트 페이지: 6개
  - sources 신규 (7): supervision, olympiad-reasoning, self-distilled-agentic-rl, MemEye, SANA-WM, MemLens, HiDream-O1-Image
  - sources 스탯 업데이트 (6): Kronos, scientific-agent-skills, agentmemory, openhuman, Sulphur-2-base, MiniCPM-V-4.6
- 핵심 인사이트: 같은 날 MemEye(업보트 46)·MemLens(업보트 38) 동시 발표 — **멀티모달 에이전트의 시각 장기 메모리 평가 표준화 경쟁이 2026-05-15에 시작됨**. openhuman ⭐6,774→8,220(+3,329/day)은 로컬 AI 에이전트 수요 폭발 지속 확인. SANA-WM(NVIDIA 선형 확산 트랜스포머)는 [[Mamba4]] 방향과 수렴하며 "Transformer 이분법을 넘어선 선형 복잡도 하이브리드 아키텍처"가 2026-05 연구 주류임을 재확인.
- canvas 업데이트: NO
- actionable 추가: NO

---

## [2026-05-14] ingest | GitHub Trending + HF 논문·모델 자동수집 (2026-05-14 일괄)
- 도메인: ai-news (전체)
- 처리 항목: 총 13개 (GitHub Trending 5 + HF 논문 5 + HF 모델 3)
  - **GitHub Trending 신규 (3개)**
    - openhuman (tinyhumansai ⭐6,774 +1,696, Rust 기반 로컬 개인 AI 에이전트)
    - scientific-agent-skills (K-Dense-AI ⭐21,394 +99, 과학·공학·금융 분야별 AI 에이전트 스킬)
    - Personal_AI_Infrastructure (danielmiessler ⭐13,581 +435, 개인 AI 인프라 TypeScript)
  - **GitHub Trending 스탯 업데이트 (2개)**
    - agentmemory (⭐3,715→⭐8,382 +1,379/day, +125% 이후), llms-from-scratch (⭐94,100→⭐94,675 +821/day)
  - **HF 논문 신규 (5개)**
    - MulTaBench (arXiv 2605.10616, upvotes 67 — 멀티모달 테이블 벤치마크)
    - MinT (arXiv 2605.13779, upvotes 65 — 대규모 LLM 관리형 인프라)
    - AnyFlow (arXiv 2605.13724, upvotes 59 — NVIDIA 임의 스텝 영상 확산 모델)
    - Long-Context-VLM-Training (arXiv 2605.13831, upvotes 43 — ByteDance 128K+ 컨텍스트 VLM)
    - AI-Agent-Decision-Prediction (arXiv 2605.12411, upvotes 31 — 에이전트 결정 예측)
  - **HF 모델 신규 + 스탯 업데이트 (3개)**
    - MiniCPM-V-4.6 신규 (OpenBMB 1B VLM, 16.8K DL), Sulphur-2-base (535K→627K DL, +17%), ZAYA1-8B (110K→131K DL, +19%)
  - **index.md 업데이트**: total_pages: 307→316, total_sources: 292→301
  - **raw.md 전량 삭제 완료**
- 추가 페이지: 9개 | 업데이트 페이지: 5개
  - sources 신규 (9): openhuman, scientific-agent-skills, Personal_AI_Infrastructure, MulTaBench, MinT, AnyFlow, Long-Context-VLM-Training, AI-Agent-Decision-Prediction, MiniCPM-V-4.6
  - sources 스탯 업데이트 (4): agentmemory, llms-from-scratch, ZAYA1-8B, Sulphur-2-base
- 핵심 인사이트: Rust 기반 로컬 AI 에이전트(openhuman, +1,696/day)의 첫 대형 트렌딩은 **AI 에이전트의 성능·안전성·프라이버시 3요소 결합** 수요의 새 신호. NVIDIA AnyFlow(임의 스텝 영상 생성)는 영상 SaaS 품질-속도 트레이드오프를 사용자가 직접 제어할 수 있는 시대를 예고.
- canvas 업데이트: NO (대규모 변경 없음)
- actionable 추가: NO

---

## [2026-05-13] ingest | GitHub Trending + HF 논문·모델 자동수집 (2026-05-13 일괄)
- 도메인: ai-news (전체), local-llm (부)
- 처리 항목: 총 13개 (GitHub Trending 5 + HF 논문 5 + HF 모델 3)
  - **GitHub Trending 신규 (3개)**
    - llms-from-scratch (rasbt ⭐94,100 +772, PyTorch LLM 처음부터 구현 교육 레포)
    - litellm (BerriAI ⭐46,782 +147, 100+ LLM API 단일 인터페이스)
    - ai-trader (HKUDS ⭐16,888 +229, 에이전트 기반 완전자동 LLM 트레이딩)
  - **GitHub Trending 스탯 업데이트 (2개)**
    - hermes-agent (⭐87K→⭐147,666 +2,465, 약 4주간 +69%), hello-agents (⭐47,169→⭐48,745 +599)
  - **HF 논문 신규 (5개)**
    - sensenova-u1 (arXiv 2605.12500, 업보트 1,580 — NEO-unify 멀티모달 통합)
    - memprivacy (arXiv 2605.09530, 업보트 86 — 에이전트 메모리 프라이버시)
    - delta-mem (arXiv 2605.12357, 업보트 65 — LLM 온라인 메모리 효율화)
    - rubricem (arXiv 2605.10899, 업보트 56 — Google 루브릭 기반 메타-RL)
    - world-action-models (arXiv 2605.12090, 업보트 34 — Embodied AI WAM 패러다임)
  - **HF 모델 스탯 업데이트 (3개)**
    - DeepSeek-V4-Pro (1.34M→2.42M DL, +81%), Sulphur-2-base (144K→535K DL, +271%), ZAYA1-8B (44.8K→110K DL, +145%)
  - **index.md 업데이트**: total_pages: 299→307, total_sources: 284→292
  - **raw.md 전량 삭제 완료**
- 추가 페이지: 8개 | 업데이트 페이지: 5개
  - sources 신규 (8): llms-from-scratch, litellm, ai-trader, sensenova-u1, memprivacy, delta-mem, rubricem, world-action-models
  - sources 스탯 업데이트 (5): hermes-agent, hello-agents, DeepSeek-V4-Pro, Sulphur-2-base, ZAYA1-8B
- 핵심 인사이트: hermes-agent ⭐87K→⭐147K(+69% 4주) — NousResearch 에이전트 프레임워크가 단순 트렌딩을 넘어 **커뮤니티 표준 에이전트 인프라**로 자리잡는 중. SenseNova-U1 업보트 1,580은 "이해+생성 단일 통합 모델" 방향이 2026년 멀티모달 AI의 핵심 레이스임을 확인. Sulphur-2-base(144K→535K, +271%) 급등은 오픈소스 텍스트→비디오 모델에 대한 폭발적 수요를 보여줌.
- canvas 업데이트: NO
- actionable 추가: NO

---

## [2026-05-12] wiki-check | 대기 항목 없음
- raw.md 확인 결과 인제스트 대기 항목 없음

---

## [2026-05-11] ingest | GitHub Trending + HF 논문·모델 자동수집 (2026-05-11 일괄)
- 도메인: ai-news (전체), local-llm (부), video-saas (부)
- 처리 항목: 총 13개 (GitHub Trending 5 + HF 논문 5 + HF 모델 3)
  - **GitHub Trending 신규 (2개)**
    - everything-claude-code(affaan-m ⭐178,846 +1,081, AI 코딩 에이전트 통합 하네스)
    - omlx(jundot ⭐13,485 +185, Apple Silicon LLM 추론 서버 + SSD 캐싱)
  - **GitHub Trending 스탯 업데이트 (3개)**
    - financial-services(⭐17,876→19,584 +1,449), hello-agents(⭐45,203→47,169 +748 → *(UPDATED)*), UI-TARS-desktop(⭐31,655→32,567 +669)
  - **HF 논문 신규 (5개)**
    - R3-SQL(arXiv 2604.25325, BIRD-dev 75.03% Text-to-SQL SOTA)
    - mean-mode-screaming(arXiv 2605.06169, DiT MMS 현상 규명 + 1000층 안정화)
    - MACE-Dance(arXiv 2512.18181, 음악→댄스 영상 MoE 캐스케이드 SOTA)
    - Gated-QKAN-FWP(arXiv 2605.06734, 양자 영감 FWP 12.5k 파라미터)
    - DTap(arXiv 2605.04808, AI 에이전트 레드팀 플랫폼 14개 도메인)
  - **HF 모델 스탯 업데이트 (3개)**
    - Gemma-4-31B(8.89M→9.12M DL), Qwen3.6-35B-A3B(3.51M→3.86M DL), Qwen3.6-27B(1.77M→2.45M DL)
  - **index.md 업데이트**: total_pages: 292→299, total_sources: 277→284
  - **raw.md 전량 삭제 완료**
- 추가 페이지: 7개 | 업데이트 페이지: 6개
  - sources 신규 (7): everything-claude-code, omlx, R3-SQL, mean-mode-screaming, MACE-Dance, Gated-QKAN-FWP, DTap
  - sources 스탯 업데이트 (6): financial-services, hello-agents, UI-TARS-desktop, Gemma-4-31B, Qwen3.6-35B-A3B, Qwen3.6-27B
- 핵심 인사이트: everything-claude-code ⭐178,846이 GitHub Trending 1위 — "AI 코딩 에이전트 설정 하네스"가 단순 개인 CLAUDE.md 공유를 넘어 커뮤니티 표준 자료집으로 자리잡았음 확인. DTap(14개 도메인 에이전트 레드팀 자동화)과 mean-mode-screaming(1000층 DiT 안정화)는 각각 에이전트 보안/영상 생성 스케일업 두 축의 인프라 연구가 성숙 단계 진입했음을 시사. Qwen3.6-27B 1.77M→2.45M DL(+38% 4일) — 덴스 27B가 MoE 35B/3B 대비 실사용 편의성으로 수요 급증.
- canvas 업데이트: NO
- actionable 추가: NO

---

## [2026-05-10] ingest | GitHub Trending + HF 논문·모델 자동수집 (2026-05-09 + 2026-05-10 통합 일괄)
- 도메인: ai-news (전체), local-llm (부)
- 처리 항목: 총 25개 (2026-05-09: 13개 + 2026-05-10: 12개)
  - **신규 소스 파일 생성 (9개)**
    - hello-agents(Datawhale ⭐45,203, 에이전트 튜토리얼 중문), CloakBrowser(⭐3,551, 봇감지 우회 Chromium)
    - Skill1-Unified-Evolution(arXiv 2605.06130, upvote 58, RL 스킬 자동 진화)
    - Beyond-Semantic-Similarity-Agentic-Search(arXiv 2605.05242, upvote 58, 에이전틱 검색 재정의)
    - UI-TARS-desktop(ByteDance ⭐31,655, 멀티모달 에이전트 데스크탑), agentmemory(⭐3,715, 영속 메모리)
    - SkillOS(arXiv 2605.06614, upvote 32, 자율 스킬 큐레이션)
    - Judge-Orchestrated-LLM-Ensemble(arXiv 2605.04523, upvote 38), Audio-Visual-Intelligence(arXiv 2605.04045, upvote 26)
  - **스탯 업데이트 (11개)**
    - agent-skills(31K→36.5K), DeepSeek-TUI(20.6K→22.6K), local-deep-research(6.5K→6.9K)
    - Gemma-4-31B(8.21M→8.89M DL), Qwen3.6-35B-A3B(3.21M→3.51M DL), Qwen3.6-35B-A3B-GGUF(2.1M→2.58M DL)
    - financial-services(13K→17.9K), dive-into-llms(31.7K→36.7K)
    - Sulphur-2-base(93K→144K DL), ZAYA1-8B(6.8K→44.8K DL), DeepSeek-V4-Pro(1.06M→1.34M DL)
  - **이미 처리된 항목 (5개)** — 이전 배치에서 완료, raw.md에서만 제거
    - MiA-Signature, MARBLE, continuous-latent-diffusion-lm, when-to-trust-imagination, nonsense-helps
  - **index.md 업데이트**: total_pages: 283→292, total_sources: 268→277
  - **raw.md 전량 삭제 완료**
- 핵심 인사이트: 같은 날 Skill1(2605.06130)과 SkillOS(2605.06614) 두 논문이 동시 등장 — "에이전트가 스킬을 스스로 큐레이션·진화"가 2026년 5월 AI 연구 핵심 트렌드. 수동 스킬 설계([[agent-skills]] 36K star) 시대와 자율 진화 시대가 동시에 존재하는 전환점.
- canvas 업데이트: NO
- actionable 추가: NO

## [2026-05-09] ingest | 대기 항목 없음

## [2026-05-08] ingest | GitHub Trending + HF 논문·모델 자동수집 (2026-05-08 일괄)
- 도메인: ai-news (전체), local-llm (부)
- 처리 항목: 총 13개 (GitHub Trending 5 + HF 논문 5 + HF 모델 3)
  - **GitHub Trending 신규 (4개)**
    - financial-services(Anthropic 공식, ⭐13,013 +1,343), local-deep-research(⭐6,480 +559), TabPFN(⭐6,859 +230), dflash(⭐3,617 +671)
  - **GitHub Trending 업데이트 (1개)**
    - DeepSeek-TUI(⭐16,640→20,630 +5,799)
  - **HF 논문 신규 (5개)**
    - MiA-Signature(2605.06416, Tencent 긴 컨텍스트), MARBLE(2605.06507, 디퓨전 RL 보상 균형), continuous-latent-diffusion-lm(2605.06548, 연속 잠재 디퓨전 LM), when-to-trust-imagination(2605.06222, 세계 모델 신뢰 판단), nonsense-helps(2605.05566, 프롬프트 노이즈 추론 향상)
  - **HF 모델 신규 (1개)**
    - ZAYA1-8B(Zyphra, 6,810 DL)
  - **HF 모델 업데이트 (2개)**
    - DeepSeek-V4-Pro(786,631→1.06M DL), Sulphur-2-base(55,500→93,000 DL)
- 추가 페이지: 10개 | 업데이트 페이지: 3개
  - sources 신규 (10): financial-services, local-deep-research, TabPFN, dflash, MiA-Signature, MARBLE, continuous-latent-diffusion-lm, when-to-trust-imagination, nonsense-helps, ZAYA1-8B
  - sources 스탯 업데이트 (3): DeepSeek-TUI(⭐20,630), DeepSeek-V4-Pro(1.06M DL), Sulphur-2-base(93K DL)
  - index.md 업데이트 (total_pages: 273→283, total_sources: 258→268)
  - raw.md 전량 삭제 완료
- 핵심 인사이트: Anthropic이 금융 서비스 공식 레포(⭐13,013)를 직접 공개 — 금융을 Claude 핵심 엔터프라이즈 버티컬로 공식화. DeepSeek-TUI ⭐4,990→20,630(+313% 4일)는 "터미널 AI 에이전트" 수요가 DeepSeek 생태계로 완전히 확산됐음을 확인. nonsense-helps는 프롬프트 노이즈가 추론 탐색 공간을 넓힌다는 반직관적 발견 — 즉시 현재 워크플로우에 적용 실험 가치 있음.
- canvas 업데이트: NO
- actionable 추가: NO

---

## [2026-05-07] ingest | GitHub Trending + HF 논문·모델 자동수집 (2026-05-06~07 일괄)
- 도메인: ai-news (전체), slam-3dgs (부), video-saas (부)
- 처리 항목: 총 26개 (GitHub 8 + HF 논문 10 + HF 모델 8)
  - **2026-05-06 배치 (13개)**
    - GitHub Trending 신규: agency-agents(⭐94,058), context-mode(⭐13,388), awesome-ai-apps(⭐11,694), cocoindex(⭐8,544)
    - GitHub Trending 업데이트: Pixelle-Video(⭐10,421→12,394)
    - HF 논문 신규: PRISM(업보트 30), X2SAM(업보트 14), WindowsWorld(업보트 9), HeavySkill(업보트 6), PatRe(업보트 4)
    - HF 모델 업데이트: DeepSeek-V4-Pro(535K→786,631 DL), openai-privacy-filter(133K→155,500 DL)
    - HF 모델 신규: Sulphur-2-base(55,500 DL)
  - **2026-05-07 배치 (13개)**
    - GitHub Trending 신규: agent-skills(⭐31,833)
    - GitHub Trending 업데이트: DeepSeek-TUI(⭐4,990→16,640), ruflo(⭐42,196→45,632), dexter(⭐23,393→24,565), deer-flow(⭐62,817→65,770)
    - HF 논문 신규: Stream-R1(업보트 96), Stream-T1(업보트 84), RLDX-1(업보트 66), HERMES++(업보트 63), PhysForge(업보트 20)
    - HF 모델 업데이트: Qwen3.6-35B-A3B(2.88M→3.21M DL), Qwen3.6-27B(1.46M→1.77M DL)
    - HF 모델 신규: LTX2.3-10Eros(28,215 DL)
- 추가 페이지: 17개 | 업데이트 페이지: 9개
  - sources 신규 (17): agency-agents, context-mode, awesome-ai-apps, cocoindex, PRISM, X2SAM, WindowsWorld, HeavySkill, PatRe, Sulphur-2-base, agent-skills, Stream-R1, Stream-T1, RLDX-1, HERMES-plus-plus, PhysForge, LTX2.3-10Eros
  - sources 스탯 업데이트 (9): Pixelle-Video, DeepSeek-V4-Pro, openai-privacy-filter, DeepSeek-TUI, ruflo, dexter, deer-flow, Qwen3.6-35B-A3B, Qwen3.6-27B
  - index.md 업데이트 (total_pages: 256→273, total_sources: 241→258)
  - raw.md 전량 삭제 완료
- 핵심 인사이트: agency-agents ⭐94,058은 "멀티에이전트 에이전시(역할·프로세스·결과물 명세화)" 패러다임이 2026-05 최대 수요임을 확인. DeepSeek-TUI ⭐4,990→16,640(+233% 하루)은 "터미널 AI 에이전트" 수요 폭발적 성장 지속. Stream-R1(업보트 96)·Stream-T1(업보트 84)은 "스트리밍 T2V + RL/TTS" 결합 연구가 video-saas 차세대 기술 방향임을 시사. cocoindex 증분 처리 패턴은 wiki 자동 수집 파이프라인 효율화에 직접 적용 가능.
- canvas 업데이트: NO
- actionable 추가: NO

---

## [2026-05-06] ingest | GitHub Trending + HF 논문·모델 자동수집 (2026-05-05 일괄)
- 도메인: ai-news (전체)
- 처리 항목: 총 13개 (GitHub Trending 5 + HF 논문 5 + HF 모델 3)
- 추가 페이지: 6개 | 업데이트 페이지: 7개
  - sources 신규 (6): dexter, MolmoAct2, From-Context-to-Skills, OceanPile, ComboStoc, AcademiClaw
  - sources 스탯 업데이트 (7): ruflo(⭐37,284→42,196 +2,598), TradingAgents(⭐63,735→68,332 +2,182), DeepSeek-TUI(⭐2,827→4,990 +1,274), jcode(⭐3,057→4,043 +548), Qwen3.6-27B(906K→1.46M DL), Qwen3.6-35B-A3B(2.6M→2.88M DL), Gemma-4-31B(8.2M→8.21M DL)
  - index.md 업데이트 (total_pages: 250→256, total_sources: 235→241)
  - raw.md 전량 삭제 완료
- 핵심 인사이트: TradingAgents ⭐68,332(+4,597/이틀)·ruflo ⭐42,196(+4,912/3일) 지속 급성장 — "금융 멀티에이전트"와 "Claude 네이티브 오케스트레이션"이 2026-05 GitHub 최고 수요 카테고리. DeepSeek-TUI ⭐2,827→4,990(76% 이틀 성장)는 "터미널 AI 에이전트" 수요가 DeepSeek 생태계로도 확산 중임을 확인. From-Context-to-Skills 논문(업보트 58)은 에이전트 스킬 ICL 일반화 한계를 체계적으로 분석 — 스킬 시스템 설계 시 파인튜닝 없는 ICL 단독 의존 경계 필요.
- canvas 업데이트: NO
- actionable 추가: NO

---

## [2026-05-05] 대기 항목 없음

---

## [2026-05-04] ingest | GitHub Trending + HF + arXiv 자동수집 (2026-05-03~04 일괄)
- 도메인: ai-news (주), slam-3dgs (부)
- 처리 항목: 총 26개 (GitHub Trending 9 + arXiv 논문 10 + HF 모델 7)
- 추가 페이지: 16개 | 업데이트 페이지: 9개
  - sources 신규 (16): ruflo, browserbase-skills, n8n-mcp, ouroboros, DeepSeek-TUI, Nemotron-3-Nano-Omni, Step-level-Optimization, ViPO, Semi-DPO, FlashRT, UniVidX, Learning-while-Deploying, Skill-Text-to-Skill-Structure, Map2World, Online-Self-Calibration-VLMs, Mistral-Medium-3.5-128B
  - sources 스탯 업데이트 (9): TradingAgents(⭐58,379→63,735), Pixelle-Video(⭐5,983→10,421), VoxCPM(⭐14,227→17,274), jcode(⭐2,014→3,057), Gemma-4-31B(2.89M→8.2M DL), Qwen3.6-35B-A3B(1.18M→2.6M DL), Qwen3.6-35B-A3B-GGUF(1.11M→2.1M DL), DeepSeek-V4-Pro(321K→535K DL), openai-privacy-filter(82.9K→133K DL)
  - index.md 업데이트 (total_pages: 234→250, total_sources: 219→235)
  - raw.md 전량 삭제 완료
- 핵심 인사이트: TradingAgents ⭐63,735(+5,356/3일)·Pixelle-Video ⭐10,421(+4,438/3일)의 폭발적 성장 — "금융 멀티에이전트"와 "쇼트폼 영상 자동화 오픈소스"가 2026-05 최고 수요. Learning-while-Deploying(실배포 중 RL로 95% 성공률)은 "배포=학습 종료" 고정관념을 깨는 이정표. Gemma-4-31B가 2.89M→8.2M DL(2.8배 급성장)로 오픈소스 멀티모달 VLM 표준 모델로 굳어지는 중. n8n-mcp ⭐19,680은 "자연어로 n8n 자동화" 수요가 폭발적임을 확인.
- canvas 업데이트: NO
- actionable 추가: NO

---

## [2026-05-03] wiki | 대기 항목 없음
- 대기 항목 없음

---

## [2026-05-01] ingest | GitHub Trending + HF 자동수집 (2026-05-01 일괄)
- 도메인: ai-news (주), local-llm (부), slam-3dgs (부)
- 처리 항목: 총 13개 (GitHub Trending 5 + HF 논문 5 + HF 모델 3)
- 추가 페이지: 7개 | 업데이트 페이지: 6개
  - sources 신규 (7): craft-agents-oss, jcode, Claw-Eval-Live, RoundPipe, LenVM, Edit-R1, ExoActor
  - sources 스탯 업데이트 (6): superpowers(⭐147K→174,963), TradingAgents(⭐54,163→58,379), warp-terminal(⭐46,560→50,282), Qwen3.6-27B(509K→906,859 DL), DeepSeek-V4-Pro(272K→321,492 DL), DeepSeek-V4-Flash(199K→281,356 DL)
  - index.md 업데이트 (total_pages: 227→234, total_sources: 212→219)
  - raw.md 전량 삭제 완료
- 핵심 인사이트: Claw-Eval-Live의 66.7% 통과율 — 2026-05 현재 최강 프론티어 모델도 워크플로우 태스크의 1/3을 실패. 에이전트 파이프라인 설계 시 실패 핸들링은 선택이 아닌 필수. RoundPipe(RTX 4090 8장 → 235B LoRA 파인튜닝)는 "클라우드 없이 대형 모델 파인튜닝" 현실화의 이정표. Qwen3.6-27B가 509K→906,859 DL로 1주일 만에 2배 급성장 — Qwen3.6 시리즈가 오픈소스 멀티모달 기준 모델로 확고히 자리잡는 추세.
- canvas 업데이트: NO
- actionable 추가: NO

---

## [2026-05-01] ingest | 대기 항목 없음

---

## [2026-04-29] ingest | GitHub Trending + HF 자동수집 (2026-04-29 일괄)
- 도메인: ai-news (주)
- 처리 항목: 총 13개 (GitHub Trending 5 + HF 논문 5 + HF 모델 3)
- 추가 페이지: 9개 | 업데이트 페이지: 4개
  - sources 신규 (9): daily-stock-analysis, recursive-multi-agent, DV-World, test-driven-data-engineering, refinement-via-regeneration, meta-cot-image-editing, Qwen3-0.6B, Qwen2.5-7B-Instruct, DeepSeek-V3.2
  - sources 스탯 업데이트 (4): VibeVoice(⭐43,576→45,300 +1,483), TradingAgents(⭐54,163→54,500 +932), GitNexus(⭐32,105→32,900 +1,607), awesome-codex-skills(⭐1,960→4,386 +953)
  - index.md 업데이트 (total_pages: 212→221, total_sources: 197→206)
  - raw.md 전량 삭제 완료
- 핵심 인사이트: GitNexus(+1,607 당일)·VibeVoice(+1,483 당일)의 급성장 — 코드 지식 그래프 + 로컬 음성 AI가 2026-04 최대 관심사. Qwen3-0.6B(18.5M DL/월)·Qwen2.5-7B-Instruct(12.8M DL/월)·DeepSeek-V3.2(11.3M DL/월) — 엣지/로컬 추론 수요가 압도적으로 커지는 중. daily-stock-analysis(LLM+멀티채널 주식 분석)는 금융-AI 도메인 실전 적용 패턴의 표준화 사례.
- canvas 업데이트: NO
- actionable 추가: NO

---

## [2026-04-28] ingest | GitHub Trending + HF 자동수집 (2026-04-28 일괄)
- 도메인: ai-news (주)
- 처리 항목: 총 14개 (GitHub Trending 5 + HF 논문 5 + HF 모델 3 + 스탯 업데이트 1)
- 추가 페이지: 6개 | 업데이트 페이지: 8개
  - sources 신규 (6): DeepSeek-V3, ClawMark, SkillsToTalent, World-R1, ReVSI, VLA-Safety
  - sources 스탯 업데이트 (8): VibeVoice(GitHub 43K 공개 → reliability 상향), TradingAgents(GitHub ⭐54,163 추가), mattpocock-skills(⭐23,518→32,812), GitNexus(⭐30,152→32,105), Qwen3.6-27B(330K→509K DL), DeepSeek-V4-Pro(174K DL 추가), openai-privacy-filter(1.9K→57.7K DL)
  - 이미 최신 상태 스킵 (없음)
  - index.md 업데이트 (total_pages: 206→212, total_sources: 191→197)
  - raw.md 전량 삭제 완료
  - ai-news.md 도메인 업데이트 없음 (스탯 업데이트 위주)
- 핵심 인사이트: microsoft/VibeVoice(⭐43K)로 VibeVoice가 논문→오픈소스 코드 공개 완료 — ElevenLabs 대체 실험 가능한 단계. mattpocock/skills(+5,645 당일, 총 32K)는 AI 코딩 스킬 생태계에서 TypeScript/프론트엔드 벡터가 빠르게 성장 중. DeepSeek-V3(⭐103K 돌파)가 오픈소스 LLM 기준점으로 고착화 — V3→V4-Pro 시리즈가 중국 AI 최전선. SkillsToTalent(조직 구조로 에이전트 성능 향상)는 TradingAgents의 "역할 분리 패러다임"을 일반화.
- canvas 업데이트: NO
- actionable 추가: YES (VibeVoice 로컬 테스트 → ElevenLabs 대체 실험 즉시 가능)

---

## [2026-04-27] ingest | GitHub Trending + HF 자동수집 (2026-04-26~27 일괄)
- 도메인: ai-news (주)
- 처리 항목: 총 27개 (GitHub Trending 9 + HF 논문 10 + HF 모델 8)
- 추가 페이지: 10개 | 업데이트 페이지: 7개
  - sources 신규 (10): rlm, mattpocock-skills, trycua-cua, beads, awesome-codex-skills, GitNexus, VLAA-GUI, TingIS, Context-Unrolling, DeepSeek-V4-Flash
  - sources 스탯 업데이트 (7): free-claude-code(⭐10,167→12,012), ml-intern(⭐5,743→6,473), Kronos(⭐17,996→21,524), open-webui(⭐133,530→134,166), Kimi-K2.6(292K→376K DL), Qwen3.6-27B(258K→330K DL), Qwen3.6-35B-A3B(583K→1.18M DL)
  - 이미 인덱스 등재·파일 존재 스킵 (10): LLaTiSA, WorldMark, UniT-Humanoid-Policy, StyleID-Facial-Identity, Co-Evolving-LLM-Agents, Seeing-Fast-and-Slow, Hybrid-Policy-Distillation, DeepSeek-V4-Pro, openai-privacy-filter, Qwen3.6-35B-A3B
  - index.md 업데이트 (total_pages: 196→206, total_sources: 181→191)
  - raw.md 전량 삭제 완료
  - ai-news.md 도메인 2026-04-26/27 섹션 추가
- 핵심 인사이트: mattpocock/skills(+2,519 당일)·awesome-codex-skills(+517)·awesome-agent-skills(기존) — 에이전트 스킬 허브가 Claude/Codex/다중 플랫폼별로 독립 형성되며 플랫폼 선택이 스킬 생태계 선택으로 연결되는 잠금 효과 발생. GitNexus(⭐30K, 서버리스 코드 지식 그래프)는 프라이버시 친화적 코드 인텔리전스의 첫 대형 후보. Qwen3.6-35B-A3B 다운로드 583K→1.18M(+102%)은 MoE 효율 구조가 로컬 추론 표준으로 굳어지는 중.
- canvas 업데이트: NO
- actionable 추가: NO (mattpocock-skills .claude/ 통합·GitNexus 테스트 기존 목록에 흡수)

## [2026-04-26] check | 대기 항목 없음
- raw.md 확인 결과 인제스트 대기 항목 없음

## [2026-04-25] ingest | GitHub Trending + HF 자동수집 (2026-04-25 일괄)
- 도메인: ai-news (주)
- 처리 항목: 총 13개 (GitHub Trending 5 + HF 논문 5 + HF 모델 3)
- 추가 페이지: 4개 | 업데이트 페이지: 5개
  - sources 신규 (4): Open-Generative-AI, DeepEP, LLaTiSA, Co-Evolving-LLM-Agents
  - sources 스탯 업데이트 (5): free-claude-code(⭐6,208→10,167), ml-intern(⭐4,371→5,743), claude-context(⭐6,953→9,167), Kimi-K2.6(54K→292K DL), Qwen3.6-27B(510→764 likes, 258K DL)
  - 이미 인덱스 등재·파일 존재 스킵 (4): WorldMark, UniT-Humanoid-Policy, StyleID-Facial-Identity, DeepSeek-V4-Pro
  - index.md 업데이트 (total_pages: 192→196, total_sources: 177→181)
  - raw.md 전량 삭제 완료
  - ai-news.md 도메인 2026-04-25 섹션 추가
- 핵심 인사이트: free-claude-code가 하루 만에 6K→10K 스타 돌파 + ml-intern GitHub Trending 진입(+2,985) — Claude Code 무료화 수요와 HuggingFace 에이전트 생태계가 동시에 폭발. DeepEP(DeepSeek MoE expert-parallel 통신 최적화)는 DeepGEMM에 이은 MoE 인프라 오픈소스화 시리즈 2탄 — MoE가 표준이 될수록 이 스택의 가치 상승. Co-Evolving-LLM-Agents(에이전트+스킬 뱅크 공진화)는 SkillClaw와 함께 에이전트 자기진화가 연구 주류임을 재확인.
- canvas 업데이트: NO
- actionable 추가: NO (Open-Generative-AI 로컬 테스트 기존 목록에 흡수, DeepEP + DeepGEMM 조합 테스트 기존 인프라 목록에 흡수)

---

## [2026-04-23] ingest | GitHub Trending + HF 자동수집 (2026-04-23 일괄)
- 도메인: ai-news (주), video-saas 교차 (Pixelle-Video, ReImagine), slam-3dgs 교차 (Spatial-Intelligence, DeVI), local-llm 교차 (Qwen3.6-27B, Qwen3.6-27B-GGUF)
- 처리 항목: 총 33개 (GitHub Trending 13 + HF 논문 10 + HF 모델 10)
- 추가 페이지: 14개 | 업데이트 페이지: 12개
  - sources 신규 (14 파일, 24개 항목):
    - 개별 파일 (13): open-webui, langfuse, claude-code-templates, last30days-skill, vercel-skills, swarms, Pixelle-Video, shannon, LLaDA2.0-Uni, DR-Venus, Qwen3.6-27B, openai-privacy-filter, Qwen3.6-27B-GGUF
    - 배치 파일 (1): 2026-04-23-papers-batch (Near-Future-Policy-Optimization, Reward-Hacking-Large-Models, Spatial-Intelligence-Generative, WavAlign, SWE-chat, Scaling-Test-Time-Agentic-Coding, ReImagine, Cortex-2.0, DeVI 9개 포함)
  - sources 스탯 업데이트 (12): RAG-Anything(⭐17,722), claude-context(⭐7,857), worldmonitor(⭐51,894), TrendRadar(⭐54,687), RuView(⭐49,483), Qwen3.6-35B-A3B(583K DL), Kimi-K2.6(54.5K DL), HY-World-2.0(557 likes), Gemma-4-31B(5.1M DL), GLM-5.1(183K DL, 1.47K likes)
  - 미처리 스킵 (2): MiniMax-M2.7(416K — 변화 없음), Qwen3.6-35B-A3B-GGUF(1.1M — 변화 없음)
  - index.md 업데이트 (total_pages: 168→182, total_sources: 146→167)
  - raw.md 전량 삭제 완료
  - ai-news.md 도메인 2026-04-23 섹션 추가
- 핵심 인사이트: open-webui(⭐133K) + langfuse(⭐25K) + openai-privacy-filter(OpenAI 공개) = 로컬 LLM 앱의 UI·관측성·안전 3대 인프라가 하루에 완성된 신호. Claude Code 에코시스템이 설정(andrej-karpathy-skills) → 모니터링(claude-code-templates) → 메모리(claude-mem) → 스킬(last30days-skill) 4계층으로 두터워지며 전환 비용 급상승 중. LLaDA2.0-Uni(확산 LLM, 85 upvotes)는 AR vs Diffusion 패러다임 논쟁 재점화 신호.
- canvas 업데이트: NO
- actionable 추가: NO (신규 actionable 없음, openai-privacy-filter → wiki 파이프라인 PII 필터 통합 기존 목록에 흡수)

---

## [2026-04-22] ingest | GitHub Trending + HF 자동수집 (2026-04-21~22 일괄)
- 도메인: ai-news (주), slam-3dgs 교차 (anyrecon)
- 처리 항목: 총 26개 (2026-04-21 13개 + 2026-04-22 13개)
- 추가 페이지: 10개 | 업데이트 페이지: 14개
  - sources 신규 (10): extending-one-step-image-gen, ai-agents-for-beginners, claude-context, awesome-agent-skills, agentspex, tstars-tryon, anyrecon, cointeract, tempo-ttt, gemma-4-e4b-obliterated
  - sources 스탯 업데이트 (14): openai-agents-python(⭐22.5K→24.2K), RuView(⭐47.7K→48.5K), thunderbolt(⭐1.7K→3.0K), worldmonitor(⭐53.1K→50.6K), DeepGEMM(⭐6.6K→6.9K), Gemma-4-31B(2M→4.47M DL), Gemma-4-26B(1.5M→3.29M DL), RAG-Anything(⭐16.5K→17.1K), TrendRadar(⭐53.1K→54K), FinceptTerminal(⭐10.3K→12.1K), Qwen3.6-35B-A3B(335K→458K DL), Kimi-K2.6(506→736 likes), MiniMax-M2.7(314K→358K DL), HY-World-2.0(오늘 신규 출시 531 likes 확인)
  - 미처리 스킵 (2): unsloth/gemma-4-26B-A4B-it-GGUF, unsloth/Qwen3.6-35B-A3B-GGUF — GGUF 양자화본, 독립 페이지 불필요
  - 이미 인덱스 등재된 HF 논문 항목 스킵 (4): OneVL, Agent-World, OpenGame, MultiWorld — 2026-04-21 일차에 이미 처리됨
  - index.md 업데이트 (total_pages: 139→149, total_sources: 117→127)
  - raw.md 전량 삭제 완료
  - ai-news.md 도메인 2026-04-22 섹션 추가
- 핵심 인사이트: FinceptTerminal이 GitHub Trending 1위(+2,548)로 폭등 — AI 금융 분석이 개인 투자자 레이어까지 침투하는 임계점 신호. Microsoft ai-agents-for-beginners(⭐58K), awesome-agent-skills(⭐17K), claude-context(⭐6.9K)가 같은 날 등장하며 "에이전트 학습→스킬 재사용→코드 통합" 3계층 에코시스템이 하루 만에 완성된 것이 이번 사이클의 가장 중요한 구조적 변화.
- canvas 업데이트: NO
- actionable 추가: YES (FinceptTerminal CLI 테스트, ai-agents-for-beginners Lesson 1~3 실행, claude-context 코드베이스 통합 테스트)

---

## [2026-04-21] ingest | GitHub Trending + HF 자동수집 (2026-04-21 일괄)
- 도메인: ai-news (주)
- 처리 항목: 총 40개 (2026-04-20 20개 raw.md 잔류 삭제 + 2026-04-21 신규 20개)
- 추가 페이지: 11개 | 업데이트 페이지: 5개
  - sources 신규 (11): worldmonitor, TrendRadar, RAG-Anything, VoxCPM2, Kimi-K2.6, Agent-World, OneVL, EasyVideoR1, WebCompass, OpenGame, MultiWorld
  - sources 스탯 업데이트 (5): FinceptTerminal(⭐7,497→10,259), MiniMax-M2.7(143K→314K DL), Gemma-4-E4B(2.12M→2.57M DL), Qwen3.6-35B-A3B(트렌딩, 335K DL), HY-World-2.0(503 likes 확인)
  - 미처리 스킵 (2): unsloth/Qwen3.6-35B-A3B-GGUF, google/gemma-4-E4B-it(이미 색인) — GGUF 양자화본·기존 인덱스 항목
  - index.md 업데이트 (total_pages: 128→139, total_sources: 106→117)
  - raw.md 전량 삭제 완료
  - ai-news.md 도메인 2026-04-20·2026-04-21 섹션 추가
- 핵심 인사이트: TrendRadar(⭐53K)의 MCP 아키텍처 지원이 핵심 — 에이전트가 실시간 트렌드 데이터를 직접 도구로 호출하는 패턴 첫 등장. RAG-Anything(⭐16K, HKUDS)은 멀티모달 RAG 올인원 프레임워크로 이 vault 파이프라인에 즉시 통합 가능. Agent-World(ByteDance, HF 1위)·WorldMonitor·TrendRadar 3종 동시 등장 = "실세계 데이터 수집→저장→학습" 전체 파이프라인이 오픈소스로 완성되는 전환점.
- canvas 업데이트: NO
- actionable 추가: YES (TrendRadar MCP 통합 테스트, RAG-Anything vault 파이프라인 통합, VoxCPM2 한국어 TTS 즉시 테스트)

---

## [2026-04-20] ingest | GitHub Trending + HF 자동수집 (2026-04-20 일괄 + raw.md 누적 정리)
- 도메인: ai-news (주)
- 처리 항목: 총 47개 (2026-04-18 13개 + 2026-04-19 20개 + 2026-04-20 14개) — 이전 인제스트에서 처리 완료된 항목들이 raw.md에 잔류해 있어 일괄 삭제
- 추가 페이지: 10개 | 업데이트 페이지: 4개
  - sources 신규 (10): deer-flow, RuView, minimind, PersonaVLM, FinceptTerminal, CutYourLosses, W-RAC, Qwen3.5-Omni, MaximalBrainDamage, ERNIE-Image
  - sources 스탯 업데이트 (4): claude-code-game-studios(⭐10,867→13,897), genericagent(⭐3,883→4,690), DeepTutor(⭐16,205→20,273), OmniVoice(958k→1M+)
  - 미처리 스킵 (2): unsloth/Qwen3.6-35B-A3B-GGUF, unsloth/gemma-4-26B-A4B-it-GGUF — 기존 모델 GGUF 양자화본, 독립 페이지 불필요
  - index.md 업데이트 (total_pages: 118→128, total_sources: 96→106)
  - raw.md 전량 삭제 완료
- 핵심 인사이트: deer-flow(⭐62,817)는 ByteDance의 오픈소스 SuperAgent — perplexity/OpenAI Deep Research의 직접 오픈소스 대항마 출현. RuView(⭐47,701) WiFi DensePose는 카메라 없는 인체 감지 분야에서 주목 폭발. 같은 날 CutYourLosses(병렬 추론 경로 가지치기)와 W-RAC(웹 RAG 청킹)이 등장해 "추론 비용 절감 + 검색 효율화"가 2026-04-20의 기술 핵심 축.
- canvas 업데이트: NO
- actionable 추가: YES (deer-flow 리서치 에이전트 파이프라인 연결 검토, FinceptTerminal 금융 데이터 테스트)

---

## [2026-04-19] ingest | GitHub Trending + HF 자동수집 (2026-04-18~19 일괄)
- 도메인: ai-news (주), slam-3dgs 교차 (GlobalSplat)
- 처리 항목: 29개 (2026-04-18 13개 + 2026-04-19 16개)
- 추가 페이지: 13개 | 업데이트 페이지: 16개
  - sources 신규 (13): chrome-devtools-mcp, DeepGEMM, evolver, claude-desktop-debian, thunderbolt, GlobalSplat, Dive-into-Claude-Code, UniDoc-RL, TRACER, Switch-KD, Representations-Before-Pixels, LeapAlign, OmniVoice
  - sources/stats 업데이트 (16): superpowers(⭐158K), dive-into-llms(⭐31.7K), omi(⭐10K), magika(⭐15.7K), openai-agents-python(⭐22.5K), HY-World-2.0(upvote 77), RAD-2(upvote 23), DR3-Eval(upvote 23), ASGuard(upvote 17), HiVLA(upvote 16), Gemma-4-31B(3.78M DL), MiniMax-M2.7(258K DL), GLM-5.1(104K DL), Gemma-4-26B(2.78M DL), Gemma-4-E4B(2.12M DL), how-to-fine-tune-reasoning-model(upvote 21 유지)
  - domains 업데이트: ai-news.md (2026-04-18, 2026-04-19 섹션 추가)
  - index.md 업데이트 (total_pages: 105→118, total_sources: 83→96)
- 핵심 인사이트: chrome-devtools-mcp(⭐35,992, 공식팀)는 코딩 에이전트의 "실행-디버그-수정" 루프를 브라우저 수준에서 완성하는 분기점 — DeepGEMM(FP8 커널), GlobalSplat(피드포워드 3DGS)와 같은 날 등장하며 에이전트 실행 스택·연산 효율·공간 인식 3계층이 동시 발전하는 수렴 신호.
- canvas 업데이트: NO
- actionable 추가: NO (chrome-devtools-mcp 설치 테스트, OmniVoice TTS 비교 기존 항목으로 흡수)
- raw.md 처리: 29개 항목 전량 삭제 완료

---

## [2026-04-18] ingest | GitHub Trending + HF 자동수집 (2026-04-18 일괄)
- 도메인: ai-news (주), local-llm 교차 (how-to-fine-tune-reasoning-model)
- 처리 항목: 17개 (2026-04-17 미삭제 13개 정리 + 2026-04-18 신규 4개)
- 추가 페이지: 2개 | 업데이트 페이지: 2개
  - sources 신규: omi (⭐9,983), how-to-fine-tune-reasoning-model (arXiv 2604.14164, upvote 21)
  - sources 업데이트: magika-google (⭐14,010→15,614), genericagent (⭐3,052→3,883)
  - raw.md 2026-04-17 미삭제 13개 항목 정리 (이미 인덱스 등재 완료 상태였음)
  - index.md 업데이트 (total_pages: 103→105, total_sources: 81→83)
- 핵심 인사이트: omi(⭐9,983)는 소프트웨어-하드웨어 동시 오픈소스화라는 드문 전략 — AI Pin·Rabbit R1 실패 이후 오픈소스 웨어러블 AI 기기 생태계의 재도전. 교사-학생 SFT 합성(2604.14164)은 로컬 모델 파인튜닝 비용 문제의 실용적 해법으로 주목.
- canvas 업데이트: NO
- actionable 추가: NO
- raw.md 처리: 17개 항목 전량 삭제 완료

---

## [2026-04-17] ingest | GitHub Trending + HF 자동수집 (2026-04-17 일괄)
- 도메인: ai-news
- 처리 항목: 13개 (GitHub Trending 5 + HF 논문 5 + HF 모델 3)
- 추가 페이지: 9개 | 업데이트 페이지: 4개
  - sources 신규: openai-agents-python, cognee, HY-World-2.0, DR3-Eval, RAD-2, HiVLA, ASGuard, HY-Embodied-0.5, Qwen3.6-35B-A3B (9개)
  - sources 업데이트: claude-mem (⭐60,473), dive-into-llms (⭐31,035), genericagent (⭐3,052), MiniMax-M2.7 (143K 다운로드) (4개)
  - domains 업데이트: ai-news.md 2026-04-17 섹션 추가
  - index.md 업데이트 (total_pages: 103, total_sources: 81)
- 핵심 인사이트: OpenAI 공식 에이전트 SDK(openai-agents-python)와 그래프 메모리 엔진(cognee)이 같은 날 동시 트렌딩 — 에이전트 인프라가 "코어 + 메모리 레이어" 2계층 구조로 표준화되는 분기점. Tencent HY-World 2.0은 slam-3dgs × video-saas 교차 도메인 신호.
- canvas 업데이트: NO
- actionable 추가: NO (기존 cognee/openai-agents 비교 검토 항목으로 흡수)
- raw.md 처리: 13개 항목 전부 처리 후 삭제 완료

---

## [2026-04-09] init | 위키 초기화
- 볼트 구조 생성: raw/, wiki/, queries/, index.md, log.md, CLAUDE.md
- 스키마 정의 완료
- 첫 번째 소스 인제스트: Karpathy LLM-Wiki 원문

## [2026-04-09] schema-update | raw 관리 방식 변경
- raw/ 폴더 → raw.md 단일 파일로 변경
- ingest 완료 후 raw.md 항목 즉시 삭제 방식 채택
- CLAUDE.md, SKILL.md 업데이트 완료

## [2026-04-09] blog | AI영상자동화-SaaS-Higgsfield-2026
- 저장 위치: 블로그/AI영상자동화-SaaS-Higgsfield-2026.md
- 주제: Higgsfield AI + 영상 자동화 SaaS 시장 2026
- 주요 내용: Higgsfield/Runway/Kling/Pika/Sora 2 비교, 시장 규모 데이터, 비즈니스별 활용법
- seomachine 초안: drafts/ai-video-automation-saas-higgsfield-2026-04-09.md

## [2026-04-10] query | Higgsfield 전체 기능 벤치마킹
- 도메인: video-saas
- 추가 페이지: 1개 (Higgsfield-벤치마킹.md)
- 핵심 인사이트: Cinema Studio의 @멘션 캐릭터/로케이션 시스템이 핵심 차별점. Chat은 생성+협업+커뮤니티 all-in-one.
- 산출물: HTML 시각화 (/tmp/higgsfield-benchmark.html)
- canvas 업데이트: NO
- actionable 추가: NO

## [2026-04-10] ingest | GitHub Trending + HF 자동수집 (2026-04-10 일괄)
- 도메인: ai-news
- 처리 항목: 16개 (GitHub Trending 5 + HF 논문 7 + HF 모델 4)
- 추가 페이지: 20개 | 업데이트 페이지: 3개
  - sources 신규: hermes-agent, DeepTutor, VoxCPM, Kronos, Archon, SkillClaw, When-Numbers-Speak, HY-Embodied, OpenSpatial, DMax, Gemma-4-31B, GLM-5.1, VOID-model, MegaStyle, Reasoning-SFT-Generalization, VoxCPM2-HF (16개)
  - entities 신규: NousResearch, Zhipu-AI, Netflix-AI (3개)
  - concepts 신규: AI-에이전트-프레임워크 (1개)
  - domains 업데이트: ai-news.md (1개)
  - index.md 업데이트 (total_pages: 38, total_sources: 15→18)
- 핵심 인사이트: 하루에 에이전트 프레임워크 항목 3개 동시 트렌딩 — 에이전트 인프라 표준화 경쟁이 결정적 국면. VoxCPM(토크나이저 없는 TTS)과 VOID(Netflix 영상 인페인팅)는 기존 워크플로우에 즉시 통합 가능.
- canvas 업데이트: NO
- actionable 추가: YES (4개 — VoxCPM TTS, VOID 통합, Gemma 벤치마크, hermes-agent 검토)
- raw.md 처리: 16개 항목 전부 처리 후 삭제 완료

## [2026-04-10] ingest | 인스타그램 저장 게시물 (2026-02-09 ~ 2026-04-10)
- 도메인: video-saas, ai-news, slam-3dgs (복합)
- 추가 페이지: 11개 | 업데이트 페이지: 4개
  - entities: Higgsfield, Seedance, Meshy, Tripo (4개 신규)
  - concepts: AI-영상-생성-2026, Claude-Code-워크플로우, 바이브코딩, AI-3D-생성, After-Effects-MCP, Mamba4 (6개 신규)
  - sources: instagram-저장-2026-02-2026-04 (1개 신규)
  - domains: video-saas.md, ai-news.md (2개 업데이트)
  - index.md, actionable.md (2개 업데이트)
- 핵심 인사이트: Claude Code + Higgsfield 완전 자동화 파이프라인이 실제로 작동하고 있음. 노트북 안 건드리고 콘텐츠 생산 자동화 가능.
- canvas 업데이트: NO (추후 예정)
- actionable 추가: YES (7개 — RTK, AE MCP, .claude/ 훅, Higgsfield 오픈소스, Seedance 테스트, 3D 워크플로우, Mamba4 검증)
- raw.md 처리: 102개 항목 → 전부 처리 후 삭제

## [2026-04-11] ingest | GitHub Trending + HF 자동수집 (2026-04-11 일괄)
- 도메인: ai-news
- 처리 항목: 27개 (GitHub Trending 8 + HF 논문 9 + HF 모델 6 + 중복/기존 4)
- 추가 페이지: 15개 | 업데이트 페이지: 7개
  - sources 신규: superpowers, multica, andrej-karpathy-skills, VibeVoice, TradingAgents, TimesFM, MinerU2.5, Gemma-4-26B, markitdown, rowboat, ClawBench, Gemma-4-E4B, Qwen3.5-Claude-Distilled (13개)
  - sources 업데이트: hermes-agent(⭐54,205 5배 급등), DeepTutor(⭐16,205), Kronos(arXiv 추가) (3개)
  - concepts 신규: 시계열-예측-파운데이션-모델, 금융-AI (2개)
  - entities 업데이트: Andrej Karpathy (andrej-karpathy-skills 추가) (1개)
  - concepts 업데이트: AI-에이전트-프레임워크 (superpowers, multica, rowboat 추가) (1개)
  - domains 업데이트: ai-news.md (1개)
  - index.md 업데이트 (total_pages: 38→53, total_sources: 15→31)
- 핵심 인사이트: hermes-agent 스타가 24시간 만에 5배(54,205) 폭등 — 에이전트 인프라 채택이 임계점 돌파. andrej-karpathy-skills(⭐12,083) 트렌딩은 Claude Code 실무 주류화 신호.
- canvas 업데이트: NO
- actionable 추가: YES (7개 — andrej-karpathy-skills 통합, MinerU2.5 파이프라인, markitdown 통합, superpowers 테스트, Gemma-4-26B 로컬 실행, TimesFM 실험, Gemma-4-E4B 테스트)
- raw.md 처리: 27개 항목 전부 처리 후 삭제 완료

## [2026-04-12] ingest | GitHub Trending + HF 자동수집 (2026-04-12 일괄)
- 도메인: ai-news (주), slam-3dgs (LIO-SAM), video-saas (LPM 1.0)
- 처리 항목: 20개 (GitHub Trending 8 + HF 논문 5 + HF 모델 3 + 기존 업데이트 4)
- 추가 페이지: 8개 | 업데이트 페이지: 5개
  - sources 신규: Gemma-4-31B-JANG_4M-CRACK, flash-attention, skypilot, silero-vad, anomalib, LIO-SAM, LPM-1.0, OpenVLThinkerV2 (8개)
  - sources 업데이트: hermes-agent(⭐61,442), markitdown(⭐103,007), superpowers(⭐147,523), multica(⭐8,427), GLM-5.1(28.8K 다운로드) (5개)
  - domains 업데이트: slam-3dgs 도메인 첫 소스(LIO-SAM) 확보
  - index.md 업데이트 (total_pages: 53→61, total_sources: 31→39)
- 핵심 인사이트: LIO-SAM 트렌딩 진입으로 slam-3dgs 도메인 첫 실용 SLAM 레퍼런스 확보. flash-attention(⭐23K) 재진입은 Gemma-4·GLM-5.1 대형 모델 출시 후 학습 인프라 관심 급증 신호 — 모델 경쟁이 인프라 레이어 수요로 파급.
- canvas 업데이트: NO
- actionable 추가: NO (기존 actionable 항목으로 커버)
- raw.md 처리: 20개 항목 전부 처리 후 삭제 완료

## [2026-04-09] ingest | LLM-Wiki 원문 (Karpathy 2026)
- 추가된 페이지: 3개 (LLM-Wiki, RAG vs LLM-Wiki, Andrej Karpathy)
- 소스 요약 페이지: wiki/sources/llm-wiki-karpathy-2026.md
- 주요 인사이트: RAG는 매번 재추출, LLM-Wiki는 복리 축적. 인간=소싱+질문, LLM=북키핑 전체.

## [2026-04-13] ingest | GitHub Trending + HF 자동수집 (2026-04-13 일괄)
- 도메인: ai-news (주도메인), slam-3dgs 교차 (WildDet3D), video-saas 교차 (RefineAnything, Matrix-Game-3.0)
- 추가 페이지: 9개 | 업데이트 페이지: 4개 (hermes-agent, Kronos, andrej-karpathy-skills, Archon)
- 신규 소스: FORGE, WildDet3D, RefineAnything, EXAONE-4.5, Matrix-Game-3.0, claude-code-best-practice, claude-mem, ai-hedge-fund, ralph
- 스타 업데이트: hermes-agent (61K→71K, 3일 연속 1위), Kronos (7K→16K, +130% 금융AI 폭등), andrej-karpathy-skills (12K→18K), Archon (12K→17K)
- 핵심 인사이트: Claude Code 에코시스템 독자 생태계 형성 — claude-code-best-practice(39K⭐) + claude-mem(51K⭐) + andrej-karpathy-skills(18K⭐) 동시 트렌딩은 Claude Code가 개발자 주류 도구로 확정됐다는 신호
- canvas 업데이트: NO
- actionable 추가: YES (claude-mem 설치, claude-code-best-practice+andrej-karpathy-skills 통합 CLAUDE.md 작성, ai-hedge-fund 에이전트 아키텍처 분석)
- raw.md 처리: 23개 항목 전량 삭제 완료

## [2026-04-14] ingest | GitHub Trending + HF 자동수집 (2026-04-14 일괄)
- 도메인: ai-news (주), video-saas 교차 (OmniShow, Uni-ViGU)
- 처리 항목: 18개 (GitHub Trending 10 + HF 논문 6 + HF 모델 2)
- 추가 페이지: 7개 | 업데이트 페이지: 11개
  - sources 신규: ClawGUI, AttentionSink, OmniShow, StripsAsTokens, PseudoUnification, Uni-ViGU, MiniMax-M2.7 (7개)
  - sources 업데이트: hermes-agent(⭐80,633 +8,735), andrej-karpathy-skills(⭐28,000 +9,156), markitdown(⭐107,555), claude-mem(⭐54,157), multica(⭐11,700), Archon(⭐17,800), ai-hedge-fund(⭐53,385), Kronos(⭐17,347), GLM-5.1(84,800 다운로드), VoxCPM(⭐12,600), Gemma-4-31B (11개)
  - domains 업데이트: ai-news.md (2026-04-14 섹션 추가)
  - index.md 업데이트 (total_pages: 70→77, total_sources: 48→55)
- 핵심 인사이트: hermes-agent 4일 연속 1위(80K⭐) + andrej-karpathy-skills 하루 +9K(28K⭐) — 에이전트 프레임워크와 Claude Code 최적화가 동시에 폭발하는 것은 AI 코딩이 "실험"에서 "인프라"로 전환됐다는 명확한 신호
- canvas 업데이트: NO
- actionable 추가: YES (3개 — andrej-karpathy-skills 즉시 통합, hermes-agent 아키텍처 검토, MiniMax-M2.7 벤치마크 확인)
- raw.md 처리: 18개 항목 전량 삭제 완료

## [2026-04-15] ingest | 대기 항목 없음

## [2026-04-16] ingest | GitHub Trending + HF 자동수집 (2026-04-15~16 일괄)
- 도메인: ai-news (주), video-saas 교차 (seedance-2, rational-rewards), slam-3dgs 교차 (spatialevo)
- 처리 항목: 26개 (GitHub Trending 10 + HF 논문 9 + HF 모델 7)
- 추가 페이지: 17개 | 업데이트 페이지: 9개
  - sources 신규: hierarchical-svg-tokenization, block-diffusion-speculative-decoding, lary-benchmark, knowrl, all-MiniLM-L6-v2, bert-base-uncased, nsfw-image-detection, dive-into-llms, open-agents-vercel, magika-google, claude-code-game-studios, genericagent, rational-rewards, seedance-2, spatialevo, gameworld, occubench (17개)
  - sources 업데이트: hermes-agent(⭐87,101), claude-mem(⭐56,602), ai-hedge-fund(⭐54,543), andrej-karpathy-skills(⭐37,597), Kronos(⭐17,996), ClawGUI(업보트 307), Gemma-4-31B(2.89M 다운로드), Gemma-4-26B(2.2M 다운로드), MiniMax-M2.7(85,500 다운로드) (9개)
  - domains 업데이트: ai-news.md (2026-04-15, 2026-04-16 섹션 추가)
  - index.md 업데이트 (total_pages: 77→94, total_sources: 55→72)
- 핵심 인사이트: all-MiniLM-L6-v2 198M 다운로드/월 + BERT 65.1M 수집 — 화려한 신모델보다 검증된 경량 실용 모델의 구조적 수요가 더 높다. Claude Code 에코시스템이 게임 개발(claude-code-game-studios ⭐10K)까지 확장되며 에코시스템 독립성 확인.
- canvas 업데이트: NO
- actionable 추가: YES (all-MiniLM-L6-v2 RAG 파이프라인 적용, magika 파일 검증 레이어 추가, GenericAgent 검증)
- raw.md 처리: 26개 항목 전량 삭제 완료

## [2026-04-22] ingest | GitHub Trending + HF 자동수집 (2026-04-22 일괄)
- 도메인: ai-news (주), local-llm 교차 (Qwen3.6-35B-A3B-GGUF/A3B, MiniMax-M2.7, Kimi-K2.6, gemma-4-e4b-obliterated), slam-3dgs 교차 (AnyRecon, HY-World-2.0), video-saas 교차 (tstars-tryon, cointeract)
- 처리 항목: 19개 (GitHub Trending 8 + HF 논문 5 + HF 모델 6)
- 추가/업데이트 페이지: 19개
  - GitHub sources: RuView(⭐49,111), thunderbolt(⭐3,627), FinceptTerminal(⭐12,332), TrendRadar(⭐54,073), ai-agents-for-beginners(⭐58,209), claude-context(⭐6,953), RAG-Anything(⭐17,214), awesome-agent-skills(⭐17,282)
  - HF 논문: tstars-tryon(upvote 54), agentspex(upvote 45), anyrecon(upvote 33), cointeract(upvote 23), tempo-ttt(upvote 18)
  - HF 모델: Qwen3.6-35B-A3B-GGUF(1.1M DL), Qwen3.6-35B-A3B(583K DL), MiniMax-M2.7(416K DL), Kimi-K2.6(54.5K DL), HY-World-2.0(신규), gemma-4-e4b-obliterated(79K DL)
  - index.md 업데이트 (total_pages: 149→168, total_sources: 127→146)
- 핵심 인사이트: Qwen3.6 MoE(35B/3B 활성) + Kimi-K2.6(1.1T MoE) + MiniMax-M2.7(229B MoE) 동시 공개 — 중국발 대규모 MoE 오픈소스 경쟁이 단일 주에 폭발. HY-World-2.0(Image-to-3D) + AnyRecon(arbitrary-view 3D)으로 slam-3dgs 연계 가능성 확인.
- canvas 업데이트: NO
- actionable 추가: NO (신규 actionable 없음, 기존 목록 유지)
- raw.md 처리: 19개 항목 전량 삭제 완료

## [2026-04-24] ingest | GitHub Trending + HF 자동수집 (2026-04-23~24 일괄)
- 도메인: ai-news (주도메인)
- 처리 항목: 44개 (2026-04-23: 31개 + 2026-04-24: 13개)
- 추가 페이지: 10개 | 업데이트 페이지: 16개
  - sources 신규: Terminal-Agent-Context-Compression, Visual-Reasoning-Tool-RL, free-claude-code, ml-intern, WorldMark, UniT-Humanoid-Policy, DeepSeek-V4-Pro, StyleID-Facial-Identity, Seeing-Fast-and-Slow, Hybrid-Policy-Distillation (10개)
  - sources 업데이트 (스탯): TrendRadar(54,772), worldmonitor(52,015), RAG-Anything(18,456), claude-context(8,697), RuView(49,992), Kimi-K2.6(208K DL), Qwen3.6-35B-A3B(861K DL), Qwen3.6-GGUF(1.28M), MiniMax-M2.7(463K), Gemma-4-E4B(3M), VoxCPM2(81.7K), FinceptTerminal(13,533), LLaDA2.0-Uni(126 upvotes), Near-Future-Policy(36), DR-Venus(32) 등 다수
  - domains 업데이트: ai-news.md (2026-04-23, 2026-04-24 섹션 추가)
  - index.md 업데이트 (total_pages: 182→192, total_sources: 167→177)
- 핵심 인사이트: DeepSeek-V4-Pro(862B) 공개 5시간 만에 HF 트렌딩 1위 + free-claude-code 하루 +2K 스타 — 가장 강력한 오픈소스 모델이 계속 공개되면서 유료 AI 도구 우회 수요도 폭발. "AI 인프라 민주화 가속" 시대 신호.
- canvas 업데이트: NO
- actionable 추가: YES (DeepSeek-V4-Pro API 테스트, ml-intern 로컬 실험)
- raw.md 처리: 44개 항목 전량 삭제 완료

## [2026-04-29] lint | 정기 대기열 점검
- 대기 항목 없음

## [2026-04-30] ingest | GitHub Trending + HF 자동수집 (2026-04-30 일괄)
- 도메인: ai-news (전량)
- 처리 항목: 13개 (GitHub Trending 5 + HF 논문 5 + HF 모델 3)
- 추가 페이지: 6개 | 업데이트 페이지: 7개
  - sources 신규: warp-terminal(⭐46,560), GLM-5V-Turbo(업보트 68), Turning-the-TIDE(업보트 32), ClawGym(업보트 28), Diffusion-Templates(업보트 5), Accelerating-RL-Post-Training(업보트 3) (6개)
  - sources 업데이트 스탯: superpowers(174K), mattpocock-skills(46,841), VibeVoice(45,909), GitNexus(33,562), DeepSeek-V4-Pro(272K DL), DeepSeek-V4-Flash(199K DL), openai-privacy-filter(82.9K DL) (7개)
  - domains 업데이트: ai-news.md (2026-04-30 섹션 추가)
  - index.md 업데이트 (total_pages: 221→227, total_sources: 206→212)
- 핵심 인사이트: DeepSeek-V4-Flash(199K DL)가 Pro(272K DL)에 버금가는 채택속도 — 엔지니어들이 "최강 모델"보다 "실배포 가능한 빠른 모델"을 선택. 터미널(warp +12,822 / day)이 에이전트 실행 레이어 경쟁장으로 부상. 에이전트 스킬 생태계는 방법론(superpowers 174K)→컬렉션(mattpocock 47K)→인프라(warp 47K) 3계층으로 분화 완료.
- canvas 업데이트: NO
- actionable 추가: NO
- raw.md 처리: 13개 항목 전량 삭제 완료

## [2026-05-16] lint | 정기 대기열 점검
- 대기 항목 없음

## [2026-05-21] lint | 정기 대기열 점검
- 대기 항목 없음

## [2026-05-22] lint | 정기 대기열 점검
- 대기 항목 없음

## [2026-05-27] lint | 정기 대기열 점검
- 대기 항목 없음

## [2026-05-30] ingest | GitHub Trending + HF 자동수집 (2026-05-30 일괄)
- 도메인: ai-news (전량)
- 처리 항목: 13개 (GitHub Trending 5 + HF 논문 5 + HF 모델 3)
- 신규 페이지: 6개 | 업데이트 페이지: 7개
  - sources 신규: n8n(⭐190,304), Qlib(⭐43,714), InvokeAI(⭐27,287), ONNX-Runtime(⭐20,678), Qwen-VLA(업보트85), Qwen3.6-35B-Uncensored(DL2.23M)
  - sources 업데이트 스탯: FunASR(date), AgentDoG(71→97), OmniRetrieval(45→56), CollectionLoRA(34→49), minWM(27→43), MiniCPM5-1B(15.6K→28.8K DL), LocateAnything-3B(7.8K→18.3K DL)
  - index.md 업데이트 (total_pages: 400→406, total_sources: 385→391)
- 핵심 인사이트: Qwen3.6-35B-Uncensored 2.23M 다운로드 = 공식 모델(583K)의 4배 — 커뮤니티의 무검열 LLM 수요가 공식 채택을 압도. n8n ⭐190K는 워크플로우 자동화+LLM 오케스트레이션의 사실상 표준 위치 확인.
- canvas 업데이트: NO
- actionable 추가: NO
- raw.md 처리: 13개 항목 전량 삭제 완료

## [2026-05-31] lint | 정기 대기열 점검
- 대기 항목 없음

## [2026-06-02] ingest | GitHub Trending + HF 자동수집 (2026-06-02 일괄)
- 도메인: ai-news (전량)
- 처리 항목: 13개 (GitHub Trending 5 + HF 논문 5 + HF 모델 3)
- 신규 페이지: 8개
  - sources 신규: hermes-webui(⭐11,945), supermemory(⭐24,250), PEFT-scaling(arXiv), crafter-scientific-figure(arXiv), K-BrowseComp(arXiv), TASTE-agent-benchmark(arXiv), Draft-OPD(arXiv), pyannote-speaker-diarization(HF 9.65M DL)
- 업데이트 페이지: 5개 (stats 갱신)
  - MoneyPrinterTurbo: ⭐72,712→77,436 (+3,375)
  - markitdown: ⭐133,359→139,776 (+3,034)
  - VoxCPM: ⭐23,009→24,625 (+888)
  - DeepSeek-V4-Pro: 5.89M→5.83M DL
  - Qwen3.6-27B: 5.06M→5.24M DL
- index.md 업데이트 (total_pages: 415→423, total_sources: 400→408)
- 핵심 인사이트: K-BrowseComp 결과 — 한국어 웹 에이전트 성능 격차 실증(한국모델 0~10% vs 글로벌 30~45%). supermemory LongMemEval 벤치마크 1위는 에이전트 장기 메모리 API 최강 후보. pyannote 월 965만 DL은 음성 분리 사실상 표준.
- canvas 업데이트: NO
- actionable 추가: NO
- raw.md 처리: 13개 항목 전량 삭제 완료

## [2026-06-05] lint | 대기 항목 없음
- 대기 항목 없음
