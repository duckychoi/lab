"""
Theorem 4 (구조 -> 효율 하한 감소) 검증 실험 v4
================================================
구조: 관측 가능한 에피소드 수준 교란 Z (제어 유효성 = 페이로드/마찰 스토리)
  Z ~ U[0.5, 1.5]   에피소드당 1회, 관측 가능, s0과 독립, 시간 불변 (persistent)
  s' = 0.5*s + Z*a + w,   w ~ N(0, 0.2^2)      (폐루프 계수 0.5+0.2Z in [0.6,0.8] 안정)
  r = -(s^2 + a^2),   pi(a|s) = N(theta*s, 0.5^2),  T=20, gamma=1

모형 비교:
  M_A: s-Markov (Z 무시)  vs  M_B: (s,Z)-Markov (Z 조건화)   — T_B ⊆ T_A (Lemma 2)

estimator (모두 불편 — E[X|s,Z]=E[X|s]=0 (Lemma 1)):
  raw       : b = 0
  adv_s     : b(s)   = E[G|s]                          (M_A advantage)
  true_s    : b(s)   = E[X^2 G|s]   / E[X^2|s]         (M_A 최적 decoupled)
  true_Z    : b(s,Z) = E[X^2 G|s,Z] / E[X^2|s,Z]       (M_B 최적 decoupled)  <<< 핵심 비교
  union_s   : joint feature (Z-fam + Phi-fam, s-only, deg3) (M_A 최적 joint)
  union_Z   : joint feature ⊗ poly2(Z)                    (M_B 최적 joint)  <<< 핵심 비교
  learned_Z : union_Z 학습판 (20k, ridge)

이론 예측 (Corollary 4.1, per-step 정확 등식):
  per-step 분산 감소 = E[X^2 (b*_Z - b*_s)^2]  (>= 0)
  -> Σ_t D_t 를 실측 단일-궤적 분산 감소와 대조 (cross-time 항은 별도 보고)

수치 안정화 (v4.1):
  * 비율 피팅 = X^2-가중최소제곱으로 E[X^2 G|·]/E[X^2|·] 를 직접 피팅 (가중 조건부평균)
    -> num/den 분리 피팅의 꼬리 폭발 제거 (초기 버전에서 Z=1.4 단면 1.5e8 관찰됨)
  * 중심화는 특징 수준: Z-family col = X_t*(phi - mu) -> Lemma 1에 의해 정확히 영평균
    (곱열 중심화 X*phi - c_hat 은 c_hat 추정 오차가 beta를 타고 편향 주입 — 초기 버전에서 확인)
  * Phi-family (X 없음): 곱열이므로 곱열 평균 중심화 + 오차는 O(1/sqrt(300k))로 무시 가능

v4.3 — 중첩성 발견:
  * 특징 수준 중심화 X*(phi-mu)*(psi-nu) 에서 상수 기저 psi0=1 은 1-mean(1)=0 으로
    정확히 소멸 -> Z-product family 가 s-only family 를 포함하지 않음 (비중첩).
    => 모집단 단조성(T_B⊆T_A 보장)이 깨져 v4.2의 zfam_Z > zfam_s (1.169x),
       union_Z > union_s (1.749x) 역전은 family 설계 결과물 (정리 모순 아님).
  * 수정: 비상수-psi 열(j>=1)만 남기고 s-only 열을 명시적으로 결합 -> 진짜 중첩 family
    (zfam_Zn, union_Zn). Theorem 4 예측: 중첩 family 에서는 Zn <= s 여야 한다.
  * learned_Z 는 union_Zn 학습판(20k)으로 교체.
"""
import numpy as np
import json
import time

t_start = time.time()
rng = np.random.default_rng(7)

# ---------------- environment ----------------
T = 20
RHO = 0.5
THETA = 0.2
SA = 0.5
SW = 0.2
GAMMA = 1.0
ZLO, ZHI = 0.5, 1.5
DEG_S = 5        # s-only decoupled weighted fits
DEG_ZS = 4       # (s,Z) decoupled weighted fits: s-degree
DEG_ZZ = 2       # (s,Z) decoupled weighted fits: z-degree
DEG_U = 3        # union family s-degree

