from kivy.uix.label import Label

class MapLayout(Label):
    def __init__(self, **kwargs):
        super(MapLayout, self).__init__(**kwargs)
        self.text = 'Map Layout'

    def on_touch_down(self, touch):
        print('MapLayout touched')
        return super(MapLayout, self).on_touch_down(touch)
    