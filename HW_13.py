# Task 1 / Task 2 

class Country:
    def __init__(self, name, population):
        self.name = name
        self.population = population
        
    def add(self, other_country):
        """
        Combines the current country with another country to create a new Country object
        with the combined name and population.

        Args:
            other_country (Country): Another Country object to be combined with.

        Returns:
            Country: A new Country object with the combined name and population.
        """
        combinated_name = f'{self.name} {other_country.name}'
        combined_population = self.population + other_country.population
        
        return Country(combinated_name, combined_population)
    
    def __str__(self):
        return f'Country: {self.name}, Population {self.population}'
    
    def __add__(self, other ):
        """
        Adds two Country objects together to create a new Country object.

        Args:
            other (Country): Another Country object to add.

        Returns:
            Country: A new Country object with the combined name and population.
        """
        combinated_name = f'{self.name} {other.name}'
        combined_population = self.population + other.population
        return Country(combinated_name, combined_population)
        


bosnia = Country('Bosnia', 10_000_000)
herzegovina = Country('Herzegovina', 5_000_000)

bosnia_herzegovina = bosnia.add(herzegovina)
print(bosnia_herzegovina)

print(bosnia_herzegovina.population)
print(bosnia_herzegovina.name)


bosnia_herzegovina_2 = bosnia + herzegovina
print(bosnia_herzegovina_2)


# Task 3
class Car():
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = 0
    
    def accelerate(self):
        self.speed += 5
        
    def brake(self):
        if self.speed >= 5:
            self.speed -= 5
        else:
            self.speed = 0
    
    def display_speed(self):
        print(f'Current speed of {self.brand} {self.model} ({self.year}): {self.speed} km/h')

car_1 = Car('Jeep', 'Renegate', 2021)

car_1.accelerate()
car_1.display_speed()
car_1.accelerate()
car_1.display_speed()

car_1.brake()
car_1.display_speed()
car_1.brake()
car_1.display_speed()

