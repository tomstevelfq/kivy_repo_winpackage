from kivy.uix.image import Image

class MyImage(Image):
    def on_touch_up_func(self,*args):
        pass
    def on_touch_down_func(self,*args):
        pass
    def on_touch_down(self,touch):
        if self.collide_point(*touch.pos):
            self.on_touch_down_func(touch)
    def on_touch_up(self,touch):
        if self.collide_point(*touch.pos):
            self.on_touch_up_func()
