from kivymd.uix.screen import MDScreen
from kivy_garden.mapview import MapMarker

class MainView(MDScreen):
    def on_enter(self, *args):
        if 'mapview' in self.ids:
            self.mapview = self.ids.mapview
            print(f"MapView loaded: {self.mapview}")
        else:
            print("MapView not found in ids")

    def add_map_marker(self):
        if not hasattr(self, 'mapview'):
            self.on_enter()
        marker = MapMarker(lat=35.6892, lon=51.3890)
        self.mapview.add_marker(marker)
