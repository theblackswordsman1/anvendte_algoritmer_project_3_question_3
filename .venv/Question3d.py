import pandas as pd

# Load data and filter for Norway
data = pd.read_csv("worldcities.csv")
norway_cities = data[data['country'] == "Norway"]
norway_latitudes = norway_cities['lat'].unique()
norway_latitudes.sort()

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

# Input target latitude for Norway and search
target_latitude_norway = float(input("Enter a latitude for Norway search: "))
index_norway = binary_search(norway_latitudes, target_latitude_norway)
if index_norway != -1:
    city_norway = norway_cities[norway_cities['lat'] == target_latitude_norway]['city'].values[0]
    print(f"Norwegian city found for latitude {target_latitude_norway}: {city_norway}")
else:
    print("Latitude not found in Norway.")
