# Thermal Network Model of an Insulated Fluid Loop

## Mathematical Specification and Code Requirements

---

## 0. Scope

You will write code that does three things, in this order.

**Forward problem.** Given a set of thermal resistances (which may depend on temperature) and a loop flow rate, plus a heater power and an ambient temperature, compute the steady-state temperature of every control volume: fluid, pipe wall, and insulation.

**Stage 1 calibration.** Given many measured *steady states* at different heater powers and ambient temperatures, estimate the thermal resistances and the flow rate by gradient-based optimization.

**Stage 2 calibration.** With those fixed, use measured *transients* (warm-up and cool-down) to estimate the heat capacities.

The forward model is a lumped-parameter thermal resistance network on a structured $(r,z)$ control-volume mesh. One temperature per cell; every energy transfer is a conductance times a temperature difference, plus a directed advective flux if the loop circulates. The conductances themselves may depend on the local temperatures, which is what makes the model both physically correct and identifiable.

---

## 1. The system, geometry, and notation

A closed loop of pipe carries a fluid heated by a heater of known electrical power. The pipe is wrapped in insulation. The only heat sink is the room, at ambient temperature $T_\infty$. The system starts at room temperature; the heater is switched on and the loop warms until the heat lost to the room balances the heater power. Depending on the loop's orientation and heater placement, the fluid may also circulate by natural convection.

### 1.1 Coordinates

Let $z$ be arc length along the loop centerline, $z\in[0,L)$, **periodic**: $z+L\equiv z$. Let $r$ be the radial coordinate measured from the pipe centerline.

| Symbol | Meaning |
|---|---|
| $L$ | total loop centerline length |
| $R_0=0$ | pipe centerline |
| $R_1$ | inner pipe radius (fluid–wall interface) |
| $R_2$ | outer pipe radius (wall–insulation interface) |
| $R_3$ | outer insulation radius (insulation–ambient interface) |

### 1.2 Instrumentation

| Sensor | Count | Location | Measures |
|---|---|---|---|
| **STC** $1$–$12$ | 12 | fluid centerline, $r=0$, at axial positions $z^S_i$ | fluid temperature |
| **PTC** $1$–$6$ | 6 | pipe outer surface, $r=R_2$, at axial positions $z^P_j$ | pipe wall temperature |

All 18 axial positions are given data. Ambient temperature $T_\infty$ and heater power $Q$ are also measured.

The PTCs are the only sensors that see inside the radial heat path. Section 8 shows that this is what makes the fluid-to-wall and wall-to-ambient resistances separately determinable, so their placement matters more than their number suggests.

### 1.3 Three radial layers

The model carries one temperature node per axial cell in each of three layers: **fluid** ($f$), **pipe wall** ($p$), and **insulation** ($s$). The pipe wall node is placed at $r=R_2$ — the reason, and the justification, are in §8.1.

---

## 2. Modeling assumptions

| # | Assumption | Consequence |
|---|---|---|
| A1 | Each control volume is isothermal (lumped). | One unknown temperature per cell. |
| A2 | Heat transfer across each link is $q=G(\Delta T)\,\Delta T$, with $G$ possibly a function of temperature. | Steady problem is **nonlinear**; see §7.4. |
| A3 | Fluid cells exchange energy with their two axial neighbors — by diffusion and by directed advection — and with their own pipe cell. | Cyclic, possibly non-symmetric fluid ring. |
| A4 | Pipe cells have **no** axial coupling to each other. | Pipe block is diagonal. |
| A5 | Insulation cells have **no** axial coupling to each other. | Insulation block is diagonal. |
| A6 | Insulation exchanges heat with ambient only. | Grounds the network. |
| A7 | All heater power enters the fluid. | $\sum_kQ_k=Q$. |
| A8 | The metal wall is radially isothermal, so the pipe node sits at $r=R_2$ and PTC readings are node temperatures directly. | Exact observation operator; see §8.1. |
| A9 | Mass flow $\dot m$ is uniform around the loop and constant in a given steady state. | Continuity in a closed incompressible loop. |
| A10 | Loop curvature is ignored in volume calculations. | Straight-cylinder volumes; see the note on bends in §9.2. |

---

## 3. Mesh generation

### 3.1 Requirement

The mesh is structured in $(r,z)$: the same axial partition at every radius. You need an axial partition of $[0,L)$ into $N$ cells such that every STC and every PTC lies at the **centroid** of some cell, with no gaps or overlaps.

Because the PTCs may not be aligned with the STCs, 12 cells will not generally satisfy both requirements, and $N>12$ will be needed. Additional *radial* cells are a separate, optional refinement covered in §3.4.

### 3.2 Sensor-conforming axial mesh

Let $\mathcal{S}$ be the sorted set of **distinct axial sensor positions**, taken cyclically:

$$\mathcal{S}=\{z^S_1,\dots,z^S_{12}\}\cup\{z^P_1,\dots,z^P_6\}=\{s_1<s_2<\dots<s_P\},\qquad P\le18$$

Cyclic gaps $d_p=s_{p+1}-s_p\pmod L$, with $s_{P+1}\equiv s_1+L$. Assign each position a symmetric half-width

$$h_p=\tfrac12\min(d_{p-1},d_p)$$

**Sensor cell** $p$ spans $[s_p-h_p,\ s_p+h_p]$, so $s_p$ is exactly its centroid. ✓

Where $s_p+h_p<s_{p+1}-h_{p+1}$, insert a **filler cell** spanning the gap, optionally subdivided into $n_{\text{sub}}$ equal cells.

$$N=P+N_{\text{filler}}$$

Store index maps $\kappa_S:\{1..12\}\to\{1..N\}$ and $\kappa_P:\{1..6\}\to\{1..N\}$.

### 3.3 Two favorable sensor arrangements

**Co-located.** If a PTC shares an axial position with an STC, that position appears once in $\mathcal{S}$ and the resulting cell hosts *both* sensors — the fluid node and the pipe node of the same cell. Nothing is lost and $P<18$. This is in fact the most informative single arrangement available, because $R^{fp}$ at that station is then determined directly from $(T^f_k-T^p_k)/q_k$ with no interpolation across cells. If you have any say in future instrumentation, place at least one PTC directly on an STC station.

**Staggered.** If the STCs are uniformly spaced and each PTC sits exactly midway between two of them, the construction gives $P=18$ and $N=18$ with no filler cells and a perfectly uniform mesh.

The trade-off is real: co-location gives the cleanest local radial calibration, staggering gives the best axial coverage. A mixed layout — a few co-located, the rest staggered — is usually the best of both, and the mesh builder handles any layout without modification.

### 3.4 Cell geometry and refinement

Faces $\zeta_{k\pm1/2}$, center $z_k=\tfrac12(\zeta_{k-1/2}+\zeta_{k+1/2})$, width $\Delta z_k$, with $\sum_k\Delta z_k=L$. Neighbor distance $\delta z_{k,k+1}=\tfrac12(\Delta z_k+\Delta z_{k+1})$.

$$V^f_k=\pi R_1^2\Delta z_k,\quad V^p_k=\pi(R_2^2-R_1^2)\Delta z_k,\quad V^s_k=\pi(R_3^2-R_2^2)\Delta z_k$$

Areas used repeatedly: $A_f=\pi R_1^2$ (flow area), $A^{\text{in}}_k=2\pi R_1\Delta z_k$, $A^{\text{out}}_k=2\pi R_3\Delta z_k$.

