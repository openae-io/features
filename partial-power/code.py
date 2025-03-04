import math
import numpy as np


def partial_power(
    spectrum: np.ndarray, samplerate: float, fmin: float, fmax: float
) -> float:
    ps = np.abs(spectrum) ** 2
    n = len(ps)
    n_lower = math.floor(2 * n * fmin / samplerate)
    n_upper = math.floor(2 * n * fmax / samplerate)
    return np.sum(ps[n_lower:n_upper]) / np.sum(ps)
