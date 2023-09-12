import numpy as np

def skewness(signal: np.ndarray) -> float:
    def central_moment(order: int):
        return np.mean((signal - signal.mean()) ** order)
    return central_moment(3) / central_moment(2) ** (3 / 2)
