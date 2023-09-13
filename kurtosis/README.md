---
title: Kurtosis
tags: [statistics]
---

# Kurtosis

Kurtosis is a statistical measure that describes the shape of the probability distribution of a dataset, specifically focusing on the tails of the distribution. It quantifies how much a dataset's distribution deviates from the normal distribution (also known as the Gaussian distribution or bell curve). In essence, kurtosis provides information about the _tailedness_ or the presence of outliers in the data.

The kurtosis is computed using the fourth central moment:

$$
\begin{aligned}
{Kurtosis} &= \frac{m_4}{m_2^2} \\
m_k &= \frac{1}{N} \sum_{i=0}^{N-1}{(x[i] - \overline{x})^k} \\
\overline{x} &= \frac{1}{N} \sum_{i=0}^{N-1}{x[i]}
\end{aligned}
$$

## References

- https://en.wikipedia.org/wiki/Kurtosis

## Code

<<< code.py
