def get_city_country(city, country, population=''):
    """ Generate a 'City, Country' str."""
    city_country = city + ", " + country
    city_country = city_country.title()
    if population:
        city_country_population = city_country + "-population" + str(population)
        return city_country_population
    else:
        return city_country