from pet import Pet

pet1 = Pet()

def get_pet_info():
    name = input("Enter your's pet name:")
    animal_type = input("Enter your animal's type:")
    age = int(input("Enter your age:"))

def store_pet_info():
    pet1.set_name(name)
    pet1.set_animal_type(animal_type)
    pet1.set_age(age)