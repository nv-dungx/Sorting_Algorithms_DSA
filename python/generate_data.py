import numpy as np
import os

os.makedirs("../data", exist_ok=True)

N = 1_000_000

def save_both(name, array):
    np.save(f"../data/{name}.npy", array)
    np.savetxt(f"../data/{name}.txt", array)

# ===== FLOAT DATA =====
float_base = np.random.rand(N)

float_sorted = np.sort(float_base)
float_reverse = float_sorted[::-1]

save_both("../data/float_1_sorted", float_sorted)
save_both("../data/float_2_reverse", float_reverse)

for i in range(3, 6):
    save_both(f"../data/float_{i}_random", np.random.rand(N))

# ===== INT DATA =====
for i in range(6, 11):
    save_both(f"../data/int_{i}_random", np.random.randint(0, 1_000_000, N))
