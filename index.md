---
title: Wiki Index
updated: 2026-04-29 (ingest batch)
total_pages: 221
total_sources: 206
---

# Wiki Index

이 파일은 위키의 모든 페이지를 카탈로그화한다. LLM은 쿼리 응답 시 여기서 시작한다.

---

## entities
<!-- 인물, 기업, 제품, 프로젝트 -->

- [[Andrej Karpathy]] — AI 연구자, OpenAI 공동창업자, LLM-Wiki 철학 창안자
- [[Higgsfield]] — AI 영상 스튜디오, Cinema Studio 2.5, 캐릭터+씬+샷 통합 파이프라인
- [[Higgsfield-벤치마킹]] — Cinema Studio 3.0 + Chat 전체 기능 심층 분석 (2026-04-10 직접 확인)
- [[Seedance]] — ByteDance VFX 특화 영상 AI, "할리우드급 VFX를 1/10 비용으로"
- [[Meshy]] — 텍스트/이미지 → 3D 모델 생성, 제품 디자인 특화
- [[Tripo]] — 단일 이미지 → 분리 메시 생성, Blender 연동 강점
- [[NousResearch]] — 오픈소스 LLM 파인튜닝, Hermes 시리즈, hermes-agent 개발사
- [[Zhipu AI]] — GLM 시리즈 개발사 (Z.AI), Monday AI 기반 모델 제공사, GLM-5.1 (753B MoE)
- [[Netflix-AI]] — Netflix AI Research, VOID 비디오 인페인팅 오픈소스 공개

---

## concepts
<!-- 아이디어, 이론, 프레임워크 -->

- [[LLM-Wiki]] — LLM을 활용한 복리 축적형 개인 지식베이스 구축 패턴
- [[RAG vs LLM-Wiki]] — 두 접근의 철학적 차이 비교
- [[AI-영상-생성-2026]] — 2026년 AI 영상 생성 도구 전체 지형도 (Higgsfield, Seedance, Kling 등)
- [[Claude-Code-워크플로우]] — .claude/ 폴더 설정, RTK 프록시, 음성 코딩, PWA 자동화
- [[바이브코딩]] — 비개발자가 AI로 앱 만드는 패러다임, 3시간 앱스토어 출시 사례
- [[AI-3D-생성]] — Meshy/Tripo/나노바나나2, 텍스트/이미지 → 3D 워크플로우
- [[After-Effects-MCP]] — AE MCP로 자연어 → After Effects 자동화, Smear/GeoLayers 기법
- [[Mamba4]] — SSM 기반 O(n) 아키텍처, Transformer O(n²) 한계 해결
- [[AI-에이전트-프레임워크]] — 2026-04-10~11 트렌딩 5종(hermes-agent, Archon, SkillClaw, superpowers, multica), 에이전트 인프라 경쟁 현황
- [[시계열-예측-파운데이션-모델]] — TimesFM·Kronos 중심, 제로샷 시계열 예측 패러다임 *(NEW)*
- [[금융-AI]] — TradingAgents·Kronos·TimesFM, 멀티에이전트+파운데이션 모델 결합 *(NEW)*
- [[에이전트-메모리-레이어]] — cognee·claude-mem으로 대표되는 에이전트 메모리 인프라 패턴 *(NEW)*

---

## sources
<!-- 소스별 요약 -->

