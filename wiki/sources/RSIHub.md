---
title: "RSIHub — 에이전트 진화 4방법(AHE·Hyperagents·A-Evolve·GEPA)을 같은 인프라에 올렸더니: 1위가 설정마다 바뀌고, A-Evolve 는 한 벤치에서 1위·다른 벤치에서 변화 0"
type: source
domain: ai-news
tags: [ai-news, hf-paper, github-trending, rsi, agent-evolution, self-improving-agent, harness, gepa, framework, bytedance, reproducibility]
created: 2026-10-26
updated: 2026-10-26
sources: [2610.32253]
reliability: high
---

# RSIHub: A Composable Framework for Agent-Evolution Methods (HF 2610.32253)

**HF**: https://huggingface.co/papers/2610.32253 · org **ByteDance** · 저자 **14명**(Zimu Wang · Xiaobo Wang · Siyu Ye 외) · published 2026-10-23 · 코드 `simple-agent-lab/RSIHub`
**실측(2026-10-26 09:08 UTC)**: upvote **27**(수집기 일치) · ★**196**(수집기 186 → +10) · fork 8 · Apache-2.0 · 레포 생성 **2026-07-03**(논문보다 약 3.5개월 먼저) · push 10-26 · `recipes/` 에 `aevolve · ahe · ahe_codex · gepa · gepa_local · hill_climb · hyperagents(_codex/_dsh/_tbench_full)` 실재 확인
**신뢰도**: ⭐⭐⭐⭐ (코드·레시피 실재 · 저자 스스로 한계 명시 · 단 1회 시행)

> [!insight] 핵심 인사이트 — **RSI 방법 비교의 첫 "같은 조건" 표가 나왔고, 결론은 "승자 없음"**
> 4방법 × 2 시드 에이전트(MiniSWE · Codex) × 2 벤치(Terminal Bench 2 · τ³ Banking), 모델·평가자 고정. 전체 pass@1(%p 는 시드 대비 절대 변화):
> ```
>                      TB2 MiniSWE   TB2 Codex    Banking MiniSWE   Banking Codex
> Seed                    56.2          69.7           27.8              24.7
> AHE                  65.2 (+9.0)   71.9 (+2.2)    28.9 (+1.1)       34.0 (+9.3)
> Hyperagents          69.7 (+13.5)     …           33.0 (+5.2)       28.9 (+4.2)
> A-Evolve             69.7 (+13.5)     …           27.8 (+0.0)          …
> GEPA                 64.0 (+7.8)      …           29.9 (+2.1)       33.0 (+8.3)
> ```
> 🎯 ① 초록의 **"13.5%p" 는 4×4 셀 중 최대치 1개**(MiniSWE·TB2, 두 방법 동률) — 강한 시드(Codex)에서는 TB2 최대 +2.2%p. ② **A-Evolve: TB2 공동 1위 → Banking 에서 train/gate/sealed/overall 전부 +0.0**. ③ Banking 1위는 MiniSWE 에선 Hyperagents, Codex 에선 AHE. ⇒ 저자 원문 *"method rankings are conditional on both the task environment and the starting agent"*.
> 🔴 **sealed(held-out) 퇴행**: Banking·MiniSWE 에서 *"Hyperagents produces the largest overall gain … despite a 2.1-point sealed regression; AHE and GEPA also lose 4.1 and 2.1 points on sealed tasks"*. 전체 점수 이득이 미노출 과제에선 음수일 수 있다.

> [!warning] 수치 해석 주의
> - **"up to" 상한 · 셀 1개**: 13.5%p 는 최약 시드 × 한 벤치. 수집기 "up to +13.5%p pass@1" 은 정확(초록 *"largest observed"*).
> - **1회 시행**: 본문 *"for **one trial per task**"* · *"These descriptive point estimates do not establish the stability of close differences **without repeated runs**"* — [[유의성-자기제한]]·[[자기제한-명시]] 의 모범 사례.
> - **분모가 작다**: TB2 = 89과제(50 train / 19 gate / 20 sealed), Banking = 97과제(50/20/27). TB2 에서 1과제 = 1.12%p. split 열은 **전체 점수 기여분**(N_pass,s / N_all)이라 sealed +5.6 = sealed 20과제 중 5개 추가 성공.
> - 표의 괄호 단위가 "%" 로 찍혀 있으나 본문 정의는 **percentage points**(절대차) — [[단위-불일치]] 소지.
> - 레시피는 *"adapt **selected** policies from"* 원 방법 — 원 논문 구현의 완전 재현이 아니라 정책 부분 이식. 원 논문 보고치와 다르게 나와도 원 방법의 반증은 아님.

