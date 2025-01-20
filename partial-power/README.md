---
title: Partial power
tags: [spectral]
---

# Partial power

Partial power quantifies the proportion of energy within a specified frequency band $[f_l, f_u)$ relative to the total energy. It is also known as the *band energy ratio*.
The frequency band is defined by its lower ($f_l$) and upper ($f_u$) frequency bounds.

$$
\text{PartialPower} = \frac{\sum_{m=m_l}^{m_u - 1} {X_p}[m]}{\sum_{m=0}^{M-1} {X_p}[m]},
$$

where:

- $X_p = |X|^2$ is the power spectrum,
- $M$ is the total number of bins,
- $m_l = \lfloor M \frac{f_l}{2f_s} \rfloor$ is the lower bin index corresponding to $f_l$,
- $m_u = \lfloor M \frac{f_u}{2f_s} \rfloor$ is the upper bin index corresponding to $f_u$,
- $m \in [0, M)$ represents the spectral bin indices.

## Parameters

| Name      | Description           | Unit  | Limits               |
|-----------|-----------------------|-------|----------------------|
| `lower`   | Lower frequency bound | Hz    | [0, $\frac{f_s}{2}$] |
| `upper`   | Upper frequency bound | Hz    | [0, $\frac{f_s}{2}$] |

## References

- Eyben, F. (2016). Real-time Speech and Music Classification by Large Audio Feature Space Extraction. https://doi.org/10.1007/978-3-319-27299-3
- Sause, M. G. R. (2016). In Situ Monitoring of Fiber-Reinforced Composites: Theory, Basic Concepts, Methods, and Applications (Vol. 242). Springer. https://doi.org/10.1007/978-3-319-30954-5
