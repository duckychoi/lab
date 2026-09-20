---
title: "Agora — '모든 주장이 체크아웃 가능한 커밋'이라는 논문의 레포에 코드가 0개다"
type: source
domain: ai-news
tags: [ai-news, hf-paper, github, autoresearch, multi-agent, git, append-only, 검사가능성-후퇴, nvidia]
created: 2026-09-20
updated: 2026-09-20
sources: []
reliability: medium
---

# Agora: Git as Shared Memory for Collective AutoResearch

> [!insight] 핵심 인사이트 — **연구 기록을 Git의 append-only DAG로 만든다**
> 자율연구 에이전트를 여러 개 돌리면 세션마다 처음부터 시작해 **탐색이 중복**된다. Agora는 결과·통찰·가설·검증·보고를 각각 **불변 커밋**으로 만들고 부모 엣지로 *무엇 위에 쌓았는지*를 남긴다. 파생 인덱스가 **프런티어 · 방치된 가지 · 각 주장의 검증 상태**를 노출한다.
> **세 장치**(README): ① Git 기반 기여 이력(+ Git에서 재구축 가능한 SQLite 인덱스) ② **증거 점수 — 자기인용 제외** ③ `analyze()` = **UCB 랭킹**으로 선두와 미탐색을 함께 추천.
> 실사용: **약 12일 · LM 워커 13개 · 중앙 플래너 없음 · 할당 과제 없음 · 두 쪽짜리 브리프만**. 141개 도너(**534GB · 32개 아키텍처 계열**)로 **119,572,320 파라미터** 어텐션-SSM 하이브리드를 **학습 데이터·경사 갱신 없이** 초기화. 1,703 기여 → 평가지표 **3.39 → 1.899 bits/byte**(학습된 GPT-2 124M 대비 격차 **62% 해소**). 우승 레시피 조상 커밋 **145개 · 15개 계정**, 독립 재현 **165건 · 실패 0**.

> [!warning] 🔴 볼트 최대 발견 — **레포에 코드가 없다**
> 볼트 실측(GitHub contents API, default branch `master`): 최상위 항목이 **`LICENSE` · `README.md` · `assets/` · `index.html` 네 개뿐**이다. `language: HTML`.
> 🎯 **논문의 논지가 "every claim is a commit anyone can check out and rerun" 인데, 그 논문의 레포에는 체크아웃할 것이 없다.** 본문 목차에 **§3.4 Prototype implementation** 이 있으므로 프로토타입은 존재하고, **공개되지 않았다.**
> 📌 볼트가 09-19에 수집기에 보낸 요청 3(*"★ 옆에 파일 트리 크기(코드 유무) — ★599 레포가 README+PDF, ★44 레포가 코드 0"*)의 **세 번째 사례**이고, **가장 아이러니한 사례**다.
> → 같은 배치 [[Ternary-Bonsai-2-27B]] 과 함께 신설 [[검사가능성-후퇴]].

> [!warning] 🔴 두 번째 발견 — **초록 마지막 문장 세 개가 전부 누락됐다**
> 초록 원문 말미: *"We describe **the single mid-run human intervention that pulled the community out of a monoculture**, **what the trace does and does not establish**, and **the controlled comparison that would settle whether shared research state improves discovery per unit of compute**."*
> 수집기 한줄요약은 *"중앙 플래너·할당 과제 없이"* 까지만 옮겼다. 빠진 셋은 각각 다음을 뜻한다:
> 1. 🔴 **사람이 한 번 개입했다.** "플래너 없음"은 맞지만 **무개입은 아니다.** 본문에 **§4.7 Human intervention** 절이 따로 있다.
> 2. 🔴 저자가 **트레이스가 입증하는 것과 못 하는 것**을 직접 구분했다.
> 3. 🔴 **핵심 주장이 미검증이라고 저자가 적었다** — *"공유 연구 상태가 연산당 발견을 개선하는지"* 를 가릴 **대조실험은 아직 안 했다.** 부록 제목이 그대로다: **C. Proposed Matched Evaluation Matrix** — *Proposed*.
>
> 🎯 **즉 이 논문의 헤드라인 이득은 저자 자신이 "아직 입증 안 됨"이라고 명시한 것**이고, 수집기 요약은 입증된 것처럼 읽힌다. [[한정어-탈락]] 중에서도 **자기보고 음성 결과의 탈락**이라 무게가 다르다.
> ⚠️ **그리고 초록 안에서 장치 하나가 자기모순한다**: *"a **diversity-aware selection rule keeps the community from collapsing onto one leader**"* 인데 **모노컬처에서 빼내려 사람이 개입해야 했다** → 그 규칙은 최소 1회 실패했다.

> [!note] ✅ 그럼에도 — **볼트가 없다고 적어 온 칸을 이 논문은 갖고 있다**
> [[검사가능성-공사]] 는 *"두 독립 생태계가 같은 배치에 '확인되지 않음' 전용 칸을 만들었다"*([[security-audit-skill]] `needs_validation` · [[oh-my-hermes]] `reported done`)고 기록했고, **볼트엔 그 칸이 없다**(✅/🔴 2값)고 자인했다.
> 🎯 **Agora는 그 칸을 일급 인덱스 차원으로 만들었다** — *"a derived index exposes the frontier, **the neglected branches**, and **the verification status of each claim**"*. **미검증 + 미탐색이 조회 가능한 뷰다.** 세 번째 수렴 사례이고 가장 구조적이다.
> ✅ **자기인용 제외**(증거 점수) · **165건 독립 재현, 실패 0** · **§4.5 Negative results** 절 · **§4.8 How we verified the record** · **부록 A Reproducibility Requirements** — 절 제목만으로도 이 팀이 무엇을 신경 썼는지가 보인다.
> 🔴 다만 README 자인: *"**Authentication and project metadata require separate database backups.**"* — **전부가 Git 안에 있지는 않다.**

