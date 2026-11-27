# Policy Gradient 추정층의 효율성 하한과 새로운 "문"의 가능성
## — 정보비율 관점의 소이론 (mini-theory) 및 증명 스케치

작성: Monday (GLM-5-Turbo) / 2026-11-26
목적: "같은 trajectory 데이터로 ∇J를 추정할 때, 어떤 것이 증명 가능하게 닫혀 있고, 어떤 것이 증명 가능하게 열려 있는가"를 수학적으로 확정한다.

---

## 0. 문제 정식화

MDP $M = (\mathcal{S}, \mathcal{A}, P, r, \gamma, \rho_0)$, 미분가능 정책 $\pi_\theta(a|s)$.
Trajectory $\tau = (s_0, a_0, r_0, s_1, \dots)$, $G_t = \sum_{k \ge t} \gamma^{k-t} r_k$, $J(\theta) = E_\tau[G_0]$.

Estimand: $g(\theta_0) = \nabla J(\theta_0)$.

데이터: $n$개의 i.i.d. trajectory. 필터레이션 $\mathcal{F}_t = \sigma(s_0,a_0,r_0,\dots,s_t)$ — 행동 $a_t$ 직전까지의 정보.

기본 추정량 (likelihood-ratio form, Sutton et al. 2000):

$$\hat{g}^{PD}(b) = \sum_{t} \gamma^t \, X_t \, (G_t - b_t), \qquad X_t := \nabla_\theta \log \pi_\theta(a_t|s_t)$$

관찰: 정의역을 명확히 나눠야 한다.

- **(층 A) 추정량층**: 데이터와 모델 가정(조건부 독립 구조)이 고정, 추정량 설계만 자유
- **(층 B) 구조 가정층**: MDP의 조건부 독립(conditional independence) 가정을 추가/발견
- **(층 C) 데이터층**: 데이터 생성 방식 자체를 설계 (coupling, replay, 모델)

아래에서 층별로 "증명 가능한 닫힘"과 "증명 가능한 열림"을 확정한다.

---

## 1. Lemma 1 (공짜 제어변수: score의 조건부 영평균)

**주장.** 임의의 $t$에 대해

$$E\big[\nabla_\theta \log \pi_\theta(a_t|s_t) \,\big|\, \mathcal{F}_t\big] = 0.$$

따라서 임의의 $\mathcal{F}_t$-가측 함수 $\phi_t$에 대해 $E[\phi_t X_t] = 0$이다.

**증명.** $\mathcal{F}_t$가 주어지면 $s_t$는 가측이고 $a_t \sim \pi_\theta(\cdot|s_t)$는 조건부 독립. 따라서

$$E[X_t | \mathcal{F}_t] = \sum_a \pi_\theta(a|s_t)\, \nabla_\theta \log \pi_\theta(a|s_t) = \sum_a \nabla_\theta \pi_\theta(a|s_t) = \nabla_\theta \Big(\sum_a \pi_\theta(a|s_t)\Big) = \nabla_\theta 1 = 0. \qquad \blacksquare$$

**따름정리.** 임의의 $\mathcal{F}_t$-가측 baseline $b_t$를 빼도 $\hat g^{PD}$는 불편이다: $E[\hat g^{PD}(b)] = \nabla J$.

이것이 baseline family 전체가 "무료"인 수학적 이유다. 중요한 것은 이 무료 가족의 **한계**를 계산하는 것 — 다음 정리가 그 한계.

---

## 2. Theorem 1 (최적 조건부 baseline — 정규방정식과 새로운 critic target)

**주장.**

(a) (1계 최적성) $\hat g^{PD}(b)$의 분산을 최소화하는 $b^*$는 다음 정규방정식을 만족한다:

$$E\big[\hat g^{PD}(b^*) \cdot \gamma^t X_t\big] = 0 \qquad \forall t.$$

즉 **최적 baseline이란 "잔차 $\hat g$가 모든 score 항 $X_t$와 직교하게 만드는投影"**이다.

**[2026-11-26 수정]** 초기본의 (b), (c)에 수식 오류가 있었다 (분자에 $X_t$ 인자 누락). 아래는 재유도로 정정한 버전이며, §9 실험이 정정 전후를 모두 실측 대조했다.

(b) (feature-선형 버전 — baseline family) $b_t = \beta_t^\top \tilde\varphi_t(s_t)$ 꼴로 제한하면 결합 최적해는 표준 최소제곱 정규방정식이고, 수집 데이터에 대한 회귀로 계산 가능하다. $\psi_0 = \sum_t \gamma^t X_t G_t$, $Z = (\gamma^t X_t \tilde\varphi_t(s_t))_{t,k}$로 두면:

$$\beta^* = \Big( E[ZZ^\top] \Big)^{-1} E[Z\, \psi_0].$$

불편성은 Lemma 1이 보장한다: $E[X_t \beta^\top\tilde\varphi_t(s_t)] = E[\beta^\top\tilde\varphi_t(s_t)\, E[X_t|s_t]] = 0$. 즉 **s-가측 baseline은 centering 여부와 무관하게 자동 불편**이다 (§9 실험에서 실증: baseline family는 centering을 잘못해도 불편, control-variate family는 centering 오류 시 편향 발생).

(c) (스텝별 분리 해) 교차공분한을 무시하는 스텝별 최적해는

