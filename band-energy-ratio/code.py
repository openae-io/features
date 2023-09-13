import numpy as np

def band_energy_ratio(
    spectrum: np.ndarray, samplerate: float, f_lower: float, f_upper: float
) -> float:
    powerspectrum = np.abs(spectrum) ** 2
    n = len(powerspectrum)
    n_lower = int(2 * n * f_lower / samplerate)
    n_upper = int(2 * n * f_upper / samplerate)
    return np.sum(powerspectrum[n_lower : n_upper + 1]) / np.sum(powerspectrum)
