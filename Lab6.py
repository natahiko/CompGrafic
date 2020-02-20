import cv2
import numpy as np
import random
from math import cos, sin
from utils import Elipse, draw_img, draw_img_points


def main():
    model = Elipse()
    while True:
        draw_img(model, "model", wait_key=1)
        # draw_img_points(model)
        model.rotate_X(-0.01)
        model.rotate_Y(-0.01)
        model.rotate_Z(-0.01)
        model.sort()


main()
cv2.waitKey(0)
