---
title: "SpeakerMem-R1 — 다자 대화 화자중심 이중트랙 메모리 (이번 배치 유일한 완전 수치)"
type: source
domain: local-llm
tags: [local-llm, agent-memory, multi-party-dialogue, GRPO, rl, benchmark, 분포지표]
created: 2026-09-24
updated: 2026-09-24
sources: []
reliability: high
---

# SpeakerMem-R1 — 누가 무엇을 말했는가를 메모리 구조로 만든다

**논문**: https://huggingface.co/papers/2609.26780 (arXiv 2609.26780)
**업보트**: **20** (볼트 실측 20 — 드리프트 **0**) · **부속 GitHub**: `2022hpsk/SpeakerMemR1` ★**70** (논문 5건 중 최다)
**게시**: arXiv **2026-09-22** → HF 등재 **2026-09-24** = **2일 차**

> [!insight] 핵심 인사이트
> **에이전트 메모리의 실패가 "검색 실패"가 아니라 "귀속 실패"임을 문제로 세운다.** 초록이 두 병목을 명시한다: *"**message attribution** and relational understanding in multi-party dialogue, and **state reconstruction** from interleaved histories"*. 🎯 볼트 [[mem0]]·[[VoiceMem]]·[[에이전트-메모리-레이어]] 축은 그동안 *무엇을 저장·검색하는가* 였다. 이건 **다자 대화에서 화자를 잃으면 내용이 남아도 쓸 수 없다**는 축을 추가한다 — [[ChinameBot]] 같은 다자 채팅 봇에 정면으로 해당한다.

> [!insight] ✅ 이번 배치 논문 5건 중 **유일하게 수치가 완비된 건**
> 09-21 수집기 요청 2(*"집계값에 분포 지표를 병기하라"*)를 **이 논문만 충족한다.** 초록이 스스로 *"We report **both binary accuracy and token-F1**"* 라고 쓰고, 통제 평가·어블레이션까지 초록에 넣었다. 나머지 4건은 0~2개 수치다.

## 수치 — 초록 축자 대조 (전부 **절대 정확도 %**, %p·상대 아님)

| 벤치/설정 | 값 | 초록 원문 |
|---|---|---|
| GroupMemBench | **47.9%** | *"achieves binary accuracies of 47.9%, 69.2%, and 61.9%, respectively"* |
| SocialMemBench | **69.2%** | 〃 |
| EverMemBench (자체) | **61.9%** | 〃 |
| EverMemBench (공개 리더보드) | **62.33%** | *"On the publicly reported EverMemBench leaderboard from EverMind-AI, we achieves 62.33%, **the best reported result among** the latest state-of-the-art frameworks"* |
| LoCoMo (전체 1,986문항) | **70.85%** | *"achieves 70.85% on all 1,986 LoCoMo questions"* — *"two-person long-term conversation **boundary test**"* |
| 통제 평가 305문항 | SFT **57.38%** → RL **68.20%** (**+10.82 절대**) | *"RL raises the SFT Writer's mean accuracy from 57.38% to 68.20%"* |

✅ **수집기 인용 6/6 문자 일치.** 한정어 *"the best **reported** result"* → *"최고 **보고값**"* 으로 보존 ✅

> [!warning] 🎯 같은 벤치에 값이 둘이다 — 볼트가 먼저 정해야 한다
> **EverMemBench: 자체 61.9% vs 리더보드 62.33%.** 초록만으로는 설정 차이(프롬프트·판정기·문항 집합)가 설명되지 않는다.
> 📌 **볼트 규약**: 이 논문을 다른 메모리 시스템과 대조할 때는 **자체 측정값 61.9% 를 쓴다.** 이유 — 리더보드값은 제출 설정이 저자 통제 밖이고, 나머지 두 벤치(47.9·69.2)가 자체 측정이라 **같은 조건끼리 비교**해야 한다. 리더보드 62.33%는 *"외부 검증 경로가 존재한다"* 는 사실로만 인용한다.
> 🎯 그리고 이 이중값 자체가 강점이다 — **외부 리더보드에 제출된 흔적이 있는 논문은 이번 배치에서 이것뿐이다.**

