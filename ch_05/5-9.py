users = []

if users:
    for user in users:
        if user == "admin":
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {user.title()},are you ready?")
else:
    print("We need find some users !!!")