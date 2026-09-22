---
title: "CodeMidas — 이슈·커밋 없이 소스코드만으로 코딩 RL 환경 5,545개. 초록의 '%'는 본문이 스스로 %p라고 적었다"
type: source
domain: ai-news
tags: [ai-news, hf-paper, xiaomi, mimo, reinforcement-learning, agentic-rl, coding-agent, rl-environment, grpo, 단위-불일치, 검사가능성-후퇴]
created: 2026-09-22
updated: 2026-09-22
sources: []
reliability: low
---

# CodeMidas: Scaling Agentic Coding RL Environments from Code Itself

> [!insight] 핵심 인사이트 — **RL 과제의 원료를 "개발 기록"에서 "이미 구현된 기능"으로 바꿨다**
> 기존 파이프라인(SWE-bench 계열·R2E-Gym·SWE-smith·SWE-Flow 등)은 이슈·PR·커밋·기존 테스트·문서 중 하나가 있어야 과제를 만든다. CodeMidas는 **소스코드만** 입력으로 받는다: 에이전트가 기존 기능을 탐색해 **행동 명세**를 쓰고 → 그 기능을 지운 개발 시작점을 만들고 → **원본 코드 실행으로 기대값을 얻은 테스트**를 짓고 → **적대적 롤아웃(누출 탐지) · 풀이 리뷰 · 롤아웃 성공률**로 거른다.
> 규모: **3,185 코드베이스 · 23개 언어 · 15개 기술 도메인 · 5,545 과제**. 참조 풀이 중앙값 **142줄**(IQR 66–305), **65.9%가 2개 이상 파일 수정**. 언어는 Python 21.4% · TypeScript 18.3% · Go 16.2%.
> 🎯 **품질 필터가 양보다 강하다는 실측**: 필터 전 **8k(바닐라)** 보다 필터 후 **3k** 가 세 평가 모두에서 높다. 5k는 8k 대비 SWE-bench Pro **+0.59** · DeepSWE **+4.59** · Val **+4.49** %p.

> [!warning] ✅ 수집기 판정 확인 — **초록의 "%" 는 %p다. 그리고 본문이 그 단위를 직접 선언한다**
> 초록: *"issue repair (DeepSWE **+ 11.7%**), whole-program construction (ProgramBench **+17%**), and terminal work (Terminal-Bench v2.1 **+8.5%**)"*.
> 본문 §4.1: *"For each benchmark, we report **absolute score improvements** relative to the initial policy **in percentage points**."* 그림 5 캡션도 *"absolute improvements … in percentage points"*.
>
> | 벤치 | 초기 | RL 후 | 초록 표기 | 실제 | 상대로 읽으면 |
> |---|---|---|---|---|---|
> | DeepSWE v1.1 | 10.0% | 21.7% | +11.7% | **+11.7%p** | +117% |
> | Terminal-Bench v2.1 | 63.7% | 72.2% | +8.5% | **+8.5%p** | +13.3% |
> | ProgramBench (**Almost Solved**) | 4.5 | 21.5 | +17% | **+17.0점** | +378% |
>
> 🔴 **저자가 본문에서 %p라고 정의해 놓고 초록에서 `%` 를 썼다** — 요약자 실수가 아니라 **원문 초록의 단위 표기 오류**다.
> 🔴 **ProgramBench 는 한 번 더 조심**: *"Almost Solved, the percentage of tasks passing **at least 95%** of their tests"* — **완전 해결률이 아니다.** 초록의 *"whole-program construction"* 만 읽으면 전체 프로그램을 짓는 성공률로 읽힌다.

> [!warning] 🎯 같은 날 두 논문의 "+11.7" — **숫자는 같고 뜻은 10배 다르다**
> - [[Code2Skill]] 초록 *"improve by **11.7%** on average"* → 본문 *"**relative** gain"*(42.90→47.90, 절대 +5.0점)
> - CodeMidas 초록 *"DeepSWE **+ 11.7%**"* → 본문 *"**percentage points**"*(10.0→21.7, 상대 +117%)
>
> 둘 다 초록에서는 `%` 로 인쇄됐고, **어느 쪽인지는 둘 다 본문을 열어야만 알 수 있다.** 같은 배치(2026-09-21 데일리)에 나란히 올라왔다. → [[단위-불일치]] 의 **"같은 기호, 다른 단위"** 형태의 교과서 사례.