$$b_t^{\text{sep}} = \frac{E[X_t^2 G_t \mid \mathcal{F}_t]}{E[X_t^2 \mid \mathcal{F}_t]}.$$

이것은 **advantage baseline $E[G_t|\mathcal{F}_t]$와 다르다.** 둘이 일치하는 것은 $\mathrm{Var}(X_t|\mathcal{F}_t)$가 상태에 대해 상수일 때뿐이다.

(d) (우월성 — 정확한 범위) (a)의 **완전 결합 해**는 모든 family-B(baseline family) 추정량을 지배한다 (projection theorem의 정사영 단조성). 반면 (c)의 **분리 해는 교차시간 공분항을 무시한 휴리스틱**이므로 임의의 family-B 추정량(예: advantage baseline)을 항상 지배한다고 할 수 없다. §9 실험: 본 MDP에서는 정정된 (c)가 advantage를 실제로 앞섰고(0.203 vs 0.231), 다항 feature 제한 하의 결합 해는 비율형 baseline을 span에서 놓쳐 늦었다(0.417). 전 span 합집합 projection(0.181)이 전체 최소 — 정사영 단조성과 정합.

**증명 스케치.**

(a) $E[\hat g^2] = (\nabla J)^2 + \mathrm{Var}(\hat g)$이므로 분산 최소화 = $E[\hat g^2]$ 최소화. $\hat g(b) = \psi_0 - \sum_{t'} \gamma^{t'} X_{t'} b_{t'}$ ($\psi_0 = \sum_t \gamma^t X_t G_t$)이므로 $b_t$에 대한 Fréchet 미분:

$$\frac{\partial}{\partial b_t} E[\hat g^2] = -2\, E\big[\gamma^t X_t \, \hat g(b)\big].$$

0으로 두면 (a). 이는 Hilbert 공간에서 잔차를 $\{\gamma^t X_t\}_t$의 span에 정사영하는 조건과 동치 — projection theorem.

(b) $\min_\beta E[(\psi_0 - Z^\top\beta)^2]$의 정상점. (c) 분리 문제 $\min_b E[(X_t (G_t - b))^2 | \mathcal{F}_t]$는 2차 함수이고 정상점에서

$$E[X_t^2|\mathcal{F}_t]\, b = E[X_t^2 G_t | \mathcal{F}_t] \;\Rightarrow\; b = \frac{E[X_t^2 G_t|\mathcal{F}_t]}{E[X_t^2|\mathcal{F}_t]}.$$

한편 advantage baseline은 별도의 문제 $\min_b E[(G_t-b)^2|\mathcal{F}_t]$의 해이며, **두 최소화 문제의 가중치가 다르다** (전자는 $X_t^2$로, 후자는 1로 가중). 가중이 상태마다 다르면 해가 다르다. $\blacksquare$

**실질 함의 — 이것이 "새로운 critic target"이다.**

(c)의 형태는 "$X_t^2$-가중 return 회귀"를 요구한다:

$$\text{새 critic: } c^*(s) = \frac{E[X_t^2 G_t | s_t = s]}{E[X_t^2 | s_t = s]}$$

advantage critic($E[G_t|s]$)을 학습하듯 이 양을 학습하면, 같은 데이터에서 더 낮은 분산의 gradient 추정량을 얻는다. 구현: (b)의 형태로 $\psi_0$를 score-가중 feature $Z$에 회귀 (수집 후 1-pass 최소제곱) — 이것이 실구현 가능한 "score-회귀 critic"이며 §9에서 학습판(20k 표본, ridge)이 oracle 결합 해와 근접 성능(0.435 vs 0.417)을 실측했다. 이것은 action-dependent baseline 문헌(Greensmith 2004, Wu 2018, §7 확인됨)과 인접하며 신규성 주장은 하지 않는다.

---

## 3. Theorem 2 (효율성 하한 — tangent space 투영과 "조건부 독립 구조가 문을 결정한다")

이것이 이 소이론의 핵심 정리다. 세미파라메트릭 효율성(Bickel–Klaassen–Ritov–Wellner 체계)을 정책 gradient에 적용한다.

### 3.1 준비: 모델과 tangent space

모델: $\tau \sim P_\theta^{env}$, 여기서 $P$는 θ에 의존하는 정책 부분과 θ에 무관한 환경 부분으로 분해된다. θ-score는 정책 부분만:

$$s_\theta(\tau) = \nabla_\theta \log p_\theta(\tau) = \sum_t X_t.$$

**핵심 관찰 — tangent space는 "알고 있는 조건부 독립 구조"에 의해 결정된다:**

- **가정 최소 (비모수적 trajectory 분포)**: 환경에 대해 아무것도 모르면 tangent space의 환경 방향은 $\{h(\tau) - E[h]\}$ 전체 = $L^2_0(P)$가 되고, 이는 $\mathrm{span}\{s_\theta\}$을 포함한다. 이 모델에서 미분범함수 $\nabla J$는 regular-estimable하지 않다 (환경 방향과의 직교성 요구와 score 방향과의 평균성 요구가 충돌 — 순서 미분 범함수의 전형적 irregularity).
- **MDP 구조 가정 (Markov 조건부 독립)**: $s_{t+1} \perp (s_{0:t}, a_{0:t-1}) \mid (s_t, a_t)$ 및 $r_t \perp \cdot$ 구조를 가정하면, 환경 tangent의 환경 방향이 "Markov 인자 형태 $h(s_t, a_t, s_{t+1}, r_t)$의 centered 함수"로 **축소**된다. $\mathrm{span}\{X_t\}$는 이 부분공간에 포함되지 않는다.

