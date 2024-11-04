import pandas as pd

# Load data
data = pd.read_csv("worldcities.csv")
latitude_longitude_pairs = data[['lat', 'lng', 'city']].drop_duplicates()
unique_latitudes = latitude_longitude_pairs['lat'].unique()
unique_latitudes.sort()  # Ensure the list is sorted for binary search

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Input target latitude and search
target_latitude = float(input("Enter a latitude to search: "))
index = binary_search(unique_latitudes, target_latitude)
if index != -1:
    city = latitude_longitude_pairs[latitude_longitude_pairs['lat'] == target_latitude]['city'].values[0]
    print(f"City found for latitude {target_latitude}: {city}")
else:
    print("Latitude not found.")
