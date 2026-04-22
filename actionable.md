# Actionable — 당장 써먹을 수 있는 것들

ingest할 때마다 LLM이 갱신한다. 완료된 항목은 삭제하지 말고 상태를 "완료"로 바꾼다.

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