## 구조

- **이중 트랙**: ① 화자 라벨이 붙은 **원문(verbatim) 메시지** ② **파생 상태(derived states)**. 질의 시점에 **엔티티·사건·시간**으로 두 트랙의 증거를 결합.
- **상태의 2뷰**: **person-level** / **group-level** — *"organized into person-level and group-level views"*
- **Writer-R1 학습**: **SpeakerLevenshtein** + **speaker-conditioned GRPO**. 목적이 명시적이다 — *"to reduce attribution and update errors during structured memory construction **while enabling local deployment**"*.
  🎯 **로컬 배포가 학습 설계의 이유로 초록에 적혀 있다.** 볼트 도메인 2(local-llm)의 *"실배포 가능?"* 질문에 저자가 선제 응답한 형태.
- **어블레이션**: 원문 트랙 ↔ 구조 트랙, person-level ↔ group-level 이 **상호보완적**임을 초록에서 주장(*"are complementary under the standardized evaluation interface"*).

## 도메인별 추출 (local-llm)

- **실용성 판단**: 🟡 **아마 YES, 단 하드웨어 수치 없음.** 로컬 배포가 설계 목표로 명시됐고 Writer를 RL로 작게 만드는 방향이지만, **모델 크기·VRAM·지연 수치가 초록에 0개**다. ⬜ 판단은 본문 필요.
- **메모리 아키텍처**: **외부DB형 + 파생 상태 병행**. RAG 단독도 KV 압축도 아니다 — 원문을 버리지 않고 상태를 따로 쌓는 **이중화**. [[mem0]] 의 단일 메모리 레이어와 다른 설계.
- **Hermes/ChinameBot 적용**: 🎯 **가장 적용 가능성 높은 논문이다.** 다자 채팅에서 *"누가 말했는가"* 를 잃는 문제가 실제로 있고, **원문 트랙 + 화자 라벨** 은 모델 교체 없이 저장 구조만 바꿔 얻을 수 있다. GRPO 학습 없이 **이중트랙 저장 + 질의시 결합**만 베끼는 경로가 있다.
- **트레이드오프**: 원문을 보존하므로 **저장량이 늘고 질의 시 결합 비용이 생긴다.** ⬜ 구체 수치 초록에 없음.
- **오픈소스 구현체**: `2022hpsk/SpeakerMemR1` ★**70** — 이번 배치 논문 중 최다이지만 절대값은 작다. ⬜ 레포 내용 미열람.

> [!warning] ⚠️ 한계
> - 🔴 **arXiv 본문 미열람** — 초록만. 모델 크기·지연·저장량 전부 미확인.
> - 🔴 **GroupMemBench 47.9% 는 절반 이하다.** SOTA 주장과 별개로 **다자 대화 메모리는 아직 대체로 실패한다.** 이 논문의 진짜 메시지는 점수가 아니라 이 숫자다.
> - ⬜ 세 벤치(GroupMemBench·SocialMemBench·EverMemBench)의 규모·출처 미확인. LoCoMo만 1,986문항으로 명시.
> - ⬜ EverMind-AI 조직 실체 미확인.

## 관련 페이지
- [[mem0]] · [[VoiceMem]] · [[에이전트-메모리-레이어]]
- [[The-Past-Frames-the-Future]] — 같은 배치, 생성 쪽 메모리
- [[하네스형-에이전틱-RL]] · [[온폴리시-증류]] — GRPO 계열 인접
- [[게시일-이중화]] · [[비매칭-비교]] — 같은 벤치 이중값
- [[local-llm]]

## 원본
- 출처: https://huggingface.co/papers/2609.26780
- 확인 범위: **HF 논문 API 초록 전문**(볼트 직접 조회) · `githubRepo`·`githubStars` 실측(★70) · **arXiv 본문 미열람** · **GitHub 레포 미열람**
- 신뢰도: ⭐⭐⭐ (업보트 20 · **수치 6종 + 이중 지표 + 어블레이션 초록 명시** · 외부 리더보드 제출 흔적)
