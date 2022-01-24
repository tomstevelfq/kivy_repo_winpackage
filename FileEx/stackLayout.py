from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.stacklayout import StackLayout
from kivy.graphics import Rectangle,Color
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
 
class StackLayoutWidget(StackLayout):
    def __init__(self,**kwargs):
        super(StackLayoutWidget, self).__init__(**kwargs)
 

        #遍历添加按钮
        for i in range(50):
            btn=Button(text=str(i),size_hint=(0.2,None))
            btn.bind(width=self.btnwidth)
            self.add_widget(btn)
    
    def btnwidth(self,obj,width,*args):
        obj.height=obj.width
 
    def update_rect(self,*args):
        self.rect.pos=self.pos
        self.rect.size=self.size
 
class StackApp(App):
    def build(self):
        ly=StackLayoutWidget(size_hint=(1,None))
        scview=ScrollView(size_hint=(1,None), size=(Window.width, Window.height))
        scview.add_widget(ly)
        return scview
 
if __name__ =="__main__":
    StackApp().run()