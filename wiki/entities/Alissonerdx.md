---
title: "Alissonerdx — 누적 100만 다운로드 얼굴교체 LoRA 제공자"
type: entity
domain: video-saas
tags: [entity, huggingface, lora, face-swap, qwen-image, flux, ltx-2]
created: 2026-10-11
updated: 2026-10-11
sources: [BFS-Best-Face-Swap.md]
reliability: low
---

# Alissonerdx

**HuggingFace**: https://huggingface.co/Alissonerdx
**대표 산출물**: [[BFS-Best-Face-Swap]] — dl30 **253,548** · **dlAll 1,007,517** · ♥**1,365** · trendingScore 148 · MIT(볼트 API 실측 2026-10-11)

> [!insight] 🎯 특징 — 모델이 아니라 "호환 지도"를 축적하는 제공자
> base_model **9종**(Qwen-Image-2.1 · Qwen-Image-Edit 2509/2511 · FLUX.2 Klein 6변종 · Krea-2-Raw)에 걸쳐 **가중치 20개 이상**(head v1~v5 · body swap · 실험 LTX-2 ic_lora 3종)을 올린다.
> 🎯 **즉 실제 자산은 LoRA 파일이 아니라 "어느 베이스에 어느 LoRA 가 붙는가"의 지도다.** ⚖️ **그런데 그 지도가 자연어 서술로만 있다.**
> 🔴 **그 결과 같은 레포 안에서 호출 계약이 역전된다** — 카드 명시: *"several BFS head releases intentionally use body first and reference face second"* ⇒ [[배포출처-봉인]] 인접 사례.
> 🎯 **누적 100만 다운로드(dlAll 1,007,517)는 금일 배치 최대 누적치**이고 `dl30` 의 **3.97배**다 ⇒ **오래 운영해 온 제공자**다 → [[지표-창길이]].

> [!insight] ⚖️ 고지 측면은 정방향이다
> 카드가 ① *"예시와 워크플로는 데모이고 모든 이미지에서 동일 결과를 보장하지 않는다"* ② **동의 없는 공인·실존 인물 사용 금지**를 명시한다.
> ⇒ 🎯 **얼굴 교체 도구에서 두 고지를 모두 적은 것은 드물다.** 📌 **단 문구이고 기술적 제약이 아니다** — 실효는 사용자에게 달려 있다. ⚖️ **볼트는 생성 캐릭터 한정으로만 다룬다.**

> [!warning] 🔴 미확인
> 제공자 실체(개인/팀) · 국적 · 다른 저장소 · 수익 모델 **전부 미조회.** HF 프로필 **미열람.**
> 🔴 **정량 수치 0건** — 품질 비교·버전 선택 근거가 없다. head v1~v5 중 **권장 버전 미확인.**
> 🔴 **버전별 입력 순서 표 미확보**(*"일부가 역전"* 만 알고 어느 버전인지 모른다) = 본 엔티티 최대 공백.

## 관련 페이지
- [[BFS-Best-Face-Swap]] — 주 저장소
- [[배포출처-봉인]] — 🆕 한 레포 안의 계약 역전
- [[지표-창길이]] — dlAll 이 dl30 의 3.97배
- [[숨김유인-부호]] — 데모 한계·윤리 고지를 먼저 적음
- [[LTX-2.5]] · [[video-saas]] · [[ai-news]]

## 원본
- 대표 산출물: [[BFS-Best-Face-Swap]] (https://huggingface.co/Alissonerdx/BFS-Best-Face-Swap)
- 확인: ✅ **볼트 HF API 실측**(dl30·dlAll·♥·trendingScore·pipeline_tag·lastModified) · 🔴 프로필·카드 본문 미열람
- 신뢰도: ⭐⭐ (저장소 메타 볼트 실측 · **제공자 실체 미확인 · 정량 수치 0건**)
