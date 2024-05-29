---
title: Spectral variance
tags: [spectral, spectral moments]
---

# Spectral variance

The spectral variance, also known as *spectral spread*, quantifies the spread or dispersion of the spectral content around its center of mass, the [spectral centroid](../spectral-centroid/) $f_{centroid}$.
It is computed from the power spectrum $X_p = |X|^2 \in \mathbb{R}^M$.

$$
\begin{aligned}
SpectralVariance &= \sum_{m=0}^{M-1}{(f(m) - f_{centroid})^2 \cdot p(m)} \\
f(i) &= \frac{i \cdot f_s}{2(M - 1)} \\
p(i) &= \frac{X_p[i]}{\sum_{m=0}^{M-1}{X_p[m]}}
\end{aligned}
$$

## References

- https://www.mathworks.com/help/audio/ref/spectralspread.html
- Peeters, G. (2004). A large set of audio features for sound description (similarity and classification) in the CUIDADO project. In CUIDADO IST Project Report (Vol. 54).
