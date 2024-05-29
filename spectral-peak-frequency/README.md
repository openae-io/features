---
title: Spectral peak frequency
tags: [spectral]
---

# Spectral peak frequency

The spectral peak frequency is the frequency at which a signal or a waveform has its highest energy.
It can be computed from the power spectrum $X_p = |X| \in \mathbb{R}^M$.

$$
f_{peak} = \frac{f_s}{2(M - 1)} \cdot \argmax_m X_p[m]
$$

The result is in the range of 0 Hz and the nyquist frequency (half the sampling rate $f_s$).
