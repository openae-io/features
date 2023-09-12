---
title: K-factor
inputdomain: time
tags: [basic]
---

# K-factor

The K-factor is defined as the product of peak amplitude and RMS.

$$
{KFactor} = \max |x_i| \cdot \sqrt{\frac{1}{N} \sum_{i = 0}^{N}{x_i ^ 2}}
$$

## References

- Farrar, C. R., & Worden, K. (2012). Structural health monitoring: a machine learning perspective. John Wiley & Sons.

## Code

<<< code.py
