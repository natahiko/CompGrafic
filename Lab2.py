import cv2
import numpy as np
from utils import Model


def line(x0, x1, y0, y1, img, color):
    steep = False
    if abs(x0 - x1) < abs(y0 - y1):
        x0, y0 = y0, x0
        x1, y1 = y1, x1
        steep = True
    if x0 > x1:
        x0, x1 = x1, x0
        y0, y1 = y1, y0
    dx = x1 - x0
    dy = y1 - y0
    derror2 = abs(dy) * 2
    error2 = 0
    y = y0
    for x in range(x0, x1 + 1):
        if steep:
            img[x,y] = color
        else:
            img[y, x] = color
        error2 += derror2
        if error2 > dx:
            if y1 > y0:
                y += 1
            else:
                y -= 1
            error2 -= (dx * 2)
    return img

def circle(x0, y0, radius, img, color):
    x = 0
    y = radius
    delta = 1 - 2 * radius
    while y >= 0:
        img[x0 + x, y0 + y] = color
        img[x0 + x, y0 - y] = color
        img[x0 - x, y0 + y] = color
        img[x0 - x, y0 - y] = color
        error = 2 * (delta + y) - 1
        if delta < 0 and error <= 0:
            x = x + 1
            delta += 2 * x + 1
            continue
        error = 2 * (delta - x) - 1
        if delta > 0 and error > 0:
            y = y - 1
            delta += 1 - 2 * y
            continue
        x = x + 1
        delta += 2 * (x - y)
        y = y - 1
    return img


def showCircles(width, height, x0, y0, radius, color):
    circleImg1 = np.zeros((width, height, 3))
    circleImg2 = np.zeros((width, height, 3))
    cv2.circle(circleImg1, (x0, y0), radius, color, 1)
    circleImg2 = circle(x0, y0, radius, circleImg2, color)
    cv2.imshow("Default circle", circleImg1)
    cv2.imshow("My circle method", circleImg2)


def showLines(width, height, model):
    img1 = np.zeros((width, height, 3))
    img2 = np.zeros((width, height, 3))

    for i in range(model.nfaces()):
        face = model.face(i)
        for j in range(3):
            v0 = model.vert(face[j])
            v1 = model.vert(face[(j + 1) % 3])
            x0 = int((v0[0] + 1) * width / 2) - 1
            y0 = height - int((v0[1] + 1) * height / 2) - 1
            x1 = int((v1[0] + 1) * width / 2) - 1
            y1 = height - int((v1[1] + 1) * height / 2) - 1
            cv2.line(img1, (x0, y0), (x1, y1), (255, 255, 255), 1)
            img2 = line(x0, x1, y0, y1, img2, [255, 255, 255])

    cv2.imshow("From .obj with MyLine", img2)
    cv2.imshow("From .obj default", img1)

    # show line methods on canva
    # imgLine1 = np.zeros((width, height, 3))
    # imgLine2 = np.zeros((width, height, 3))
    # cv2.line(imgLine1, (100,100), (800,800), (255, 255, 255), 1)
    # imgLine2 = line(100, 800, 100, 800, imgLine2, [255, 255, 255])
    # cv2.imshow("Default Line", imgLine1)
    # cv2.imshow("My Line", imgLine2)


def main():
    width = 800
    height = 800
    model = Model('D:\graphExample\iafrican_head.obj')
    showLines(width, height, model)
    showCircles(500, 500, 200, 200, 70, [255, 255, 255])
    cv2.waitKey(0)
    cv2.destroyAllWindows()


main()
