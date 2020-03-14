import pygame as pg
from pygame.locals import *
import numpy as np
from math import cos, sin, pi, radians
from OpenGL.GL import *
from OpenGL.GLU import *
from utils import getElipseCord

vectors, faces = getElipseCord(a=0.5, b=0.7, c=1)

def rotate(vertex, theta_x=0., theta_y=0., theta_z=0.):
    arr: np.ndarray = np.array(
        # X
        [[1, 0, 0],
         [0, cos(-theta_x), -sin(-theta_x)],
         [0, sin(-theta_x), cos(-theta_x)]],
    ).dot(
        # Y
        np.array([
            [cos(-theta_y), 0, sin(-theta_y)],
            [0, 1, 0],
            [-sin(-theta_y), 0, cos(-theta_y)]
        ])
    ).dot(
        # Z
        np.array([
            [cos(-theta_z), -sin(-theta_z), 0],
            [sin(-theta_z), cos(-theta_z), 0],
            [0, 0, 1]
        ])
    ).dot(
        np.transpose(np.array(vertex))
    )
    return arr.tolist()

def solidCube():
    res_shadow = []
    glBegin(GL_TRIANGLES)
    for face in faces:
        glColor3fv([(face[0] %100) / 100, (face[1]%100) / 100,(face[2]%100) / 100])
        arr = []
        for vert in face:
            glVertex3fv(vectors[vert])
            arr.append(vectors[vert])
        res_shadow.append(arr)
    glEnd()
    return res_shadow



def main(width=800, height=600, perspective=45, x_cord=0, y_cord=0, z_cord=-5, ambient=0.4):
    pg.init()
    display = (width, height)
    pg.display.set_mode(display, DOUBLEBUF|OPENGL)
    gluPerspective(perspective, (display[0]/display[1]), 0.1, 10.0)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glEnable(GL_COLOR_MATERIAL)
    glEnable(GL_LIGHT0)
    glTranslatef(0, 0, -1)
    glTranslatef(x_cord, y_cord, z_cord)
    glLightfv(GL_LIGHT0, GL_AMBIENT, [ambient, ambient, ambient, 20])

    glLightfv(GL_LIGHT0, GL_DIFFUSE, [2, 2, 2, 1])
    glLightfv(GL_LIGHT0, GL_POSITION, [5, -4, 0, 0])
    rotate1 = 0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()

        # clear all
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glPushMatrix()
        glRotatef(rotate1, 1, 1, 0)
        rotate1 += (0 + 1) * 1.5
        shadow = solidCube()
        shadow_casters = []
        for face in shadow:
                rotation = radians(rotate1)
                shadow_casters.append([rotate(v, theta_x=-rotation, theta_y=-rotation, theta_z=0) for v in face])
        glPopMatrix()

        #build shadow
        glColor3fv((100, 100, 100))
        glBegin(GL_TRIANGLES)
        for shadow_caster in shadow_casters:
            for (x, y, z) in shadow_caster:
                glVertex3fv((x, -2, z))
        glEnd()

        pg.display.flip()
        pg.time.wait(10)

if __name__ == "__main__":
    main()
