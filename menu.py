from kivy.uix.relativelayout import RelativeLayout 
from kivy.properties import StringProperty 
#from kivy.uix.button import Button
class Menu(RelativeLayout):
     menu_title=StringProperty("G  A  L  A  X  Y")
     button_title=StringProperty("Start")
     def on_touch_down(self,touch):
         if self.opacity==0:
             return False
         return super(RelativeLayout,self).on_touch_down(touch)
     
 