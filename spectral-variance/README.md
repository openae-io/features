---
title: Spectral variance
tags: [spectral, spectral moments]
---

# Spectral variance

Spectral variance, also known as **spectral spread**, quantifies the dispersion or spread of the spectral content around its *center of mass*, the [spectral centroid](../spectral-centroid/) $f_{centroid}$.

The spectral variance is computed from the power spectrum $X_p = |X|^2 \in \mathbb{R}^M$ using the following formula:

$$
\text{SpectralVariance} = \sum_{m=0}^{M-1} (f(m) - f_{centroid})^2 \cdot p(m),
$$

where:

- $f(m)$ is the frequency corresponding to bin $m$:

  $$
  f(m) = \frac{m \cdot f_s}{2(M - 1)},
  $$

- $p(m)$ is the normalized power at bin $m$:

  $$
  p(m) = \frac{X_p[m]}{\sum_{m=0}^{M-1} X_p[m]}.
  $$

## References

- https://www.mathworks.com/help/audio/ref/spectralspread.html
- Peeters, G. (2004). A large set of audio features for sound description (similarity and classification) in the CUIDADO project. In CUIDADO IST Project Report (Vol. 54).
