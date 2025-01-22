import numpy as np


def energy(signal: np.ndarray, samplerate: float) -> float:
    return 1 / samplerate * np.sum(signal**2)
