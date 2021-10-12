class Country:
    def __init__(self, name, population, area):
        self.name = name
        self.population = population
        self.area = area

    def is_larger(self, objCountry):
        if self.arena > objCountry.area:
            return True
        else:
            return False