from kv.lib import *

class Residri(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.item_direction = ""
    
    def on_switch_tabs(
        self,
        bar: MDNavigationBar,
        item: MDNavigationItem,
        item_icon: str,
        item_text: str,
    ):
        if item_text == "Menu":
            self.item_direction = "right"
        elif item_text == "Settings":
            self.item_direction = "left"
        else:
            if self.item_direction == "right":
                self.item_direction = "left"
            else:
                self.item_direction = "right"

        self.root.ids.screen_manager.transition = SlideTransition(direction=self.item_direction)
        self.root.ids.screen_manager.current = item_text

    def on_emergency_button_press(self):
        print("Emergency button pressed")

    def build(self):
        return Builder.load_file("kv/map_page.kv")
    
    def search_callback(self):
        print("Search button pressed")


Residri().run()
