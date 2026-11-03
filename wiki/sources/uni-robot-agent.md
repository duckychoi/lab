---
title: "uni-robot-agent — 오픈웨이트 모델로 로봇을 조작하는 통합 하네스 (같은 하네스에선 GPT-6 Astra 51.90 vs Qwen 31.39)"
type: source
domain: slam-3dgs
tags: [slam-3dgs, robotics, robot-use-agent, harness, open-weights, robodojo, camera-calibration, triangulation]
created: 2026-11-03
updated: 2026-11-03
sources: [https://huggingface.co/papers/2611.01560]
reliability: medium
---

**HF**: published 2026-11-01 · upvote **31** · 제목 *"Democratizing Robot-Use Agents: A Unified Harness with Open Models"* · Jiarui Yuan 외 27인(**28명** · UC Berkeley 등) · HF 조직 표기 없음 · arXiv 2611.01560 · 코드 [Open-RUA/uni-robot-agent](https://github.com/Open-RUA/uni-robot-agent) **★31 · MIT** · 레포 생성 2026-11-02 (GitHub API 11-03 실측 · HF 캐시 7) · 실행 0회

## 핵심 인사이트
> [!insight] 로봇 조작 능력은 '로봇 전용 능력'이 아니라 일반 능력 4개의 합이다 — 그리고 하네스가 그걸 꺼낸다
> 하네스는 카메라 캘리브레이션·로봇 설명·피드백이 있는 도구 인터페이스(삼각측량 도구가 재투영 오차가 큰 결과를 거부하는 식)를 제공한다. 통신 실패 시 같은 물리 행동이 반복되지 않도록 요청 ID와 실행 상태도 기록한다. 이 조건에서 오픈웨이트 모델이 **깊이 없이** 조작한다. 실패 분석으로 저자가 꼽은 네 능력은 ①일반 시각 이해 ②다시점 대응점 지정(공간 그라운딩) ③위치·자세 계산 코드 ④파지 자세 같은 임바디드 추론이다. MMMU-Pro·ERQA·ScreenSpot-Pro·LiveCodeBench와 RoboDojo 점수 사이에 양의 상관이 있었다(6개 모델 기준, n이 작다).
> - 깊이 제거: Qwen 35.89→31.39(87.5% 유지). **카메라 파라미터까지 제거하면 Qwen 9.13**으로 급락한다. 핵심 입력은 깊이가 아니라 **캘리브레이션**이다.
> - 스킬 라이브러리 제거: 31.39→**30.31**(96.6% 유지). 성능이 과제별 사전지식에서 나오지 않았다는 저자 측 반증이다.

> [!warning] "오픈모델이 GPT-6 Astra를 넘었다"는 하네스가 다른 비교다 (본문 Table 1, RoboDojo 42과제 · SR/Score)
> | 모델 | 하네스 | Avg SR / Score |
> |---|---|---|
> | GPT-6 Astra | RoboProbe (**공개 결과 인용 · 재실행 아님**) | 22.48 / 28.97 |
> | **GPT-6 Astra** | **uni-robot-agent** | **46.67 / 51.90** |
> | GPT-6 Astra | uni-robot-agent + depth | 52.36 / 56.76 |
> | Qwen3.8-Flash-Next | RoboProbe | 0.83 / **1.90** |
> | Qwen3.8-Flash-Next | RPent | 4.31 / 7.75 |
> | Qwen3.8-Flash-Next | GAP (Hybrid, π0.5 포함) | 16.11 / 21.01 |
> | **Qwen3.8-Flash-Next** | **uni-robot-agent** | **25.00 / 31.39** |
> | DeepSeek-V4.1-Flash | uni-robot-agent | 21.39 / 27.11 |
> | Xiaomi-Robotics-1 (VLA 최고) | – | 13.93 / 20.07 |
>
> - 수집기 지적(같은 하네스에서는 Astra 51.90 ≫ Qwen 31.39)은 **맞다**.
> - 🔴 **수집기 누락 ①**: 같은 Qwen 모델이 RoboProbe에서 **1.90**, uni-robot-agent에서 **31.39**다. 하네스만 바꿔서 **약 16배** 차이가 난다. "하네스 효과 > 모델 격차"의 가장 직접적인 증거는 Astra 비교가 아니라 이 행이다. → [[하네스-설계-축]]
> - 🔴 **누락 ② 추론 강도 불일치**(부록 A): Astra **medium**, Qwen **xhigh**, DeepSeek **max**. 같은 하네스 안의 모델 비교도 추론 예산이 같지 않다. → [[비매칭-비교]]
> - 🔴 **누락 ③ 문서 내 값 충돌**: §5.1은 깊이 제거 시 "Astra 55.83 → 55.04 (98.6% 유지)"라고 쓴다. 그런데 Table 1은 **56.76 → 51.90(91.4%)**다. Qwen 수치(35.89→31.39)는 표와 일치한다. 어느 쪽이 맞는지 본문만으로는 판정할 수 없다. → [[문서내-값충돌]]
> - 장기(Long-Hor.) 과제에서는 Qwen(6.25/23.75)·DeepSeek이 VLA인 Xiaomi-Robotics-1(23.67/38.39)·OpenWAM-α보다 **낮다**(저자 명시). 정밀(Prec.) 과제에서도 Qwen 2.08% SR로 VLA들보다 낮다.
> - uni-robot-agent 설정은 **과제 검증기 피드백을 제외**했다(캡션 명시). 이 점은 공정성 측면에서 좋다.

> [!warning] 실환경 19과제 — 입력 조건이 다르다 (Table 2, 듀얼암 ARX · 5차원×20점)
> 총점: π0.5(과제당 10시간 데모로 **파인튜닝**) **47.75** · Dream-1(제로샷) **35.50** · **GPT-6 Astra 75.50** · **Qwen3.8-Flash-Next 49.50**. 저자 표현은 "matches fine-tuned π0.5"다. 그런데 본문에 "**our agents additionally receive depth** … while π0.5 and Dream-1 use RGB only"라고 명시돼 있다. 시뮬레이션 주 결과(깊이 없음)와 달리 **실환경 에이전트는 깊이를 받았다**. 수집기는 이 비대칭을 적지 않았다.
> - 비용: 에피소드당 Qwen **$1.09** vs Astra **$21.29**(약 20배). 점수 25에 도달하는 데 Astra는 7.4M 토큰·42.6분, Qwen은 23.5M·95.5분이 걸렸다. **싸지만 느리다.**

## 도메인별 추출 (slam-3dgs)
- **현재 SOTA**: RoboDojo에서 GPT-6 Astra + 이 하네스가 SR 46.67 / Score 51.90(깊이 없음)이다. 오픈웨이트 최고는 Qwen3.8-Flash-Next 31.39다. 코드는 MIT로 공개돼 있다.
- **실시간 가능성**: 없음. 점수 25까지 수십 분이 걸리는 *계획형* 조작이다. 실시간 제어는 여전히 [[VLA]] 영역이다.
- **카메라 파이프라인**: 시뮬레이션은 Isaac Sim 다시점 RGB + **카메라 내·외부 파라미터**다. 모델이 다시점 대응점을 찍으면 삼각측량 도구가 3D 좌표를 돌려주고, 재투영 오차가 크면 거부한다. 실환경은 RealSense D405 3대(헤드 1 + 손목 2)다. 캘리브레이션 없이 RGB만 주면 Qwen 9.13으로 무너진다. **SLAM/캘리브레이션 품질이 그대로 에이전트 성능 상한이 된다**는 뜻이다.
- **응용 가능성**: 다시점 대응점 지정 실패율이 성능과 음의 상관을 보였다. 최고 모델(GPT-6.1 Sol)도 31.5%가 거부됐다. "LLM이 찍은 점 → 기하 검증 도구" 구조는 카메라 2대 이상의 저가 로봇 셋업에 바로 옮길 수 있는 패턴이다.
- **필수 레퍼런스**: [[RoboDojo]] · RoboProbe · GAP(GPT-as-Policy) · π0.5.

## 관련 페이지
- [[RoboDojo]] · [[RobotUse]] · [[VLA]] · [[임바디드-AI]] · [[월드모델]] · [[Xiaomi-Robotics-U0]] · [[HiFOR]]
- [[Qwen3.8-Flash-Next]] · [[DeepSeek-V4.1-Flash]] · [[OpenAI]] · [[Qwen]] · [[DeepSeek]]
- [[하네스-설계-축]] · [[비매칭-비교]] · [[문서내-값충돌]] · [[한정어-탈락]] · [[유의성-자기제한]]
- [[CUA-Master]] · [[CoworkOS]] (같은 날 하네스 3건)

## 원본
- 출처: https://huggingface.co/papers/2611.01560 · https://arxiv.org/html/2611.01560
- 확인 범위: HF `api/papers/2611.01560` · arXiv HTML 본문 Table 1·2, §3~§6, 부록 A · GitHub API(메타·루트 목록) · 🔴 실환경 과제별 시행 횟수(부록 B Table 4)·Figure 9 원값 미확인 → §5.1과 Table 1의 Astra 값 충돌은 미해결 · 코드 실행 0회
- 신뢰도: ⭐⭐ (MIT 코드 ★31 · 하네스 대조 행이 강한 증거 · 추론 강도 불일치·값 충돌·실환경 입력 비대칭)
