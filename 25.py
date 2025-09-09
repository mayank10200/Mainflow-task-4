#---------------------------------------------------------------
#Find Missing Number
#---------------------------------------------------------------
def find_missing_number(nums):
    n = len(nums) + 1
    total = n * (n + 1) // 2
    return total - sum(nums)

# User Input
nums = list(map(int, input("Enter numbers separated by space (1 to n+1 with one missing): ").split()))
print("Missing Number:", find_missing_number(nums))
