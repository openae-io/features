---
title: Spectral kurtosis
tags: [spectral, spectral moments]
---

# Spectral kurtosis

Spectral kurtosis is a measure of the "tailedness" or peakedness of the power spectrum around its mean, the [spectral centroid](../spectral-centroid/) $f_{centroid}$. It indicates how much of the spectrum's power is concentrated in the tails of the distribution compared to the center:

- **High kurtosis**: Indicates a spectrum with heavy tails and a sharp peak (leptokurtic), where spectral energy is concentrated in a few dominant frequencies far from the mean.
- **Low kurtosis**: Indicates a flatter spectrum (platykurtic), where spectral energy is more evenly distributed across frequencies.
- **Normal kurtosis**: A kurtosis value of 3 corresponds to a normal distribution (mesokurtic).

Spectral kurtosis is computed from the power spectrum $X_p = |X|^2 \in \mathbb{R}^M$ using the following formula:

$$
\text{SpectralKurtosis} = \frac{m_4}{m_2^2},
$$

where:

- $m_k$ is the $k$-th central moment of the spectrum:

  $$
  m_k = \sum_{m=0}^{M-1} (f(m) - f_{centroid})^k \cdot p(m),
  $$

- $f(m)$ is the frequency corresponding to bin $m$:

  $$
  f(m) = \frac{m \cdot f_s}{2(M - 1)},
  $$

- $p(m)$ is the normalized power at bin $m$:

  $$
  p(m) = \frac{X_p[m]}{\sum_{k=0}^{M-1} X_p[k]}.
  $$

## References

- https://www.mathworks.com/help/signal/ref/spectralkurtosis.html
- Peeters, G. (2004). A large set of audio features for sound description (similarity and classification) in the CUIDADO project. In CUIDADO IST Project Report (Vol. 54).
