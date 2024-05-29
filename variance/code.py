import numpy as np


def variance(signal: np.ndarray) -> float:
    return np.mean((signal - signal.mean()) ** 2)
