from kivy.uix.floatlayout import FloatLayout
from kivy.app import App
from kivy.uix.image import Image
from clickableImg import MyImage
from kivy.uix.label import Label
from kivy.graphics import Color,Rectangle,Line
import os

class topNaviBar(FloatLayout):
    def __init__(self,path,**kwargs):
        super().__init__(**kwargs)
        self.path=path
        self.arrowimg=MyImage(source='./pics/arrow-left-l.png',size_hint=(0.1,None))
        self.arrowimg.bind(width=self.update_arrow)
        self.add_widget(self.arrowimg)
        self.lab=Label(text='hello world',size_hint=(0.9,None),pos_hint={'x':0.1},halign='left',valign='center',padding=[10,0])
        with self.lab.canvas:
            Color(1,0,0,0.5)
            self.labline=Line(width=1.5,rectangle=(self.lab.x,self.lab.y,500,100))
        self.lab.bind(size=self.update_lab,pos=self.update_lab)
        self.lab.bind(size=self.lab.setter('text_size'))
        self.add_widget(self.lab)
    def update_arrow(self,obj,width,*args):
        self.arrowimg.height=width
        self.lab.height=width
    def update_lab(self,obj,size,*args):
        self.labline.rectangle=(self.lab.x,self.lab.y+self.lab.height*0.15,self.lab.width,self.lab.height*0.7)

class MyLabel(Label):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.text='hello world'
        self.color=(1,0,0,1)
        with self.canvas:
            c=Color(1,0.3,0,0.4)
            #self.rect=Rectangle(pos=self.pos,size=self.size)
            self.rect=Line(rectangle=(0,0,200,200),width=10,dashs=[2,3,4,5])
        #self.bind(pos=self.update_rect)
        self.bind(size=self.update_rect)
    def update_rect(self,*args):
        #self.rect.pos=self.pos
        self.rect.rectangle=(self.pos[0],self.pos[1],self.width,self.height)

class test(App):
    def build(self):
        return topNaviBar(path=os.getcwd())

if __name__=='__main__':
    test().run()

        