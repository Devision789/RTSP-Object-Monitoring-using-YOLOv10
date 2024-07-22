# RTSP-Object-Monitoring-using-YOLOv10
# RTSP Object Monitoring using YOLOv10

## Giới thiệu
Dự án này sử dụng YOLOv10 để giám sát đối tượng thông qua luồng video RTSP. Mục tiêu là phát hiện và theo dõi các đối tượng trong thời gian thực từ các camera giám sát.

## Tính năng
- Phát hiện đối tượng trong thời gian thực
- Hỗ trợ nhiều loại đối tượng khác nhau
- Tích hợp với các luồng video RTSP
- Giao diện người dùng trực quan để xem và quản lý các đối tượng được phát hiện

## Yêu cầu
- Python 3.8+
- OpenCV
- YOLOv10
- RTSP camera
- Inference

## Cài đặt
1. Clone repo này:
    ```bash
    git clone https://github.com/Devision789/RTSP-Object-Monitoring-using-YOLOv10.git
    cd RTSP-Object-Monitoring-YOLOv10
    ```

2. Cài đặt các thư viện cần thiết:
    ```bash
    pip install -r requirements.txt
    ```

3. Tải mô hình YOLOv10 và đặt vào thư mục `models/`:
    ```bash
    wget -P models/ https://path-to-yolov10-model
    ```

## Sử dụng
1. Chạy script để bắt đầu giám sát:
    ```bash
    python run.py
    ```


## Đóng góp
Chúng tôi hoan nghênh các đóng góp từ cộng đồng. Vui lòng tạo pull request hoặc mở issue để báo cáo lỗi hoặc đề xuất tính năng mới.

## Giấy phép
Dự án này được cấp phép theo giấy phép MIT. Xem file LICENSE để biết thêm chi tiết.