def rollout(theta, N, rng, s0=None, eps=None, w=None, Z=None):
    if s0 is None: s0 = rng.standard_normal(N)
    if eps is None: eps = rng.standard_normal((N, T))
    if w is None:   w = rng.standard_normal((N, T)) * SW
    if Z is None:   Z = rng.uniform(ZLO, ZHI, N)
    s = np.empty((N, T)); a = np.empty((N, T)); r = np.empty((N, T))
    cur = s0
    for t in range(T):
        act = theta * cur + SA * eps[:, t]
        rew = -(cur ** 2) - act ** 2
        nxt = RHO * cur + Z * act + w[:, t]
        s[:, t] = cur; a[:, t] = act; r[:, t] = rew
        cur = nxt
    G = np.empty((N, T))
    G[:, T - 1] = r[:, T - 1]
    for t in range(T - 2, -1, -1):
        G[:, t] = r[:, t] + GAMMA * G[:, t + 1]
    return s, a, G, Z

def score(s, a, theta):
    return (a - theta * s) * s / SA ** 2

def poly_cols(x, deg):
    z = x / 2.0
    return np.stack([z ** k for k in range(deg + 1)], 1)

def zpoly(Z, deg):
    z = (Z - 1.0) * 2.0           # in [-1, 1]
    return np.stack([z ** k for k in range(deg + 1)], 1)

def basis2(s, Z, deg_s, deg_z):
    Ps = poly_cols(s, deg_s)
    Pz = zpoly(Z, deg_z)
    return (Ps[:, :, None] * Pz[:, None, :]).reshape(s.shape[0], -1)

def eval_poly(coef, x):
    z = x / 2.0
    out = np.zeros_like(x)
    for k, c in enumerate(coef):
        out += c * z ** k
    return out

# ---------- decoupled baselines: X^2-가중 조건부평균 피팅 ----------
def fit_ratio_weighted(theta, s, a, G, Z, deg_s, deg_z, useZ):
    """b*(·) = E[X^2 G|·]/E[X^2|·] 를 X^2-가중 lstsq로 직접 피팅 (비율 폭발 없음)"""
    X = score(s, a, theta)
    coefs = []
    for t in range(T):
        B = basis2(s[:, t], Z, deg_s, deg_z) if useZ else poly_cols(s[:, t], deg_s)
        W = X[:, t] ** 2
        BtW = B * W[:, None]
        K = B.T @ BtW + 1e-9 * np.trace(B.T @ BtW) / B.shape[1] * np.eye(B.shape[1])
        coefs.append(np.linalg.solve(K, BtW.T @ G[:, t]))
    return coefs

def b_matrix_s(coefs, s):
    return np.stack([eval_poly(coefs[t], s[:, t]) for t in range(T)], 1)

def b_matrix_Z(coefs, s, Z, deg_s, deg_z):
    out = np.empty_like(s)
    for t in range(T):
        out[:, t] = basis2(s[:, t], Z, deg_s, deg_z) @ coefs[t]
    return out

# ---------- joint family builders (특징 수준 중심화) ----------
def build_family(s, a, theta, Z, deg, zfam_deg, withX, withZ, cs=None, cz=None, cprod=None):
    """col = X_t*(phi_k(s_t)-cs) [* (psi_j(Z)-cz)]  (withX: Lemma 1로 정확 영평균)
       Phi-family(withX=False): 곱열 평균 중심화, 오차 O(1/sqrt(N_or))
       반환: (행렬, cprod(처음 계산 시))"""
    X = score(s, a, theta)
    if cs is None:
        cs = np.stack([poly_cols(s[:, t], deg).mean(0) for t in range(T)], 0)
    if withZ and cz is None:
        cz = zpoly(Z, zfam_deg).mean(0)
    cols, cprods_used = [], []
    for t in range(T):
        Ps = poly_cols(s[:, t], deg) - cs[t]
        if withZ:
            Pz = zpoly(Z, zfam_deg) - cz
            blk = (Ps[:, :, None] * Pz[:, None, :]).reshape(s.shape[0], -1)
        else:
            blk = Ps
        if withX:
            cols.append(blk * X[:, t][:, None])
        else:
            if cprod is None:
                cp = blk.mean(0)
                cprods_used.append(cp)
            else:
                cp = cprod[t]
            cols.append(blk - cp)
    M = np.concatenate(cols, 1)
    return M, (np.stack(cprods_used, 0) if cprod is None and len(cprods_used) else None)

def solve_union(M, psi0, ridge_rel):
    K = M.T @ M
    lam = ridge_rel * np.trace(K) / K.shape[0]
    return np.linalg.solve(K + lam * np.eye(K.shape[0]), M.T @ psi0)

