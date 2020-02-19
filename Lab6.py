import cv2
import numpy as np
import random
from math import cos, sin
from utils import Elipse


def get_rand_color(face):
    return (face[0] % 255 + 70, face[1] % 255 + 70, face[2] % 255 + 70)
    # return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


def draw_img(model, window_name, wait_key=16, width=600, height=600):
    img = np.zeros((height, width, 3), dtype=np.uint8)
    for i in range(model.nfaces()):
        face = model.face(i)
        triang = [0, 0, 0]
        for j in range(3):
            vert = model.vert(face[j])
            triang[j] = width - int((vert[0] + 1) * width / 2), int(abs(height - (vert[1] + 1) * height / 2))
        cv2.drawContours(img, [np.array([triang[0], triang[1], triang[2]])], 0, get_rand_color(face), -1)
    cv2.imshow(window_name, img)
    cv2.waitKey(wait_key)


def main():
    height = 400
    width = 400
    model = Elipse()
    while True:
        draw_img(model, "model", wait_key=1)
        model.rotate_X(-0.01)
        model.rotate_Y(-0.01)
        model.rotate_Z(-0.01)
        model.sort()


    # while True:
    #
    #     model.rotate_X(-0.001)
    #     model.rotate_Y(-0.001)
    #     model.rotate_Z(-0.001)
    #     img = np.zeros((400, 400, 3), dtype=np.uint8)
    #     for vect in model.vectors():
    #         x = int((vect[0]+1) * width / 2 ) - 1
    #         y = int((vect[1]+1) * height / 2 ) - 1
    #         img[x, y] = (230,55,140)
    #     cv2.imshow("img", img)
    #     cv2.waitKey(1)


main()
cv2.waitKey(0)
