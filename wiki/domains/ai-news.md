---
title: AI 뉴스 / GitHub 트렌딩 누적 인사이트
type: domain
domain: ai-news
tags: [ai-news, github-trending, workflow, tool, claude-code, agent-framework, tts, video-inpainting, MoE]
created: 2026-04-09
updated: 2026-04-22
sources: [instagram-저장-2026-02-2026-04.md, hermes-agent.md, DeepTutor.md, VoxCPM.md, Kronos.md, Archon.md, SkillClaw.md, When-Numbers-Speak.md, HY-Embodied.md, OpenSpatial.md, DMax.md, Gemma-4-31B.md, GLM-5.1.md, VOID-model.md, superpowers.md, multica.md, andrej-karpathy-skills.md, VibeVoice.md, TradingAgents.md, TimesFM.md, MinerU2.5.md, Gemma-4-26B.md, FORGE.md, WildDet3D.md, RefineAnything.md, EXAONE-4.5.md, Matrix-Game-3.0.md, claude-code-best-practice.md, claude-mem.md, ai-hedge-fund.md, ralph.md, ClawGUI.md, AttentionSink.md, OmniShow.md, StripsAsTokens.md, PseudoUnification.md, Uni-ViGU.md, MiniMax-M2.7.md, markitdown.md, openai-agents-python.md, cognee.md, HY-World-2.0.md, DR3-Eval.md, RAD-2.md, HiVLA.md, ASGuard.md, HY-Embodied-0.5.md, Qwen3.6-35B-A3B.md, omi.md, how-to-fine-tune-reasoning-model.md, chrome-devtools-mcp.md, DeepGEMM.md, evolver.md, claude-desktop-debian.md, thunderbolt.md, GlobalSplat.md, Dive-into-Claude-Code.md, UniDoc-RL.md, TRACER.md, Switch-KD.md, Representations-Before-Pixels.md, LeapAlign.md, OmniVoice.md]
---

# AI 뉴스 / GitHub 트렌딩 누적 인사이트

목표: 쓸모있는 AI 도구 발굴 + 내 워크플로우에 통합

---

## 내 워크플로우에 당장 통합 가능한 것

### .claude/ 폴더 최적화 (즉시 적용)
- CLAUDE.md에 역할/규칙 명확히 → Claude 자율성 향상
- 트렌드 레이더 + 자동 커밋 훅 설정 → 콘텐츠 자동화 파이프라인
- → [[Claude-Code-워크플로우]]

### RTK CLI 프록시 (즉시 적용)
- Claude Code 토큰 소비 90% 절감 주장
- @codingknowledge: "high-performance CLI proxy that filters and compresses command outputs"
- 신뢰도: ⭐⭐ (독립 검증 필요하나 원리는 타당)

### After Effects MCP (즉시 테스트 가능)
- 자연어로 AE 제어 → 모션 디자인 워크플로우 자동화
- → [[After-Effects-MCP]]

---

## 6개월 내 영향력 있을 것

### Mamba4 (SSM 아키텍처)
- Transformer O(n²) → Mamba O(n) 선형 시간
- 긴 컨텍스트(문서, 영상, 오디오) 처리 효율 향상
- 채택 시 로컬 LLM의 긴 컨텍스트 처리 가능성 ↑
- → [[Mamba4]]

### Newton 물리 엔진 (NVIDIA + DeepMind + Disney)
- 로봇 훈련 70x 가속
- "Open sourced Newton, a physics engine that can train robots 70x faster"
- → 로봇틱스 도메인 확장 시 주시

### MiroShark 스웜 인텔리전스
- 500 에이전트가 하나의 문서를 서로 다른 관점에서 분석
- "Open-source swarm intelligence engine"
- → 리서치 자동화, 다각도 분석에 활용 가능

### AI Scientist (Sakana AI)
- 연구 주제 선정 → 논문 작성까지 AI가 자율 수행
- Nature 논문으로 발표됨 (2026-03)

---

## 현재 쓰는 도구 대체/강화 후보

| 기존 도구/방식 | AI 대체 도구 | 상태 |
|---|---|---|
| SaaS 구독 (다수) | Claude Code 자체 제작 | 이미 실증됨 (SaaS 25개 대체) |
| PPT 수동 제작 | Calamus PPT AI | 테스트 필요 |
| 디자인 제안서 | Manus AI | @kyeongahko 후기 있음 |
| AE 수동 키프레임 | After Effects MCP | 테스트 필요 |
| 거래 분석 | Claude + TradingView MCP | 참고용 |

---

## 과장 대비 실제 능력 검증

### Seedance 2.0 "100x better than Sora 2"
- 소셜미디어 마케팅 클레임
- → 직접 테스트 전까지 ⭐⭐ 신뢰도 유지

### RTK "90% 토큰 절감"
- 원리는 타당 (출력 필터링/압축)
- → 실측 전까지 50~70% 절감으로 보수적 예상

