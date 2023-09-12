import numpy as np

def clearance_factor(signal: np.ndarray) -> float:
    return np.max(np.abs(signal)) / (np.mean(np.sqrt(np.abs(signal))) ** 2)
