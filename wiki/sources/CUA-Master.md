---
title: "CUA-Master — 교육 영상에서 워크플로를 채굴해 과제를 합성하는 이중 재귀개선 CUA (27B · OSWorld Verified 80.2, 같은 크기 범용 Qwen-3.8-27B는 81.2)"
type: source
domain: ai-news
tags: [ai-news, computer-use, cua, osworld, data-flywheel, gui-cli-hybrid, open-weights]
created: 2026-11-03
updated: 2026-11-03
sources: [https://huggingface.co/papers/2611.03126]
reliability: medium
---

**HF**: published 2026-11-02 · upvote **40**(11-03 재조회 · 수집기 39) · Xinlei Yu 외 17인(**18명**) · HF 조직 표기 없음 · arXiv 2611.03126 · 코드 [xlyu0106/CUA-Master](https://github.com/xlyu0106/CUA-Master) **★77 · 라이선스 필드 없음**(GitHub API `license: null`) · 가중치 [yxl66666/CUAMaster-27B](https://huggingface.co/yxl66666/CUAMaster-27B) 공개(dl **16** · likes 5 · 카드 라이선스 미기재 · 11-03 실측) · 실행 0회

## 핵심 인사이트
> [!insight] 데이터 다양성 병목을 "실제 사람이 찍은 소프트웨어 교육 영상"으로 푼다
> 내부 루프에서는 YouTube·TikTok 교육 영상을 분류 체계 질의(README 기준 8도메인·36하위도메인·650+앱)로 수집한다. 자막 절과 프레임 변화를 교차시켜 과제 경계와 궤적을 복원하고, 이를 시드로 삼는다. 시드를 재사용 프리미티브로 추상화해 복잡도(K프리미티브×N앱)를 조절하며 검증 가능한 과제를 합성한다. 외부 루프에서는 모델 실패 분석이 다음 데이터 구축을 유도한다. 수집기는 VM 스냅샷-롤백으로 실패 지점부터 재시도한다. 학습은 Qwen-3.5-27B에서 SFT 3회(63K→38K→14K 누적 약 115K) 후 RL(약 12K 과제)이다.
>
> 가장 큰 효과는 **GUI+CLI 혼합 행동공간**에서 나왔다. WeaveBench에서 GUI 전용 **6.6** · CLI 전용 11.5 → 혼합 **43.9**, ALE에서 GUI 전용 5.9 → 혼합 **25.0**이다(§3.3).

> [!warning] "approaching larger models"의 실제 위치 — 본문 Table 1 (모든 기준선 동일 프로토콜 재평가)
> | 모델 | OSWorld Verified† | OSWorld 2.0† | WeaveBench‡ | ALE‡ |
> |---|---|---|---|---|
> | Qwen-3.5-27B (베이스) | 54.6 | 0.8 | 13.5 | 1.3 |
> | **Qwen-3.8-27B (같은 크기 범용)** | **81.2** | 36.5 | 14.1 | 19.1 |
> | UI-Mate-27B (같은 크기 전문) | 77.6 | 24.0 | 18.3 | 13.2 |
> | Qwen-CUA-397B-A17B | 84.0 | 43.6 | 35.1 | 21.1 |
> | Kimi-K3-2.8T-A104B | 84.2 | 55.9 | 43.2 | 25.0 |
> | GPT-5.6-Sol* | 83.6 | 59.0 | 50.6 | 26.3 |
> | Claude-Opus-5* | **86.3** | **64.2** | **55.7** | **28.3** |
> | **CUA-Master-27B** | 80.2 | 36.9 | 43.9 | 25.0 |
>
> - 수집기 수치(80.2/36.9/43.9/25.0 · UI-Mate 대비 +2.6/+12.9/+25.6/+11.8 · Qwen-CUA 대비 GUI −3.8/−6.7, 혼합 우위)는 **전부 맞다**.
> - 🔴 **수집기 누락**: 같은 27B 범용 모델 **Qwen-3.8-27B가 OSWorld Verified에서 81.2로 CUA-Master(80.2)보다 높다**. OSWorld 2.0은 36.5 vs 36.9로 동률권이다. 저자도 "GUI-only에서 Qwen-3.8-27B와 comparable"이라고 썼다. 즉 GUI 전용 이득은 *더 새로운 베이스 세대*로도 얻을 수 있는 수준이다. 고유한 이득은 **혼합 벤치 2종**(WeaveBench +29.8, ALE +5.9 vs Qwen-3.8-27B)에 있다.
> - ALE "GPT-5.6-Sol·Claude-Opus-5 다음"은 **Kimi-K3·Qwen-3.8-Max와 25.0 동률**을 평균점수로 가른 결과다(저자 명시).
> - 폐쇄 모델 Claude-Opus-5가 **4개 벤치 전부 1위**다.
> - 교차 플랫폼(Table 2): WindowsAgentArena **56.2 < UI-Mate 63.2** · MacAgentBench **59.9 < Qwen-CUA 65.3** · MacOSWorld 43.0만 1위다. 초록의 "strong cross-platform generalization"은 3개 중 1개에서만 1위라는 뜻이다.
> - 추론 온도 1, **단일 실행 여부·분산은 본문에서 확인되지 않음**(grep `runs|variance|std` 관련 결과 없음). → [[유의성-자기제한]]

## 도메인별 추출 (ai-news)
- **신뢰도**: 논문 + 코드(★77, 라이선스 없음) + 27B 가중치 공개. 기준선을 같은 환경·행동 인터페이스로 **재평가**했다고 명시한 점은 [[비매칭-비교]] 기준에서 좋은 쪽이다. 다만 Kimi-K2.6·Seed 등 일부 셀은 "–"(미평가)다.
- **즉시 활용**: 부분 YES. 데이터 파이프라인(영상→시드 궤적 복원)은 README의 CLI로 공개돼 있어 *데이터 합성 레시피*로 읽을 가치가 있다. 단, 학습 인프라는 H200 16노드(128장)이고, 수집기에는 대규모 VM 오케스트레이션이 필요하다(한계 절 명시). 라이선스 미기재라 재사용 전에 확인해야 한다.
- **6개월 영향력**: "GUI만으로는 장기 과제가 안 된다"는 결론이 [[WeaveBench]] 위에서 다시 확인됐다(GUI 6.6 vs 혼합 43.9). 데스크톱 에이전트는 CLI/코드 실행을 1급 수단으로 가져가야 한다. → [[OpenGCUA]](코드 실행 1급 수단)와 같은 방향이고, 접근성 트리 기반 [[agent-desktop]]과는 보완 관계다.
- **대체 관계**: [[UI-Mate]]·[[Qwen-UI-Agent]]·[[trycua-cua]] 계열 오픈 CUA의 상위 대안이다. 하지만 같은 크기 최신 범용 모델과 GUI 성능이 같다면, 전문 모델을 따로 운용할 이유는 혼합 과제에서만 남는다.
- **허와 실**: 저자 한계 절에 따르면 합성 데이터 품질의 상한은 **어노테이터 모델의 능력**에 달려 있다(강한 어노테이터일수록 이득이 크다). 즉 "재귀개선"의 일부는 강한 외부 모델의 증류다. → [[RSI-프레이밍]]
- **효율**: OSWorld Verified 평균 8분 · OSWorld 2.0에서 Qwen-3.8-27B 대비 런타임 −24%(저자). 런타임은 배포 구성과 API 속도의 영향을 받는다(저자 주석).

## 관련 페이지
- [[WeaveBench]] · [[UI-Mate]] · [[Qwen-UI-Agent]] · [[OpenGCUA]] · [[trycua-cua]] · [[agent-desktop]]
- [[Qwen]] · [[OpenAI]] · [[Anthropic]]
- [[RSI-프레이밍]] · [[비매칭-비교]] · [[한정어-탈락]] (approaching ≠ 넘어섬) · [[표-부분인용]] · [[벤치마크-외부축]]
- [[CoworkOS]] · [[uni-robot-agent]] (같은 날 · "하네스/행동공간이 모델 크기를 상쇄" 계열)

## 원본
- 출처: https://huggingface.co/papers/2611.03126 · https://arxiv.org/html/2611.03126
- 확인 범위: HF `api/papers/2611.03126` · arXiv HTML 본문 Table 1·2, §3.1~3.3, 부록 E 한계 · GitHub API·README 상단 · HF `api/models/yxl66666/CUAMaster-27B` · 🔴 Table 3(난이도별 롤아웃 성공률)·Figure 9 반복별 수치·부록 도메인 표 미확인 · 코드 실행 0회
- 신뢰도: ⭐⭐ (코드·가중치 공개 · 재평가 기준선 · 라이선스 미기재 · 단일 실행 여부 불명)