### AI 아바타 "경험 없어도 가능"
- 실제로는 프롬프트 엔지니어링 + 편집 스킬 필요
- 진입 장벽 낮아진 것은 사실, 완전 무경험은 과장

---

## 2026-04-10 업데이트: GitHub Trending + HF 급상승

### 에이전트 프레임워크 트리플 등장 (주목)
하루에 3개 에이전트 관련 항목 동시 트렌딩 — 에이전트 인프라 경쟁 결정적 국면 진입.
- [[hermes-agent]] (⭐10,999) — NousResearch 오픈소스 에이전트
- [[Archon]] (⭐12,392) — AI 코딩 결정론화 하네스
- [[SkillClaw]] — 집단 스킬 진화 논문 (HF upvotes 109)

### 오픈소스 TTS 강자
- [[VoxCPM]] (⭐14,227) — 토크나이저 없는 TTS. reat-voice ElevenLabs 대체 후보

### Netflix 비디오 인페인팅 오픈소스
- [[VOID-model]] — 객체 제거·인페인팅, Apache 2.0. 영상 편집 자동화 즉시 적용 가능

### Gemma 4 31B 멀티모달 오픈소스
- [[Gemma-4-31B]] — 1.6M 다운로드, Apache 2.0. 오픈소스 VLM 기준 재정의

### Zhipu AI GLM-5.1 (MoE 753B)
- [[GLM-5.1]] — Monday(GLM-5-Turbo) 기반 모델 계열 최신작. 한국어+영어 MIT

### 교육 AI
- [[DeepTutor]] (⭐8,046) — 에이전트 기반 적응형 튜터링

### 논문 클러스터 (slam-3dgs 교차)
- [[OpenSpatial]] — 3D 공간 이해 데이터 엔진 → slam-3dgs 도메인 연관
- [[HY-Embodied]] — 실세계 로봇 소형 모델 → slam-3dgs 도메인 연관
- [[DMax]] — 확산 LLM 병렬 디코딩 → local-llm 도메인 연관
- [[When-Numbers-Speak]] — T2V 숫자 정렬 → video-saas 도메인 연관

---

## 2026-04-11 업데이트: GitHub Trending + HF 급상승

### hermes-agent 스타 5배 폭등 (특이 신호)
24시간 만에 10,999 → 54,205스타. 에이전트 프레임워크 수요가 임계점 도달 — 단순 관심이 아닌 대규모 채택 국면.
- [[hermes-agent]] (⭐54,205, +7,671 당일) — 트렌딩 1위

### 에이전트 생태계 추가 확장
- [[superpowers]] (⭐146,198, +2,150) — Shell 기반 스킬 프레임워크. 언어 독립, 초경량 — **즉시 테스트 대상**
- [[multica]] (⭐6,713, +1,506) — 매니지드 에이전트 플랫폼, 팀 워크플로우 통합

### Claude Code 실무 채택 주류화 신호
- [[andrej-karpathy-skills]] (⭐12,083, +1,450) — Karpathy 관찰 기반 단일 CLAUDE.md. **즉시 현재 설정에 통합 검토**

### DeepTutor 이틀 연속 급상승
- [[DeepTutor]] (⭐16,205, +1,424) — 교육 AI 지속 관심. 이틀 연속 트렌딩은 일시적 관심 아닌 실질 수요

### 시계열·금융 AI 클러스터 (3종 동시)
같은 날 시계열/금융 AI 관련 논문 3종 트렌딩 → [[시계열-예측-파운데이션-모델]] 도메인 본격 형성.
- [[TimesFM]] (Google Research) — 제로샷 시계열, 즉시 HF 사용 가능
- [[TradingAgents]] — 멀티에이전트 트레이딩, 백테스트 결과 우수
- [[Kronos]] — 120억 K-line 학습, arXiv 논문 공개 확인

### 음성 합성 진화
- [[VibeVoice]] — 장시간(90분) 다화자 TTS, next-token diffusion

### 문서 파싱 SOTA
- [[MinerU2.5]] (1.2B VLM) — PDF·수식·표 파싱 SOTA. **wiki 인제스트 파이프라인 통합 우선 검토**

### Gemma 4 MoE 로컬 실행 가능
- [[Gemma-4-26B]] (활성 4B) — 일반 GPU로 멀티모달 로컬 실행 가능

---

---

## 2026-04-13 업데이트: GitHub Trending + HF 급상승

### Claude Code 에코시스템 폭발 (3종 동시 트렌딩 — 중요 신호)
Claude Code 관련 툴이 하루에 3개 동시 트렌딩 — Claude Code가 개발자 주류 도구로 완전히 자리잡은 증거.
- [[claude-code-best-practice]] (⭐39,886, +1,548) — 커뮤니티 집대성 모범 사례 모음. **andrej-karpathy-skills보다 2배 스타**
- [[claude-mem]] (⭐51,057, +753) — 세션 간 컨텍스트 AI 압축·주입 플러그인. 메모리 연속성 문제 해결 직접 대응
- [[andrej-karpathy-skills]] (⭐18,844, +2,369) — 12K → 18K (+56%) 지속 상승

