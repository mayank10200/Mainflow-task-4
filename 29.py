#--------------------------------------
#Check Pythagorean Triplet
#--------------------------------------
def is_pythagorean_triplet(a, b, c):
    sides = sorted([a, b, c])
    return sides[0]**2 + sides[1]**2 == sides[2]**2

# User Input
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
print("Is Pythagorean Triplet:", is_pythagorean_triplet(a, b, c))
