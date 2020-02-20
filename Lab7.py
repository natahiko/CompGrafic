import cv2
import numpy as np
import random
from math import cos, sin
from utils import Elipse, draw_img_points, draw_img


def get_color(face, model, ambient=0.2):
    color = [(face[0] % 255 + 70) * ambient,
             (face[1] % 255 + 70) * ambient,
             (face[2] % 255 + 70) * ambient]
    point1 = model.vert(face[0])
    point2 = model.vert(face[1])
    point3 = model.vert(face[2])
    res_color = color
    return res_color

def draw_img(model, window_name, wait_key=16, width=600, height=600):
    img = np.zeros((height, width, 3), dtype=np.uint8)
    for i in range(model.nfaces()):
        face = model.face(i)
        triang = [0, 0, 0]
        for j in range(3):
            vert = model.vert(face[j])
            triang[j] = width - int((vert[0] + 1) * width / 2), int(abs(height - (vert[1] + 1) * height / 2))
        cv2.drawContours(img, [np.array([triang[0], triang[1], triang[2]])], 0, get_color(face, model), -1)
    cv2.imshow(window_name, img)
    cv2.waitKey(wait_key)

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
