from kivy.lang import Builder
from kivy.properties import StringProperty

from kivymd.app import MDApp
from kivymd.uix.navigationbar import MDNavigationBar, MDNavigationItem
from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import SlideTransition
from kivy_garden.mapview import MapView, MapMarker
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.button import MDFabButton
from kivymd.uix.appbar import MDTopAppBar
from kivy.uix.image import Image

item_direction = ""

class BaseMDNavigationItem(MDNavigationItem):
    icon = StringProperty()
    text = StringProperty()


class BaseScreen(MDScreen):
    pass