def solve_trunc(M, psi0, rel=1e-6):
    """고유값 절단 최소노름 해 — 공선 열에 강인 (Gram 대각화, 480x480이라 저렴)"""
    n = M.shape[0]
    K = M.T @ M / n
    w, V = np.linalg.eigh(K)
    keep = w > rel * w.max()
    rhs = M.T @ psi0 / n
    return V[:, keep] @ ((V[:, keep].T @ rhs) / w[keep])   # 절단 방향 외 성분은 0

# ================= 1. oracle sample & truth =================
print("[1] oracle sample (300k) ...")
N_OR = 300_000
s_or, a_or, G_or, Z_or = rollout(THETA, N_OR, rng)
X_or = score(s_or, a_or, THETA)
psi0_or = (X_or * G_or).sum(1)

print("[2] finite-difference ground truth ...")
N_FD, h = 400_000, 1e-2
def J_of(theta, N):
    s, a, G, _ = rollout(theta, N, rng)
    return G[:, 0].mean()
Jp = J_of(THETA + h, N_FD)
Jm = J_of(THETA - h, N_FD)
grad_true = (Jp - Jm) / (2 * h)
print(f"    J(theta±h) = {Jp:.6f}, {Jm:.6f}  ->  grad_true = {grad_true:.6f}")

# ================= 2. decoupled oracle fits + Corollary 4.1 prediction =================
print("[3] decoupled weighted fits: b*(s) deg-5, b*(s,Z) 2D ...")
coef_s = fit_ratio_weighted(THETA, s_or, a_or, G_or, Z_or, DEG_S, None, useZ=False)
coef_Z = fit_ratio_weighted(THETA, s_or, a_or, G_or, Z_or, DEG_ZS, DEG_ZZ, useZ=True)

bs_or = b_matrix_s(coef_s, s_or)
bZ_or = b_matrix_Z(coef_Z, s_or, Z_or, DEG_ZS, DEG_ZZ)
X2_or = X_or ** 2

D_t = (X2_or * (bZ_or - bs_or) ** 2).mean(0)                 # Corollary 4.1 예측
gap_s = (X2_or * (G_or - bs_or) ** 2).mean(0)
gap_Z = (X2_or * (G_or - bZ_or) ** 2).mean(0)
gap_direct = gap_s - gap_Z                                    # 같은 항의 직접 차이 (fit 오차 검증용)

# Z-의존성 진단: s = 평균 상태에서 b*(s,Z) 단면
t_diag = 5
s_mean_t = float(s_or[:, t_diag].mean())
z_probe = np.array([0.6, 1.0, 1.4])
s_probe = np.tile(s_mean_t, (3, T))
b_probe = b_matrix_Z(coef_Z, s_probe, z_probe, DEG_ZS, DEG_ZZ)[:, t_diag]
print(f"    b*(s̄={s_mean_t:.3f}, Z) @t={t_diag}: "
      + ", ".join(f"Z={z:.1f}: {v:.3f}" for z, v in zip(z_probe, b_probe)))
print(f"    Σ_t D_t (예측 per-step 감소)      = {D_t.sum():.5f}")
print(f"    Σ_t [E[X²(G-b_s)²]−E[X²(G-b_Z)²]] = {gap_direct.sum():.5f}")

# ================= 3. union joint fits =================
print("[4] union joint fits (특징 수준 중심화) ...")
Zu_s_raw, _ = build_family(s_or, a_or, THETA, Z_or, DEG_U, 0, True, False)
Ph_s_raw, cp_s = build_family(s_or, a_or, THETA, Z_or, DEG_U, 0, False, False)
Zu_z_raw, _ = build_family(s_or, a_or, THETA, Z_or, DEG_U, 2, True, True)
Ph_z_raw, cp_z = build_family(s_or, a_or, THETA, Z_or, DEG_U, 2, False, True)
M_s = np.concatenate([Zu_s_raw, Ph_s_raw], 1)
M_z = np.concatenate([Zu_z_raw, Ph_z_raw], 1)
print(f"    union_s dim={M_s.shape[1]}, union_Z dim={M_z.shape[1]}")
print(f"    열평균 검증: |E[Z-fam]| <= {np.abs(Zu_z_raw.mean(0)).max():.2e}, "
      f"|E[Phi-fam]| <= {np.abs(Ph_z_raw.mean(0)).max():.2e}")
beta_s = solve_trunc(M_s, psi0_or)
beta_z = solve_trunc(M_z, psi0_or)
# 인구 평균 중심화 상수 (learned critic 과 측정 단계에서 재사용)
cs_or = np.stack([poly_cols(s_or[:, t], DEG_U).mean(0) for t in range(T)], 0)
cz_or = zpoly(Z_or, 2).mean(0)