> [!note] 📌 저자 소속 — 수집기가 적지 않은 것
> README 실측 저자: Yifan Zhang · Yunheng Zou · Shaokun Zhang · Jian Hu · **Hao Zhang** · Binfeng Xu · **Jan Kautz** · **Yi Dong (NVIDIA)**.
> 🎯 **[[NVIDIA]] 가 들어 있다**(Jan Kautz · Yi Dong). 09-18 배치의 [[SoL-Pi]](NVlabs) 에 이어 **NVIDIA가 자율연구/자기개선 축에 두 배치 연속 등장**한다 → [[RSI-프레이밍]] 과 같은 축.
> ⚠️ 저자 중 `Hao Zhang` 은 볼트가 보유한 [[FastVideo]] 제작 조직 `hao-ai-lab` 과 **이름이 같다. 동일인 여부는 확인하지 못했다** — 흔한 이름이므로 단정하지 않는다.

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐⭐ — ★**59**(수집기 57 → +2) · **Apache-2.0** · fork 2 · **open issues 0** · created 2026-09-17 · 🔴 **코드 0**. 업보트 45(수집기 일치).
- **즉시 활용**: 🔴 **NO — 돌릴 것이 없다.** ✅ **개념은 즉시 활용 가능**: *자기인용 제외* · *방치된 가지를 조회 가능한 뷰로* · *미검증을 등급이 아닌 범주로*. 🎯 **볼트 자신이 그 셋 중 둘을 안 하고 있다** — 볼트 `log.md`/`index.md` 에는 **방치된 가지 뷰가 없고 미검증 전용 칸이 없다.**
- **6개월 영향력**: 대조실험이 나오기 전까지는 **사례 보고 1건**이다. 🎯 다만 *"append-only 기록 + 파생 인덱스"* 라는 형태는 [[apache-maka]] 가 에이전트 대화에서 이미 한 것과 **같은 원형**이다(*"Shorter context is not deleted history"*) — **연구 기록으로 한 층 올라왔다.**
- **대체 관계**: AutoResearch류 단일 에이전트 루프를 **대체하지 않고 감싼다**.
- **허와 실**: 🔴 *"13개 워커가 스스로"* 는 **사람 1회 개입**이 붙어야 정확하다. ✅ 반면 **3.39 → 1.899 bits/byte** 는 고정 평가자(FineWeb-Edu 200문서, 사전학습·파인튜닝·평가자 수정 **금지**)에서 나온 값이라 **과제 설계는 단단하다**.
- **액션**: 볼트 자체에 **"미검증" 칸과 "방치된 가지" 뷰를 만든다.** 코드 없이 규약만으로 가능하다.

> [!action] 당장 할 것
> 볼트 `log.md` 판정값을 **✅/🔴 2값에서 3값으로 확장**한다 — `✅ 확인 · 🔴 틀림 · ⬜ 미검증(심각도 없음)`. [[security-audit-skill]] · [[oh-my-hermes]] · **Agora 세 사례가 같은 것을 가리킨 뒤 볼트만 안 하고 있다.**

> [!question] 미해결 질문
> 1. **§4.7 사람 개입의 내용** — 목차까지만 읽었다. 무엇을 했는지 모른다.
> 2. **1,703 기여 / 165 재현의 원본 DAG가 어디 있는가** — 레포에 없다. 공개 여부 미확인.
> 3. Hao Zhang ↔ `hao-ai-lab` 동일인 여부 — **미확인**.

## 관련 페이지
- [[검사가능성-후퇴]]
- [[검사가능성-공사]]
- [[apache-maka]]
- [[NVIDIA]]
- [[SoL-Pi]]
- [[RSI-프레이밍]]
- [[한정어-탈락]]
- [[Feyospace-v1]]
- [[Recuris]]
- [[FastVideo]]
- [[ai-news]]

## 원본
- 출처: https://huggingface.co/papers/2609.18094 · https://arxiv.org/abs/2609.18094 · https://github.com/yifanzhang-pro/Agora
- 볼트 실측(2026-09-20): 업보트 **45**(수집기 일치) · 저자 **8** · `publishedAt` **2026-09-16** · `submittedOnDailyAt` **2026-09-17** · GitHub ★**59**(수집기 57) · fork 2 · **Apache-2.0** · open issues 0 · **contents = LICENSE · README.md · assets/ · index.html (코드 0)** · default branch `master`
- 수치 출처: 초록 원문 + **arXiv HTML 목차**(§3.4 Prototype implementation · §4.5 Negative results · **§4.7 Human intervention** · §4.8 How we verified the record · **부록 C Proposed Matched Evaluation Matrix**) + **GitHub README 원문**(세 장치 · 저자 소속 · 534GB/32계열/119,572,320 · 두 쪽 브리프 · 인증 메타데이터 예외)
- raw 대비: 볼트 추가 = 🔴 **레포 코드 0** · 🔴 **초록 말미 3개 항목 누락 적발(사람 개입 · 입증 범위 · 대조실험 미실시)** · 🔴 **다양성 규칙의 자기모순** · ✅ **검사가능성 수렴 3번째 사례로 승격** · **NVIDIA 소속 확인**
- 신뢰도: ⭐⭐ (초록 수치 전건 일치 · 과제 설계 견고 · 저자의 자기한정 우수 / **구현 미공개 · 핵심 주장 저자 자인 미검증**)
