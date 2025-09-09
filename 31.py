#------------------------------------------
#binary search 
#--------------------------------------
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# User Input
arr = list(map(int, input("Enter sorted list: ").split()))
target = int(input("Enter target to search: "))
index = binary_search(arr, target)
print("Index Found:" if index != -1 else "Not Found", index)