> [!action] 당장 할 것
> claude-code-best-practice + andrej-karpathy-skills 두 레포를 함께 읽고 현재 CLAUDE.md에 통합 가능한 패턴 추출. claude-mem은 wiki 세션에 설치 테스트.

### hermes-agent 3일 연속 트렌딩 1위
- [[hermes-agent]] (⭐71,898, +7,454) — 61K → 71K (+17%). 3일 연속 1위는 단순 반짝 아닌 에이전트 프레임워크 실질 채택 국면 확인

### Kronos 금융 AI 스타 폭등 (+130%)
- [[Kronos]] (⭐16,335, +1,985) — 7K → 16K, 이틀 만에 2배 이상. [[ai-hedge-fund]](52K⭐)와 함께 금융 AI 클러스터 견고화

### AI 에이전트 루프 신규
- [[ralph]] (⭐16,181, +463) — PRD 항목 완료까지 자율 반복 실행. 에이전트 자율성 접근의 단순화 버전

### 논문 클러스터 (2026-04-13 HF Daily Papers)
- [[FORGE]] — 제조 VLM 평가 벤치마크 (업보트 50, Waterloo)
- [[WildDet3D]] — 실환경 오픈 어휘 3D 탐지 (업보트 36, Ai2) → slam-3dgs 교차
- [[RefineAnything]] — 이미지 지역별 리파인 (업보트 29) → video-saas 편집 연관
- [[EXAONE-4.5]] — LG AI Research LLM 보고서 (업보트 24) → 국내 엔터프라이즈 LLM 경쟁
- [[Matrix-Game-3.0]] — 실시간 스트리밍 인터랙티브 월드 모델 (업보트 21) → video-saas 미래 방향

### 모델 다운로드 급상승
- [[GLM-5.1]] — 28.8K → 35,900 다운로드 (+25%)
- [[Gemma-4-31B]] — 2M → 2,440,000 다운로드

---

## 2026-04-14 업데이트: GitHub Trending + HF 급상승

### hermes-agent 4일 연속 1위 — 역대급 성장
- [[hermes-agent]] (⭐80,633, +8,735 today) — 71K → 80K (+12%). 4일간 총 26,428 스타 증가. 이 속도는 GitHub 역사에서 손에 꼽히는 수준.

> [!insight] 핵심 인사이트
> hermes-agent의 4일 연속 1위는 **에이전트 프레임워크가 선택지에서 표준으로 전환됐다**는 신호. LangChain이 2022년에 겪은 폭발과 동일한 패턴 — 단, 3배 빠른 속도.

### andrej-karpathy-skills 폭발 (+132%)
- [[andrej-karpathy-skills]] (⭐28,000, +9,156 today) — 12K → 28K. Karpathy 이름 효과 + Claude Code 주류화 맞물린 결과.

### MiniMax-M2.7 신규 등장
- [[MiniMax-M2.7]] — 229B MoE, 43,600 다운로드 (출시 1일). 중국계 오픈소스 LLM 경쟁([[GLM-5.1]] vs MiniMax vs Qwen) 한층 심화.

### GLM-5.1 다운로드 3배 폭증
- [[GLM-5.1]] — 28.8K → 84,800 다운로드 (+195%). likes 1,160. HF 트렌딩 1위 유지.

### 영상 생성 논문 클러스터 (video-saas 교차)
- [[OmniShow]] — ByteDance HOI 영상 생성 (업보트 35). 인간-사물 상호작용 장면 특화.
- [[Uni-ViGU]] — 영상 생성+이해 통합 단일 모델 (업보트 33). 생성→분석 파이프라인 단축.

### 해석·메서드 논문 클러스터
- [[ClawGUI]] — GUI 에이전트 통합 프레임워크 (업보트 41, arXiv 2604.11784)
- [[AttentionSink]] — 트랜스포머 어텐션 싱크 종합 서베이 (업보트 39, 20인 저자)
- [[PseudoUnification]] — 멀티모달 모델 엔트로피 프로빙 (업보트 31, HKUST)

### 3D 메시 생성 발전
- [[StripsAsTokens]] — 네이티브 UV 분할 아티스트급 메시 생성 (업보트 33). [[AI-3D-생성]] 도메인 발전.

### 기존 레포 지속 상승
- [[markitdown]] (⭐107,555, +4,548) — Microsoft 문서→마크다운 변환기 10만 돌파 안정화
- [[claude-mem]] (⭐54,157, +3,100) — 세션 메모리 플러그인 지속 상승
- [[multica]] (⭐11,700, +3,273) — 매니지드 에이전트 플랫폼 가파른 성장

---

## 2026-04-17 업데이트: GitHub Trending + HF 급상승

