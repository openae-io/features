import numpy as np


def partial_power(
    spectrum: np.ndarray, samplerate: float, f_lower: float, f_upper: float
) -> float:
    ps = np.abs(spectrum) ** 2
    n = len(ps)
    n_lower = int(2 * n * f_lower / samplerate)
    n_upper = int(2 * n * f_upper / samplerate)
    return np.sum(ps[n_lower:n_upper]) / np.sum(ps)
