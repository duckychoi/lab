---
title: PentAGI — 자율 침투테스트 에이전트 시스템
type: source
domain: ai-news
tags: [ai-news, github-trending, security, offensive-security, agent, sandbox, go, 한정어-탈락]
created: 2026-09-13
updated: 2026-09-13
sources: [raw.md]
reliability: high
identifiers: [vxcontrol/pentagi]
---

# PentAGI — 자율 침투테스트 에이전트 시스템

**GitHub**: https://github.com/vxcontrol/pentagi · `vxcontrol/pentagi`
**지표(2026-09-13 API 실호출)**: ⭐**23,624** · fork **3,076** · 이슈 **60** · **Go** · **MIT**
**생성 2025-01-06 · 최종 푸시 2026-09-10** — 8개월 된 레포다(신생 아님)
**드리프트**: raw ⭐23,621 vs API **23,624**(+3) → API값 채택. fork·이슈·언어·라이선스 **전건 일치**

> [!insight] 핵심 인사이트 — **레포가 자기 설명을 19행 뒤에서 스스로 부인한다**
> GitHub description과 README 63행은 *"**Fully Autonomous**"* 다. 그런데 **82행 `### Current Capability Boundaries`** 섹션이 이렇게 적는다(원문 84~85행 실측):
> - *"PentAGI today is an autonomous **and assistant-guided** penetration testing platform, **not** a CALDERA-style Breach and Attack Simulation (BAS) or adversary emulation product with predefined campaigns or attack plans."*
> - *"BAS-like agent-authored attack scripts should be treated as **conceptual or future work, not as a feature that is implemented today**."*
>
> 🎯 **"완전 자율"을 부인하는 주체가 경쟁자도 리뷰어도 아니라 레포 자신이다.** 그리고 그 부인은 **주장으로부터 19행 거리**에 있다. 헤드라인만 읽는 독자와 한 화면 더 내린 독자가 **다른 제품을 보게 된다** → [[한정어-탈락]]의 구조적 사례.

> [!note] 실제 구조 — 샌드박스 + 툴 위임
> Docker 샌드박스 안에서 nmap·metasploit·sqlmap 등 **20+ 보안 툴**을 LLM 에이전트가 위임 구조로 호출하는 자가호스팅 플랫폼. LLM 공급자 **10종+ 교체 가능**. 실행 모니터링과 태스크 플래닝은 *optional*(63행)로 표기된다.

> [!warning] 사용 조건이 명시되어 있다
> README **1067행**: *"Only test systems you own or are **explicitly authorized** to assess."* 별도 `EULA.md` 존재.
> → 이 레포는 **허가된 대상 한정** 도구다. 볼트는 이 조건을 페이지에 고정해 둔다.

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐23,624 · MIT 본문 확인 · 8개월 운영 · 푸시 3일 전 → **high**
- **즉시 활용**: **NO.** 허가된 침투테스트 대상이 없으면 실행 자체가 규약 위반이다. 구조 참고만.
- **6개월 영향력**: 툴 위임 + 샌드박스 격리 패턴은 보안 외 도메인(데이터 파이프라인)에도 이식 가능한 형태다.
- **허와 실**: *"Fully autonomous"* 는 **레포 자신이 부인한다.** 실제는 **자율 + 어시스트 혼합**이고 BAS는 미구현.
- **액션**: 아키텍처(에이전트↔툴 위임 경계) 읽기. 실행 금지.

> [!question] 미해결
> 20+ 툴의 실제 목록과 위임 프로토콜은 README 밖(소스)에 있다. "어떤 단위로 에이전트에 권한을 주는가"가 [[검사가능성-공사]] 관점의 핵심인데 미확인.

## 관련 페이지
- [[Claude-Red]] — 같은 배치 공격보안. **둘의 차이: PentAGI는 실행기, Claude-Red는 방법론 문서다**
- [[한정어-탈락]] · [[자기제한-명시]] · [[검사가능성-공사]]
- [[에이전트-스킬]]

## 원본
- 출처: https://github.com/vxcontrol/pentagi
- 신뢰도: ⭐⭐⭐ (API 실호출 + README 63/82/84/85/1067행 원문 대조)

---

