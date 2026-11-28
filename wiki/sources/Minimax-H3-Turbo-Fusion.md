---
title: "Minimax-H3-Turbo-Fusion — LoRA 3개를 가중 합성한 비공식 터보 퓨전 (lightx2v · MiniMax-H3 파생)"
type: source
domain: video-saas
tags: [video-saas, model, lora, fusion, minimax-h3, ref2va, turbo, lightx2v, unofficial]
created: 2026-11-28
updated: 2026-11-28
sources: [https://huggingface.co/lightx2v/Minimax-H3-Turbo-Fusion]
reliability: low
---

**모델**: https://huggingface.co/lightx2v/Minimax-H3-Turbo-Fusion · **다운로드 22,131**(볼트 API 11-28 · 생성 2026-11-24) · 베이스 [[MiniMax-H3]](baseModels relation='adapter' — 볼트 API 확인) · [[lightx2v]] · [[MiniMax]]

## 핵심 인사이트
> [!insight] 어댑터 스택이 아니라 가중 합성 1개로 병합하는 방식이 커뮤니티 표준이 되어가고 있다
> [[Minimax-h3-Turbo-lightx2v]] 의 후속. 3개 LoRA를 스택하는 대신 **단일 퓨전으로 병합**: LightX2V turbo(×1.0) + Pika Ref2VA Flex(×0.4) + Larry Turbo v4 EMA(×0.4). MiniMax-H3 **Ref2VA** 과제용, 4/8스텝 양쪽 지원. 전작이 FL2V 8스텝이었던 것과 달리 레퍼런스→영상 계열로 확장.

> [!warning] 정량 벤치 0개 — 스펙트럼 에너지 98.41%는 "지각 품질 점수가 아니다"라고 카드가 직접 경고([[자기제한-명시]])
> Lite r32 기준 스펙트럼 에너지 98.41%/97.80%만 제시하는데, 카드 스스로 **"지각 품질 점수가 아님"** 을 명시. 정성 비교만 존재하는 **비공식 커뮤니티 퓨전** — 도입 판단은 자체 테스트에만 의존 가능. [[ProxyGenBench]] 가 보여준 "프록시 지표 ≠ 최종 품질"이 정확히 적용되는 사례.

## 도메인별 추출 (video-saas)
- **기능 벤치마킹**: 가중치 합성 퓨전(x1.0/x0.4/x0.4 공개) — 자체 워크플로우에서 LoRA 조합 실험 시 "스택 대신 사전 병합" 옵션으로 재현 가능.
- **크리에이터 인사이트**: Ref2VA 4스텝 → 로컬에서 레퍼런스 변환을 빠르게 돌리는 용도. 단 품질 보장 없음 — A/B 테스트 필수.
- **경쟁 우위 빈틈**: [[MiniMax-H3]] 계열의 공식 터보/퓨전 라인이 없는 빈틈을 커뮤니티가 채우는 중 — [[ProxyGenBench]] 에서 H3가 Joint 최하위였음을 감안하면 파생 생태계의 품질 관리 리스크도 함께 커짐.
- **액션**: [[Minimax-h3-Turbo-Fusion]] 후속 실검 후보(정량 비교 시 사전 병합 vs 스택 비교) — 우선순위 낮음.

## 관련 페이지
- [[Minimax-h3-Turbo-lightx2v]] · [[MiniMax-H3]] · [[MiniMax]] · [[lightx2v]] · [[자기제한-명시]] · [[ProxyGenBench]] · [[video-saas]]

## 원본
- 출처: https://huggingface.co/lightx2v/Minimax-H3-Turbo-Fusion
- 확인 범위: HF API(볼트 11-28 — DL 22,131 · 생성일 · baseModels='adapter'→MiniMax-H3 일치) · 카드 내용(퓨전 구성 · 가중치 · 스펙트럼 에너지 · 면책 문구 — 수집기 11-28 판독 인용) · 실행 0
- 신뢰도: ⭐⭐ (메타 실측 · 정량 벤치 전무 · 비공식 커뮤니티물 · 면책은 성실)