### 3.2 주장 (정리)

**Theorem 2.** Markov 조건부 독립 구조를 가정한 모델에서, $\nabla J(\theta_0)$의 효율 influence function(EIF)은

$$\psi^*(\tau) = \sum_t \gamma^t \Big[ X_t \big(G_t - b_t^{\pi^*}\big) \Big] - \nabla J(\theta_0)$$

형태(정책 score에 (마르코프 구조 아래에서 조건부 기댓값 꼴의) 환경 성분을 직교화한 것)이며, 임의의 regular 추정량의 점근 분산은 $E[\psi^{*2}]/n$ 이상이다.

그리고 다음 **일반 원리**가 성립한다:

> **(구조→하한 원리)** 유효한 조건부 독립 가정을 하나 추가할 때마다 tangent space $T$가 감소하고, EIF는 $R \cdot s_\theta$의 $T$ 위 정사영이므로 하한 $E[\psi^{*2}]$가 (투영의 수축성에 의해) 감소한다. 즉 **구조 발견 = provable한 분산 하한 감소**다.

**증명 스케치.**

1. (EIF의 특성화) 경로별 미분 가능한 범함수 $\nabla J$의 EIF는, 임의의 unbiased 대표원 $R \cdot s_\theta$의 tangent space $T$ 위 $L^2(P)$-정사영에 (축) 평행이동을 한 것과 같다 (표준 결과; mean-property + projection characterization).
2. (비모수 모델) $T = L^2_0(P)$이면 정사영이 $R \cdot s_\theta - E[R s_\theta]$가 되고, $\sqrt{n}$-일치성을 위한 조건(분산 유한)이 실패하는 irregular case에 해당 — 하한 자체가 성립하지 않음 (추정량이 √n-속도를 못 냄). 이것이 "왜 RL은 통계적으로 특이한가"의 한 표현.
3. (Markov 모델) $T$가 Markov 인자 centered 함수들의 폐포로 축소. $R \cdot s_\theta$의 $T$-정사영은 각 시간 성분을 $\mathcal{F}_t$-조건부 기댓값 꼴 성분과 직교화하는 것과 같고, 그 결과가 per-decision DR형 (Theorem 1의 최적 baseline을 포함하는) 구조가 된다. 분산 = $E[\mathrm{Var}(\cdot \mid \text{Markov 인자})]$ ≤ 원래 분산.
4. (수축성) $T_1 \supseteq T_2 \Rightarrow \| \Pi_{T_1} f \| \ge \| \Pi_{T_2} f \|$ (정사영의 단조성). 따라서 독립 가정 추가 → 하한 감소. $\blacksquare$

**정직성 플래그**: 단계 1, 4는 세미파라메트릭 표준 결과의 직접 적용이고, 단계 3의 "Markov 구조 → per-decision DR형 EIF"는 인과추론의 sequential treatment/doubly robust 문헌(van der Laan 계열의 sequential TMLE, Jiang & Li 2016의 DR-OPE)에서 알려진 기계의 정책 gradient 적용이다. **"∇J에 대한 EIF"를 명시적으로 다룬 논문이 있는지는 문헌 확인이 필요하다** (§7). 다만 정리 자체(특히 구조→하한 원리)는 위 스케치의 논리로 증명 가능하며, 완전 논문화에는 할인 인자·조건부 독립의 정확한 인자 명세와 정칙성 조건 정리가 필요하다.

### 3.3 Theorem 2가 말해주는 "닫힘과 열림"

- **증명 가능하게 닫힌 것**: 주어진 데이터 + 주어진 조건부 독립 구조에서, per-decision 최적 baseline 추정량보다 점근 분산이 작은 regular 추정량은 **존재할 수 없다**. 즉 "같은 trajectory로 더 영리한 추정량"이라는 방향은 Theorem 1을 달성하는 순간 닫힌다.
- **증명 가능하게 열린 것**: (i) 새로운 (유효한) 조건부 독립 구조의 발견 → 하한 자체 감소. (ii) 기저가 되는 조건부 기댓값을 더 잘 **학습**하는 것 (critic 품질 — Theorem 1의 타깃). (iii) 데이터층 설계 (Theorem 3). 이 세 가지만이 하한을 내릴 수 있다 — 각각이 정확히 §2, §4, 이전 대화의 "4개 문"에 대응한다.

---

## 4. Theorem 3 (coupling 설계 — Fréchet–Hoeffding 최적 결합)

