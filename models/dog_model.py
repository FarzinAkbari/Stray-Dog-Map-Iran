class DogModel:
    def __init__(self):
        self.dogs = []

    def add_dog(self, name, location, description, latitude, longitude):
        dog = {"name": name, "location": location, "description": description, "latitude": latitude, "longitude": longitude}
        self.dogs.append(dog)

    def get_dogs(self):
        return self.dogs

