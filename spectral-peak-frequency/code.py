import numpy as np


def spectral_peak_frequency(spectrum: np.ndarray, samplerate: float) -> float:
    peak_index = np.argmax(spectrum**2)
    return 0.5 * samplerate * peak_index / (len(spectrum) - 1)
