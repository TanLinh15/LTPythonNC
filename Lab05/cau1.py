from Country import Country
#cau a:
canada = Country('Cananda', 34482779, 9984670)
canada.name
print('canada.name ->',canada.name)
print('canada.population ->',canada.population)
print('canada.area ->',canada.area)

#cau b:
usa = Country('United States of America', 313914040, 9826675)
print('canada.is_larger(usa) -> ',canada.is_larger(usa))

#cau c:
print('canada.population_density -> ', canada.population_density())

#cau d:
usa = Country('United States of America', 313914040, 9826675)
print('usa ->', usa)

#cau e:
canada = Country('Canada', 34482779, 9984670)
print(canada)
[canada]
print([canada])

