import numpy as np


def _spectral_centroid(spectrum: np.ndarray, samplerate: float):
    ps = np.abs(spectrum) ** 2
    ps_sum = 0.0
    ps_sum_weighted = 0.0
    for i, magnitude in enumerate(ps):
        ps_sum += magnitude
        ps_sum_weighted += magnitude * i
    return 0.5 * samplerate / (len(ps) - 1) * (ps_sum_weighted / ps_sum)


def spectral_variance(spectrum: np.ndarray, samplerate: float):
    f_centroid = _spectral_centroid(spectrum, samplerate)
    ps = np.abs(spectrum) ** 2
    ps_sum = 0.0
    ps_sum_weighted = 0.0
    for i, magnitude in enumerate(ps):
        f = 0.5 * samplerate / (len(ps) - 1) * i
        ps_sum += magnitude
        ps_sum_weighted += magnitude * (f - f_centroid) ** 2
    return ps_sum_weighted / ps_sum
