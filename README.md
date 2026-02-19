# 📊 Benchmarking Sorting Algorithms (Python vs C++)

Báo cáo thực nghiệm so sánh hiệu năng các thuật toán sắp xếp trên nhiều loại dữ liệu khác nhau, bao gồm cả cài đặt Python thuần, NumPy và C++ `std::sort`.

---

## 📋 Mục tiêu

So sánh thời gian thực thi của các thuật toán:

1. **QuickSort** (Python – tự cài đặt)
2. **MergeSort** (Python – tự cài đặt)
3. **HeapSort** (Python – tự cài đặt)
4. **NumPy Sort (`np.sort`)**
5. **C++ `std::sort`**

Trên các tập dữ liệu:

- Float:
  - Sorted (tăng dần)
  - Reverse (giảm dần)
  - Random
- Int:
  - Random (5 tập mẫu)
- Kích thước mỗi tập: **1,000,000 phần tử**

---

## 📁 Cấu trúc thư mục

```
Sorting_Algorithms_DSA/
│
├── data/              # Dataset (.npy và .txt)
│
├── python/
│   ├── sorting_algorithms.py
│   ├── generate_data.py
│   ├── benchmark.py
│   └── visualize.py
│
├── cpp/
│   └── sorting_func_cpp.cpp
│
├── results/
│   ├── benchmark_results.csv
│   ├── comparison_by_dataset.png
│   └── average_comparison.png
│
└── README.md
```

---

## ⚙️ Môi trường thực nghiệm

- Python 3.x
- NumPy
- Matplotlib
- Trình biên dịch C++ (g++)

Cài thư viện Python:

```bash
pip install numpy matplotlib
```

Biên dịch chương trình C++:

```bash
cd cpp
g++ sorting_func_cpp.cpp -O2 -o sorting_func_cpp
```

---

## 🚀 Cách chạy

### 1️⃣ Generate dữ liệu

```bash
cd python
python generate_data.py
```

---

### 2️⃣ Chạy Benchmark

```bash
python benchmark.py
```

Script sẽ:

- Đọc dữ liệu từ `data/`
- Gọi C++ executable
- Ghi kết quả vào:

```
results/benchmark_results.csv
```

Cuối bảng có thêm một dòng:

```
Average
```

Là thời gian trung bình của từng thuật toán.

---

### 3️⃣ Vẽ biểu đồ

```bash
python visualize.py
```

Sinh ra:

- `results/comparison_by_dataset.png`
- `results/average_comparison.png`

---

# 📊 Kết quả

## So sánh theo từng dataset

![Dataset Comparison](results/comparison_by_dataset.png)

---

## Thời gian trung bình

![Average Comparison](results/average_comparison.png)

---

# 📈 Phân tích kết quả

## C++ `std::sort`

- Rất nhanh (~7–10 ms cho 1 triệu phần tử).
- Sử dụng Introsort (QuickSort + HeapSort + InsertionSort).
- Được tối ưu hóa ở mức compiler (-O2).
- Không có interpreter overhead như Python.

---

## NumPy Sort

- Gần tương đương C++.
- Được viết bằng C.
- Tận dụng tốt cache CPU và vectorization.
- Có một lượng nhỏ overhead khi gọi từ Python.

---

## Python Pure Implementations

| Thuật toán | Nhận xét |
|------------|----------|
| QuickSort  | Nhanh nhất trong nhóm Python |
| MergeSort  | Ổn định và hiệu năng đều |
| HeapSort   | Chậm nhất do cache locality kém |

Nguyên nhân chậm:

- Interpreter overhead
- Không tối ưu bộ nhớ mức thấp
- Không vectorization
- Hệ số hằng số lớn

---

# 🧠 Kết luận

1. Trong thực tế nên ưu tiên sử dụng `np.sort()` hoặc `std::sort`.
2. Các thuật toán tự cài đặt phù hợp mục đích học thuật.
3. Mặc dù có cùng độ phức tạp O(n log n), hiệu năng thực tế khác nhau rất lớn do hệ số hằng số và tối ưu hóa hệ thống.
4. HeapSort có cùng O(n log n) nhưng hiệu năng thực tế kém hơn đáng kể.

---

## 👨‍🎓 Tác giả

Nguyễn Văn Dũng  
