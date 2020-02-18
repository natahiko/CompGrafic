import cv2
import numpy
def getYCbCr(img):
    R, G, B = img[:,:,0], img[:,:,1], img[:,:,2]

    Y = (0.299 * R) + (0.587 * G) + (0.114 * B)
    Cb = 256 - ((-0.169 * R) - (0.331 * G) + (0.499 * B)+128)
    Cr = (0.500 * R) - (0.418 * G) - (0.0812 * B)+128
    return Y,Cb, Cr
def vetroscope(img):
    Y,Cb, Cr = getYCbCr(img)
    #res = numpy.zeros((256,256,3), dtype=img.dtype)
    res = cv2.imread('D:\graphExample\outVetroscope.tif')
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            res[int(Cb[i,j]), int(Cr[i,j])] = numpy.array([0, int(Y[i,j]), 0])#Y[i,j]
    return res

def showNewPict(img):
    Y,Cb, Cr = getYCbCr(img)
    res2 = img.copy()
    res2[:, :, 0] = Y
    res2[:, :, 1] = Cb
    res2[:, :, 2] = Cr
    cv2.imshow("Result", res2)


def main():
    img = cv2.imread('D:\graphExample\imgRGB.jpg')
    cv2.imshow("Before", img)
    vetrsc= vetroscope(img)
    cv2.imshow("Vetroscope", vetrsc)
    showNewPict(img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

main()
