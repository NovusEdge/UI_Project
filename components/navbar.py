from kivymd.uix.navigationbar import MDNavigationBar, MDNavigationItem
from kivy.lang import Builder
from kivy.properties import StringProperty


class BaseMDNavigationItem(MDNavigationItem):
    icon = StringProperty()
    text = StringProperty()

class BaseMDNavigationBar(MDNavigationBar):
    pass