### 에이전트 메모리 클러스터 등장 (주목 신호)
에이전트 메모리 관련 항목 2종 동시 트렌딩 — 에이전트 인프라에서 **메모리 레이어**가 다음 전선으로 부상.
- [[openai-agents-python]] (⭐21,420, +172 today) — OpenAI 공식 멀티에이전트 SDK. 경량 설계로 표준화 포지션
- [[cognee]] (⭐15,974, +170 today) — 그래프 기반 에이전트 메모리. "6줄 코드" API

> [!insight] 핵심 인사이트
> OpenAI가 직접 경량 에이전트 프레임워크를 공식화 — [[hermes-agent]](61K⭐)·[[superpowers]](147K⭐) 등 서드파티 경쟁자와 정면 대결. 동시에 [[cognee]] 같은 메모리 엔진이 부상하는 것은 **에이전트 = 코어 + 메모리 레이어** 구조가 표준으로 굳어지는 과정.

### 기존 레포 지속 성장
- [[claude-mem]] (⭐60,473, +1,897 today) — 세션 메모리 플러그인 60K 돌파
- [[dive-into-llms]] (⭐31,035, +1,385 today) — LLM 교육 튜토리얼 31K 돌파
- [[genericagent]] (⭐3,052, +872 today) — 자기진화 에이전트 3K 돌파

### MiniMax-M2.7 다운로드 급증
- [[MiniMax-M2.7]] — 85,500 → 143,000 다운로드 (+67%). 출시 3일 만에 1.5배.

### Tencent Embodied AI 공세
- [[HY-World-2.0]] — 단일 모델로 3D 세계 재구성·생성·시뮬레이션 통합 (upvote 39) → slam-3dgs·video-saas 교차
- [[HY-Embodied-0.5]] — 4B 파라미터 embodied AI 모델 (HF 트렌딩 2위, 다운로드 1,060) → slam-3dgs 교차

### Qwen MoE 효율화
- [[Qwen3.6-35B-A3B]] — 35B 총 파라미터, 활성 3B로 효율 추론 (HF 트렌딩 3위). [[Gemma-4-26B]](활성 4B)와 같은 경량 MoE 경쟁 심화

### HF 논문 클러스터 (2026-04-17)
- [[DR3-Eval]] — deep research 에이전트 현실적 평가 프레임워크 (upvote 18). 에이전트 벤치마크 표준화 수요 지속
- [[RAD-2]] — 생성기-판별기 구조 RL 스케일링 (upvote 17) → 영상 생성 훈련 방법론
- [[HiVLA]] — 계층적 VLA 로봇 조작 (upvote 15) → slam-3dgs 교차
- [[ASGuard]] — 활성화 스케일링 jailbreak 방어 (upvote 13)

---

---

## 2026-04-18 업데이트: GitHub Trending + HF 수집

### superpowers ⭐158,202 — 역대급 폭증
- [[superpowers]] (⭐158,202, +10,679 vs 어제) — 에이전트 스킬 프레임워크 전체 1위 유지. Claude Code 생태계 직접 연결.

### Chrome DevTools MCP 공식화 — 브라우저 제어 표준화
- [[chrome-devtools-mcp]] (⭐35,992) — Chrome DevTools 공식팀 MCP 서버 공개. LLM이 브라우저 DevTools에 직접 접근.

> [!insight] 핵심 인사이트
> DevTools 공식 MCP 공개는 "코딩 에이전트의 디버깅 루프 완성" 신호 — 에이전트가 코드 작성→실행→브라우저 오류 확인→수정을 자동 수행 가능.

### HF 모델 트렌딩 (2026-04-18)
- [[Gemma-4-31B]] — 3,780,000 다운로드 (HF 1위). Google Gemma 4 멀티모달 대규모 채택.
- [[MiniMax-M2.7]] — 258,000 다운로드 (HF 2위). 229B MoE 오픈소스 최상위권.
- [[GLM-5.1]] — 104,000 다운로드 (HF 3위). [[Zhipu AI]] GLM 시리즈 지속 성장.

---

## 2026-04-19 업데이트: GitHub Trending + HF 수집

### DeepGEMM — LLM 추론 커널 오픈소스화
- [[DeepGEMM]] (⭐6,587) — DeepSeek FP8 GEMM 커널 공개. 동일 하드웨어 추론 처리량 향상.

### 에이전트 자기진화 / 개방형 AI
- [[evolver]] (⭐5,147) — Genome Evolution Protocol 기반 에이전트 자기진화. 수동 프롬프트 엔지니어링 대체 시도.
- [[thunderbolt]] (⭐1,735) — Thunderbird 내장 AI, 벤더 종속 없는 모델 선택. "모델 주권" 오픈소스 대표 사례.
- [[claude-desktop-debian]] (⭐3,515) — Linux Claude Desktop 비공식 패키징. MCP 생태계 Linux 확장.

