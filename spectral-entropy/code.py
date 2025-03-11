import numpy as np


def spectral_entropy(spectrum: np.ndarray):
    ps = np.abs(spectrum) ** 2
    ps_sum = np.sum(ps)
    if ps_sum == 0.0:
        return 0.0
    p = ps / ps_sum
    p = p[p != 0]
    return -np.sum(p * np.log2(p)) / np.log2(len(ps))
