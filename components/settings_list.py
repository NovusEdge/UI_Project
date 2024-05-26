from kivy.lang import Builder
from kivy.properties import StringProperty

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

class SettingsView(MDScreen):
    items = [
        {"icon": "account", "text": "Account"},
        {"icon": "bell", "text": "Notifications"},
        {"icon": "cog", "text": "Tab 3"},
        {"icon": "help", "text": "Help"},
    ]
        
class SettingsListItem(MDNavigationItem):
    icon = StringProperty()
    text = StringProperty()