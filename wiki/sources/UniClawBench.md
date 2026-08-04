---
title: UniClawBench — 능동적 에이전트 실세계 범용 벤치마크
type: source
domain: ai-news
tags: [ai-news, huggingface, paper, agent-benchmark, proactive-agent, hku, meituan]
created: 2026-07-10
updated: 2026-07-10
sources: []
reliability: medium
---

# HF논문: UniClawBench — A Universal Benchmark for Proactive Agents on Real-World Tasks (arXiv 2607.08768)

**HuggingFace**: https://huggingface.co/papers/2607.08768
**기관**: 홍콩대 MMLab(Zhekai Chen·Chengqi Duan·Xihui Liu 외) + [[Meituan]](Manyuan Zhang)

> [!insight] 핵심 인사이트
> **실세계 과업에서 능동적(proactive) 에이전트를 평가하는 역량 기반 범용 벤치마크.** WebFetch로 초록 실측: 400개 이중언어 과업을 5개 근본 역량(**Skill Usage·Exploration·Long-Context Reasoning·Multimodal Understanding·Cross-Platform Coordination**)으로 조직. 핵심은 **3역할 폐루프 평가** — ①실제 Docker 컨테이너에서 과업 수행하는 executor, ②세밀 루브릭을 적용하는 **숨은 supervisor**, ③채점 기준 접근 없이 피드백만 주는 user simulator(정보 누출 차단 + 멀티턴). 충격 결과: **[[Claude-Code-워크플로우|Claude Opus-4.8]]·GPT-5.4도 pass 50% 미만** — 샌드박스 성능과 실세계 성능의 큰 격차 실증. 프레임워크가 결과를 크게 좌우(OpenClaw > EDICT/Nanobot), 모델은 skill usage·exploration엔 강하나 **롱호라이즌 메모리·크로스플랫폼 협조에 약함**. 사람 채점 일치율 92%. 내 스케줄 에이전트 운용에 "능동 에이전트는 아직 롱호라이즌·크로스플랫폼에서 신뢰 못 함"이라는 현실 앵커.

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐⭐⭐ (arXiv 2607.08768 초록 WebFetch 검증 — 400과업·5역량·3역할 루프·Opus-4.8/GPT-5.4 <50%·92% 일치 확인. 재현 미실측 → medium)
- **즉시 활용**: 간접 — 벤치. 단 "롱호라이즌 메모리·크로스플랫폼이 약점"은 내 [[에이전트-메모리-레이어]] 투자 우선순위의 근거.
- **6개월 영향력**: 에이전트 평가가 정적 태스크→**"하니스까지 포함한 폐루프 실측"**으로 이동([[UniClawBench]]=하니스 영향 명시). 프런티어 모델도 <50%라 "에이전트 자율성 과신 금지" 상수.
- **대체 관계**: [[EnterpriseClawBench]]·[[TUA-Bench]]·[[Beyond-Static-Leaderboards]] 계보 확장 — 능동성·크로스플랫폼 축 추가.
- **허와 실**: "Opus-4.8·GPT-5.4 <50%"는 초록 명시. 단 과업 구성·루브릭 난이도 설계가 점수를 좌우하므로 절대 비교보다 "격차 존재"를 취함.
- **액션**: 없음(벤치). 다만 스케줄 태스크 설계 시 "크로스플랫폼·롱호라이즌 단계는 사람 확인 게이트" 원칙 채택 근거로 기록.

## 관련 페이지
- [[EnterpriseClawBench]] — 실무 세션 기반 에이전트 벤치(계보)
- [[Beyond-Static-Leaderboards]] — 정적 리더보드 타당성 한계
- [[에이전트-메모리-레이어]] — 롱호라이즌 메모리 약점 → 투자 근거
- [[Meituan]] — 공동 제작(하루 뒤 [[LongCat-2.0]]와 별개)
- [[ai-news]]

## 원본
- 출처: https://huggingface.co/papers/2607.08768
- arXiv: 2607.08768, UniClawBench (HKU MMLab + Meituan)
- 성과: 400 이중언어 과업 / 5역량 / 3역할 폐루프 / 프런티어 모델 pass <50% / 사람 일치 92%
- 신뢰도: ⭐⭐⭐ (초록 원문 검증 / 재현 미실측)
