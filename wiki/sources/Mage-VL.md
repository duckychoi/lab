---
title: Mage-VL — 코덱 네이티브 스트리밍 멀티모달 파운데이션 모델(4B, 토큰 75%↓)
type: source
domain: ai-news
tags: [ai-news, multimodal, video-understanding, streaming, microsoft, codec, efficient]
created: 2026-07-29
updated: 2026-07-29
sources: []
reliability: medium
---

# Mage-VL (논문 2607.24904)

> [!insight] 핵심 인사이트
> [[Microsoft]] Mage 팀의 **4B 비전-언어 모델** — 영상 처리의 계산 비효율을 겨냥한 **코덱 네이티브 스트리밍 멀티모달**. 균일 프레임 샘플링 대신 **모션·잔차(residual) 신호 기반 코덱 네이티브 희소 패치 선택**으로 **약 75% 토큰 감소**를 유지 성능으로 달성. **이중 시스템 아키텍처** — 경량 게이트(System 1)가 영상 스트림을 감시하다 **이벤트 트리거 응답**, 완전 언어 디코더(System 2)가 상세 답변 생성. 자체 제작 **Mage-ViT 인코더**(이미지 5.6억·영상 프레임 1억으로 from-scratch 학습)로 공간추론·영상이해·스트리밍 상호작용에서 강한 결과 주장. [[Kimi-K3]] MoonViT-V2·[[Scaling-Native-Multimodal-Pretraining]]과 함께 **"네이티브 멀티모달 + 효율(토큰↓)"** 계보. 내 [[down-analysis]] 영상 분석의 토큰↔충실도 트레이드오프에 직접 참고.

> [!action] down-analysis·claude-video 토큰 전략 참고
> Mage-VL의 **"모션·잔차 기반 희소 패치 선택으로 토큰 75%↓"**와 **"이벤트 트리거 게이트(System 1)"**는 내 [[down-analysis]]·[[claude-video]](4모드 프레임 추출)의 핵심 과제와 동일 — **정보성 높은 프레임/패치만 선별**해 토큰을 아끼는 설계 아이디어로 차용.

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐⭐⭐ — 초록·기관([[Microsoft]] Mage 팀)·기여자(Senqiao Yang 외)·구체 수치(4B·75%↓·5.6억 이미지·1억 프레임) WebFetch 실확인. 단 미래형 ID·재현 전.
- **즉시 활용**: 개념 이식 — 소형(4B)이라 실배포 매력. 코덱 네이티브 희소 선택은 내 영상 분석 파이프라인의 프레임 선별 로직에 참고. 웨이트 공개 여부는 추가 확인 필요.
- **6개월 영향력**: 멀티모달이 "고비용 영상 토큰"에서 **코덱 신호 활용 효율화**로 이동. 스트리밍/실시간 영상 이해가 4B급으로 내려오는 신호.
- **대체 관계**: [[Kimi-K3]](2.8T 멀티모달)·[[Qwen-Image-Agent]] 대비 **경량·효율 스트리밍** 포지션. 영상이해 전용 소형 백본 후보.
- **허와 실**: 75% 토큰↓·강한 결과는 자체 발표 — 효율 방향은 설득력 있으나 절대 성능은 재현 전. 이중 시스템(게이트+디코더)은 지연·정확도 트레이드오프 실측 필요.
- **액션**: down-analysis에 "모션·잔차 기반 프레임 선별" 휴리스틱을 실험 → [[claude-video]] token-burner 대비 토큰 절감 재현성 스팟체크.

## 관련 페이지
- [[Microsoft]]
- [[Kimi-K3]]
- [[Scaling-Native-Multimodal-Pretraining]]
- [[down-analysis]]
- [[claude-video]]
- [[ai-news]]

## 원본
- 출처: https://huggingface.co/papers/2607.24904 (arXiv 2607.24904)
- 기관/기여자: Microsoft Mage 팀(Senqiao Yang·Kaichen Zhang·Zhaoyang Jia·Jinghao Guo·Yifei Shen·Xinjie Zhang 외)
- 업보트: 15 (HF 데일리 논문, raw 기재)
- 핵심(자체): 4B VLM·코덱 네이티브 희소 패치(모션/잔차)로 토큰 ~75%↓·이중 시스템(게이트 System1+디코더 System2)·Mage-ViT from-scratch(5.6억 이미지·1억 프레임)
- 신뢰도: ⭐⭐⭐ (초록·기관·기여자·수치 WebFetch 실확인, 미래형 ID·원문 재현 미검증 medium)