**Refinement guidance.** Choose $n_{\text{sub}}$ so no cell exceeds about twice the width of its neighbors; large width jumps degrade the axial stencil. Place cell faces at zone boundaries (§9.2) — a cell straddling an elbow and a straight run has an ill-defined conductance. And if the loop circulates, $n_{\text{sub}}$ is not a free choice: see the mesh-convergence requirement in §9.6.

**Optional radial refinement.** The minimum model has three radial layers. To resolve the gradient through the insulation, replace the single insulation node with a series chain at equal-volume radii $R_2=\rho_0<\rho_1<\dots<\rho_{M_s}=R_3$. Nothing structural changes. Get three layers working first.

---

## 4. Unknowns

$$\mathbf{x}=\begin{bmatrix}\mathbf{T}^f\\\mathbf{T}^p\\\mathbf{T}^s\end{bmatrix}\in\mathbb{R}^{3N}$$

Fluid block first, then pipe, then insulation; index by $k$ within each block. Work in **kelvin** internally — radiation terms are wrong in any other unit.

---

## 5. The thermal network

Work with **conductances** $G=1/R$ in W/K. The equations are linear in $G$ at fixed temperature, which makes both the assembly and the inverse problem tractable. Convert to resistances only for reporting.

| Symbol | Count | Connects | Nonlinear? |
|---|---|---|---|
| $G^{ff}_{k,k+1}$ | $N$ | fluid $k$ ↔ fluid $k{+}1$ (cyclic), diffusive | mildly (§9.6) |
| $\dot m$ | 1 | directed advection around the whole ring | via $\dot m(Q)$ (§9.6) |
| $G^{fp}_k$ | $N$ | fluid $k$ ↔ pipe wall $k$ | yes, inner film (§9.5) |
| $G^{ps}_k$ | $N$ | pipe wall $k$ ↔ insulation $k$ | weakly, $k_s(T)$ (§9.4) |
| $G^{s\infty}_k$ | $N$ | insulation $k$ ↔ ambient | **strongly** (§9.3) |

$$\boldsymbol\theta=[\mathbf{G}^{ff};\mathbf{G}^{fp};\mathbf{G}^{ps};\mathbf{G}^{s\infty};\dot m]$$

In the temperature-dependent model $\boldsymbol\theta=\boldsymbol\theta(\mathbf{x},Q;\boldsymbol\varphi)$, where $\boldsymbol\varphi$ is the small vector of physical parameters you actually calibrate (§9).

### Network topology (one axial station, unrolled)

```
        ambient  T∞
            |
         G^s∞_k            ← natural convection + radiation (strongly nonlinear)
            |
   ...   [T^s_k]   ...     insulation node, no axial links
            |
         G^ps_k            ← insulation conduction (weakly nonlinear via k_s(T))
            |
   ...   [T^p_k]   ...     pipe wall node AT r = R2 — this is what a PTC reads
            |
         G^fp_k            ← inner film (nonlinear) + wall conduction
            |
  --G^ff--[T^f_k]--G^ff--  fluid ring, cyclic: symmetric diffusion
      ==> ṁ cp ==>              plus directed advection
            ^
            |
           Q_k
```

---

## 6. Governing equations (steady state)

Heater distribution $Q_k=w_kQ$, $w_k\ge0$, $\sum_kw_k=1$.

Split the signed mass flow into upwind parts, $\dot m^+=\max(\dot m,0)$ and $\dot m^-=\min(\dot m,0)$, and define the **one-sided advective conductances**

$$G^{\text{adv},+}=c_p\,\dot m^+\ \ge0\quad\text{(coefficient on the upstream neighbor)},\qquad G^{\text{adv},-}=c_p\,|\dot m^-|\ \ge0$$

For every $k=1,\dots,N$, indices **mod $N$**:

$$Q_k+\big(G^{ff}_{k-1,k}+G^{\text{adv},+}\big)\big(T^f_{k-1}-T^f_k\big)+\big(G^{ff}_{k,k+1}+G^{\text{adv},-}\big)\big(T^f_{k+1}-T^f_k\big)+G^{fp}_k\big(T^p_k-T^f_k\big)=0 \tag{F$_k$}$$

$$G^{fp}_k\big(T^f_k-T^p_k\big)+G^{ps}_k\big(T^s_k-T^p_k\big)=0 \tag{P$_k$}$$

$$G^{ps}_k\big(T^p_k-T^s_k\big)+G^{s\infty}_k\big(T_\infty-T^s_k\big)=0 \tag{S$_k$}$$

$3N$ equations, $3N$ unknowns. §9.6 derives the advective form and explains why upwinding is the only acceptable discretization here.

**Residual convention.** Throughout the rest of this document, define

$$\mathbf{r}(\mathbf{x})\;=\;\mathbf{A}(\mathbf{x})\,\mathbf{x}-\mathbf{b}$$

which is *minus* the net inflow written above. Setting $\mathbf{r}=\mathbf{0}$ reproduces (F), (P), (S). Fix this sign convention in your code and never flip it — every gradient formula in §11 depends on it.

---

## 7. Assembly and solution

### 7.1 Block form

$$\mathbf{A}\,\mathbf{x}=\mathbf{b},\qquad
\mathbf{A}=\begin{bmatrix}\mathbf{L}^{f}+\mathbf{D}^{fp}&-\mathbf{D}^{fp}&\mathbf{0}\\
-\mathbf{D}^{fp}&\mathbf{D}^{fp}+\mathbf{D}^{ps}&-\mathbf{D}^{ps}\\
\mathbf{0}&-\mathbf{D}^{ps}&\mathbf{D}^{ps}+\mathbf{D}^{s\infty}\end{bmatrix},\qquad
\mathbf{b}=\begin{bmatrix}Q\mathbf{w}\\\mathbf{0}\\T_\infty\mathbf{g}^{s\infty}\end{bmatrix}$$

The fluid-ring operator $\mathbf{L}^{f}$ is cyclic with

$$L^{f}_{k,k-1}=-\big(G^{ff}_{k-1,k}+G^{\text{adv},+}\big),\qquad
L^{f}_{k,k+1}=-\big(G^{ff}_{k,k+1}+G^{\text{adv},-}\big),\qquad
L^{f}_{kk}=-\big(L^{f}_{k,k-1}+L^{f}_{k,k+1}\big)$$

including the corner entries $L^{f}_{1,N}$ and $L^{f}_{N,1}$ that close the loop. **Do not forget the corner entries.** This is the single most common bug in this assembly, and the loop-closure test in §13 exists to catch it.

Note the diagonal is defined as minus the sum of the off-diagonals, so $\mathbf{L}^f$ has **exactly zero row sums** by construction — advection around a closed loop is conservative. Build it this way rather than accumulating terms independently; it makes the global energy balance exact to machine precision.

### 7.2 Properties

**No flow ($\dot m=0$).** $\mathbf{A}$ is a grounded graph Laplacian: symmetric, weakly diagonally dominant with strict dominance in every insulation row (since $G^{s\infty}_k>0$), and irreducible. Therefore symmetric positive definite.

**With flow.** Symmetry is lost, but everything that matters for solvability survives: positive diagonal, non-positive off-diagonals, zero row sums in the ungrounded part, strict dominance from the grounding, and irreducibility. $\mathbf{A}$ is an **irreducibly diagonally dominant M-matrix**, hence nonsingular with $\mathbf{A}^{-1}\ge0$ elementwise.

