from Country import Country
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