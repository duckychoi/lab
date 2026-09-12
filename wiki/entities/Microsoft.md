---
title: Microsoft
type: entity
domain: ai-news
tags: [ai-news, organization, bigtech, education, open-source]
created: 2026-07-02
updated: 2026-07-10
sources: [AI-For-Beginners.md, SkillOpt.md]
reliability: high
---

# Microsoft

> [!insight] 핵심 인사이트
> 빅테크로서 AI 제품(Copilot·Azure AI)뿐 아니라 **대규모 오픈 교육 자산**을 GitHub에 다수 운영한다(AI/ML/데이터사이언스 for Beginners 시리즈). 이 위키에는 [[AI-For-Beginners]](12주 24강 AI 기초 커리큘럼, MIT)로 등장 — MS발 교육 레포는 신뢰도는 높지만 *실무 도구가 아닌 레퍼런스*로 분류해 신호/잡음을 구분해야 한다.

> [!note] 2026-07-10 추가 — 연구가 실무 도구로
> 교육 레퍼런스 외에 **에이전트 스킬 최적화 툴**을 실제 코드로 공개. **[[SkillOpt]]**(GitHub ⭐12,019, MIT)는 5월 논문(arXiv 2605.23904)이 **동작하는 텍스트공간 옵티마이저**로 릴리스된 것 — 프로즌 LLM의 자연어 스킬을 궤적 기반 편집 + 검증 게이트로 최적화해 `best_skill.md` 산출, Claude/Claude Code 백엔드 지원. Microsoft가 "교육 자산"을 넘어 **에이전트 스킬 인프라**로도 실무 도구를 내놓기 시작한 신호.

## 관련 소스
- [[AI-For-Beginners]] — 12주 24강 AI 기초 커리큘럼 (MIT, 50+ 언어)
- [[SkillOpt]] — 프로즌 LLM 스킬 텍스트공간 최적화 툴 (⭐12,019, MIT) *(2026-07-10)*

## 관련 페이지
- [[SkillCoach]] · [[agent-skills]] — 스킬 생태계(평가·배포)
- [[ai-news]]

## 원본
- 조직: Microsoft
- 관련 활동: 오픈 교육 커리큘럼(GitHub) · Azure AI · Copilot
- 신뢰도: ⭐⭐⭐ (공식 빅테크)

---

## 🔄 2026-09-12 — [[VibeVoice-ASR-Streaming-7B]] 공개, 그러나 **평가 수치가 0개다**

> [!insight] 화자귀속을 후처리에서 모델 내부로
> ♥**213** · 30일 다운로드 **2,279** · **MIT** · created 2026-09-02(2026-09-12 HF API 실호출).
> 별도 다이어리제이션 단계 없이 **'누가 무엇을 말했는지'를 스트리밍 출력**(고정 청크 + 소량 lookahead + 이전 텍스트 인터리빙). 핫워드 지원. **언어 10종 — 한국어 포함**(메타 실측).
> 볼트 기존 [[VibeVoice]](TTS) · [[VibeVoice-microsoft]](TTS 1.5B / ASR 7B / 실시간TTS 0.5B)의 **ASR 축이 스트리밍으로 독립 공개**된 것.

> [!warning] 🔴 두 가지 문서 결함 — Microsoft 공식 레포인데도
> **① 모델카드 전체가 2,236B 이고 수치가 0건이다.** `## Evaluation` 섹션의 내용물은 **이미지 태그 1줄**(`VibeVoice_ASR_Streaming_results.png`). 정규식 전수 검색으로 WER/CER/백분율 **0건 확인**. 테크리포트(arXiv 2609.02812) 초록도 *"5개 평가셋 평균 최저"*, *"13개 설정 중 12개 최고"* 라는 **상대 표현만** — 절대 수치 없음.
> → 🎯 **"최저/최고"는 순위이지 성능이 아니다.** WER 3%의 1등과 25%의 1등은 도입 판단이 정반대다.
>
> **② 이름은 7B인데 `safetensors` 실측 8,674,021,857 = 8.67B (+24%).** 반올림이 아니다. 추정 원인은 *LM 백본 + 오디오 인코더 타워* 이지만 **카드에 아키텍처·파라미터 설명이 전혀 없어 확인 불가.** VRAM 산정 시 **17.3GB 기준**으로 잡아야 한다 → [[단위-불일치]] ②.
> → **벤더 신뢰도와 문서 품질은 별개**라는 사례. 볼트가 보통 경계하는 *과장* 이 아니라 **정보 부재**가 문제다.

## 관련 페이지 (2026-09-12 추가)
- [[VibeVoice-ASR-Streaming-7B]]
- [[단위-불일치]]
- [[X-AuT]]
