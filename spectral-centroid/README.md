---
title: Spectral centroid
tags: [spectral, spectral moments]
---

# Spectral Centroid

The centroid frequency of a spectrum indicates where the center of mass of the spectrum is located.
It is commonly associated with the measure of the brightness of a sound.

$$
\begin{aligned}
f_{centroid} &= \frac{f_s}{2(M - 1)} \frac{\sum_{m=0}^{M-1}{X_m[m] \cdot i}}{\sum_{m=0}^{M-1}{X_m[m]}} \\
X_m &= |X|
\end{aligned}
$$

Where $X_m[m]$ is the magnitude corresponding to bin $m \in [0, M)$ in the DFT spectrum.
The result is in the range of 0 Hz and the nyquist frequency (half the sampling rate $f_s$).

## References

- https://en.wikipedia.org/wiki/Spectral_centroid
