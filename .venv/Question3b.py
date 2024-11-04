import pandas as pd

# Load data
data = pd.read_csv("worldcities.csv")
latitude_longitude_pairs = data[['lat', 'lng', 'city']].drop_duplicates()
unique_latitudes = latitude_longitude_pairs['lat'].unique()

# (b) Quick Sort Implementation
comparison_count = 0

def quick_sort(arr):
    global comparison_count
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = []
    middle = []
    right = []
    for x in arr:
        comparison_count += 1
        if x < pivot:
            left.append(x)
        elif x == pivot:
            middle.append(x)
        else:
            right.append(x)
    return quick_sort(left) + middle + quick_sort(right)

# Sort and print results
sorted_latitudes_quick = quick_sort(unique_latitudes.copy())
print("Quick Sort - Sorted Latitudes:", sorted_latitudes_quick)
print("Number of comparisons:", comparison_count)