### HF 논문 클러스터 (2026-04-19)
- [[GlobalSplat]] — 3DGS 단일 피드포워드 패스 (upvote 18). slam-3dgs × ai-news 교차.
- [[Dive-into-Claude-Code]] — Claude Code 에이전트 설계 공간 분석 (upvote 13). 아키텍처 이해 필독.
- [[Representations-Before-Pixels]] — 의미론적 계층 영상 예측 (upvote 7). 영상 생성 품질 향상.
- [[LeapAlign]] — ByteDance Seed 플로우 매칭 사후 정렬 (upvote 7). 이미지/영상 생성 품질.

> [!insight] 핵심 인사이트
> 2026-04-19: "브라우저 제어(chrome-devtools-mcp) + 추론 커널(DeepGEMM) + 3DGS 가속(GlobalSplat)" 3종이 같은 날 — 에이전트 실행 스택(도구 사용), 연산 효율(인프라), 공간 인식(지각) 3계층이 동시 발전하는 수렴 신호.

### HF 모델 트렌딩 (2026-04-19)
- [[Gemma-4-26B]] — 2,780,000 다운로드 (HF 1위). Google Gemma 4 27B MoE, 이미지·텍스트.
- [[Gemma-4-E4B]] — 2,120,000 다운로드 (HF 2위). Google Gemma 4 8B Any-to-Any 멀티모달.
- [[OmniVoice]] — 958,000 다운로드 (HF 3위). 다국어 TTS, [[VoxCPM]] 대비 광범위 다국어 지원.

---

## 관련 페이지

- [[Claude-Code-워크플로우]] — Claude Code 심화
- [[바이브코딩]] — 비개발자 앱 개발
- [[After-Effects-MCP]] — AE 자동화
- [[Mamba4]] — SSM 아키텍처
- [[AI-에이전트-프레임워크]] — 에이전트 인프라 개념 페이지
- [[시계열-예측-파운데이션-모델]] — TimesFM, Kronos 클러스터 (NEW)
- [[금융-AI]] — TradingAgents, Kronos, TimesFM (NEW)
- [[Zhipu AI]] — GLM/Monday 기반 모델 회사
- [[NousResearch]] — hermes-agent 개발사
- [[Andrej Karpathy]] — karpathy-skills 출처
- [[claude-code-best-practice]] — Claude Code 모범 사례 집대성
- [[claude-mem]] — 세션 간 메모리 연속성 플러그인
- [[ai-hedge-fund]] — AI 에이전트 헤지펀드 시뮬레이터
- [[ralph]] — 자율 AI 에이전트 루프
- [[ClawGUI]] — GUI 에이전트 통합 프레임워크
- [[AttentionSink]] — 어텐션 싱크 종합 서베이
- [[OmniShow]] — ByteDance HOI 영상 생성
- [[StripsAsTokens]] — 네이티브 UV 분할 3D 메시
- [[PseudoUnification]] — 멀티모달 모델 엔트로피 프로빙
- [[Uni-ViGU]] — 영상 생성+이해 통합 모델
- [[MiniMax-M2.7]] — MiniMax 229B MoE 모델
- [[chrome-devtools-mcp]] — Chrome DevTools MCP 서버
- [[DeepGEMM]] — DeepSeek FP8 GEMM 커널
- [[OmniVoice]] — 다국어 고품질 TTS
- [[GlobalSplat]] — 피드포워드 3DGS (slam-3dgs 교차)

---

## 2026-04-15 업데이트: GitHub Trending + HF 급상승

### hermes-agent 5일 연속 트렌딩 — ⭐87,101
- [[hermes-agent]] (⭐87,101, +8,301 today) — 80K → 87K. NousResearch 에이전트 프레임워크 5일 연속 1위 유지.

### andrej-karpathy-skills 지속 폭등 — ⭐37,597
- [[andrej-karpathy-skills]] (⭐37,597) — 28K → 37K (+35%). Claude Code 최적화 CLAUDE.md 수요 지속.

### claude-mem + ai-hedge-fund 성장
- [[claude-mem]] (⭐56,602, +2,997 today) — 세션 메모리 플러그인 지속 성장
- [[ai-hedge-fund]] (⭐54,543, +1,007 today) — AI 헤지펀드 시뮬레이터 지속 관심

### ClawGUI 업보트 급등 (41 → 307)
- [[ClawGUI]] 업보트 307으로 재부상 — GUI 에이전트 관심 급증

### HF 논문 클러스터 (2026-04-15)
- [[hierarchical-svg-tokenization]] — SVG 계층 토크나이징 (업보트 224, Tencent Hunyuan)
- [[block-diffusion-speculative-decoding]] — 블록 확산 드래프트 트리 투기적 디코딩 가속 (업보트 177)
- [[lary-benchmark]] — 비전-액션 잠재 행동 표현 벤치마크 (업보트 18, Meituan)
- [[knowrl]] — 지식 가이드 RL로 LLM 추론 향상 (업보트 14, Tianjin)

