import numpy as np


def spectral_rolloff(spectrum: np.ndarray, samplerate: float, rolloff: int):
    ps = np.abs(spectrum) ** 2
    ps_sum_rolloff = (rolloff / 100) * np.sum(ps)
    ps_sum = 0.0
    for i, magnitude in enumerate(ps):
        ps_sum += magnitude
        if ps_sum >= ps_sum_rolloff:
            return 0.5 * samplerate / (len(ps) - 1) * i
    return 0.5 * samplerate
