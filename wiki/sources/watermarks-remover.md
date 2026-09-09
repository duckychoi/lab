---
title: "watermarks-remover — 다중 벤더 AI 출처표시 제거 에이전트 스킬"
type: source
domain: ai-news
tags: [ai-news, github, provenance, watermark, c2pa, synthid, agent-skill, dual-use]
created: 2026-09-09
updated: 2026-09-09
sources: []
reliability: high
---

# watermarks-remover

> [!insight] 핵심 인사이트
> raw는 이것을 *"로컬 앱"* 이라 적었지만 README 실측은 **에이전트 스킬 + stdlib Python 서비스**다 — 즉 **[[Claude-Code-워크플로우]]·Codex 안에 설치되어 모델이 스스로 호출하는 도구**다. 그리고 제거 대상이 추상적 "워터마크"가 아니라 **벤더 이름으로 명시**돼 있다: [[Anthropic]] Claude · [[Google]] Gemini/SynthID-Text · [[OpenAI]] provenance surfaces · 오픈LLM Kirchenbauer green-list · keyed-Gumbel/EXP(Aaronson). 파일 계층은 **C2PA/EXIF/XMP**를 약 30종 포맷에서 제거한다.
> → raw의 분류 판단(*"기능상 AI 출처표시 무력화 도구"*)은 **원문으로 오히려 더 강하게 뒷받침된다.**

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐⭐⭐ — ⭐21,458 · fork 2,469 · Python · MIT · pushed 2026-09-09(당일) · 생성 2026-08-11. **한 달 만에 2만 스타** — 이 배치 최다.
- **즉시 활용**: **NO — 의도적으로 설치하지 않는다.** 기술적으로는 `python3 install_skill.py --skill remove-ai-marks --target claude-code` 한 줄이면 내 환경에 들어온다. 그게 바로 위험이다.
- **6개월 영향력**: C2PA/SynthID 진영이 밀고 있는 **출처표시 인프라의 실효성**을 정면으로 시험한다. 표식이 "붙어 있다"와 "지워지지 않는다"는 완전히 다른 문제라는 것을 2만 스타로 증명하는 중.
- **대체 관계**: 대체가 아니라 **무력화**. 내가 쓰는 생성 도구가 남기는 표식을 지우는 쪽에 선다.
- **허와 실**: README는 *"content **you own**"*(본인 소유 콘텐츠)와 *"privacy and hygiene"*를 전제로 내건다. 그러나 **소유권을 검증하는 코드는 없다** — 전제일 뿐 강제가 아니다. 3계층 중 Layer B(통계적 토큰 샘플링 워터마크)는 README가 스스로 *"model-instruction-based and therefore **best-effort**"* 라고 인정한다. **Layer A(비가시 유니코드·bidi·tag chars)와 파일 메타데이터 제거만 결정적(deterministic)이다.**

> [!warning] 이중용도 — 볼트 분류 판단
> 이 레포는 **"내 문서에서 실수로 들어간 비가시 문자를 지운다"**(정당)와 **"AI 생성물임을 숨긴다"**(출처표시 무력화)를 **같은 코드 경로**로 수행한다. 벤더 provenance 시스템을 이름으로 겨냥하고 C2PA를 벗겨내는 이상, 후자가 부수효과가 아니라 **설계된 기능**이다.
> 볼트는 이것을 **기록은 하되 채택하지 않는다.** 남이 이 도구를 쓴다는 전제로 **내 검증 파이프라인을 설계**하는 것이 올바른 대응이다.

> [!note] 이름이 바뀌었다
> 원래 이름은 **`remove-claude-marks`** 였고 슬래시 별칭 `/remove-claude-marks` 가 아직 문서에 남아 있다. 즉 **처음에는 [[Anthropic]] 단일 벤더 표적으로 출발**해 다중 벤더로 확장된 프로젝트다.

> [!action] 당장 할 것
> 설치가 아니라 **방어**: 내가 배포하는 산출물의 출처표시가 이 3계층 중 어디에 해당하는지 확인한다. Layer A(비가시 문자)에만 의존하는 표식은 **결정적으로 제거된다**고 가정하고 설계할 것.

## 관련 페이지
- [[출처표시-무력화]]
- [[에이전트-스킬]]
- [[Claude-Code-워크플로우]]
- [[Anthropic]]
- [[OpenAI]]
- [[Google]]

## 원본
- 출처: https://github.com/guillaumemeyer/watermarks-remover
- 실측(2026-09-09): ⭐21,458 · fork 2,469 · Python · MIT · created 2026-08-11 · pushed 2026-09-09 · archived=False
- raw 대비 드리프트: 21,457 → **21,458 (+1)**
- 릴리스: v0.7.0
- 신뢰도: ⭐⭐⭐ (스타 2만 초과, 활발한 개발)