### HF 모델 — 실용 다운로드 톱3 (2026-04-15)
- [[all-MiniLM-L6-v2]] — 22.7M 파라미터 문장 임베딩, **198M 다운로드/월** (RAG 표준 선택지)
- [[bert-base-uncased]] — Google BERT 110M, **65.1M 다운로드/월** (분류 파인튜닝 기준)
- [[nsfw-image-detection]] — NSFW 이미지 분류, **37.9M 다운로드/월** (콘텐츠 필터 즉시 사용)

> [!insight] 핵심 인사이트
> 2026-04-15의 핵심: 고다운로드 임베딩/분류 모델(all-MiniLM, BERT, NSFW) 수집은 **인프라 레이어 표준화** 신호. 화려한 신모델보다 검증된 실용 모델 수요가 구조적으로 높다.

---

## 2026-04-16 업데이트: GitHub Trending + HF 급상승

### 신규 GitHub Trending
- [[dive-into-llms]] (⭐29,991, +941 today) — 《动手学大模型》 LLM 실습 튜토리얼, Jupyter Notebook 기반
- [[magika-google]] (⭐14,010, +768 today) — Google AI 파일 타입 감지, Apache 2.0, VirusTotal 실사용 검증
- [[claude-code-game-studios]] (⭐10,867, +612 today) — Claude Code 49에이전트·72워크플로우 게임 스튜디오 변환
- [[open-agents-vercel]] (⭐2,820, +915 today) — Vercel 공식 에이전트 빌딩 템플릿, 신규 급등
- [[genericagent]] (⭐2,198, +446 today) — 자기진화 에이전트, 토큰 소비 6배 절감 주장

### Gemma 4 시리즈 다운로드 급성장
- [[Gemma-4-31B]] — 2.89M 다운로드 (2026-04-16)
- [[Gemma-4-26B]] — 2.2M 다운로드 (2026-04-16)

### MiniMax-M2.7 다운로드 급성장
- [[MiniMax-M2.7]] — 85,500 다운로드 (출시 이후 2배+)

### HF 논문 클러스터 (2026-04-16)
- [[rational-rewards]] — 추론 보상으로 시각 생성 스케일링 (업보트 63)
- [[seedance-2]] — ByteDance Seedance 2.0 복잡 세계 영상 생성 (업보트 62) → video-saas 교차
- [[spatialevo]] — 결정론적 기하학 환경 기반 공간 지능 자기진화 (업보트 46, 19인 저자) → slam-3dgs 교차
- [[gameworld]] — 멀티모달 게임 에이전트 표준 평가 벤치마크 (업보트 42, NUS)
- [[occubench]] — 실세계 직업 전문 태스크 에이전트 평가 벤치마크 (업보트 38, Qwen/Alibaba)

> [!insight] 핵심 인사이트
> 2026-04-16 핵심: Claude Code 에코시스템 확장이 게임 개발 도메인까지 침투(claude-code-game-studios ⭐10K). 동시에 에이전트 벤치마크(GameWorld, OccuBench)가 쏟아지는 것은 "에이전트 성능 측정 표준화" 수요가 임계점에 달했다는 신호.

---

## 2026-04-20 업데이트: GitHub Trending + HF 수집

### SuperAgent 대형 오픈소스 등장 — deer-flow
- [[deer-flow]] (⭐62,817, +190 today) — ByteDance 오픈소스 장기 작업 SuperAgent. 샌드박스+메모리+서브에이전트 내장. **Perplexity Deep Research 직접 대항마.**

> [!insight] 핵심 인사이트
> deer-flow는 에이전트 프레임워크 경쟁의 다음 단계: 단순 API 래퍼 → 분 단위 장기 작업 자율 수행. [[openai-agents-python]](23K), [[hermes-agent]](61K+)와 함께 "에이전트 3대 축"이 완성됐다는 신호.

### 새로운 AI 감지 도메인 — WiFi DensePose
- [[RuView]] (⭐47,701) — WiFi 신호만으로 실시간 인체 자세 추정+바이탈+존재 감지. 카메라 없는 프라이버시 친화형 AI 센싱. 실용화 여부 검증 필요.

### LLM 학습 입문 표준
- [[minimind]] (⭐47,657, +214 today) — 64M GPT를 2시간 만에 학습. LLM 내부 구조 이해의 오픈소스 표준.

### 개인화 VLM 메모리
- [[PersonaVLM]] — 사용자 페르소나 장기 기억 개인화 멀티모달 VLM (HF upvote 19). **[[에이전트-메모리-레이어]]** 패턴의 VLM 특화 구현.

### 금융 AI 계속 성장
- [[FinceptTerminal]] (⭐7,497+1,254) — AI 통합 터미널 기반 금융 분석 CLI. [[금융-AI]] 도메인 지속 확장.

