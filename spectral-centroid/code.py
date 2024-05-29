import numpy as np


def spectral_centroid(spectrum: np.ndarray, samplerate: float):
    magnitudes = np.abs(spectrum)
    magnitudes_sum = 0.0
    magnitudes_sum_weighted = 0.0
    for i, magnitude in enumerate(magnitudes):
        magnitudes_sum += magnitude
        magnitudes_sum_weighted += magnitude * i
    bin_centroid = magnitudes_sum_weighted / magnitudes_sum
    return 0.5 * samplerate / (len(magnitudes) - 1) * bin_centroid
