import numpy as np


def counts(signal: np.ndarray, threshold: float) -> int:
    above_threshold = signal >= threshold
    # count crossings from below threshold to above threshold
    crossings = ~above_threshold[:-1] & above_threshold[1:]
    return np.count_nonzero(crossings)