## 🔄 2026-10-15 갱신 (인제스트 2026-10-15) — **32일 묵은 페이지. 그리고 "수치 없음" 판정이 또 틀렸다**

**GitHub API 실측(2026-10-15)**: ★**30,093**(수집기 30,080 → **+13**) · 포크 **4,503** · watchers **160** · `open_issues` **30** · **Go** · **MIT** · created **2025-01-06T22:22:48Z** · pushed **2026-10-09T20:54:31Z** · 60,947 KB

> [!warning] 🔴 **[[캐시된-지표-신선도]] — 본 페이지는 2026-09-13 이후 갱신되지 않았다 (32일)**
> 파일 수정시각 **09-13 09:17** · 크기 **3,642 B** ⇒ 📌 **금일 배치 7개 갱신 대상 중 가장 오래 방치된 페이지다**(다음은 [[Comfy-Org-Qwen-Image-2.1]] 10-03, 12일).
> 🎯 ⇒ **10-11 [[context-mode]] 에서 세운 *"볼트 전수 나이 점검 스크립트 1회 집행"* action 이 금일까지 미이행이고, 그 비용이 본 페이지로 나타났다.** ⚖️ **본 건은 외부 지적이 아니라 수집기 재배달로 발견됐다 — 여전히 볼트가 스스로 센 것이 아니다.**

> [!warning] 🔴🔴 **볼트 신규 — 수집기 "능력 수치는 레포 설명에 없다"는 *레포 설명* 기준으로는 맞고, README 기준으로는 틀리다**
> 수집기 10-15 보고: *"성공률·탐지율 등 **능력 수치는 레포 설명에 없다**"* · 한계보고 ⑨ *"`pentagi` 성공률"* 미확인
> ✅ **볼트가 README 전문을 수신했다**(`raw.githubusercontent.com` HTTP **200** · **254,433 B** = 금일 배치 최대 문서).
> 🔴 **README 에 측정 수치가 있다** — 다만 **성공률이 아니라 배수(multiplier)다**:
> > *"**Testing with Qwen3.5-27B-FP8** demonstrates that enabling both Execution Monitoring and Task Planning is **essential** for smaller open source models"*
> > — *"**Quality Improvement**: **2x** better results compared to baseline execution without supervision"*
> > — *"Token consumption: **2-3x** increase due to mentor/planner invocations"*
> > — *"Execution time: **2-3x** longer due to analysis and planning steps"*
> > — *"Result quality: **2x** improvement in completeness, accuracy, and attack coverage"*
> 🎯 ⇒ 📌 **수집기 문장은 *"레포 설명(description)"* 으로 범위를 한정했으므로 **거짓이 아니다** — ✅ **정확한 한정어를 썼다.** ⚖️ **그러나 한계보고 ⑨ 의 *"pentagi 성공률 미확인"* 은 README 를 열면 부분 해소된다.**
> 🆕 **볼트 판정: "레포 설명에 없다"와 "레포에 없다"는 다르다** — 📌 **[[벤치마크-이미지-봉인]] ④ 탐색깊이형의 *보고 표현* 버전이다.** 🆕 **규약 ⑪: 수치 부재를 보고할 때 탐색 범위를 명시한다**(10-14 에 볼트가 세운 *"②부재 — README 전문 기준"* 규약의 수집기 측 대응). ✅ **수집기는 이미 그렇게 적고 있다 — 규약이 양쪽에서 정렬됐다.**

### 🔴 그러나 성공률·탐지율은 **진짜로 없다** — 배수는 성공률이 아니다

