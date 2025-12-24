def transform(self,x,y):
   return self.transform_perspective(x,y)
 #   return self.transform_2d(x,y)  
def transform_perspective(self,x,y):
    lin_y=int(y*self.perspectivepoint_y/self.height)
    if lin_y>self.height:
        lin_y=self.perspectivepoint_y
    diff_y=self.perspectivepoint_y-lin_y
    factor=diff_y/self.perspectivepoint_y
    factor=pow(factor,4)
    diff_x=int(x-self.perspectivepoint_x)
    tr_x=int(self.perspectivepoint_x+diff_x*factor)
    tr_y=int(self.perspectivepoint_y-factor*self.perspectivepoint_y)
    return int(tr_x),int(tr_y)
def transform_2d(self,x,y):
    return int(x),int(y)