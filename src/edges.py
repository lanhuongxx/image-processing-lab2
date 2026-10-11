# P3: Sobel và Prewitt: giữ kết quả có dấu
import numpy as np

from .filters import apply_kernel


def gradients(gray, method="sobel"):
    """Trả về Gx, Gy và độ lớn gradient chưa chuẩn hóa."""
    if gray.ndim != 2:
        raise ValueError("Yêu cầu ảnh xám 2D")

    method = method.lower()

    if method == "sobel":
        kernel_x = np.array([
            [-1, 0, 1],
            [-2, 0, 2],
            [-1, 0, 1],
        ], dtype=np.float32)

    elif method == "prewitt":
        kernel_x = np.array([
            [-1, 0, 1],
            [-1, 0, 1],
            [-1, 0, 1],
        ], dtype=np.float32)

    else:
        raise ValueError("method phải là sobel hoặc prewitt")

    kernel_y = kernel_x.T

    gx = apply_kernel(gray, kernel_x)
    gy = apply_kernel(gray, kernel_y)
    magnitude = np.hypot(gx, gy)

    return gx, gy, magnitude


def gradient_to_uint8(values):
    """Chuẩn hóa độ lớn về 0–255, chỉ phục vụ hiển thị."""
    values = np.abs(values)
    maximum = float(values.max())

    if maximum == 0:
        return np.zeros(values.shape, dtype=np.uint8)

    return np.clip(
        values / maximum * 255, 0, 255
    ).astype(np.uint8)