> [!warning] 🔴 공개된 것이 없다 — 코드·데이터·체크포인트 0
> - HF 논문 API `githubRepo`: **없음**. `projectPage`: `https://mimo.xiaomi.com/rl/` — 볼트 정적 fetch 결과 제목이 **"mimo-v2.6 RL"** 인 JS 대시보드다. 즉 **CodeMidas 전용 페이지가 아니라 [[MiMo-V2.6-RL-Livestream]] 의 그 생중계 대시보드**를 가리킨다.
> - GitHub `XiaomiMiMo` 조직 공개 레포 18개(MiMo · MiMo-V2-Flash · MiMo-Skills · MiMo-Code · verl 등) 중 **CodeMidas 없음**. GitHub 검색 "CodeMidas" 13건 전부 무관(논문 요약 봇 등).
> - HF 데이터셋·모델 검색 "CodeMidas": **0건**.
> - 본문에 **공개 계획 문장 없음**(release/available/github 검색 0건).
> 🎯 **"코드 자체에서 검증 가능한 환경을 만든다"는 논문의 환경도, 검증기도, 5,545 과제 목록도 공개되지 않았다.** [[Agora]] 와 같은 형태 → [[검사가능성-후퇴]] 후보(단 Agora처럼 "누구나 체크아웃"을 논지로 내세우지는 않았으므로 아이러니 강도는 낮다).
> 📌 [[MiMo-V2.6-RL-Livestream]] 페이지의 미검증 항목 *"몇 주 내 학습 방식·세부 기술 오픈소스 순차 공개"* — **이 논문은 그 "세부 기술" 공개의 일부로 볼 수 있지만, 오픈소스 공개는 아니다.** 해당 주장은 여전히 미검증으로 둔다.

> [!note] 📌 본문에서 초록이 말하지 않은 것
> 1. **"다섯 개 벤치 전부 향상"인데 본문 텍스트 수치는 셋뿐**이다. SWE-bench Pro · RepoZero C2Rust 의 초기/RL 후 값은 **그림 5 안에만** 있다(볼트 미전사). SWE-bench Pro 에서 5k vs 바닐라 8k 차이는 **+0.59%p** 로 작다.
> 2. **학습 규모** (부록 A): GRPO · 이진 보상 · 배치 32 · 롤아웃 32/과제 · 최대 응답 **516,096 토큰** · **최대 500턴** · staleness 8 · lr 5e-6 · std 정규화 **비활성**. 학습 곡선은 **step 0–70**.
>    ⚠️ 볼트 산술: 배치 32가 과제 수라면 70 step × 32 = **2,240 과제 샘플** — 5,545는 물론 **3k 풀보다도 적다.** 그렇다면 "5k > 3k"는 **더 많이 봐서가 아니라 추출 풀의 다양성/난이도 차이**로 읽어야 한다. (배치 단위가 과제인지 원문이 명시하지 않음 — **확인 필요**.)
> 3. **시드 반복·분산 보고 없음.** 1k/3k/5k/8k 비교가 각 1회로 보인다.
> 4. **행동 변화**(표 2·3): 첫 편집 전 read/search **27.2→40.1** · drafting ratio **0.358→0.629** · 편집 후 고유 검증 명령 **2.03→2.53**(수집기 일치). ProgramBench 에서는 탐색이 늘면서 **총 턴은 155.1→122.8로 줄었다**. 자기검증 유무 차이 **+4.2%p(95% CI 1.8–6.6)** 는 유의하나, 탐색(+0.7, CI −1.9–3.7)·drafting(+1.95, CI −0.04–3.96)은 **CI가 0을 포함**한다 — *"탐색을 늘리면 성공"* 이라고 읽으면 안 된다.
> 5. 저자 19명: 샤오미 **LLM Core** + 베이징대·홍콩대·인민대 인턴, 교신 **Tong Yang · Fuli Luo**. Fuli Luo는 [[MiMo-V2.6-RL-Livestream]] 페이지의 *"루푸리(샤오미 LLM 총괄)"* 로 보인다(한자 표기 대조는 미확인).

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐ — 업보트 103 · 샤오미 MiMo 공식 논문 · 수치는 본문 텍스트로 확인 가능 / **코드·데이터·체크포인트 0 · 시드 반복 없음 · 두 벤치 수치는 그림에만**. 스타·다운로드 기반 스키마로는 측정 대상 자체가 없다.
- **즉시 활용**: **NO — 돌릴 것이 없다.** ✅ **설계 아이디어는 즉시 가져갈 수 있다**: *기존 기능을 지우고 → 원본 실행 결과를 기대값으로 테스트를 만든다.* 볼트가 가진 스크립트(수집기·인제스트 도구)에 **회귀 테스트를 자동 생성하는 방법**으로 그대로 쓸 수 있다.
- **6개월 영향력**: 🎯 코딩 RL 데이터의 병목이 **"이슈가 달린 레포"에서 "돌아가는 코드가 있는 레포"로** 풀린다 — 원료 풀이 몇 자릿수 커진다. [[Code2Skill]] 이 같은 원료(소스코드)를 **스킬**로, CodeMidas는 **RL 환경**으로 가공했다 — **같은 주에 "코드를 원료로" 두 갈래**.
- **대체 관계**: SWE-smith·R2E-Gym·SWE-rebench 류 환경 합성과 **경쟁**. [[하네스형-에이전틱-RL]] 의 환경 공급측에 해당(최대 500턴 · 516K 응답 토큰의 장기 에이전틱 롤아웃).
- **허와 실**: ✅ 필터 절제(3k > 바닐라 8k)는 설득력 있다. ✅ 행동 지표 정의(부록 B)가 구체적이고 CI를 보고했다. 🔴 초록 `%` 표기는 본문과 모순. 🔴 ProgramBench는 "거의 해결" 지표. 🔴 재현 불가.
- **액션**: 볼트 도구 스크립트 하나에 **"기능 삭제 → 원본 실행으로 기대값 채집 → 테스트화"** 절차를 수작업으로 1회 적용해 본다.

