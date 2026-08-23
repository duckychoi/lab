# Actionable — 당장 써먹을 수 있는 것들

ingest할 때마다 LLM이 갱신한다. 완료된 항목은 삭제하지 말고 상태를 "완료"로 바꾼다.

---

## [2026-08-23] openai/codex 병행 실행 대조 — 하네스 안전 규칙을 문서가 아닌 코드로 확인
- **도메인**: ai-news (코딩 에이전트)
- **출처**: [[openai-codex]] · [[anthropic-claude-code]] · [[Claude-Code-워크플로우]] · [[codex-plugin-cc]]
- **할 것**: [[openai-codex]]는 **Apache-2.0·Rust로 에이전트 본체 소스가 공개된 사실상 유일한 대형 상용급 구현체**다(⭐114,383·API 실검증). 반면 [[anthropic-claude-code]]는 라이선스 미명시·본체 비공개의 배포/이슈 채널이다. ① `npm install -g @openai/codex` 또는 `brew install --cask codex`로 설치하고 **동일 태스크 1건을 Claude Code와 병행 실행**해 셸 조작 방식·승인(permission) 흐름·컨텍스트 처리 차이를 직접 대조. ② 소스가 열려 있으므로 **샌드박싱·권한 분리 구현부를 읽어** 내 하네스 안전 규칙에 이식 가능한 결정론적 규칙만 발췌. ③ 대체가 아니라 조합이 현실적임은 [[codex-plugin-cc]]와 [[ECC]]의 "Claude Code 우선 + Codex 동기화" 채택이 이미 시사 — 리뷰어/서브에이전트 배치 가능성까지 확인.
- **우선순위**: 낮음 (급하지 않으나, "에이전트가 셸·파일을 어떻게 격리하는가"를 **문서가 아닌 코드로 확인할 수 있는 유일 경로**라 레퍼런스 가치가 높음)
- **상태**: 대기
- ⚠️ **개방성≠성능**. 같은 배치 [[SWE-bench-Science]]의 실측 최고 성능은 **Claude Code + Opus-5(max)**이고 codex는 상위에 없다(그조차 pass@1 50% 미만). "OpenAI 공식"을 품질 근거로 쓰지 말 것. 또한 인증 기본 경로가 **ChatGPT 유료 요금제 로그인**이라 계정이 없으면 API 키 별도 설정이 필요하고, **요금제별 실제 토큰/요청 한도는 레포에 미기재**라 비용 비교는 불가.

## [2026-08-22] 메모리 ON/OFF A/B — 메모리 인지 함정이 내 봇에서 실제 발생하는지 스팟체크
- **도메인**: ai-news / local-llm (agent-memory)
- **출처**: [[MemTrapBench]] · [[에이전트-메모리-레이어]]
- **할 것**: [[MemTrapBench]]가 **2개 모델 패밀리 × 5개 메모리 프레임워크에서 평가된 모든 메모리 전략이 no-memory보다 못했고 최강도 10%+ 하락**을 보고했다(초록 원문 실검증). 내 에이전트/봇의 메모리 주입 경로에 대해 ① 동일 질의 세트를 **메모리 ON vs OFF로 각 1회** 돌려 정답률·응답 일관성 비교, ② 틀린 케이스에서 **Reasoning Fixation**(과거 결론에 고착)과 **Belief Distortion**(과거 전제를 현재에 잘못 적용)이 실제로 나타나는지 육안 분류, ③ 발생 시 AdaptiveMem을 모사해 메모리 주입 프롬프트에 **"검색된 메모리가 현재 질문과 충돌하거나 무관하면 무시하라"** 가드 문장을 넣고 재측정. 이건 새 도구 설치가 아니라 **기존 경로에 대한 감사**라 비용이 거의 들지 않는다.
- **우선순위**: **중간** (이번 배치 최우선 — 볼트의 메모리 축 전제를 흔드는 첫 정량 반례이고, 완화책이 프롬프트 한 줄이라 검증 대비 비용이 매우 낮음)
- **상태**: 대기
- ⚠️ MemTrapBench는 **함정을 겨냥해 설계된 적대적 벤치**이고 표본이 5개 프레임워크·2개 모델 패밀리다. "메모리는 해롭다"로 일반화 금지 — 검증 대상 명제는 **"내 경로에서 추론 오염이 실제로 관측되는가"** 뿐.

## [2026-08-22] 스킬 개선을 싱글턴이 아니라 멀티턴 로그에서 뽑기
- **도메인**: ai-news (agent-skills)
- **출처**: [[SkillEvo]] · [[에이전트-스킬]] · [[Claude-Code-워크플로우]]
- **할 것**: [[SkillEvo]]의 핵심 발견은 **싱글턴 QA 피드백으로 스킬을 고치면 1라운드 뒤 진화 기울기가 소멸**하고, 여러 턴에 걸쳐야만 드러나는 결함은 영영 안 보인다는 것(자기반성 대비 +23.0점·싱글턴QA 대비 +15.4점). 내 스킬 중 하나(예: wiki 스킬)를 골라 **1회 실행 결과가 아니라 3턴 이상 이어 쓴 실제 세션 로그**에서 결함을 뽑아 수정하는 루프를 1회 수동 실행하고, 싱글턴 개선과 무엇이 달랐는지 기록. 프레임워크 코드 없이 **설계 원칙만으로 즉시 적용 가능**.
- **우선순위**: 낮음
- **상태**: 대기
- ⚠️ +23.0/+15.4점은 **자체 정의 벤치 위 상대 비교**이며 절대 품질 보장이 아니다. 멀티턴 시뮬레이터가 LLM이면 평가자 편향이 기울기에 실릴 수 있는데 초록은 이를 다루지 않는다.

## [2026-08-22] 프리뷰↔최종 2-티어 렌더 구조를 영상 파이프라인 설계 옵션으로 기록
- **도메인**: video-saas (교차 ai-news)
- **출처**: [[ForgeWM]] · [[월드모델]] · [[reat-render]]
- **할 것**: [[ForgeWM]]의 **dual-path 배포**(지연 임계 구간은 1-step으로, 나중에 같은 초안을 re-noise 후 정제해 4-step 참조 품질에 필적시키되 **노이즈 재생성 대비 실제 궤적에 약 3배 근접** 유지)는 영상 제작의 **프리뷰↔최종 렌더 2-티어**와 동형이다. 핵심 이점은 속도가 아니라 **초안의 구도·모션 일관성을 버리지 않고 품질만 올린다**는 점 — 지금처럼 최종 렌더에서 처음부터 다시 생성하면 프리뷰와 결과가 달라지는 문제를 구조적으로 없앤다. 설계 노트로만 기록하고, 파이프라인 개편 시점에 꺼내 쓴다.
- **우선순위**: 낮음
- **상태**: 대기
- ⚠️ ForgeWM은 **게임 상호작용 월드모델**이고 절대 지연시간·해상도·비교군 목록이 초록 미기재다. 아이디어만 이식하고 수치는 인용 금지.

## [2026-08-18] llmfit — 하드웨어 적합성 사전 필터로 로컬 모델 후보 축소
- **도메인**: ai-news / local-llm
- **출처**: [[llmfit]] · [[Qwen3.8-27B-GGUF]] · [[LLMRouter]]
- **할 것**: [[llmfit]](Rust CLI·수백 모델 중 내 하드웨어에서 실제 구동 가능한 것만 한 명령으로 필터)을 내 워크스테이션에서 실행해 로컬 후보를 먼저 좁힌 뒤, 상위 후보를 [[Qwen3.8-27B-GGUF]] Q4/Q5 스팟체크(기존 액션)의 대상 선정에 연결 — "적합성 사전 필터(llmfit·상류) → 품질 스팟체크 → [[LLMRouter]] 저지연 게이트 편입(하류)"의 로컬 스택 앞단을 구체화. ⚠️⭐32,541은 raw 자동수집·실WebFetch 미수행 → "구동 가능" 판정 로직(VRAM 추정 정확도·프로바이더 커버리지)은 실행해 실측 전 신뢰 금지, "뜨는 것"과 "쓸 만한 것"은 별개.
- **우선순위**: 낮음
- **상태**: 대기

## [2026-08-17] 방어·보안 각도 — 영상 자동화 출처표시 + 코드 보안 점검 개념 참조
- **도메인**: ai-news (교차 video-saas)
- **출처**: [[Crisis-Video-Attack-Defense]] · [[strix]] · [[video-saas]]
- **할 것**: 두 축을 개념 참조로 편입 — ① [[Crisis-Video-Attack-Defense]](AI 생성 영상 공격 방어·탐지)의 원문 공개 시 출처검증·워터마킹·확산 신호만 발췌해 내 영상 자동화([[reat-render]]) 결과물의 **출처표시/워터마킹 책임 설계**에 참고, ② [[strix]](자율 침투 테스트 에이전트·⭐5.3만)를 격리 환경에서 데모 취약 앱에 1회 돌려 탐지율·오탐·PoC 품질 체감 후 내 SaaS/봇 코드 보안 점검 보조 편입 여부 판단. ⚠️Crisis 논문은 미래형 arxiv ID(2608.14391)·원문 미검증 → 수치 인용 금지·공개 전 대기. strix 자율 "수정"은 오탐 시 기능 파손 위험 → 사람 리뷰 필수·본인 소유 자산만.
- **우선순위**: 낮음
- **상태**: 대기

## [2026-08-16] Qwen3.8-27B-GGUF — 로컬 GGUF 27B 스팟체크 후 상비 후보 판정
- **도메인**: ai-news / local-llm
- **출처**: [[Qwen3.8-27B-GGUF]] · [[unsloth]] · [[LLMRouter]]
- **할 것**: [[unsloth]]가 재배포한 [[Qwen3.8-27B-GGUF]](DL 1.95M·GGUF 양자화·로컬 추론용)를 llama.cpp류에서 **Q4/Q5 단계별로 스팟체크**해 응답 품질·지연을 실측 후, 오프라인·저지연 로컬 상비 모델 후보로 판정 — [[LLMRouter]] 라우팅 스펙트럼의 "로컬 GGUF 저지연 게이트" 슬롯 후보. ⚠️DL·좋아요는 접근성 지표이지 품질 근거 아님·양자화 단계별 손실 raw 미기재(실WebFetch 미수행) → 실측 전 성능 단정 금지, 원본 Qwen3.8-27B 라이선스 확인.
- **우선순위**: 낮음
- **상태**: 대기

## [2026-08-14] LLMRouter — 다중 모델 하네스 라우팅 게이트 설계 개념 참고
- **도메인**: ai-news / local-llm
- **출처**: [[LLMRouter]] · [[DeepSeek-V4-Flash-0731]] · [[Kimi-K3]] · [[needle]]
- **할 것**: [[LLMRouter]](LLM 라우터 개발·평가·배포 통합 인프라·HF 데일리 2위·raw 업보트 "2.3k대" 자릿수 이상치 반복 발생으로 절대값 미채택)의 코드/문서 공개 시, 라우팅 기준(비용·품질·지연 시그널)과 평가 방식만 발췌해 내 다중 모델·스킬 하네스의 "요청→모델 선택" 게이트 설계에 개념 참고 — 저지연([[DeepSeek-V4-Flash-0731]])·대형([[Kimi-K3]])·온디바이스([[needle]]) 분배 축. ⚠️미래형 arxiv ID(2608.06867)·원문 미검증·UIUC 소속 raw 기재 → 공개 전 대기, 수치·순위 인용 금지.
- **우선순위**: 낮음
- **상태**: 대기

## [2026-08-14] LTX-2 / LTX-2.5 — 오디오 동반 오픈 i2v 비교군 편입
- **도메인**: ai-news / video-saas
- **출처**: [[LTX-2]] · [[LTX-2.5]] · [[MiniMax-H3]] · [[ComfyUI]]
- **할 것**: [[LTX-2]](Lightricks 공식 추론/LoRA 패키지)+[[LTX-2.5]](i2v 가중치)를 기존 [[ComfyUI]] 오픈 i2v 스팟체크에 **오디오 동반 생성 비교군**으로 편입 — [[MiniMax-H3]](무성 i2v) vs LTX 계열(오디오 동반)의 품질·통제력·설치 난이도를 재현 가능한 프롬프트↔결과 쌍으로 대조. ⚠️해상도·오디오 동기·라이선스 raw·미검증(실WebFetch 미수행) → 실행 전 요구사항·라이선스 확인, 수치 인용 금지.
- **우선순위**: 낮음
- **상태**: 대기

