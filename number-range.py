# Number Range Check
# Write a program to check if a number is between 1 and 100.
# If it is, check if it's also a multiple of 5.
# Print "Valid multiple of 5 in range" or "Not a multiple of 5"
num=79
if num>=1 and num <=100:
    if num%5==0:
        print("vaild multiple of 5 in range")
    else:
        print("Not a multiple of 5")    
