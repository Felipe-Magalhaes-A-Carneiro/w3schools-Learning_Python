login = input("User is:")
password = input("now use your password:")

if login == "admin" and password == "1234":
    print(f"Welcome {login}")
else:
    print("Invalid login")