## [2026-08-13] unsloth — 오픈 소형 모델 로컬 QLoRA 파인튜닝 스팟체크
- **도메인**: ai-news / local-llm
- **출처**: [[unsloth]] · [[DeepSeek-V4-Flash]] · [[needle]]
- **할 것**: [[unsloth]](⭐70,732·오픈 LLM·디퓨전 로컬 파인튜닝/추론 메모리 최적화)로 오픈 소형 모델(Qwen/Gemma 계열) + 도메인 데이터 소량 **QLoRA 파인튜닝을 단일 GPU에서 스팟체크** — 실제 VRAM 점유·학습 속도·수렴을 측정해 내 봇(ChinameBot류) 자체 파인튜닝 스택 채택 여부 판정. ⚠️절감 배수·속도 주장은 raw 자동수집·미검증 → 실측 결과만, 배수 인용 금지.
- **우선순위**: 중간
- **상태**: 대기

## [2026-08-13] StateFlow — 편집 가능한 3D 월드 상태 previz 파이프라인 개념 참조
- **도메인**: ai-news (교차 slam-3dgs / video-saas)
- **출처**: [[StateFlow]] · [[Beyond-Pixels-4D]] · [[reat-render]]
- **할 것**: [[StateFlow]](프리비주얼라이제이션용 3D 월드 상태 구축·진화·접근)의 코드/원문 공개 시, "픽셀 직생성" 대신 **편집 가능한 지속 3D 상태를 유지 후 렌더**하는 파이프라인 구조(상태 표현·질의·비파괴 수정)만 발췌해 내 영상 자동화 씬 일관성 설계에 개념 참고. ⚠️미래형 arxiv ID(2608.12314)·원문 미검증 → 공개 전 대기, 수치·순위 인용 금지.
- **우선순위**: 낮음
- **상태**: 대기

## [2026-08-12] 오픈 i2v 스팟체크에 Turbo-Lora 가속 A·B 비교 추가
- **도메인**: ai-news / video-saas
- **출처**: [[MiniMax-H3-Turbo-Lora]] · [[MiniMax-H3]] · [[ComfyUI]]
- **할 것**: 기존 [[ComfyUI]] 오픈 i2v 스팟체크(2026-08-11 항목)에 **가속 LoRA A·B 비교**를 얹는다 — 동일 이미지→영상 프롬프트 1건을 ①베이스 [[MiniMax-H3]] ②베이스+[[MiniMax-H3-Turbo-Lora]]로 각각 생성해 *생성 속도 vs 모션 일관성·디테일* 트레이드오프를 실측. 오픈 i2v를 로컬에서 실용 속도로 돌릴 부품 후보 판정. ⚠️DL 669 초기 단계·가속효과/품질손실/호환성 미검증 — 가속 배수·품질 주장 인용 금지, 실측 결과만.
- **우선순위**: 낮음
- **상태**: 대기

## [2026-08-12] 스케줄형 LLM 자동 리포트 파이프라인 구조 참조 (daily_stock_analysis)
- **도메인**: ai-news (교차 금융-AI)
- **출처**: [[daily_stock_analysis]] · [[TradingAgents]] · [[Firecrawl]]
- **할 것**: [[daily_stock_analysis]](⭐62,436·LLM 다중 시장 주식 분석)의 코드 공개 확인 시, **"스케줄 → 외부 데이터 수집 → LLM 정형 리포트 산출"** 구조(데이터 소스 배선·프롬프트·리포트 포맷)만 발췌해 내 스케줄형 자동 리포트 설계에 개념 참고. ⚠️투자 판단 신뢰성·백테스트·데이터 소스 미검증(인기 스타는 알파 근거 아님) — 투자 신호·수익 주장 인용 금지, 파이프라인 패턴만 참조.
- **우선순위**: 낮음
- **상태**: 대기

## [2026-08-11] ComfyUI를 오픈 i2v 스팟체크 실행 환경으로 편입
- **도메인**: ai-news / video-saas
- **출처**: [[ComfyUI]] · [[MiniMax-H3]] · [[Higgsfield]] · [[Seedance]]
- **할 것**: [[ComfyUI]](노드 기반 디퓨전 실행 엔진)를 로컬 백엔드로 세워, [[MiniMax-H3]] 등 오픈 i2v 모델 스팟체크 시 *재현 가능한 프롬프트↔결과 쌍 1건*(노드 그래프로 파이프라인 버전관리)을 확보. 폐쇄형 [[Higgsfield]]·[[Seedance]] 대비 오픈·로컬·완전제어 축의 품질/제어 실효를 판정해 [[video-saas]] 오픈 축 레퍼런스에 편입. ⚠️스타·다운로드는 접근성 지표이지 품질 근거 아님 — 실제 출력 품질만 판단.
- **우선순위**: 중간
- **상태**: 대기

## [2026-08-11] 그래프 RAG 인프라(semantica·code-graph-rag) 개념을 위키·코드 컨텍스트 검색에 이식 검토
- **도메인**: ai-news
- **출처**: [[semantica]] · [[code-graph-rag]] · [[LLM-Wiki]]
- **할 것**: [[code-graph-rag]](모노레포 구조 그래프 기반 코드 RAG)·[[semantica]](그래프 네이티브·감사가능성 인프라)의 **"임베딩 유사도가 아닌 구조 그래프로 컨텍스트·근거를 좁히고 추적"** 발상을, 내 [[LLM-Wiki]] 볼트(wikilink 그래프)의 검색·코드 컨텍스트 합성·근거 추적 설계에 개념만 이식 검토. ⚠️두 repo 모두 아키텍처·실사용성 미검증(급상승은 관심도 지표) — 코드/그래프 스키마 공개 범위 확인 후 발상만 참고, 수치·성능 주장 인용 금지.
- **우선순위**: 낮음
- **상태**: 대기

## [2026-08-03] Meshy-T2 네이티브 메시 생성을 3D 백본 스팟체크에 편입
- **도메인**: ai-news / slam-3dgs
- **출처**: [[Meshy-T2]] · [[TRELLIS.2]] · [[Meshy]] · [[Tripo]]
- **할 것**: [[Meshy-T2]](플로우 매칭·네이티브 메시 생성)의 **가중치·데모 공개 여부 확인 후**, 08-02 [[TRELLIS.2]] 오픈 3D 백본 스팟체크에 묶어 텍스트/이미지→3D 샘플 1건으로 *생성 속도(few-step)·메시 토폴로지 편집성·후처리 손실*을 [[Meshy]]·[[Tripo]] 상용 대비 비교. "표현 계층(TRELLIS.2 구조화 latent) vs 생성 방식(Meshy-T2 flow matching)" 두 축의 실효 차이 판정.
- **우선순위**: 낮음
- **상태**: 대기

## [2026-08-03] RLSVR·AISPA "자기검증·프롬프트 감사" 개념을 위키·스킬에 이식 검토
- **도메인**: ai-news
- **출처**: [[RLSVR]] · [[AISPA]] · [[LLM-Wiki]] · [[AskChem]]
- **할 것**: [[RLSVR]]의 **"과제를 검증 가능한 형태로 변환해 자기검증 보상을 만든다"**를 내 [[LLM-Wiki]] 인제스트의 *주장 단위 사실확인*(검증 가능한 클레임으로 구조화)에, [[AISPA]]의 **"시스템 프롬프트를 사용자 편에서 감사"**를 내 다수 스킬 프롬프트 자기점검 체크리스트에 각각 개념만 이식 검토. ⚠️두 논문 모두 미래형 ID·원문 미검증이므로 **수치·방법 세부 인용 금지, 발상만 참고**.
- **우선순위**: 낮음
- **상태**: 대기

## [2026-08-02] TRELLIS.2 오픈 3D 생성 백본 품질 스팟체크
- **도메인**: ai-news / slam-3dgs
- **출처**: [[TRELLIS.2]] · [[Meshy]] · [[Tripo]]
- **할 것**: [[Microsoft]] [[TRELLIS.2]](구조화 latent 3D 생성)의 **가중치·라이선스 공개 여부 확인 후**, 텍스트/이미지→3D 샘플 1건으로 생성 품질·메시 변환 손실·편집성을 [[Meshy]]·[[Tripo]] 상용 대비 스팟체크. 오픈·자체호스팅 3D 백본으로서 실효성 판단.
- **우선순위**: 낮음
- **상태**: 대기

## [2026-08-02] 스킬 라우팅·에이전트 SDK 임베드 설계 패턴만 개념 추출
- **도메인**: ai-news
- **출처**: [[reverse-skill]] · [[copilot-sdk]] · [[OpenSpace]]
- **할 것**: [[reverse-skill]]의 **"태스크→스킬 자동 라우팅"**과 [[copilot-sdk]]의 **"코딩 에이전트 SDK 임베드 인터페이스"** 설계 패턴만 개념 참고 → 내 다수 스킬(wiki·reat·pptx) 자동 선택 로직 개선 힌트로 활용. ⚠️reverse-skill은 개인 프로젝트·보안 리버싱 도구이므로 **코드 실행·의존 없이 아이디어만**, 정당 목적·감사 전제.
- **우선순위**: 낮음
- **상태**: 대기

## [2026-07-29] RARG relevance-aware ripgrep를 위키 쿼리·인제스트 탐색에 이식
- **도메인**: ai-news
- **출처**: [[RARG]] · [[InMind]] · [[LLM-Wiki]]
- **할 것**: 지금 위키 탐색은 순진한 `grep -rli`인데, [[RARG]]의 **"index 요약 기반 문서 랭킹으로 어떤 페이지를 먼저 열지 결정 + 매치 스니펫 리랭킹으로 정보성 발췌 우선"**을 얹은 쿼리 프로토타입을 만든다 → 도구호출 횟수·토큰 대비 정확도 개선 재현 여부 실측. 동시에 [[InMind]]가 규명한 **"암묵적 연상 사각지대(간접 적용 14.4%)"**를 이 위키 쿼리에 재현 테스트(직접 매칭 vs 암묵 연결).
- **우선순위**: 높음
- **상태**: 대기

## [2026-07-29] OpenSpace "실행 결과 기반 스킬 품질 로깅"을 wiki log.md에 편입
- **도메인**: ai-news
- **출처**: [[OpenSpace]] · [[ECC]] · [[book-to-skill]]
- **할 것**: [[OpenSpace]](⭐7.2k MIT)의 **스킬 품질 측정(선택/적용/완료/폴백 추적) + 자가진화 3연산(FIX/DERIVED/CAPTURED)**을 내 다수 스킬(wiki·reat·pptx) 운용에 부분 이식 → log.md에 스킬별 "선택/적용/완료/폴백" 필드를 남겨 증거화하고, 반복 실패 스킬을 FIX/DERIVED 대상으로 식별하는 루프 실험.
- **우선순위**: 중간
- **상태**: 대기

## [2026-07-29] Mage-VL "모션/잔차 희소 프레임 선별"을 down-analysis 토큰 전략에 스팟 적용
- **도메인**: ai-news
- **출처**: [[Mage-VL]] · [[down-analysis]] · [[claude-video]]
- **할 것**: [[Mage-VL]]의 **코덱 네이티브 희소 패치(모션·잔차 신호로 정보성 프레임만 선별, 토큰 ~75%↓)** 아이디어를 내 [[down-analysis]] 영상 분석 프레임 선별에 휴리스틱으로 실험 → [[claude-video]] 4모드(특히 token-burner) 대비 토큰↔충실도 절감이 재현되는지 스팟체크.
- **우선순위**: 낮음
- **상태**: 대기

## [2026-07-27] impeccable 60개 결정론 디자인 룰을 tools-frontend/reat 산출물 감사 게이트로 이식
- **도메인**: ai-news
- **출처**: [[impeccable]] · [[design.md]] · [[tools-frontend]] · [[reat-layout]]
- **할 것**: pbakaus/impeccable(⭐51,000, Apache 2.0)의 키 불필요 CLI를 설치 → 내 프런트 산출물([[tools-frontend]] 오버레이·[[reat-layout]]/[[reat-slides]] 슬라이드)에 `/impeccable audit` 실행. **60개 결정론 디텍터 룰 중 이식 가능 항목**(대비·간격·타이포 위계)을 추출해, AI 생성 UI/슬라이드에 "결정론 디자인 게이트"를 붙이는 실험. 순수 프롬프트로 못 잡던 안티패턴을 규칙으로 잡아 산출물 하한선 상승 여부 확인.
- **우선순위**: 중간
- **상태**: 대기

