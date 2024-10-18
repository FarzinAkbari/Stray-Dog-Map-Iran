from models.dog_model import DogModel

class MainController:
    def __init__(self):
        self.model = DogModel()

    def add_dog(self, name, location, description):
        self.model.add_dog(name, location, description)

    def get_dogs(self):
        return self.model.get_dogs()

