---
title: Skewness
tags: [statistics]
---

# Skewness

Skewness is a statistical measure that quantifies the asymmetry of a dataset's probability distribution relative to its mean. It indicates the direction and degree of skew (departure from symmetry) in the distribution, helping to identify whether data values are concentrated more on one side of the mean.

- **Positive skewness**: The distribution has a long tail on the right side (values greater than the mean).
- **Negative skewness**: The distribution has a long tail on the left side (values less than the mean).
- **Zero skewness**: The distribution is symmetric.

The skewness is calculated using the third and second central moment:

$$
\text{Skewness} = \frac{m_3}{\sqrt{m_2}^3},
$$

where:

- $m_k$ is the $k$-th central moment:

  $$
  m_k = \frac{1}{N} \sum_{i=0}^{N-1} (x[i] - \overline{x})^k,
  $$

  with $k = 3$ for skewness and $k = 2$ for variance.

- $\overline{x}$ is the mean of the dataset:

  $$
  \overline{x} = \frac{1}{N} \sum_{i=0}^{N-1} x[i].
  $$

- $N$ is the number of data points in the dataset.

## References

- https://en.wikipedia.org/wiki/Skewness
