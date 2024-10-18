from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivymd.app import MDApp
import sys
import os

# اضافه کردن پوشه پروژه به مسیر پایتون
sys.path.append(os.path.dirname(os.path.abspath(__file__)))


class MainView(BoxLayout):
    def __init__(self, controller, **kwargs):
        super(MainView, self).__init__(**kwargs)
        self.controller = controller
        self.orientation = 'vertical'
        
        self.add_widget(Button(text="Add Dog", on_press=self.add_dog))
        self.add_widget(Button(text="Show Dogs", on_press=self.show_dogs))

    def add_dog(self, instance):
        self.controller.add_dog("Buddy", "Park", "Friendly dog")

    def show_dogs(self, instance):
        dogs = self.controller.get_dogs()
        for dog in dogs:
            print(f"Name: {dog['name']}, Location: {dog['location']}, Description: {dog['description']}")

class MainApp(MDApp):
    def build(self):
        from controllers.main_controller import MainController
        controller = MainController()
        return MainView(controller)

