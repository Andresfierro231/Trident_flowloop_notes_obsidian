# Internal annotations: 04_model.tex

- Author/agent coordination only; not committee text.
- Original source locators are retained below. Refer to the coverage CSV for original questions and review answers.
- Entry numbers refer to the prior expanded source, not the revised file.

- Prior entry 3:

```tex
\noindent\small Source labels: \href{run:doc_support/reconciliation/2026-11-02/SOURCES.md}{reconciliation source map}; \href{run:doc_support/reconciliation/2026-11-02/FIGURE_POINTERS.md}{figure pointers}.\normalsize
```

- Prior entry 9:

```tex
\item \ranchor{HS01}\textbf{Research insertion: Full-loop physical solver and numerical readiness.} Insert one resolved M1/\allowbreak{}M2/\allowbreak{}M3 input--output example with state ordering, selected cooler/\allowbreak{}flow form, conservation residuals and numerical sensitivity. [HC05]
```

- Prior entry 14:

```tex
\item Divide the loop into axial cells with fluid, pipe and optional insulation temperatures; declare heater, cooler, ambient and axial/\allowbreak{}radial heat paths. [N09; N10]
```

- Prior entry 15:

```tex
\item Explain M0 radial diagnostic, M1 stagnant segmented loop, M2 prescribed signed-flow transport, and M3 coupled buoyancy/\allowbreak{}resistance root. These are distinct from the empirical reduced-zone response family. [N09]
```

- Prior entry 16:

```tex
\item Fill: minimal equations, sign conventions, property choices and conservation ledger; identify source derivation and implementation location. Do not rederive all background theory. [G01: Theory motivation]
```

- Prior entry 17:

```tex
\item Use stored energy and signed enthalpy fluxes as the starting balance; evaluate each shared transfer once with opposite signs for adjacent volumes. Define state, units, positive loop direction and property temperature before presenting the reduced equations. [Review A Section 2, EQ-01--03]
```

- Prior entry 18:

```tex
\item For temperature-dependent heat capacity, use an enthalpy difference obtained by integrating $c_p(T)$; distinguish fluid, pipe and optional insulation storage. A steady M3 algebraic circulation balance does not itself provide transient inertia. [Review A Sections 2--3]
```

- Prior entry 21:

```tex
\item \qanchor{C1}\textbf{State meanings across the physical hierarchy.} A lumped RC model aggregates thermal storage/\allowbreak{}exchange; a segmented conjugate model retains fluid/\allowbreak{}wall/\allowbreak{}insulation and directional enthalpy; a regional grey-box model identifies effective storage/\allowbreak{}couplings; a 1D circulation model adds buoyancy/\allowbreak{}resistance and possibly inertia; a low-order spatial model retains profile/\allowbreak{}mode information.
```

- Prior entry 24:

```tex
\item \textit{Expansion evidence:} S50/\allowbreak{}S52/\allowbreak{}S66/\allowbreak{}S73; LIT-003 AUD09--13; A\S{}2--3/\allowbreak{}11. Full answer and unresolved follow-up: C1 in the source-linked coverage register.
```

- Prior entry 26:

```tex
\item \qanchor{C2}\textbf{Which storage and heat paths are retained?.} Retain paths that carry source, rejection, ambient loss, storage or transport relevant to the target.
```

- Prior entry 29:

```tex
\item \textit{Expansion evidence:} S52 Eqs7--23; S65/\allowbreak{}S66; A\S{}2/\allowbreak{}4/\allowbreak{}13/\allowbreak{}17. Full answer and unresolved follow-up: C2 in the source-linked coverage register.
```

- Prior entry 31:

```tex
\item \qanchor{C3}\textbf{Steady momentum, inertia and transport.} An algebraic steady momentum root supplies a circulation branch, not a transient stability result.
```

- Prior entry 34:

```tex
\item \textit{Expansion evidence:} S54 \S{}5; S55 \S{}\S{}2--4; S57; LIT-003 AUD12--13; A\S{}2.2/\allowbreak{}10. Full answer and unresolved follow-up: C3 in the source-linked coverage register.
```

- Prior entry 43:

```tex
\item Start from attempted master closures, then characterize hydraulic/\allowbreak{}thermal development before choosing transfer-law descriptors. Keep closure selection separate from sensor mapping. [October 14 directions; literature A Sections 4, 13--14]
```

- Prior entry 44:

```tex
\item Compare bulk enthalpy, centerline/\allowbreak{}radial/\allowbreak{}angular fluid temperature and wall/\allowbreak{}contact sensor responses according to their distinct meanings. [G01: Proposed methodology; literature A Section 5]
```

- Prior entry 45:

```tex
\item Treat simple local-to-average ratios as historical candidates; test conditioning and conservation before adopting a universal mapping. [G01 indices 8879--8950, 10284--10431; literature A Section 14]
```

- Prior entry 46:

```tex
\item Write the observation model schematically as $y_k=H_k(x,u,\theta)+b_k+\varepsilon_k$: location/\allowbreak{}footprint and contact or filtering belong in $H_k$, shared calibration in $b_k$, and residual variation in $\varepsilon_k$. Choose those terms from evidence rather than inventing independent noise. [Review A Section 5]\cite{jcgm2020measurementmodels}
```

- Prior entry 47:

```tex
\item If a proposed profile descriptor requires contemporaneous CFD or measured primary temperature, classify that result as conditional reconstruction. An autonomous forward closure must obtain its descriptors from the retained state and allowed inputs. [Review A Sections 1, 14]
```

