---
title: Spectral kurtosis
tags: [spectral, spectral moments]
---

# Spectral kurtosis

Spectral kurtosis is a measure of the "tailedness" or peakedness of the power spectrum around its mean, the [spectral centroid](../spectral-centroid/) $f_{centroid}$. It indicates how much of the spectrum's power is concentrated in the tails of the distribution compared to the center:

- **High kurtosis**: Indicates a distribution with heavy tails and a sharp peak (leptokurtic). This suggests that the spectral energy is concentrated in a few frequencies with significant deviations from the mean.
- **Low kurtosis**: Indicates a flatter distribution (platykurtic). This suggests that the spectral energy is more evenly spread across frequencies.
- **Normal kurtosis** (value of 3): Indicates a normal distribution (mesokurtic).

It is computed from the power spectrum $X_p = |X|^2 \in \mathbb{R}^M$.

$$
\begin{aligned}
SpectralSkewness &= \frac{m_4}{\sqrt{m_2}^4} \\
m_x  &= \sum_{m=0}^{M-1}{(f(m) - f_{centroid})^x \cdot p(m)} \\
f(i) &= \frac{i \cdot f_s}{2(M - 1)} \\
p(i) &= \frac{X_p[i]}{\sum_{m=0}^{M-1}{X_p[m]}}
\end{aligned}
$$

## References

- https://www.mathworks.com/help/signal/ref/spectralkurtosis.html
- Peeters, G. (2004). A large set of audio features for sound description (similarity and classification) in the CUIDADO project. In CUIDADO IST Project Report (Vol. 54).
