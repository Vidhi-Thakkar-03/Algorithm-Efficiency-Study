import random
import time
import pandas as pd
import matplotlib.pyplot as plt


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


    
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1

        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1

        arr[j+1] = key

    return arr


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left,right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i = i+1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result



def generate_random_data(size):
    arr = []

    for i in range(size):
        num = random.randint(1,1000)
        arr.append(num)

    return arr



def generate_nearly_sorted_data(size):
    arr = list(range(size))
    swaps = int(size * 0.05)

    for x in range(swaps):
        i = random.randint(0, size - 1)
        j = random.randint(0, size - 1)
        arr[i], arr[j] = arr[j], arr[i]

    return arr


# Main code

sizes = [100,500,1000,2000]

results = []

for i in sizes:

    random_data = generate_random_data(i)
    nearly_sorted_data = generate_nearly_sorted_data(i)

    datasets = { "Random" : random_data, "Nearly Sorted" : nearly_sorted_data}

    algorithms = { "Bubble Sort" : bubble_sort, "Insertion Sort" : insertion_sort, "Merge Sort" : merge_sort }

    for data_type, data in datasets.items():
        for algo_name, algo_func in algorithms.items():

            data_copy = data.copy()

            start = time.time()
            algo_func(data_copy)
            end = time.time()
            
            elapsed = end - start

            results.append( { "Algorithms" : algo_name, "Data Type" : data_type, "Input Size" : i, "Time" : elapsed } )
            
df = pd.DataFrame(results)

print("\n Experiment Result:")
print(df)

df.to_csv("sorting_results.csv", index=False)

for algo in df["Algorithms"].unique():

    subset = df[df["Algorithms"] == algo]

    plt.plot(subset["Input Size"],subset["Time"], marker='o', label=algo)
    
plt.xlabel("Input Size")
plt.ylabel("Execution Time (seconds)")
plt.title("Sorting Algorithm Performance Comparison")
plt.legend()
plt.grid(True)


print("\n" + "="*40)
print(" PROJECT ANALYSIS QUESTIONS")
print("="*40)

print("\nQ1: Which algorithm is the fastest for large datasets?")
print("Ans: Merge Sort. It remains efficient even as input size increases.")

print("\nQ2: Which algorithm is the slowest as data grows?")
print("Ans: Bubble Sort. Its execution time rises steeply, as show in the graph")

print("\nQ3: Does the type of data (Random vs Nearly Sorted) affect performance?")
print("Ans: Yes. Insertion Sort becomes significantly faster on Nearly Sorted data.")
print("="*40)

plt.show()





















        
        
