# Internal annotations: 07_assessment.tex

- Author/agent coordination only; not committee text.
- Original source locators are retained below. Refer to the coverage CSV for original questions and review answers.
- Entry numbers refer to the prior expanded source, not the revised file.

- Prior entry 3:

```tex
\noindent\small Source labels: \href{run:doc_support/reconciliation/2026-11-02/SOURCES.md}{reconciliation source map}; \href{run:doc_support/reconciliation/2026-11-02/FIGURE_POINTERS.md}{figure pointers}.\normalsize
```

- Prior entry 9:

```tex
\item Qualify ACU flow evidence; CFD flow at VCU is an uncertain reference, not direct experimental circulation validation. [literature A Sections 10--11]
```

- Prior entry 10:

```tex
\item Temperature report: residuals in K by channel/\allowbreak{}location, channel-wise bias and RMSE, and declared time/\allowbreak{}space aggregation; report flow/\allowbreak{}duty and local heat budgets separately. Retain excluded channels with reasons and a sensitivity route. [MS01: score-policy lesson; Review A Section 10]
```

- Prior entry 14:

```tex
\item \qanchor{G7}\textbf{Numerical reference error versus model discrepancy.} Estimate numerical sensitivity/\allowbreak{}error for the actual target using spatial, temporal, modal and sampling/\allowbreak{}extraction checks.
```

- Prior entry 17:

```tex
\item \textit{Expansion evidence:} S19 Table5; S20 Table3; S29 verification dossier; A\S{}10/\allowbreak{}14. Full answer and unresolved follow-up: G7 in the source-linked coverage register.
```

- Prior entry 27:

```tex
\item Distinguish measurement variability, installed accuracy, model discrepancy and numerical uncertainty. Propagate through steady and transition outputs. [N02--N04; R01; literature A Sections 8, 15]
```

- Prior entry 29:

```tex
\item Separate a scenario envelope, parameter interval and predictive interval; assess uncertainty against the intended output and available case count. Do not turn a few temperature comparisons into a calibrated rare-event probability. [Review A Section 8]
```

- Prior entry 32:

```tex
\item \qanchor{G1}\textbf{Primitive uncertainty and dependence budget.} Start from primitive sources: shared calibration references/\allowbreak{}coefficient errors; channel noise, installation/\allowbreak{}drift/\allowbreak{}time; geometry/\allowbreak{}material/\allowbreak{}property laws; deposited power and secondary/\allowbreak{}ambient boundaries; hidden initial states; learned parameters/\allowbreak{}closure families; numerical error and CFD/\allowbreak{}reference inadequacy; and transfer distortion.\cite{jcgm2020measurementmodels}
```

- Prior entry 35:

```tex
\item \textit{Expansion evidence:} S02/\allowbreak{}S31/\allowbreak{}S32; LIT-003 CQ05; A\S{}8/\allowbreak{}15. Full answer and unresolved follow-up: G1 in the source-linked coverage register.
```

- Prior entry 37:

```tex
\item \qanchor{G2}\textbf{Propagation method and nonlinear failure limits.} Use linear covariance propagation for locally smooth, well-conditioned mappings and joint Monte Carlo for the primary nonlinear parameter/\allowbreak{}boundary/\allowbreak{}discrepancy propagation.\cite{jcgm2011vectorcovariance}
```

- Prior entry 40:

```tex
\item \textit{Expansion evidence:} S02 \S{}5/\allowbreak{}\S{}7.9.4; S31 Eqs3/\allowbreak{}8--10; S04; A\S{}8. Full answer and unresolved follow-up: G2 in the source-linked coverage register.
```

- Prior entry 42:

```tex
\item \qanchor{G3}\textbf{Shared instruments and derived outputs.} Compute secondary duty, loss allocation and inferred primary flow from one shared set of primitive draws/\allowbreak{}covariances.\cite{jcgm2011vectorcovariance,jcgm2020measurementmodels}
```

- Prior entry 45:

```tex
\item \textit{Expansion evidence:} S31/\allowbreak{}S32 \S{}10.5; S29 Eq3; A\S{}8 EQ06/\allowbreak{}\S{}15. Full answer and unresolved follow-up: G3 in the source-linked coverage register.
```

- Prior entry 47:

