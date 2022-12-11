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
    # coordenadas de textura
    def ft(i,j):
        return 1-(i/N), j/N
    def adiciona(lista,vertice):
        for v in vertice:
            lista.append(v)
    for i in range(N):
        for j in range(N):
            vA = fv(i,j)
            tA = ft(i,j)
            vB = fv(i,j+1)
            tB = ft(i,j+1)
            vC = fv(i+1,j+1)
            tC = ft(i+1,j+1)
            vD = fv(i+1,j)
            tD = ft(i+1,j)
            adiciona(v,vA)
            adiciona(t,tA)
            adiciona(v,vB)
            adiciona(t,tB)
            adiciona(v,vD)
            adiciona(t,tD)
            adiciona(v,vB)
            adiciona(t,tB)
            adiciona(v,vC)
            adiciona(t,tC)
            adiciona(v,vD)
            adiciona(t,tD)
    return v, t

N=50
a=2

def esfera(i,j):
    theta = i*2*math.pi/N
    phi = j*math.pi/N-math.pi/2
    return math.cos(theta)*math.cos(phi), math.sin(phi), math.sin(theta)*math.cos(phi)

v, t = solidoFuncional(esfera,N)

class SolidoFuncionalTextureApp(GLAPP):
    def setup(self):
        # Window setup
        self.title("Solido Funcional")
        self.size(800,800)
        # OpenGL Initialization
        GL.glClearColor(0.2, 0.2, 0.2, 0.0)
        GL.glEnable(GL.GL_DEPTH_TEST)
        GL.glEnable(GL.GL_MULTISAMPLE)
        # Pipeline (shaders)
        self.pipeline = self.loadPipeline("SimpleTexture")
        GL.glUseProgram(self.pipeline)
        # Texture
        GL.glActiveTexture(GL.GL_TEXTURE0)
        self.loadTexture("./T1/C4/mapa.png")
        GL.glUniform1i(GL.glGetUniformLocation(self.pipeline, "textureSlot"),0)
        self.squareArrayBufferId = None

    def drawSquare(self):
        if self.squareArrayBufferId == None:
            position = v
            textureCoord = t
            self.squareArrayBufferId = GL.glGenVertexArrays(1)
            GL.glBindVertexArray(self.squareArrayBufferId)
            GL.glEnableVertexAttribArray(0)
            GL.glEnableVertexAttribArray(1)
            idVertexBuffer = GL.glGenBuffers(1)
            GL.glBindBuffer(GL.GL_ARRAY_BUFFER, idVertexBuffer)
            GL.glBufferData(GL.GL_ARRAY_BUFFER, len(position)*position.itemsize, ctypes.c_void_p(position.buffer_info()[0]), GL.GL_STATIC_DRAW)
            GL.glVertexAttribPointer(0,3,GL.GL_FLOAT,GL.GL_FALSE,0,ctypes.c_void_p(0))
            idTextureBuffer = GL.glGenBuffers(1)
            GL.glBindBuffer(GL.GL_ARRAY_BUFFER, idTextureBuffer)
            GL.glBufferData(GL.GL_ARRAY_BUFFER, len(textureCoord)*textureCoord.itemsize, ctypes.c_void_p(textureCoord.buffer_info()[0]), GL.GL_STATIC_DRAW)
            GL.glVertexAttribPointer(1,2,GL.GL_FLOAT,GL.GL_FALSE,0,ctypes.c_void_p(0))
       
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