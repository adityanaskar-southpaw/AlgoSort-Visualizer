import time
import matplotlib.pyplot as plt
import os

from data_generator import generate_random, generate_sorted, generate_reversed

# -----------------------------
# COUNTER CLASS
# -----------------------------
class Counter:
    def __init__(self):
        self.comparisons = 0

# -----------------------------
# SORTING ALGORITHMS
# -----------------------------
def bubble_sort(arr, counter):
    arr = arr.copy()
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            counter.comparisons += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def insertion_sort(arr, counter):
    arr = arr.copy()
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0:
            counter.comparisons += 1
            if arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            else:
                break
        arr[j + 1] = key
    return arr

def merge_sort(arr, counter):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid], counter)
    right = merge_sort(arr[mid:], counter)

    return merge(left, right, counter)

def merge(left, right, counter):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        counter.comparisons += 1
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

def quick_sort(arr, counter):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr)//2]
    left, middle, right = [], [], []

    for x in arr:
        counter.comparisons += 1
        if x < pivot:
            left.append(x)
        elif x > pivot:
            right.append(x)
        else:
            middle.append(x)

    return quick_sort(left, counter) + middle + quick_sort(right, counter)

def hybrid_sort(arr, counter):
    if len(arr) < 20:
        return insertion_sort(arr, counter)
    else:
        return merge_sort(arr, counter)

# -----------------------------
# MEASURE FUNCTION
# -----------------------------
def measure(func, data):
    counter = Counter()
    start = time.time()
    func(data.copy(), counter)
    end = time.time()
    return end - start, counter.comparisons

# -----------------------------
# MAIN ANALYSIS FUNCTION
# -----------------------------
def run_analysis():
    sizes = [50, 100, 200, 400]

    algorithms = {
        "Bubble": bubble_sort,
        "Merge": merge_sort,
        "Quick": quick_sort,
        "Hybrid": hybrid_sort
    }

    results_time = {name: [] for name in algorithms}
    results_comp = {name: [] for name in algorithms}

    # TEST DIFFERENT CASES
    for size in sizes:
        data_cases = {
            "Random": generate_random(size),
            "Sorted": generate_sorted(size),
            "Reversed": generate_reversed(size)
        }

        # Just use RANDOM for plotting (clean graphs)
        data = data_cases["Random"]

        for name, func in algorithms.items():
            t, c = measure(func, data)
            results_time[name].append(t)
            results_comp[name].append(c)

    # CREATE RESULTS FOLDER
    os.makedirs("results", exist_ok=True)

    # TIME GRAPH
    for name in algorithms:
        plt.plot(sizes, results_time[name], label=name)

    plt.xlabel("Input Size")
    plt.ylabel("Time (seconds)")
    plt.title("Sorting Algorithm Time Comparison")
    plt.legend()
    plt.savefig("results/time_graph.png")
    plt.show()

    # COMPARISON GRAPH
    for name in algorithms:
        plt.plot(sizes, results_comp[name], label=name)

    plt.xlabel("Input Size")
    plt.ylabel("Comparisons")
    plt.title("Sorting Algorithm Comparison Count")
    plt.legend()
    plt.savefig("results/comparison_graph.png")
    plt.show()