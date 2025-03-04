---
title: Spectral flatness
tags: [spectral]
---

# Spectral flatness

Spectral flatness is a measure used to quantify how flat or "white" a signal's power spectrum is. It compares the *flatness* of a signal's spectrum to that of a completely flat (white noise) spectrum.
A signal with high spectral flatness appears *noisy*, while a signal with low spectral flatness has more tonal or periodic characteristics.

Spectral flatness is calculated as the ratio of the geometric mean to the arithmetic mean of the power spectrum $X_p = |X|^2 \in \mathbb{R}^M$:

$$
\text{SpectralFlatness}
= \frac{\sqrt[M]{\prod_{m=0}^{M-1} X_p[m]}}{\frac{1}{M} \sum_{m=0}^{M-1} X_p[m]}
= \frac{\exp(\frac{1}{M} \sum_{m=0}^{M-1} \ln X_p[m])}{\frac{1}{M} \sum_{m=0}^{M-1} X_p[m]}
$$

The geometric mean can be alternatively represented as the exponential of the arithmetic mean of the logarithms. The logarithmic method is often preferred as it provides better numerical stability and accuracy, particularly when dealing with very large or small values. Since the logarithm of zero is undefined, any zero values in the dataset must be managed accordingly.

The [inequality of arithmetic and geometric means](https://en.wikipedia.org/wiki/AM%E2%80%93GM_inequality) states, that that the arithmetic mean of non-negative real numbers is greater than or equal to the geometric mean of the same numbers.
Therefore, the spectral flatness will always lie in the range of $[0, 1]$.

## References

- Kim, H.-G., Moreau, N., & Sikora, T. (2006). MPEG-7 audio and beyond: Audio content indexing and retrieval. John Wiley & Sons.
- Peeters, G. (2004). A large set of audio features for sound description (similarity and classification) in the CUIDADO project. In CUIDADO IST Project Report (Vol. 54).
- Eyben, F. (2016). Real-time Speech and Music Classification by Large Audio Feature Space Extraction. https://doi.org/10.1007/978-3-319-27299-3
- https://en.wikipedia.org/wiki/Spectral_flatness