> [!action] 당장 할 것 (1건)
> [[단위-불일치]] 에 **"같은 배치·같은 숫자·다른 단위"** 사례로 Code2Skill(+11.7% 상대) ↔ CodeMidas(+11.7% 실은 %p)를 한 줄 표로 추가하고, 수집기 규칙에 *"초록 `%` 는 본문에서 relative/percentage points 문구를 찾아 확정"* 을 제안한다.

> [!question] 미해결 질문
> 1. 그림 5의 SWE-bench Pro · RepoZero C2Rust 초기/RL 후 값.
> 2. 배치 32의 단위(과제 vs 롤아웃)와 총 학습 step — 5k 풀이 실제로 한 번이라도 다 소비됐는가.
> 3. 과제·검증기 공개 계획 여부 — 본문·프로젝트 페이지 어디에도 없음.

## 관련 페이지
- [[MiMo-V2.6-RL-Livestream]]
- [[Code2Skill]]
- [[단위-불일치]]
- [[하네스형-에이전틱-RL]]
- [[agent-lightning]]
- [[검사가능성-후퇴]]
- [[Agora]]
- [[한정어-탈락]]
- [[게시일-이중화]]
- [[ai-news]]

## 원본
- 출처: https://huggingface.co/papers/2609.22068 · https://arxiv.org/abs/2609.22068 · (projectPage) https://mimo.xiaomi.com/rl/
- 날짜: arXiv `publishedAt` **2026-09-18**(v1) · HF 데일리 `submittedOnDailyAt` **2026-09-21**(3일 차) → [[게시일-이중화]]
- 볼트 실측(2026-09-22): 업보트 **103**(수집기 54) · 저자 **19**(수집기 일치) · 조직 Xiaomi MiMo · `githubRepo` 없음 · GitHub `XiaomiMiMo` 조직 레포 18개 중 해당 없음 · HF 데이터셋/모델 검색 0건 · projectPage = MiMo-V2.6 RL 대시보드
- 수치 출처: arXiv HTML **목차 + §3.5 · §4.1 · §4.2 · §5.1 · §5.2 · 표 2·3 · 부록 A(표 A1)·B** 원문 실열람
- raw 대비: ✅ **%p 판정 · 10.0→21.7 · 63.7→72.2 · 4.5→21.5 · Val 35.0→44.7 · 행동지표 3종 전건 일치** · 볼트 추가 = 🔴 본문이 %p를 스스로 선언(초록과 모순) · 🎯 Code2Skill "+11.7" 과 단위 상반 · 🔴 공개물 0(조직 레포·HF 검색) · 📌 projectPage = V2.6 생중계 대시보드 · ⚠️ 5개 중 2개 벤치 수치는 그림에만 · ⚠️ 학습 step×배치 < 풀 크기(확인 필요) · ⚠️ 탐색·drafting 연관 CI 0 포함
- 신뢰도: ⭐ (수치 본문 확인 가능 · 필터 절제 설득력 / **재현 수단 0** · 시드 반복 없음 · 초록 단위 오표기)
