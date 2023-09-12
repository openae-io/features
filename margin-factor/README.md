---
title: Margin factor
inputdomain: time
tags: [basic]
---

# Margin factor

The margin factor is defined as the ratio of the peak amplitude and the square mean of square root of absolute values.

$$
{MarginFactor} = \frac{\max |x_i|}{(\frac{1}{N} \sum_{i = 0}^{N}{\sqrt{|x_i|}})^2}
$$

## Applications

- Fault detection in bearings

## References

- Caesarendra, W., & Tjahjowidodo, T. (2017). A Review of Feature Extraction Methods in Vibration-Based Condition Monitoring and Its Application for Degradation Trend Estimation of Low-Speed Slew Bearing. Machines, 5(4), 21. https://doi.org/10.3390/machines5040021

## Code

<<< code.py
