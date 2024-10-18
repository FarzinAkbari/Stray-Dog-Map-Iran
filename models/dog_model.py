class DogModel:
    def __init__(self):
        self.dogs = []

    def add_dog(self, name, location, description):
        dog = {"name": name, "location": location, "description": description}
        self.dogs.append(dog)

    def get_dogs(self):
        return self.dogs

