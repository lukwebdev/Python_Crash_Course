current_users = ["mark", "john", "big", "EVE", "mario"]
new_users = ["MAYA", "zen", "big", "luk", "Eve"]
current_users_lower = [user.lower() for user in current_users]

# print(current_users_lower)

for new_user in new_users:
    if new_user in current_users:
        print(f"Sorry {new_user} is taken, please enter a new username")
    else:
        print(f"{new_user} - username is availble")

# for new_user in new_users:
#     if new_user.lower() in current_users_lower:
#         print(f"Sorry {new_user} is taken, please enter a new username")
#     else:
#         print(f"{new_user} - username is availble")