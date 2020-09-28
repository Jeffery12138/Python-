# for循环是一种遍历列表的有效方式，但在for循环中不应修改列表，否则将导致Python难以跟踪其中的元素。
# 要在遍历列表的同时对其进行修改，可使用while循环

# 7.3.1 在列表之间移动元素
# 首先，创建一个待验证用户列表
unconfirmed_users = ['alice', 'brian', 'candace']
# 和一个用于存储已验证用户的空列表
confirmed_users = []

# 验证每个用户，直到没有未验证用户为止
while unconfirmed_users:
    # 将每个经过验证的用户都移到已验证用户列表中
    current_user = unconfirmed_users.pop()
    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)

# 显示所有已验证的用户
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())