## [2026-07-27] book-to-skill로 기술 PDF 1권→에이전트 스킬 변환해 위키 인제스트 반자동화 시험
- **도메인**: ai-news
- **출처**: [[book-to-skill]] · [[LLM-Wiki]] · [[awesome-claude-skills]] · [[agent-skills]]
- **할 것**: virgiliojr94/book-to-skill(⭐10,260, Python·MIT)로 기술 PDF 1권을 **챕터별 온디맨드 스킬 + 용어집 + 치트시트**로 변환 → 챕터 로딩 품질·용어집 정확도 평가. 07-25 액션([[awesome-claude-skills]] 문서 스킬 이식)의 구체 실행. 성립하면 **긴 문서 인제스트를 이 위키 스킬의 보조 파이프로 이식**해 반자동화(수동 소스 분할 대체). RAG 대비 온디맨드 스킬 로딩의 실효 확인.
- **우선순위**: 중간
- **상태**: 대기

## [2026-07-20] AstrBot Telegram 어댑터로 ChinameBot류 다중채널 봇 골격 스팟체크
- **도메인**: ai-news
- **출처**: [[AstrBot]] · [[AI-에이전트-프레임워크]] · [[lobehub]]
- **할 것**: AstrBotDevs/AstrBot(⭐36,836)을 로컬 구동 → Telegram 어댑터 1개로 최소 봇을 띄우고 Hermes/GLM 백엔드 + [[MCP]] 도구 1개를 연결. "다중 IM 어댑터 + 플러그인 마켓 + 페르소나"를 밑바닥부터 안 짜고 재사용 가능한지, 특히 **텔레그램/Slack 어댑터 성숙도와 한국어 대응**을 실측(중화권 IM 편중 여부 확인). 골격 재사용 가치가 있으면 ChinameBot류 다중채널 서빙의 베이스로 채택 판단.
- **우선순위**: 중간
- **상태**: 대기

## [2026-07-20] ktransformers MoE CPU 오프로딩 vs airllm 레이어 스와핑 로컬 대형 구동 실측
- **도메인**: local-llm / ai-news
- **출처**: [[ktransformers]] · [[airllm]] · [[LMCache]]
- **할 것**: kvcache-ai/ktransformers(⭐18,544)를 설치해 프런티어 MoE(GLM-5/Kimi-K2.5·DeepSeek급) 1개를 가용 하드웨어에서 구동, **kt-kernel 추론 속도(it/s)·필요 CPU RAM·AMX 유무 영향**을 [[airllm]](레이어 스와핑)과 나란히 실측. "가중치 그대로 두고 배치를 바꾸는" 두 오프로딩 축의 실용 경계(속도 vs 하드웨어 요구)를 수치로 확정 — 로컬 대형 구동이 필요해지는 시점의 1순위 선택 근거로 삼음.
- **우선순위**: 낮음
- **상태**: 대기

## [2026-07-19] wigolo MCP를 위키 자동수집 파이프에 붙여 무과금 로컬 웹 리서치 A/B
- **도메인**: ai-news
- **출처**: [[wigolo]] · [[firecrawl]] · [[crawl4ai]]
- **할 것**: KnockOutEZ/wigolo(⭐1,400)를 MCP 서버로 로컬 등록 후, 이 위키 자동수집(트렌드 조사) 리서치 태스크 1건을 wigolo vs [[firecrawl]]로 나란히 돌려 **검색 결과 품질·크롤 안정성·차단율**을 비교. "API키·과금 없이 로컬로 검색까지"가 실제로 성립하는지(어떤 검색 백엔드를 쓰는지, 봇 차단은 어떻게 우회하는지) README·실측으로 확인. 품질이 상용 API의 실용 하한을 넘으면 무인 크론 리서치의 웹 접근을 로컬·무과금으로 이관해 운영 원가 절감.
- **우선순위**: 중간
- **상태**: 대기

## [2026-07-19] airllm 레이어 스와핑으로 프론티어 오픈모델 1회 추론 속도 실측
- **도메인**: local-llm / ai-news
- **출처**: [[airllm]] · [[Bonsai-27B]] · [[LMCache]]
- **할 것**: lyogavin/airllm(⭐23,500)을 소형 GPU(4~8GB)에 설치해 중대형 오픈모델(예: [[Qwen3.6-27B]]) 1회 추론으로 **토큰/초·첫 토큰 지연**을 실측. "671B on 4GB"는 *가능*이지 *실용*이 아님을 수치로 확인하고, 양자화([[Bonsai-27B]] 삼진 1.71bit)·KV재사용([[LMCache]])과 대비해 "일회성 대형모델 품질 확인용 탈출구"로만 편입할지 판정. 속도가 실사용 불가 수준이면 상시 도구에서 배제, 헤드라인을 액면가로 인용하지 말 것.
- **우선순위**: 낮음
- **상태**: 대기

## [2026-07-18] Bonsai-27B 삼진 1.71bit 양자화를 8GB급 하드웨어에서 IQ2/NVFP4와 실측 비교
- **도메인**: local-llm / ai-news
- **출처**: [[Bonsai-27B]] · [[Qwen3.6-27B]] · [[Qwen3.6-27B-NVFP4]]
- **할 것**: `prism-ml/Ternary-Bonsai-27B-gguf`(~7.2GB)를 llama.cpp/Ollama로 받아 8GB VRAM/CPU 환경에서 thinking 태스크 실행 → "FP16의 95%(평균 80.49)" 자체 리포트를 소규모 실측으로 검증하고, IQ2_XXS·[[Qwen3.6-27B-NVFP4]](4bit)와 정확도·속도·VRAM 3자 비교. 삼진 1.71bit가 실사용에서도 정확도를 지키면 중형 로컬 기본 후보로 편입, 무너지면 NVFP4로 대체. 벤치는 배포자 자체값이니 액면가로 믿지 말 것.
- **우선순위**: 중간
- **상태**: 대기

## [2026-07-18] code-review-graph MCP를 Claude Code에 붙여 대형 레포 컨텍스트 절감 스팟체크
- **도메인**: ai-news / local-llm
- **출처**: [[code-review-graph]] · [[graphify]] · [[turbovec]]
- **할 것**: tirth8205/code-review-graph를 MCP 서버로 로컬 등록 후 중형 레포에서 "그래프 질의로 필요한 부분만 읽기 vs 파일 통독"의 토큰 사용량·응답 정확도를 A/B로 비교. 인덱스 구축·유지 비용이 절감분을 상쇄하지 않는지 확인하고, [[graphify]] 같은 기존 코드 그래프와 차별점(리뷰 특화·지속성·MCP 표준) 원문 검증. "돌아간다"와 "실제로 컨텍스트를 아낀다"를 구분해 판정.
- **우선순위**: 낮음
- **상태**: 대기

## [2026-07-17] VideoChat3 완전공개 비디오 MLLM을 down-analysis 장면이해 백엔드로 대조 스팟체크
- **도메인**: video-saas / ai-news
- **출처**: [[VideoChat3]] · [[down-analysis]] · [[Video-Oasis]]
- **할 것**: VideoChat3 가중치·코드 공개 시(원문 2607.14935 확인 선행) 샘플 영상 2~3개로 장면 캡션·요약 품질을 현재 [[down-analysis]]의 Gemini 멀티모달 결과와 나란히 대조. "완전공개" 실제 범위(데이터셋 포함 여부)와 로컬 구동 가능 여부 확인 후, Gemini 의존을 낮출 오픈 백엔드 후보로 편입할지 판정. [[Video-Oasis]]가 밝힌 "영상 안 보고 푸는" 함정 고려해 리더보드 수치는 액면가로 믿지 말 것.
- **우선순위**: 중간
- **상태**: 대기

## [2026-07-17] KeyFrame-Compass 평가 축을 reat 영상 "구도 일관성" 자기점검에 응용
- **도메인**: video-saas / ai-news
- **출처**: [[KeyFrame-Compass]] · [[DomainShuttle]] · [[krea2-identity-edit]]
- **할 것**: 원문(2607.14202) 공개 시 키프레임 충실도 평가 지표를 정리 → reat-render 결과 중 "지정한 앵커 구도/캐릭터를 얼마나 지켰나"를 사후 점검하는 경량 체크리스트로 축약 적용. 지표가 인간 지각과 어긋날 위험([[PerceptionRubrics]])을 전제로, 자동 채점이 아닌 "탈락 후보 걸러내기" 용도로만 사용. 상용 툴(Higgsfield·Kling)의 일관성 주장 비교 잣대로도 활용.
- **우선순위**: 낮음
- **상태**: 대기

## [2026-07-16] hallmark 안티-슬롭 디자인 스킬을 reat 슬라이드/tools-frontend에 이식 스팟체크
- **도메인**: ai-news / video-saas
- **출처**: [[hallmark]] · [[mattpocock-skills]]
- **할 것**: Nutlope/hallmark(⭐9,734)의 디자인 규칙 세트를 클론해 reat-slides 또는 [[tools-frontend]] 오버레이 1개 화면에 적용 → AI 생성 UI의 "슬롭"(보라 그라디언트·과한 그림자·뻔한 레이아웃) 억제 효과를 적용 전/후 A/B로 확인. 규칙이 또 다른 획일성(hallmark 룩)을 낳지 않는지도 함께 점검 후 스킬 편입 판단.
- **우선순위**: 중간
- **상태**: 대기

## [2026-07-16] openinterpreter Rust판 + 로컬 소형모델로 무인 자동화 실행 벤치
- **도메인**: local-llm / ai-news
- **출처**: [[openinterpreter]] · [[destructive_command_guard]] · [[needle]]
- **할 것**: openinterpreter Rust 재작성판을 설치하고 로컬 GGUF 소형모델(예: [[MiniCPM5-1B]]·Ornith 계열)을 백엔드로 붙여 단순 파일/셸 태스크 성공률을 벤치. [[destructive_command_guard]] pre-exec 훅과 결합해 "무인 로컬 실행 + 파괴 명령 차단" 조합의 안전성·실용성을 확인. "돌아간다"와 "쓸 만하다"를 구분해 판정.
- **우선순위**: 낮음
- **상태**: 대기

## [2026-07-15] Read-It-Back MLLM 되읽기 채점을 reat 이미지 배치 QA에 실험
- **도메인**: video-saas / ai-news
- **출처**: [[Read-It-Back]] · [[verifiers]]
- **할 것**: reat-slides/이미지 에셋 생성 배치에 "생성 이미지 → MLLM 캡션/QA 되읽기 → 원 프롬프트 일치도 스코어"를 붙여 **best-of-N 자동 선별**을 소규모 실험. 전용 리워드 모델·사람 검수 없이 프롬프트 충실도만 걸러지는지, 사람 검수 대비 일치율 확인. 미학·디테일은 못 잡는다는 한계 전제로 "탈락 필터"로만 사용.
- **우선순위**: 중간
- **상태**: 대기

## [2026-07-15] needle 26M 온디바이스 함수호출을 "로컬 라우터 + 클라우드 추론" 2단 분업으로 벤치
- **도메인**: local-llm / ai-news
- **출처**: [[needle]] · [[MiniCPM5-1B]]
- **할 것**: cactus-compute/needle(26M)을 받아 도구 스키마 5~10개로 **오호출률·지연**을 벤치. 통과하면 봇/에이전트 앞단에 로컬 도구 라우터로 두고 상위 대형 모델 호출 횟수를 줄이는 분업 실현성 판단. 26M 정확도가 임계치 미달이면 폐기.
- **우선순위**: 낮음
- **상태**: 대기

## [2026-07-14] krea2-identity-edit로 "동일 캐릭터 다중 씬" 정체성 유지 편집 실험

- **도메인**: video-saas
- **출처**: [[krea2-identity-edit]]
- **할 것**: HF `conradlocke/krea2-identity-edit`를 로컬/파이프라인에 얹어 원본 얼굴 → 배경·의상·포즈 변경 시 **정체성 보존 강도**를 스팟체크. 안정적이면 [[Higgsfield]]류 캐릭터+씬+샷 워크플로우의 "인물 일관성" 부품으로 reat-*/숏폼 파이프에 통합 검토. 라이선스·해상도 카드 확인 선행.
- **우선순위**: 중간
- **상태**: 대기

---

## [2026-07-14] Qwen-Fixed-Chat-Templates를 로컬 Qwen 추론 정비 상비 도구로 등록

- **도메인**: local-llm
- **출처**: [[Qwen-Fixed-Chat-Templates]]
- **할 것**: 로컬에서 [[Qwythos-9B]]·[[ThinkingCap-Qwen3.6-27B-GGUF]] 등 Qwen 파생 모델 출력이 이상할 때 `froggeric/Qwen-Fixed-Chat-Templates`의 교정 template로 교체해 포맷 정합성 복구. "출력 품질 조용한 열화 = 템플릿 깨짐" 체크리스트에 상비.
- **우선순위**: 낮음
- **상태**: 대기

