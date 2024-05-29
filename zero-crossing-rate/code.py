import numpy as np


def zero_crossing_rate(signal: np.ndarray, samplerate: float) -> int:
    if len(signal) == 0:
        return 0
    crossings = 0
    was_positive = signal[0] >= 0
    for value in signal[1:]:
        is_positive = value >= 0
        if was_positive != is_positive:
            crossings += 1
        was_positive = is_positive
    return samplerate * crossings / len(signal)
