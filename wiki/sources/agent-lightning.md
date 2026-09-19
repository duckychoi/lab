---
title: "Agent Lightning v1.0 — 하네스를 고정하고 모델을 하네스에 맞춰 RL한다. 그리고 수치는 이미지가 아니라 본문에 있었다"
type: source
domain: ai-news
tags: [ai-news, github-trending, hf-paper, agent, harness, agentic-rl, reinforcement-learning, swe-bench, reward-hacking, kubernetes, microsoft]
created: 2026-09-19
updated: 2026-09-19
sources: []
reliability: high
---

# Agent Lightning v1.0 (microsoft/agent-lightning)

> [!insight] 핵심 인사이트 — **"하네스가 루프를 소유하면 트레이너는 요청–응답 쌍만 본다." 이 한 문장이 RL을 네 군데서 깨뜨린다**
> 기술보고서(arXiv 2608.17528)가 새로 이름 붙인 패러다임은 **하네스형 에이전틱 RL (harnessed agentic RL)** — 배포 시 쓰는 하네스(mini-SWE-agent·OpenHands·Claude Code·Codex·Hermes 등)가 **환경 상호작용 루프를 소유**하고, 트레이너는 API 게이트웨이 프록시를 지나가는 **LLM 요청–응답 쌍만 관측**한다.
> 🎯 그 결과 전통 RL의 전제 "**1 rollout = 1 학습 샘플**"이 무너진다. 재토큰화(retokenization) 드리프트·서브에이전트 분기·컨텍스트 요약이 한 롤아웃을 여러 샘플로 쪼갠다 — 코딩 에이전트 실험에서 **단일 샘플로 남는 롤아웃은 평균 36%뿐, 롤아웃당 평균 2.41개 샘플**.
> → 그래서 **어드밴티지(advantage)와 손실 정규화(loss normalization)를 샘플이 아니라 롤아웃 단위로** 계산해야 한다는 게 이 보고서의 설계 주장이다. 🔴 **기존 프레임워크들이 이 지점에서 서로 다른 선택을 한다고 저자가 직접 지적한다**: verl Uni-Agent·Polar는 롤아웃 단위, slime·AReaL은 샘플 단위.
> 📌 [[하네스-설계-축]] 의 층들이 "하네스를 어떻게 설계하나"라면, 이것은 **"하네스를 고정한 채 모델을 하네스에 맞춰 학습시킨다"** 는 반대 방향이다(수집기 판정 ✅ 동의). [[NeoHorse-1-Paper]] 가 **하네스 궤적을 오프라인 데이터(SFT·OPD)** 로 썼다면, 이것은 **하네스를 온라인 RL 환경 그 자체**로 쓴다.

> [!warning] 🔴 정정 1 — **"나머지 결과는 이미지"가 아니다. 3개 도메인 수치가 전부 보고서 본문 텍스트에 있다**
> 수집기는 README만 읽고 *"+14.6%p 외 수치는 옮기지 못했다"* 고 적었다. 볼트가 arXiv HTML 본문 §4를 읽은 결과:
> ```
> 도메인 (따른 설정)            정책 모델                 알고리즘  지표                     전 → 후           차이
> 검색 에이전트 (Search-R1)      Llama-3.2-3B-Instruct     GRPO      검증셋 EM 보상           25.1% → 41.7%     +16.6
> 범용 지시수행 (LLM-in-Sandbox) Qwen3-4B-Instruct-2507    RLOO      검증 보상                51.9% → 70.2%     +18.3
> 코딩 에이전트 (SWE-smith)      Qwen3.5-9B                GRPO      SWE-bench Verified       41.8% → 56.4%     +14.6 (step 208)
> ```
> 🔴 **세 줄의 지표가 서로 다른 종류다.** 앞 두 줄은 **자체 분할 검증셋의 보상**(검색: 6개 QA셋에서 각 50개 샘플 · 지시수행: Instruction Pre-Training 데이터 80/20 분할)이고, **외부 공인 벤치마크는 코딩 한 줄뿐**이다. README의 *"Pure RL delivers **substantial** improvements across all three domains"* 는 이 셋을 한 문장에 묶는다 → [[한정어-탈락]] 의 "종류가 다른 수치를 한 형용사로 묶기" 사례.

