from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from views.main_view import MainView
from views.profile_view import ProfileView

class MainApp(MDApp):
    def build(self):
        Builder.load_file('views/main_view.kv')
        Builder.load_file('views/profile_view.kv')
        
        screen_manager = MDScreenManager()
        screen_manager.add_widget(MainView(name='main'))
        screen_manager.add_widget(ProfileView(name='profile'))
        
        return screen_manager

if __name__ == "__main__":
    MainApp().run()

