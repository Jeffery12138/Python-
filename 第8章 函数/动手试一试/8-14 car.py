def make_car_profile(manufacturer, model, **kwargs):
    """创建一个字典，包含车辆的已知所有信息"""
    car_profile = {}
    car_profile['manufacturer'] = manufacturer
    car_profile['model'] = model
    for key, value in kwargs.items():
        car_profile[key] = value

    return car_profile


car = make_car_profile('subaru', 'outback', color='blue', tow_package=True)
print(car)