### 추론 비용 절감 논문 2종 동시
- [[CutYourLosses]] — 병렬 추론 불필요 경로 조기 제거 (upvote 16)
- [[W-RAC]] — 웹 RAG 청크 분할 최적화 (upvote 14)
→ "추론 비용 절감 + 검색 효율화"가 2026-04-20의 기술 핵심 축.

### 기타
- [[Qwen3.5-Omni]] — 전방위 모달리티 통합 기술보고서 (upvote 9)
- [[MaximalBrainDamage]] — 부호 비트 플립 최대 손상 공격 (NVIDIA, upvote 8)
- [[ERNIE-Image]] — Baidu 텍스트-이미지 생성, Apache 2.0 (HF 3.8K 다운로드)

---

## 2026-04-21 업데이트: GitHub Trending + HF 수집

### AI 인텔리전스 모니터링 2종 동시 — 신호
AI가 실시간 뉴스·여론을 자동 수집·분석하는 도구가 같은 날 2종 급상승 — **정보 수집 자동화**가 다음 주목 도메인으로 부상.
- [[worldmonitor]] (⭐53,142, +316 today) — 지정학 뉴스 AI 인텔리전스 대시보드
- [[TrendRadar]] (⭐53,142, +604 today) — 멀티플랫폼 여론·트렌드 모니터링 + **MCP 아키텍처 지원**

> [!insight] 핵심 인사이트
> TrendRadar의 MCP 지원은 핵심 차별점 — Claude Code에서 직접 실시간 트렌드 데이터를 도구로 호출 가능. 에이전트 + 실시간 정보 수집이 MCP로 결합되는 패턴의 본격 등장.

> [!action] 당장 할 것
> TrendRadar MCP 서버를 Claude Code에 통합 테스트. RSS + AI 필터링 파이프라인을 wiki 자동 수집에 연결.

### FinceptTerminal 폭등 (+3,109 오늘)
- [[FinceptTerminal]] (⭐10,259, +3,109 today) — AI 금융 분석 CLI. 어제 1,254 → 오늘 3,109 급등. 금융 AI 관심 폭발.

### RAG 올인원 프레임워크
- [[RAG-Anything]] (⭐16,457, +245 today) — 텍스트·이미지·코드·테이블 통합 RAG. [[MinerU2.5]]·[[markitdown]]과 통합하면 범용 멀티모달 지식 수집 파이프라인 완성.

> [!action] 당장 할 것
> RAG-Anything을 이 vault 파이프라인에 통합 — Query 작업을 단순 파일 읽기에서 의미 검색으로 고도화.

### 오픈소스 TTS 신작 — VoxCPM2
- [[VoxCPM2]] (HF ⭐1,198 likes, 66.6K 다운로드, Apache 2.0) — 30개 언어 지원 + 음성 복제. [[OmniVoice]](1M+ 다운로드) 대항마. **즉시 한국어 TTS 테스트 권장.**

### 대규모 MoE 모델 경쟁 — Kimi-K2.6
- [[Kimi-K2.6]] — Moonshot AI 1.1조 파라미터 MoE (HF 506 likes). 실제 활성 파라미터 미공개. [[GLM-5.1]](753B)·[[MiniMax-M2.7]](229B) 대비 규모 경쟁.

> [!warning] 주의
> 1.1조 파라미터는 MoE 총 파라미터 — 실제 추론 시 활성 파라미터와 성능 검증 없이 채택 판단 금지.

### HF 논문 클러스터 (2026-04-21 Daily Papers)
- [[Agent-World]] — ByteDance Seed 에이전트 환경 합성 대규모 확장 (upvote 42) ← **데일리 1위**
- [[OneVL]] — Xiaomi 단일 스텝 비전-언어 추론+계획 (upvote 42) ← **데일리 2위**
- [[EasyVideoR1]] — 비디오 이해 RL 적용 단순화 (upvote 9). video-saas 파인튜닝 연관
- [[WebCompass]] — 멀티모달 웹 코딩 평가 벤치마크 (upvote 11). 웹 개발 LLM 선택 기준
- [[OpenGame]] — 게임 코드 에이전트 자동화 (upvote 8). [[claude-code-game-studios]] 학술 기반
- [[MultiWorld]] — HKU 멀티에이전트 멀티뷰 월드 모델 (upvote 4)

### HF 모델 트렌딩 (2026-04-21)
- [[Kimi-K2.6]] — HF 트렌딩 2위 (506 likes)
- [[MiniMax-M2.7]] — 314,000 다운로드 (↑ 143K → 314K)
- [[Qwen3.6-35B-A3B]] — 335,000 다운로드 (HF 트렌딩)
- [[Gemma-4-E4B]] — 2,570,000 다운로드 (HF 트렌딩 상위)
- [[VoxCPM2]] — 66,600 다운로드 (HF 트렌딩 11위, 1,198 likes)

> [!insight] 핵심 인사이트
> 2026-04-21 핵심: **"정보 수집 자동화(worldmonitor+TrendRadar) + RAG 멀티모달화(RAG-Anything) + 에이전트 훈련 환경(Agent-World)"** 3종이 같은 날 — AI가 실세계 데이터를 수집→저장→학습하는 전체 파이프라인이 오픈소스로 완성되는 전환점.

