import numpy as np


def _spectral_centroid(spectrum: np.ndarray, samplerate: float):
    magnitudes = np.abs(spectrum)
    sum = 0.0
    sum_weighted = 0.0
    for i, magnitude in enumerate(magnitudes):
        sum += magnitude
        sum_weighted += magnitude * i
    return 0.5 * samplerate / (len(magnitudes) - 1) * (sum_weighted / sum)


def spectral_variance(spectrum: np.ndarray, samplerate: float):
    magnitudes = np.abs(spectrum)
    f_centroid = _spectral_centroid(spectrum, samplerate)
    sum = 0.0
    sum_weighted = 0.0
    for i, magnitude in enumerate(magnitudes):
        f = 0.5 * samplerate / (len(magnitudes) - 1) * i
        sum += magnitude
        sum_weighted += magnitude * (f - f_centroid) ** 2
    return sum_weighted / sum
