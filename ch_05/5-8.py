users = ["mark", "john", "admin", "eve", "mario"]
for user in users:
    if user == "admin":
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {user.title()},are you ready?")