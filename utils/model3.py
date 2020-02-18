import cv2
from math import cos, sin
import numpy as np


class Model3D():
    def __init__(self, filename):
        file = open(filename, "r")
        lines = file.readlines()
        self.__vector = []
        self.__faces = []
        for line in lines:
            if line[:2] == 'v ':
                vals = line.split(" ")
                self.__vector.append([float(vals[1]), float(vals[2]), float(vals[3])])
            elif line[:2] == 'f ':
                vals = line.split(" ")
                val1 = vals[1].split('/')
                val2 = vals[2].split('/')
                val3 = vals[3].split('/')
                self.__faces.append([int(val1[0]) - 1, int(val2[0]) - 1, int(val3[0]) - 1])

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