## 도메인별 추출 (ai-news)
- **신뢰도**: ★196 · ByteDance · Apache-2.0 · 레시피·평가·컨테이너 디렉터리 실재 · 저자 자기제한 명시. 볼트 기준(스타 1000+)엔 못 미치나 논문+코드 일치도 높음.
- **즉시 활용**: **YES(설계 차용)** — 핵심 설계 원칙 두 개는 지금 내 에이전트 개선 루프에 바로 쓸 수 있다: ① **평가자는 변이 가능 표면(mutable surface) 밖에 둔다**, ② **train / gate / sealed 3분할** — gate 로 후보 채택, sealed 는 변이 피드백에서 완전 배제. 코드 실행은 하지 않았음.
- **6개월 영향력**: 높음 — [[ModularRSI]] 가 "벤치에서 진화시키면 벤치에 맞춰진다(AHE·Meta-Harness 를 벤치 분리 시 기준선 근처)"를 보였고, RSIHub 가 같은 현상을 **4방법 공통 인프라 + sealed split** 으로 재확인. RSI/하네스 진화 논문의 "X 가 Y%p 올렸다"는 이제 **어느 시드·어느 벤치·어느 split** 인지 묻는 것이 기본이 된다.
- **대체 관계**: 방법별 개별 레포(AHE · Hyperagents · A-Evolve · GEPA)를 공통 런타임으로 대체. [[Self-Evolving-Agent-Harness]](이론 서베이 + 주장-증거 감사 대장)의 **실행판** 성격.
- **허와 실**: 프레임워크로서는 실재·견고(중단 복구·경계 강제 시험까지 함). "진화 방법이 효과 있다"는 메시지보다 **"효과가 조건부이고 이월이 불확실하다"** 가 실제 결론. [[RSI-프레이밍]] 관점: 제목에 RSI 를 달았지만 본문은 RSI 달성을 주장하지 않는다(정직한 서술, [[Physical-RSI]] 와 같은 쪽).
- **액션**: ★ + `recipes/README.md`·`docs/` 읽기(실행 X). 내 하네스 개선 실험에 sealed split 도입.

> [!note] 교차 배치 패턴 — "순위가 설정마다 바뀐다"
> [[ModularRSI]](벤치 분리 시 AHE 이득 소멸) · [[RSIAgent]](격차 대부분이 RSI 이전 하네스 몫) · [[Physical-RSI]](재귀 귀속 이득 미분리) · **RSIHub**(1위 교체 + sealed 퇴행) — 볼트의 RSI 계열 4건이 **모두 "보고된 이득 ≠ 진화 방법의 일반적 우위"** 방향. [[분포내-우위]] 와 같은 구조.

## 관련 페이지
- [[RSI-프레이밍]] · [[Self-Evolving-Agent-Harness]] · [[ModularRSI]] · [[RSIAgent]] · [[Dream-RSI]] · [[Physical-RSI]] · [[HarnessOpt-Bench]]
- [[하네스-설계-축]] · [[에이전트-스킬]] · [[분포내-우위]] · [[유의성-자기제한]] · [[자기제한-명시]] · [[단위-불일치]]
- [[ByteDance]] · [[OpenAI]](Codex 시드)
- 같은 배치: [[HiSTEVE]](하네스 이득이 원자과제엔 거의 0) · [[UserArena]] · [[RynnUnify]] · [[Omni-Woodpecker]]

## 원본
- 출처: https://huggingface.co/papers/2610.32253 · https://arxiv.org/html/2610.32253 · https://github.com/simple-agent-lab/RSIHub
- 볼트 실측: upvote 27 · ★196 · fork 8 (2026-10-26 09:08 UTC)
- 신뢰도: ⭐⭐⭐⭐ (코드 실재 · 자기제한 명시 / 1회 시행 · 소분모)