---

## [2026-07-12] claude-cookbooks prompt caching·자동평가 레시피를 위키 파이프에 이식

- **도메인**: ai-news
- **출처**: [[claude-cookbooks]]
- **할 것**: [[claude-cookbooks]]의 **prompt caching** 노트북으로 위키 자동수집의 반복 시스템 프롬프트 토큰비를 절감하고, **automated evals** 노트북으로 인제스트 품질(인사이트 vs 요약)을 코드로 점수화. 서브에이전트(Haiku+Opus) 패턴은 소스 초벌 분류에 적용 검토.
- **우선순위**: 중간
- **상태**: 대기

---

## [2026-07-12] OpenViking 티어드 로딩·파일시스템 검색을 위키 쿼리에 차용 검토

- **도메인**: ai-news (+ local-llm)
- **출처**: [[OpenViking]]
- **할 것**: [[OpenViking]]의 **L0/L1/L2 티어드 로딩 + `viking://` 디렉터리 재귀검색**을 로컬 데모(OpenViking Studio)로 띄워, 이 위키(index→domain→page 계층)의 쿼리 응답 토큰 절감 구조로 이식 가능한지 검증. AGPLv3 코어라 상용 임베딩은 라이선스 주의.
- **우선순위**: 낮음
- **상태**: 대기

---

## [2026-07-11] MTP GGUF + LMCache 로컬 추론 이중 최적화 벤치

- **도메인**: local-llm
- **출처**: [[Qwen3.6-35B-A3B-MTP-GGUF]] · [[LMCache]]
- **할 것**: [[Qwen3.6-35B-A3B-MTP-GGUF]](Q4_K_M)를 로컬 서빙에 올리고 [[LMCache]] prefix 캐시를 결합해, **MTP 자기투기(throughput) + prefix 캐시(TTFT)** 이중 최적화의 실측 이득을 비-MTP·비캐시 대비 측정. 시스템 프롬프트가 반복되는 스케줄/에이전트 워크로드 기준.
- **우선순위**: 중간
- **상태**: 대기

---

## [2026-07-11] Qwopus3.6 Coder를 로컬 코딩 에이전트 백엔드로 검증

- **도메인**: local-llm
- **출처**: [[Qwopus3.6-35B-A3B-Coder-MTP-GGUF]] · [[UniClawBench]]
- **할 것**: [[Qwopus3.6-35B-A3B-Coder-MTP-GGUF]](Q5_K_M)를 로컬 코딩 에이전트 백엔드로 올려 **thinking-off** 모드의 코드 패칭·멀티턴 도구 루프 정확도·속도를 범용 [[Qwen3.6-35B-A3B-MTP-GGUF]]과 대조. [[UniClawBench]]가 지적한 롱호라이즌 약점을 "짧고 정확한 실행"으로 얼마나 메우는지 확인.
- **우선순위**: 중간
- **상태**: 대기

---

## [2026-07-11] DesktopCommanderMCP 격리 설치 후 위키 자동수집 보조 실험

- **도메인**: ai-news
- **출처**: [[DesktopCommanderMCP]] · [[stitch-skills]]
- **할 것**: [[DesktopCommanderMCP]]를 **Docker 격리 + command blocklist**로 설치해 로컬 파일 정리·diff 편집·crawl 결과 파싱을 보조하는 안전 실험. 병행으로 [[stitch-skills]] Build(Remotion) 플러그인 스킬 정의를 뜯어 [[reat-render]] 레이아웃 패턴 추출. ⚠️무인 스케줄엔 격리·blocklist 필수.
- **우선순위**: 낮음
- **상태**: 대기

---

## [2026-07-07] firecrawl + last30days-skill로 raw.md 자동수집 파이프 PoC

- **도메인**: ai-news
- **출처**: [[firecrawl]] · [[last30days-skill]]
- **할 것**: [[firecrawl]](셀프호스트/API)로 GitHub Trending·HF 페이지를 크롤·정제 → [[last30days-skill]] 계열 소셜 조사([[last-30days]] 스킬)를 얹어 raw.md 인제스트 큐를 반자동 적재하는 파이프라인 PoC. 현재 수동 자동수집을 대체·강화. 수집 노이즈(자가제출 수치 등) 필터 규칙 포함.
- **우선순위**: 중간
- **상태**: 대기

---

## [2026-07-07] meetily 로컬 회의록 스택 vs down-analysis 정확도 비교

- **도메인**: ai-news
- **출처**: [[meetily]]
- **할 것**: macOS/Linux에서 [[meetily]] 빌드 설치 → 내 인터뷰/회의 녹음 1건으로 로컬 Whisper/Parakeet 전사 + Ollama 요약 품질을 [[down-analysis]] 파이프와 대조. 화자 분리(PRO 미구현) 한계 확인. 합격 시 로컬 우선 회의 기록 스택으로 편입.
- **우선순위**: 낮음
- **상태**: 대기

---

## [2026-07-04] Claude Code + Codex 이중 리뷰 조합 실험

- **도메인**: ai-news
- **출처**: [[codex-plugin-cc]]
- **할 것**: 격리 브랜치에서 실제 PR 1건에 대해 [[anthropic-claude-code]]로 작성 → codex-plugin-cc로 OpenAI Codex 교차 리뷰를 붙여, 두 모델 관점차로 잡히는 버그 수 vs 추가 토큰·API 비용을 대조. 순이득 확인 시 위험도 높은 변경에만 선택적 이중화 도입.
- **우선순위**: 중간
- **상태**: 대기

---

## [2026-07-04] CubeSandbox로 에이전트 생성 코드 격리 실행층 검토

- **도메인**: ai-news
- **출처**: [[CubeSandbox]]
- **할 것**: 데모 에이전트가 만든 스크립트를 CubeSandbox에서 병렬 실행 → 격리 강도(커널/네임스페이스 수준 vs 프로세스 수준)·기동 지연·동시 처리량을 컨테이너 방식과 대조. 격리 강도 코드 확인 전까지 비신뢰 코드 실행 금지. 합격 시 위키 자동수집/에이전트 코드 실행층 후보 편입.
- **우선순위**: 낮음
- **상태**: 대기

---

## [2026-07-03] AgenticSTS "bounded-contract" 메모리 조립 패턴을 내 파일 메모리에 이식

- **도메인**: ai-news
- **출처**: [[AgenticSTS]]
- **할 것**: 현재 raw transcript/기록을 **통째로 append**하는 방식 대신, [[AgenticSTS]]의 *타입별 검색으로 필요한 조각만 뽑아 fresh-prompt를 재조립하는* bounded-contract 구조를 내 파일 기반 memory([[에이전트-메모리-레이어]]) 설계에 적용 검토. 메모리 타입(사용자/피드백/프로젝트/레퍼런스)별 검색·주입 규칙을 정의해 컨텍스트 오염·비대화를 줄인다. [[MemSyco-Bench]]의 "메모리가 판단을 오염"과 짝지어 부작용도 점검.
- **우선순위**: 높음
- **상태**: 대기

---

## [2026-07-03] superpowers + agency-agents 조합 설치·검증

- **도메인**: ai-news
- **출처**: [[superpowers]] / [[agency-agents]]
- **할 것**: `/plugin install superpowers@claude-plugins-official`로 [[superpowers]](스펙→계획→서브에이전트→리뷰 방법론) 설치 후 실제 태스크 1건에 서브에이전트 주도 루프 실행. [[agency-agents]]의 Frontend/QA/Research 역할 프리셋을 얹어 산출물 품질·역할 정의 포맷을 비교하고, 유용한 역할 정의를 내 자동화 스키마로 흡수. 둘 다 [[Claude-Code-워크플로우]] 직결.
- **우선순위**: 중간
- **상태**: 대기

---

## [2026-07-03] Program-as-Weights 퍼지 함수 1건 컴파일 실측

- **도메인**: ai-news
- **출처**: [[Program-as-Weights]]
- **할 것**: `pip install programasweights`로 자연어 "퍼지 함수"(예: 텍스트 분류/추출 규칙) 1건을 로컬 LoRA 어댑터로 컴파일 → 동일 작업을 API 호출로 했을 때 대비 **품질·메모리·지연**을 실측. "0.6B가 32B급·1/50 메모리" 주장이 내 반복 분류 작업(위키 도메인 태깅 등)에 실효 있는지 검증. local-llm 축 교차.
- **우선순위**: 낮음
- **상태**: 대기

---

## [2026-07-02] olmocr vs MinerU — 위키 인제스트 PDF 정제 게이트 대조

- **도메인**: ai-news
- **출처**: [[olmocr]] / [[MinerU]]
- **할 것**: 실제 PDF 소스 1건(수식·표·다단 포함)을 [[olmocr]](AI2, 7B VLM, Apache 2.0)와 [[MinerU]](2.5 VLM 엔진)로 각각 마크다운 변환 → 레이아웃 보존·표 정확도·순서(선형화) 품질·처리 속도 비교. 우세한 쪽을 [[wiki]] 인제스트의 **PDF/스캔 전처리 표준 게이트**로 채택(현재 `defuddle`가 담당하는 웹 HTML의 PDF 대칭축). 로컬 GPU/Docker 배포 비용도 함께 체크.
- **우선순위**: 높음
- **상태**: 대기

---

## [2026-07-02] agents-cli 로컬 eval 흐름 시험 (GCP 미종속 부분만)

- **도메인**: ai-news
- **출처**: [[agents-cli]]
- **할 것**: [[Google]] agents-cli의 `create → eval` 로컬 흐름만 먼저 실행(배포/GKE 등 GCP 종속부 제외). **멀티턴 eval 합성·메트릭·데이터셋** 기능이 내 에이전트([[Claude-Code-워크플로우]]·[[ChinameBot]]) 품질 측정에 재사용 가능한지 확인. 유용하면 GCP 없이도 eval 하네스로 채택, 배포 파트는 GCP 사용 시에만 재검토. Apache 2.0.
- **우선순위**: 중간
- **상태**: 대기


## [2026-07-01] OmniRoute로 코딩 루프 API 비용 절감 PoC

- **도메인**: ai-news
- **출처**: [[OmniRoute]]
- **할 것**: Docker로 OmniRoute 1회 기동 → [[Claude-Code-워크플로우]]/코딩 에이전트를 OpenAI 호환 엔드포인트로 연결 → (a) 무료 프로바이더 자동 폴백 동작, (b) RTK/Caveman 토큰 압축 on/off 시 실제 절감률과 품질 저하를 실측. 무료 티어(예: Z.AI GLM-Flash) 품질을 유료 대비 체감. 합격 시 저위험(비민감) 작업에 상시 비용 절감 레이어로 편입. 손실 압축이므로 코드·정확 수치 프롬프트는 압축 강도별 검증 필수.
- **우선순위**: 높음
- **상태**: 대기

---

## [2026-07-01] Ornith-1.0-9B 로컬 에이전틱 코딩 모델 벤치 (단일 GPU)

- **도메인**: local-llm
- **출처**: [[Ornith-1.0-9B]]
- **할 것**: 9B(reasoning+tool-call, vLLM 등 파서 활성화) 로컬 로드 → 실제 리포 수정 태스크 1건으로 [[gemma-4-12B-coder-GGUF]] 대비 정확도·속도·토큰 소모 비교(9B 자체 벤치 SWE-bench Verified 69.4 주장 체감). `<think>` 블록으로 토큰 생성량↑ 실측. 합격 시 로컬 코딩 보조 후보. 벤치는 모델카드 자체 측정이므로 실사용 검증 필수.
- **우선순위**: 중간
- **상태**: 대기

---

## [2026-06-30] video-use 영상 편집 에이전트 구조 분석 (영상 자동화 파이프라인)

- **도메인**: ai-news / video-saas
- **출처**: [[video-use]]
- **할 것**: 레포 clone → 자연어 지시를 어떤 편집 프리미티브(컷/자막/전환/속도)로 분해하는지 매핑 구조 분석 → [[reat-render]]/[[reat-slides]] 파이프라인에 "자연어 편집 지시" 레이어를 얹을 수 있는지 검토. [[OpenMontage]]·[[After-Effects-MCP]]와 편집 추상화 비교.
- **우선순위**: 중간
- **상태**: 대기

---

## [2026-06-30] FluidVoice 한국어 로컬 STT 정확도 테스트

- **도메인**: local-llm
- **출처**: [[FluidVoice]]
- **할 것**: Apple Silicon Mac에 설치 → 한국어 받아쓰기 정확도·지연시간 측정, STT 백엔드 모델 확인 → 합격 시 음성 코딩/메모 워크플로의 클라우드 STT 대체 후보로 채택. [[voicebox]](로컬 TTS)와 함께 온디바이스 음성 입출력 스택 구성 검토.
- **우선순위**: 낮음
- **상태**: 대기