> [!warning] 🔴 **README 수치의 한계 4건 (볼트 분석)**
> 1. **기준선이 자기 자신이다.** *"compared to baseline execution **without supervision**"* ⇒ 📌 **같은 시스템의 기능을 끈 상태와 비교한다.** 🔴 **다른 침투테스트 도구·인간 대비 비교는 0건이다.**
> 2. **"2x better results"의 측정 지표가 없다.** *"completeness, accuracy, and attack coverage"* 3축이라 적었으나 🔴 **각 축의 정의·측정 방법·절대값 전부 미제시.** ⇒ [[임계-의존-성공률]]: **무엇을 성공으로 세는지 모른다.**
> 3. **모델 1종(Qwen3.5-27B-FP8) 단일 조건이다.** 🔴 **"models < 32B parameters" 일반화를 1개 모델로 한다** → [[표본순위-전수순위]] 계열.
> 4. 🔴 **비용이 품질과 같은 배수다**: 품질 **2x** ↔ 토큰 **2-3x** ↔ 시간 **2-3x** ⇒ 📌 **품질 2배를 위해 비용 2~3배를 쓴다 — 효율 이득이 아니라 등가 교환이거나 손실이다.** ⚖️ **레포는 이 트레이드오프를 `Trade-offs` 제목 아래 스스로 적는다** → 🏆 [[측정도구-먼저-반증]] **금일 3번째 사례**([[VoiceStudio]]·[[iFixAi]] 에 이어).
> ⇒ ⚖️ **종합 판정: 수집기가 찾던 "성공률·탐지율"은 레포 어디에도 없다. README 에 있는 것은 *자기 기능 on/off 배수* 다.** 📌 **미확인 항목을 "부분 해소"로 내리고 종결하지 않는다.**

> [!insight] 🏆 볼트 신규 2 — **지표 구조가 금일 5건 중 가장 이례적이다**
> | | 값 | 금일 배치 내 위치 |
> |---|---:|---|
> | ★ | 30,093 | 4위 |
> | `open_issues` | **30** | 🔴 **2위로 낮다**([[iFixAi]] 8 다음) |
> | 포크 | **4,503** | 3위 |
> | **이슈/포크** | **0.0067** | 🔴 **최저급**([[context-mode]] 0.174 의 **1/26**) |
> | pushed | **2026-10-09** | 🔴 **금일 5건 중 유일하게 6일 정체** |
> | created | **2025-01-06** | 🏆 **유일한 2025년 레포**(나머지 4건은 2026-02~04) |
>
> 🎯 **생성 1년 9개월 · 포크 4,503 · 이슈 30.** ⚖️ **해석 2가지 모두 가능하다**: ① 성숙해서 안정적이다 ② 포크는 되지만 실제로 돌려 보는 사람이 적다. 🔴 **이슈/PR 분해 미실행이므로 판정하지 않는다** → [[복합지표-분해]].
> 📌 **그리고 pushed −6일은 당일 +1,025 증분과 어긋난다** — **코드는 안 움직이는데 스타가 붙었다.** ⚖️ **이것은 10-14 에 볼트가 [[vercel-skills]] 에서 *"pushed −5일 = 정체"* 로 쓴 지표와 같은 패턴이나, 결론은 반대다**(그쪽은 +190 으로 증분도 낮았고 이쪽은 +1,025 다) ⇒ 🆕 **즉 pushed 정체는 단독으로 "급상승 아님"의 근거가 되지 않는다.** 🔴 **10-14 볼트 판정의 과잉 일반화를 금일 스스로 제한한다.**

### ⚖️ 도메인 재판정 — **ai-news 유지, 단 소유자 축 거리 명시**

> [!note] 📌 볼트 소유자 4축과의 거리
> - **video-saas**: 무관
> - **local-llm**: ⚖️ **부분 연결** — *"10+ cloud LLM providers, your own OpenAI-compatible gateway, or **local models through Ollama or vLLM**"* · *"**Air-Gapped Deployments**: production-grade autonomous pentesting in closed network environments with **local LLM inference**"* ⇒ 🏆 **에어갭 환경 로컬 추론 사례로서는 볼트 local-llm 축에 실제 정보가 있다.**
> - **slam-3dgs**: 무관
> - **ai-news**: ✅ 주 분류 유지
> 🎯 **볼트 신규 발굴: PentAGI 의 메모리 스택이 local-llm 축과 겹친다** — *"Results and successful approaches are kept in **PostgreSQL with pgvector**"* · *"optional **Neo4j knowledge graph** tracks hosts, services and findings"* ⇒ 📌 **[[에이전트-메모리-레이어]] 의 실배포 사례다**(벡터DB + 지식그래프 2층). ⚖️ **금일 [[Cortex]](파라메트릭 공고화)와 정반대 극이고, 둘을 나란히 두면 메모리 설계 스펙트럼이 양끝으로 채워진다.**

