---
title: Spectral entropy
tags: [spectral]
---

# Spectral entropy

The spectral entropy captures the "peakiness" of a spectrum. A spectrum with sharp peaks will have low
entropy while a spectrum with flat distribution will have high entropy. The definition is based on the definition of the Shannon entropy [^1]:

$$
\text{SpectralEntropy} = -\frac{\sum_{m=0}^{M-1}{p[m] \cdot \log_2{p[m]}}}{\log_2{M - 1}}
$$

where:
- $p[m] = \frac{X_p[m]}{\sum_{m=0}^{M-1} X_p[m]}$: The probability mass function (PMF) of the power spectrum $X_p = |X|^2 \in \mathbb{R}^M$,
- $X_p[m]$: The power at frequency bin $m$,
- $M$: The total number of frequency bins.

## Normalization

The entropy is normalized by dividing by $\log_2{M-1}$ to constrain the output to the range $[0, 1]$. This normalization guarantees that the spectral entropy is comparable across different spectra, independent of their resolution. The normalized value of 0 indicates a perfectly deterministic spectrum (e.g., a single peak), while a value of 1 indicates maximum uncertainty (e.g., a flat spectrum).

## Single-pass computation

The entropy is derived from the PMF of the power spectrum $p[m]$. As a result, computing the entropy typically requires two steps: first, calculating the total energy of the power spectrum, $X_{p,sum} = \sum_{m=0}^{M-1}{X_p[m]}$, and second, computing the entropy using the PMF $p[m] = \frac{X_p[m]}{X_{p,sum}}$.

However, the entropy formula can be reformulated to allow for a single-pass computation:

$$
\begin{aligned}
-\sum_{m=0}^{M-1}{p[m]\cdot \log_2{p[m]}}
&= -\sum_{m=0}^{M-1}{\frac{X_p[m]}{X_{p,sum}} \cdot \log_2{\frac{X_p[m]}{X_{p,sum}}}} \\
&= -\sum_{m=0}^{M-1}{\frac{X_p[m]}{X_{p,sum}} \cdot (\log_2{X_p[m]} - \log_2{X_{p,sum}})} \\
&= -\sum_{m=0}^{M-1}{\frac{X_p[m]}{X_{p,sum}} \log_2{X_p[m]}} + \log_2{X_{p,sum}} \cdot \underbrace{\sum_{m=0}^{M-1}{\frac{X_p[m]}{X_{p,sum}}}}_{= 1} \\
&= \log_2{X_{p,sum}} - \frac{1}{X_{p,sum}} \cdot \sum_{m=0}^{M-1}{X_p[m] \cdot \log_2{X_p[m]}}
\end{aligned}
$$

## References

- Misra, H., Ikbal, S., Bourlard, H., & Hermansky, H. (2004). Spectral entropy based feature for robust ASR. 2004 IEEE International Conference on Acoustics, Speech, and Signal Processing, 1. https://doi.org/10.1109/ICASSP.2004.1325955
- Peeters, G. (2004). A large set of audio features for sound description (similarity and classification) in the CUIDADO project. In CUIDADO IST Project Report (Vol. 54).
- Eyben, F. (2016). Real-time Speech and Music Classification by Large Audio Feature Space Extraction. https://doi.org/10.1007/978-3-319-27299-3
- https://en.wikipedia.org/wiki/Entropy_(information_theory)
