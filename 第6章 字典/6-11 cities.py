cities = {
    'Shanghai': {
        'country': 'China',
        'population': '24.2814 million',
        'fact': 'Shanghai is China\'s financial center.',
    },
    'Tokyo': {
        'country': 'Japan',
        'population': '13.92 million',
        'fact': 'The central city of Tokyo metropolitan area, one of Japan\'s three major metropolitan areas.',
    },
    'New York': {
        'country': 'USA',
        'population': '8.62 million',
        'fact': 'The headquarters of the United Nations and the headquarters of many international organizations '
                'and multinational companies in the world are located in New York.',
    },
}
for city, city_info in cities.items():
    print("\nCity: " + city)
    print("\tCountry: " + city_info['country'])
    print('\tPopulation: ' + city_info['population'])
    print('\tFact: ' + city_info['fact'])
    