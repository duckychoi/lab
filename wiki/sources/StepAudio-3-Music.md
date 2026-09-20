---
title: "StepAudio 3 Music — ABC 악보로 먼저 편곡 계획을 쓰고 음악을 만든다"
type: source
domain: ai-news
tags: [ai-news, hf-paper, music-generation, audio, tokenizer, dit, moe, backlog, 계획-먼저]
created: 2026-09-20
updated: 2026-09-20
sources: []
reliability: medium
---

# StepAudio 3 Music Technical Report

> [!insight] 🎯 핵심 인사이트 — **생성 전에 "악보"를 쓰게 만든다**
> MoE 자기회귀 모델이 음악 토큰을 예측하기 **전에 ABC 표기법으로 중간 편곡 계획(ABC-CoT)** 을 먼저 만든다. 초록 원문: *"...uses ABC notation to produce an intermediate arrangement plan (ABC-CoT) before predicting music tokens, **making harmony, rhythm, and melodic structure part of the generation context**."*
> 🎯 **화성·리듬·선율 구조가 "출력의 성질"이 아니라 "입력 컨텍스트"가 된다.** 이건 텍스트 쪽 CoT의 음악 이식이 아니라 **도메인 고유 표기법을 중간 언어로 쓴 것**이고, ABC는 사람이 읽고 고칠 수 있는 포맷이다 → **개입 지점이 생긴다.**
> 구조: **50Hz · 65,536엔트리 단일 코드북** 토크나이저(의미 기반 자기지도 + 멀티태스크 학습) → **flow-matching DiT** 가 연속 VAE 잠재를 예측 → VAE 디코더가 **48kHz** 오디오로. 최대 **5분 30초**, 드라이 보컬 반주 생성·커버곡 합성 지원. 마무리는 **DPO**.
> ✅ **설계 선택에 근거가 있다**: *"guided by **comparisons of** single-codebook VQ, Semantic and Acoustic RVQ, and different DiT configurations"* — 단일 코드북을 **비교 끝에** 골랐다고 적었다.

> [!warning] ⚠️ "최고"의 범위 — 수집기가 뗀 한정어 하나
> 초록 원문: *"achieves the highest AudioBox Content Enjoyment, Content Usefulness, and Production Quality scores and the highest MuQ-MuLan similarity **among the evaluated systems**, with **competitive** SongBench results."*
> ✅ 수집기는 *"competitive"* 를 **보존**했다(6배치 연속 한정어 보존 기록 유지).
> 🔴 그러나 ***"among the evaluated systems"* 는 떨어졌다.** *"비교 시스템 중 최고"* 로 옮겨 실질은 맞지만, **평가 대상 목록을 저자가 정했다**는 점이 흐려진다. 🎯 볼트가 [[m-a-p]] 에서 기록한 것과 **같은 형태의 위험**이다(*"자기 모델을 자기 벤치로 잰다"*).

> [!note] ✅ 다만 [[m-a-p]] 와 결정적으로 다르다 — **외부 리더보드를 들고 왔다**
> *"On the **preliminary** Artificial Analysis Music Arena Vocals leaderboard, it obtains a **Quality Elo of 1105, behind only Suno V5.5 and Mureka** and ahead of Suno V5, MiniMax models, and other systems."*
> ✅ **제3자 아레나 · 3위 · 자기가 진 상대를 이름으로 적었다.** [[m-a-p]] 는 *"Suno만 비교군으로 지목하고 실제 2위 Mureka 9는 표 안에만 뒀다"*([[한정어-탈락]] 기록)인데, **여기는 Suno V5.5와 Mureka를 초록 본문에 직접 쓴다.**
> ✅ *"**preliminary**"* 한정어도 저자가 달았고 수집기가 보존했다.
> 🎯 **그리고 Mureka 가 두 독립 논문에서 상위에 등장했다** — [[YuE2-3B]] 표 안 2위, 여기 아레나 2위. **볼트가 페이지를 갖고 있지 않은 이름이 두 번째로 상위에 나왔다** → [[mem0]] 과 같은 **본체 누락**의 초기 징후일 수 있다.
> 🎯 *"ahead of ... **MiniMax models**"* — 볼트 [[MiniMax]] · [[MiniMax-H3]] 와 연결. 같은 배치의 [[FastVideo]] 가 MiniMax-H3 를 증류하고 있다.

