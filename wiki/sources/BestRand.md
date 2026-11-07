---
title: "BestRand — 벤치 압축은 무작위로 거의 충분하다. 문제는 오차의 긴 꼬리이고, 그것만 잘라낸다"
type: source
domain: ai-news
tags: [ai-news, hf-paper, benchmark, evaluation, benchmark-compression, cmu, tinybenchmarks]
created: 2026-11-07
updated: 2026-11-07
sources: [https://huggingface.co/papers/2611.00883]
reliability: medium
---

**HF**: upvote **50**(볼트 11-07 · 수집기 34 · 11-06 2위) · Carnegie Mellon University · 저자 6명 · arXiv 2611.00883 · 코드 [George-Ling3/BestRand](https://github.com/George-Ling3/BestRand) **★7 · MIT**(볼트 11-07 실측 · 수집기 ★3) · 벤치별 `items.jsonl.gz`·`scores.npz` 데이터 동봉

## 핵심 인사이트
> [!insight] 부분집합 추정 오차는 평균이 아니라 꼬리가 문제다
> 전체 벤치 점수를 부분집합으로 추정할 때 **대부분의 무작위 부분집합은 오차가 작고, 소수가 큰 오차를 낸다(long-tail)**. 이 불안정성은 모델 수를 늘려도 사라지지 않는다. 그래서 정교한 데이터 의존 선택(ZipBench·TinyBenchmarks)보다 **"무작위 + 꼬리 제거"** 가 싸고 안정적이다. BestRand 는 후보 풀만 탐침해 고오차 꼬리를 줄인다. 70+ 텍스트·멀티모달·에이전트 벤치 + VLA 평가.

> [!warning] 수치마다 "무엇 대비"가 다르다 (초록 원문 볼트 확인)
> - *"Compared with competitive methods, BestRand reduces high-error risk by **50.2%** and estimation error by **16.4%** on average, while requiring only **51.3%** of the construction cost. It further reduces OOD estimation error by **21.8%**"*.
> - 수집기 분해(본문 실험 절 기준): 16.4%·50.2% = Random·ZipBench·TinyBenchmarks 3종 대비 평균 · **51.3% = 데이터 의존 베이스라인(ZipBench·TinyBenchmarks)의 구축 비용 대비** — **Random 대비가 아니다**(Random 구축 비용은 사실상 0). → [[비매칭-비교]]

## 도메인별 추출 (ai-news)
- **신뢰도**: CMU · 코드+데이터 공개(★7) · 70+ 벤치.
- **즉시 활용**: YES(개념) — 로컬 모델 비교 시 전체 벤치 대신 **무작위 부분집합을 여러 번 뽑고 극단값을 버리는** 것만으로 비용 대비 안정성 확보. 코드가 작다(`.py` 7개).
- **6개월 영향력**: "작은 평가셋"의 신뢰 구간을 꼬리 관점으로 보게 한다 — [[표본순위-전수순위]] 와 같은 문제의식.
- **대체 관계**: TinyBenchmarks 류 데이터 의존 압축을 대체.
- **허와 실**: 51.3% 를 "Random 의 절반 비용"으로 읽으면 틀린다.
- **액션**: 레포 star · 다음 로컬 LLM 비교 때 적용 검토.

## 관련 페이지
- [[벤치마크-외부축]] · [[표본순위-전수순위]] · [[비매칭-비교]] · [[벤치-개조-재평가]]
- 같은 날 논문: [[VFlash]] · [[Harness-S]] · [[TailSteer]] · [[WeLM-Image]]

## 원본
- 출처: https://huggingface.co/papers/2611.00883 · https://arxiv.org/html/2611.00883v1 · https://github.com/George-Ling3/BestRand
- 확인 범위: HF API · arXiv HTML 초록 원문(볼트) · 4개 수치 본문 검출 · "무엇 대비" 분해는 수집기 기준(본문 실험 절) · GitHub API · 실행 0회
- 신뢰도: ⭐⭐ (CMU · 코드·데이터 공개)
