import numpy as np

def spectral_rolloff(spectrum: np.ndarray, samplerate: float, rolloff: int):
    magnitudes = np.abs(spectrum)
    n = len(magnitudes)
    magnitudes_cumsum = np.cumsum(magnitudes)
    magnitudes_rolloff = rolloff / 100 * magnitudes_cumsum[-1]
    index = np.searchsorted(magnitudes_cumsum, magnitudes_rolloff)
    return 0.5 * samplerate * index / (n - 1)
