---
title: Skewness
tags: [statistics]
---

# Skewness

Skewness is a statistical measure that quantifies the asymmetry of the probability distribution of a dataset. It provides information about the direction and degree of skew (departure from symmetry) in the distribution. Skewness helps us understand whether the data is concentrated more to the left or right of the mean, and it is an important aspect of data analysis and statistics.

The skewness is computed using the third central moment:

$$
\begin{aligned}
\text{Skewness} &= \frac{m_3}{m_2^{3/2}} \\
m_k &= \frac{1}{N} \sum_{i=0}^{N-1}{(x[i] - \overline{x})^k} \\
\overline{x} &= \frac{1}{N} \sum_{i=0}^{N-1}{x[i]}
\end{aligned}
$$

## References

- https://en.wikipedia.org/wiki/Skewness