> [!action] 당장 할 것 (갱신)
> ⬜ 🔴 **볼트 전수 나이 점검 스크립트 집행 — 5배치 연속 미이행.** 📌 **본 페이지(32일)가 그 비용의 3번째 구체 사례다**([[context-mode]] 158일 · [[claude-mem]] 6개월). ⚖️ **비용은 `grep` 1회다.** 🆕 **금일 이후로 미루지 않기 위해 이번 배치에서 집행한다** → 아래 `## 📊 볼트 전수 나이 점검` 참조(index.md 기록).
> ⬜ ⚖️ **설치·실행은 보류** — 침투테스트 도구이므로 **권한 있는 대상 없이 실행하면 안 된다.** 🔴 **볼트는 테스트 대상 자산이 없다** ⇒ **"외부 코드 실행 0건" 해소 후보에서 제외한다.** 📌 **이것은 적자가 아니라 정당한 제외다 — 구분해서 적는다.**
> ⬜ **`pgvector` + `Neo4j` 2층 메모리 구성을 [[에이전트-메모리-레이어]] 에 실배포 사례로 등재**(금일 집행).

> [!warning] 🔴 미확인 (갱신)
> - **성공률·탐지율** — 🔴 **레포 전체에 없음**(README 254,433 B 기준). **배수만 있다.**
> - **"2x better results"의 측정 지표 정의** — 미제시
> - **Qwen3.5-27B-FP8 외 모델에서의 수치** — 미제시(1종 단일 조건)
> - **`open_issues` 30 의 이슈/PR 분해** — 미실행(볼트 연속 누락)
> - **PentAGI Enterprise 와 OSS 의 기능 경계** — README 에 언급만 있고 상세 미확인

## 관련 페이지 (10-15 추가)
- [[캐시된-지표-신선도]] — 🔴 **32일 방치 · 볼트 전수 점검 5배치 미이행의 3번째 구체 비용**
- [[벤치마크-이미지-봉인]] — 🆕 **규약 ⑪**(수치 부재 보고 시 탐색 범위 명시) · ✅ **수집기는 이미 준수 중**
- [[측정도구-먼저-반증]] — 🏆 **금일 3번째 사례**(`Trade-offs` 로 비용 2-3x 를 자기 공개)
- [[임계-의존-성공률]] — 🔴 "2x better results"의 성공 정의 부재
- [[복합지표-분해]] — 🔴 `open_issues` 30 미분해
- [[에이전트-메모리-레이어]] — 🏆 **실배포 사례 등재**(pgvector + Neo4j 2층)
- [[Cortex]] — ⚖️ **메모리 설계 정반대 극**(외부 저장 ↔ 파라메트릭 공고화)
- [[vercel-skills]] — 🔴 **10-14 "pushed 정체 = 급상승 아님" 판정을 본 건이 제한한다**(pushed −6일인데 +1,025)
- [[vxcontrol]] — 저작자(엔티티)
- [[rea]] · [[VoiceStudio]] · [[iFixAi]] · [[context-mode]] — 금일 GitHub 동일 배치
- [[ai-news]]

## 원본 (10-15 갱신)
- 수집: 2026-10-15 자동수집(ai-news) · 인제스트 2026-10-15 · **이전 갱신 2026-09-13(32일 전)**
- 볼트 실측 **2건**: GitHub API `/repos`(HTTP **200** · ★30,093 · 포크 4,503 · issues 30 · MIT · topics 18개) · **README 전문**(HTTP **200** · **254,433 B** · 금일 최대 문서)
- raw 대비: ✅ 스타(+13)·포크·언어·MIT·생성일·pushed **전건 일치** · ✅ **수집기 *"레포 설명에 없다"* 한정어 정확** · 🏆 **볼트 신규 5건**: README 배수 수치 4종 발굴(2x 품질 / 2-3x 토큰·시간) · **배수의 기준선이 자기 자신임을 특정**(타 도구 비교 0건) · **품질 2x ↔ 비용 2-3x = 등가 교환 이상** 지적 · **pgvector+Neo4j 실배포 메모리 2층** 발굴 · 🔴 **10-14 볼트 "pushed 정체" 판정의 과잉 일반화를 자기 제한**
- 신뢰도: ⭐⭐⭐ (지표·README 1차 확인 / 🔴 **성공률·탐지율 레포 전체 부재 확정 · 코드 미실행(정당 제외) · 이슈 미분해**)
