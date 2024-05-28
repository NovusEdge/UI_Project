from kivy.properties import StringProperty

from kivy.config import Config
Config.set('graphics', 'width', '450')
Config.set('graphics', 'height', '900')

from kivymd.uix.appbar import MDTopAppBar, MDTopAppBarLeadingButtonContainer   
 
class BaseMDTopAppBar(MDTopAppBar):
    screen_name = StringProperty()
