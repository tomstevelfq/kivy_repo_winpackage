from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.app import runTouchApp

layout = StackLayout(size_hint=(1,None))
# Make sure the height is such that there is something to scroll.
#layout.bind(minimum_height=layout.setter('height'))
#layout.minimum_height=200
for i in range(100):
    btn = Button(text=str(i),size_hint_x=0.5, size_hint_y=None, height=40)
    layout.add_widget(btn)
root = ScrollView(size_hint=(1, None), size=(Window.width, Window.height))
root.add_widget(layout)

runTouchApp(root)