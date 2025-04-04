---
title: Clearance factor
tags: [basic]
---

# Clearance factor

The clearance factor is defined as the ratio of the peak amplitude and the squared mean of the square roots of the absolute amplitudes.

$$
\text{ClearanceFactor} = \frac{\max |x|}{(\frac{1}{N} \sum_{i=0}^{N-1}{\sqrt{|x[i]|}})^2}
$$

## Applications

- Fault detection in bearings

  > For rotating machinery, this feature is maximum for healthy bearings and goes on decreasing for defective ball, defective outer race, and defective inner race respectively. The clearance factor has the highest separation ability for defective inner race faults.
  >
  > ⸺ https://de.mathworks.com/help/predmaint/ug/signal-features.html

## References

- https://de.mathworks.com/help/predmaint/ug/signal-features.html
- Sharma, V., & Parey, A. (2016). A Review of Gear Fault Diagnosis Using Various Condition Indicators. Procedia Engineering, 144, 253–263. https://doi.org/10.1016/j.proeng.2016.05.131