That non-negative inverse is not a technicality. It is what guarantees $T\ge T_\infty$ everywhere for $Q\ge0$ and rules out spurious oscillations in the temperature profile — precisely the property that central differencing of the advective term would destroy.

Assert in tests: positive diagonal, non-positive off-diagonals, zero row sums of $\mathbf{L}^f$, and — in the $\dot m=0$ mode — symmetry and $\lambda_{\min}>0$.

### 7.3 Linear solve

$3N\approx54$–$108$. Dense LU is fine; sparse if you refine heavily. Keep a branch that uses Cholesky when $\dot m=0$ — roughly half the work, and the no-flow mode is your regression-test path. Never form $\mathbf{A}^{-1}$.

### 7.4 Nonlinear solve — and why it costs almost nothing

Define the tangent conductance of any link carrying $q(\Delta T)=G(\Delta T)\Delta T$:

$$G^{\text{tan}}=\frac{dq}{d\Delta T}=G+\Delta T\frac{dG}{d\Delta T}$$

**Key structural result.** The Jacobian $\mathbf{J}=\partial\mathbf{r}/\partial\mathbf{x}$ is *the same operator*, assembled with $G^{\text{tan}}$ in place of $G$. Every piece of machinery you built — the assembly routine, the factorization, the adjoint solve, the edge-wise gradient formula — carries straight over. The advective coefficients are already linear in $\mathbf{x}$ (with $\dot m$ a function of $Q$, not of temperature), so they enter $\mathbf{J}$ unchanged.

