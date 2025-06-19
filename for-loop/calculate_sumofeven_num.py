# Use a for loop to calculate the sum of all even numbers between 1 and 20. 
# Display the total sum after the loop finishes.
total=0
for num in range(1,20):
    if num % 2==0:
        total=num+total
       
print(total)


