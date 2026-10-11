# Image Processing Lab 2

Dự án thực hành xử lý ảnh bằng Python, tập trung vào các phép biến đổi điểm ảnh, lọc ảnh, phát hiện biên, xử lý nhiễu và đánh giá chất lượng hình ảnh. Mã nguồn được tổ chức theo module trong thư mục `src/`, và các thí nghiệm được minh họa trong notebook `image_processing_lab2.ipynb`.

## Mục tiêu

- Thực hiện các phép biến đổi điểm ảnh: độ sáng, tương phản, âm bản, phân ngưỡng.
- Áp dụng các bộ lọc tuyến tính và phi tuyến để làm mịn, làm sắc nét và giảm nhiễu.
- Tính toán và hiển thị các kết quả phát hiện biên như Sobel và Prewitt.
- Đánh giá ảnh sau xử lý dựa trên các chỉ số như MSE, PSNR và SSIM.
- Lưu ảnh và hình vẽ ra thư mục `outputs/` để quan sát trực quan.

## Tính năng chính

### 1. Toán tử điểm ảnh
- `brightness(image, beta)`: thay đổi độ sáng bằng cách cộng/trừ hằng số.
- `contrast(image, alpha)`: thay đổi độ tương phản theo hệ số.
- `negative(image)`: tạo ảnh âm bản.
- `binary_threshold(gray, threshold)`: tạo ảnh nhị phân theo ngưỡng.

### 2. Xử lý nhiễu
- `gaussian_noise(gray, sigma=25, seed=42)`: thêm nhiễu Gaussian.
- `salt_pepper_noise(gray, amount=0.05, seed=42)`: thêm nhiễu muối tiêu.

### 3. Bộ lọc ảnh
- `mean_filter(image, k=3)`: lọc trung bình.
- `gaussian_filter(image, k=5, sigma=1.0)`: lọc Gaussian.
- `median_filter(image, k)`: lọc trung vị.
- `bilateral_filter(image, d=9, sigma_color=75, sigma_space=75)`: lọc song phương.
- `sharpen(image)`: làm sắc nét bằng kernel cố định.

### 4. Phát hiện biên
- `gradients(gray, method="sobel")`: tính gradient theo phương x, y và độ lớn gradient.
- Hỗ trợ cả phương pháp Sobel và Prewitt.

### 5. Đọc/ghi ảnh và đánh giá
- `read_image(path, grayscale=False)`: đọc ảnh với OpenCV.
- `save_image(path, image)`: lưu ảnh tự động tạo thư mục.
- `evaluate(reference, result)`: trả về MSE, PSNR, SSIM.

## Cấu trúc thư mục

```text
image-processing-lab2/
├── data/
│   └── original/
│       └── desk.jpg
├── outputs/
│   ├── figures/
│   ├── images/
│   └── metrics/
├── src/
│   ├── _init_.py
│   ├── edges.py
│   ├── evaluation.py
│   ├── filters.py
│   ├── image_io.py
│   ├── noise.py
│   └── point_ops.py
├── image_processing_lab2.ipynb
├── requirements.txt
├── README.md
└── .gitignore
```

## Yêu cầu môi trường

- Python 3.10+
- OpenCV
- NumPy
- scikit-image
- Matplotlib
- Jupyter Notebook

## Cài đặt

Từ thư mục dự án, thực hiện:

```bash
python -m venv .venv
```

Trên Windows:

```powershell
.venv\Scripts\Activate.ps1
```

Trên macOS/Linux:

```bash
source .venv/bin/activate
```

Sau đó cài đặt các phụ thuộc:

```bash
pip install -r requirements.txt
```

## Chạy dự án

### Chạy notebook

```bash
jupyter notebook image_processing_lab2.ipynb
```

Hoặc:

```bash
jupyter lab
```

### Ví dụ sử dụng

```python
from src.image_io import read_image
from src.point_ops import brightness, negative
import cv2

image = read_image("data/original/desk.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

bright = brightness(gray, 50)
neg = negative(gray)
```

## Kết quả đầu ra

Các kết quả xử lý thường được lưu trong các thư mục:

- `outputs/figures/`: hình so sánh trực quan giữa các phương pháp.
- `outputs/images/`: ảnh đã xử lý theo từng bộ lọc/thuật toán.
- `outputs/metrics/`: số liệu đánh giá (MSE, PSNR, SSIM) nếu có lưu tệp kết quả.

## Ghi chú

- Dự án này phù hợp cho mục tiêu học tập và thực hành xử lý ảnh cơ bản.
- Một số chức năng hỗ trợ đường dẫn có dấu tiếng Việt trên Windows để đọc/ghi ảnh ổn định hơn.
- Để hiểu rõ từng thao tác, nên chạy từng cell trong notebook theo thứ tự và quan sát kết quả trực quan.

## Tác giả / Mục đích học tập

Dự án này được xây dựng nhằm mục đích thực hành các kỹ thuật cơ bản trong xử lý ảnh số, đặc biệt phù hợp cho người học muốn làm quen với:

- biến đổi điểm ảnh,
- lọc ảnh dựa trên kernel,
- phát hiện biên,
- khử nhiễu,
- so sánh chất lượng ảnh bằng metric số.

Nếu bạn muốn, tôi có thể tiếp tục viết thêm một phiên bản README theo kiểu chuyên nghiệp hơn với badge, demo screenshots và hướng dẫn chi tiết cho từng module.
