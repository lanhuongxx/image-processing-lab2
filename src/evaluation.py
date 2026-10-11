import numpy as np
from skimage.metrics import (
    peak_signal_noise_ratio,
    structural_similarity,
)


def evaluate(reference, result):
    """Đánh giá ảnh xám uint8 so với ảnh tham chiếu."""
    if reference.shape != result.shape:
        raise ValueError("Hai ảnh phải cùng kích thước")

    difference = (
        reference.astype(np.float64)
        - result.astype(np.float64)
    )

    return {
        "MSE": float(np.mean(difference ** 2)),
        "PSNR": float(peak_signal_noise_ratio(
            reference, result, data_range=255
        )),
        "SSIM": float(structural_similarity(
            reference, result, data_range=255
        )),
    }