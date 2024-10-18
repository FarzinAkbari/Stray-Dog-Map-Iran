
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy_garden.mapview import MapView, MapMarker
from kivymd.app import MDApp
from kivymd.uix.toolbar import MDToolbar
from kivymd.uix.button import MDFloatingActionButton
from kivymd.uix.label import MDLabel
from kivy.uix.screenmanager import Screen, ScreenManager

class MainView(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.build_ui()

    def build_ui(self):
        layout = BoxLayout(orientation='vertical')

        toolbar = MDToolbar(title="Stray Dog Map Iran")
        toolbar.md_bg_color = 0, 0, 0, 1
        toolbar.specific_text_color = 1, 1, 0, 1
        toolbar.right_action_items = [["account", lambda x: self.change_to_profile()]]

        layout.add_widget(toolbar)

        self.mapview = MapView(lat=35.6892, lon=51.3890, zoom=10)
        layout.add_widget(self.mapview)

        fab = MDFloatingActionButton(icon="plus", md_bg_color=(1, 1, 0, 1))
        fab.pos_hint = {"center_x": 0.5, "center_y": 0.1}
        fab.bind(on_press=self.report_dog)

        layout.add_widget(fab)
        self.add_widget(layout)

    def on_enter(self):
        marker = MapMarker(lat=35.6892, lon=51.3890)
        self.mapview.add_marker(marker)

    def change_to_profile(self):
        self.manager.current = 'profile'

    def report_dog(self, instance):
        print("Report a Dog functionality triggered!")

class ProfileView(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.build_ui()

    def build_ui(self):
        layout = BoxLayout(orientation='vertical')

        toolbar = MDToolbar(title="Profile")
        toolbar.md_bg_color = 0, 0, 0, 1
        toolbar.specific_text_color = 1, 1, 0, 1
        toolbar.left_action_items = [["arrow-left", lambda x: self.change_to_main()]]

        layout.add_widget(toolbar)

        profile_label = MDLabel(text="User Profile", halign="center", theme_text_color="Custom")
        profile_label.text_color = 1, 1, 0, 0.8
        profile_label.pos_hint = {"center_x": 0.5, "center_y": 0.5}
        
        layout.add_widget(profile_label)
        self.add_widget(layout)

    def change_to_main(self):
        self.manager.current = 'main'

class MainApp(MDApp):
    def build(self):
        self.screen_manager = ScreenManager()
        self.screen_manager.add_widget(MainView(name="main"))
        self.screen_manager.add_widget(ProfileView(name="profile"))
        return self.screen_manager

    def on_start(self):
        self.screen_manager.get_screen('main').on_enter()

if __name__ == '__main__':
    MainApp().run()
