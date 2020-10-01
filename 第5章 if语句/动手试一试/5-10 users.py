current_users = ['Eric', 'Bob', 'Susan', 'Lily', 'Franklin']
new_users = ['boB', 'susan', 'LILY', 'Jeffery', 'Tom']
for new_user in new_users:
    if new_user.lower().title() in current_users:
        print("The user id " + new_user + " has been used, you need input another user id.")
    else:
        print("The user id " + new_user + " has never been used.")