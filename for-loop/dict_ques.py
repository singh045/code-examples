# Given the dictionary ages = {"Alice": 25, "Bob": 30, "Charlie": 35}, use a for loop to iterate through the dictionary and print each key-value 
# pair in the format: "Name: Alice, Age: 25".
ages = {"Alice": 25, "Bob": 30, "Charlie": 35}

for key,value in ages.items():
    print(f"Name: {key}, Age: {value}")