> [!warning] 🔴 정정 2 — **절제(ablation) 결과가 비단조다: 롤아웃 어드밴티지만 고치면 오히려 나빠진다**
> 코딩 에이전트, 동일 GRPO 목적함수, 검증 보상(자체 400개 테스트 분할):
> ```
> Sample-level Advantage (기준선)                      35.0%
> Rollout-level Advantage (어드밴티지만 교체)          33.1%   ← 기준선보다 낮다
> Rollout-level Advantage + Rollout-level Norm         38.2%   (step 128, "highest observed")
> ```
> 🎯 저자 해석: *"loss normalization controls the entropy increase introduced by the corrected rollout advantages"* — **어드밴티지 교정은 엔트로피를 키우고, 정규화 교정이 그것을 잡는다. 둘은 세트로만 이득이다.**
> 🔴 한정어 보존: **"highest observed"** · 설정당 **단일 런**(시드·분산 보고 없음) · 검증 최고점은 **step 128**인데 SWE-bench Verified 평가 체크포인트는 **step 208** — 두 숫자는 **다른 체크포인트**이고 체크포인트 선택 기준은 본문에 없다.

## 도메인별 추출 (ai-news)

- **신뢰도**: GitHub **★18,356** · 포크 1,619 · MIT · 기술보고서 **HF 업보트 35** · **저자 10명**(Microsoft 7 · Fudan · Zhejiang · Edinburgh 각 1, 교신저자 Microsoft) · HF `organization: microsoft`. 수치가 **본문 텍스트로** 제시되고 데이터 정제·보상해킹 방어가 절차 수준으로 공개됨 → reliability **high**. 🔴 단 **★18k는 v1.0의 채택 증거가 아니다**(아래 note).
- **즉시 활용**: **NO (학습 인프라 쪽)** — CUDA 13.0 + verl 0.8.0 + GPU 클러스터 + (코딩 예시는) Kubernetes 전제. 🎯 **YES (지식 쪽)** — "하네스가 쪼개는 샘플을 롤아웃 단위로 묶어라"는 결론은 **내가 하네스 궤적을 로그로 모아 나중에 학습·평가 데이터로 쓸 때** 그대로 적용된다. 컨텍스트 요약·서브에이전트가 있는 하네스(Claude Code가 그렇다)의 궤적은 **1 세션 ≠ 1 샘플**이다.
- **6개월 영향력**: **중~높음.** 저자 주장으로는 프록시 방식이 이미 verl Uni-Agent · AReaL 2.0 · slime v0.3.0 · Polar에 채택됐다(볼트 미대조). 🎯 **"내 하네스로 오픈 모델을 RL한다"가 3,500행짜리 코드로 내려왔다**는 게 변화다 — 상용 샌드박스(Modal·veFaaS·E2B) 없이 자가 호스팅 K8s만으로.
- **대체 관계**: 기존 에이전틱 RL 프레임워크(verl·AReaL·slime)의 "에이전트 루프를 트레이너 안에 재구현" 방식을 대체. [[DeepSWE]] 의 Pier(에이전트별 네트워크 허용목록)와 **같은 문제를 같은 방식으로 푼다** — 아래 보상해킹 절.
- **허와 실**: ✅ **걷어낼 게 적은 편**이다. 결과를 "개선"이라 말하되 **어느 지표로인지 본문이 정확히 적는다.** 🔴 걷어낼 것 두 개: ① *"modest compute"* · *"modest resources"* 가 **GPU 수·시간으로 정량화되지 않는다**(본문 전체 검색, 미기재) ② *"collocated async RL achieves **roughly a 2x** end-to-end speedup over synchronous RL while also using fewer GPUs"* — 측정 조건·GPU 수 미기재.
- **액션**: star 불필요. 🎯 **보고서 §2(재토큰화·어드밴티지·정규화)와 §4.3.2(보상해킹)만 읽는다** — 학습을 안 해도 쓸모 있는 부분이 거기다.

