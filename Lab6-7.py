import cv2
import numpy as np
import random
from math import cos, sin
from utils import Elipse, draw_img, draw_img_points, Model3D


def main():
# for lab with elipse
# model = Elipse()
# for lab 7 use model 3d
    model = Model3D(r'D:/african_head.obj')
    while True:
        draw_img(model, "model", wait_key=1)
        # draw_img_points(model)
        model.rotate_X(0.0)
        model.rotate_Y(0.1)
        model.rotate_Z(0)
        model.sort()


main()
cv2.waitKey(0)
