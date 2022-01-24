import os
from kivy.resources import resource_add_path, resource_find
resource_add_path(os.path.abspath('./datas'))
from kivy.core.text import LabelBase
LabelBase.register('Roboto', 'SIMHEI.TTF')
from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.popup import Popup
from functools import partial
import glob

class MyImage(Image):
    def on_touch_up_func():
        pass
    def on_touch_down_func():
        pass
    def on_touch_down(self,touch):
        if self.collide_point(*touch.pos):
            self.on_touch_down_func()
    def on_touch_up(self,touch):
        if self.collide_point(*touch.pos):
            self.on_touch_up_func()

class fileImage(Image):
    def on_touch_down_func():
        pass
    def on_touch_down(self,touch):
        if self.collide_point(*touch.pos):
            self.on_touch_down_func()

def test():
    for root,dirs,files in os.walk('.'):
        return(root,dirs,files)

class filesLayout(BoxLayout):
    pass

class imgshow(App):
    imglist=[]
    pos=0
    mainlayout=FloatLayout()
    def build(self):
        self.imglist=glob.glob('./pics/*.jpg')+glob.glob('./pics/*.ico')
        self.add_interface()
        self.add_option()
        return self.mainlayout
    def add_interface(self):
        verlayout=BoxLayout(orientation='vertical')
        horlayout=BoxLayout(orientation='horizontal')
        flolayout=FloatLayout()
        button=Button(text='下一张',size_hint=(0.5,1),pos_hint={'x':0.5})
        button1=Button(text='上一张',size_hint=(0.5,1))
        flolayout.add_widget(button)
        flolayout.add_widget(button1)
        flolayout.size_hint=(1,0.3)
        button.on_press=self.nextpic
        button1.on_press=self.lastpic
        horlayout.spacing=10
        self.img1=Image(source=self.imglist[0])
        img2=Image(source='./pics/test2.jpg')
        horlayout.add_widget(self.img1)
        verlayout.add_widget(horlayout)
        verlayout.add_widget(flolayout)
        self.mainlayout.add_widget(verlayout)
        
    def add_option(self):
        self.imgxx=MyImage(source='./pics/xx2.png',size_hint=(0.1,0.1),pos_hint={'y':0.6})
        self.imgxx.on_touch_up_func=partial(self.callbackup,self.imgxx)
        self.imgxx.on_touch_down_func=partial(self.callbackdown,self.imgxx)
        #self.imgxx.bind(on_touch_down=self.xxtouch)
        # self.imgxx.on_touch_up=self.xxtouchup
        self.mainlayout.add_widget(self.imgxx)
    def on_touch_up(self,touch):
        print('on touch up')
        if self.imgxx.collide_point(*touch.pos):
            self.xxtouchup()
    def nextpic(self):
        print('next')
        self.pos=(self.pos+1)%len(self.imglist)
        self.img1.source=self.imglist[self.pos]
    def lastpic(self):
        self.pos=(self.pos-1)%len(self.imglist)
        self.img1.source=self.imglist[self.pos]
    def xxtouch(self,obj,touch):
        if self.imgxx.collide_point(*touch.pos):
            self.imgxx.source='./pics/xx1.png'
            print('xx touch')
    def xxtouchup(self,*args):
        self.imgxx.source='./pics/xx2.png'
        self.popup_file_window()
        print('xx touch up')
    def filechoosefunc(self,*args):
        print('filechoose function')
    def popup_file_window(self,*args):
        self.filechoose=FileChooserIconView()
        self.filechoose.path='C:\\Users\\tomst\\Desktop\\Icons'
        filechoose=BoxLayout(orientation='horizontal')
        img=Image(source='./pics/test.jpg')
        filechoose.add_widget(self.filechoose)
        popupwindow=Popup(title='file choose here',content=filechoose,size_hint=(None,None),size=(500,500))
        popupwindow.open()
    def callbackup(self,obj):
        print('callbackup')
        obj.source='./pics/xx2.png'
        self.popup_file_window()
    def callbackdown(self,obj):
        print('callbackdownfunc')
        obj.source='./pics/xx1.png'

if __name__=='__main__':
    #imgshow().run()
    print(test())