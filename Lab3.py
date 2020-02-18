import cv2
import numpy as np
import random
from utils import Model

def get_rand_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def triangle(x0, y0, x1, y1, x2, y2, img, color):
    if y0 > y2:
        x0, x2 = x2, x0
        y0, y2 = y2, y0
    if y0 > y1:
        x0, x1 = x1, x0
        y0, y1 = y1, y0
    if y1 > y2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1

    total_height = y2 - y0
    segment_height = y1 - y0 + 1
    if total_height != 0 and segment_height != 0:
        for y in range(y0, y1 + 1):
            alpha = (y - y0)/total_height
            beta = (y - y0)/segment_height

            x_a = int(x0 + (x2 - x0) * alpha)
            y_a = y0 + (y2 - y0) * alpha
            x_b = int(x0 + (x1 - x0) * beta)
            y_b = y0 + (y1 - y0) * beta

            if x_a > x_b:
                x_a, y_a, x_b, y_b = x_b, y_b, x_a, y_a

            for j in range(x_a, x_b + 1):
                    img[y, j] = color

    return img


def main():
    width = 400
    height = 400
    img = np.zeros((width, height, 3), dtype=np.uint8)
    img2 = np.zeros((width, height, 3), dtype=np.uint8)
    model = Model('D:\graphExample\iafrican_head.obj')

    for i in range(model.nfaces()):
        face = model.face(i)
        triang = [0, 0, 0]
        for j in range(3):
            vert = model.vert(face[j])
            triang[j] = 400 - int((vert[0] + 1) * width/2), int(abs(height - (vert[1] + 1) * height/2))
        color = get_rand_color()
        img = triangle(triang[0][0], triang[0][1], triang[1][0],
                            triang[1][1], triang[2][0], triang[2][1],
                            img, color)
        cv2.drawContours(img2, [np.array([triang[0], triang[1],triang[2]])], 0, color, -1)

    cv2.imshow('My triangle', img)
    cv2.imshow('Default triagle', img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


main()
