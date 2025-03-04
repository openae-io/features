import numpy as np


def spectral_flatness(spectrum: np.ndarray):
    def geometric_mean(x):
        if np.any(x == 0):
            return 0.0
        return np.exp(np.mean(np.log(x)))

    ps = np.abs(spectrum) ** 2
    return geometric_mean(ps) / np.mean(ps)
