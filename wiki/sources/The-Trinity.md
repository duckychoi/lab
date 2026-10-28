---
title: "The Trinity (NUS) — Creator·Explorer·Evolver로 하니스를 재귀 개선. 헤드라인 +34/+26은 Oracle 선택값이고, 원래 있던 벤치 17개만 보면 +4.4"
type: source
domain: ai-news
tags: [ai-news, hf-paper, recursive-self-improvement, harness, multimodal-agent, real2sim2real, capability-tree, claude-opus-5, nus]
created: 2026-10-28
updated: 2026-10-28
sources: [https://huggingface.co/papers/2610.36077, https://arxiv.org/html/2610.36077]
reliability: low
---

# The Trinity: Capability-Driven Recursive Self-Improvement for Multimodal Agents

**HF**: https://huggingface.co/papers/2610.36077 · published **2026-10-26** · **National University of Singapore**(Weidong Tang · Ruiheng Wang 외 · 저자 **20** · 수집기 일치) · upvote **102**(수집기 일치)
**코드**: 없음(HF `githubRepo` null · 수집기 일치) · arXiv 라이선스 CC BY 4.0
**신뢰도**: ⭐ low(코드 미공개 · 백본 고정 · 아래 분해 참조)

> [!insight] 핵심 인사이트 — "겉모양이 다른 과제도 필요한 능력은 같다"를 하니스 진화의 단위로 삼았다
> - **Evolver**: 검증된 실행 궤적을 바탕으로 과제 트리(표면 범주)를 **능력 트리**로 재구성한다.
> - **Creator**: 같은 노드의 과제들이 공유하는 요구를 **단순화된 검증 가능 시뮬 월드**로 만든다(*Capability-Driven Real2Sim2Real*). 원래 과제로 평가해 전이를 측정한다.
> - **Explorer**: 능력 트리를 따라 재사용 모듈을 선택적 상속으로 진화시켜 **하니스 트리**를 만든다. **Capability-Aware Harness Router**가 공개 과제 정보로 모듈 구성을 고른다.
> - 백본: **동결된 Claude Opus 5** + Base Harness(Prime Agent). 바뀌는 것은 하니스뿐이다 → [[하네스-설계-축]] · [[Anthropic]].

> [!warning] 주의 — 수치 분해(arXiv HTML 본문 직접 확인)
> - 📐 **베이스라인 = Iteration 0 Base Harness**(같은 Claude Opus 5). 외부 에이전트 대비 +34가 아니다. 수집기는 "베이스라인 정의를 확인해야 한다"고 했고, 확인 결과 자기 초기값이다.
> - 🎯 **+34 / +26은 Oracle 라우팅 값이다**: Train 28개 **39.06→73.16**, Unseen 18개 **37.45→63.61**. Table 4의 Oracle이 정확히 73.16/63.61이다. 실제 배포 가능한 **Agent Self-Routing은 71.27 / 60.96**이어서 이득은 **+32.2 / +23.5**가 된다. → [[천장-기준선]]
> - 🧪 **Train 28개 중 11개는 "Agent-built from web-searched sources"(*)**, 즉 에이전트가 직접 만든 벤치다. **원래 있던(native) 벤치 17개만 보면 64.4→68.8(+4.4)**에 그친다(Iteration 1 이후 증가폭도 작다). 큰 이득은 자체 제작 벤치에서 나왔다.
> - 🤖 "실제 임베디드 과제 2개"는 SOON(robot) **1경로 10에피소드**, CaP-X(robot) **10레이아웃 10에피소드**이고 둘 다 **0→60%**다. n=10 두 개가 Unseen 평균을 끌어올린다. 로봇 제외 Unseen 16개는 **42.13→64.06(+21.9)**이다.
> - 📏 외부 참조선: Unseen 16개에서 Codex **47.49** · DeepSeek **46.18**(Iteration 4는 64.06). 다만 같은 하니스 조건인지는 본문만으로 단정할 수 없다 → [[비매칭-비교]].
> - 🔍 저자가 밝힌 한계: 웹 검색으로 벤치를 찾기 때문에 커버리지가 질의마다 달라지고, 연구 범위는 **하니스 수준 자기개선**에 한정된다(가중치는 그대로).
> - 수집기 요약은 28/18개 벤치와 +34/+26을 정확히 옮겼다. 다만 **Oracle 값이라는 점, 자체 제작 벤치 비중, 로봇 n=10을 빠뜨렸다.**

## 도메인별 추출 (ai-news)
- **RSI 계보에서의 위치**: [[RSI-프레이밍]]의 규칙("시드 강도·벤치·sealed split 3축을 확인하기 전에는 인용하지 않는다")을 적용하면, 시드는 강하지만(Claude Opus 5) 벤치의 상당수가 자체 제작이고 sealed split에 해당하는 것은 native 17개다. 그 17개에서 +4.4이므로 [[RSIHub]]의 "보고된 이득 ≠ 일반적 우위" 방향과 맞는다. 볼트 RSI 계열 5번째 사례.
- **쓸 만한 아이디어**: 모듈 효과 측정 실험(관련 모듈 1개 추가 시 Base 39.06→**58.45**, 무관 모듈은 40.08 · Iteration 4에서 관련 모듈 1개 제거 시 73.16→70.42)은 [[하네스-설계-축]]의 "무엇이 이득을 내는가"에 대한 직접 증거다.
- 비교: [[Self-Evolving-Agent-Harness]] · [[EnvHarness]] · [[Co-Evolution-Agentic]] · [[Physical-RSI]] · [[하네스형-에이전틱-RL]]

## 관련 페이지
- [[RSI-프레이밍]] · [[RSIHub]] · [[Physical-RSI]] · [[하네스-설계-축]] · [[천장-기준선]] · [[비매칭-비교]] · [[임바디드-AI]]
- [[Anthropic]](백본 Claude Opus 5)
- 같은 배치(10-28): [[ChronoReplay]] · [[PDRVLA]] · [[Hy-Nomas]] · [[Rollback]]
- [[ai-news]]

## 원본
- https://huggingface.co/papers/2610.36077 · https://arxiv.org/html/2610.36077 (Table 1·4·8, §4.3, §7)
- 볼트 실측(2026-10-28): upvote 102 · 저자 20 · githubRepo null
