import json


def get_new_favorite_num():
    """提示用户输入喜欢的数字，并存储到文件中"""
    filename = 'favorite_number.json'
    favorite_num = input("Enter your favorite num:")
    with open(filename, 'w') as f_obj:
        json.dump(favorite_num, f_obj)
    return favorite_num


def get_stored_favorite_num():
    """读取存在的数字，如果不存在返回None"""
    filename = 'favorite_number.json'
    try:
        with open(filename) as f_obj:
            favorite_num = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return favorite_num


def greet_user():
    """问候用户，指出他喜欢的数字"""
    favorite_num = get_stored_favorite_num()
    if favorite_num:
        print("I know your favorite number! It's " + str(favorite_num) + ".")
    else:
        favorite_num = get_new_favorite_num()
        print("I'll memorize you favorite number is " + str(favorite_num) + ".")


greet_user()