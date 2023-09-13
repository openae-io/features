---
title: Spectral centroid
tags: [spectral, spectral moments]
---

# Spectral Centroid

The centroid frequency of a spectrum indicates where the center of mass of the spectrum is located.
It is commonly associated with the measure of the brightness of a sound.

$$
{SpectralCentroid} = \frac{f_s}{2(n - 1)} \frac{\sum_{i=0}^{N-1}{i S_i}}{\sum_{i=0}^{N-1}{S_i}} 
$$

Where $S_i$ is the amplitude corresponding to bin $i$ in the DFT spectrum.
The result is in the range of 0 Hz and the nyquist frequency (half the sampling rate $f_s$).

## References

- https://en.wikipedia.org/wiki/Spectral_centroid

## Code

<<< code.py
