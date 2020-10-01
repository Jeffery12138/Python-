def city_country(city, country):
    info = city.title() + ", " + country.title()
    return info


city_info = city_country('shanghai', 'china')
print(city_info)
city_info = city_country('santiago', 'chile')
print(city_info)
city_info = city_country('tokyo', 'japan')
print(city_info)