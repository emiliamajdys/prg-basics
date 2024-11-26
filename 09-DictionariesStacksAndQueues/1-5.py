countries = [
{"name":"Poland", "population":38000000},
{"name":"Sweden", "population":10000000},
{"name":"Norway", "population":5000000},
{"name":"Cambodia", "population":16000000},
{"name":"Grecce", "population":10000000},
]


print(f'COUNTRY  POPULATION')
print('-------------------')
for dict in countries:
   print(dict['name'], dict["population"])