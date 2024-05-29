---
title: Band energy
tags: [spectral]
---

# Band energy

The band energy is defined as the energy in an arbitrary frequency band $[f_l, f_u)$, where $f_l$ and $f_u$ are the lower and upper frequency bounds of the band.

$$
\begin{aligned}
{BandEnergy} &= \sum_{m=m_l}^{m_u - 1} X_p[m] \\
X_p &= |X|^2 \\
m_l &= \lfloor M \frac{f_l}{2f_s} \rfloor \\
m_u &= \lfloor M \frac{f_u}{2f_s} \rfloor
\end{aligned}
$$

Where $m \in [0, M)$ is the bin index of the spectrum $X$ and the power spectrum $X_p$.

## References

- Eyben, F. (2016). Real-time Speech and Music Classification by Large Audio Feature Space Extraction. https://doi.org/10.1007/978-3-319-27299-3