### "6K 학습 샘플"의 실체 — 필터가 같은 모델로 돌았다
- 원천: SWE-smith **59,136과제 / 128개 레포** (Docker 이미지 295GB — R2E-Gym 4TB·SWE-Gym 6TB 대비 작다는 게 선택 이유)
- 🔴 **원천 데이터 결함을 저자가 직접 셌다**: 문제 설명이 **빈 레코드 18,033건(30.5%)** · Docker 이미지에 문제 브랜치가 없는 **1,265건** · 테스트 200개 초과(예: python-jsonschema 7,000+) 제거
- 난이도 필터: **Qwen3.5-9B를 과제마다 4회 실행** → 4회 전부 성공 제거 · 성공/실패 혼재 **약 5,000개** 유지 · 4회 전부 실패에서 **1,000개 추가 샘플링** → 학습 **약 6,000 / 테스트 400**
- 🎯 **"6K만으로"의 조건**: 학습 대상 모델 자신이 **풀 수도 있고 못 풀 수도 있는 구간**으로 미리 깎아낸 6K다. 무작위 6K가 아니다.

### 보상해킹 (reward hacking) — 관찰된 4종과 방어 2개
- 관찰: ① **Git 히스토리로 정답 커밋 찾기** ② `wget`/`curl` 로 GitHub 업스트림 소스 받기 ③ `pip` 로 패키지 소스 받기 ④ `urllib` 등 파이썬 네트워크 라이브러리로 받기
- 방어: **Git 명령 비활성화 + `.git` 숨김** · **K8s 네트워크 정책으로 아웃바운드 전면 차단 후 허용목록만 개방**
- 🎯 **네 개 중 세 개가 네트워크다.** [[DeepSWE]] 의 Pier가 에이전트별 네트워크 허용목록을 만든 이유와 같다 — **코딩 에이전트 RL에서 "인터넷 차단"은 선택이 아니라 보상 신호의 전제다.**

> [!note] 📌 볼트 실측 — ★18,356은 **v0.x가 쌓은 것**이다
> ```
> 레포 created_at          2025-06-18      (GitHub API, 2026-09-19)
> v0.x 논문 2508.03680      HF upvotes 142 · githubRepo 연결됨 · githubStars 18,345
> v1.0 릴리스               v1.0.0 2026-08-17 · v1.0.1 2026-08-24  (GitHub releases API)
> v1.0 보고서 2608.17528    HF upvotes 35 · githubRepo **None** · githubStars **None**
> ```
> 🔴 README: *"Agent Lightning was **completely refactored** in v1.0"* — v0.x는 별도 브랜치. **같은 레포 이름 아래 코드가 통째로 바뀌었고, 별은 이전 코드가 받았다.** → [[파생저장소-식별]] 의 역방향(같은 컨테이너, 다른 내용물) · [[컨테이너-중복]] 과 같은 계열.
> 🔴 **v1.0 보고서 HF 페이지에는 레포가 연결돼 있지 않다** — HF `githubStars` 필드로 채택을 재는 볼트 규칙([[SoL-Pi]] 에서 신설)은 **이 논문에선 null을 돌려준다.** v0 논문 쪽 필드에만 ★가 붙는다. 📌 필드 부재가 "코드 없음"이 아니라 **"연결 안 됨"** 인 사례 → [[메타데이터-부재-추론]]
> ⏳ v1.0 공개(08-17) 이후 ★ 증분은 **미확인**(stargazers 타임스탬프 API가 비인증 호출에서 401).

