# Nested If: Number Range Check
# Write a program that checks if a number is between 1 and 100.
# If true, check if it is divisible by 2.
# Print "In range and even", or "In range but odd".
num=3
if num>1 and num<100:
    if num%2==0:
        print("In range and even")
    else:
        print("In range but odd")        