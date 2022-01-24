from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from tools import MyImage

class FileImage(MyImage):
    def __init__(self,par,**kwargs):
        super().__init__(**kwargs)
        self.par=par
    def on_touch_up_func(self, *args):
        self.par.updateFileList()

class fileIcon(BoxLayout):
    def __init__(self,par,iconpath='./pics/fileicon.png',fname='fname',**kwargs):
        super().__init__(**kwargs)
        fileimg=FileImage(par=par,source=iconpath,size_hint=(1,0.8))
        filename=Label(text=fname,size_hint=(1,0.2))
        self.orientation='vertical'
        self.add_widget(fileimg)
        self.add_widget(filename)
        self.bind(width=self.setter('height'))
    def on_touch_function(self,path,par):
        pass

class dirIcon(BoxLayout):
    def __init__(self,iconpath='./pics/diricon.png',fname='dirname',**kwargs):
        super().__init__(**kwargs)
        fileimg=Image(source=iconpath,size_hint=(1,0.8))
        filename=Label(text=fname,size_hint=(1,0.2))
        self.orientation='vertical'
        self.add_widget(fileimg)
        self.add_widget(filename)
        self.bind(width=self.setter('height'))