---

## 2026-04-22 업데이트: GitHub Trending + HF 수집

### 에이전트 교육·스킬 생태계 트리플 등장
에이전트를 만들고(ai-agents-for-beginners), 스킬을 공유하고(awesome-agent-skills), 코드베이스와 연결하는(claude-context) 3계층 에이전트 생태계 인프라가 하루에 완성되는 신호.
- [[ai-agents-for-beginners]] (⭐58,091, +200 today) — Microsoft 공식 12강 에이전트 실습 커리큘럼
- [[awesome-agent-skills]] (⭐17,117, +139 today) — Claude Code·Cursor·Gemini 호환 1000개+ 스킬 큐레이션
- [[claude-context]] (⭐6,878, +169 today) — Zilliz 코드베이스 시맨틱 검색, Claude Code 컨텍스트 주입

> [!insight] 핵심 인사이트
> 에이전트 생태계가 **학습 → 스킬 재사용 → 코드베이스 통합** 3계층으로 성숙 중. [[microsoft/ai-agents-for-beginners]]가 입문 표준이 되고, [[awesome-agent-skills]]가 스킬 마켓플레이스 역할, [[claude-context]]가 대규모 코드베이스 연결 인프라 담당.

### FinceptTerminal GitHub Trending 1위 — 금융 AI 폭발
- [[FinceptTerminal]] (⭐12,144, +2,548 today) — **GitHub Trending 오늘 1위**. 어제 10,259 → 오늘 12,144. AI 금융 분석 터미널. 단기간 스타 급등은 투자자·트레이더 커뮤니티 확산 신호.

> [!action] 당장 할 것
> FinceptTerminal 설치 테스트 — CLI에서 실시간 금융 데이터 조회 + LLM 분석 연동 품질 확인.

### HF 논문 클러스터 (2026-04-22 Daily Papers)

**AgentSPEX (데일리 1위, upvote 44)**
- [[agentspex]] — UIUC ScaleML Lab. 에이전트 행동을 형식 명세 언어로 정의·실행. 자연어 프롬프트 기반 에이전트의 비결정성 문제에 대한 학술적 접근.

**패션 AI + 영상 합성 클러스터 (Alibaba 2종 동시)**
- [[tstars-tryon]] — Alibaba 가상 피팅 1.0 (upvote 29). 복잡 패턴 의류 처리 강화.
- [[cointeract]] — Alibaba 물리 일관 HOI 영상 합성 (upvote 19). Alibaba가 같은 날 패션·영상 2종 발표 — 이커머스 AI 파이프라인 구축 의도.

**3D 재구성 (slam-3dgs 교차)**
- [[anyrecon]] — 비디오 디퓨전 활용 임의 시점 3D 재구성 (upvote 24). 단일 이미지 → 3D, [[GlobalSplat]]과 함께 3D 재구성 2방향 수렴.

**추론 비용 연구**
- [[tempo-ttt]] — 대형 추론 모델 테스트 타임 트레이닝 스케일링 (upvote 17). 추론 중 온라인 학습 방향.

**1-step 이미지 생성 (2026-04-21 데일리 1위)**
- [[extending-one-step-image-gen]] — 클래스 레이블 → 텍스트 조건 1-step 이미지 생성 (upvote 70). 실시간 이미지 생성 가능성 열어줌.

### HF 모델 트렌딩 (2026-04-22)
- [[Qwen3.6-35B-A3B]] — 458,000 다운로드 (HF 트렌딩 1위). MoE 효율 모델 최다 다운로드 1위.
- [[Kimi-K2.6]] — 8,240 다운로드 (HF 트렌딩 2위, 736 likes). 신규 공개 1.1조 파라미터 MoE.
- [[HY-World-2.0]] — Tencent Image-to-3D 세계 생성, 오늘 출시 직후 트렌딩 4위 (531 likes).
- [[MiniMax-M2.7]] — 358,000 다운로드 (트렌딩 9위, 1,030 likes). 229B MoE 꾸준한 성장.
- [[gemma-4-e4b-obliterated]] — 79,000 다운로드 (트렌딩 5위, 433 likes). Gemma 4B abliteration 경량 로컬 수요.

> [!insight] 핵심 인사이트
> 2026-04-22 핵심: **"에이전트 교육(ai-agents-for-beginners) + 스킬 큐레이션(awesome-agent-skills) + 코드 검색(claude-context)"** 에이전트 생태계 3계층 동시 등장. 동시에 Qwen3.6 MoE가 HF 다운로드 1위 — 효율적 MoE 아키텍처가 오픈소스 표준으로 자리잡는 중. FinceptTerminal GitHub Trending 1위(+2,548)는 금융 AI가 개인 투자자 레이어까지 침투하는 신호.

