import matplotlib.pyplot as plt
from data_generator import generate_random

# visual function
def draw_bars(arr, title, color="blue"):
    plt.clf()
    plt.bar(range(len(arr)), arr, color=color)
    plt.title(title)
    plt.pause(0.05)

#bubble sort visual
def bubble_sort_visual(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            draw_bars(arr, "Bubble Sort", "blue")

#quick sort visual
def quick_sort_visual(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort_visual(arr, low, pi - 1)
        quick_sort_visual(arr, pi + 1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
        draw_bars(arr, "Quick Sort", "green")

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# merge sort visual
def merge_sort_visual(arr, l, r):
    if l < r:
        m = (l + r) // 2
        merge_sort_visual(arr, l, m)
        merge_sort_visual(arr, m + 1, r)
        merge(arr, l, m, r)

def merge(arr, l, m, r):
    left = arr[l:m+1]
    right = arr[m+1:r+1]

    i = j = 0
    k = l

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
        draw_bars(arr, "Merge Sort", "orange")

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
        draw_bars(arr, "Merge Sort", "orange")

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1
        draw_bars(arr, "Merge Sort", "orange")

# main fucntion
def run_visual():
    data = generate_random(30)

    print("\nChoose Algorithm:")
    print("1. Bubble Sort")
    print("2. Quick Sort")
    print("3. Merge Sort")

    choice = input("Enter choice: ")

    plt.figure()

    if choice == "1":
        bubble_sort_visual(data)
    elif choice == "2":
        quick_sort_visual(data, 0, len(data) - 1)
    elif choice == "3":
        merge_sort_visual(data, 0, len(data) - 1)
    else:
        print("Invalid choice")

    plt.show()
