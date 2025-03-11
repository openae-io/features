---
title: Spectral centroid
tags: [spectral, spectral moments]
---

# Spectral centroid

The centroid frequency of a spectrum indicates where the center of mass of the spectrum is located.
The spectral centroid is commonly associated as a measure of the brightness of a sound.

The spectral centroid is calculated from the power spectrum $X_p = |X|^2 \in \mathbb{R}^M$ using the following formula:

$$
f_{centroid} = \frac{f_s}{2(M - 1)} \cdot \frac{\sum_{m=0}^{M-1} X_p[m] \cdot m}{\sum_{m=0}^{M-1} X_p[m]},
$$

where:

- $X_p[m]$ is the power at frequency bin $m$,
- $M$ is the total number of frequency bins,
- $f_s$ is the sampling rate of the signal.

The result lies within the range of $0$ Hz to the Nyquist frequency, which is $f_s / 2$.


## References

- https://en.wikipedia.org/wiki/Spectral_centroid
- Peeters, G. (2004). A large set of audio features for sound description (similarity and classification) in the CUIDADO project. In CUIDADO IST Project Report (Vol. 54).
