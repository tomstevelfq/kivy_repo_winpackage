import luanma
from kivy.app import App
from fileNaviBar import fileNaviBar
from kivy.uix.stacklayout import StackLayout
from kivy.graphics import Color,Rectangle
from fileListLayout import scrollFileView
import os

class mainInterface(StackLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.spacing=10
        with self.canvas:
            Color(0.1484,0.1680,0.1836,1)
            self.rt=Rectangle()
        self.bind(size=self.update,pos=self.update)
        for root,dirs,files in os.walk(os.getcwd()):
            break
        self.flist=scrollFileView(path=os.getcwd())
        fnavi=fileNaviBar(fun=self.flist.predir,size_hint=(1,None),height=40)
        self.flist.updatePath=fnavi.showpath
        self.flist.update()
        self.add_widget(fnavi)
        self.add_widget(self.flist)
    def update(self,*args):
        self.rt.pos=self.pos
        self.rt.size=self.size

class fileApp(App):
    def build(self):
        return mainInterface()

if __name__=='__main__':
    fileApp().run()