import numpy as np


def spectral_peak_frequency(spectrum: np.ndarray, samplerate: float) -> float:
    peak_bin = np.argmax(spectrum**2)
    return 0.5 * samplerate / (len(spectrum) - 1) * peak_bin
