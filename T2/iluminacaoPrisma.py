from GLAPP import GLAPP
from OpenGL import GL
from array import array
import ctypes
import glm
import math
from math import *



a = 0

vertices = (
  (-1,1,0),
  (1,1,0),
  (-1,-1,-1),
  (-1,-1,1),
  (1,-1,-1),
  (1,-1,1)
)

linhas = (
    (0,1),
    (0,2),
    (0,3),
    (2,3),
    (2,4),
    (3,5),
    (4,1),
    (4,5),
    (1,5),
)

faces = (
    (0,2,3),
    (1,4,5),
    (2,3,5,4),
    (0,1,4,2),
    (0,1,5,3)
)

v = array('f',[])
t = array('f',[])
n = array('f',[])


for i in vertices:
    v.append(i[0])
    v.append(i[1])
    v.append(i[2])


for i in faces:
    for j in i:
        t.append(j)


for i in linhas:
    for j in i:
        n.append(j)


class SolidoFuncionalTextureApp(GLAPP):

    def setup(self):
        # Window setup
        self.title("Prisma iluminado")
        self.size(500,500)

        # OpenGL Initialization
        GL.glClearColor(0.2, 0.2, 0.2, 0.0)
        GL.glEnable(GL.GL_DEPTH_TEST)
        GL.glEnable(GL.GL_MULTISAMPLE)

        # Pipeline (shaders)
        self.pipeline = self.loadPipeline("Lambert")
        GL.glUseProgram(self.pipeline)

        
        self.squareArrayBufferId = None

    def drawSquare(self):
        if self.squareArrayBufferId == None:
            position = v
            textureCoord = t
            normal = n
            self.squareArrayBufferId = GL.glGenVertexArrays(1)
            GL.glBindVertexArray(self.squareArrayBufferId)
            GL.glEnableVertexAttribArray(0)
            GL.glEnableVertexAttribArray(1)
            GL.glEnableVertexAttribArray(2)
            
            idVertexBuffer = GL.glGenBuffers(1)
            GL.glBindBuffer(GL.GL_ARRAY_BUFFER, idVertexBuffer)
            GL.glBufferData(GL.GL_ARRAY_BUFFER, len(position)*position.itemsize, ctypes.c_void_p(position.buffer_info()[0]), GL.GL_STATIC_DRAW)
            GL.glVertexAttribPointer(0,3,GL.GL_FLOAT,GL.GL_FALSE,0,ctypes.c_void_p(0))

            idTextureBuffer = GL.glGenBuffers(1)
            GL.glBindBuffer(GL.GL_ARRAY_BUFFER, idTextureBuffer)
            GL.glBufferData(GL.GL_ARRAY_BUFFER, len(textureCoord)*textureCoord.itemsize, ctypes.c_void_p(textureCoord.buffer_info()[0]), GL.GL_STATIC_DRAW)
            GL.glVertexAttribPointer(1,2,GL.GL_FLOAT,GL.GL_FALSE,0,ctypes.c_void_p(0))
        
            idNormalBuffer = GL.glGenBuffers(1)
            GL.glBindBuffer(GL.GL_ARRAY_BUFFER, idNormalBuffer)
            GL.glBufferData(GL.GL_ARRAY_BUFFER, len(normal)*normal.itemsize, ctypes.c_void_p(normal.buffer_info()[0]), GL.GL_STATIC_DRAW)
            GL.glVertexAttribPointer(2,3,GL.GL_FLOAT,GL.GL_FALSE,0,ctypes.c_void_p(0))

            GL.glBindAttribLocation(self.pipeline,0,"position")
            GL.glBindAttribLocation(self.pipeline,1,"textureCoord")
            GL.glBindAttribLocation(self.pipeline,2,"normal")

        global a
        a += 0.0005
        projection = glm.perspective(math.pi/4,self.width/self.height,0.1,100)
        camera = glm.lookAt(glm.vec3(0,0,6),glm.vec3(0,0,0),glm.vec3(0,1,0))
        model = glm.rotate(a,glm.vec3(0,1,0))
        mvp = projection * camera * model
        GL.glUniformMatrix4fv(GL.glGetUniformLocation(self.pipeline, "MVP"),1,GL.GL_FALSE,glm.value_ptr(mvp))
        GL.glBindVertexArray(self.squareArrayBufferId)
        GL.glDrawArrays(GL.GL_TRIANGLES,0,len(v)//3)

    def draw(self):
        # clear screen and depth buffer
        GL.glClear(GL.GL_COLOR_BUFFER_BIT|GL.GL_DEPTH_BUFFER_BIT)

        # Draw a Triangle
        self.drawSquare()

SolidoFuncionalTextureApp()
