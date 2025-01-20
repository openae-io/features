---
title: Spectral skewness
tags: [spectral, spectral moments]
---

# Spectral skewness

Spectral skewness is a measure of the asymmetry of the power spectrum around its mean, the [spectral centroid](../spectral-centroid/) $f_{centroid}$. It indicates whether the bulk of the spectral power lies to the left or right of the centroid:
- **Positive skewness**: Indicates a spectrum with a tail extending towards higher frequencies.
- **Negative skewness**: Indicates a spectrum with a tail extending towards lower frequencies.
- **Zero skewness**: Indicates a symmetric spectrum around the centroid.

It is computed from the power spectrum $X_p = |X|^2 \in \mathbb{R}^M$.

$$
\begin{aligned}
\text{SpectralSkewness} &= \frac{m_3}{\sqrt{m_2}^3} \\
m_x  &= \sum_{m=0}^{M-1}{(f(m) - f_{centroid})^x \cdot p(m)} \\
f(i) &= \frac{i \cdot f_s}{2(M - 1)} \\
p(i) &= \frac{X_p[i]}{\sum_{m=0}^{M-1}{X_p[m]}}
\end{aligned}
$$

## References

- https://www.mathworks.com/help/signal/ref/spectralskewness.html
- Peeters, G. (2004). A large set of audio features for sound description (similarity and classification) in the CUIDADO project. In CUIDADO IST Project Report (Vol. 54).
