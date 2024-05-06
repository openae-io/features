import numpy as np


def peak_amplitude(signal: np.ndarray) -> float:
    return np.max(np.abs(signal))
