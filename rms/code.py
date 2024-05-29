import numpy as np


def rms(signal: np.ndarray) -> float:
    return np.sqrt(np.mean(signal**2))