# Z-family 단독 비교 (Lemma 1로 정확 영평균 — 편향 기계장치 없는 순수 구조 비교)
zfam_s = Zu_s_raw                       # X*phi~(s),       deg3 -> 80열
zfam_Z = Zu_z_raw                       # X*phi~(s)*psi~(Z), deg3 ⊗ poly2 -> 240열 (비중첩!)
beta_zs = solve_trunc(zfam_s, psi0_or)
beta_zZ = solve_trunc(zfam_Z, psi0_or)

# v4.3: 진짜 중첩 family — 비상수-psi 열(j>=1)만 남기고 s-only 열을 명시 결합.
#   per-t 블록 폭 = (DEG_U+1)*(DEG_ZZ+1) = 12, 열 순서 k-major: idx = k*3+j
idx = np.concatenate([[tb * 12 + k * 3 + j
                       for k in range(DEG_U + 1) for j in range(1, DEG_ZZ + 1)]
                      for tb in range(T)])
zfam_Zn = np.concatenate([zfam_s, zfam_Z[:, idx]], 1)          # 80 + 160 = 240열
union_Zn = np.concatenate([Zu_s_raw, Zu_z_raw[:, idx],
                           Ph_s_raw, Ph_z_raw[:, idx]], 1)     # 480열, union_s 포함
beta_zZn = solve_trunc(zfam_Zn, psi0_or)
beta_zn = solve_trunc(union_Zn, psi0_or)
print(f"    중첩 family: zfam_Zn dim={zfam_Zn.shape[1]}, union_Zn dim={union_Zn.shape[1]}")

print("[5] learned_Z critic (20k, union_Zn features, 절단 최소노름) ...")
N_LR = 20_000
s_lr, a_lr, G_lr, Z_lr = rollout(THETA, N_LR, rng)
X_lr = score(s_lr, a_lr, THETA)
psi0_lr = (X_lr * G_lr).sum(1)
Zu_s_lr, _ = build_family(s_lr, a_lr, THETA, Z_lr, DEG_U, 0, True, False, cs=cs_or)
Zu_z_lr, _ = build_family(s_lr, a_lr, THETA, Z_lr, DEG_U, 2, True, True, cs=cs_or, cz=cz_or)
Ph_s_lr, _ = build_family(s_lr, a_lr, THETA, Z_lr, DEG_U, 0, False, False, cs=cs_or, cprod=cp_s)
Ph_lr, _ = build_family(s_lr, a_lr, THETA, Z_lr, DEG_U, 2, False, True, cs=cs_or, cz=cz_or, cprod=cp_z)
Mz_lr = np.concatenate([Zu_s_lr, Zu_z_lr[:, idx], Ph_s_lr, Ph_lr[:, idx]], 1)  # = union_Zn 레이아웃
beta_lz = solve_trunc(Mz_lr, psi0_lr, rel=1e-4)

# ================= 4. measurement batches =================
print("[6] measurement: 2000 batches x 100 trajectories ...")
coef_adv = []
for t in range(T):
    V = poly_cols(s_or[:, t], DEG_S)
    coef_adv.append(np.linalg.lstsq(V, G_or[:, t], rcond=None)[0])

NB, NTR = 2000, 100
keys = ['raw', 'adv_s', 'true_s', 'true_Z', 'zfam_s', 'zfam_Z', 'zfam_Zn',
        'union_s', 'union_Z', 'union_Zn', 'learned_Z']
