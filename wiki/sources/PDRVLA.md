---
title: "PDRVLA — 비디오 월드모델을 추론 루프 밖으로 뺀 VLA. 시뮬 4벤치 1위지만 차이는 전부 1점 미만, 실로봇·지연 수치는 없다"
type: source
domain: ai-news
tags: [ai-news, hf-paper, VLA, world-model, distillation, physical-dynamics, robotics, simulation-only, slam-3dgs]
created: 2026-10-28
updated: 2026-10-28
sources: [https://huggingface.co/papers/2610.37381, https://arxiv.org/html/2610.37381]
reliability: low
---

# PDRVLA: A Vision-Language-Action Model with Physical Dynamics Representations

**HF**: https://huggingface.co/papers/2610.37381 · published **2026-10-27** · Hanqing Wang · Zhaotian Cai 외 **저자 15**(수집기 일치) · HF organization 미등록 · upvote **105**(🔴 수집기 101 → **+4 드리프트**, 수집 이후 증가)
**코드**: 없음(HF `githubRepo` null · 수집기 일치)
**신뢰도**: ⭐ low(코드·가중치 없음 · 시뮬 전용 · 차이가 작음)

> [!insight] 핵심 인사이트 — 월드모델은 학습 때만 쓰고 추론 때는 떼어낸다
> 4B VLM 백본에 경량 **Physical Dynamics Module**을 붙인다. 이 모듈은 vision-language 특징에서 **물리 토큰**을 뽑아 action expert(flow matching, 4 Euler step)를 조건화한다. 미래 **RGB·깊이·광류 특징을 직접 예측**하도록 학습하고, **동결된 사전학습 비디오 월드모델**이 보조 감독을 준다. *"The video world model and its output heads are used only during physical pretraining"* — 추론 루프에서는 영상을 생성하지 않는다.
> 데이터는 전부 공개 데이터다. 실로봇·UMI·시뮬 데이터를 human-to-robot 합성, subtask 주석(1.79B 프레임), ECoT 주석(2.56M 키프레임)으로 확장했다.
> ⇒ [[월드모델]]을 정책의 **표현 교사**로만 쓰는 노선이다. 온라인 생성형 WAM([[FRED]] · [[World-Action-Models-Survey]])과는 반대 방향이다.

> [!warning] 주의
> - 🧪 **4개 벤치 모두 시뮬레이션이다**(초록: *"Across four simulation benchmarks"*). 수집기도 이 점을 적었다(✅). 실로봇 성공률은 없다.
> - 📏 **1위 차이가 모두 1점 미만이다**(arXiv Table): LIBERO **99.3** vs Qwen-RobotManip 99.1(+0.2) · LIBERO-Plus **89.9** vs 89.0(+0.9) · RoboTwin 2.0 **93.6** vs LingBot-VLA 2.0/InternVLA-A1.5 93.2(+0.4) · SimplerEnv **81.5** vs InternVLA-A1.5 80.8(+0.7). 시드 수와 분산은 보지 못했다. 이 정도 차이는 시드 노이즈 안에 있을 수 있다 → [[천장-기준선]](LIBERO는 99%대에서 포화).
> - 📑 비교 행은 각 논문의 보고값을 인용한 것으로 보인다(같은 조건에서 재실행했는지 확인하지 못함) → [[비매칭-비교]].
> - ⏱️ "지연 없음"이 논문의 핵심 주장인데, **추론 지연(ms·Hz) 수치는 본문 검색에서 찾지 못했다**. 구조상 영상 생성이 없다는 정성적 논증뿐이다. 모듈 파라미터 수도 HTML 변환 과정에서 빠졌다(원문 PDF 확인 필요).
> - 수집기가 빠뜨린 것: **1위 차이가 1점 미만이라는 점**, 4B 백본, 비교가 보고값 인용이라는 점.

## 도메인별 추출 (ai-news · slam-3dgs 접점)
- **slam-3dgs 연결**: 미래 **깊이·광류** 특징을 예측하는 것은 SLAM의 단기 기하 예측과 같은 신호다. 로컬 VLA에 기하 사전지식을 넣는 경량 경로로 참고할 만하다 → [[리서치-휴머노이드-로봇-SLAMVLA로컬LLM-기반-제어-기술-2026년-최신-동향]].
- **실용성**: 코드가 공개되면 "월드모델 증류 모듈"을 기존 VLA에 덧붙이는 레시피로 쓸 수 있다. 지금은 재현할 수 없다.
- 비교 계보: [[TurboVLA]] · [[Qwen-VLA]] · [[Xiaomi-Robotics-VLA-Scaling]] · [[LaMem-VLA]] · [[VLA-Corrector]] · [[LaLa-World]]

## 관련 페이지
- [[VLA]] · [[월드모델]] · [[Diffusion-월드모델]] · [[임바디드-AI]] · [[천장-기준선]] · [[비매칭-비교]]
- [[Xiaomi]](비교 대상 Xiaomi-Robotics-0 LIBERO 98.7) · [[Qwen]](Qwen-VLA-Instruct·Qwen-RobotManip 비교 행)
- 같은 배치(10-28): [[Rollback]] · [[Hy-Nomas]] · [[ChronoReplay]] · [[The-Trinity]]
- [[ai-news]] · [[slam-3dgs]]

## 원본
- https://huggingface.co/papers/2610.37381 · https://arxiv.org/html/2610.37381 (주 결과표·LIBERO-Plus 세부표)
- 볼트 실측(2026-10-28): upvote 105 · 저자 15 · githubRepo null
