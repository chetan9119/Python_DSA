import random

city_names = ['paris', 'london', 'newyork', 'france', 'berlin']

city_temp = {item:random.randint(20,32) for item in city_names}
print(city_temp)


new_dict = {city:temp for (city,temp) in city_temp.items() if temp > 25}
print(new_dict)