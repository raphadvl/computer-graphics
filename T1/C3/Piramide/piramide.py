import sdl2
import sys
from OpenGL.GL import *
from OpenGL.GLU import *


vertices = (
    (0,1,0),
    ( 1,-1,-1),
    (-1,-1,-1),
    ( 1,-1, 1),
    (-1,-1, 1),
)

linhas = (
    (0,1),
    (0,2),
    (0,3),
    (0,4),
    (1,2),
    (3,4),
    (1,3),
    (2,4)
)

faces = (
    (1,2,4,3),
    (0,1,2),
    (0,3,4),
    (0,1,3),
    (0,2,4),
)

cores = ( (1,0.5,0.4),(1,1,0),(0,1,0),(0,1,1),(0,0,1),(1,0,1),(0.7,1,1),(1,0,0.8) )

a = 0

def piramide():
    glPushMatrix()
    glRotatef(a,1,0,0)
    glBegin(GL_QUADS)
    glColor3fv(cores[0])
    for vertex in faces[0]:
       glVertex3fv(vertices[vertex]) 

    glEnd()
    glBegin(GL_TRIANGLES)
    for i in range(1,5):
        glColor3fv(cores[i])
        for vertex in faces[i]:
           glColor3fv(cores[vertex])
           glVertex3fv(vertices[vertex])

    glEnd()
    glColor3f(0,0.5,0)
    glBegin(GL_LINES)
    for linha in linhas:
        for vertice in linha:
            glVertex3fv(vertices[vertice])

    glEnd()
    glPopMatrix()
    
def desenha():
    global a
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glPushMatrix()
    piramide()
    glPopMatrix()
    a += 0.1

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

sdl2.SDL_Init(sdl2.SDL_INIT_EVERYTHING)
sdl2.SDL_GL_SetAttribute(sdl2.SDL_GL_CONTEXT_MAJOR_VERSION, 2)
sdl2.SDL_GL_SetAttribute(sdl2.SDL_GL_CONTEXT_MINOR_VERSION, 1)
sdl2.SDL_GL_SetAttribute(sdl2.SDL_GL_CONTEXT_PROFILE_MASK,sdl2.SDL_GL_CONTEXT_PROFILE_CORE)
sdl2.SDL_GL_SetAttribute(sdl2.SDL_GL_DOUBLEBUFFER, 1)
sdl2.SDL_GL_SetAttribute(sdl2.SDL_GL_DEPTH_SIZE, 24)
sdl2.SDL_GL_SetSwapInterval(1)
window = sdl2.SDL_CreateWindow(b"Piramide", sdl2.SDL_WINDOWPOS_CENTERED, sdl2.SDL_WINDOWPOS_CENTERED, WINDOW_WIDTH, WINDOW_HEIGHT, sdl2.SDL_WINDOW_OPENGL | sdl2.SDL_WINDOW_SHOWN)
if not window:
    sys.stderr.write("Error: Could not create window\n")
    exit(1)
glcontext = sdl2.SDL_GL_CreateContext(window)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
print(glGetString(GL_VERSION))
gluPerspective(45,800.0/600.0,0.1,100.0)
glTranslatef(0.0,0.0,-20)

running = True
event = sdl2.SDL_Event()
while running:
    while sdl2.SDL_PollEvent(ctypes.byref(event)) != 0:
        if event.type == sdl2.SDL_QUIT:
            running = False
        if event.type == sdl2.events.SDL_KEYDOWN:
            print("SDL_KEYDOWN")
            if event.key.keysym.sym == sdl2.SDLK_ESCAPE:
                running = False
        if (event.type == sdl2.SDL_MOUSEMOTION):
            print("SDL_MOUSEMOTION")
        if (event.type == sdl2.SDL_MOUSEBUTTONDOWN):
            print("SDL_MOUSEBUTTONDOWN")
    desenha()
    sdl2.SDL_GL_SwapWindow(window)