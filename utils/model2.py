import cv2


class Model():
    def __init__(self, filename):
        file = open(filename, "r")
        lines = file.readlines()
        self.__vector = []
        self.__faces = []
        for line in lines:
            if line[:2] == 'v ':
                vals = line.split(" ")
                self.__vector.append([float(vals[1]), float(vals[2]), float(vals[3])])
            elif line[:2] == 'f ':
                vals = line.split(" ")
                val1 = vals[1].split('/')
                val2 = vals[2].split('/')
                val3 = vals[3].split('/')
                self.__faces.append([int(val1[0])-1, int(val2[0])-1, int(val3[0])-1])

    def nverts(self):
        return len(self.__vector)

    def nfaces(self):
        return len(self.__faces)

    def face(self, idx):
        return self.__faces[idx]

    def vert(self, id):
        return self.__vector[id]
