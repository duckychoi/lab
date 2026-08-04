---
title: ruvnet/RuView — WiFi 기반 프라이버시 보호 자세 추정
type: source
domain: ai-news
tags: [ai-news, wifi-sensing, pose-estimation, privacy-ai, edge-ai, healthcare]
created: 2026-04-22
updated: 2026-07-25
sources: []
reliability: high
---

# ruvnet/RuView

> [!update] 2026-07-25 갱신 — ⭐86,127 + 벤치·하드웨어 스펙 재확인
> ⭐**86,127**(2026-07-25, GitHub API 실측 · WebFetch "86.1k" 일치) ← ⭐78,763(07-08). 17일간 +7,364로 8만 중반 진입, "카메라 없는 프라이버시 감지" 수요 지속. WebFetch 재확인: CSI를 **6채널 멀티밴드 융합**·Hampel 필터·스펙트로그램으로 처리해 **17키포인트 자세**·의미론적 방실상태 산출, **105개 엣지 모듈**(헬스케어·보안·리테일·산업·연구). 검증치와 실험치를 **정직하게 구분**(존재감지 82.3% temporal-triplet accuracy는 validated, 생체·자세 정밀도는 experimental). reliability high 유지.

> [!insight] 핵심 인사이트
> 카메라 없이 WiFi RF 신호(CSI)만으로 실시간 인체 자세 추정·생체신호·존재 감지. ⭐78,763이 보여주는 건 "프라이버시 보호 AI 감지"에 대한 구조적 수요가 존재한다는 신호다. 2026-07-08 재확인 시 README가 구체 스펙을 명시: **존재 감지 82.3% 정확도**, 호흡 6–30 BPM·심박 40–120 BPM, 낙상·17키포인트 자세, 수면 단계·무호흡 스크리닝. 최소 **$9 ESP32-S3**로 구동돼 "저가 엣지 하드웨어 + 카메라 없는 모니터링"이 실제품 수준으로 성숙.

**GitHub**: https://github.com/ruvnet/RuView
**스타**: ⭐78,763 (2026-07-08, 당일 +1,129) ← ⭐73,058 (2026-06-11) ← ⭐57,762 (2026-05-16) ← ⭐49,992
**라이선스**: MIT · **스택**: Rust 55.1% + Python 15.1% + JS/TS 20% / ESP32 펌웨어 · Docker · PyPI
**신뢰도**: ⭐⭐⭐⭐

## 도메인별 추출

- **신뢰도**: ⭐78,763 (2026-07-08; 이전 73,058) — 두 달 연속 상승, MIT, README 실측(82.3% 존재감지·232 릴리스)
- **즉시 활용**: 헬스케어·노인케어·스마트홈 시나리오에 즉시 적용 가능. Home Assistant·Matter·Apple/Google Home·Alexa 연동으로 스마트홈 통합 용이.
- **6개월 영향력**: CCTV 대체 수요 시장 — 의료기관·요양원에서 카메라 없는 모니터링 니즈. $9 ESP32-S3 진입장벽이 확산 가속.
- **하드웨어**: 최소 $9 ESP32-S3, 권장 메시 2–6노드($24–54), Cognitum Seed 어플라이언스(~$140)
- **허와 실**: WiFi 환경 품질에 정확도 크게 의존. 카메라 대비 낮은 해상도. 82.3%는 held-out temporal-triplet 존재감지 수치로, 정밀 자세·생체신호 정확도는 별개 검증 필요.
- **액션**: star + 헬스케어 연계 PoC 검토 ($9 ESP32-S3로 존재감지 재현 실험)

## 관련 페이지
- [[AI-에이전트-프레임워크]]
- [[comma-ai]] — 저가 하드웨어 + ML 엣지 배포 계열
- [[ai-news]]

## 원본
- 출처: https://github.com/ruvnet/RuView
- GitHub: ⭐86,127 (2026-07-25, GitHub API 실측·WebFetch 일치) ← ⭐78,763(07-08) ← ⭐73,058(06-11), MIT
- 스택: Rust+Python+JS/TS, ESP32 CSI 6채널 멀티밴드 융합, 105 엣지 모듈, 검증 존재감지 82.3%
- 신뢰도: ⭐⭐⭐⭐ (라이브 스타·README WebFetch 실측, 생체·자세 정밀도는 experimental)
