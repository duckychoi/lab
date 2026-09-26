---
title: "hindsight — SOTA 주장의 수치는 그림 안에 있는데, 누가 쟀는지는 본문에 적혀 있다"
type: source
domain: local-llm
tags: [local-llm, ai-news, github-trending, agent-memory, longmemeval, mcp, 벤치마크-이미지-봉인, 자기제한-명시]
created: 2026-09-26
updated: 2026-09-26
sources: []
reliability: medium
---

# vectorize-io/hindsight

> [!insight] 핵심 인사이트 — **정직한 비대칭 표기와 봉인된 수치가 한 README에 같이 있다**
> 44행: *"Hindsight is the **most accurate agent memory system ever tested** … state-of-the-art performance on the **LongMemEval** benchmark"*.
> 🔴 **그 문장을 뒷받침하는 수치가 README 442행 본문에 0개다.** 바로 다음 46행이 `![Overview](./hindsight-docs/static/img/hindsight-benchmarks.png)` — **점수는 이미지 안에만 있다.** 본문에서 `%` 를 포함한 줄은 딱 2개인데 둘 다 *"99.9% uptime SLA"*(클라우드 상품 설명)다. **벤치 수치는 문자로 존재하지 않는다.**
> 🎯 **그런데 50행이 드물게 정직하다**: *"The benchmark performance data for Hindsight has been **independently reproduced** by research collaborators at the Virginia Tech Sanghani Center … and The Washington Post. **Other scores are self-reported by software vendors.**"* — **자기 점수는 제3자 재현, 남의 점수는 자기보고**라고 **스스로 구분해 적는다.**
> 📌 이 조합이 이 페이지의 요점이다. **비교의 신뢰 구조는 밝히고, 비교의 값은 봉인했다.** 전자는 [[자기제한-명시]] 의 좋은 사례고 후자는 [[벤치마크-이미지-봉인]] 의 사례다. **같은 저자가 한쪽은 열고 한쪽은 닫았다.**

> [!warning] 🔴 기준 시점이 8개월 낡았다
> 44행이 비교 기준을 *"as of **January 2026**"* 로 못 박는다. 오늘은 2026-09-26이므로 **약 8개월 전 스냅샷으로 "ever tested" 를 주장**하는 셈이다. 그 사이 [[mem0]]·[[SpeakerMem-R1]] 등 경쟁·인접 작업이 갱신됐다.
> 🎯 09-24 [[TradingAgents]] 교훈(*"시점 의존 관측을 인사이트의 토대로 쓰면 만료된다"*)의 **벤더판**이다. 볼트가 자기 페이지에서 겪은 만료를 여기서는 벤더가 README에 박아 두고 있다 — **다만 시점을 적어 뒀기 때문에 만료를 알 수 있다.** 적지 않은 것보다 낫다.

> [!note] 구조 — retain / recall / reflect 3연산
> 메모리 뱅크 + 멘탈 모델 구조 위에서 3연산을 노출한다(137·140·143행): **Retain**(저장) · **Recall**(검색) · **Reflect**(성향 반영 응답 생성). 목표는 대화 회상이 아니라 **누적 학습**이다.
> 배치 경로 3종: Docker 서버 · **Python 임베디드(서버 불필요)** · MCP 서버(269행 — *"expose retain, recall and reflect as tools"*). LLM 래퍼는 2줄(225~226행: *"Hindsight recalls relevant memories before the call and retains the conversation after it"*).
> 논문: arXiv **2512.12818**(README 5·413행에서 확인). ⬜ **논문 본문 미열람** — 봉인된 수치가 여기 있을 가능성이 가장 높다(actionable 등록).

## 도메인별 추출 (local-llm)

- **실용성 판단**: **배포 가능.** Python 임베디드 모드가 서버를 요구하지 않는 것이 결정적이다 — 단일 프로세스 에이전트에 바로 얹힌다. 🔴 단 지연시간 수치가 README에 **없다**(하드웨어 요구도 없음).
- **메모리 아키텍처**: **외부DB + 반성(reflection) 혼합**. 순수 RAG가 아니라 memory bank(원자적 관찰) → mental model(요약된 성향)의 **2층 승격 구조**다. [[에이전트-메모리-레이어]] 의 "압축이 아니라 이중화" 계열([[SpeakerMem-R1]]·[[The-Past-Frames-the-Future]] 09-24 관측)과 **같은 처방**이며, 오늘 그 계열에 **제품 구현체**가 붙었다.
- **Hermes 적용**: **가능성 높음** — MCP 서버 경로가 있으므로 [[hermes-agent]] 에 도구로 노출할 수 있다. 🎯 같은 배치 [[superpowers]] 가 **Hermes Agent 를 공식 설치 대상에 포함**하고 있어, 두 건이 같은 날 같은 방향을 가리킨다. ⬜ 실제 연결 미검증.
- **트레이드오프**: ⬜ **수치로 말할 수 없다.** 정확도는 그림 안, 지연·비용은 미제시. 말할 수 있는 것은 **운영 형태의 트레이드오프**뿐이다 — 임베디드(간단·확장 불가) vs Docker(운영 부담) vs Cloud(종속·사용량 과금, 99.9% SLA).
- **오픈소스 구현체**: **이 리포 자체가 그것이다**(MIT · Python · ★30,382). 🔴 단 [[mem0ai]] 와 **같은 오픈코어 형태** — 405행이 *"Skip all of it with Hindsight Cloud"* 로 매니지드를 권한다. mem0 때 볼트가 기록한 *"벤치 점수는 매니지드 플랫폼의 것"* 의혹이 **여기서는 확인도 반박도 불가**하다(점수가 이미지라서).

> [!action] 당장 할 것
> ① arXiv **2512.12818** 본문을 열어 **LongMemEval 점수표를 문자로 확보** — 이 페이지의 최대 공백이다. ② 임베디드 모드 `pip` 설치 후 retain/recall 1회 왕복 실측(볼트 **코드 실행 0건 8배치 연속** 해소 후보).

## 관련 페이지
- [[에이전트-메모리-레이어]] · [[벤치마크-이미지-봉인]] · [[자기제한-명시]] · [[표-부분인용]]
- [[mem0]] · [[mem0ai]] · [[SpeakerMem-R1]] · [[The-Past-Frames-the-Future]] · [[PageIndex]]
- [[vectorize-io]] · [[hermes-agent]] · [[superpowers]]

## 원본
- 출처: https://github.com/vectorize-io/hindsight
- 실측(2026-09-26 GitHub API): ★**30,382** · 포크 3,260 · 오픈이슈 137 · watchers 68 · MIT · Python · 생성 2025-10-30 · 푸시 2026-09-25T20:14:12Z · topics `agentic-ai,agents,ai-memory,memory` · repo id 1086419061
- 수집기 대조: ★30,373 → 볼트 30,382(**+9 드리프트**) · **당일 +1,653** · 포크·라이선스·topics·생성일 **일치** · 인용 문구 3건(44·50행) **축자 일치**
- 확인 범위: **README 442행 전문 열람.** 🔴 arXiv 2512.12818 본문 미열람 · 🔴 벤치 이미지 미판독 · 🔴 미실행
- 신뢰도: ⭐⭐⭐ **medium** — 수치는 API 실검증이나 **성능 주장이 문자로 대조 불가**. 기준 시점 8개월 낡음. (제3자 재현 표기가 있어 low 가 아니다)
