# P2: Triển khai các bộ lọc
import cv2
import numpy as np

# Phản chiếu các pixel tại biên ảnh.
BORDER = cv2.BORDER_REFLECT_101

# kiểm tra kích thước kernel có hợp lệ không (số nguyên dương lẻ)
def check_kernel_size(k):
    if not isinstance(k, int) or k < 1 or k % 2 == 0:
        raise ValueError("k phải là số nguyên dương lẻ")

# Lọc trung bình và lọc Gaussian  
def mean_filter(image, k=3):
    """Lọc trung bình với kernel k × k."""
    check_kernel_size(k)

    return cv2.blur(
        image,
        (k, k),
        borderType=BORDER,
    )

def gaussian_filter(image, k=5, sigma=1.0):
    """Lọc Gaussian với kích thước k và độ lệch chuẩn sigma."""
    check_kernel_size(k)

    if sigma <= 0:
        raise ValueError("sigma phải lớn hơn 0")

    return cv2.GaussianBlur(
        image,
        (k, k),
        sigmaX=sigma,
        sigmaY=sigma,
        borderType=BORDER,
    )

def apply_kernel(image, kernel):
    """Áp dụng kernel, trả về float32 để giữ đáp ứng có dấu."""
    kernel = np.asarray(kernel, dtype=np.float32)

    if kernel.ndim != 2 or kernel.size == 0:
        raise ValueError("Kernel phải là ma trận 2D không rỗng")

    # Project quy ước kernel có kích thước lẻ ở cả hai chiều.
    check_kernel_size(kernel.shape[0])
    check_kernel_size(kernel.shape[1])

    return cv2.filter2D(
        image.astype(np.float32),
        cv2.CV_32F,
        kernel,
        borderType=BORDER,
    )


def sharpen(image):
    """Làm sắc nét bằng kernel cố định 3 × 3."""
    kernel = np.array([
        [0, -1, 0],
        [-1, 5, -1],
        [0, -1, 0],
    ], dtype=np.float32)

    result = apply_kernel(image, kernel)

    return np.clip(result, 0, 255).astype(np.uint8)


# P3: Nâng cao - Lọc trung vị và lọc song phương
def median_filter(image, k):
    check_kernel_size(k)
    return cv2.medianBlur(image, k)


def bilateral_filter(image, d=9, sigma_color=75, sigma_space=75):
    check_kernel_size(d)
    return cv2.bilateralFilter(
        image, d, sigma_color, sigma_space,
        borderType=BORDER
    )