from kivy.app import App
from kivy.uix.stacklayout import StackLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from fileicon import fileIcon,dirIcon
from kivy.uix.label import Label
import os
from kivy.uix.image import Image
from tools import MyImage
from functools import partial

class fileIcon(BoxLayout):
    def __init__(self,fun=None,iconpath='./pics/fileicon.png',fname='fname',**kwargs):
        super().__init__(**kwargs)
        fileimg=MyImage(source=iconpath,size_hint=(1,0.8))
        if fun!=None:
            fileimg.on_touch_up_func=partial(fun,name=fname)
        filename=Label(text=fname[0:10],size_hint=(1,0.2),font_size=13)
        self.orientation='vertical'
        self.add_widget(fileimg)
        self.add_widget(filename)
        self.bind(width=self.setter('height'))

class dirIcon(BoxLayout):
    def __init__(self,fun=None,iconpath='./pics/diricon.png',fname='dirname',**kwargs):
        super().__init__(**kwargs)
        fileimg=MyImage(source=iconpath,size_hint=(1,0.8))
        if fun!=None:
            fileimg.on_touch_up_func=partial(fun,name=fname)
        filename=Label(text=fname[0:10],size_hint=(1,0.2),font_size=13)
        self.orientation='vertical'
        self.add_widget(fileimg)
        self.add_widget(filename)
        self.bind(width=self.setter('height'))

class FileApp(App):
    def build(self):
        return scrollFileView(os.getcwd())

class scrollFileView(ScrollView):
    def __init__(self,path,**kwargs):
        self.path=path
        super().__init__(**kwargs)
        self.st=StackLayout(size_hint=(1,None),spacing=10)
        self.add_widget(self.st)
        self.st.bind(minimum_height=self.st.setter('height'))
        self.size_hint=(1,1)
        self.update()
    def update_dir(self,name,*args):
        print('dir',name)
        self.path=os.path.join(self.path,name)
        print(self.path)
        self.update()
    def update_file(self,name,*args):
        print('file',name)
    def update(self):
        self.st.clear_widgets()
        dirs=files=[]
        for root,dirs,files in os.walk(self.path):
            break
        for i in dirs:
            self.st.add_widget(dirIcon(fun=self.update_dir,fname=i,size_hint=(0.1,None)))
        for i in files:
            self.st.add_widget(fileIcon(fun=self.update_file,fname=i,size_hint=(0.1,None)))
        self.updatePath(path=self.path)
    def predir(self):
        self.path=os.path.dirname(self.path)
        self.update()
    def updatePath(self,path=''):
        pass

if __name__=='__main__':
    FileApp().run()