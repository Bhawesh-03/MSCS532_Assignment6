# test_selection.py
import time, random
from deterministic_selection import select_median_of_medians
from randomized_selection import randomized_quickselect

sizes = [1000, 5000, 10000]
for n in sizes:
    arr = random.sample(range(n*2), n)
    k = n // 2
    
    # Deterministic
    start = time.time()
    select_median_of_medians(arr[:], k)
    print(f"Deterministic size={n} time={time.time()-start:.6f}s")
    
    # Randomized
    start = time.time()
    randomized_quickselect(arr[:], 0, n-1, k)
    print(f"Randomized size={n} time={time.time()-start:.6f}s")
