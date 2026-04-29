# Wiki Log

시간순 기록. `grep "^## \[" log.md | tail -10` 으로 최근 항목 확인 가능.

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
