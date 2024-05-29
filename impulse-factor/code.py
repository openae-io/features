import numpy as np


def impulse_factor(signal: np.ndarray) -> float:
    return np.max(np.abs(signal)) / np.mean(np.abs(signal))
