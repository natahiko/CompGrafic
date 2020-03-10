import cv2
import numpy as np
import random
from math import cos, sin
from utils import Model3D, draw_img


def main():
    model = Model3D(r'D:\graphExample\iafrican_head.obj')
    draw_img(model, "MyHead")
    while True:
        model.rotate_X(-0.1)
        model.rotate_Y(-0.1)
        model.rotate_Z(-0.1)
        model.sort()
        draw_img(model, "MyHead", wait_key=1)


main()
cv2.waitKey(0)
