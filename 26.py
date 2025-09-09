#--------------------------------------------------------
#Check Balanced Parentheses
#-------------------------------------------------------
def is_balanced(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping:
            if not stack or mapping[char] != stack.pop():
                return False
    return not stack

# User Input
s = input("Enter a string with parentheses: ")
print("Is Balanced:", is_balanced(s))