When $\dot m=0$, $\mathbf{J}$ is symmetric. That holds because each nonlinear $G$ depends only on the temperature difference across its own link, and because radiation appears **only on ground edges**, where the partner node is the fixed boundary $T_\infty$. (Surface-to-surface radiation between two *unknown* nodes would break symmetry even at zero flow. Don't add it unless you mean to.)

Useful tangent values:

| Constitutive law | $G$ | $G^{\text{tan}}$ |
|---|---|---|
| Constant | $G_0$ | $G_0$ |
| Natural convection, $q=CA\Delta T^{5/4}$ | $CA\Delta T^{1/4}$ | $\tfrac54G$ |
| Radiation to ambient, $q=\varepsilon\sigma A(T_s^4-T_\infty^4)$ | $\varepsilon\sigma A(T_s^2+T_\infty^2)(T_s+T_\infty)$ | $4\varepsilon\sigma AT_s^3$ |
| Advection (one-sided) | $c_p\dot m^\pm$ | $c_p\dot m^\pm$ |

**Newton:** solve $\mathbf{J}\,\delta\mathbf{x}=-\mathbf{r}(\mathbf{x})$, update $\mathbf{x}\leftarrow\mathbf{x}+\alpha\,\delta\mathbf{x}$ with backtracking on $\|\mathbf{r}\|$. Quadratic convergence, typically 4–6 iterations from a decent guess.

**Picard** (simpler, use it first): freeze $\boldsymbol\theta$ at $\mathbf{x}^{(m)}$, solve the linear system, under-relax with $\omega\approx0.7$. Robust but linear; 10–30 iterations.

**Three practical requirements:**

1. **Initial guess.** Solve the linear model with the §9.7 priors and start from that. Never start from $T_\infty\mathbf{1}$ — the $\Delta T^{1/4}$ terms are singular there.
2. **Regularize the $1/4$ power near zero.** Use $G=C(\Delta T^2+\delta^2)^{1/8}$ with $\delta\approx0.1$ K, or a fixed linear $h$ below $\Delta T<0.5$ K. Without this the Jacobian blows up at low power and Newton diverges.
3. **Continuation in power.** If Newton struggles at high $Q$, ramp: solve at $0.1Q$, use as the guess for $0.2Q$, and so on.

---

## 8. What the data can and cannot determine

Read this before writing §11. It governs the entire inverse problem setup.

### 8.1 The pipe node sits at $R_2$, and this matters

Estimate the Biot number across the metal wall:

$$\mathrm{Bi}=\frac{U_{\text{ext}}\,t_{\text{wall}}}{k_p}\approx\frac{(0.5\ \text{W/m}^2\text{K})(0.003\ \text{m})}{20\ \text{W/mK}}\sim10^{-4}\ \lll\ 0.1$$

The wall is radially isothermal to far better than thermocouple accuracy. So place the pipe node at $r=R_2$ and fold the *entire* wall conduction into $R^{fp}$. Then

$$T^{P,\text{meas}}_j=T^p_{\kappa_P(j)}$$

**exactly**, and the observation operator is a clean selector matrix with no correction term. Do this — it removes a source of modeling error and makes the argument below exact rather than approximate.

### 8.2 The PTCs split the radial chain

Let $q_k$ be the radial heat flow leaving fluid cell $k$. At steady state it is identical through every link of the radial chain, so at a PTC station $k=\kappa_P(j)$:

$$R^{fp}_k=\frac{T^f_k-T^p_k}{q_k},\qquad R^{p\to\infty}_k=\frac{T^p_k-T_\infty}{q_k}$$

and $q_k$ itself follows from the fluid energy balance (F$_k$):

$$q_k=Q_k+\big(G^{ff}_{k-1,k}+G^{\text{adv},+}\big)\big(T^f_{k-1}-T^f_k\big)+\big(G^{ff}_{k,k+1}+G^{\text{adv},-}\big)\big(T^f_{k+1}-T^f_k\big)$$

So the six PTCs give a **direct, local, separate determination of the inner half and the outer half of the radial chain** at those six axial stations. This is the principal value of having them.

Note that $q_k$ depends on the axial transport parameters, so this is not a sensor-by-sensor closed-form extraction — the axial and radial parameters are coupled and must be fit jointly. But the information is there, and it is why §11 fits everything simultaneously rather than in stages.

### 8.3 What remains degenerate, and how nonlinearity breaks it

Within the outer half, steady-state data depends on $R^{ps}$ (insulation conduction) and $R^{s\infty}$ (outer film plus radiation) only through their sum, and $T^s_k$ is unobservable. **In a constant-conductance model this degeneracy is exact and unbreakable.**

Temperature dependence breaks it, because the two paths have different signatures:

- $R^{ps}$ is nearly constant — only the weak $k_s(T)$ drift.
- $R^{s\infty}$ *falls* as the surface heats: $\propto\Delta T^{-1/4}$ from natural convection and $\propto T_s^{-3}$ from radiation.

So the measured $R^{p\to\infty}_j(Q)$ is a decreasing curve whose **high-power asymptote is $R^{ps}$**, with the curvature carrying the film and emissivity parameters. Multi-power data identifies both.

Be honest about conditioning. This split needs a wide power range (at least a factor of four in $Q$, preferably more), well-calibrated thermocouples, and the SVD diagnostic of §11.7 reported alongside the answer. It is genuinely identifiable, but it is the weakest direction in the problem and the first to fall apart under noise.

### 8.4 The linear limit, and the nonlinearity as a diagnostic

If all conductances were constant *and* $\dot m$ were fixed, subtracting $T_\infty$ from (F),(P),(S) would cancel every ambient term, giving

$$\mathbf{x}=T_\infty\mathbf{1}+Q\,\boldsymbol\psi,\qquad\boldsymbol\psi=\mathbf{A}^{-1}[\mathbf{w};\mathbf{0};\mathbf{0}]$$

Two exact invariances: temperature rise proportional to power, and independence from ambient. **Under those invariances, fifty steady-state experiments give exactly as much information as one** — only noise averaging.

Three separate effects break them:

- radiation depends on absolute temperature, killing ambient-independence;
- natural convection gives $q\propto\Delta T^{5/4}$, killing power-proportionality;
- $\dot m$ growing with power (§9.6) redistributes energy differently at each power level.

*The departure from linearity is the entire information content of a multi-power dataset.*

**Required diagnostic, before fitting anything.** Compute the reduced sensitivity

$$s_i(Q,T_\infty)=\frac{T^{S,\text{meas}}_i-T_\infty}{Q}$$

and plot it against $Q$ at fixed $T_\infty$, then against $T_\infty$ at fixed $Q$.

- Flat in $Q$ → the data is in the linear regime; you cannot separate $R^{ps}$ from $R^{s\infty}$, and you should say so rather than reporting a fitted split.
- Decreasing in $Q$ → losses stiffening; convection and radiation parameters are identifiable.
- Sensitive to $T_\infty$ → radiation is contributing; $\varepsilon$ is identifiable.
- Profile *asymmetric about the heater* → the loop is circulating; $\dot m$ is identifiable (§9.6).

This tells you whether your dataset is rich enough before you spend a day on an optimizer.

Keep a `nonlinear=False` flag. The linear model remains valuable as a regression target and as the Stage 1 initial guess.

### 8.5 Parameter counting

$4N+1\ge73$ free conductances against 18 measurements per experiment. Even with the invariances broken, the independent information across $D$ experiments is roughly *18 profile values plus two or three curvature coefficients per sensor* — call it 40–60 well-conditioned numbers under favorable conditions, far fewer under poor ones.

Budget $n_\varphi\lesssim20$. A student who fits 73 free parameters to this data and reports a small residual has fit noise.

---

## 9. Constitutive models and parameterization

### 9.1 Structure

Every conductance is written as **a smooth distributed baseline plus localized corrections**, with all quantities scaled by cell size so the result is mesh-independent:

$$G_k=\underbrace{\hat u_{\zeta(k)}A_k}_{\text{zone baseline}}+\underbrace{\sum_bg_b\Phi_{bk}}_{\text{localized bridges}}$$

$\zeta(k)$ is the zone index of cell $k$; $\Phi_{bk}\in[0,1]$ is the fraction of feature $b$'s axial footprint falling in cell $k$, so $\sum_k\Phi_{bk}=1$. Conductances add in parallel, so this is linear in $g_b$ — convenient for the $\theta$-step of §11.5.

### 9.2 Zones and thermal bridges

**Zones** partition the loop by construction type. A reasonable default: heated section, straight runs, bends and fittings. Each zone gets its own $\hat u$.

**Bridges** are localized penetrations of the insulation at known $z$: pipe supports and hangers, instrument penetrations, valve stems, flange pairs. Their locations come from the as-built drawings, not from the fit — you fit only their strength $g_b$. Group identical supports to share a single $g_b$ rather than fitting each one.

Two geometric notes:

- **Bends.** By Pappus's theorem, a smooth toroidal bend has outer surface area *exactly* $2\pi R_3\times$(centerline length), the same as a straight run. The genuine excess at corners comes from fittings having a larger OD than the pipe, and from insulation over elbows being mitered, oversized, gapped, or compressed. Both are real; both are captured by giving bends their own zone $\hat u$, which will come out higher than the straight runs. Don't try to derive it geometrically.
- **Supports as shunts.** A metal support conducts from the *pipe* to ambient, bypassing the insulation entirely. The faithful model adds a fourth family $G^{p\infty}_k$ in parallel with the whole radial chain, turning the chain into a chain-with-shunt; at steady state only the parallel combination is identifiable unless the shunt's temperature dependence differs from the main path. **Default to the simpler treatment** — bumps in $G^{s\infty}$ at the support locations — and add the explicit shunt only if residuals at PTCs near supports demand it.

### 9.3 Outer surface: natural convection plus radiation

$$G^{s\infty}_k=A^{\text{out}}_k\Big[\underbrace{C_{nc,\zeta(k)}\big(|T^s_k-T_\infty|^2+\delta^2\big)^{1/8}}_{\text{natural convection}}+\underbrace{\varepsilon_{\zeta(k)}\sigma\big(T^{s\,2}_k+T_\infty^2\big)\big(T^s_k+T_\infty\big)}_{\text{radiation, exactly linearized}}\Big]$$

The radiation form is exact, not a $4\varepsilon\sigma\bar T^3$ approximation — use it, it costs nothing.

For a prior on $C_{nc}$, use Churchill–Chu for a horizontal cylinder,

$$\mathrm{Nu}=\left\{0.60+\frac{0.387\,\mathrm{Ra}^{1/6}}{\big[1+(0.559/\mathrm{Pr})^{9/16}\big]^{8/27}}\right\}^2,\qquad\mathrm{Ra}=\frac{g\beta\Delta T(2R_3)^3}{\nu\alpha}$$

evaluated at film temperature, then match $h=\mathrm{Nu}\,k_{\text{air}}/(2R_3)$ to $C_{nc}\Delta T^{1/4}$ at a representative $\Delta T$. Fit $C_{nc}$; don't hard-code Churchill–Chu into the model, since the loop is not a set of isolated horizontal cylinders.

Fitted here: $C_{nc,\zeta}$ and $\varepsilon_\zeta$. These are what the $s_i(Q)$ curvature identifies.

### 9.4 Insulation conduction

$$G^{ps}_k=\frac{2\pi\Delta z_k\,k_s(\bar T_k)}{\ln(r_s/R_2)},\qquad r_s=\sqrt{\tfrac{R_2^2+R_3^2}{2}},\qquad\bar T_k=\tfrac12(T^p_k+T^s_k)$$

with a mildly temperature-dependent conductivity, a real and well-documented effect in fibrous and cellular insulation:

$$k_s(T)=k_{s,0}\big[1+\beta_s(T-T_{\text{ref}})\big]$$

Fit $k_{s,0}$ per zone — this is where variation in insulation density, compression, and moisture shows up. Take $\beta_s$ from the manufacturer datasheet rather than fitting it; it is a weak effect and fitting it will just soak up noise.

$r_s$ is the *equal-volume* mean radius, the correct node location for a lumped annulus. The arithmetic mean introduces a systematic bias in thick insulation.

### 9.5 Inner film and wall

$$R^{fp}_k=\frac{1}{h^{\text{in}}_kA^{\text{in}}_k}+\frac{\ln(R_2/R_1)}{2\pi k_p\Delta z_k},\qquad h^{\text{in}}_k=C_{in}\big(|T^p_k-T^f_k|^2+\delta^2\big)^{1/8}$$

The wall term is small, known, and should not be fitted — compute it from handbook $k_p$ and hold it fixed. Fit $C_{in}$, one value for the whole loop unless residuals say otherwise.

If the loop circulates strongly, the inner film becomes forced-convection rather than natural-convection dominated, and $h^{\text{in}}\propto\dot m^{0.8}$ (Dittus–Boelter) is the better form. Check the internal Reynolds number at the fitted $\dot m$ and switch if $\mathrm{Re}>2300$.

### 9.6 Axial fluid transport: diffusion plus directed advection

Because the losses vary around the loop, the fluid temperature varies around the loop, and that gradient drives axial transport. Two mechanisms, and they behave very differently.

**Diffusive (symmetric).** Molecular conduction plus small-scale buoyant mixing:

$$G^{ff}_{k,k+1}=\frac{A_f}{\delta z_{k,k+1}}\big[k_f+k_{\text{mix}}\big]$$

$k_f$ is known and held fixed; $k_{\text{mix}}$ is fitted.

**Advective (directed).** By continuity (A9) the signed mass flow $\dot m$ is identical at every face. First-order **upwind** flux at face $k+\tfrac12$:

$$F_{k+1/2}=c_p\big(\dot m^+T^f_k+\dot m^-T^f_{k+1}\big)$$

The net advective gain of cell $k$ is $F_{k-1/2}-F_{k+1/2}$, which expands to

$$c_p\dot m^+\big(T^f_{k-1}-T^f_k\big)+c_p|\dot m^-|\big(T^f_{k+1}-T^f_k\big)$$

This is algebraically identical to a pair of **one-sided conductances**: $c_p\dot m^+$ on the upstream link and $c_p|\dot m^-|$ on the downstream link. Assemble it in the same routine as the diffusive terms — the only difference is that you do not mirror the entry into the neighbor's row. That asymmetry is the whole of the flow physics in this model.

**Flow model.**

$$\dot m=\pm\,\dot m_0\left(\frac{Q}{Q_0}\right)^{1/3}$$

The exponent is the classical thermosiphon scaling: for a natural-circulation loop, buoyancy drive balances friction to give $\dot m\propto Q^{1/3}$. Fit $\dot m_0$; fix the sign from loop geometry and heater placement, or determine it by running the fit both ways and keeping the better one. As a check, fit $\dot m$ independently per experiment and see whether the recovered values follow $Q^{1/3}$.

**How $\dot m$ is identified.** Flow carries hot fluid downstream of the heater, making the STC profile asymmetric about it — and that asymmetry is the signal. More directly, the fluid temperature rise across the heated section is

$$\Delta T_{\text{heater}}\approx\frac{Q}{\dot m\,c_p}$$

so the STC-to-STC jump straddling the heater gives $\dot m$ almost in closed form. Use it as the initial guess. If the measured profile is symmetric, $\dot m\approx0$ and you should drop back to the diffusive model rather than fitting a flow the data does not support.

**Numerical diffusion — read this before fitting $k_{\text{mix}}$.**

First-order upwinding adds an artificial diffusivity

$$k_{\text{num},k}=\frac{|\dot m|\,c_p\,\delta z_{k,k+1}}{2A_f}$$

The cell Péclet number is $\mathrm{Pe}_k=|\dot m|c_p\delta z_{k,k+1}/\big[(k_f+k_{\text{mix}})A_f\big]$. With only $N\approx18$–$36$ cells around an entire loop, $\delta z$ is large and $\mathrm{Pe}$ can easily exceed 10, making $k_{\text{num}}$ comparable to or larger than the physical $k_{\text{mix}}$ you are trying to measure.

Two consequences you must handle:

1. The fitted $k_{\text{mix}}$ will be **biased low**, and can come out negative — the scheme is supplying diffusion for free and the optimizer compensates by removing physical diffusion.
2. The fitted value will be **mesh-dependent**. Refine $n_{\text{sub}}$ and it changes. That is the signature of a discretization artifact, not physics.

Do one of the following, and state which:

- Report the total effective diffusivity $k_{\text{mix}}+k_{\text{num}}$ rather than $k_{\text{mix}}$ alone, together with the mesh it was obtained on.
- Refine until $k_{\text{mix}}$ is mesh-converged — increase $n_{\text{sub}}$ until it moves by less than its error bar. Cheapest honest option, and the default recommendation.
- Use deferred correction to second order: assemble with upwind, add the explicit central-minus-upwind difference to the right-hand side, and iterate. Retains the M-matrix and recovers second-order accuracy.

**A mesh-convergence study is mandatory whenever $\dot m\ne0$.** Run the full calibration at $n_{\text{sub}}=1,2,4$ and report the drift in every fitted parameter. Any parameter that moves by more than its error bar is not yet converged.

Central differencing is not an acceptable alternative. At $\mathrm{Pe}>2$ it produces oscillatory temperature fields, destroys the M-matrix property of §7.2, and the monotonicity test will fail.

### 9.7 Prior parameter set

A workable default:

| Parameter | Count | Prior source |
|---|---|---|
| $k_{s,0}$ per zone | 3 | insulation datasheet |
| $C_{nc}$ per zone | 2 | Churchill–Chu |
| $\varepsilon$ (shared) | 1 | jacket material, 0.1 (foil) to 0.9 (painted) |
| $C_{in}$ | 1 | internal natural-convection correlation |
| $k_{\text{mix}}$ | 1 | order-of-magnitude estimate |
| $\dot m_0$ | 1 | $Q/(c_p\Delta T_{\text{heater}})$ from the raw STC jump |
| bridge strengths $g_b$ | 3–6 | grouped supports; 1-D fin estimate |
| **Total $n_\varphi$** | **12–15** | comfortably within the §8.5 budget |

Enforce positivity by optimizing $\log\boldsymbol\varphi$. Hold the sign of $\dot m$ fixed within a run (see §11.3).

---

## 10. Symbol table

| Symbol | Units | Meaning |
|---|---|---|
| $L$, $N$ | m, – | loop length; number of axial cells |
| $z_k,\Delta z_k,\delta z_{k,k+1}$ | m | cell center, width, neighbor spacing |
| $R_1,R_2,R_3$ | m | inner pipe, outer pipe, outer insulation radii |
| $T^f_k,T^p_k,T^s_k$ | K | fluid, pipe wall (at $R_2$), insulation temperatures |
| $T_\infty$, $Q$, $w_k$ | K, W, – | ambient; heater power; heater distribution |
| $G$, $R=1/G$ | W/K, K/W | conductance, resistance |
| $G^{\text{tan}}$ | W/K | tangent conductance, $dq/d\Delta T$ |
| $\dot m$, $c_p$ | kg/s, J/(kg·K) | signed loop mass flow; fluid specific heat |
| $G^{\text{adv},\pm}$ | W/K | one-sided advective conductances, $c_p\dot m^\pm$ |
| $\mathrm{Pe}_k$, $k_{\text{num}}$ | –, W/(m·K) | cell Péclet number; numerical diffusivity |
| $k_p,k_s,k_f,k_{\text{mix}}$ | W/(m·K) | pipe, insulation, fluid, fitted mixing conductivity |
| $C_{nc},C_{in}$ | W/(m²·K⁵ᐟ⁴) | fitted natural-convection coefficients |
| $\varepsilon,\sigma$ | –, W/(m²·K⁴) | emissivity; Stefan–Boltzmann |
| $g_b,\Phi_{bk}$ | W/K, – | thermal bridge strength; footprint weight |
| $C^f_k$ etc., $f_f,f_p,f_s$ | J/K, – | heat capacities; Stage 2 multipliers |
| $\boldsymbol\theta,\boldsymbol\varphi$ | mixed, – | full conductance vector; fitted parameters |
| $\mathbf{H},\boldsymbol\mu$ | –, – | observation operator ($18\times3N$); adjoint variable |

---

## 11. Stage 1 — calibrating resistances and flow from steady-state data

### 11.1 Data and observation operator

Experiments $d=1,\dots,D$ with inputs $u^d=(Q^d,T^d_\infty)$ and

$$\mathbf{y}^d=\big[T^{S,\text{meas}}_1\dots T^{S,\text{meas}}_{12},\ T^{P,\text{meas}}_1\dots T^{P,\text{meas}}_6\big]^\mathsf{T}\in\mathbb{R}^{18}$$

$\mathbf{H}\in\mathbb{R}^{18\times3N}$ is a selector: row $i\le12$ picks $T^f_{\kappa_S(i)}$; row $12+j$ picks $T^p_{\kappa_P(j)}$. By A8 there is no correction term.

**Design the experiment matrix deliberately.** Vary $Q$ over at least a factor of four, *and* vary $T_\infty$ by as much as the room allows — run overnight, or across seasons. Power variation separates insulation conduction from the outer film; ambient variation separates radiation from convection. Neither alone is sufficient.

### 11.2 Objective

$$J(\boldsymbol\varphi)=\tfrac12\sum_{d=1}^{D}\big\|\mathbf{W}\big(\mathbf{H}\mathbf{x}^d(\boldsymbol\varphi)-\mathbf{y}^d\big)\big\|_2^2+\tfrac{\lambda}{2}\big\|\boldsymbol\Gamma(\log\boldsymbol\varphi-\log\boldsymbol\varphi_{\text{prior}})\big\|_2^2$$

$\mathbf{W}=\operatorname{diag}(1/\sigma_i)$ from sensor uncertainties — weight STCs and PTCs by their actual accuracies, which usually differ. $\boldsymbol\Gamma$ pulls toward the §9.7 priors. Choose $\lambda$ by L-curve or cross-validation, not by eye.

### 11.3 Adjoint gradient

Do not use finite differences. Let $\mathbf{r}^d_{\text{data}}=\mathbf{H}\mathbf{x}^d-\mathbf{y}^d$ and let $\mathbf{J}^d$ be the **tangent** operator at the converged solution (§7.4). Solve the adjoint system

$$\big(\mathbf{J}^d\big)^{\!\mathsf{T}}\boldsymbol\mu^d=-\,\mathbf{H}^\mathsf{T}\mathbf{W}^2\mathbf{r}^d_{\text{data}}$$

reusing the factorization Newton just built — with LU, solve with `trans=1`; with $\dot m=0$ and Cholesky, $\mathbf{J}$ is symmetric and no transpose is needed. Either way this is free.

Then, with the §6 sign convention, for any conductance held at its converged value:

$$\boxed{\;\frac{\partial J}{\partial G_{ab}}=\sum_d\big(\mu^d_a-\mu^d_b\big)\big(x^d_a-x^d_b\big)\quad\text{(symmetric internal edge)}\;}$$

$$\boxed{\;\frac{\partial J}{\partial G^{s\infty}_k}=\sum_d\mu^{s,d}_k\big(x^{s,d}_k-T^d_\infty\big)\quad\text{(ground edge)}\;}$$

$$\boxed{\;\frac{\partial J}{\partial\dot m}=c_p\sum_d\sum_k\mu^{f,d}_k\big(x^{f,d}_k-x^{f,d}_{\mathrm{up}(k)}\big)\quad\text{(advection)}\;}$$

with $\mathrm{up}(k)=k-1$ for $\dot m>0$ and $k+1$ for $\dot m<0$. Chain-rule through the parameterization, $\nabla_{\boldsymbol\varphi}J=(\partial\boldsymbol\theta/\partial\boldsymbol\varphi)^\mathsf{T}\nabla_{\boldsymbol\theta}J$.

Two things to get right:

- $\partial\boldsymbol\theta/\partial\boldsymbol\varphi$ is evaluated at **fixed $\mathbf{x}$**. The implicit dependence of $\boldsymbol\theta$ on $\mathbf{x}$ is already accounted for by using $\mathbf{J}$ rather than $\mathbf{A}$ in the adjoint solve. Getting this wrong is the classic error, and the adjoint check in §13 catches it.
- $\partial J/\partial\dot m$ has a **kink at $\dot m=0$** — the upwind direction switches, so the derivative is discontinuous. Don't initialize the optimizer at zero flow, and don't be surprised if a quasi-Newton method stalls when $\dot m$ tries to cross zero. Fit $|\dot m_0|$ with the sign held fixed for the run.

One extra linear solve per experiment gives the full gradient, regardless of $n_\varphi$.

### 11.4 Optimizers and strategy

1. **Fit the linear, no-flow model first** (`nonlinear=False`, $\dot m=0$). Fast and well-behaved; gives a sane $\boldsymbol\varphi_0$.
2. **Add flow**, initialized from the closed-form $\Delta T_{\text{heater}}$ estimate of §9.6.
3. **Then turn on temperature dependence**, warm-started from step 2. Warm-start each Newton solve from the previous optimizer iterate — this typically drops Newton to 2 iterations per objective evaluation.
4. **Levenberg–Marquardt** for $n_\varphi\lesssim20$, or **L-BFGS-B** with box bounds on $\log\boldsymbol\varphi$.
5. **Multiple restarts.** Report the spread. A single converged run says nothing about global optimality.

### 11.5 Alternating least squares (robust fallback)

At *fixed* temperatures the residual is **linear in $\boldsymbol\theta$**, and — with the upwind direction fixed — linear in $\dot m$ as well:

$$\mathbf{A}\mathbf{x}-\mathbf{b}=-\big[\mathbf{M}(\mathbf{x})\boldsymbol\theta+\mathbf{q}\big]$$

with $\mathbf{M}(\mathbf{x})$ built from temperature differences: for a symmetric internal edge $m$ joining $a,b$, $M_{a,m}=x_b-x_a$ and $M_{b,m}=x_a-x_b$; for a ground edge at insulation node $k$, $M_{k,m}=T_\infty-x^s_k$; for the advection column, $M_{k,\dot m}=c_p(x^f_{\mathrm{up}(k)}-x^f_k)$; and $\mathbf{q}=[Q\mathbf{w};\mathbf{0};\mathbf{0}]$.

Alternate: (i) fix $\mathbf{x}$, solve a non-negative linear least-squares problem for $\boldsymbol\varphi$ — globally optimal, no local minima; (ii) fix $\boldsymbol\theta$, forward-solve for $\mathbf{x}$. Repeat.

Converges only to a stationary point, but easy to implement, hard to break, and an excellent initialization for §11.4. Recommended as the first inversion to get working.

### 11.6 Machine-learning framings

**(a) Differentiable physics — recommended.** Implement the forward model in PyTorch or JAX with $\boldsymbol\theta=\exp(\boldsymbol\eta)$ and `linalg.solve`. Autodiff through the solve computes exactly the adjoint of §11.3. Train with L-BFGS or Adam. About 30 lines of model code; use implicit differentiation (`jax.lax.custom_root` or equivalent) to differentiate the Newton loop correctly rather than unrolling it.

**(b) Learned closure.** Where a functional form is genuinely unknown, replace it with a small network *wrapped around a physical scaling*:

$$G^{s\infty}_k=A^{\text{out}}_k\exp\!\big[\mathrm{NN}_\omega\big(\log(T^s_k-T_\infty),\ T_\infty,\ z_k/L\big)\big]$$

Keep it tiny — two layers, 8–16 units. Never let the network output a raw conductance; always multiply by area and exponentiate so positivity and mesh-scaling are structural rather than learned. If the network doesn't beat the parametric form of §9.3 on held-out data, report the parametric result.

**(c) Bayesian calibration.** Priors from §9.7, posterior by NUTS (`numpyro`/`pymc`). Given the conditioning discussion in §8.3, credible intervals are the honest deliverable, and the forward solve is cheap enough to make MCMC feasible.

### 11.7 Validation of the inversion

- **Twin experiment first.** Generate synthetic data from known $\boldsymbol\varphi^\star$, add realistic noise ($\sigma\approx0.5$ K), recover. **Report parameter error $\|\hat{\boldsymbol\varphi}-\boldsymbol\varphi^\star\|$, not data misfit.** Small residual with wrong parameters is the expected failure mode.
- **Power-range sweep.** Repeat the twin study with $Q_{\max}/Q_{\min}\in\{1,2,4,10\}$ and plot recovery error of the $R^{ps}$/$R^{s\infty}$ split against it. This tells you quantitatively what experiment to run.
- **Mesh-convergence sweep** at $n_{\text{sub}}=1,2,4$ whenever $\dot m\ne0$ (§9.6). Mandatory.
- **Identifiability diagnostic.** SVD of $\partial\mathbf{F}/\partial\log\boldsymbol\varphi$ at the solution. Report singular values and condition number. Directions with $\sigma_i/\sigma_1<10^{-3}$ are *not determined by the data*; say so rather than reporting them as fitted values.
- **Error bars.** $\operatorname{Cov}(\hat{\boldsymbol\varphi})\approx(\mathbf{J}^\mathsf{T}\mathbf{W}^2\mathbf{J}+\lambda\boldsymbol\Gamma^\mathsf{T}\boldsymbol\Gamma)^{-1}$.
- **Hold-out by power level**, now meaningful since §8.4's invariance is broken.

---

## 12. Stage 2 — calibrating heat capacities from transient data

Only after Stage 1 has converged and passed §11.7. Freeze $\hat{\boldsymbol\varphi}$.

### 12.1 Transient model

$$\mathbf{C}\frac{d\mathbf{x}}{dt}=-\mathbf{r}(\mathbf{x};Q,T_\infty),\qquad\mathbf{x}(0)=T_\infty\mathbf{1}$$

$$C^f_k=f_f\rho_fc_fV^f_k,\qquad C^p_k=f_p\rho_pc_pV^p_k,\qquad C^s_k=f_s\rho_sc_sV^s_k$$

The unknowns are three **multipliers** $\mathbf{f}=(f_f,f_p,f_s)$, each $O(1)$. Geometry and $\rho c$ are known; the multipliers absorb unknown insulation density and moisture, the heater block's mass, and fittings not in the geometry model. Three parameters against a whole time series is a comfortable problem — resist making it per-cell.

### 12.2 Two exact results that do most of the work

**Early time.** At $t=0$ every temperature equals $T_\infty$, so all transport terms vanish and

$$C^f_k\left.\frac{dT^f_k}{dt}\right|_{t=0^+}=Q_k$$

The initial slope at the STC nearest the heater gives $C^f$ of that cell **directly**, with no reference to any resistance or to the flow rate. Fit a straight line to the first few seconds — specify the required logger sampling rate before running the test.

**Late time.** The final approach decays as $e^{-t/\tau_1}$ with

$$\tau_1\approx\frac{\sum_k\big(C^f_k+C^p_k+C^s_k\big)}{\sum_kG^{f\to\infty}_k}$$

The denominator is known from Stage 1, so the tail time constant gives the **total** heat capacity. Combined with $C^f$ from the early slope, this pins $C^s$.

$C^p$ is typically smallest and poorly identified — expect a wide error bar and report it as such rather than quoting a spuriously precise number.

### 12.3 Prefer cool-down data

Turn the heater off from a converged steady state and record the decay. $Q\equiv0$ exactly, so heater power calibration and heater-block thermal mass drop out of the source term entirely; and the surface sweeps a wide temperature range, independently re-checking the Stage 1 nonlinear parameters. Run both: warm-up for $C^f$ (the early-slope result needs $Q\ne0$), cool-down for the tail.

### 12.4 Numerics

The system is stiff, with three well-separated time scales: fluid cells (seconds), loop transit time $\tau_{\text{loop}}=\rho_fA_fL/|\dot m|$ (seconds to minutes), and insulation (minutes to hours). Use **implicit Euler or BDF2** with a Newton solve per step:

$$\big(\mathbf{C}/\Delta t+\mathbf{J}\big)\delta\mathbf{x}=-\big[\mathbf{C}(\mathbf{x}^{n+1}-\mathbf{x}^n)/\Delta t+\mathbf{r}(\mathbf{x}^{n+1})\big]$$

Same tangent operator; the $\mathbf{C}/\Delta t$ term only strengthens the diagonal. Use adaptive $\Delta t$, or `scipy.integrate.solve_ivp` with `method='BDF'` and an analytic Jacobian. Explicit schemes would need $\Delta t$ of order milliseconds — don't.

### 12.5 Fitting

$$J(\mathbf{f})=\tfrac12\sum_n\big\|\mathbf{W}\big(\mathbf{H}\mathbf{x}(t_n)-\mathbf{y}(t_n)\big)\big\|_2^2$$

Sample $t_n$ **logarithmically**, or the long flat tail contributes thousands of nearly identical residuals and swamps the informative early transient.

With three parameters, finite-difference gradients plus Nelder–Mead or L-BFGS-B are perfectly acceptable; the adjoint-ODE machinery is not worth the implementation cost here. Revisit if you enlarge to per-zone $f_s$.

**Optional joint refit.** Once $\mathbf{f}$ is known, a joint refit of $(\boldsymbol\varphi,\mathbf{f})$ against steady *and* transient data will improve the $R^{ps}$/$R^{s\infty}$ split of §8.3, because the insulation's thermal mass sits physically between those two resistances and its charging dynamics see them separately. This is the one route to breaking that degeneracy without relying on the nonlinearity. Treat it as an extension, not a requirement.

---

## 13. Required unit tests

Automated assertions, not plots you look at.

**Mesh**

| # | Test | Expected |
|---|---|---|
| 1 | Sensor conformity | $\vert z_{\kappa_S(i)}-z^S_i\vert<10^{-10}$ for all STCs; same for PTCs |
| 2 | Closure | $\sum_k\Delta z_k=L$ to machine precision |
| 3 | Co-located sensors | an STC and PTC at the same $z$ map to the same cell, and both remain distinct unknowns |

**Structure, all modes**

| # | Test | Expected |
|---|---|---|
| 4 | Global energy balance | $Q=\sum_kG^{s\infty}_k(T^s_k-T_\infty)$ to $\sim10^{-12}$ relative |
| 5 | Radial monotonicity | $Q>0\Rightarrow T^f_k>T^p_k>T^s_k>T_\infty$ for every $k$ |
| 6 | M-matrix structure | positive diagonal, non-positive off-diagonals, $\mathbf{A}^{-1}\ge0$ elementwise |
| 7 | Ring conservation | rows of $\mathbf{L}^f$ sum to zero to machine precision |
| 8 | Loop closure | cyclically permuting all cell indices permutes the solution identically |
| 9 | Bridge partition | $\sum_k\Phi_{bk}=1$ for every bridge; total added conductance independent of $n_{\text{sub}}$ |

**Linear, no-flow mode**

| # | Test | Expected |
|---|---|---|
| 10 | Zero power | $Q=0\Rightarrow\mathbf{x}=T_\infty\mathbf{1}$ exactly |
| 11 | Ambient shift | $\mathbf{x}(Q,T_\infty+\Delta)=\mathbf{x}(Q,T_\infty)+\Delta\mathbf{1}$ |
| 12 | Power scaling | $\mathbf{x}(2Q)-T_\infty\mathbf{1}=2[\mathbf{x}(Q)-T_\infty\mathbf{1}]$ |
| 13 | Symmetry | $\|\mathbf{A}-\mathbf{A}^\mathsf{T}\|_\infty<10^{-12}$ |
| 14 | Positive definiteness | $\lambda_{\min}(\mathbf{A})>0$ |
| 15 | Uniform limit | uniform $\boldsymbol\theta$ and $\mathbf{w}$ ⟹ all $T^f_k$ equal, all $T^p_k$ equal, all $T^s_k$ equal |

**Advection**

| # | Test | Expected |
|---|---|---|
| 16 | Zero-flow reduction | $\dot m=0$ reproduces the symmetric solver to solver tolerance |
| 17 | Well-mixed limit | as $\dot m\to\infty$, $\max_kT^f_k-\min_kT^f_k\to0$ |
| 18 | Flow reversal | with symmetric geometry and heater, $\dot m\to-\dot m$ mirrors the solution about the heater |
| 19 | No oscillation | fluid profile has exactly one maximum (at or downstream of the heater) and one minimum; no interior spurious extrema |
| 20 | Heater jump | $\Delta T$ across the heated section matches $Q/(\dot mc_p)$ within the numerical-diffusion estimate |
| 21 | Mesh convergence | fitted parameters drift below their error bars from $n_{\text{sub}}=2$ to $4$ |

**Nonlinear mode**

| # | Test | Expected |
|---|---|---|
| 22 | Reduction to linear | constant-$G$ constitutive laws ⟹ nonlinear solver reproduces linear solver |
| 23 | Tangent conductance | $G^{\text{tan}}$ matches a central difference of $q(\Delta T)$ to $10^{-6}$ relative |
| 24 | Jacobian symmetry | at $\dot m=0$, $\|\mathbf{J}-\mathbf{J}^\mathsf{T}\|_\infty<10^{-12}$ at the converged state |
| 25 | Newton convergence rate | $\|\mathbf{r}^{(m+1)}\|\lesssim\|\mathbf{r}^{(m)}\|^2$ near the solution |
| 26 | Nonlinearity is present | $s_i(2Q)<s_i(Q)$ measurably |
| 27 | Low-$\Delta T$ robustness | solver converges at $Q\to0^+$ without the $1/4$-power singularity |

**Inverse and transient**

| # | Test | Expected |
|---|---|---|
| 28 | Adjoint check | analytic gradient matches central difference to $\sim10^{-6}$ relative, including the $\dot m$ component |
| 29 | Twin recovery | noiseless twin data recovers $\boldsymbol\varphi^\star$ to optimizer tolerance |
| 30 | Transient → steady | integrating §12 to $t\to\infty$ reproduces the steady solution |
| 31 | Initial slope | $dT^f_k/dt\vert_{t=0}=Q_k/C^f_k$ to time-integration tolerance |
| 32 | Transient energy | $\int_0^\infty\!\big[Q-\sum_kG^{s\infty}_k(T^s_k-T_\infty)\big]dt=\sum_mC_m(T^{ss}_m-T_\infty)$ |

Tests 4, 7, 8, 23 and 31 catch the highest-frequency bugs. Test 26 catches a subtle and demoralizing failure: a nonlinear model whose parameters happen to sit in a regime where it behaves linearly, making Stage 1 silently unidentifiable. Test 19 is what tells you your advection discretization is sound.

---

## 14. Suggested code structure

```
mesh.py
    build_axial_mesh(L, stc_z, ptc_z, zone_edges, n_sub=1) -> Mesh
        # Mesh: z, dz, dz_face, N, kappa_S, kappa_P, zone_id, Phi
    cell_geometry(mesh, R1, R2, R3) -> Vf, Vp, Vs, A_in, A_out

constitutive.py
    class Constitutive:                        # holds phi
        g_ff(x, mesh)          -> G, dG_dDT    # sec 9.6 diffusive
        mdot(Q)                -> m_signed     # sec 9.6 advective
        g_fp(x, mesh)          -> G, dG_dDT    # sec 9.5
        g_ps(x, mesh)          -> G, dG_dDT    # sec 9.4
        g_sinf(x, T_amb, mesh) -> G, dG_dDT    # sec 9.3
    analytic_prior(geom, props) -> phi_prior   # sec 9.7
    LinearConstitutive(...)                    # constant-G, no flow: test path

network.py
    assemble(mesh, theta, mdot) -> A           # one routine, both modes
    assemble_tangent(mesh, theta_tan, mdot) -> J
    rhs(mesh, theta, Q, w, T_amb) -> b
    peclet(mesh, mdot, k_eff) -> Pe            # report max Pe every solve

solver.py
    solve_steady_linear(mesh, theta, mdot, Q, w, T_amb) -> x
    solve_steady(mesh, con, Q, w, T_amb, x0=None) -> x, J, info
    solve_transient(mesh, con, C, Q_of_t, w, T_amb, t_eval) -> X
    observe(x, mesh) -> y                      # 18-vector

inverse.py
    reduced_sensitivity(data) -> s             # sec 8.4 diagnostic, run FIRST
    mdot_from_heater_jump(data, mesh) -> m0    # sec 9.6 initial guess
    gradient_adjoint(phi, data) -> dJ_dphi     # sec 11.3
    fit_als(data, phi0) -> phi                 # sec 11.5, robust start
    fit_lm(data, phi0, prior, lam) -> phi, info
    identifiability(phi, data) -> svals, cond, cov
    mesh_convergence(data, phi0, n_subs) -> table   # sec 9.6, mandatory
    fit_capacities(phi_hat, transient_data, f0) -> f

tests/
    test_mesh.py, test_structure.py, test_forward_linear.py,
    test_advection.py, test_forward_nonlinear.py,
    test_inverse.py, test_transient.py
```

`assemble` and `assemble_tangent` are the *same function* called with different conductance values. Write it once. Likewise the diffusive and advective contributions go into the same loop over faces — the only difference is whether the entry is mirrored into the neighbor's row.

---

## 15. Milestones

**Phase A — forward model**
1. Mesh builder; tests 1–3.
2. Linear no-flow assembly and solver; tests 4–15. *Do not proceed until all pass.*
3. Upwind advection; tests 16–21, including the first mesh-convergence study.
4. Constitutive layer with analytic priors; sanity-check magnitudes by hand.
5. Newton/Picard nonlinear solver; tests 22–27.

**Phase B — Stage 1 calibration**
6. Twin-experiment data generator with realistic noise and a realistic experiment matrix in $(Q,T_\infty)$.
7. Reduced-sensitivity diagnostic (§8.4) on the twin data — confirm the nonlinearity and any flow asymmetry are visible before trying to fit them.
8. Alternating least squares (§11.5); recover $\boldsymbol\varphi^\star$ from noiseless twin data.
9. Adjoint gradient; test 28; then Levenberg–Marquardt with noisy data.
10. Identifiability analysis, power-range sweep, and mesh-convergence sweep (§11.7). **Deliverable: a written statement of which parameters the data determines and which it does not.**
11. Apply to real steady-state data. Inspect residuals *by sensor location* — a systematic residual at one PTC is a missing thermal bridge, not noise. A systematic residual that flips sign across the heater is a flow-model error.

**Phase C — Stage 2 calibration**
12. Transient solver; tests 30–32.
13. Early-slope and tail-constant estimates of $C^f$ and $\sum C$ (§12.2) as independent checks.
14. Three-multiplier fit against warm-up and cool-down data.
15. Optional joint refit of $(\boldsymbol\varphi,\mathbf{f})$; report whether it improves the $R^{ps}$/$R^{s\infty}$ split.
