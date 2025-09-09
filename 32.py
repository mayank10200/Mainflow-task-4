#---------------------------------------
#Find Subarray with Given Sum
#---------------------------------------
def find_subarray_with_sum(arr, target):
    start, curr_sum = 0, 0
    for end in range(len(arr)):
        curr_sum += arr[end]
        while curr_sum > target and start <= end:
            curr_sum -= arr[start]
            start += 1
        if curr_sum == target:
            return (start, end)
    return -1

# User Input
arr = list(map(int, input("Enter list: ").split()))
target = int(input("Enter target sum: "))
result = find_subarray_with_sum(arr, target)
print("Subarray Found at indices:" if result != -1 else "No Subarray Found", result)
