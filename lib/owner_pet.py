# lib/pet_owner.py

class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        self.name = name
        if pet_type in Pet.PET_TYPES:
            self.pet_type = pet_type
        else:
            raise Exception(f"{pet_type} is not a valid pet type.")
        self.owner = owner
        Pet.all.append(self)


class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("Provided object is not of type Pet.")
        pet.owner = self

    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda pet: pet.name)


# Example usage (you can remove this when testing):
# owner = Owner("Alice")
# pet1 = Pet("Buddy", "dog", owner)
# pet2 = Pet("Whiskers", "cat", owner)
# print(owner.get_sorted_pets())
