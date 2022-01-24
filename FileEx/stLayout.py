from kivy.uix.stacklayout import StackLayout
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout

class MyImage(Image):
    def __init__(self,**kwargs):
        if 'layobj' in kwargs:
            self.layobj=kwargs['layobj']
            kwargs.pop('layobj')
        super().__init__(**kwargs)
        self.bind(width=self.update)
    def update(self,obj,width,*args):
        self.height=width
        if hasattr(self,'layobj'):
            print('minimum height',self.layobj.height,self.layobj.minimum_height)

class MyButton(Button):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.bind(width=self.setter('height'))

class MyStackLayout(StackLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.add_widget(MyImage(layobj=self,source='./pics/test.jpg',size_hint=(0.2,None)))
        for i in range(100):
            self.add_widget(MyButton(text=str(i),size_hint=(0.2,None)))

class TestApp(App):
    def build(self):
        blayout=BoxLayout(orientation='vertical')
        mstack=MyStackLayout(size_hint=(1,None))
        mstack.bind(minimum_height=mstack.setter('height'))
        scView=ScrollView(size_hint=(1,1))
        scView.add_widget(mstack)
        blayout.add_widget(MyImage(source='./pics/test.jpg',size_hint=(0.15,None)))
        blayout.add_widget(scView)
        return blayout

TestApp().run()