> [!note] 📌 볼트 실측 (2026-09-20)
> 업보트 **102**(수집기 101 · 볼트 09-19 기록 **86**) · 저자 **13**(배치 최다) · **githubRepo: None**.
> 🔴 게시일 `publishedAt` **2026-09-11** / `submittedOnDailyAt` **2026-09-16**(5일 차) — 수집기 *"게시 09-16"* 은 데일리 등재일 → [[게시일-이중화]].
> `backlog` 태그 — 09-19 볼트 판정 (a)의 **배치당 2건** 중 두 번째. ✅ 규칙 준수. 업보트 **86 → 101 → 102** 로 볼트 기록값과 나란히 적힌 것도 ✅.
> 🎯 저자 **13인**은 볼트 09-19 구분(기업형 60·54 vs 연구형 6~14)에서 **연구형 상단**이다. 다만 StepAudio 계열은 이미 볼트에 [[StepAudio-3-Realtime]]·[[StepAudio-2.5]] 가 있는 **연속 출하 조직**이다 — **저자 수만으로는 연속성이 안 잡힌다.**

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐⭐ — 🔴 **코드·가중치·데모 페이지 외 공개 0**(githubRepo None, 데모는 `stepaudiollm.github.io`). ✅ 외부 아레나 Elo 1105는 **검증 표면**이지만 *preliminary* 다.
- **즉시 활용**: 🔴 **NO — 받을 것이 없다.** ✅ **차용 가능한 설계 1개**: **중간 계획을 사람이 읽는 표기법으로 내보내기.** 볼트 `/reat-*` 영상 파이프라인에서 **장면 계획을 사람이 고칠 수 있는 중간 포맷으로 빼는 것**과 정확히 같은 발상이다(Scene DSL ↔ ABC-CoT).
- **6개월 영향력**: 🎯 **"생성 모델에 계획 단계를 넣는다"가 음악·영상에서 동시에 나오고 있다.** 09-18 [[하네스-설계-축]] 이 *"결론이 대체로 빼라다"*(계획=정확도 불변)라고 적었는데 — **텍스트 에이전트에서는 계획이 무용했고, 생성 도메인에서는 계획이 구조를 준다.** 🔴 **두 결론이 충돌하는 것처럼 보이지만 과제가 다르다**(정확도 vs 구조적 일관성). 성급히 하나로 묶지 않는다.
- **대체 관계**: [[YuE2-3B]]([[m-a-p]]·CC BY-NC) 와 같은 칸. 🔴 **단 YuE2는 가중치가 있고 이건 없다** — 실사용 가능성은 YuE2 쪽이 높다.
- **허와 실**: 🎯 **"최고"는 저자가 고른 비교군 안에서, "3위"는 외부 아레나에서.** 두 수치가 같은 초록에 있고 **서로 다른 이야기를 한다** — 정직한 배치다. 걷어낼 마케팅은 오히려 적다.
- **액션**: **읽기 + 1개 이식 검토.** ABC-CoT 발상을 `/reat-scene` 중간 산출물 설계에 적용할지 판단.

> [!question] 미해결 질문
> 1. **5분 30초 생성의 계산 비용** — 초록에 없다.
> 2. **ABC-CoT 제거 시 손실(ablation)** 수치 — 본문에 있을 가능성이 높으나 **미열람**.
> 3. **Mureka 의 정체** — 두 논문에서 상위에 나왔는데 볼트에 페이지가 없다.

## 관련 페이지
- [[StepAudio-3-Realtime]]
- [[StepAudio-2.5]]
- [[YuE2-3B]]
- [[m-a-p]]
- [[MiniMax]]
- [[한정어-탈락]]
- [[게시일-이중화]]
- [[하네스-설계-축]]
- [[ai-news]]

## 원본
- 출처: https://huggingface.co/papers/2609.16034 · https://arxiv.org/abs/2609.16034 · 데모 https://stepaudiollm.github.io/step-audio-3-music
- 볼트 실측(2026-09-20, HF papers API): 업보트 **102**(수집기 101 · 볼트 09-19 **86**) · 저자 **13** · **githubRepo: None** · `publishedAt` **2026-09-11** / `submittedOnDailyAt` **2026-09-16**(5일 차)
- 수치 출처: 초록 원문 — 50Hz · 65,536 단일 코드북 · 48kHz · 5분 30초 · Elo **1105** · Suno V5.5·Mureka 뒤 3위 **전건 대조 일치**
- raw 대비: 볼트 추가 = 🔴 ***"among the evaluated systems"* 한정어 탈락 지적** · ✅ **[[m-a-p]] 대비 외부 아레나 사용이라는 차이를 명시** · 🎯 **Mureka 2회 상위 등장 = 볼트 미보유 이름** · **설계 선택이 비교에 근거함(단일 코드북)** · 🔴 **게시일 5일 차**
- 신뢰도: ⭐⭐ (초록 전건 일치 · 외부 아레나 존재 · 한정어 저자 명시 / **공개 아티팩트 0 · 아레나는 preliminary**)
