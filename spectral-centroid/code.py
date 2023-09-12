import numpy as np

def spectral_centroid(spectrum: np.ndarray, samplerate: float):
    n = len(spectrum)
    sum_magnitudes = np.sum(spectrum)
    sum_weighted_magnitudes = np.sum(np.arange(n) * spectrum)
    return 0.5 * samplerate / (n - 1) * sum_weighted_magnitudes / sum_magnitudes
