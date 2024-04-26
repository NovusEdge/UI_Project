import kivy
kivy.require('2.3.0')

from kivy.app import App

# Layouts
from kivy.uix.boxlayout import BoxLayout
from widgets.map import MapLayout

# Widgets

from kivy.lang.builder import Builder

class UIApp(App):
    def load_modules(self):
        ''' Load the modules for the UI '''
        Builder.load_file('graphics/map_layout.kv')

    def build(self):
        ''' Build the UI '''
        root = BoxLayout()
        root.add_widget(MapLayout())

        return root
