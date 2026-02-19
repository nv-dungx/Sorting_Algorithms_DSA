import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RESULTS_PATH = os.path.join(BASE_DIR, "..", "results")

csv_path = os.path.join(RESULTS_PATH, "benchmark_results.csv")
df = pd.read_csv(csv_path)

color_map = {
    "QuickSort (ms)": "tab:blue",
    "HeapSort (ms)": "tab:red",
    "MergeSort (ms)": "tab:green",
    "NumPy Sort (ms)": "tab:purple",
    "C++ Sort (ms)": "tab:orange"
}

algorithms = [
    "QuickSort (ms)",
    "HeapSort (ms)",
    "MergeSort (ms)",
    "NumPy Sort (ms)",
    "C++ Sort (ms)"
]

# -----------------------------
# Tách dữ liệu thường và dòng Average
# -----------------------------

df_main = df[df["Dataset"] != "Average"]
df_avg = df[df["Dataset"] == "Average"].iloc[0]

datasets = df_main["Dataset"].str.replace(".npy", "", regex = False)

x = np.arange(len(datasets))
width = 0.15

# -----------------------------
# Biểu đồ 1: theo từng dataset
# -----------------------------

plt.figure(figsize=(15, 6))

for i, algo in enumerate(algorithms):
    plt.bar(
        x + i * width,
        df_main[algo],
        width,
        label=algo.replace(" (ms)", ""),
        color=color_map[algo]
    )

plt.xticks(x + width * 2, datasets, rotation=45)
plt.ylabel("Thời gian (ms)")
plt.title("So sánh thời gian thực hiện theo tập dữ liệu")
plt.legend()
plt.tight_layout()

plt.savefig(os.path.join(RESULTS_PATH, "comparison_by_dataset.png"))
plt.close()

# -----------------------------
# Biểu đồ 2: Trung bình (lấy trực tiếp từ CSV)
# -----------------------------

plt.figure(figsize=(8, 6))

means = [df_avg[algo] for algo in algorithms]
algo_names = [algo.replace(" (ms)", "") for algo in algorithms]
colors = [color_map[algo] for algo in algorithms]

bars = plt.bar(algo_names, means, color=colors)

plt.ylabel("Thời gian trung bình (ms)")
plt.title("Thời gian trung bình của các thuật toán")

for bar in bars:
    yval = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        yval,
        f"{yval:.2f}",
        ha="center",
        va="bottom"
    )

plt.tight_layout()
plt.savefig(os.path.join(RESULTS_PATH, "average_comparison.png"))
plt.close()
