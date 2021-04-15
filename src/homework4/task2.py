# The function takes as input a list of countries and cities for each country.
# For each city from the list with requests, the function prints the name of the country
# to which the city belongs.
# Initial data:
# n - number of countries
# countries - string with countries
# m - number of requests
# cities - string with cities


def find_country(n, countries, m, cities):
    list_of_countries = countries.split("\n")
    list_of_cities = cities.split("\n")
    country_city = {}
    for i in range(n):
        value, *keys = list_of_countries[i].split()
        dict_ = dict().fromkeys(keys, value)
        country_city.update(dict_)
    for i in range(m):
        print(country_city.get(list_of_cities[i].strip()))


string_of_countries = """Russia Moscow Petersburg Novgorod Kaluga
                         Ukraine Kiev Donetsk Odessa"""
string_of_cities = """Odessa
                      Moscow
                      Novgorod
                      Gomel"""
find_country(2, string_of_countries, 3, string_of_cities)