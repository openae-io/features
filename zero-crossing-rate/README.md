---
title: Zero-crossing rate
tags: [basic]
---

# Zero-crossing rate

The zero-crossing rate (ZCR) is the rate at which a signal changes from positive to zero to negative or from negative to zero to positive.

The ZCR is computed by counting the zero crossings and converting it to a rate in Hz using the sampling rate $f_s$.

$$
\begin{aligned}
{ZCR} &= \frac{f_s}{N} \sum_{i=1}^{N-1}{|p(x[i]) - p(x_{i - 1})|} \\
p(x) &= \begin{cases}
1 & x \geq 0 \\
0 & x < 0
\end{cases}
\end{aligned}
$$

## References

- https://en.wikipedia.org/wiki/Zero-crossing_rate
- Kim, H.-G., Moreau, N., & Sikora, T. (2006). MPEG-7 audio and beyond: Audio content indexing and retrieval. John Wiley & Sons.
