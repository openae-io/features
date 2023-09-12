import numpy as np

def k_factor(signal: np.ndarray) -> float:
    return np.max(np.abs(signal)) * np.sqrt(np.mean(signal ** 2))
