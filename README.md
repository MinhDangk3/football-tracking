# ⚽ Football Tracking System - AI Computer Vision

<p align="center">
  🚀 Hệ thống phân tích video bóng đá sử dụng YOLOv8, Object Tracking và AI Pipeline hoàn chỉnh
</p>

---

## 📌 Tổng Quan

Dự án xây dựng hệ thống **phân tích video bóng đá end-to-end** sử dụng **Computer Vision và Deep Learning** để:

* Phát hiện cầu thủ và bóng
* Theo dõi chuyển động theo thời gian thực
* Phân tích hành vi và dữ liệu trận đấu

👉 Đây là một hệ thống mô phỏng **AI Sports Analytics Platform thực tế**

---

## 🎯 Tính Năng Chính

* 🎥 Phát hiện đối tượng với **YOLOv8**
* 🔄 Tracking cầu thủ theo ID xuyên suốt video
* ⚽ Gán bóng cho cầu thủ gần nhất
* 🧭 Chuyển đổi góc nhìn (top-view)
* 📏 Tính toán tốc độ & quãng đường
* 🔥 Heatmap di chuyển cầu thủ
* 👕 Phân đội dựa trên màu áo
* 🎨 Visualization (bounding box, overlay stats)

---

## 🖼️ Demo

### 📌 Output

<p align="center">
  <img src="demo.jpg" width="800"/>
  <img width="800" height="600" alt="possession_IRAN_vs_USA" src="https://github.com/user-attachments/assets/2f716c8f-453b-4080-ab1c-004ec690eed0" />
  <img width="1280" height="800" alt="IRAN_heatmap" src="https://github.com/user-attachments/assets/8cd6a850-c864-4c53-bcd8-2646e1e0de2e" />
<img width="1920" height="1080" alt="ball_touches_IRAN_vs_USA" src="https://github.com/user-attachments/assets/83f33692-4ae8-423c-b625-39eeb1c4213b" />
<img width="1920" height="1080" alt="distance_chart_IRAN_vs_USA" src="https://github.com/user-attachments/assets/71d11677-a531-4bbe-acc3-c5a5759a5bc3" />
<img width="1800" height="750" alt="space_timeline" src="https://github.com/user-attachments/assets/d88cc0a1-c0b5-4f82-9a90-8448f1defb2d" />
<img width="1050" height="680" alt="space_heatmap" src="https://github.com/user-attachments/assets/a13d0d75-3ec0-409d-9f36-fd741b5ca54a" />



</p>

### 🎬 Video Demo

<p align="center">
  <a href="https://drive.google.com/file/d/10RdQbyuDMdFAaBrp8coeJ7m40OLBzCVC/view?usp=sharing">
    <img src="https://drive.google.com/file/d/10RdQbyuDMdFAaBrp8coeJ7m40OLBzCVC/view?usp=sharing"/>
    
  </a>
</p>



---

## 🧠 Công Nghệ Sử Dụng

* **Computer Vision:** YOLOv8, OpenCV
* **Deep Learning:** PyTorch
* **Tracking:** Object Tracking (custom pipeline)
* **Data Processing:** NumPy, Pandas
* **Visualization:** OpenCV / custom overlay
* **Ngôn ngữ:** Python

---

## ⚙️ Cấu Trúc Dự Án

```bash
football-tracking/
│
├── camera_movement_estimator/    # Ước lượng chuyển động camera
├── heatmap_generator/            # Tạo heatmap
├── mini_map/                     # Bản đồ mini sân bóng
├── player_ball_assigner/         # Gán bóng cho cầu thủ
├── speed_and_distance_estimator/ # Tính tốc độ & khoảng cách
├── team_assigner/                # Phân đội theo màu áo
│
├── trackers/                     # Tracking object
├── view_transformer/             # Transform góc nhìn
├── visualizations/               # Vẽ kết quả
├── utils/                        # Hàm tiện ích
│
├── input_video/                  # Video đầu vào
├── output_videos/                # Video đầu ra
├── models/                       # Model YOLO
│
├── training/                     # Training (nếu có)
├── tests/                        # Unit test
│
├── main.py                       # Pipeline chính
├── yolo_inf.py                   # Test YOLO
├── football_dashboard_app.py     # Dashboard
│
├── requirements.txt
└── README.md
```

---

## 🧠 Kiến Trúc Hệ Thống

Pipeline xử lý:

```
Video Input
   ↓
YOLO Detection
   ↓
Object Tracking (ID)
   ↓
Player-Ball Assignment
   ↓
Perspective Transform (Top View)
   ↓
Speed & Distance Calculation
   ↓
Visualization + Output Video
```

---

## 🛠️ Cài Đặt & Chạy

### 1. Tạo môi trường ảo

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

---

### 2. Cài thư viện

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

👉 Nếu có GPU:

https://pytorch.org/get-started/locally/

---

### 3. Chạy project

```powershell
python main.py
```

---

## 📂 File Quan Trọng

* `main.py` → Pipeline chính
* `trackers/` → Logic tracking
* `player_ball_assigner/` → Gán bóng
* `team_assigner/` → Phân đội
* `view_transformer/` → Transform góc nhìn

---


## 📈 Hướng Phát Triển

* 🔥 Player Re-identification (Re-ID)
* 📊 Tactical Analysis (chiến thuật)
* ⚡ Tối ưu FPS real-time
* 🤖 Kết hợp LLM để phân tích trận đấu

---

## 💡 Điểm Nổi Bật

* ✅ Thiết kế theo **modular architecture**
* ✅ Pipeline giống hệ thống AI thực tế
* ✅ Có nhiều module nâng cao:

  * Camera motion
  * Perspective transform
  * Heatmap
  * Tracking nâng cao

---

## 👨‍💻 Tác Giả

**Lê Minh Đăng**
🔗 https://github.com/MinhDangk3

---

<p align="center">
🔥 Nếu bạn thấy project hữu ích, hãy ⭐ repo để ủng hộ!
</p>
