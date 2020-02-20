import numpy as np
import cv2
import random


def get_rand_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


def get_face_color(face, model):
    return (face[0] % 255 + 70, face[1] % 255 + 70, face[2] % 255 + 70)


def draw_img(model, window_name, wait_key=16, width=600, height=600):
    img = np.zeros((height, width, 3), dtype=np.uint8)
    for i in range(model.nfaces()):
        face = model.face(i)
        triang = [0, 0, 0]
        for j in range(3):
            vert = model.vert(face[j])
            triang[j] = width - int((vert[0] + 1) * width / 2), int(abs(height - (vert[1] + 1) * height / 2))
        cv2.drawContours(img, [np.array([triang[0], triang[1], triang[2]])], 0, get_face_color(face,model), -1)
    cv2.imshow(window_name, img)
    cv2.waitKey(wait_key)


def draw_img_points(model, width=400, height=400):
    img = np.zeros((400, 400, 3), dtype=np.uint8)
    for vect in model.vectors():
        x = int((vect[0] + 1) * width / 2) - 1
        y = int((vect[1] + 1) * height / 2) - 1
        img[x, y] = (230, 55, 140)
    cv2.imshow("img", img)
    cv2.waitKey(1)
