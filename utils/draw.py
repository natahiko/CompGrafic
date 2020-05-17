import numpy as np
import cv2
import random

light_vector = np.array([-1, -1, -1])
see_vect = [1, 0, 0]


def get_rand_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def get_opengl_color(face, vectors, ambient_coef=0.1, diffuse_coef=0.6, reff_coef=0.3, brightness=13):
    x1, y1, z1 = vectors[face[0]]
    x2, y2, z2 = vectors[face[1]]
    x3, y3, z3 = vectors[face[2]]
    original_color = np.array([face[0] % 255 + 70, face[1] % 255 + 70, face[2] % 255 + 70])
    res_color = np.zeros(3)
    normal_vect = np.array([
        (y2 - y1) * (z3 - z1) - (z2 - z1) * (y3 - y1),
        (z2 - z1) * (x3 - x1) - (x2 - x1) * (z3 - z1),
        (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)
    ])
    normal_vect = normal_vect / np.linalg.norm(normal_vect)

    # Ambient
    res_color += original_color * ambient_coef

    # Diffuse
    diff_comp = max(np.dot(normal_vect, light_vector), 0.0)
    res_color += diff_comp*diffuse_coef*original_color

    # Specular
    reff_light_vect = normal_vect*(2*np.dot(normal_vect, see_vect)/np.dot(normal_vect,normal_vect)) - see_vect
    reff_comp = max(np.dot(see_vect, reff_light_vect), 0.0)
    reff_comp = pow(reff_comp, brightness)
    res_color += reff_comp*reff_coef*original_color

    return [min(c, 255) for c in res_color]

def get_def_color(face):
    return ([face[0] % 255 + 70, face[1] % 255 + 70, face[2] % 255 + 70])

def get_face_color(face, model, ambient_coef=0.1, diffuse_coef=0.6, reff_coef=0.3, brightness=13):
    x1, y1, z1 = model.vert(face[0])
    x2, y2, z2 = model.vert(face[1])
    x3, y3, z3 = model.vert(face[2])
    original_color = np.array([face[0] % 255 + 70, face[1] % 255 + 70, face[2] % 255 + 70])
    res_color = np.zeros(3)
    normal_vect = np.array([
        (y2 - y1) * (z3 - z1) - (z2 - z1) * (y3 - y1),
        (z2 - z1) * (x3 - x1) - (x2 - x1) * (z3 - z1),
        (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)
    ])
    normal_vect = normal_vect / np.linalg.norm(normal_vect)

    # Ambient
    res_color += original_color * ambient_coef

    # Diffuse
    diff_comp = max(np.dot(normal_vect, light_vector), 0.0)
    res_color += diff_comp*diffuse_coef*original_color

    # Specular
    reff_light_vect = normal_vect*(2*np.dot(normal_vect, see_vect)/np.dot(normal_vect,normal_vect)) - see_vect
    reff_comp = max(np.dot(see_vect, reff_light_vect), 0.0)
    reff_comp = pow(reff_comp, brightness)
    res_color += reff_comp*reff_coef*original_color

    return [min(c, 255) for c in res_color]


def draw_img(model, window_name, wait_key=16, width=600, height=600):
    img = np.zeros((height, width, 3), dtype=np.uint8)
    for i in range(model.nfaces()):
        face = model.face(i)
        triang = [0, 0, 0]
        for j in range(3):
            vert = model.vert(face[j])
            triang[j] = width - int((vert[0] + 1) * width / 2), int(abs(height - (vert[1] + 1) * height / 2))
        cv2.drawContours(img, [np.array([triang[0], triang[1], triang[2]])], 0, get_face_color(face, model), -1)
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
