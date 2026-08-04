---
title: OfficeCLI — AI 에이전트 전용 오피스 스위트(CLI/MCP)
type: source
domain: ai-news
tags: [ai-news, github-trending, agent, office, docx, xlsx, pptx, mcp, csharp]
created: 2026-07-08
updated: 2026-07-08
sources: []
reliability: high
---

# iOfficeAI/OfficeCLI (GitHub ⭐10,728)

**GitHub**: https://github.com/iOfficeAI/OfficeCLI
**스타수**: 10,728 (2026-07-08 기준, 당일 +893) · 포크 718
**라이선스**: Apache 2.0 · **스택**: C# 94.4% + 임베디드 .NET 런타임 (단일 네이티브 바이너리, macOS·Linux·Windows)

> [!insight] 핵심 인사이트
> "**AI 에이전트를 위한 최초의 오피스 스위트**"를 표방 — Word·Excel·PowerPoint를 XML 탐색 없이 **경로 기반 주소(`/slide[1]/shape[2]`)**로 읽고 쓴다. 핵심 차별점은 ①**Office 설치 없이** 문서→HTML/PNG 렌더링 내장, ②쓰기 시 **350+ Excel 함수 자동 계산**(동적 배열 포함), ③`{{key}}` 템플릿 치환, ④**MCP 서버** 제공으로 에이전트가 JSON-RPC 도구로 직접 호출. [[OfficeCLI]]는 "에이전트가 오피스 산출물을 직접 만든다"는 유스케이스를 겨냥 — [[pptx-generate]]·[[reat-slides]] 같은 문서/슬라이드 자동화 스킬의 오픈소스 대조군이자, MCP 도구로 붙일 수 있는 산출물 생성 백엔드.

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐⭐⭐ (⭐10,728 당일 +893, Apache 2.0, README WebFetch 실측 — MCP 서버·렌더링 엔진·350+ 함수 확인)
- **즉시 활용**: YES — MCP 서버로 내 에이전트에 붙이면 pptx/xlsx/docx **네이티브 산출**이 가능. 현재 [[pptx-generate]]가 PDF/이미지 재현에 의존하는 데 비해, OfficeCLI는 편집 가능한 진짜 오피스 파일을 생성 → 산출물 편집성이 필요할 때 유력.
- **6개월 영향력**: "에이전트가 보고서/슬라이드/스프레드시트를 직접 완성"하는 워크플로가 흔해짐. Office 설치 없는 서버 렌더링은 헤드리스 파이프라인에 유리.
- **대체 관계**: python-docx/openpyxl/python-pptx 조합을 단일 CLI+MCP로 대체. 라운드트립 JSON 직렬화로 재현성 확보.
- **허와 실**: "최초·최고"는 마케팅. 실체는 = .NET 오피스 라이브러리를 에이전트 친화 인터페이스(경로 주소+MCP+구조화 JSON)로 잘 감싼 것. C#/.NET 스택이라 파이썬 생태계와는 별도 프로세스.
- **액션**: MCP 서버 등록 후 [[pptx-generate]] 산출물 1건을 OfficeCLI로 네이티브 pptx 생성해 편집성·정확도 비교.

## 관련 페이지
- [[pptx-generate]] — PDF/이미지 재현식 슬라이드 스킬 (대조군)
- [[reat-slides]] — 슬라이드 영상 자동화
- [[claude-skills]] — 스킬/도구 생태계
- [[ai-news]]

## 원본
- 출처: https://github.com/iOfficeAI/OfficeCLI
- GitHub: ⭐10,728 (2026-07-08, 당일 +893), Apache 2.0, 포크 718
- 스택: C# 94.4% / 단일 네이티브 바이너리 / MCP 서버 제공
- 신뢰도: ⭐⭐⭐ (라이브 스타·README WebFetch 실측)
