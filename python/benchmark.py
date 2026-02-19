import os
import time
import numpy as np
import subprocess
import pandas as pd

from sorting_algorithms import (
    mergesort,
    quicksort,
    heapsort,
    numpysort
)

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "..", "data")
RESULTS_PATH = os.path.join(BASE_DIR, "..", "results")
CPP_EXE = os.path.join(BASE_DIR, "..", "cpp", "sorting_func_cpp.exe")

# Tạo folder results nếu chưa có
os.makedirs(RESULTS_PATH, exist_ok=True)


# -----------------------------
# Benchmark Python Algorithms
# -----------------------------

def benchmark_python(func, arr):
    data = arr.copy()
    start = time.perf_counter()
    func(data)
    end = time.perf_counter()
    return (end - start) * 1000  # ms


# -----------------------------
# Benchmark NumPy
# -----------------------------

def benchmark_numpy(arr):
    data = arr.copy()
    start = time.perf_counter()
    np.sort(data)
    end = time.perf_counter()
    return (end - start) * 1000  # ms


# -----------------------------
# Benchmark C++
# -----------------------------

def benchmark_cpp(txt_file):
    result = subprocess.run(
        [CPP_EXE, txt_file],
        capture_output=True,
        text=True
    )

    microseconds = float(result.stdout.strip())
    return microseconds / 1000  # convert to ms


# -----------------------------
# Main
# -----------------------------

def main():

    results = []

    files = sorted([f for f in os.listdir(DATA_PATH) if f.endswith(".npy")])

    for file in files:
        print(f"\nBenchmarking: {file}")

        npy_path = os.path.join(DATA_PATH, file)
        txt_path = os.path.join(DATA_PATH, file.replace(".npy", ".txt"))

        arr = np.load(npy_path)

        merge_time = benchmark_python(mergesort, arr)
        quick_time = benchmark_python(quicksort, arr)
        heap_time = benchmark_python(heapsort, arr)
        numpy_time = benchmark_numpy(arr)
        cpp_time = benchmark_cpp(txt_path)

        results.append([
            file,
            merge_time,
            quick_time,
            heap_time,
            numpy_time,
            cpp_time
        ])

        print(f"MergeSort:  {merge_time:.2f} ms")
        print(f"QuickSort:  {quick_time:.2f} ms")
        print(f"HeapSort:   {heap_time:.2f} ms")
        print(f"NumPySort:  {numpy_time:.2f} ms")
        print(f"C++ sort:   {cpp_time:.2f} ms")

    df = pd.DataFrame(results, columns=[
        "Dataset",
        "MergeSort (ms)",
        "QuickSort (ms)",
        "HeapSort (ms)",
        "NumPy Sort (ms)",
        "C++ Sort (ms)"
    ])
    
    avg_row = {
        "Dataset": "Average",
        "MergeSort (ms)": df["MergeSort (ms)"].mean(),
        "QuickSort (ms)": df["QuickSort (ms)"].mean(),
        "HeapSort (ms)": df["HeapSort (ms)"].mean(),
        "NumPy Sort (ms)": df["NumPy Sort (ms)"].mean(),
        "C++ Sort (ms)": df["C++ Sort (ms)"].mean()
    }

    df = pd.concat([df, pd.DataFrame([avg_row])], ignore_index=True)

    output_csv = os.path.join(RESULTS_PATH, "benchmark_results.csv")
    df.to_csv(output_csv, index=False)

    print("\n===== FINAL RESULTS =====")
    print(df)


if __name__ == "__main__":
    main()
