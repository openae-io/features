import numpy as np

def spectral_centroid(spectrum: np.ndarray, samplerate: float):
    magnitudes = np.abs(spectrum)
    n = len(magnitudes)
    sum_magnitudes = np.sum(magnitudes)
    sum_weighted_magnitudes = np.sum(np.arange(n) * magnitudes)
    return 0.5 * samplerate / (n - 1) * sum_weighted_magnitudes / sum_magnitudes
