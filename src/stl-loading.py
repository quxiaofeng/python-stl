import os
import sys
import struct

from OpenGL.GL import *
from OpenGL.GLU import *
import pygame
from pygame.locals import *

#class for a 3d point
class createpoint:
  def __init__(self,p,c=(1,0,0)):
    self.point_size=0.5
    self.color=c
    self.x=p[0]
    self.y=p[1]
    self.z=p[2]

  def glvertex(self):
    glVertex3f(self.x,self.y,self.z)

#class for a 3d face on a model
class createtriangle:
  points=None
  normal=None

  def __init__(self,p1,p2,p3,n=None):
    #3 points of the triangle
    self.points=createpoint(p1),createpoint(p2),createpoint(p3)

    #triangles normal
    self.normal=createpoint(self.calculate_normal(self.points[0],self.points[1],self.points[2]))#(0,1,0)#

  #calculate vector / edge
  def calculate_vector(self,p1,p2):
    return -p1.x+p2.x,-p1.y+p2.y,-p1.z+p2.z

  def calculate_normal(self,p1,p2,p3):
    a=self.calculate_vector(p3,p2)
    b=self.calculate_vector(p3,p1)
    #calculate the cross product returns a vector
    return self.cross_product(a,b)    

  def cross_product(self,p1,p2):
    return (p1[1]*p2[2]-p2[1]*p1[2]) , (p1[2]*p2[0])-(p2[2]*p1[0]) , (p1[0]*p2[1])-(p2[0]*p1[1])

class loader:
  model=[]

  #return the faces of the triangles
  def get_triangles(self):
    if self.model:
      for face in self.model:
        yield face

  #draw the models faces
  def draw(self):
    glBegin(GL_TRIANGLES)
    for tri in self.get_triangles():
      glNormal3f(tri.normal.x,tri.normal.y,tri.normal.z)
      glVertex3f(tri.points[0].x,tri.points[0].y,tri.points[0].z)
      glVertex3f(tri.points[1].x,tri.points[1].y,tri.points[1].z)
      glVertex3f(tri.points[2].x,tri.points[2].y,tri.points[2].z)
    glEnd()

  #load stl file detects if the file is a text file or binary file
  def load_stl(self,filename):
    #read start of file to determine if its a binay stl file or a ascii stl file
    fp=open(filename,'rb')
    h=fp.read(80)
    type=h[0:5]
    fp.close()

    if type.decode('ascii')=='solid':
      print "reading text file "+str(filename)
      self.load_text_stl(filename)
    else:
      print "reading binary stl file "+str(filename,)
      self.load_binary_stl(filename)

  #read text stl match keywords to grab the points to build the model
  def load_text_stl(self,filename):
    fp=open(filename,'r')

    for line in fp.readlines():
      words=line.split()
      if len(words)>0:
        if words[0]=='solid':
          self.name=words[1]

        if words[0]=='facet':
          center=[0.0,0.0,0.0]
          triangle=[]
          normal=(eval(words[2]),eval(words[3]),eval(words[4]))

        if words[0]=='vertex':
          triangle.append((eval(words[1]),eval(words[2]),eval(words[3])))


        if words[0]=='endloop':
          #make sure we got the correct number of values before storing
          if len(triangle)==3:
            self.model.append(createtriangle(triangle[0],triangle[1],triangle[2],normal))
    fp.close()

  #load binary stl file check wikipedia for the binary layout of the file
  #we use the struct library to read in and convert binary data into a format we can use
  def load_binary_stl(self,filename):
    fp=open(filename,'rb')
    h=fp.read(80)

    l=struct.unpack('I',fp.read(4))[0]
    count=0
    while True:
      try:
        p=fp.read(12)
        if len(p)==12:
          n=struct.unpack('f',p[0:4])[0],struct.unpack('f',p[4:8])[0],struct.unpack('f',p[8:12])[0]

        p=fp.read(12)
        if len(p)==12:
          p1=struct.unpack('f',p[0:4])[0],struct.unpack('f',p[4:8])[0],struct.unpack('f',p[8:12])[0]

        p=fp.read(12)
        if len(p)==12:
          p2=struct.unpack('f',p[0:4])[0],struct.unpack('f',p[4:8])[0],struct.unpack('f',p[8:12])[0]

        p=fp.read(12)
        if len(p)==12:
          p3=struct.unpack('f',p[0:4])[0],struct.unpack('f',p[4:8])[0],struct.unpack('f',p[8:12])[0]

        new_tri=(n,p1,p2,p3)

        if len(new_tri)==4:
          tri=createtriangle(p1,p2,p3,n)
          self.model.append(tri)
        count+=1
        fp.read(2)

        if len(p)==0:
          break
      except EOFError:
        break
    fp.close()



class draw_scene:
  def __init__(self,style=1):
    #create a model instance and
    self.model1=loader()
    #self.model1.load_stl(os.path.abspath('')+'/text.stl')
    if len(sys.argv) < 2:
      self.model1.load_stl('Door-handle.stl')
    else:
      self.model1.load_stl(sys.argv[1])
    self.init_shading()
    self.x=-20
    self.y=-20


  #solid model with a light / shading
  def init_shading(self):
    glShadeModel(GL_SMOOTH)
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glClearDepth(1.0)
    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_SMOOTH) 
    glDepthFunc(GL_LEQUAL)
    glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST)

    glEnable(GL_COLOR_MATERIAL)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)   
    glLight(GL_LIGHT0, GL_POSITION,  (0, 1, 1, 0))      
    glMatrixMode(GL_MODELVIEW)

  def resize(self,(width, height)):
    if height==0:
      height=1
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, 1.0*width/height, 1,100.0)
    gluLookAt(self.x, self.y, 0.0, 0, 0, 0, 0, 0.0, 40.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


  def init(self):
    glShadeModel(GL_SMOOTH)
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glClearDepth(1.0)
    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_SMOOTH) 
    glDepthFunc(GL_LEQUAL)
    glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST)


    glEnable(GL_COLOR_MATERIAL)

    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)   
    glLight(GL_LIGHT0, GL_POSITION,  (0, 1, 1, 0))

    glMatrixMode(GL_MODELVIEW)

  def draw(self):    
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    gluLookAt(self.x, self.y, 0.0, 0, 0, 0, 0, 0.0, 40.0)

    #glTranslatef(0.0,-26.0, -100.0)
    self.model1.draw()

  def event_handle(self,event):
    if event.type == pygame.KEYDOWN:
        key = pygame.key.get_pressed()
        # vertical
        if key[pygame.K_w]:
            self.y += 20.0;
            print "self.y = %d" % self.y
        if key[pygame.K_s]:
            self.y -= 20.0;
            print "self.y = %d" % self.y
        # horizontal
        if key[pygame.K_d]:
            self.x += 20.0
            print "self.x = %d" % self.x
        if key[pygame.K_a]:
            self.x -= 20.0
            print "self.x = %d" % self.x

#main program loop
def main():
  #initalize pygame
  pygame.init()
  pygame.display.set_mode((640,480), OPENGL|DOUBLEBUF)

  #setup the open gl scene
  scene=draw_scene()
  scene.resize((640,480))

  frames = 0
  ticks = pygame.time.get_ticks()
  while 1:
    event = pygame.event.poll()
    if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
      break
    else:
      scene.event_handle(event)

    #draw the scene
    scene.draw()
    pygame.display.flip()
    frames = frames+1

  print "fps:  %d" % ((frames*1000)/(pygame.time.get_ticks()-ticks))


if __name__ == '__main__':
  main()
