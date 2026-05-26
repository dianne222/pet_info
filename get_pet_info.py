from pet import Pet

pet1 = Pet()

def get_pet_info():
    name = input("Enter your's pet name:")
    animal_type = input("Enter your animal's type:")
    age = int(input("Enter your age:"))

def store_pet_info(name, animal_type, age):
    pet1.set_name(name)
    pet1.set_animal_type(animal_type)
    pet1.set_age(age)

def display_pet_info():
    print("Pet Information")
    print("Name:", pet1.get_name())
    print("Animal Type:", pet1.get_animal_type())
    print("Age:", pet1.get_age())
    print("")

get_pet_info()
store_pet_info()
display_pet_info()