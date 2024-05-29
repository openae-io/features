import numpy as np


def spectral_centroid(spectrum: np.ndarray, samplerate: float):
    ps = np.abs(spectrum) ** 2
    ps_sum = 0.0
    ps_sum_weighted = 0.0
    for i, magnitude in enumerate(ps):
        ps_sum += magnitude
        ps_sum_weighted += magnitude * i
    return 0.5 * samplerate / (len(ps) - 1) * (ps_sum_weighted / ps_sum)
