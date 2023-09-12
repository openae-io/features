import numpy as np

def kurtosis(signal: np.ndarray) -> float:
    def central_moment(order: int):
        return np.mean((signal - signal.mean()) ** order)
    return central_moment(4) / central_moment(2) ** 2
