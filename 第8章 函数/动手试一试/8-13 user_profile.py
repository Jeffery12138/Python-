def build_profile(first, last, **kwargs):
    """创建一个字典，包含用户的已知一切信息"""
    profile = {}
    profile['fisrt_name'] = first
    profile['last_name'] = last
    for key, value in kwargs.items():
        profile[key] = value

    return profile


my_profile = build_profile('Jiawei', 'Zhang', age=28, height=175, location='Shanghai')
print(my_profile)