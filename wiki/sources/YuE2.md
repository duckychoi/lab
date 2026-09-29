---
title: "YuE2 — 악보를 먼저 쓰게 했더니 같은 체크포인트가 더 나아졌다 (49.3% vs 34.6%)"
type: source
domain: ai-news
tags: [ai-news, video-saas, hf-paper, 음악생성, symbolic-planning, MoT, AR-NAR, MERT2, 동일체크포인트-대조, 자기제한-명시]
created: 2026-09-29
updated: 2026-09-29
sources: []
reliability: high
---

# YuE2 — Unifying Symbolic and Audio Music Generation at Frontier Quality

> [!insight] 핵심 인사이트 — **"계획을 거치게 하면 좋아진다"를 같은 체크포인트로 증명했다**
> 초록 축자: *"In comparisons using **the same checkpoint**, experts prefer symbolic planning for overall quality and musicality, with **49.3% of overall preferences versus 34.6%** without planning."*
> 🎯 **이 대조 설계가 핵심이다.** 모델을 바꿔 비교하면 "더 큰 모델이 낫다"와 구분되지 않는다. **같은 가중치에서 악보 계획 경로만 껐다 켰다** 했기 때문에 **이득이 계획 자체에 귀속된다.** [[비매칭-비교]] 를 피한 드문 설계다.
> 📌 구조: 단일 **AR-NAR Mixture-of-Transformers(MoT)** 가 ① 읽을 수 있는 악보(멜로디·화성)를 쓰고 → ② 시맨틱 음악 토큰으로 확장 → ③ 풀송 오디오로 실현. **[[암묵을-명시로]] 의 음악판** — 오디오 모델이 암묵적으로 두던 작곡을 문자로 꺼냈다.

> [!insight] 명시된 악보가 **부작용으로 편집 가능성을 만든다**
> 초록 축자: *"The same checkpoint **follows score edits while largely preserving unedited musical content**"* · *"its readable score also enables **agentic music editing**, with external language models translating user feedback into revisions of the composition."*
> 🎯 **성능 향상은 부차적이고, 진짜 결과물은 인터페이스다.** 악보가 문자로 존재하니 **외부 LLM이 사용자 피드백을 악보 수정으로 번역**할 수 있다 — 오디오 생성물에는 불가능한 조작이다. [[검사가능성-공사]] 의 생성모델 사례: **검사 가능하게 만들었더니 편집도 가능해졌다.**
> 추가: *"generates **zero-shot covers** without cover-specific training"*.

> [!note] 수치 — 벤치 3종
> - **WildSongBench**: SongBench Global Avg **6.73**, *"exceeding all evaluated public baselines"* · best-of-8 시 **6.96**(*"the highest observed mean among all evaluated systems"*)
> - **MERT2**(음악 표현학습 보조 모델): *"surpassing previous best results on **14 of 15 MARBLE metrics**"*
> - **SheetSage2**(리드시트 전사): *"leads **12 of 15** benchmark-metric pairs"* — 🎯 **수집기가 누락한 항목**

> [!warning] 🟡 Suno 상대 주장은 **등급이 나뉘어 있다 — 뭉뚱그리면 안 된다**
> 초록 축자: *"favoring **best-of-8 over Suno v4.5** and yielding **nearly balanced preferences against Suno v5**."*
> 📌 **v4.5 에는 이기고, v5 와는 비긴다.** 그리고 이긴 쪽 조건은 **best-of-8**(8개 뽑아 고르기)이다 — **단일 생성 기준의 승리가 아니다.** 수집기 요약(*"Suno v5 상대로는 거의 대등"*)은 정확했으나, **"v4.5 우위"에 붙은 best-of-8 조건**은 인용 시 반드시 따라가야 한다 → [[한정어-탈락]] 위험 지점.
> 🔴 *"frontier quality"*(제목)는 **이 비김을 근거로 한 자칭**이다. 제3자 재현 없음.

## 도메인별 추출 (ai-news / video-saas 교차)

- **신뢰도**: HF 업보트 **56**(볼트 09-29 실측 · 수집기 56 → **드리프트 0**) · arXiv 2609.33757 · 게재 2026-09-27. 초록 무손상.
- **즉시 활용**: 🟡 **간접.** 볼트 [[video-saas]] 축에서 **영상용 BGM 자동 생성**은 실수요다. 🔴 단 **가중치 공개 여부가 초록에 없다** — `m-a-p` 조직의 기존 [[YuE2-3B]] 모델이 볼트에 이미 있으므로 **그쪽이 이 논문의 공개 구현체인지 대조가 필요**하다(actionable 등록).
- **6개월 영향력**: **"생성 전에 계획을 문자로 쓰게 한다"가 음악에서도 통한다**는 사례 추가. 볼트의 [[암묵을-명시로]] 축이 **LLM 추론 → 로봇 정책([[HexaAnything]], 같은 배치) → 음악** 3개 영역으로 확장됐다.
- **대체 관계**: Suno 를 대체하지 않는다(v5 와 비김). **오픈 진영 내에서 기존 공개 베이스라인을 대체**한다는 주장.
- **허와 실**: 걷어내면 — **① 계획 경로의 이득은 동일 체크포인트로 확실히 입증 ② 절대 품질 우위는 오픈 진영 한정 ③ 상용 최상위와는 동급 주장이며 그것도 best-of-8 보정 포함.**

> [!action] 당장 할 것
> [[YuE2-3B]](볼트 09-13 등록, `m-a-p/YuE2-3B`)와 **이 논문의 관계 확정** — 같은 계보인지, 공개 체크포인트가 논문 모델인지. 두 페이지가 지금 **연결 없이 따로 존재**한다. 우선순위 중간.

## 관련 페이지
- [[YuE2-3B]] — 🔗 **동명 모델 페이지(별도 URL). 계보 대조 필요**
- [[암묵을-명시로]] · [[검사가능성-공사]] · [[비매칭-비교]] · [[한정어-탈락]] · [[자기제한-명시]]
- [[AI-영상-생성-2026]] · [[video-saas]] · [[ai-news]]
- 같은 배치: [[DN-MOPD]] · [[TraceDance]] · [[HexaAnything]] · [[LTX-2.5]]

## 원본
- 출처: https://huggingface.co/papers/2609.33757 · arXiv **2609.33757**
- 실측(2026-09-29 09:08 UTC · HF papers API): 업보트 **56**(드리프트 0) · 게재 **2026-09-27** · 초록 전문 정상
- 수집기 대조: 인용 수치 **49.3 / 34.6 / 6.73 / 6.96 / MARBLE 14-of-15 전부 축자 일치**. 🎯 수집기 누락 2건 — **SheetSage2 12-of-15** · **Suno v4.5 우위의 best-of-8 조건**
- 확인 범위: 초록 전문. 🔴 본문·오디오 샘플 **미청취** · 가중치 공개 여부 미확인 · 🔴 미실행
- 신뢰도: ⭐⭐⭐⭐ **high** — 동일 체크포인트 대조 설계 + API 실검증. (청취 검증 부재 · 제3자 재현 없음)