```tex
\item \qanchor{G4}\textbf{Physical constraints for uncertain operators.} Parameterize or constrain positive capacities/\allowbreak{}conductances and paired exchanges; use energy-consistent signed fluxes and declared closure domains.
```

- Prior entry 50:

```tex
\item \textit{Expansion evidence:} S04; S24 \S{}\S{}3--5; S26/\allowbreak{}S75; S79/\allowbreak{}S80 scoped; A\S{}16. Full answer and unresolved follow-up: G4 in the source-linked coverage register.
```

- Prior entry 52:

```tex
\item \qanchor{G8}\textbf{Real-time inverse acceleration and its limits.} NEMO exploits a problem structure separating nonlinear parameter dependence from linear inversion variables and a reduced inverse representation.
```

- Prior entry 55:

```tex
\item \textit{Expansion evidence:} S05 selected methods \S{}2.1/\allowbreak{}Eqs1--4/\allowbreak{}14; A\S{}3. Full answer and unresolved follow-up: G8 in the source-linked coverage register.
```

- Prior entry 62:

```tex
\item Sensor minima/\allowbreak{}maxima and model-inferred spatial extrema require different evidence; freezing/\allowbreak{}temperature margins require a sourced threshold. [N01; R01]
```

- Prior entry 67:

```tex
\item \qanchor{B5}\textbf{Decision tolerance, measurement resolution and numerical error.} Set operating usefulness from a declared decision or margin, measurement distinguishability from its joint uncertainty, and numerical adequacy from target-specific solver error.
```

- Prior entry 70:

```tex
\item \textit{Expansion evidence:} S32 \S{}6; S75 \S{}3; A\S{}15; RELEASE\_SCOPE.md. Full answer and unresolved follow-up: B5 in the source-linked coverage register.
```

- Prior entry 72:

```tex
\item \qanchor{G5}\textbf{What uncertainty calibration would mean.} Report prediction error/\allowbreak{}bias, residual structure, interval width and proper predictive scores on whole independent cases.\cite{litS75}
```

- Prior entry 75:

```tex
\item \textit{Expansion evidence:} S31 \S{}6.5; S72/\allowbreak{}S73/\allowbreak{}S75; A\S{}8/\allowbreak{}10/\allowbreak{}15. Full answer and unresolved follow-up: G5 in the source-linked coverage register.
```

- Prior entry 77:

```tex
\item \qanchor{G6}\textbf{Extrema, crossing and settling uncertainty.} Propagate joint state/\allowbreak{}closure/\allowbreak{}input/\allowbreak{}reference uncertainty into the complete extremum or event functional, not separate independent point bands.
```

- Prior entry 80:

```tex
\item \textit{Expansion evidence:} S72/\allowbreak{}S75/\allowbreak{}S76 target operators; analyst specification; A\S{}5/\allowbreak{}8/\allowbreak{}14; B\S{}8. Full answer and unresolved follow-up: G6 in the source-linked coverage register.
```

- Prior entry 89:

```tex
\item Retain the planning questions about sensor reliability, loss and evolving installation/\allowbreak{}material conditions as bounded assessment branches. [GP03/\allowbreak{}17/\allowbreak{}26; Review A Sections 5--8]
```

- Prior entry 94:

```tex
\item Connect a residual pattern to an evidence request before promising diagnosis or operator advice. [GP26--GP27; HC12--HC14]
```

- Prior entry editorial:

```tex
\item Fill target/\allowbreak{}reference/\allowbreak{}metric/\allowbreak{}tolerance-symbol/\allowbreak{}runtime table; assign numbers only with an intended-use and evidence basis.
```

- Prior entry editorial:

```tex
\item Retain the planning questions about sensor reliability, loss and evolving installation/\allowbreak{}material conditions as bounded assessment branches.
```

- Prior entry editorial:

```tex
\item \topiclabel{real-time-inverse-acceleration-and-its-limits}\textbf{Real-time inverse acceleration and its limits.} NEMO exploits a problem structure separating nonlinear parameter dependence from linear inversion variables and a reduced inverse representation.
```

- Prior entry editorial:

```tex
\item Check whether a NEMO-type nonlinear/\allowbreak{}linear factorization fits the actual inverse variables and hidden states; keep it an optional comparator, not total model-form UQ.
```
