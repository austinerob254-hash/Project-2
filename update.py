import menu
def get_line_x(self,index):
    central_line_point=self.perspectivepoint_x 
    offset=index-0.5
    self.line_point_y=central_line_point+offset*self.spacing*self.width+self.current_onset
    return self.line_point_y 
def get_line_y(self,index):
    self.line_point_x=index*self.spacing_x*self.height-self.current_offset
    return self.line_point_x
def update_y(self):
       start=-int(self.Nb_lines_y/2)+1
       end=start+self.Nb_lines_y
       for I in range(start,end):
           a=self.get_line_x(I)
           x_1,y_1=self.transform(a,0)
           x_2,y_2=self.transform(a,self.height)
           self.line_list_y[I].points=[x_1,y_1,x_2,y_2]
def get_actual_coordinates(self,ti_x,ti_y):
    ti_x=self.get_line_x(ti_x)
    ti_y=ti_y-self.current_loop
    ti_y=self.get_line_y(ti_y)
    return ti_x,ti_y
def update_ship(self):
    ship_center=self.width/2
    self.ship_coordinates[0]=(ship_center-self.ship_width/2*self.width,self.ship_base_y*self.height)
    self.ship_coordinates[1]=(ship_center+self.ship_width/2*self.width,self.ship_base_y*self.height)
    self.ship_coordinates[2]=(self.width/2,self.ship_base_y*self.height+self.ship_height*self.height)
    x_1,y_1=self.transform(*self.ship_coordinates[0])
    x_2,y_2=self.transform(*self.ship_coordinates[1])
    x_3,y_3=self.transform(*self.ship_coordinates[2])
    self.ship.points=[x_1,y_1,x_2,y_2,x_3,y_3]
def ship_collision_with_tile(self,ti_x,ti_y):
    x_min,y_min=self.get_actual_coordinates(ti_x,ti_y)
    x_max,y_max=self.get_actual_coordinates(ti_x+1,ti_y+1)
    for I in range(0,3):
        px,py=self.ship_coordinates[I]
        if x_min<=px<=x_max and y_min<=py<=y_max:
            return True
    return False
def ship_collision(self):
    for I in range(0,len(self.tile_coordinates)):
        px,py=self.tile_coordinates[I]
        if py>self.current_loop+1:
            return False
        if self.ship_collision_with_tile(px,py):
            return True
    return False
def get_tile(self):
    for I in range(0,self.Nb_tiles):
        tile=self.tile_coordinates[I]
        xmin,ymin=self.get_actual_coordinates(tile[0],tile[1])
        xmax,ymax=self.get_actual_coordinates(tile[0]+1,tile[1]+1)
        x1,y1=self.transform(xmin,ymin)
        x2,y2=self.transform(xmin,ymax)
        x3,y3=self.transform(xmax,ymax)
        x4,y4=self.transform(xmax,ymin)
        self.tiles[I].points=[x1,y1,x2,y2,x3,y3,x4,y4]
def update_x(self):
    start=-int(self.Nb_lines_y/2)+1
    end=start+self.Nb_lines_y
    max=self.get_line_x(end-1)
    min=self.get_line_x(start)
    for I in range(0,self.Nb_lines_x):
        b=self.get_line_y(I)
        x_1,y_1=self.transform(min,b)
        x_2,y_2=self.transform(max,b)
        self.line_list_x[I].points=[x_1,y_1,x_2,y_2]
def update(self,dt):
    time_factor=dt*60
    self.update_ship()
    self.update_y()
    self.update_x()
    self.get_tile()
    if self.game_over==False and self.game_start:
        true_speed=self.speed*self.height/100
        self.current_offset+=true_speed*time_factor 
        while self.current_offset>=self.spacing_x*self.height:
            self.current_offset-=(self.spacing_x*self.height)
            self.current_loop+=1
            self.score="score:"+str(self.current_loop)
            self.get_tile_coordinates()
        true_speed_x=self.speed_x*self.width/100
        self.current_onset+=true_speed_x *time_factor 
    if self.current_loop%100==0 and self.current_loop>0:
        self.speed+=0.01
    if not self.ship_collision() and not self.game_over:
       menu.Menu.menu_title="GAME_OVER"
       self.menu_widget.button_title="Restart"
       self.game_over=True
       self.menu_widget.opacity=1
       