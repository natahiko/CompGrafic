import pygame as pg
from pygame.locals import *
import numpy as np
from math import cos, sin, pi, radians
from OpenGL.GL import *
from OpenGL.GLU import *
from utils import getElipseCord

# create global variable for use them in different methods
vectors = []
faces = []


# methods for rotate objects
# change all vectors coordinates with new one
def rotate(vertex, theta_x=0., theta_y=0., theta_z=0.):
    arr: np.ndarray = np.array(
        # X - coordinate
        [[1, 0, 0],
         [0, cos(-theta_x), -sin(-theta_x)],
         [0, sin(-theta_x), cos(-theta_x)]],
    ).dot(
        # Y - coordinate
        np.array([
            [cos(-theta_y), 0, sin(-theta_y)],
            [0, 1, 0],
            [-sin(-theta_y), 0, cos(-theta_y)]
        ])
    ).dot(
        # Z - coordinate
        np.array([
            [cos(-theta_z), -sin(-theta_z), 0],
            [sin(-theta_z), cos(-theta_z), 0],
            [0, 0, 1]
        ])
    ).dot(
        np.transpose(np.array(vertex))
    )
    return arr.tolist()

# for drawind elipce use gl triangles
def solidElipse():
    global vectors, faces
    # array with shadows coordinates to use it later for ahsdow
    res_shadow = []
    glBegin(GL_TRIANGLES)
    for face in faces:
        glColor3fv([(face[0] % 100) / 100, (face[1] % 100) / 100, (face[2] % 100) / 100])
        arr = []
        for vert in face:
            glVertex3fv(vectors[vert])
            arr.append(vectors[vert])
        # append shadow with specific points
        res_shadow.append(arr)
    glEnd()
    return res_shadow

# main blick
def main(width=800, height=600, perspective=45, x_cord=0, y_cord=0, z_cord=-5, ambient=0.4):
    # initialise vectors coordinates and faces as we did it in previous labs wher we worked with head 3d object
    getElipseCord(a=0.5, b=0.7, c=1)

    # initailise all openGL features
    pg.init()
    display = (width, height)
    pg.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(perspective, (display[0] / display[1]), 0.1, 10.0)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glEnable(GL_COLOR_MATERIAL)
    glEnable(GL_LIGHT0)
    glTranslatef(1, 1, 0)
    glTranslatef(x_cord, y_cord, z_cord)

    glLightfv(GL_LIGHT0, GL_AMBIENT, [ambient, ambient, ambient, 20])
    glLightfv(GL_LIGHT0, GL_DIFFUSE, [2, 2, 2, 1])
    glLightfv(GL_LIGHT0, GL_POSITION, [5, -4, 0, 0])

    # starting rotation position
    rotate1 = 0
    # loop for drawing and rotation object
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()

        # clear all
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # block for rotate and draw elipse
        glPushMatrix()
        glRotatef(rotate1, 1, 1, 0)
        rotate1 += (0 + 1) * 1.5
        shadow = solidElipse()
        shadow_casters = []
        for face in shadow:
            rotation = radians(rotate1)
            shadow_casters.append([rotate(v, theta_x=-rotation, theta_y=-rotation, theta_z=0) for v in face])
        glPopMatrix()

        # block for build shadow
        glColor3fv((100, 100, 100))
        glBegin(GL_TRIANGLES)
        for shadow_caster in shadow_casters:
            for (x, y, z) in shadow_caster:
                glVertex3fv((x, -2, z))
        glEnd()

        # pause
        pg.display.flip()
        pg.time.wait(10)

# run the main app
if __name__ == "__main__":
    main()
