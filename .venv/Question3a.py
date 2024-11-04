import pandas as pd

# Load data
data = pd.read_csv("worldcities.csv")
latitude_longitude_pairs = data[['lat', 'lng', 'city']].drop_duplicates()
unique_latitudes = latitude_longitude_pairs['lat'].unique()

# (a) Merge Sort Implementation
merge_count = 0

def merge_sort(arr):
    global merge_count
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            merge_count += 1
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    return arr

# Sort and print results
sorted_latitudes = merge_sort(unique_latitudes.copy())
print("Merge Sort - Sorted Latitudes:", sorted_latitudes)
print("Number of merges:", merge_count)
