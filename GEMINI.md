# Deep Learning & Computer Vision Project Guidelines

Khi người dùng yêu cầu thực hiện bài tập hoặc dự án Deep Learning (DL) / Computer Vision (CV) phối hợp giữa Antigravity IDE và Google Colab:

### 1. Phân chia vai trò môi trường (Dual-Environment Workflow)
* **Antigravity IDE (Local)**: Nơi phát triển chính (80% khối lượng) bao gồm: viết mã nguồn (`.py`), thiết kế mô hình (`models/`), DataLoaders, hàm mất mát (loss functions), cấu hình (`configs/`). Đồng bộ qua GitHub repo.
* **Google Colab (Cloud GPU)**: Môi trường chạy tính toán nặng (20% khối lượng). Mở trực tiếp Notebook (`.ipynb`) từ GitHub repo để kích hoạt GPU (T4/A100) và trực quan hóa kết quả.

### 2. Nguyên tắc BẮT BUỘC về Checkpoints & Auto-Resume
Trong MỌI script hoặc notebook huấn luyện mô hình:
* **Luôn có hàm lưu Checkpoint**: Sau mỗi epoch (hoặc N steps), lưu trạng thái mới nhất (`model.state_dict()`, `optimizer.state_dict()`, `scheduler.state_dict()`, `epoch`, `loss`) vào Google Drive (`/content/drive/MyDrive/.../last_checkpoint.pt`).
* **Luôn có cơ chế Tự Động Resume**: Trước vòng lặp train, code phải kiểm tra xem `last_checkpoint.pt` có tồn tại không. Nếu có, tự động nạp lại và tiếp tục từ epoch tiếp theo thay vì bắt đầu lại từ Epoch 1.
* **Lưu riêng Best Model**: Lưu `best_checkpoint.pt` khi metric validation đạt kỷ lục mới.

### 3. Quy chuẩn Quản lý Dữ liệu & Trọng số
* **Tuyệt đối KHÔNG đẩy Artifact nặng lên Git**: Toàn bộ file weights (`.pt`, `.pth`, `.bin`, `.onnx`) và thư mục dataset phải được khai báo trong `.gitignore`.
* **Dataset lớn (>10GB)**: Nén thành 1 file duy nhất (`.tar`/`.zip`) lưu trên Google Drive. Khi Colab khởi động, copy duy nhất file nén này sang ổ NVMe cục bộ (`/content/`) và giải nén ra để đạt tốc độ đọc tối đa cho GPU, tránh nghẽn I/O qua Drive FUSE.
* **Logs & Metrics**: Khuyến khích tích hợp Weights & Biases (`wandb`) hoặc TensorBoard để theo dõi biểu đồ real-time từ xa.
