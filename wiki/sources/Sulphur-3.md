---
title: "SulphurAI/Sulphur-3 — MiniMax H3 기반 검열 해제 영상 생성 체크포인트 · 🔴 H3 Community License 승계(대한민국 제외)"
type: source
domain: video-saas
tags: [video-saas, hf-model, video-generation, uncensored, minimax-h3, license-restriction]
created: 2026-11-24
updated: 2026-11-24
sources: [https://huggingface.co/SulphurAI/Sulphur-3]
reliability: low
---

**HF**: dl30 133,732(볼트 API 11-24 · 수집기 11-23 78,931 — 급등 구간) · 좋아요 864(수집기 813) · 생성 2026-10-31 · 내부 ID `988224b9…`(수집기 `6ae65005…` — 🔴 볼트 API 재확인값) · base_model `MiniMaxAI/MiniMax-H3` · [[Sulphur-2-base]] 후속

## 핵심 인사이트
> [!insight] "일반 H3 모델처럼 그대로 쓰면 된다"는 카드 — 그 말은 지역 라이선스까지 그대로 승계한다는 뜻
> [[MiniMax-H3]] 를 파인튜닝한 검열 해제 영상 생성 체크포인트. `s3.safetensors` 를 일반 H3 모델처럼 그대로 사용하면 된다고 카드가 설명. 변형: `s3_raw`(RL LoRA 미적용) · `s3_raw_lora`(LoRA 형태) · `s3_ref2va`(Ref2VA 변형, **카드 표기 "not trained"**) · 선택형 corrector(ComfyUI 노드 · 워크플로 zip, 다른 H3 모델에도 적용) · 저VRAM 양자화(`quantized/` int8 · w4a8) · experimental 다수(작성자가 "무시 권장").

> [!warning] 🔴 라이선스 — [[라이선스-지역-제외]] 파생, 벤치 수치 0
> **카드에는 벤치마크 · 생성 시간 · 화질 수치가 전혀 없다** — 텍스트 55행, 사용법과 파일 목록뿐. **라이선스: MiniMax H3 Community License 그대로 승계 — LICENSE 10행 "Excluded Territories = EU · 영국 · 대한민국 · 미국", 8행 적용 지역 = 제외 지역 밖 전 세계, 42행 "적용 지역 밖에서 사용 · 복제 · 배포 · 출력물 이용 금지"**(83행 중 `territor|korea|exclud` 적중 10행 — 수집기 판독, H3 계열 라이선스 판독과 동일 구조). **한국에서는 라이선스상 사용 불가 — 동향 기록용.**

## 도메인별 추출 (video-saas)
- **[[라이선스-지역-제외]] 파생**: H3 계열 파생 중 다운로드 상위권(dl30 133k)인데 지역 제외를 승계 — **"검열을 풀었지만 권리는 못 풀었다"**. 파생 카드의 license 필드만 보면 지역 조항이 보이지 않는 문제([[Hy4-flash-GGUF]] 때와 동일)가 여기서도 반복.
- **[[원본-파생-역전]] 방향 보강**: Sulphur-2-base dl 92,239 · 좋아요 2,234 vs Sulphur-3 dl 133,732 · 좋아요 864(볼트 API 11-24) — 다운로드는 파생 우세, 좋아요는 원본 2.6배. 계열 3번째 표본.
- **H3 생태 관찰**: "corrector 를 다른 H3 모델에도 적용 가능" — 검열 해제 부품이 모델 경계를 넘어 재사용되는 구조. 부품화된 우회는 원본 라이선스 집행과 충돌하는 지점.
- **액션**: 없음 — H3 보류 목록에 추가(기존 actionable 갱신).

## 관련 페이지
- [[Sulphur-2-base]] · [[MiniMax-H3]] · [[라이선스-지역-제외]] · [[FreeVideo]] · [[원본-파생-역전]] · [[video-saas]]

## 원본
- 출처: https://huggingface.co/SulphurAI/Sulphur-3
- 확인 범위: HF models API(볼트 11-24) · LICENSE 판독(10 · 8 · 42행)은 수집기 11-23 — 볼트 라이선스 원문 직접 재열람은 미실시(H3 계열 3종 동일 문언 확인 이력) · 카드 벤치 수치 0 재확인 · 실행 0
- 신뢰도: ⭐⭐
