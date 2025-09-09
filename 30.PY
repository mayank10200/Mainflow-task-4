#------------------------------------
#bubble sort
#-----------------------------------
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# User Input
arr = list(map(int, input("Enter numbers to sort (space-separated): ").split()))
print("Sorted Array:", bubble_sort(arr))
