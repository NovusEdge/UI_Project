from kivy.lang import Builder
from kivy.properties import StringProperty

from kivy.config import Config
Config.set('graphics', 'width', '450')
Config.set('graphics', 'height', '900')

from kivymd.uix.screen import MDScreen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.list import OneLineAvatarListItem
      
class SettingsListItem(OneLineAvatarListItem):
    text = StringProperty()
    source = StringProperty()

class SettingsScreen(Screen):
    pass