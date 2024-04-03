---
title: Spectral rolloff
tags: [spectral]
---

# Spectral rolloff

The $n\%$ spectral roll-off point is defined as the frequency below which $n \%$ of the total energy of the spectrum is contained.
It is computed from the power spectrum $X_p = |X|^2 \in \mathbb{R}^M$.

The $n\%$ roll-off point is estimated by iteratively increasing $r \in [0, M)$ in the following equation until the equation becomes valid:

$$
\sum_{m=0}^{r} X_p[m] \ge \frac{n}{100} \sum_{m=0}^{M-1} X_p[m]
$$

The roll-off frequency $f_{rolloff}$ can be computed from $r$ and the sampling rate $f_s$:

$$
f_{rolloff} = \frac{f_s}{2} \frac{r}{M}
$$

Typical values for $n$ are 95, 90, 75 and 50 %.

## Parameters

| Name      | Description        | Unit | Limits   |
|-----------|--------------------|------|----------|
| `rolloff` | Roll-off point $n$ | %    | [0, 100] |

## References

- Peeters, G. (2004). A large set of audio features for sound description (similarity and classification) in the CUIDADO project. In CUIDADO IST Project Report (Vol. 54).
- Eyben, F. (2016). Real-time Speech and Music Classification by Large Audio Feature Space Extraction. https://doi.org/10.1007/978-3-319-27299-3
