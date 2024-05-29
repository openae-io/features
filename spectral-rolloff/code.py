import numpy as np


def spectral_rolloff(spectrum: np.ndarray, samplerate: float, rolloff: int):
    magnitudes = np.abs(spectrum)
    magnitudes_sum_rolloff = (rolloff / 100) * np.sum(magnitudes)
    magnitudes_sum = 0.0
    for i, magnitude in enumerate(magnitudes):
        magnitudes_sum += magnitude
        if magnitudes_sum >= magnitudes_sum_rolloff:
            return 0.5 * samplerate / (len(magnitudes) - 1) * i
    return 0.5 * samplerate
