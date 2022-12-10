from GLAPP import GLAPP
from OpenGL import GL
from array import array
import ctypes
import glm
import math

#função para processar e numero de vertices
def solidoFuncional(fv,N):
    #vertices
    v = array('f',[])
    t = array('f',[])

    def adiciona(lista,vertice):
        for v in vertice:
            lista.append(v)

    for i in range(N):
        for j in range(N):
            vA = fv(i,j)
            vB = fv(i,j+1)
            vC = fv(i+1,j+1)
            vD = fv(i+1,j)
            adiciona(v,vA)
            adiciona(v,vB)
            adiciona(v,vD)
            adiciona(v,vB)
            adiciona(v,vC)
            adiciona(v,vD)
            
    return v

N=50
a=2

def paraboloide(i,j):
    x = (2*i/N)-1
    y = (2*j/N)-1
    return x, y, x**2+y**2

v = solidoFuncional(paraboloide,N)

class SolidoFuncionalTextureApp(GLAPP):
    def setup(self):
        # Window setup
        self.title("Paraboloide Definido por uma Função")
        self.size(800,800)
        # OpenGL Initialization
        GL.glClearColor(0.2, 0.2, 0.2, 0.0)
        GL.glEnable(GL.GL_DEPTH_TEST)
        GL.glEnable(GL.GL_MULTISAMPLE)
        # Pipeline (shaders)
        self.pipeline = self.loadPipeline("SimpleTexture")
        GL.glUseProgram(self.pipeline)
        self.squareArrayBufferId = None

    def drawSquare(self):
        if self.squareArrayBufferId == None:
            position = v
            self.squareArrayBufferId = GL.glGenVertexArrays(1)
            GL.glBindVertexArray(self.squareArrayBufferId)
            GL.glEnableVertexAttribArray(0)
            GL.glEnableVertexAttribArray(1)
            idVertexBuffer = GL.glGenBuffers(1)
            GL.glBindBuffer(GL.GL_ARRAY_BUFFER, idVertexBuffer)
            GL.glBufferData(GL.GL_ARRAY_BUFFER, len(position)*position.itemsize, ctypes.c_void_p(position.buffer_info()[0]), GL.GL_STATIC_DRAW)
            GL.glVertexAttribPointer(0,3,GL.GL_FLOAT,GL.GL_FALSE,0,ctypes.c_void_p(0))

        global a
        a += math.pi/5000
        projection = glm.perspective(math.pi/4,self.width/self.height,0.1,100)
        camera = glm.lookAt(glm.vec3(4,0,4),glm.vec3(0,0,0),glm.vec3(0,1,0))
        #model = glm.mat4(1.0) 
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