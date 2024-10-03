class Animal:
    def __init__(self, genus, name, year_of_birth, color):
        self.genus = genus
        self.name = name
        self.year_of_birth = year_of_birth
        self.color = color
        
    def get_age(self, year):
        """you pass a year as a parameter and calculate the age of the animal at this year"""
        return year - self.year_of_birth
    
    def get_info(self):
        """prints a string like “Kaa is a python” or “Dumbo is an elephant” for a given instance"""
        return f"{self.name} is a {self.genus}"

    def dossier(self):
        return f"{self.name} ({self.genus}), Year of Birth: {self.year_of_birth}, Color: {self.color}"
    
animals = [
    Animal('elephant', 'Dumbo', 1941, 'grey'),
    Animal('python', 'Kaa', 1894, 'brown'),
    Animal('cat', 'Garfield', 2004, 'yellow'),
    Animal('lion', 'Simba', 1994, 'orange'),
    Animal('mouse', 'Stuart', 1999, 'white'),
    Animal('fish', 'Nemo', 2003, 'striped'),
    Animal('crocodile', 'Gena', 1966, 'green')
]

def find_oldest_animal(animals):
    oldest_animal = None
    current_year = 2024
    max_age = -1

    for animal in animals:
        age = animal.get_age(current_year)
        if age > max_age:
            max_age = age
            oldest_animal = animal

    return oldest_animal

oldest = find_oldest_animal(animals)
if oldest:
    print(f"The oldest animal is {oldest.name}, a {oldest.genus}, aged {oldest.get_age(2024)} years.")
    
def write_animals_to_file(animals, filename):
    with open('/home/jovyan/MyPy9/'+filename, 'w') as file:
        for animal in animals:
            file.write(f"{animal.name}, {animal.genus}\n")
            
write_animals_to_file(animals, 'animals_list.txt')