store = {k: np.empty(NB) for k in keys}
rng2 = np.random.default_rng(99)
for b in range(NB):
    s, a, G, Z = rollout(THETA, NTR, rng2)
    X = score(s, a, THETA)
    XG = X * G
    p0 = XG.sum(1)
    store['raw'][b] = p0.mean()
    b_adv = np.stack([eval_poly(coef_adv[t], s[:, t]) for t in range(T)], 1)
    store['adv_s'][b] = (X * (G - b_adv)).sum(1).mean()
    store['true_s'][b] = (X * (G - b_matrix_s(coef_s, s))).sum(1).mean()
    store['true_Z'][b] = (X * (G - b_matrix_Z(coef_Z, s, Z, DEG_ZS, DEG_ZZ))).sum(1).mean()
    Zu_z, _ = build_family(s, a, THETA, Z, DEG_U, 2, True, True, cs=cs_or, cz=cz_or)
    Ph_z, _ = build_family(s, a, THETA, Z, DEG_U, 2, False, True, cs=cs_or, cz=cz_or, cprod=cp_z)
    Zu_s, _ = build_family(s, a, THETA, Z, DEG_U, 0, True, False, cs=cs_or)
    Ph_s, _ = build_family(s, a, THETA, Z, DEG_U, 0, False, False, cs=cs_or, cprod=cp_s)
    store['union_s'][b] = (p0 - np.concatenate([Zu_s, Ph_s], 1) @ beta_s).mean()
    store['union_Z'][b] = (p0 - np.concatenate([Zu_z, Ph_z], 1) @ beta_z).mean()
    store['learned_Z'][b] = (p0 - np.concatenate([Zu_s, Zu_z[:, idx], Ph_s, Ph_z[:, idx]], 1) @ beta_lz).mean()
    store['zfam_s'][b] = (p0 - Zu_s @ beta_zs).mean()
    store['zfam_Z'][b] = (p0 - Zu_z @ beta_zZ).mean()
    store['zfam_Zn'][b] = (p0 - np.concatenate([Zu_s, Zu_z[:, idx]], 1) @ beta_zZn).mean()
    store['union_Zn'][b] = (p0 - np.concatenate([Zu_s, Zu_z[:, idx], Ph_s, Ph_z[:, idx]], 1) @ beta_zn).mean()

# ================= 5. summary =================
print("[7] summarizing ...")
summary = {'grad_true': float(grad_true), 'pred_per_step_sum': float(D_t.sum()),
           'pred_per_step': D_t.tolist(), 'gap_direct_sum': float(gap_direct.sum()),
           'estimators': {}}
base_var = store['raw'].var()
print(f"\n    grad_true = {grad_true:.4f}")
print(f"    {'estimator':10s} {'mean':>10s} {'bias':>8s} {'var(batch)':>12s} {'ratio_vs_raw':>12s}")
for k in keys:
    est = store[k]
    mean, var = float(est.mean()), float(est.var())
    summary['estimators'][k] = {
        'mean': mean, 'bias_vs_fd': mean - grad_true,
        'var': var, 'var_ratio_vs_raw': var / base_var,
        'single_traj_var': float(var * NTR),
    }
    print(f"    {k:10s} {mean:10.4f} {mean - grad_true:8.4f} {var:12.4e} {var / base_var:12.3f}")

drop_dec = (store['true_s'].var() - store['true_Z'].var()) * NTR
drop_uni = (store['union_s'].var() - store['union_Z'].var()) * NTR
drop_zf = (store['zfam_s'].var() - store['zfam_Z'].var()) * NTR
drop_unin = (store['union_s'].var() - store['union_Zn'].var()) * NTR
drop_zfn = (store['zfam_s'].var() - store['zfam_Zn'].var()) * NTR
print(f"\n    이론 예측  Σ_t D_t                 = {D_t.sum():.5f}  (단일-궤적 분산 감소, per-step 항)")
print(f"    실측 감소   true_s - true_Z        = {drop_dec:.5f}  (cross-time 항 포함)")
print(f"    실측 감소   zfam_s - zfam_Z        = {drop_zf:.5f}  (비중첩 — 단조성 보장 없음)")
print(f"    실측 감소   zfam_s - zfam_Zn       = {drop_zfn:.5f}  (중첩 — 보장됨)")
print(f"    실측 감소   union_s - union_Z      = {drop_uni:.5f}  (비중첩)")
print(f"    실측 감소   union_s - union_Zn     = {drop_unin:.5f}  (중첩 — 보장됨)")
print(f"    Z-효과 크기(참고): true_Z/true_s = {store['true_Z'].var() / store['true_s'].var():.3f}, "
      f"zfam_Z/zfam_s = {store['zfam_Z'].var() / store['zfam_s'].var():.3f}, "
      f"zfam_Zn/zfam_s = {store['zfam_Zn'].var() / store['zfam_s'].var():.3f}, "
      f"union_Z/union_s = {store['union_Z'].var() / store['union_s'].var():.3f}, "
      f"union_Zn/union_s = {store['union_Zn'].var() / store['union_s'].var():.3f}")
print(f"\n done in {time.time() - t_start:.1f}s")

with open('/home/ducky/.cokacdir/workspace/wrbx1oz4/thm4_results.json', 'w') as f:
    json.dump(summary, f, indent=2)
print("saved -> thm4_results.json")
