import pygame as pg
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
from utils import getElipseCord, Elipse

# initialise vectors coordinates and faces as we did it in previous labs wher we worked with head 3d object
vectors, faces = getElipseCord(a=0.5, b=0.7, c=1)

# method for draw elipse with OPENGL triangles
def solidElipse(elipse):
    faces = elipse.faces()
    vectors = elipse.vectors()
    glBegin(GL_TRIANGLES)
    for face in faces:
        glColor3fv([(face[0] % 100) / 100, (face[1] % 100) / 100, (face[2] % 100) / 100])
        for vert in face:
            glVertex3fv(vectors[vert])
    glEnd()


def main(width=800, height=600, perspective=45, x_cord=0, y_cord=0, z_cord=-5, ambient=0.4):
    # # initailise all openGL features
    pg.init()
    display = (width, height)
    pg.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(perspective, (display[0] / display[1]), 0.1, 10.0)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glEnable(GL_COLOR_MATERIAL)
    glEnable(GL_LIGHT0)
    glTranslatef(x_cord, y_cord, z_cord)
    # lightning components
    glLightfv(GL_LIGHT0, GL_AMBIENT, [ambient, ambient, ambient, 20])
    glLightfv(GL_LIGHT0, GL_DIFFUSE, [2, 2, 2, 1])
    glLightfv(GL_LIGHT0, GL_POSITION, [2, 2, 2, 1])

    # create elipses
    elipse1 = Elipse(a=0.5, b=0.7, c=1)
    elipse2 = Elipse(a=1, b=0.3, c=0.3)
    elipse3 = Elipse(a=0.2, b=1, c=0.8)
    # create starting position for different epilsis
    rotation1 = 0
    rotation2 = 0
    rotation3 = 0

    # loop for drawing and rotation object
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()

        # clear all
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # block for building object 1
        glPushMatrix()
        #rotate
        glTranslatef(2, 2, -1)
        glRotatef(rotation1, 1, 0, -1)
        rotation1 += (0 + 1) * 1.5
        # draw
        solidElipse(elipse1)
        #end block
        glPopMatrix()

        # block for building object 2
        glPushMatrix()
        #rotate
        glTranslatef(-0.5, -0.5, 3)
        glRotatef(rotation2, 0, -1, -1)
        rotation2 += (1 + 1) * 1.5
        # draw
        solidElipse(elipse2)
        #end block
        glPopMatrix()

        # block for building object 3
        glPushMatrix()
        #rotate
        glTranslatef(0, 0, 0)
        glRotatef(rotation3, 1, 1, 0)
        rotation3 += (2 + 1) * 1.5
        # draw
        solidElipse(elipse3)
        #end block
        glPopMatrix()

        pg.display.flip()
        pg.time.wait(10)

# run the main app
if __name__ == "__main__":
    main()
