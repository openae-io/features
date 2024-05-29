import numpy as np


def energy(signal: np.ndarray) -> float:
    return np.sum(signal**2)
