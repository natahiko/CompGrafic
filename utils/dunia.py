import cv2
from math import cos, sin
import numpy as np


class Elipse():
    def __init__(self, a=0.5, b=0.7, c=1):
        self.__vector, self.__faces = getElipseCord(a, b, c)

    def nverts(self):
        return len(self.__vector)

    def nfaces(self):
        return len(self.__faces)

    def face(self, idx):
        return self.__faces[idx]

    def faces(self):
        return self.__faces

    def vert(self, id):
        return self.__vector[int(id)]

    def vectors(self):
        return self.__vector

    def sort(self):
        self.__faces.sort(key=lambda i: self.vert(i[0])[2], reverse=False)
        pass

    def rotate_X(self, angle):
        rx = np.array([[1, 0, 0], [0, cos(angle), -sin(angle)], [0, sin(angle), cos(angle)]])
        for id, face in enumerate(self.__vector):
            y = np.array(face)
            self.__vector[id] = rx @ y

    def rotate_Y(self, angle):
        rx = np.array([[cos(angle), 0, sin(angle)], [0, 1, 0], [-sin(angle), 0, cos(angle)]])
        for id, face in enumerate(self.__vector):
            y = np.array(face)
            self.__vector[id] = rx @ y

    def rotate_Z(self, angle):
        rx = np.array([[cos(angle), -sin(angle), 0], [sin(angle), cos(angle), 0], [0, 0, 1]])
        for id, face in enumerate(self.__vector):
            y = np.array(face)
            self.__vector[id] = rx @ y


def getElipseCord(a, b, c, step=0.1):
    faces = []
    vectors = []

    total_t = 0
    t = 0.1
    while t < (3.15 * 2):
        q = 0.1
        total_q = 0
        while q < 3.15:
            vectors.append([a * sin(q) * cos(t),
                            b * sin(q) * sin(t), c * cos(q)])
            q += step
            total_q += 1
        t += step
        total_t += 1
    print(total_q)
    print(total_t)
    print(len(vectors))

    for x in range(total_q - 1):
        for y in range(total_t - 1):
            faces.append([y * x, (y + 1) * x, y * (x + 1)])
            faces.append([(y + 1) * (x + 1), (y + 1) * x, y * (x + 1)])

    return vectors, faces
