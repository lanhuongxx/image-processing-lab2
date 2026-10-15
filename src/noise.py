# P3: Nâng cao - Tạo nhiễu Gaussian và nhiễu muối tiêu
import numpy as np


def gaussian_noise(gray, sigma=25, seed=42):
    """Cộng nhiễu Gaussian, sigma tính trên thang 0–255."""
    if sigma < 0:
        raise ValueError("sigma phải >= 0")

    rng = np.random.default_rng(seed)
    noise = rng.normal(0, sigma, gray.shape)

    result = gray.astype(np.float32) + noise

    return np.clip(np.rint(result), 0, 255).astype(np.uint8)


def salt_pepper_noise(gray, amount=0.05, seed=42):
    """Chọn amount phần pixel, thay bằng đen hoặc trắng."""
    if gray.ndim != 2:
        raise ValueError("Yêu cầu ảnh xám 2D")

    if not 0 <= amount <= 1:
        raise ValueError("amount phải nằm trong khoảng 0–1")

    rng = np.random.default_rng(seed)
    result = gray.copy()

    count = int(round(amount * gray.size))
    indices = rng.choice(gray.size, size=count, replace=False)

    # Chia gần đều số vị trí muối và tiêu.
    half = count // 2
    result.flat[indices[:half]] = 0
    result.flat[indices[half:]] = 255

    return result