- [[LLM-Wiki 원문 (Karpathy 2026)]] — Andrej Karpathy의 LLM-Wiki 패턴 가이드 원문
- [[instagram-저장-2026-02-2026-04]] — 102개 인스타그램 저장 게시물 (2026-02~04), video-saas/ai-news/3D/모션디자인
- [[hermes-agent]] — NousResearch 오픈소스 에이전트 프레임워크 (GitHub ⭐61,442, 이틀 연속 1위)
- [[DeepTutor]] — 에이전트 기반 적응형 학습 보조 시스템 (GitHub ⭐20,273) *(UPDATED)*
- [[VoxCPM]] — 토크나이저 없는 오픈소스 TTS (GitHub ⭐14,227)
- [[Kronos]] — 금융 시계열 파운데이션 모델 (GitHub ⭐7,045 + arXiv 2508.02739)
- [[Archon]] — AI 코딩 결정론화 하네스 (GitHub ⭐12,392)
- [[SkillClaw]] — AI 에이전트 스킬 집단 진화 논문 (arXiv 2604.08377)
- [[When-Numbers-Speak]] — T2V 숫자-객체 정렬 (arXiv 2604.08546)
- [[HY-Embodied]] — 실세계 로봇용 소형 임베디드 모델 (arXiv 2604.07430)
- [[OpenSpatial]] — 멀티모달 3D 공간 이해 데이터 엔진 (arXiv 2604.07296)
- [[DMax]] — 확산 LLM 병렬 디코딩 가속 (arXiv 2604.08302)
- [[Gemma-4-31B]] — Google 멀티모달 31B, Apache 2.0 (HF 5.1M 다운로드) *(UPDATED)*
- [[GLM-5.1]] — Zhipu AI MoE 753B, 한국어+영어, MIT (HF 183K 다운로드, 1.47K likes) *(UPDATED)*
- [[VOID-model]] — Netflix 비디오 객체 인페인팅, Apache 2.0
- [[superpowers]] — Shell 기반 에이전트 스킬 프레임워크 (GitHub ⭐158,202, +10,679)
- [[multica]] — 오픈소스 매니지드 에이전트 플랫폼 (GitHub ⭐8,427)
- [[andrej-karpathy-skills]] — Karpathy 관찰 기반 Claude Code 최적화 CLAUDE.md (GitHub ⭐12,083) *(NEW)*
- [[VibeVoice]] — Microsoft 오픈소스 STT/TTS 엔진 + Next-token diffusion 장시간 다화자 (GitHub ⭐43,576) *(UPDATED)*
- [[TradingAgents]] — 멀티에이전트 LLM 주식거래 프레임워크 (arXiv 2412.20138 / GitHub ⭐54,163) *(UPDATED)*
- [[TimesFM]] — 디코더 전용 시계열 예측 파운데이션 모델, Google Research (arXiv 2310.10688) *(NEW)*
- [[MinerU2.5]] — 1.2B 문서 파싱 VLM, PDF/수식/표 SOTA (arXiv 2509.22186) *(NEW)*
- [[Gemma-4-26B]] — Google Gemma 4 26B MoE (활성 4B), 멀티모달, HF 3.29M 다운로드 *(UPDATED)*
- [[markitdown]] — Microsoft 오픈소스 전방위 문서→마크다운 변환기 (GitHub ⭐103,007)
- [[rowboat]] — 지속 기억 기반 오픈소스 AI 동료 플랫폼 (GitHub ⭐11,922) *(NEW)*
- [[ClawBench]] — AI 에이전트 일상 온라인 태스크 종합 벤치마크 (arXiv 2604.08523) *(NEW)*
- [[Gemma-4-E4B]] — Google Gemma 4 E4B Any-to-Any 8B 멀티모달 (HF 3M 다운로드) *(UPDATED)*
- [[Qwen3.5-Claude-Distilled]] — Claude 4.6 Opus 추론 → Qwen3.5 27B 증류 (HF 567K)
- [[Gemma-4-31B-JANG_4M-CRACK]] — Gemma-4 커뮤니티 파인튠, 이미지-텍스트 멀티모달 (HF 99.1K, 검증 필요) *(NEW)*
- [[flash-attention]] — 메모리 효율 정확 어텐션 CUDA 구현, LLM 인프라 표준 (GitHub ⭐23,304) *(NEW)*
- [[skypilot]] — 멀티클라우드 AI 워크로드 통합 실행 시스템 (GitHub ⭐9,826) *(NEW)*
- [[silero-vad]] — 엔터프라이즈급 경량 음성활성감지 모델, TTS 파이프라인 전처리 (GitHub ⭐8,760) *(NEW)*
- [[anomalib]] — SOTA 이상 탐지 라이브러리, 엣지 AI 산업 비전 (GitHub ⭐5,622) *(NEW)*
- [[LIO-SAM]] — 라이다-IMU 긴밀 결합 SLAM, 실시간 3D 지도 생성 (GitHub ⭐4,676, slam-3dgs) *(NEW)*
- [[LPM-1.0]] — 영상 기반 캐릭터 퍼포먼스 모델, 25명 대형 연구 (HF 업보트 194, video-saas) *(NEW)*
- [[OpenVLThinkerV2]] — UCLA NLP 범용 멀티모달 추론 모델 (HF 업보트 139)
- [[FORGE]] — 제조 시나리오 특화 멀티모달 세밀 평가 벤치마크 (HF 업보트 50, Waterloo대) *(NEW)*
- [[WildDet3D]] — 실환경 프롬프트 기반 3D 객체 탐지 스케일링 (HF 업보트 36, Ai2) *(NEW)*
- [[RefineAnything]] — 이미지 지역별 세부 품질 향상 멀티모달 접근법 (HF 업보트 29) *(NEW)*
- [[EXAONE-4.5]] — LG AI Research 대형 언어 모델 기술 보고서 (HF 업보트 24) *(NEW)*
- [[Matrix-Game-3.0]] — 장기 메모리 실시간 스트리밍 인터랙티브 월드 모델 (HF 업보트 21) *(NEW)*
- [[claude-code-best-practice]] — Claude Code 모범 사례 집대성 (GitHub ⭐39,886) *(NEW)*
- [[claude-mem]] — Claude Code 세션 간 컨텍스트 AI 압축·주입 플러그인 (GitHub ⭐60,473) *(UPDATED)*
- [[ai-hedge-fund]] — AI 에이전트 기반 헤지펀드 시뮬레이터 (GitHub ⭐52,482, 연구용) *(NEW)*
- [[ralph]] — PRD 항목 완료까지 반복 실행 자율 AI 에이전트 루프 (GitHub ⭐16,181)
- [[ClawGUI]] — GUI 에이전트 학습·평가·배포 통합 프레임워크 (arXiv 2604.11784, upvotes 41) *(NEW)*
- [[AttentionSink]] — 트랜스포머 어텐션 싱크 현상 종합 서베이, 20인 저자 (arXiv 2604.10098, upvotes 39) *(NEW)*
- [[OmniShow]] — ByteDance 인간-사물 상호작용 영상 생성, 멀티모달 조건 통합 (arXiv 2604.11804, upvotes 35) *(NEW)*
- [[StripsAsTokens]] — 기하학 스트립 토큰화 + 네이티브 UV 분할 3D 메시 생성 (arXiv 2604.09132, upvotes 33) *(NEW)*
- [[PseudoUnification]] — 통합 멀티모달 모델 엔트로피 프로빙, HKUST (arXiv 2604.10949, upvotes 31) *(NEW)*
- [[Uni-ViGU]] — 확산 기반 영상 생성+이해 통합 단일 프레임워크 (arXiv 2604.08121, upvotes 33) *(NEW)*
- [[MiniMax-M2.7]] — MiniMax 229B MoE 텍스트 생성 모델 (HF 463,000 다운로드) *(UPDATED)*
- [[hierarchical-svg-tokenization]] — SVG 계층 토크나이징 LLM 생성, Tencent Hunyuan (HF 업보트 224) *(NEW)*
- [[block-diffusion-speculative-decoding]] — 블록 확산 드래프트 트리 투기적 디코딩 가속 (HF 업보트 177) *(NEW)*
- [[lary-benchmark]] — 비전-액션 정렬 잠재 행동 표현 벤치마크, Meituan (HF 업보트 18) *(NEW)*
- [[knowrl]] — 지식 가이드 RL로 LLM 추론 향상, Tianjin University (HF 업보트 14) *(NEW)*
- [[all-MiniLM-L6-v2]] — 22.7M 파라미터 문장 임베딩 표준, 198M 다운로드/월 *(NEW)*
- [[bert-base-uncased]] — Google BERT 110M, NLP 파인튜닝 기준 모델, 65.1M 다운로드/월 *(NEW)*
- [[nsfw-image-detection]] — NSFW 이미지 분류, 콘텐츠 필터링 즉시 투입, 37.9M 다운로드/월 *(NEW)*
- [[dive-into-llms]] — 《动手学大모델》 LLM 실습 튜토리얼 (GitHub ⭐31,747) *(UPDATED)*
- [[open-agents-vercel]] — Vercel 공식 에이전트 빌딩 템플릿 (GitHub ⭐2,820) *(NEW)*
- [[magika-google]] — Google AI 파일 타입 감지 도구, Apache 2.0 (GitHub ⭐15,614) *(UPDATED)*
- [[claude-code-game-studios]] — Claude Code 49에이전트·72워크플로우 게임 스튜디오 (GitHub ⭐13,897) *(UPDATED)*
- [[genericagent]] — 자기진화 에이전트, 스킬트리 자동 성장, 토큰 6배 절감 주장 (GitHub ⭐4,690) *(UPDATED)*
- [[rational-rewards]] — 추론 보상으로 훈련+추론 시간 시각 생성 스케일링 (HF 업보트 63) *(NEW)*
- [[seedance-2]] — ByteDance Seedance 2.0 복잡 세계 영상 생성 (HF 업보트 62) *(NEW)*
- [[spatialevo]] — 결정론적 기하학 환경 공간 지능 자기진화, 19인 저자 (HF 업보트 46) *(NEW)*
- [[gameworld]] — 멀티모달 게임 에이전트 표준 평가 벤치마크, NUS (HF 업보트 42) *(NEW)*
- [[occubench]] — 실세계 직업 전문 태스크 에이전트 평가, Qwen/Alibaba (HF 업보트 38) *(NEW)*
- [[openai-agents-python]] — OpenAI 공식 멀티에이전트 워크플로우 프레임워크, 경량 설계 (GitHub ⭐24,205) *(UPDATED)*
- [[cognee]] — AI 에이전트 메모리를 6줄 코드로 구성하는 그래프 기반 지식 엔진 (GitHub ⭐15,974) *(NEW)*
- [[HY-World-2.0]] — 단일 멀티모달 모델로 3D 세계 재구성·생성·시뮬레이션 통합 (557 likes) *(UPDATED)*
- [[DR3-Eval]] — AI deep research 에이전트 재현 가능한 현실적 평가 프레임워크 (HF upvote 23) *(UPDATED)*
- [[RAD-2]] — 생성기-판별기 구조에서 강화학습 확장 프레임워크 (HF upvote 23) *(UPDATED)*
- [[HiVLA]] — 계층적 시각 기반 로봇 조작 시스템, VLA 실세계 정확도 향상 (HF upvote 16) *(UPDATED)*
- [[ASGuard]] — 활성화 스케일링으로 Jailbreak 방어, 성능 저하 없이 안전성 강화 (HF upvote 17) *(UPDATED)*
- [[HY-Embodied-0.5]] — Tencent 4B embodied AI 모델, 이미지-텍스트 입력 물리 세계 행동 계획 (HF 1,060) *(NEW)*
- [[Qwen3.6-35B-A3B-GGUF]] — unsloth Qwen3.6-35B-A3B GGUF 양자화, llama.cpp 로컬 실행 최적화 (HF 1.28M 다운로드, local-llm) *(UPDATED)*
- [[Qwen3.6-35B-A3B]] — Qwen MoE 멀티모달 36B, 활성 3B로 효율적 추론 (HF 트렌딩, 1.18M 다운로드) *(UPDATED)*
- [[omi]] — BasedHardware 화면+음성 멀티모달 오픈소스 AI 비서, 웨어러블 디바이스 연동 (GitHub ⭐10,022) *(UPDATED)*
- [[how-to-fine-tune-reasoning-model]] — 교사-학생 협력 SFT 데이터 합성으로 추론 파인튜닝 효율 향상 (arXiv 2604.14164, upvote 21)
- [[chrome-devtools-mcp]] — Chrome DevTools 공식 MCP 서버, 코딩 에이전트 브라우저 직접 제어·디버깅 (GitHub ⭐35,992) *(NEW)*
- [[DeepGEMM]] — DeepSeek FP8 GEMM 커널, LLM 추론 연산 효율 극대화 (GitHub ⭐6,903) *(UPDATED)*
- [[evolver]] — Genome Evolution Protocol 기반 AI 에이전트 자기진화 엔진 (GitHub ⭐5,147) *(NEW)*
- [[claude-desktop-debian]] — Debian Linux에서 Claude Desktop 네이티브 실행, MCP 통합 (GitHub ⭐3,515) *(NEW)*
- [[thunderbolt]] — Thunderbird 내장 AI 프레임워크, 벤더 종속 없는 모델 자유 선택 (GitHub ⭐3,040) *(UPDATED)*
- [[GlobalSplat]] — 전역 장면 토큰으로 3DGS 단일 피드포워드 패스 처리, 실시간 3D 재구성 (HF upvote 18) *(NEW)*
- [[Dive-into-Claude-Code]] — Claude Code 구조 분석으로 AI 에이전트 설계 공간 체계화 (arXiv 2604.14228, upvote 13) *(NEW)*
- [[UniDoc-RL]] — 계층적 행동+밀집 보상 RL로 문서 이해 RAG 훈련 (arXiv 2604.14967, upvote 9) *(NEW)*
- [[TRACER]] — 추론 트레이스 기반 적응형 LLM 라우팅, API 비용 최적화 (arXiv 2604.14531, upvote 6) *(NEW)*
- [[Switch-KD]] — 시각적 스위치 메커니즘으로 VLM 지식 증류 (arXiv 2604.14629, upvote 8) *(NEW)*
- [[Representations-Before-Pixels]] — 의미론적 표현 계층 생성으로 비디오 예측 품질 향상 (arXiv 2604.11707, upvote 7) *(NEW)*
- [[LeapAlign]] — ByteDance Seed, 플로우 매칭 모델 사후 정렬 2-스텝 궤적 (arXiv 2604.15311, upvote 7) *(NEW)*
- [[OmniVoice]] — 다국어 고품질 TTS 모델, HF 1M+ 다운로드 (HF 트렌딩 3위)
- [[deer-flow]] — ByteDance 장기 작업 수행 SuperAgent, 웹 리서치·코딩·콘텐츠 생성 자율 처리 (GitHub ⭐62,817) *(NEW)*
- [[RuView]] — WiFi 신호 기반 DensePose 인체 자세 추정, 카메라 없이 벽 통과 실시간 감지 (GitHub ⭐49,992) *(UPDATED)*
- [[minimind]] — 64M 파라미터 GPT를 2시간 만에 처음부터 학습, LLM 내부 구조 실습 표준 (GitHub ⭐47,657) *(NEW)*
- [[PersonaVLM]] — 사용자 페르소나 장기 기억 개인화 멀티모달 VLM 프레임워크 (arXiv 2604.13074, upvote 19) *(NEW)*
- [[FinceptTerminal]] — AI·LLM 기반 금융 데이터 분석·투자 리서치 CLI 터미널 (GitHub ⭐13,533) *(UPDATED)*
- [[CutYourLosses]] — 병렬 추론 불필요 경로 조기 제거 학습 기법, 추론 비용 절감 (arXiv 2604.16029, upvote 16) *(NEW)*
- [[W-RAC]] — 웹 검색 특성 고려 청크 분할로 RAG 검색 정확도·비용 효율 개선 (arXiv 2604.04936, upvote 14) *(NEW)*
- [[Qwen3.5-Omni]] — Qwen3.5 전방위 모달리티(텍스트·음성·이미지·비디오) 통합 모델 기술 보고서 (arXiv 2604.15804, upvote 9) *(NEW)*
- [[MaximalBrainDamage]] — 부호 비트 플립으로 신경망 최대 손상 적대적 공격 연구 (NVIDIA, arXiv 2502.07408, upvote 8) *(NEW)*
- [[ERNIE-Image]] — Baidu 8B Apache 2.0 텍스트-이미지 생성 모델, diffusers 기반 (HF 3,800 다운로드) *(NEW)*
- [[worldmonitor]] — koala73, AI 기반 실시간 지정학 인텔리전스 대시보드 (GitHub ⭐52,015) *(UPDATED)*
- [[TrendRadar]] — sansan0, AI 여론·트렌드 모니터링 + MCP 아키텍처 지원 (GitHub ⭐54,772) *(UPDATED)*
- [[RAG-Anything]] — HKUDS, 멀티모달 올인원 RAG 프레임워크 텍스트+이미지+코드+테이블 (GitHub ⭐18,456) *(UPDATED)*
- [[VoxCPM2]] — OpenBMB, 30개 언어 TTS + 음성 복제, Apache 2.0 (HF 81.7K 다운로드, 1,198 likes) *(UPDATED)*
- [[Kimi-K2.6]] — Moonshot AI, 1.1조 파라미터 멀티모달 MoE 모델 (HF 376K DL, 989 likes) *(UPDATED)*
- [[Agent-World]] — ByteDance Seed, 에이전트 학습용 실세계 환경 합성 대규모 확장 (HF 데일리 1위, upvote 42) *(NEW)*
- [[OneVL]] — Xiaomi Research, 단일 스텝 비전-언어 추론·계획 모델 (HF 데일리 2위, upvote 42) *(NEW)*
- [[EasyVideoR1]] — 비디오 이해 RL 적용 단순화 프레임워크 (HF 데일리 5위, upvote 9) *(NEW)*
- [[WebCompass]] — 멀티모달 웹 코딩 평가 벤치마크 (HF upvote 11) *(NEW)*
- [[OpenGame]] — 에이전트 기반 게임 코드 자동 생성·자동화 (HF 데일리 3위, upvote 8) *(NEW)*
- [[MultiWorld]] — HKU, 멀티에이전트 멀티뷰 비디오 월드 모델 (HF 데일리 4위, upvote 4) *(NEW)*
- [[extending-one-step-image-gen]] — 클래스 레이블→텍스트 조건 1-step 이미지 생성 확장, 판별적 텍스트 표현 활용 (HF 데일리 1위 2026-04-21, upvote 70) *(NEW)*
- [[ai-agents-for-beginners]] — Microsoft 공식 AI 에이전트 12강 Jupyter 실습 커리큘럼 (GitHub ⭐58,091) *(NEW)*
- [[claude-context]] — Zilliz 코드베이스 시맨틱 검색으로 코딩 에이전트 컨텍스트 주입, Milvus 기반 (GitHub ⭐9,167) *(UPDATED)*
- [[awesome-agent-skills]] — Claude Code·Cursor·Gemini CLI·Codex 호환 1000개+ 에이전트 스킬 큐레이션 (GitHub ⭐17,117) *(NEW)*
- [[agentspex]] — UIUC ScaleML Lab 에이전트 명세·실행 언어 SPEX, 형식적 에이전트 행동 정의 (HF 데일리 1위 2026-04-22, upvote 44) *(NEW)*
- [[tstars-tryon]] — Alibaba 다양한 패션 아이템 강건하고 사실적인 가상 피팅 시스템 (HF 데일리 2위 2026-04-22, upvote 29) *(NEW)*
- [[anyrecon]] — 비디오 디퓨전 모델 활용 임의 시점 3D 재구성, 단일/희소 뷰 입력 (HF 데일리 3위 2026-04-22, upvote 24) *(NEW)*
- [[cointeract]] — Alibaba 공간 구조화 공동 생성으로 물리 일관 인간-객체 상호작용 영상 합성 (HF 데일리 4위 2026-04-22, upvote 19) *(NEW)*
- [[tempo-ttt]] — 대형 추론 모델 테스트 타임 트레이닝 스케일링, 추론 중 온라인 학습 (HF 데일리 5위 2026-04-22, upvote 17) *(NEW)*
- [[gemma-4-e4b-obliterated]] — Gemma 4 4B abliteration + GGUF 양자화 커뮤니티 파인튠, 경량 무제한 로컬 추론 (HF 트렌딩 5위, 79K DL) *(NEW)*
- [[open-webui]] — 오픈소스 AI 채팅 인터페이스, Ollama·OpenAI API 등 다양한 LLM 백엔드 통합 (GitHub ⭐133,530) *(NEW)*
- [[langfuse]] — LLM 앱 오픈소스 관측성 플랫폼, 메트릭·평가·프롬프트 관리 통합 (GitHub ⭐25,791) *(NEW)*
- [[claude-code-templates]] — Claude Code 설정·모니터링 CLI, 에이전트 코딩 워크플로 템플릿 모음 (GitHub ⭐24,971) *(NEW)*
- [[last30days-skill]] — Reddit·X·YouTube·HN·Polymarket 멀티소스 자율 조사·종합 에이전트 스킬 (GitHub ⭐23,614) *(NEW)*
- [[vercel-skills]] — Vercel Labs 공식 AI 에이전트용 오픈 스킬 레지스트리, npx 한 줄 설치 (GitHub ⭐15,695) *(NEW)*
- [[swarms]] — 엔터프라이즈 프로덕션용 멀티에이전트 오케스트레이션 프레임워크 (GitHub ⭐6,471) *(NEW)*
- [[Pixelle-Video]] — AIDC-AI, AI 기반 쇼트 영상 자동 생성 엔진, 입력→완성 영상 파이프라인 자동화 (GitHub ⭐5,983) *(NEW)*
- [[shannon]] — KeygraphHQ, AI 화이트박스 웹 펜테스터, 소스코드 분석 후 공격 벡터 식별·익스플로잇 (GitHub ⭐39,847) *(NEW)*
- [[LLaDA2.0-Uni]] — 확산 기반 LLM으로 멀티모달 이해·생성 단일 모델 통합 (HF 85 upvotes) *(NEW)*
- [[DR-Venus]] — 10K 오픈 데이터로 훈련한 엣지 규모 딥 리서치 에이전트 (HF 25 upvotes) *(NEW)*
- [[Near-Future-Policy-Optimization]] — 근미래 보상 예측 활용 강화학습 정책 최적화 신기법 (HF 19 upvotes) *(NEW)*
- [[Reward-Hacking-Large-Models]] — 대형 모델 리워드 해킹 메커니즘·비정렬 현상 종합 분석 (HF 15 upvotes) *(NEW)*
- [[Spatial-Intelligence-Generative]] — 생성 모델 관점 공간 추론 능력 탐색·벤치마크 (HF 10 upvotes) *(NEW)*
- [[WavAlign]] — 적응형 하이브리드 후처리 훈련으로 음성 대화 모델 지능성·표현력 향상 (HF 9 upvotes) *(NEW)*
- [[Scaling-Test-Time-Agentic-Coding]] — Meta AI, 에이전틱 코딩에서 테스트 시점 연산 확장 분석 *(NEW)*
- [[ReImagine]] — 이미지 우선 합성 방식 고품질 인간 동작 영상 제어 생성 (HF 5 upvotes) *(NEW)*
- [[SWE-chat]] — 실제 사용자가 코딩 에이전트와 상호작용한 자연발생 데이터셋 (HF 3 upvotes) *(NEW)*
- [[Cortex-2.0]] — 실제 산업 현장 배포를 위한 세계 모델 그라운딩 방법론 (HF 3 upvotes) *(NEW)*
- [[Qwen3.6-27B]] — Qwen3.6 27B 덴스 멀티모달 모델, 이미지-텍스트 이해·생성 (509K DL, 764 likes) *(UPDATED)*
- [[openai-privacy-filter]] — OpenAI 공개 1B 토큰 PII 필터링 분류 모델, 57.7K DL *(UPDATED)*
- [[DeepSeek-V3]] — DeepSeek 공식 MoE LLM 레포, 오픈소스 대형 언어 모델 기준점 (GitHub ⭐103,231) *(NEW)*
- [[ClawMark]] — 멀티턴·멀티데이·멀티모달 AI 동료 에이전트 평가 벤치마크 (HF upvotes 80) *(NEW)*
- [[SkillsToTalent]] — 이질적 에이전트를 실제 회사 구조로 조직화하는 멀티에이전트 협업 프레임워크 (HF upvotes 57) *(NEW)*
- [[World-R1]] — 3D 제약 강화학습으로 텍스트→비디오 물리 일관성 향상 (HF upvotes 44) *(NEW)*
- [[ReVSI]] — VLM 3D 공간 추론 평가 프레임워크 재구성 (HF upvotes 36) *(NEW)*
- [[VLA-Safety]] — VLA 시스템 위협·도전·평가·방어 메커니즘 종합 조사 (HF upvotes 35) *(NEW)*
- [[Qwen3.6-27B-GGUF]] — unsloth Qwen3.6 27B GGUF 양자화, 로컬 추론 최적화 (131,398 DL) *(NEW)*
- [[DeVI]] — 합성 비디오 모방 학습으로 물리 기반 정밀 손-물체 상호작용 구현 (HF 12 upvotes) *(UPDATED)*
- [[Terminal-Agent-Context-Compression]] — MAP Research Group, 관찰 컨텍스트 압축 자기진화형 터미널 에이전트 효율화 (HF 5 upvotes) *(NEW)*
- [[Visual-Reasoning-Tool-RL]] — Amazon AGI, 도구 활용 강화학습으로 시각 추론 능력 향상 (HF 2 upvotes) *(NEW)*
- [[Open-Generative-AI]] — Flux·Midjourney·Sora 등 200개+ 생성 AI 무검열 오픈소스 통합 플랫폼 (GitHub ⭐7,902, +842 오늘) *(NEW)*
- [[DeepEP]] — DeepSeek 공식 MoE expert-parallel 통신 최적화 CUDA 라이브러리 (GitHub ⭐9,394) *(NEW)*
- [[LLaTiSA]] — 시각 인식→의미 이해 계층화 시계열 추론 벤치마크 (arXiv 2604.17295) *(NEW)*
- [[Co-Evolving-LLM-Agents]] — LLM 에이전트·스킬 뱅크 공진화로 장기 태스크 성능 향상 프레임워크 (arXiv 2604.20987) *(NEW)*
- [[free-claude-code]] — Alishahryar1, 터미널·VSCode·Discord에서 Claude Code 무료 사용 프록시 (GitHub ⭐12,012) *(UPDATED)*
- [[ml-intern]] — HuggingFace 공식 ML 엔지니어 에이전트, 논문 읽기·모델 학습·배포 자동화 (GitHub ⭐6,473) *(UPDATED)*
- [[WorldMark]] — 인터랙티브 비디오 월드 모델 통합 벤치마크 스위트 (HF 27 upvotes) *(NEW)*
- [[UniT-Humanoid-Policy]] — XPENG Robotics, 인간→휴머노이드 정책 학습 물리 언어 프레임워크 (HF 25 upvotes) *(NEW)*
- [[DeepSeek-V4-Pro]] — DeepSeek 862B 플래그십 텍스트 생성 모델, HF 트렌딩 1위 (174K DL) *(UPDATED)*
- [[StyleID-Facial-Identity]] — 스타일화 얼굴 신원 인식 인지 기반 데이터셋+메트릭 (HF 14 upvotes) *(NEW)*
- [[Seeing-Fast-and-Slow]] — 빠른/느린 시간 인식 분리 학습 시각 모델, System 1/2 비디오 이해 (HF 11 upvotes) *(NEW)*
- [[Hybrid-Policy-Distillation]] — LLM 추론 품질 유지 효율 정책 증류 하이브리드 방법론 (HF 8 upvotes) *(NEW)*
- [[rlm]] — alexzhang13, 재귀적 언어 모델(RLM) 추론 plug-and-play 라이브러리 (GitHub ⭐3,916) *(NEW)*
- [[mattpocock-skills]] — Matt Pocock, 실무 엔지니어용 Claude 에이전트 스킬 모음, .claude/ 즉시 적용 (GitHub ⭐32,812) *(UPDATED)*
- [[trycua-cua]] — Computer-Use 에이전트 오픈소스 샌드박스·SDK·벤치마크 인프라 (GitHub ⭐14,360) *(NEW)*
- [[beads]] — gastownhall, 코딩 에이전트용 메모리 업그레이드 레이어, 장기 기억 개선 (GitHub ⭐21,666) *(NEW)*
- [[awesome-codex-skills]] — ComposioHQ, Codex CLI 실무 워크플로우 자동화 검증 스킬 큐레이션 (GitHub ⭐1,960, +517 당일) *(NEW)*
- [[GitNexus]] — abhigyanpatwari, 서버 없이 클라이언트 사이드 코드베이스 지식 그래프 엔진 (GitHub ⭐32,105) *(UPDATED)*
- [[VLAA-GUI]] — GUI 자동화 멈춤·복구·검색 판단 모듈형 에이전트 프레임워크 (arXiv 2604.21375) *(NEW)*
- [[TingIS]] — 기업 규모 노이즈 인시던트 데이터 실시간 위험 이벤트 탐지 시스템 (arXiv 2604.21889) *(NEW)*
- [[Context-Unrolling]] — 옴니 모달 모델 순차 컨텍스트 언롤링으로 멀티모달 처리 효율 개선 (arXiv 2604.21921) *(NEW)*
- [[DeepSeek-V4-Flash]] — DeepSeek 158B 경량 고속 추론 최적화 텍스트 생성 모델 (HF 46K DL) *(NEW)*
- [[daily-stock-analysis]] — ZhuLinsen, LLM 기반 A주·홍콩·미국 주식 일일 분석 자동화, 기술지표+뉴스감성+차금흐름 (GitHub ⭐32,300) *(NEW)*
- [[recursive-multi-agent]] — 재귀적 구조 멀티 에이전트 시스템, 계층적 조율로 복잡 문제 해결 향상 (HF upvote 54) *(NEW)*
- [[DV-World]] — 실세계 시나리오 AI 에이전트 데이터 시각화 생성·해석 능력 벤치마크 (HF upvote 33) *(NEW)*
- [[test-driven-data-engineering]] — 테스트 주도 데이터 엔지니어링으로 원시 코퍼스에서 LLM 자기개선 데이터 자동 생성 (HF upvote 32) *(NEW)*
- [[refinement-via-regeneration]] — 재생성을 통한 수정 공간 확대, 통합 멀티모달 모델 이미지 정제 성능 향상 (HF upvote 22) *(NEW)*
- [[meta-cot-image-editing]] — 메타 체인오브생각으로 이미지 편집 세밀도+일반화 동시 개선, Tsinghua (HF upvote 22) *(NEW)*
- [[Qwen3-0.6B]] — 0.6B 경량 Qwen3 텍스트 생성 모델, 소형 디바이스 배포·빠른 추론 최적화 (HF 18.5M DL/월) *(NEW)*
- [[Qwen2.5-7B-Instruct]] — 7B 인스트럭션 튜닝, 코딩·수학·다국어 균형 성능, 로컬 배포 실용성 (HF 12.8M DL/월) *(NEW)*
- [[DeepSeek-V3.2]] — DeepSeek 685B MoE 플래그십 텍스트 생성 최신 버전, MIT 라이선스 (HF 11.3M DL/월) *(NEW)*