---

## [2026-06-28] OpenSpec 스펙 주도 개발 시범 적용 (코딩 에이전트 일관성)

- **도메인**: ai-news
- **출처**: [[OpenSpec]]
- **할 것**: `npm i -g @fission-ai/openspec@latest`(Node 20.19+) → 실제 기능 1건을 `/opsx:propose`로 명세화 → proposal/spec/design/checklist 산출물 품질과 구현 일관성을 즉흥 프롬프팅과 대조. 우위 시 [[Claude-Code-워크플로우]] 표준에 편입.
- **우선순위**: 높음
- **상태**: 대기

---

## [2026-06-28] ppt-master 한국어 PPTX 편집 품질 테스트

- **도메인**: ai-news
- **출처**: [[ppt-master]]
- **할 것**: Python 3.10+ 환경에서 `pip install -r requirements.txt` → 한국어 보고서 1건 입력 → 도형/텍스트가 실제로 네이티브 편집되는지, 한글 폰트·표 깨짐 여부 확인. 합격 시 문서→발표자료 변환 파이프라인 후보로 채택.
- **우선순위**: 중간
- **상태**: 대기

---

## [2026-06-25] design.md 디자인 명세 도입 (프론트엔드 에이전트 일관성)

- **도메인**: ai-news
- **출처**: [[design-md]]
- **할 것**: Google Labs `design.md` 명세 정독 → [[reat-layout]]/[[tools-frontend]] 프로젝트 루트에 디자인 토큰 명세 파일 작성 → 에이전트 레이아웃 생성이 이를 참조하도록 연결 (코드의 `CLAUDE.md`처럼)
- **우선순위**: 높음
- **상태**: 대기

---

## [2026-06-25] gemma-4-12B-agentic vs coder function-calling 대조 벤치

- **도메인**: ai-news
- **출처**: [[gemma-4-12B-agentic-GGUF]]
- **할 것**: agentic(165k DL)·coder(496k DL) 두 GGUF를 동일 환경(Ollama)에서 한국어 function-calling 성공률·환각률 대조 → 우위 모델을 [[hermes-agent]]/[[ChinameBot]] 로컬 백엔드로 채택 검토
- **우선순위**: 중간
- **상태**: 대기

---

## [2026-04-10] VoxCPM 로컬 TTS 테스트 (reat-voice 대체)

- **도메인**: ai-news
- **출처**: [[VoxCPM]]
- **할 것**: VoxCPM 로컬 설치 → 한국어 음성 품질 테스트 → ElevenLabs 비용 대비 품질 비교
- **우선순위**: 높음
- **상태**: 대기

---

## [2026-04-10] VOID 모델 영상 편집 파이프라인 통합

- **도메인**: ai-news
- **출처**: [[VOID-model]]
- **할 것**: HF Space(VOID-Quadmask-Reasoner)에서 즉시 테스트 → reat-render 후처리 파이프라인에 객체 제거 자동화 추가
- **우선순위**: 높음
- **상태**: 대기

---

## [2026-04-10] Gemma-4-31B 멀티모달 벤치마크

- **도메인**: ai-news
- **출처**: [[Gemma-4-31B]]
- **할 것**: Together AI API로 이미지 이해 테스트 → GPT-4o Vision 대비 비용/성능 비교
- **우선순위**: 중간
- **상태**: 대기

---

## [2026-04-10] hermes-agent 에이전트 프레임워크 검토

- **도메인**: ai-news
- **출처**: [[hermes-agent]]
- **할 것**: GitHub README 숙독 → 기존 Claude Code 워크플로우 대비 추가 가치 평가 → star 결정
- **우선순위**: 중간
- **상태**: 대기

---

## [2026-04-10] RTK CLI 프록시 설치 테스트

- **도메인**: ai-news
- **출처**: [[instagram-저장-2026-02-2026-04]], @codingknowledge
- **할 것**: Claude Code 토큰 90% 절감 주장 RTK CLI 프록시 설치 및 실측. 실제 절감율 측정.
- **우선순위**: 높음
- **상태**: 대기

---

## [2026-04-10] After Effects MCP 조사 및 테스트

- **도메인**: ai-news
- **출처**: [[After-Effects-MCP]], @hyun2xyz
- **할 것**: GitHub "after-effects MCP" 검색 → 구현체 찾기 → 실제 테스트. 자연어 → 키프레임 생성 가능 여부 확인.
- **우선순위**: 높음
- **상태**: 대기

---

## [2026-04-10] .claude/ 트렌드 레이더 + 자동 커밋 훅 구성

- **도메인**: ai-news
- **출처**: [[Claude-Code-워크플로우]], @leadgenman
- **할 것**: .claude/hooks/ 에 트렌드 감지 + 변경 시 자동 커밋 훅 설정. 콘텐츠 기획 자동화 파이프라인 완성.
- **우선순위**: 높음
- **상태**: 대기

---

## [2026-04-10] 오픈소스 Higgsfield 대안 조사

- **도메인**: video-saas
- **출처**: [[Higgsfield]], @appinventiv4ai
- **할 것**: "open-source alternative to Higgsfield" GitHub 검색 → 자체 영상 SaaS 엔진으로 활용 가능성 검토.
- **우선순위**: 중간
- **상태**: 대기

---

## [2026-04-10] Seedance 2.0 직접 테스트

- **도메인**: video-saas
- **출처**: [[Seedance]]
- **할 것**: invideo AI 통해 Seedance 2.0 테스트. "100x better than Sora 2" 검증.
- **우선순위**: 중간
- **상태**: 대기

---

## [2026-04-10] 나노바나나2 + Tripo 3D 워크플로우 실습

- **도메인**: slam-3dgs
- **출처**: [[AI-3D-생성]]
- **할 것**: 사진 1장 → 나노바나나2/Tripo → Blender 워크플로우 직접 실행.
- **우선순위**: 낮음
- **상태**: 대기

---

## [2026-04-10] Mamba4 독립 검증

- **도메인**: ai-news
- **출처**: [[Mamba4]]
- **할 것**: Mamba4 GitHub 레포 / 논문 확인. 소셜미디어 클레임 검증.
- **우선순위**: 낮음
- **상태**: 대기

---

## [2026-04-11] andrej-karpathy-skills CLAUDE.md 현재 설정 통합

- **도메인**: ai-news
- **출처**: [[andrej-karpathy-skills]]
- **할 것**: https://github.com/forrestchang/andrej-karpathy-skills 읽기 → 현재 /home/monday/ CLAUDE.md 또는 프로젝트 CLAUDE.md에 적용 가능한 규칙 추출 → 즉시 반영
- **우선순위**: 높음
- **상태**: 대기

---

## [2026-04-11] MinerU2.5 wiki 인제스트 파이프라인 통합

- **도메인**: ai-news
- **출처**: [[MinerU2.5]]
- **할 것**: HF arXiv 2509.22186 확인 → 코드 레포 찾기 → PDF → 마크다운 변환 파이프라인 구축 테스트. 현재 defuddle 대비 수식·표 인식 품질 비교.
- **우선순위**: 높음
- **상태**: 대기

---

## [2026-04-11] superpowers Shell 스킬 프레임워크 테스트

- **도메인**: ai-news
- **출처**: [[superpowers]]
- **할 것**: https://github.com/obra/superpowers 클론 → 스킬 구조 분석 → Monday 스킬 아키텍처와 비교. Shell 기반 에이전트 패턴 벤치마킹.
- **우선순위**: 중간
- **상태**: 대기

---

## [2026-04-11] Gemma 4 26B-A4B GGUF 로컬 실행 테스트

- **도메인**: ai-news
- **출처**: [[Gemma-4-26B]]
- **할 것**: Ollama 또는 LM Studio로 unsloth/gemma-4-26B-A4B-it-GGUF 실행 → 이미지 이해 + 텍스트 생성 성능 측정. 활성 4B이므로 일반 GPU에서 가능.
- **우선순위**: 중간
- **상태**: 대기

---

## [2026-04-11] TimesFM 제로샷 시계열 예측 실험

- **도메인**: ai-news
- **출처**: [[TimesFM]]
- **할 것**: HF에서 google/timesfm 모델 확인 → 간단한 비즈니스 지표(트래픽, 매출) 예측 파이프라인 실험. Fine-tuning 없이 즉시 사용 가능 여부 확인.
- **우선순위**: 낮음
- **상태**: 대기

---

## [2026-04-11] markitdown wiki 인제스트 파이프라인 통합

- **도메인**: ai-news
- **출처**: [[markitdown]]
- **할 것**: pip install markitdown → wiki ingest 파이프라인에서 PDF/DOCX/HTML 일괄 변환 테스트. 현재 defuddle과 비교. 수식·표 많은 문서는 MinerU2.5와 병용 결정.
- **우선순위**: 높음
- **상태**: 대기

---

## [2026-04-11] Gemma-4-E4B Any-to-Any 멀티모달 로컬 테스트

- **도메인**: ai-news
- **출처**: [[Gemma-4-E4B]]
- **할 것**: Ollama로 gemma4-e4b 실행 → 이미지+텍스트 Any-to-Any 입력 테스트. Gemma-4-26B 대비 8B 실체 모델의 추론 품질 비교.
- **우선순위**: 중간
- **상태**: 대기


---

## [2026-04-14] andrej-karpathy-skills CLAUDE.md 즉시 통합 (스타 28K 폭발)

- **도메인**: ai-news
- **출처**: [[andrej-karpathy-skills]]
- **할 것**: 레포 내용 확인 → 현재 CLAUDE.md에 적용 가능한 규칙 추출 → 즉시 반영. 스타 12K→28K (+132%) — Claude Code 커뮤니티가 검증한 설정.
- **우선순위**: 높음
- **상태**: 대기

---

## [2026-04-14] hermes-agent 4일 연속 1위 — 에이전트 메모리 아키텍처 검토

- **도메인**: ai-news
- **출처**: [[hermes-agent]]
- **할 것**: hermes-agent 공식 문서 읽기 → 메모리 레이어 아키텍처 분석 → ChinameBot 적용 가능 여부 판단. 스타 80K 돌파, 4일간 26K 증가.
- **우선순위**: 높음
- **상태**: 대기

---

## [2026-04-14] MiniMax-M2.7 벤치마크 확인

- **도메인**: ai-news
- **출처**: [[MiniMax-M2.7]]
- **할 것**: HF 페이지에서 벤치마크·라이선스 확인 → GLM-5.1 대비 로컬 실행 적합성 비교.
- **우선순위**: 낮음
- **상태**: 대기

---

## [2026-04-21] TrendRadar MCP 서버 Claude Code 통합 테스트

- **도메인**: ai-news
- **출처**: [[TrendRadar]]
- **할 것**: TrendRadar MCP 서버 설치 → Claude Code에서 실시간 트렌드 데이터 호출 테스트 → wiki 자동 수집 파이프라인 연결 가능성 평가
- **우선순위**: 높음
- **상태**: 대기

---

## [2026-04-21] RAG-Anything vault 파이프라인 통합

- **도메인**: ai-news
- **출처**: [[RAG-Anything]]
- **할 것**: pip install RAG-Anything → vault wiki/ 디렉터리 인덱싱 → Query 작업을 의미 검색 기반으로 고도화
- **우선순위**: 높음
- **상태**: 대기

---

## [2026-04-21] VoxCPM2 한국어 TTS 품질 테스트

- **도메인**: ai-news
- **출처**: [[VoxCPM2]]
- **할 것**: HuggingFace에서 VoxCPM2 다운로드 → 한국어 음성 합성 품질 테스트 → OmniVoice·VoxCPM 기존 버전과 비교 → reat-voice 파이프라인 교체 여부 판단
- **우선순위**: 높음
- **상태**: 대기

---

## [2026-06-23] firecrawl로 raw.md 자동수집 파이프라인 구축

- **도메인**: ai-news
- **출처**: [[firecrawl]]
- **할 것**: firecrawl(self-host 또는 API)로 GitHub Trending·HF 트렌딩 페이지 크롤 → 정제 → raw.md 인제스트 큐 자동 적재 PoC
- **우선순위**: 높음
- **상태**: 대기

---

## [2026-06-23] 위키 쿼리 단계에 리랭커 도입

- **도메인**: ai-news
- **출처**: [[KaLM-Reranker-V1]]
- **할 것**: 위키 query 단계에서 grep/임베딩 검색 결과를 KaLM-Reranker로 재정렬 → 답변 정밀도 비교 측정
- **우선순위**: 중간
- **상태**: 대기

