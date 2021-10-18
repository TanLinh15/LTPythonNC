#cau a:
class Country:
    def __init__(self, name, population, area):
        self.name = name
        self.population = population
        self.area = area
#cau b:
    def is_larger(self, other):
        if isinstance(other,Country):
            return self.area > other.area
        else:
            print("Both objects need to be from class Country")
            return -1
#cau c:   
    def population_density(self):
        return (self.population / self.area)
#cau d:
    def __str__(self):
        return ("{0} has a population of {1} and its area is {2} square kilometers.".format(self.name,self.population,self.area))
#cau e:    
    def __repr__(self):
        return "{0}({1},{2},{3})".format(self.__class__.__name__,self.name,self.population,self.area)

#Cau 2:
class Continent(Country):
    def __init__(self,continentName,countryList):
        self.continentName = continentName
        self.countryList = countryList[:]
    
    def total_population(self):
        populationSum = 0
        for i in range(len(self.countryList)):
            populationSum = populationSum + self.countryList[i].population
        return populationSum

    def __str__(self):
        output = self.continentName + "\n"
        for i in self.countryList:
            output = output + i.__str__() + "\n"
        return output

