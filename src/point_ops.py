# P1: Triển khai 4 toán tử điểm ảnh bằng Numpy (độ sáng, tương phản, âm bản, phân ngưỡng)
import numpy as np

# Giới hạn giá trị và chuyển kiểu dữ liệu sang uint8
def to_uint8(image):
    """Giới hạn giá trị về 0–255 rồi chuyển sang uint8."""
    return np.clip(image, 0, 255).astype(np.uint8)

# tăng/giảm độ sáng ảnh
def brightness(image, beta):
    """g = f + beta. beta dương: sáng hơn; âm: tối hơn."""
    values = image.astype(np.float32)
    return to_uint8(values + beta)

# điều chỉnh độ tương phản ảnh
def contrast(image, alpha):
    """Thay đổi tương phản theo đề: g = alpha * f."""
    if alpha < 0:
        raise ValueError("alpha phải lớn hơn hoặc bằng 0")

    values = image.astype(np.float32)
    return to_uint8(alpha * values)

# tạo ảnh âm bản
def negative(image):
    """Ảnh âm bản: g = 255 - f."""
    return 255 - image

# cắt ngưỡng tạo ảnh nhị phân
def binary_threshold(gray, threshold):
    """Pixel >= threshold thành 255, còn lại thành 0."""
    if gray.ndim != 2:
        raise ValueError("Phân ngưỡng này yêu cầu ảnh xám")

    if not 0 <= threshold <= 255:
        raise ValueError("threshold phải nằm trong khoảng 0–255")

    return np.where(
        gray >= threshold, 255, 0
    ).astype(np.uint8)