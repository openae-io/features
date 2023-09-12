import numpy as np

def shape_factor(signal: np.ndarray) -> float:
    return np.sqrt(np.mean(signal ** 2))  / np.mean(np.abs(signal))
