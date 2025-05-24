# Login System (Nested If)
# Create a simple login system:
# If username is "admin", check if password is "1234"
# Print "Access granted" or "Incorrect password" accordingly
# If username is incorrect, print "Unknown user"

username= "admin"
password= 12
if username=="admin":
    if password==1234:
        print("Access granted")
    else:
        print("Incorrect Password")
else:
    print("unknown user")           
