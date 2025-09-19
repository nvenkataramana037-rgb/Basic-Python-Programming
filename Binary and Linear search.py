# Binary Search 
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

arr_binary = [1, 5, 3, 7, 8, 2, 9]
target_binary = 9
result = binary_search(arr_binary, target_binary)
if result != -1:
    print("Binary Search: Target found at index", result)
else:
    print("Binary Search: Target not found")


# Linear Search
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  
    return -1

arr_linear = [10, 40, 30, 20, 90]
target_linear = int(input("Enter target: "))
result = linear_search(arr_linear, target_linear)
if result != -1:
    print("Linear Search: Target found at index", result)
else:
    print("Linear Search: Target not found")
                   