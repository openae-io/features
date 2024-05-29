import numpy as np


def counts(signal: np.ndarray, threshold: float) -> int:
    if len(signal) == 0:
        return 0
    result = 0
    was_above_threshold = signal[0] >= threshold
    for value in signal[1:]:
        is_above_threshold = value >= threshold
        if not was_above_threshold and is_above_threshold:
            result += 1
        was_above_threshold = is_above_threshold
    return result