- Prior entry 50:

```tex
\item \qanchor{B2}\textbf{Bulk, area, transport and local temperature.} Point, centerline, wall and sensor-filtered temperatures need distinct operators.\cite{jcgm2020measurementmodels}
```

- Prior entry 53:

```tex
\item \textit{Expansion evidence:} S32 \S{}6; S21 Eqs5--16; A\S{}5/\allowbreak{}14.2, EQ17--19. Full answer and unresolved follow-up: B2 in the source-linked coverage register.
```

- Prior entry 55:

```tex
\item \qanchor{B4}\textbf{Sensor footprint, wall response and interpolation.} Apply interpolation, sensor footprint, contact conduction and response/\allowbreak{}timing in the forward observation operator before comparing predictions.\cite{jcgm2020measurementmodels}
```

- Prior entry 58:

```tex
\item \textit{Expansion evidence:} S32 \S{}6/\allowbreak{}\S{}10.5; S68--S70; LIT-003 CQ05; A\S{}5/\allowbreak{}15. Full answer and unresolved follow-up: B4 in the source-linked coverage register.
```

- Prior entry 60:

```tex
\item \qanchor{C4}\textbf{Development and correlation applicability.} Choose closures using hydraulic/\allowbreak{}thermal development, source and wall conditions, orientation, property variation, buoyancy and geometry.\cite{reis2024molten}
```

- Prior entry 63:

```tex
\item \textit{Expansion evidence:} S57/\allowbreak{}S60; LIT-004 Ch9/\allowbreak{}14/\allowbreak{}17; A\S{}4/\allowbreak{}13. Full answer and unresolved follow-up: C4 in the source-linked coverage register.
```

- Prior entry 72:

```tex
\item Startup-conditioned trajectories may use measured initial temperatures and supplied later ambient; label that information and do not call it an autonomous forecast. [R04--R05]
```

- Prior entry 73:

```tex
\item CFD-conditioned reconstruction, full-forward ROM prediction and later sensor-updated estimation need separate contracts and scores. [literature A Sections 1, 11]
```

- Prior entry 76:

```tex
\item \qanchor{B1}\textbf{Input, observation and prediction contracts.} For steady prediction supply facility/\allowbreak{}revision, geometry and property laws, source deposition or a source model, cooler inlet/\allowbreak{}flow or an equivalent external boundary model, ambient and declared parameter uncertainty.\cite{litS11}
```

- Prior entry 79:

```tex
\item \textit{Expansion evidence:} S71 Eqs1--5; S75 Eqs1--8; LIT-003 CQ03; A\S{}1/\allowbreak{}11/\allowbreak{}14. Full answer and unresolved follow-up: B1 in the source-linked coverage register.
```

- Prior entry 81:

```tex
\item \qanchor{B3}\textbf{Unobserved hot and cold locations.} Sparse observations alone do not determine arbitrary unobserved hot/\allowbreak{}cold spots.\cite{litS75}
```

- Prior entry 84:

```tex
\item \textit{Expansion evidence:} S72 \S{}2.5; S75 \S{}3.3; S76 Eqs14--17; A\S{}5/\allowbreak{}8/\allowbreak{}14; B\S{}8. Full answer and unresolved follow-up: B3 in the source-linked coverage register.
```

- Prior entry 92:

```tex
\item Explain the model end to end using its resolved configuration and ledgers, as requested in the earlier Moser discussion. [GP10--GP11; HC05; Review A Section 12]
```

- Prior entry 97:

```tex
\item Keep the three temperature roles explicit when evaluating developing-profile additions. [GP12--GP13; HC06--HC07; Review A Sections 5, 14]
```

- Prior entry editorial:

```tex
\item \researchlabel{hs01}\textbf{Research insertion: Full-loop physical solver and numerical readiness.} Insert one resolved M1/\allowbreak{}M2/\allowbreak{}M3 input--output example with state ordering, selected cooler/\allowbreak{}flow form, conservation residuals and numerical sensitivity.
```

- Prior entry editorial:

```tex
\item Explain M0 radial diagnostic, M1 stagnant segmented loop, M2 prescribed signed-flow transport, and M3 coupled buoyancy/\allowbreak{}resistance root. These are distinct from the empirical reduced-zone response family.
```

- Prior entry editorial:

```tex
\item Fill: minimal equations, sign conventions, property choices and conservation ledger; identify source derivation and implementation location. Do not rederive all background theory.
```

- Prior entry editorial:

```tex
\item For temperature-dependent heat capacity, use an enthalpy difference obtained by integrating $c_p(T)$; distinguish fluid, pipe and optional insulation storage. A steady M3 algebraic circulation balance does not itself provide transient inertia.
```

- Prior entry editorial:

```tex
\item Explain M3 steady roots separately from transient momentum and local counterflow; preserve signed-flow/\allowbreak{}zero-flow limits and declare branch/\allowbreak{}stability evidence needed.
```

- Prior entry editorial:

```tex
\item Start from attempted master closures, then characterize hydraulic/\allowbreak{}thermal development before choosing transfer-law descriptors. Keep closure selection separate from sensor mapping.
```

- Prior entry editorial:

```tex
\item Treat simple local-to-average ratios as historical candidates; test conditioning and conservation before adopting a universal mapping.
```

- Prior entry editorial:

```tex
\item Explain the model end to end using its resolved configuration and ledgers, as requested in the earlier Moser discussion.
```
