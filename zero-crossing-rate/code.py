import numpy as np

def zero_crossing_rate(signal: np.ndarray, samplerate: float) -> int:
    if len(signal) == 0:
        return 0
    crossings = np.count_nonzero(np.diff(signal >= 0))
    return samplerate * crossings / len(signal)
