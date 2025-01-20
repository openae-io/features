---
title: Kurtosis
tags: [statistics]
---

# Kurtosis

Kurtosis is a statistical measure that describes the shape of a dataset's probability distribution, with a specific focus on the distribution's tails. It quantifies the degree to which the dataset's distribution differs from the normal distribution (Gaussian distribution or bell curve). Essentially, kurtosis indicates the **tailedness** of the distribution, highlighting the presence and extremity of outliers.

- **High kurtosis**: Indicates heavy tails, meaning more extreme outliers than the normal distribution.
- **Low kurtosis**: Indicates light tails, with fewer extreme outliers.
- **Normal kurtosis**: A kurtosis of 3 corresponds to a normal distribution.

The kurtosis is calculated using the fourth and second central moment:

$$
\text{Kurtosis} = \frac{m_4}{m_2^2} \\
$$

where:

- $m_k$ is the $k$-th central moment:

  $$
  m_k = \frac{1}{N} \sum_{i=0}^{N-1} (x[i] - \overline{x})^k,
  $$

  with $k = 4$ for kurtosis and $k = 2$ for variance.

- $\overline{x}$ is the mean of the dataset:

  $$
  \overline{x} = \frac{1}{N} \sum_{i=0}^{N-1} x[i].
  $$

- $N$ is the number of data points in the dataset.

## References

- https://en.wikipedia.org/wiki/Kurtosis