---

## [2026-06-24] voicebox 로컬 음성 스튜디오로 reat-voice 대체 검토

- **도메인**: ai-news
- **출처**: [[voicebox]]
- **할 것**: voicebox 로컬 설치 → 한국어 내레이션 품질을 ElevenLabs와 블라인드 비교 → 합격 시 [[reat-voice]] 백엔드를 로컬 무제한 음성으로 교체 PoC ([[VoxCPM2]] 테스트와 함께 진행)
- **우선순위**: 높음
- **상태**: 대기

---

## [2026-06-24] Unlimited-OCR로 위키 인제스트 이미지 입력 게이트 확장

- **도메인**: ai-news
- **출처**: [[Unlimited-OCR]]
- **할 것**: Baidu Unlimited-OCR로 한국어 표/스캔 문서·스크린샷 정확도 테스트 → 합격 시 raw.md 인제스트에 이미지/PDF→텍스트 단계 편입 ([[mark-clean]]는 웹 HTML 담당, OCR은 이미지 담당)
- **우선순위**: 중간
- **상태**: 대기

---

## [2026-06-26] page-agent로 웹 폼·다단계 클릭 자동화 PoC

- **도메인**: ai-news
- **출처**: [[page-agent]]
- **할 것**: Alibaba page-agent로 단순 웹폼 자동 입력 1건 재현 → [[firecrawl]] 수집과 결합해 "수집→동작" 파이프 가능성 점검. CSP/iframe/shadow DOM 제약과 LLM 백엔드 확인.
- **우선순위**: 중간
- **상태**: 대기

---

## [2026-06-26] 이미지 생성 앞단에 프롬프트 보강 에이전트 루프 도입

- **도메인**: ai-news
- **출처**: [[Qwen-Image-Agent]]
- **할 것**: 약한 프롬프트 → LLM 자동 보강 → 생성의 2단계 미니 파이프를 [[reat-layout]] 자산 생성에 시험. 비전문 입력의 결과 품질 상향 효과 측정.
- **우선순위**: 중간
- **상태**: 대기

---

## [2026-06-27] MinerU를 위키 인제스트 PDF/문서 전처리로 시험

- **도메인**: ai-news
- **출처**: [[MinerU]]
- **할 것**: MinerU CLI/MCP Server로 논문 PDF 1편을 markdown 변환 → [[markitdown]]·[[liteparse]] 결과와 수식·표·레이아웃 품질 비교. 합격 시 raw.md 인제스트의 PDF→markdown 표준 전처리로 채택([[Unlimited-OCR]]는 이미지 OCR 담당, MinerU는 구조화 문서 담당으로 역할 분담).
- **우선순위**: 높음
- **상태**: 대기

---

## [2026-06-29] strix로 내 코드베이스 보안 자동 점검 PoC

- **도메인**: ai-news
- **출처**: [[strix]]
- **할 것**: 격리 환경에서 데모 취약 앱(OWASP juice-shop류)에 strix 1회 실행 → 탐지 결과의 증거·재현 단계 신뢰성, 오탐률 체감. 합격 시 내 SaaS/봇 코드베이스 정기 보안 점검 보조로 편입(자동 수정은 PR 제안까지만, 사람 리뷰 필수). 본인 소유 자산에만 사용.
- **우선순위**: 중간
- **상태**: 대기

---

## [2026-06-29] 위키 자동수집·열거 작업에 완전성 검증 루프 도입

- **도메인**: ai-news
- **출처**: [[Ko-WideSearch]]
- **할 것**: Ko-WideSearch가 지적한 "집합 식별은 정확하나 행 복구는 일관 실패" 실패 모드 방어 — raw.md 자동수집/열거형 쿼리 처리 시 "찾은 집합 크기 vs 실제 복구한 행 수" 자가 점검 + 누락 시 재수집 단계를 인제스트 절차에 추가 검토. 내 위키 파이프라인 신뢰성 직결.
- **우선순위**: 높음
- **상태**: 대기

---

## [2026-07-05] mattpocock/skills에서 재사용 스킬 발췌 + agentskills 표준 정렬 검토

- **도메인**: ai-news
- **출처**: [[mattpocock-skills]] · [[agentskills]]
- **할 것**: ⭐156,933 mattpocock/skills를 클론해 내 도메인(영상/로컬LLM/위키)과 무관한 TS 편향을 걷어내고 재사용 가능한 스킬 2~3개만 발췌 이식. 동시에 [[agentskills]] 규격 문서를 훑어 내 `.claude/skills` 프론트매터·구조를 호환 포맷으로 정렬할지 판단(벤더 간 이식성 확보). 스킬 남발 방지 위해 [[SkillCoach]]식 "실제로 잘 쓰이는가" 기준으로 선별.
- **우선순위**: 중간
- **상태**: 대기

---

## [2026-07-05] 웹 자동화 "수집→동작→디버깅" 파이프 시험 (page-agent + chrome-devtools-mcp)

- **도메인**: ai-news
- **출처**: [[page-agent]] · [[chrome-devtools-mcp]]
- **할 것**: [[firecrawl]](수집)·[[mark-clean]](정제) 뒤에 [[page-agent]](인페이지 DOM 동작)와 [[chrome-devtools-mcp]](콘솔·네트워크 디버깅)를 붙여 단순 웹폼 자동화 1건을 end-to-end로 재현. 스크린샷 좌표 추론 없이 DOM 직접 조작이 동적 SPA·CSP 환경에서 얼마나 견고한지 체감 → 합격 시 내 웹 자동화 스택의 동작 레이어로 편입.
- **우선순위**: 낮음
- **상태**: 대기

---

## [2026-07-06] claude-video와 내 down-analysis 파이프라인 대조 검증

- **도메인**: video-saas
- **출처**: [[claude-video]] · [[down-analysis]]
- **할 것**: [[claude-video]](`/watch`)의 "**자막 우선 → 필요 구간만 다운로드 → scene-aware 프레임 추출 → Whisper 폴백**" 순서를 내 [[down-video]]+[[down-analysis]] 파이프라인과 1건 대조. 특히 ①자막 우선으로 다운로드·전사 비용을 아끼는 부분, ②scene-aware 프레임 추출 로직이 내 Gemini 멀티모달 방식 대비 토큰·정확도에서 어떤지 실측. 합격 요소는 down-analysis에 흡수.
- **우선순위**: 중간
- **상태**: 대기

---

## [2026-07-06] speech-to-speech로 완전 로컬 음성 파이프라인 실험 (reat-voice 로컬 대안)

- **도메인**: local-llm
- **출처**: [[speech-to-speech]] · [[reat-voice]]
- **할 것**: HF [[speech-to-speech]](VAD→STT→LLM→TTS, OpenAI Realtime WS)를 `pip install` 후 **Parakeet TDT + Qwen3-TTS + llama.cpp 로컬 LLM**([[Gemma-4-31B]] GGUF)으로 무과금 음성 파이프 1건 구성. 내 [[reat-voice]](ElevenLabs 클라우드·유료) 대비 지연·품질을 체감해 나레이션·자막 생성을 로컬로 내릴지 판단. Reachy Mini 실배포 검증된 스택이라 신뢰도 높음.
- **우선순위**: 낮음
- **상태**: 대기

---

## [2026-07-08] pocket-tts vs reat-voice 로컬 음성 비교 (무과금 TTS 대안)

- **도메인**: local-llm
- **출처**: [[pocket-tts]] · [[reat-voice]]
- **할 것**: [[kyutai-labs]] [[pocket-tts]](CPU 2코어·100M·첫청크 200ms·6언어, MIT)를 `pip` 설치 후 내 나레이션 대본 1건을 생성해 [[reat-voice]](ElevenLabs 클라우드·유료)와 **지연·품질·비용 3축 비교**. GPU 없는 서버·엣지에서도 도는지 체감 → 합격 시 reat-voice의 로컬 폴백으로 편입. [[speech-to-speech]] 로컬 파이프의 TTS 단으로도 후보.
- **우선순위**: 중간
- **상태**: 대기

---

## [2026-07-08] OfficeCLI MCP로 pptx-generate 네이티브 산출 대조

