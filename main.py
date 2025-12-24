from kivy.config import Config
Config.set('graphics','width','760')
Config.set('graphics','height','1500')

from kivy.app import App 
from kivy.uix.relativelayout import RelativeLayout
from kivy.properties import NumericProperty,Clock,ObjectProperty,StringProperty 
from kivy.graphics.vertex_instructions import Line,Ellipse,Rectangle,Quad,Triangle 
from kivy.graphics.context_instructions import Color
from kivy.lang import Builder
#from pygame import mixer 
from kivy.core.audio import SoundLoader 
import random 
import menu

Builder.load_file("menu.kv")
#mixer.init()

class Mainwidget(RelativeLayout):
    from update import update_x,update_y,update,get_line_x,get_line_y,get_tile,get_actual_coordinates,update_ship,ship_collision_with_tile,ship_collision
    from transform import transform,transform_perspective,transform_2d
    perspectivepoint_x=NumericProperty(0)
    perspectivepoint_y=NumericProperty(0)
  
    menu_widget=ObjectProperty()
    score=StringProperty("score:0")
  
    line_list_y=[]
    line_list_x=[]
    Nb_lines_y=8
    Nb_lines_x=8
    spacing=0.4
    spacing_x=0.1
    line_point_y=0
    line_point_x=0
    current_offset=0
    current_onset=0
    speed=0.4
    speed_x=0
    tiles=[]
    Nb_tiles=16
    current_loop=0
    tile_coordinates=[]
    ship=None
    ship_base_y=0.04
    ship_height=0.035
    ship_width=0.1
    game_over=False
    game_start=False
    game_voice=None
    ship_coordinates=[(0,0),(0,0),(0,0)]
    #menu_title=StringProperty("G A L A X Y")
    #button_title=StringProperty("start")
    def __init__(self,**kwargs):
        super(Mainwidget,self).__init__(**kwargs)
        #print("size"+str(self.width) +str(self.height))
        self.init_sound()
        self.init_vertical_line()
        self.init_horizontal_line()
        self.init_tiles()
        self.init_ship()
        self.gen_tiles()
        self.get_tile_coordinates()
        Clock.schedule_interval(self.update,1/60)
    def init_sound(self):
        self.game_voice=SoundLoader.load("Space_music.mp3")
        self.game_voice.volume=1
    def reset_game(self):
       # self.game_voice.play()
        self.current_loop=0
        self.current_offset=0
        self.current_onset=0
        self.score="score:"+str(self.current_loop)
        self.tile_coordinates=[]
        self.gen_tiles()
        self.get_tile_coordinates()
        self.game_over=False
        self.game_start=False 
        self.speed=0.4
    def init_vertical_line(self):
        with self.canvas:
            Color(1,1,1)
            for I in range(0,self.Nb_lines_y):
                self.line_list_y.append(Line())
    def init_ship(self):
        with self.canvas:
            Color(0,0,0)
            self.ship=Triangle()
    def init_tiles(self):
        with self.canvas:
            Color(1,1,1,.6)
            for I in range(self.Nb_tiles):
                self.tiles.append(Quad())
    def gen_tiles(self):
        for I in range(0,10):
            self.tile_coordinates.append((0,I))
    def get_tile_coordinates(self):
        last_y=0
        last_x=0
        start=-int(self.Nb_lines_y/2)+1
        end=start+self.Nb_lines_y-1
        for I in range(len(self.tile_coordinates)-1,-1,-1):
            #self.tile_coordinates.append((0,I))
            if self.tile_coordinates[I][1]<self.current_loop:
                del self.tile_coordinates[I]
        if len(self.tile_coordinates)>0:
            last_coordinates=self.tile_coordinates[-1]
            last_y=last_coordinates[1]+1
            last_x=last_coordinates[0]
        for I in range(len(self.tile_coordinates),self.Nb_tiles):
            self.tile_coordinates.append((last_x,last_y))
            r=random.randint(0,2)
            if last_x>=end-1:
                r=2
            elif last_x<=start:
                r=1
            if r==1:
                last_x+=1
                self.tile_coordinates.append((last_x,last_y))
                last_y+=1
                self.tile_coordinates.append((last_x,last_y))
            if r==2:
                last_x-=1
                self.tile_coordinates.append((last_x,last_y))
                last_y+=1
                self.tile_coordinates.append((last_x,last_y))
            last_y+=1
    def init_horizontal_line(self):
         with self.canvas:
             Color(1,1,1)
             for I in range(0,self.Nb_lines_x):
                 self.line_list_x.append(Line())
    def on_touch_down(self,touch):
        if self.menu_widget.opacity==0:
            if touch.x<=self.width/2:
                self.speed_x=2
            else:
                self.speed_x=-2
        return super(Mainwidget,self).on_touch_down(touch)
    def on_touch_up(self,touch):
        if touch.x<self.width/2:
            self.speed_x=0
        else:
            self.speed_x=0
    def game_start_function(self):
        self.game_voice.play()
        #mixer.music.play()
        self.reset_game()
        self.game_start=True
        #self.game_voice.play()
        self.menu_widget.opacity=0
class background(RelativeLayout):
    pass
class GalaxyApp(App):
    pass
    
GalaxyApp().run()