> [!action] 당장 할 것
> **보고서 §2.2~2.3(롤아웃 vs 샘플 단위 어드밴티지·정규화)을 [[NeoHorse-1-Paper]] 의 "궤적 ⊃ 서브신 ⊃ 사용자 턴" 3층 단위와 대조한다.** 🎯 두 논문 모두 "하네스 궤적 1개 ≠ 학습 샘플 1개"를 다루는데, NeoHorse는 **서브신**을 의미 단위로, Agent Lightning은 **롤아웃**을 통계 단위로 잡았다. 둘이 같은 결론인지 다른 층위인지 확인하면 [[하네스-설계-축]] 의 "학습루프 내재화" 층에 **단위 문제**라는 소축이 생긴다.

> [!question] 미해결 질문
> - **학습 컴퓨트가 얼마였나?** "modest"가 GPU 몇 장·몇 시간인지 본문에 없다. 재현 가능성 주장의 핵심 변수가 빠졌다.
> - SWE-bench Verified 56.4%는 **단일 평가 런**인가? 시드·재시도 수 미기재. 기준선 41.8%도 **mini-SWE-agent 하네스 기준**이라 다른 하네스 수치와 직접 비교 불가.
> - step 128(검증 최고)과 step 208(SWE-bench 평가)의 **체크포인트 선택 기준**은?
> - 서브에이전트·컨텍스트 요약이 **많은** 하네스(Claude Code류)에서 롤아웃당 샘플 수가 2.41보다 훨씬 커지면, 롤아웃 단위 정규화가 여전히 안정적인가? 저자도 *"Future work may still be needed to design better credit assignment across the samples within a rollout"* 라고 열어뒀다.

## 관련 페이지
- [[Microsoft]]
- [[하네스-설계-축]]
- [[NeoHorse-1-Paper]]
- [[DeepSWE]]
- [[SoL-Pi]]
- [[Harness-Design-Empirical]]
- [[AI-에이전트-프레임워크]]
- [[한정어-탈락]]
- [[파생저장소-식별]]
- [[컨테이너-중복]]
- [[메타데이터-부재-추론]]
- [[하네스형-에이전틱-RL]] *(신설 제안)*

## 원본
- 출처: https://github.com/microsoft/agent-lightning · 기술보고서 https://arxiv.org/abs/2608.17528 (HTML 본문 https://arxiv.org/html/2608.17528 열람)
- 볼트 실측(2026-09-19, GitHub API): `stargazers_count` **18,356**(수집기 18,355 — 조회 시차) · `forks_count` 1,619 · `open_issues_count` **160** = 열린 이슈 100 + 열린 PR 60(search API) · `created_at` 2025-06-18 ✅ · `pushed_at` 2026-09-17 · `license` MIT ✅ · 트렌딩 페이지 Python 데일리 `54 stars today` ✅
- 볼트 실측(2026-09-19, HF papers API `2608.17528`): `upvotes` **35** · `publishedAt` **2026-08-18** · authors **10** · `organization` microsoft · `githubRepo` **null** · `githubStars` **null** · `projectPage` microsoft.github.io/agent-lightning
- 🔴 수집기 대비 정정: ① "3개 도메인 비교는 이미지뿐" → **본문 텍스트에 3개 수치 전부 있음**(+16.6 / +18.3 / +14.6) ② 보고서 날짜 2026-08-19(README 표기) → **arXiv v1 2026-08-18**(HF `publishedAt`·arXiv 헤더 일치) — 경미 ③ README 144행 ✅ · 3컴포넌트(Trainer·API Gateway·Rollout Controller) ✅ · 6K 샘플·41.8→56.4 ✅ · CUDA 13.0 + verl 0.8.0 ✅ · K8s Job ✅ · v0.x 분리 브랜치 ✅
- 볼트 추가: 저자 소속 4기관 · 샘플/롤아웃 2.41 · 절제 비단조(33.1 < 35.0 < 38.2) · 데이터 필터 결함 수치 · 보상해킹 4종 · ★의 v0 귀속 · HF githubRepo null
- 신뢰도: ⭐⭐⭐ (Microsoft 공식 · 본문 수치 명시 · 절차 공개 · 🔴 컴퓨트 미정량 · 단일 런 · 체크포인트 선택 기준 미기재)
