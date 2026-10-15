# B1: Đọc ảnh, lưu ảnh, in thông tin cơ bản của ảnh
from pathlib import Path

import cv2
import numpy as np

# Đọc ảnh xám (hoặc dùng cv2.IMREAD_COLOR nếu muốn đọc ảnh màu)
def read_image(path, grayscale=False):
    """Đọc ảnh từ đường dẫn, trả về ảnh BGR hoặc ảnh xám."""
    path = Path(path)

    if not path.is_file():
        raise FileNotFoundError(f"Không tìm thấy ảnh: {path}")

    # Hỗ trợ đường dẫn có dấu tiếng Việt trên Windows.
    encoded = np.fromfile(str(path), dtype=np.uint8)

    flag = (
        cv2.IMREAD_GRAYSCALE
        if grayscale
        else cv2.IMREAD_COLOR
    )

    image = cv2.imdecode(encoded, flag)

    if image is None:
        raise ValueError(f"Không giải mã được ảnh: {path}")

    return image

# Lưu ảnh ra tệp
def save_image(path, image):
    """Lưu ảnh, tự tạo thư mục nếu chưa có."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)

    success, encoded = cv2.imencode(path.suffix, image)

    if not success:
        raise ValueError(f"Không mã hóa được ảnh: {path}")

    encoded.tofile(str(path))

# khi đọc ảnh xong, kiểm tra thông tin cơ bản của ảnh
def print_image_info(image):
    print("Shape:", image.shape) #chiều cao,chiều rộng
    print("Dtype:", image.dtype) 
    print("Min/max:", image.min(), image.max()) #miền giá trị 0-255