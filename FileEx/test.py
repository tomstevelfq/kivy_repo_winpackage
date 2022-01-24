from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
import copy

class fileLayout(BoxLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.bind(size=self.update)
    def update(self,*args):
        print('file layout',self.size)

class testApp(App):
    def build(self):
        file=fileLayout(orientation='horizontal')
        print('after file create')
        print(file.size)
        mfile=BoxLayout(orientation='vertical')
        img=Image(source='./pics/test.jpg')
        img1=Image(source='./pics/test.jpg')
        img2=Image(source='./pics/test.jpg')
        img3=Image(source='./pics/test.jpg')
        img4=Image(source='./pics/test.jpg')
        img5=Image(source='./pics/test.jpg')
        file.add_widget(img)
        file.add_widget(img1)
        file.add_widget(img2)
        file.add_widget(img3)
        file.add_widget(img4)
        file.add_widget(img5)
        mfile.add_widget(file)
        
        return mfile

def testa(b,**kwargs):
    print(b,kwargs)
#testApp().run()

#testa(a=23,b=89,c=888)

class testApp1(App):
    def build(self):
        b=BoxLayout(orientation='vertical')
        b.add_widget(Image(source='./pics/test.jpg',size_hint=(1,0.5)))
        b.add_widget(Image(source='./pics/test.jpg',size_hint=(1,0.3)))
        f=FloatLayout()
        f.add_widget(Image(source='./pics/test.jpg',size_hint=(1,0.5),pos_hint={'top':1}))
        f.add_widget(Image(source='./pics/test.jpg',size_hint=(1,0.3),pos_hint={'y':0.2}))
        return f
#testApp1().run()

class b():
    def bb():
        print('bb')

class a():
    val=12
    def __init__(self):
        self.bb=b(bb=self.update)
    def update(self):
        print('update',self.val)

import os
print('hello',os.path.isfile('C:/Users/tomst/「开始」菜单'))
for root,dir,file in os.walk('C:/Users/tomst/「开始」菜单'):
    print(root,dir,file)