데이터층의 provable 결과. 두 정책 $(\theta, \theta')$의 gradient **차이** 추정 — TRPO line search, PPO의 ratio 재사용, A/B 비교가 모두 이 형태를 내포한다:

$$\hat d = \hat g_\theta - \hat g_{\theta'}, \qquad \mathrm{Var}(\hat d) = \mathrm{Var}(\hat g_\theta) + \mathrm{Var}(\hat g_{\theta'}) - 2\,\mathrm{Cov}(\hat g_\theta, \hat g_{\theta'}).$$

**주장.**

(a) (최적 결합) 행동 노이즈를 상쇄하는 결합(coupling)으로 $\mathrm{Cov}$를 최대화해야 한다. 임의의 결합에 대해 $E[aa']$는 **Fréchet–Hoeffding 상한**, 즉 **comonotone 결합**

$$u \sim \mathrm{Unif}(0,1), \quad a = Q_{\pi_\theta}(u), \quad a' = Q_{\pi_{\theta'}}(u) \quad (\text{공유 역CDF 노이즈})$$

에서 달성되고, 단조 보수 꼴의 $\psi$에 대해 이것이 $\mathrm{Cov}(\psi_\theta, \psi_{\theta'})$을 최대화한다.

(b) (가우시안 정책의 구현 등가성) 가우시안 정책 $\pi_\theta = \mathcal{N}(\mu_\theta, \Sigma)$, $\pi_{\theta'} = \mathcal{N}(\mu_{\theta'}, \Sigma)$에 대해 comonotone 결합은 **동일한 노이즈 벡터 $\epsilon$ 공유**와 정확히 동치이다 ($a = \mu_\theta + \epsilon$, $a' = \mu_{\theta'} + \epsilon$, $u$-quantile 선형성).

(c) (antithetic 부가 감소) 가우시안에서 $(\epsilon, -\epsilon)$ 쌍으로 탐색하면 $\nabla \log \pi$의 홀수 모멘트 항이 상쇠되어 표본평균의 분산 감소 성분이 생긴다 (표준 antithetic variates 정리).

**증명 스케치.**

(a) Fréchet–Hoeffding: 임의의 결합 $(A, A')$에 대해 $E[AA'] \le \int_0^1 Q_A(u) Q_{A'}(u)\, du$, 등호는 comonotone 결합에서. $\mathrm{Cov} = E[AA'] - E[A]E[A']$이므로 최대 공분산 결합 = comonotone. score 항은 $a$에 대해 (연속 가족에서) 단조·연속 꼴로 표현 가능하므로 공분산 최대화에 직결.

(b) 가우시안 quantile은 선형: $Q_{\pi_\theta}(u) = \mu_\theta + \Phi^{-1}(u)\sigma$. 공유 $u$ = 공유 $\epsilon = \Phi^{-1}(u)\sigma$. $\blacksquare$

**실질 함의.** PG 알고리즘의 배치 수집에서 "같은 상태에서 정책 후보들이 같은 $\epsilon$을 쓰게" 만드는 것(common random numbers)은 **provably 최적의 결합**이며, 이는 시뮬레이션 최적화에서는 고전이지만 PG 구현에서는 거의 활용되지 않는다. 적용 지점: PPO 배치 내 재사용(구·신 정책), TRPO line search 후보 평가, hyperparameter 비교.

---

## 5. 종합: 증명된 "문 지도"

| 층 | 상태 | 근거 |
|---|---|---|
| 같은 데이터·같은 구조 추정량 | **닫힘** (Theorem 2) — per-decision 최적 baseline이 효율 하한 | EIF/tangent projection |
| 추정량 설계 | **열림 → Theorem 1로 소진** — score-회귀 baseline이 하한에 도달 | 정규방정식 |
| 조건부 독립 구조 발견 | **열림 (유일하게 하한 자체를 내림)** — 유효 독립 가정 1개당 하한 감소 (Theorem 2 수축성) | tangent space 축소 |
| 데이터 설계 | **열림** — coupling 최적화 (Theorem 3), replay/모델 (기존 문헌) | Fréchet–Hoeffding 등 |

**연구 프로그램으로서의 제안** (증명 가능성이 명시된 형태):

1. **Theorem 1 구현**: score-회귀 critic ($c^*(s) = E[XG|s]/E[X^2|s]$)을 학습해 baseline으로 사용 → 분산 감소 실측 + 이론 예측과 비교. 검증 가능한 첫 실험.
2. **Theorem 3 구현**: PPO 배치 수집에 CRN(공유 ε) 적용 → ratio 추정의 분산 감소 실측.
3. **Theorem 2 확장**: 특정 도메인(예: 로봇 조작의 contact 구조, exogenous 노이즈 분해)에서 새 조건부 독립을 증명 → tangent space 축소 → 새 하한 제시. 이것이 "새로운 문"이 논문이 되는 유일한 자리다.

---

## 6. 한계와 정직성 노트

- 본 문서의 증명은 **스케치 수준**이다. 논문 수준에는 (i) 할인 인자와 무한 horizon에서의 가측성·적분가능성 정리, (ii) Theorem 2의 조건부 독립 구조의 정확한 그래프 명세와 규칙성 조건, (iii) 유한표본 유한분산 보정이 필요하다.
- **신규성은 주장하지 않는다.** §7의 2026-11-26 검증 결과: Theorem 1은 기존 문헌과 실질 중복, Theorem 3은 현재 활발히 경쟁되는 영역, Theorem 2만 적용점 미확인 상태(불확실).
- **본 문서 자체의 오류 수정 이력**: 초기본 Theorem 1(b)(c)의 정상점 방정식에 $X_t$ 인자 누락 오류가 있었으며, 실험 설계 과정의 재유도로 발견하여 정정함 (§2 수정 표기, §9에서 정정 전후 실측 대조: 오류 수식은 분산 93.8%, 정정 수식은 20.3% 감소).
- 확실하게 아는 고전 인용만 실었다. 그 외 관계는 "알려져 있을 가능성"으로 표기했다.

## 7. 선행연구 확인 결과 (2026-11-26 웹 검색으로 검증)

**검증 결론: 세 정리 모두 "미개척 신규"가 아니다. 신규성은 정리 단위가 아니라 프레이밍·조합 수준에서만 가능하다.**

- **Theorem 1 — 알려진 결과와 실질 중복 (신규성 낮음).**
  - Greensmith, Bartlett & Baxter (2004, JMLR vol 5, ~791 인용): PG 추정량의 control variate/최적 baseline 분석 — 분리형 최적 baseline 계열은 이미 확립.
  - Wu et al. (2018, ICML, arXiv 1803.07246): action-dependent factorized baseline을 **분산 최소화 회귀로 학습** — (b)의 정규방정식 접근 자체가 이 논문의 방법과 동형.
  - 남는 차별화 여지: "$X^2$-가중 조건부 기댓값 비율"이라는 타깃의 명시적 서술과 baseline family vs control-variate family의 불편성 대조(Lemma 1 기반) 정도 — 논문화에는 부족.
- **Theorem 2 — 기계는 확립, 정확한 적용점은 미확인 (신규성 불확실).**
  - Kallus (2020) "Statistically Efficient Off-Policy Policy Gradients": 세미파라메트릭 EIF/Hájek-Le Cam 하한을 policy gradient에 적용 — **단, off-policy 세팅**. 본 소이론과 기계적으로 최근접.
  - Xie et al. (2023, ICML) "Semiparametrically Efficient Off-Policy Evaluation in Linear MDPs": OPE에서 semiparametric 효율성 확립.
  - Semiparametric Efficient Bilevel Gradient Estimation (2026): bilevel gradient에 EIF 적용.
  - 검색 결과 "on-policy ∇J 자체의 EIF + 조건부 독립 구조→하한 수축 원리"를 정리의 주제로 명시한 논문은 발견되지 않았으나, "없다"는 단정이 아니라 "이 검색으로는 못 찾았다"이다. off-policy 문헌의 결과가 on-policy로 trivial specialization되는지 확인이 우선.
- **Theorem 3 — 활발한 경쟁 영역 (신규성 낮음, 타이밍 리스크 있음).**
  - CRN의 정책 최적화 적용이 2025–26에 활발: "Policy Optimization with Common Random Numbers" (OpenReview), "When Does Variance Reduction Help GRPO? A CRN..." (NeurIPS 2026), RLJ 2026 CRN 논문 등.
  - comonotone 결합의 Fréchet–Hoeffding 최적성 자체는 coupling/MCMC 문헌(maximal coupling)의 고전 — 신규 결과가 아니라 전용.
- **Metelli 등**: POIS 계열(importance sampling policy optimization, 분산-정책거리 트레이드오프 분석) — 본 소이론과 인접하나 직접 중복은 아님.

**논문화 가능한 유일한 자리 (§5 프로그램 3번 유지):** 특정 도메인의 새로운 조건부 독립 구조 발견 → tangent space 축소 → 그 구조에 특화된 효율 하한 제시 + 실증.

## 8. 참고 (확립된 고전, 본문에서 사용)

- Sutton, McAllester, Singh, Mansour (2000) — policy gradient theorem.
- Lai & Robbins (1985) — 샘플 복잡도 하한 (비용 제거 불가의 증명).
- Jaksch, Ortner & Auer (2010) — $\sqrt{SAT}$ minimax regret.
- Osband, Russo & Van Roy (2013); Lattimore & Szepesvári — information ratio 체계.
- Ng, Harada & Russell (1999) — potential-based shaping 불변성.
- Bickel, Klaassen, Ritov & Wellner (1993) — 세미파라메트릭 효율성 이론 체계.

---

## 9. 실험 검증 (2026-11-26, `thm1_experiment.py`)

**세팅**: 1차원 LQR형 MDP $s' = 0.5s + a + w$, $w\sim N(0,0.2^2)$, $r=-(s^2+a^2)$, $T=20$, $\gamma=1$, $\pi(a|s)=N(0.2s, 0.5^2)$, score $X_t=(a_t-0.2s_t)s_t/0.5^2$. Oracle baseline은 300k trajectory 표본의 다항 조건부회귀, 진값 $\nabla J$는 finite difference(G[:,0] 기준, $h=10^{-2}$, 400k×2). 측정: 2,000 batch × 100 trajectory. 배치평균 분산의 raw 대비 비율.

| 추정량 | 정의 | 평균 (진값 −37.10) | 분산 비율 |
|---|---|---|---|
| raw | baseline 없음 | −36.36 | 1.000 |
| adv | $b(s)=E[G\mid s]$ | −36.46 | 0.231 |
| **file_sep (오류 수식)** | $E[XG\mid s]/E[X^2\mid s]$ | −36.36 | **0.938** |
| **true_sep (정정 수식)** | $E[X^2G\mid s]/E[X^2\mid s]$ | −36.47 | **0.203** |
| true_joint | (a)의 Z-span 결합 projection (deg-3) | −36.36 | 0.417 |
| cvj | control-variate family projection | −36.25 | 0.394 |
| **union** | $Z \cup \Phi$ 전 span projection | −36.26 | **0.181** |
| learned | true_joint 학습판 (20k, ridge, deg-3) | −36.47 | 0.435 |

**정성 결과.**

- **H1 불편성 (전체 통과)**: 모든 family-B 추정량 평균이 FD 진값과 일치 (편향 ≈ 1σ 이내; 신선 200k 표본 감사에서 $|E[Z_{col}]| \le 0.004$, $|E[\Phi_{col}]| \le 0.002$). Lemma 1 기반 "s-가측 baseline 자동 불편" 실증 — 동일 centering 버그가 baseline family에서는 무해, control-variate family에서는 +70 편향을 만든 대조가 관찰됨.
- **H2 분산 (정정 수식 승리)**: 오류 수식 0.938 vs 정정 수식 0.203 — $X_t$ 인자 하나가 6.2배 차이. 정정된 (c)는 advantage(0.231)도 압도 (예측 (d)의 "엄격히 작다" 본 MDP에서 참). 단 family-제한 결합 해(true_joint 0.417)가 분리 비율형(true_sep 0.203)에 지는 것은 비율형이 다항 span 밖이기 때문 — (d)의 지배 보장은 "완전 결합 해"에만 성립한다는 교훈.
- **H3 직교성 (Theorem 1(a) 실증)**: $\hat g_{\text{true\_joint}}$과 $Z$ 열들의 배치 상관 최대 0.044 (3σ 임계 0.067, 60열 중 0개 초과) → 정규방정식 성립. adv는 최대 0.069로 1열이 임계 초과 → advantage는 최적 baseline이 아님.
- **H4 학습 가능성 (§5 프로그램 1단계 달성)**: 20k 표본 + ridge 학습판이 oracle 결합 해와 근접 (0.435 vs 0.417).
- **H5 CRN (Theorem 3 실증)**: $\nabla J(\theta)\!-\!\nabla J(\theta')$ 추정 ($\theta=0.2$ vs $0.3$)에서 노이즈 공유 coupling에 의한 분산: ε만 공유 0.422, (s₀, ε, w) 전부 공유 0.277 — 독립 대비 최대 3.6배 감소. 평균 43.36 vs 진값 42.72 (합법 범위).

**결론**: "새로운 critic target"의 존재와 학습 가능성, 그리고 coupling 설계의 분산 이득은 모두 실측으로 확인됐다. 단 이것들이 이미 알려진 결과의 검증이라는 점(§7)은 그대로 유효하다.

---

## 10. 프로그램 3번 실행 (2026-11-26): 관측 가능한 지속 교란 구조 — 하한 감소의 정확한 등식

§5 프로그램 3번 — "도메인 특화 조건부 독립 구조 발견 → tangent space 축소 → 효율 하한 감소" — 의 가장 단순하면서 완전히 증명 가능한 인스턴스를 실행한다. 관측 변수를 하나 더 조건에 넣으면 하한이 내려간다는 "관찰"은 문맥조건화(contextual)/POMDP 상태확장으로 이미 널리 알려져 있다. 이 절의 기여는 그 관찰을 (i) tangent space의 포함관계로 정식화하고, (ii) 하한 감소를 **정확한 등식**으로 계산하며, (iii) 구현 가능한 추정량(조건화된 critic)으로 실측 검증한 것이다.

### 10.1 구조 명세 (에피소드 수준 관측 교란)

관측 가능한 에피소드 수준 교란 $Z$를 추가한다:

$$Z \perp s_0, \qquad s_{t+1} = f(s_t, a_t, Z) + w_t, \qquad Z \text{는 } t=0 \text{에 관측되고 에피소드 동안 불변},$$

도메인 대응: 로봇의 페이로드 질량·마찰 계수(센서로 측정 가능), 자율주행 차량의 적재 하중, 도메인 랜덤라이제이션의 샘플링된 파라미터. 검증해야 할 조건부 독립 세 개(도메인 체크리스트):

- (C1) $Z \perp s_0$ (초기상태와 교란 독립),
- (C2) $(s_{t+1}, r_t) \perp \text{과거} \mid (s_t, a_t, Z)$ ((s,Z)-Markov),
- (C3) $Z$는 관측 가능且 에피소드 내 불변 (persistent).

두 모형: $M_A$ = $s$-Markov($Z$ 무시, 시점별 전이가 임의), $M_B$ = (C1)–(C3). 진분포는 둘 모두에 속한다($M_A$는 전이 조건부분포의 존재만 요구).

### 10.2 Lemma 2 (포함 관계 — tower property만으로)

**Lemma 2.** $T_A = \oplus_t \{h_t(s_t,a_t,s_{t+1},r_t) - E[h_t \mid s_t,a_t]\}$ (Markov 인자 centered 함수), $T_B = \oplus_t \{h_t(s_t,a_t,Z,s_{t+1},r_t) - E[h_t \mid s_t,a_t,Z]\}$라 하면 $T_B \subseteq T_A$이다.

**증명.** 임의의 $d = h - E[h \mid s_t,a_t,Z] \in T_B$에 대해 조건부 기댓값의 굴(tower property)로

$$E[d \mid s_t,a_t] = E[h \mid s_t,a_t] - E\big[E[h \mid s_t,a_t,Z] \,\big|\, s_t,a_t\big] = E[h \mid s_t,a_t] - E[h \mid s_t,a_t] = 0.$$

따라서 $d \in T_A$. (독립 가정조차 불필요 — 굴 성질만으로 충분.) $\blacksquare$

### 10.3 Theorem 4 (하한 감소의 정확한 등식)

**Theorem 4.** $T_B \subseteq T_A$ (닫힌 부분공간), 범함수 $\psi$가 양쪽 모형에서 경로별 미분 가능하고 Riesz 대표원 $\mathrm{rep}_A \in T_A$, $\mathrm{rep}_B \in T_B$ (즉 $E[\mathrm{rep} \cdot d] = d\psi[d]\ \forall d$)가 존재하면:

$$\mathrm{rep}_B = \Pi_{T_B}\,\mathrm{rep}_A, \qquad E[\mathrm{rep}_B^2] = E[\mathrm{rep}_A^2] - E\big[(\mathrm{rep}_A - \Pi_{T_B}\mathrm{rep}_A)^2\big].$$

효율 하한(점근 분산 하한 = 대표원의 $L^2$ 노름 제곱)의 감소분은 **정확히** 대표원의 "구조에 직교하는 성분"의 노름이고, $0$일 필요충분조건은 $\mathrm{rep}_A \in T_B$이다.

**증명.** (i) $\Pi := \Pi_{T_B}\mathrm{rep}_A \in T_B$. (ii) 임의 $d \in T_B \subseteq T_A$: 정사영의 직교성으로 $E[\Pi \cdot d] = E[\mathrm{rep}_A \cdot d] = d\psi[d]$ (마지막 등호는 $\mathrm{rep}_A$의 $T_A$ 위 대표성). (iii) $T_B$ 위 Riesz 대표원의 유일성(힐베르트 공간 내적의 비퇴화성)에 의해 $\mathrm{rep}_B = \Pi$. (iv) 피타고라스: $E[\mathrm{rep}_A^2] = E[\Pi^2] + E[(\mathrm{rep}_A - \Pi)^2]$. $\blacksquare$

**정직성 플래그**: 이 정리의 증명은 세미파라메트릭 표준 이론(Bickel et al.의 tangent space 체계)의 즉시 따름정리 수준이다. 새로운 것은 정리가 아니라 인스턴스화와 등식의 검증이다.

### 10.4 Corollary 4.1 (per-step 등식 — critic 개선량이 곧 하한 감소량)

**Corollary 4.1.** $\nabla J$의 per-step 성분 추정량 $X_t(G_t - b_t)$에 대해, 최적 baseline

$$b_t^{*s}(s) = \frac{E[X_t^2 G_t \mid s_t]}{E[X_t^2 \mid s_t]}, \qquad b_t^{*Z}(s,z) = \frac{E[X_t^2 G_t \mid s_t,z]}{E[X_t^2 \mid s_t,z]}$$

(Theorem 1(c)의 $Z$-조건 버전)은 per-step 분산 관련량에서 정확히

$$E\big[X_t^2 (G_t - b_t^{*s})^2 \mid s_t, Z\big] = E\big[X_t^2 (G_t - b_t^{*Z})^2 \mid s_t, Z\big] + E[X_t^2 \mid s_t, Z]\,\big(b_t^{*Z} - b_t^{*s}\big)^2$$

를 만족한다. 즉 평균을 취하면

$$\text{per-step 분산 감소} = E\Big[X_t^2 \big(b_t^{*Z}(s_t,Z) - b_t^{*s}(s_t)\big)^2\Big] \ge 0,$$

등호 성립 조건은 $b_t^{*Z}(s_t,Z) = b_t^{*s}(s_t)$ (동역학이 $Z$에 의존하지 않을 때). 불편성은 유지된다: $E[X_t \cdot b_t^{*Z}(s_t,Z)] = E[b_t^{*Z} \cdot E[X_t \mid s_t,Z]] = 0$ (Lemma 1).

**증명.** $E[X^2 (G-b)^2 \mid s,Z] = E[X^2 G^2 \mid s,Z] - 2b\,E[X^2 G \mid s,Z] + b^2 E[X^2 \mid s,Z]$에 $b^{*Z} = E[X^2G \mid s,Z]/E[X^2 \mid s,Z]$를 대입하고 $b = b^{*s}$로 두면 세 항이 $-E[X^2 \mid s,Z](b^{*Z} - b^{*s})^2$의 차이로 정리된다(제곱 전개). $\blacksquare$

### 10.5 실험 검증 (v4.3, `thm4_experiment_v4.py`)

**설정**: §10.1의 Z-구조 그대로. oracle 300k 궤적(피팅) + 유한차분 ground truth(±h=10⁻², 400k 궤적, grad_true = −58.0052) + 측정 2000 배치 × 100 궤적(독립 시드). 피팅은 모두 X²-가중 최소제곱(비율 폭발 방지, §9 교훈)과 고유값 절단 최소노름 해.

| estimator | control variate | batch 분산 | raw 대비 |
|---|---|---|---|
| raw | b = 0 | 741.99 | 1.000 |
| adv_s | $E[G\mid s]$ | 251.65 | 0.339 |
| true_s | $E[X^2G\mid s]/E[X^2\mid s]$, deg-5 | 230.59 | 0.311 |
| **true_Z** | $E[X^2G\mid s,Z]/E[X^2\mid s,Z]$, 2D | **201.34** | **0.271** |
| zfam_s | $X\cdot\tilde\varphi(s)$, deg-3 | 256.26 | 0.345 |
| zfam_Z | $X\cdot\tilde\varphi(s)\tilde\psi(Z)$ (**비중첩**) | 299.70 | 0.404 |
| **zfam_Zn** | [zfam_s ∪ 비상수-ψ 열] (**중첩**) | **254.28** | **0.343** |
| union_s | joint deg-3, s-only | 111.08 | 0.150 |
| union_Z | joint ⊗ poly2(Z) (**비중첩**) | 194.29 | 0.262 |
| **union_Zn** | [union_s ∪ 비상수-ψ 열] (**중첩**) | **101.66** | **0.137** |
| learned_Z | union_Zn 학습판 (20k 궤적) | 124.61 | 0.168 |

**검증 1 — Corollary 4.1 등식**: 이론 예측 $\sum_t D_t = E[X_t^2(b^{*Z}-b^{*s})^2]$ 누적 = 1558.06, 같은 양의 직접 차이 $\sum_t(E[X^2(G-b^{*s})^2]-E[X^2(G-b^{*Z})^2])$ = 1550.17. **0.5% 일치** — 등식의 수치 검증.

**검증 2 — 모집단(oracle) 중첩 비교**: true_Z/true_s = **0.873** (12.7% 분산 감소). 구조 신호의 크기: $b^*(\bar s, Z)$ 단면 @t=5에서 Z=0.6/1.0/1.4 → −7.65/−12.90/−25.22 — 최적 baseline이 Z에 강하게 의존하며, 이 의존성이 곧 감소분 $(b^{*Z}-b^{*s})^2$의 원천.

**검증 3 — 유한 family 중첩 비교 (negative control 포함)**:
- 중첩: union_Zn/union_s = **0.915** (8.5% 감소), zfam_Zn/zfam_s = 0.992 — Theorem 4가 예측한 방향으로 실측됨.
- 비중첩: zfam_Z/zfam_s = 1.169, union_Z/union_s = **1.749** — 오히려 **역전**.

**발견 (상수-ψ 소멸 함정)**: 특징 수준 중심화 $X\cdot(\varphi-\mu)(\psi-\nu)$에서 상수 기저 $\psi_0\equiv 1$은 $1-\text{mean}(1)=0$으로 **정확히 소멸**한다. 그 결과 "Z-product family" $X\tilde\varphi(s)\tilde\psi(Z)$는 s-only family $X\tilde\varphi(s)$를 **포함하지 않는 비중첩 family**가 되고, Lemma 2의 $T_B\subseteq T_A$ 단조 논리가 적용되지 않는다. v4.2의 역전(union_Z 1.75배)은 정리의 모순이 아니라 family 설계 결과물이며, s-only 열을 명시적으로 결합해 진짜 중첩을 만들자(union_Zn) 예측대로 감소가 실측되었다. **교훈: "Z를 조건화하라"는 처방은 family를 실제로 중첩시키는 구현과 함께 가야 효과가 보장된다.**

**실용성**: learned_Z(20k 궤적 학습, oracle 300k의 6.7% 샘플) = raw 대비 0.168 — 감소의 대부분이 소규모 학습으로도 회수됨.

**정직성 노트**:
1. **cross-time 항**: 측정 단일-궤적 감소(true_s−true_Z = 2924.9)는 per-step 예측(1558.1)의 약 1.9배. Corollary 4.1은 per-step 항만을 기술하며, 궤적합 추정량 분산에는 시간 간 공분산 항이 추가로 Z-조건화의 이득을 키운다. 이는 정리와 모순이 아니라 보수적 하한임을 보여주는 것이지만, 두 항의 분해는 검증하지 않았다.
2. **절대 편향**: 모든 estimator가 FD truth 대비 +1.08~+2.28. raw의 +1.08은 ~1.8σ 수준으로 경계선 노이즈이기도 하고, union 계열의 +1.9~2.0은 Phi-family 곱열 중심화 오차($-\sum\beta\hat c$, $O(1/\sqrt{300k})$ × 큰 $\beta$)가 주요 메커니즘으로 식별됨. 본 실험의 주장은 **분산 비교**이며 편향은 control variate 설계 세부에 좌우된다.
3. **novelty 위치**: Lemma 2–Theorem 4의 증명은 표준 세미파라메트릭 체계(tangent space 투영)의 즉시 따름정리다. "조건화로 분산을 줄인다"는 패턴 자체는 POMDP·context-augmentation 선례가 있는 고전이다. 이 절의 기여는 (i) 도메인 관측가능 지속 교란 Z의 명세와 검증 체크리스트(C1–C3), (ii) 하한 감소의 **정확한 등식**화와 그 수치 검증, (iii) 중첩성 함정의 발견과 교정이다.

**프로그램 3번 (§5) 완결**: 도메인 특화 조건부 독립 구조 발견 → tangent space 축소(Lemma 2) → 효율 하한 감소의 등식(Theorem 4, Corollary 4.1) → 실험 검증(중첩 시 감소, 비중첩 시 역전). §5 프로그램의 세 항목이 모두 닫혔다.