---

## domains
<!-- 도메인별 누적 인사이트 -->

- video-saas → `wiki/domains/video-saas.md` — 영상 AI SaaS 기능/워크플로우/경쟁 우위 분석
- ai-news → `wiki/domains/ai-news.md` — AI 뉴스, 툴 발굴, 워크플로우 통합 (2026-04-23 업데이트)

---

## blog
<!-- 발행된 블로그 글 -->

- [[AI영상자동화-SaaS-Higgsfield-2026]] — AI 영상 자동화 SaaS 완벽 가이드 (Higgsfield, Runway, Kling, Pika 비교)

---

## actionable
<!-- 당장 실행 가능한 항목 -->

`actionable.md` 참조. 대기 중: RTK CLI, AE MCP 테스트, .claude/ 자동화 훅 구성, VoxCPM TTS 테스트, VOID 모델 통합, Gemma-4-31B 벤치마크, hermes-agent 검토, **andrej-karpathy-skills CLAUDE.md 통합**, **MinerU2.5 wiki 파이프라인 통합**, **markitdown wiki pipeline 통합**, superpowers 테스트, Gemma-4-26B 로컬 실행, Gemma-4-E4B 테스트, **claude-code-best-practice + andrej-karpathy-skills 통합 CLAUDE.md 작성**, **claude-mem 설치 테스트**, **ai-hedge-fund 에이전트 아키텍처 분석** (20개)

---

## synthesis
<!-- 교차 도메인 통찰 -->

_소스 39개 누적됨 → 에이전트 프레임워크 클러스터(hermes-agent⭐61K, superpowers⭐147K, multica⭐8.4K) + LLM 인프라 클러스터(flash-attention, skypilot) synthesis 우선 작성 예정. LIO-SAM으로 slam-3dgs 도메인 첫 소스 확보._

---

## queries
<!-- 보존된 질문과 답변 -->

_아직 없음_