- **도메인**: ai-news
- **출처**: [[OfficeCLI]] · [[pptx-generate]]
- **할 것**: [[OfficeCLI]](Apache 2.0·C#·MCP 서버·350+ Excel함수·Office설치 불요 렌더링)를 MCP 서버로 등록 후, 현재 [[pptx-generate]]가 PDF/이미지 재현에 의존하는 슬라이드 1건을 OfficeCLI로 **편집 가능한 네이티브 pptx**로 생성해 편집성·정확도·워크플로 단순성 비교. 합격 요소는 산출물 생성 백엔드로 흡수.
- **우선순위**: 낮음
- **상태**: 대기

---

## [2026-07-09] zvec + TencentDB-Agent-Memory로 로컬 RAG/메모리 PoC

- **도메인**: local-llm
- **출처**: [[zvec]] · [[TencentDB-Agent-Memory]] · [[에이전트-메모리-레이어]]
- **할 것**: [[zvec]](인프로세스 벡터 DB, Apache 2.0) Python SDK로 위키 소스 임베딩을 서버 없이 인덱싱하고, [[TencentDB-Agent-Memory]](완전 로컬·MIT)의 "도구 로그→Mermaid 압축 + 대화→페르소나 구조화" 패턴을 참고해 **파일 기반 memory에 로컬 시맨틱 검색 + 구조화 장기기억**을 얹는 PoC 1건 구성. dense vs 하이브리드 검색 품질·지연 실측, 외부 API 0 원칙 유지 확인.
- **우선순위**: 중간
- **상태**: 대기

---

## [2026-07-09] herdr vs orca 병렬 에이전트 관제 비교

- **도메인**: ai-news
- **출처**: [[herdr]] · [[orca]]
- **할 것**: [[herdr]](터미널 멀티플렉서·Rust·AGPL)와 [[orca]](GUI ADE·TS·MIT)로 **동일 태스크(에이전트 2개 병렬 git worktree)**를 돌려 관제 UX·리소스 점유·결과 비교 방식·모바일 관제(orca) 실효를 평가. best-of-N 워크플로에 어느 쪽이 내 스케줄 태스크 운용에 맞는지 판단. MIT인 orca 우선 검토(라이선스 자유도).
- **우선순위**: 낮음
- **상태**: 대기

---

## [2026-07-10] graphify로 스킬 저장소 지식 그래프화

- **도메인**: ai-news
- **출처**: [[graphify]] · [[LLM-Wiki]] · [[codebase-memory-mcp]]
- **할 것**: [[graphify]](`uv tool install graphifyy`, MIT)를 Claude Code 스킬로 등록 후 내 스킬 디렉터리(`~/.claude/skills/`, reat-*·pixl-*·obsi-* 등)에 `/graphify .` 실행 → `graph.html`로 스킬 간 의존·중복·**god node**(가장 많이 연결된 핵심)를 시각화. 이 위키의 wikilink 그래프(overview.canvas)와 대조해 "코드 그래프 vs 지식 그래프" 접근을 비교. tree-sitter 로컬 파싱이라 외부 유출 0.
- **우선순위**: 중간
- **상태**: 대기

---

## [2026-07-10] SkillOpt로 down-analysis 스킬 텍스트공간 최적화

- **도메인**: ai-news
- **출처**: [[SkillOpt]] · [[down-analysis]] · [[SkillCoach]]
- **할 것**: [[SkillOpt]](Microsoft, GitHub ⭐12,019·MIT)를 **Claude Code 백엔드**로 붙여 내 스킬 1개(down-analysis 또는 reat-script 프롬프트)를 궤적 기반 + 검증 게이트로 최적화 → 산출 `best_skill.md`(300–2,000토큰)를 원본과 품질·토큰·일관성 3축 비교. "가중치 없이 텍스트로 스킬을 학습"이 실제 내 스킬 품질을 올리는지 실측(자가 벤치 +19~24점 주장 검증). 합격 시 스킬 유지보수 루틴에 SkillOpt-Sleep 야간 최적화 편입 검토.
- **우선순위**: 중간
- **상태**: 대기

## [2026-07-12] C-JEPA 레포·서베이 아카이브 확인
- **도메인**: ai-news
- **출처**: [[C-JEPA]] · [[JEPA-월드모델-서베이-2026]]
- **할 것**: github.com/galilai-group/cjepa star·클론, V-JEPA 2(github.com/facebookresearch/vjepa2)·NVIDIA Cosmos(github.com/nvidia-cosmos) 레포 확인
- **우선순위**: 낮음
- **상태**: 대기

## [2026-07-12] Latent CoT-JEPA 최소 실험 스케치
- **도메인**: local-llm
- **출처**: [[Flow-JEPA-연구아이디어]]
- **할 것**: "잠재공간 추론(Coconut+JEPA)" 최소 스켈레톤 — 선행연구(data2vec·REPA) 대조 후 실현성 판단
- **우선순위**: 낮음
- **상태**: 대기

## [2026-07-13] destructive_command_guard를 무인 스케줄 셸에 seatbelt 도입
- **도메인**: ai-news
- **출처**: [[destructive_command_guard]] · [[UniClawBench]]
- **할 것**: Dicklesworthstone/destructive_command_guard(Rust, ⭐3,447)를 이 위키를 갱신하는 무인 크론·에이전트 셸 실행 파이프에 pre-exec 훅으로 얹어 `rm -rf`·force push 등 비가역 명령 게이트를 실측. 오탐(false block)률·차단 커버리지·우회 가능성 확인 후 방어의 한 겹으로 편입 판단.
- **우선순위**: 중간
- **상태**: 대기

## [2026-07-13] awesome-llm-apps RAG/멀티에이전트 예제 포크 스팟체크
- **도메인**: ai-news
- **출처**: [[awesome-llm-apps]] · [[claude-cookbooks]]
- **할 것**: Shubhamsaboo/awesome-llm-apps(⭐119,041)에서 RAG·멀티에이전트 카테고리 예제 2~3개를 실제 클론·구동해 reat-* 스택 또는 ChinameBot RAG 골격 이식 가치를 스팟체크. 프로덕션 견고성보다 구조 학습·시작점 재사용 관점으로 접근.
- **우선순위**: 낮음
- **상태**: 대기

## [2026-07-21] ai-agent-book Context/Tools 실습으로 ChinameBot 골격 참조
- **도메인**: ai-news
- **출처**: [[ai-agent-book]] · [[에이전트-메모리-레이어]]
- **할 것**: bojieli/ai-agent-book(⭐12.6K, 88실습)에서 "Context/Tools" 관련 실습 2~3개를 클론·구동해 "Agent = LLM + Context + Tools" 분해가 ChinameBot 골격·[[Claude-Code-워크플로우]] 정리와 어떻게 대응되는지 스팟체크. 실습 코드 품질과 실제 재사용 가치 확인.
- **우선순위**: 중간
- **상태**: 대기

## [2026-07-21] SWE-Pruner Pro 백본 은닉상태 프루닝 개념 검토
- **도메인**: ai-news
- **출처**: [[SWE-Pruner-Pro]] · [[code-review-graph]]
- **할 것**: 원문(2607.18213) 공개 시 경량 프루닝 헤드 구조·손실함수(길이인지 임베딩+포컬로스) 확인 → 긴 도구 출력이 잦은 무인 에이전트 파이프에서 "외부 그래프([[code-review-graph]]) vs 모델 내부 신호" 컨텍스트 절감 접근 비교 검토. 직접 구현보다 개념 이식 가능성 판단 우선.
- **우선순위**: 낮음
- **상태**: 대기

## [2026-07-22] i-have-adhd 간결화 규칙을 위키 자동 리포트에 선별 적용
- **도메인**: ai-news
- **출처**: [[i-have-adhd]] · [[agent-skills]]
- **할 것**: ayghri/i-have-adhd(⭐7.4K)의 10개 규칙 중 "다음 행동 맨앞·서론 제거·리스트 5개 상한" 2~3개를 이 위키의 무인 크론 산출물(log 한 줄·domain 요약·query 답변)에 선별 적용해 가독성 A/B. 과도 적용 시 필요한 맥락 손실 여부도 함께 관찰.
- **우선순위**: 중간
- **상태**: 대기

## [2026-07-22] jcode 1만 돌파 — 시맨틱 메모리·swarm 실체 스팟체크
- **도메인**: ai-news
- **출처**: [[jcode]] · [[kimi-cli]] · [[에이전트-메모리-레이어]]
- **할 것**: 05-06 예약된 재검토 임계점(⭐1만) 발동. 1jehuang/jcode(Rust, ⭐10.5K)를 실제 클론·구동해 **시맨틱 메모리(대화 벡터 임베딩 컨텍스트 자동 회수)·에이전트 swarm·자기수정**의 실체와 "245배 빠름·저RAM" 자체 주장을 스팟체크. [[kimi-cli]]·[[OpenManus]] 대비 장기세션 메모리 하네스로서 재사용 가치 판단.
- **우선순위**: 중간
- **상태**: 대기

## [2026-07-25] awesome-claude-skills 카탈로그에서 위키 인제스트 보조 스킬 이식
- **도메인**: ai-news
- **출처**: [[awesome-claude-skills]] · [[agent-skills]] · [[i-have-adhd]]
- **할 것**: ComposioHQ/awesome-claude-skills(⭐70.3K)의 **문서처리·데이터분석 카테고리**에서 스킬 3~5개를 실검토 → 이 위키의 인제스트·리포트 생성에 재사용 가능한 스킬 1건을 클론·이식 실험(예: PDF/이미지 소스 정제, 표 추출). 어썸 리스트 특성상 품질 편차·죽은 링크 감안해 실제 동작 검증 후 편입.
- **우선순위**: 중간
- **상태**: 대기

## [2026-07-25] Solar-Open2-250B 한국어 성능 — 국산 봇 백본 후보 스팟체크
- **도메인**: local-llm
- **출처**: [[Solar-Open2-250B]] · [[Upstage]] · [[GLM-5.2]]
- **할 것**: upstage/Solar-Open2-250B(250B/15B MoE·1M·한일영)의 한국어 생성·툴콜 품질을 데모/API로 스팟체크해 GLM 계열 대비 **국산 봇(ChinameBot) 백본** 후보로서 경쟁력 판단. 자체벤치(SWE 70.4·AIME 95.7) 대비 실제 한국어 체감·서빙 비용(250B 웨이트 인프라)·Solar License 상업조건(접두·표기 의무) 확인 병행.
- **우선순위**: 낮음
- **상태**: 대기

## [2026-07-26] open-code-review — 결정론+LLM 하이브리드 리뷰를 위키 코드 산출물 게이트로 실험
- **도메인**: ai-news
- **출처**: [[open-code-review]] · [[code-review-graph]] · [[aisuite]]
- **할 것**: alibaba/open-code-review(⭐13,269 Go)를 Anthropic/OpenAI 호환 백엔드로 소규모 레포에 연결 → **내장 룰셋(NPE·XSS·SQLi·thread-safety) 히트**와 **LLM 라인코멘트**를 분리 로깅해 "결정론 층이 실제로 오탐을 줄이고 재현성을 주는가"를 실측. 유효하면 위키 스케줄/코드 산출물 자동 사전리뷰 게이트로 편입 검토.
- **우선순위**: 중간
- **상태**: 대기

## [2026-07-28] StateAct — "DOM 상태 우선 + 완료 검증 게이트"를 lightpanda 자동화에 이식
- **도메인**: ai-news
- **출처**: [[StateAct]] · [[impeccable]] · [[open-code-review]]
- **할 것**: 내 lightpanda 브라우저 자동화에서 **스크린샷 대신 DOM/파일 상태 직접 조회를 우선**하고, 작업 완료를 스크린샷이 아닌 **실제 산출물(파일·DOM 노드) 점검으로 검증하는 게이트**를 스팟 적용 → StateAct가 주장한 토큰·오탐 절감(픽셀 의존 1.1%·비용 9배↓)이 내 워크로드에서도 재현되는지 실측.
- **우선순위**: 중간
- **상태**: 대기

## [2026-07-28] Unlimited-OCR MIT 확인 — 한국어 PDF 인제스트 게이트 실편입 테스트
- **도메인**: ai-news
- **출처**: [[Unlimited-OCR]] · [[mark-clean]] · [[MinerU]]
- **할 것**: baidu/Unlimited-OCR(3B·**MIT 라이선스 확인**·269만 DL·32,768 컨텍스트)로 한국어 표/스캔/PDF 샘플을 텍스트추출 vs 포맷보존 각각 테스트 → 순수 추출 합격 시 위키 인제스트의 **이미지·PDF 입력 게이트**로 실편입([[mark-clean]] HTML 담당과 분업), 서식 재현은 [[MinerU]]와 조합. (라이선스 미확인으로 대기하던 항목이 MIT 확인으로 해소됨)
- **우선순위**: 중간
- **상태**: 대기

## [2026-07-28] airi — 프로바이더 추상화·DuckDB WASM 브라우저 메모리 부품 스팟체크
- **도메인**: ai-news
- **출처**: [[airi]] · [[speech-to-speech]] · [[local-llm]]
- **할 것**: moeru-ai/airi(⭐44,374 TypeScript)의 **모델 프로바이더 추상화(Ollama↔OpenAI↔Claude 교체)**와 **DuckDB WASM/pglite 브라우저 내장 메모리** 구현을 코드 레벨로 확인 → 내 캐릭터 봇에 "로컬 우선·클라우드 폴백" 라우팅과 브라우저 내장 메모리 이식 가능성 판단.
- **우선순위**: 낮음
- **상태**: 대기

## [2026-07-30] 로컬 음성 스택 3종 묶음 평가 — reat-voice 대체 후보
- **도메인**: ai-news
- **출처**: [[VibeVoice]] · [[speech-to-speech]] · [[airi]]
- **할 것**: 같은 배치서 동시 급성장한 로컬 음성 3종을 한 묶음으로 실측 — [[VibeVoice]](다화자·장시간 TTS, ⭐51,534)로 나레이션/대화 합성, [[speech-to-speech]](STT→LLM→TTS 로컬 파이프)로 실시간 대화 루프, [[airi]] 프로바이더 추상화로 로컬↔클라우드 폴백 라우팅 → 현재 [[reat-voice]]/ElevenLabs 대비 비용·품질·다화자·지연 비교표 작성.
- **우선순위**: 중간
- **상태**: 대기

## [2026-07-30] rubric-guided RL(DecoEvo+CoRT) — 위키 자기검증 설계 개념 검토
- **도메인**: ai-news
- **출처**: [[DecoEvo]] · [[CoRT]] · [[AREX]]
- **할 것**: [[DecoEvo]]("채점기준을 능력과 분리해 공진화")·[[CoRT]]("토큰 단위 rubric·반사실 신용할당")의 아이디어를 이 위키 자동 리포트의 **자기검증**에 개념 이식 검토 — 산출물 품질 기준(rubric)을 결과 점수와 분리 유지하면 [[LLM-Wiki]] lint의 기준 붕괴/보상해킹을 줄일 수 있는지. 원문은 미래형 ID로 재현 전이므로 **개념 차용만**, 수치 인용 금지.
- **우선순위**: 낮음
- **상태**: 대기

## [2026-07-31] openwork — 워크플로 저장·공유 포맷·라이선스 코드 확인
- **도메인**: ai-news
- **출처**: [[openwork]] · [[ECC]]
- **할 것**: different-ai/openwork(⭐19,035 TypeScript·"Claude Cowork 오픈소스 대안")의 코드/README로 (1) opencode 종속 여부 (2) **워크플로 저장·공유(패키징) 포맷** (3) 라이선스 확인 → 내 스킬(위키·reat·pptx) 공유·재사용 패턴에 참고할 워크플로 자산화 아이디어만 발췌.
- **우선순위**: 낮음
- **상태**: 대기

## [2026-07-31] Metis·AskChem — "메모리 모델·클레임 단위 구조화" LLM-Wiki 개념 이식 검토
- **도메인**: ai-news
- **출처**: [[Metis]] · [[AskChem]] · [[LLM-Wiki]] · [[RARG]]
- **할 것**: [[Metis]]("메모리를 파운데이션 레이어로 승격")·[[AskChem]]("문헌을 클레임 단위로 추출·상충 추적")의 아이디어를 이 위키 쿼리·인제스트 고도화에 개념 이식 검토 — 인제스트를 "소스 요약"에서 "**소스→클레임 분해→상충 플래그**"로, 쿼리를 "wikilink/grep 직접매칭"에서 "관련성 랭킹([[RARG]] 결합)"으로. **원문이 미래형 ID로 재현 전이므로 개념 차용만·수치 인용 금지.**
- **우선순위**: 낮음
- **상태**: 대기

## [2026-08-04] pdf-inspector — 문서 인제스트 OCR 분기 전처리 편입
- **도메인**: ai-news
- **출처**: [[pdf-inspector]] · [[Unlimited-OCR]]
- **할 것**: [[Firecrawl]]/pdf-inspector(⭐9,016 Rust)로 입력 PDF를 "스캔본 vs 텍스트"로 자동 분류 → 스캔본만 [[Unlimited-OCR]]로 라우팅하는 **OCR 분기 전처리**를 내 문서/자료 인제스트에 편입. 기존 [[Unlimited-OCR]] 한국어 PDF 게이트 actionable에 앞단 게이트로 묶어 실험. 라이선스·Python 바인딩(FFI)·하이브리드 PDF 판별 정확도 먼저 확인.
- **우선순위**: 중간
- **상태**: 대기

## [2026-08-04] Progressive-Agent-Skill·LongHorizon-Harness — 스킬 자가개선·롱호라이즌 안정성 개념 이식 검토
- **도메인**: ai-news
- **출처**: [[Progressive-Agent-Skill]] · [[LongHorizon-Harness]] · [[OpenSpace]] · [[LLM-Wiki]]
- **할 것**: [[Progressive-Agent-Skill]]("RL로 스킬 점진 생성·개선")·[[LongHorizon-Harness]]("장기 순차 의사결정 학습·평가")의 아이디어를 내 다수 스킬 하네스(wiki·reat·pptx) 자가개선에 개념 이식 검토 — lint/QA 결과→스킬 프롬프트 개선 루프를 "스킬 레퍼토리 점진 확장"으로, 다단계 워크플로를 "롱호라이즌 신용할당·안정성" 관점으로 자기점검. **원문이 미래형 ID(2608.x)로 재현 전이므로 개념 차용만·수치 인용 금지.**
- **우선순위**: 낮음
- **상태**: 대기

## [2026-08-05] 오픈 3D 백본 스팟체크 확장 — Hunyuan3D-Buffalo 편입
- **도메인**: ai-news (교차 slam-3dgs · video-saas)
- **출처**: [[Hunyuan3D-Buffalo]] · [[TRELLIS.2]] · [[Meshy-T2]] · [[Meshy]] · [[Tripo]]
- **할 것**: [[Tencent]] [[Hunyuan3D-Buffalo]](3D 생성·이해·편집 통합)를 기존 [[TRELLIS.2]]·[[Meshy-T2]] "오픈 3D 백본 품질 스팟체크" actionable에 묶어, 가중치·라이선스 공개 시 텍스트/이미지→3D 생성·편집 품질을 [[Meshy]]/[[Tripo]] 폐쇄형과 비교. **미래형 arxiv ID(2608.02711)·데모만 공개·수치 미검증 → 가중치 공개 전 대기, 수치 인용 금지.**
- **우선순위**: 낮음
- **상태**: 대기

## [2026-08-05] JoyAI-Video-Edit — 실시간 비디오 편집 품질 스팟체크
- **도메인**: ai-news (교차 video-saas)
- **출처**: [[JoyAI-Video-Edit]] · [[Seedance]] · [[Higgsfield]]
- **할 것**: [[JoyAI-Video-Edit]](AR 디퓨전 실시간 오픈엔디드 비디오 편집)의 코드/데모 공개 시 실시간 편집 품질·지연(fps·해상도·편집 자유도)을 [[Seedance]]/[[Higgsfield]] 편집 기능과 비교 — 내 영상 자동화 후반부(post) 편입 가치 판단. **미래형 arxiv ID(2608.03974)·소속 추정·미검증 → 가중치/코드 공개 전 대기.**
- **우선순위**: 낮음
- **상태**: 대기

## [2026-08-06] MiniMax-H3 (ComfyUI판) — 오픈 i2v 품질 스팟체크
- **도메인**: ai-news (교차 video-saas)
- **출처**: [[MiniMax-H3]] · [[Seedance]] · [[Higgsfield]]
- **할 것**: [[MiniMax]]-H3 ComfyUI 배포판(DL 2.3M)으로 짧은 이미지→영상 1건을 생성해 모션 일관성·해상도·길이 한계를 [[Seedance]]/[[Higgsfield]] 폐쇄형과 비교, [[reat-render]]류 자동화와 노드 접목 가능성 탐색. **VRAM 요구·상업 라이선스·원본 스펙 먼저 확인.**
- **우선순위**: 낮음
- **상태**: 대기

## [2026-08-06] cloudflare/computer — computer-use 위임 백엔드 후보 등재
- **도메인**: ai-news
- **출처**: [[cloudflare-computer]] · [[OpenComputer]]
- **할 것**: [[Cloudflare]] [[cloudflare-computer]](에이전트용 원격 가상 컴퓨터 실행 위임)의 오픈소스/셀프호스트 가능 여부·격리 모델(컨테이너/마이크로VM)·지연·요금을 확인해, 컴퓨터 조작·브라우저 자동화 위임 백엔드 후보 목록에 등재. **아키텍처·라이선스 미검증(실WebFetch 미수행) → 문서 확인 후 판단.**
- **우선순위**: 낮음
- **상태**: 대기

## [2026-08-07] WorldClaw — 대규모 3D 오픈월드 생성 백본 스팟체크 편입
- **도메인**: ai-news (교차 slam-3dgs · video-saas)
- **출처**: [[WorldClaw]] · [[Hunyuan3D-Buffalo]] · [[TRELLIS.2]] · [[Meshy-T2]]
- **할 것**: [[WorldClaw]](에이전트형 3D 오픈월드 생성·에셋→월드 스케일)의 코드/데모·가중치 공개 시, 기존 "오픈 3D 백본 품질 스팟체크" 묶음([[Hunyuan3D-Buffalo]]·[[TRELLIS.2]]·[[Meshy-T2]])에 월드 단위 생성 품질(일관성·기하 정합·편집성)로 편입. **미래형 arxiv ID(2608.05248)·원문 초록 미검증 → 가중치 공개 전 대기, 수치 인용 금지.**
- **우선순위**: 낮음
- **상태**: 대기

## [2026-08-07] AgentOPSD·EnvACE — 자기증류·동역학 내재화 안정화 개념 검토
- **도메인**: ai-news
- **출처**: [[AgentOPSD]] · [[EnvACE]] · [[OneDayAgent]] · [[LongHorizon-Harness]]
- **할 것**: [[AgentOPSD]](재귀적 자기증류)·[[EnvACE]](월드 리허설 동역학 내재화)의 원문/코드 공개 시, 롱호라이즌 학습 안정화 기법(재귀 증류 붕괴 방지·상상 롤아웃 오차 누적 억제)만 내 다단계 하네스 자기점검 설계에 개념 참고. **미래형 arxiv ID(2608.05987·2608.06197)·원문 미검증 → 수치·방법 인용 금지, 개념 참고만.**
- **우선순위**: 낮음
- **상태**: 대기

## [2026-08-08] prime-agent — 자기개선 루프 개념 참고 (하네스 자기점검 설계)
- **도메인**: ai-news
- **출처**: [[prime-agent]] · [[AgentOPSD]] · [[superpowers]]
- **할 것**: [[prime-agent]](자기개선형 RLM 코딩 에이전트·⭐7,254 급상승)의 오픈소스 범위·자기개선 루프 구현(추론시 루프 vs 별도 학습)·라이선스를 확인해, 내 다단계 스킬 하네스의 "계획→실행→자기점검·자기개선" 폐루프 설계에 개념만 참고. **아키텍처·라이선스 미검증(실WebFetch 미수행) → 오픈범위 확인 후 판단, 수치 인용 금지.**
- **우선순위**: 낮음
- **상태**: 대기

## [2026-08-08] HarnessOpt-Bench — 하네스 평가 기준 개념 참고
- **도메인**: ai-news
- **출처**: [[HarnessOpt-Bench]] · [[superpowers]] · [[loopx]]
- **할 것**: [[HarnessOpt-Bench]](LLM의 하네스 최적화 능력 벤치)의 코드/원문 공개 시, "좋은 하네스"의 평가 기준(도구 배선·루프·검증 게이트)만 발췌해 내 자기점검 체크리스트 설계에 개념 참고. **미래형 arxiv ID(2608.06301)·원문 미검증 → 가중치/코드 공개 전 대기, 수치·순위 인용 금지.**
- **우선순위**: 낮음
- **상태**: 대기

## [2026-08-10] code-graph-rag — 그래프 기반 코드/지식 컨텍스트 검색 개념 참고
- **도메인**: ai-news (교차 local-llm)
- **출처**: [[code-graph-rag]] · [[code-review-graph]] · [[Learning-from-Failures]]
- **할 것**: [[code-graph-rag]](모노레포용 지식그래프 기반 코드 RAG)의 코드/문서 확인 시, 그래프 구축 파이프라인(파서·언어 커버리지·증분 색인)과 "구조 그래프로 컨텍스트 좁히기" 아이디어만 발췌해 내 위키(wikilink 그래프)·코드 컨텍스트 검색 합성 설계에 개념 참고. **아키텍처·검색 품질·백엔드 요구사항 미검증(실WebFetch 미수행) → 설치 전 요구사항 확인, 수치 인용 금지.**
- **우선순위**: 낮음
- **상태**: 대기

## [2026-08-10] StreamArena — 스트리밍 비디오 이해 에이전트 한계 진단 참조
- **도메인**: ai-news (교차 video-saas)
- **출처**: [[StreamArena]] · [[GST-Bench]] · [[video-saas]]
- **할 것**: [[StreamArena]](에이전틱 스트리밍 비디오 이해 벤치)의 코드/리더보드 공개 시, 실시간·상호작용·롱호라이즌 태스크 정의만 발췌해 향후 영상 자동화 파이프라인의 VLM 한계 진단 프레임으로 참조. **미래형 arxiv ID(2608.05703)·원문 미검증 → 공개 전 대기, 수치·순위 인용 금지.**
- **우선순위**: 낮음
- **상태**: 대기

## [2026-08-19] Qwen3.8-27B FP8↔GGUF 환경별 양자화 포맷 비교
- **도메인**: ai-news (교차 local-llm)
- **출처**: [[Qwen3.8-27B-FP8]] · [[Qwen3.8-27B-GGUF]] · [[omlx]] · [[LLMRouter]]
- **할 것**: FP8 지원 GPU(Hopper/Ada급) 보유 시, 동일 베이스 [[Qwen3.8-27B]]의 공식 FP8판과 [[unsloth]] GGUF(Q4/Q5)를 동일 프롬프트로 품질·지연·메모리 비교 → "GPU 서버=FP8·CPU/워크스테이션=GGUF" 환경별 라우팅 게이트([[LLMRouter]]) 배치 판정. **FP8 양자화 손실·요구 하드웨어·벤치 미검증(실WebFetch 미수행) → 수치 인용 금지, 스팟체크 우선.**
- **우선순위**: 낮음
- **상태**: 대기

## [2026-08-20] SemComp-Bench — 비디오 생성 "의미 완료도" 자동 채점을 video-saas 결과 QA 렌즈로 참조
- **도메인**: ai-news (교차 video-saas)
- **출처**: [[SemComp-Bench]] · [[HarnessEval-W]] · [[AVA-Encoder]] · [[MoneyPrinterTurbo]]
- **할 것**: [[SemComp-Bench]](비디오 생성이 프롬프트가 요구한 의미적 태스크·사건·상태 변화를 실제 구현했는지 채점)의 프레임을 내 [[video-saas]] 파이프라인([[reat-render]]·[[reat-scene]]) 결과 검수에 참조 → "사람 눈 QA"를 "요청 완수도 자동 채점"으로 옮기는 설계 스케치. **벤치 데이터·채점 코드 공개 여부·채점 신뢰도 미검증(미래형 arxiv ID·실WebFetch 미수행) → 프레임 참조만, 수치 인용 금지.**
- **우선순위**: 낮음
- **상태**: 대기

## [2026-08-21] Modular Platform(MAX/Mojo) — 로컬 27B 서빙 백엔드 이식성 스팟체크
- **도메인**: ai-news (교차 local-llm)
- **출처**: [[Modular-Platform]] · [[Qwen3.8-27B-GGUF]] · [[Qwen3.8-27B-FP8]] · [[llmfit]] · [[LLMRouter]]
- **할 것**: [[Modular-Platform]](Mojo+MAX)의 지원 모델·하드웨어 매트릭스·라이선스 확인 후, [[Qwen3.8-27B]]류 로컬 27B를 MAX로 서빙해 llama.cpp(GGUF Q4/Q5)·FP8(GPU) 대비 처리량·지연·이식성을 스팟체크 → "적합성 필터([[llmfit]])→서빙 백엔드(MAX)→라우팅 게이트([[LLMRouter]])" 로컬 스택에 편입할지 판정. **GPU/CPU 이식성·성능 벤치 미검증(실WebFetch 미수행) → 수치 인용 금지, 지원 매트릭스·라이선스 확인 우선.**
- **우선순위**: 낮음
- **상태**: 대기
