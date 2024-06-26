from kivy.lang import Builder
from kivy.properties import StringProperty, BooleanProperty

from kivy.config import Config
Config.set('graphics', 'width', '450')
Config.set('graphics', 'height', '900')

from kivymd.app import MDApp
from kivymd.uix.navigationbar import MDNavigationBar, MDNavigationItem
from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import SlideTransition
from kivy_garden.mapview import MapView, MapMarker
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.button import MDFabButton
from kivymd.uix.appbar import MDTopAppBar
from kivy.uix.image import Image
from kivymd.uix.navigationrail import MDNavigationRail, MDNavigationRailItem

from components.navbar import *
from components.settings_list import *
from components.top_bar import *

item_direction = ""

class BaseScreen(MDScreen):
    pass

class Example(MDApp):
    rail_visible = BooleanProperty(False)

    def on_switch_tabs(
        self,
        bar: MDNavigationBar,
        item: MDNavigationItem,
        item_icon: str,
        item_text: str,
    ):
        global item_direction
        if item_text == "Menu":
            item_direction = "right"
        elif item_text == "Friends":
            item_direction = "left"
        else:
            if item_direction == "right":
                item_direction = "left"
            else:
                item_direction = "right"

        self.root.ids.screen_manager.transition = SlideTransition(direction=item_direction)
        self.root.ids.screen_manager.current = item_text

    def switch_screen(self, screen_name):
        self.root.ids.screen_manager.current = screen_name
        self.root.ids.nav_rail.set_active_item(None)
        self.root.ids.nav_bar.set_active_item(None)
    
    def on_emergency_button_press(self):
        print("Emergency button pressed")

    def build(self):
        with open("kv/map_view.kv", "r") as kv:
            return Builder.load_string(kv.read())
    
    def search_callback(self):
        print("Search button pressed")

    def toggle_nav_rail(self):
        self.rail_visible = not self.rail_visible

Example().run()
