import numpy
import cv2

def convertRBGtoGray():
    im = cv2.imread("hellenergy.jpg")
    print(im.shape[:2])
    i = numpy.ndarray(im.shape[:2], numpy.uint8)
    i[:, :] = im[:, :, 0] * 0.07 + im[:, :, 1] * 0.72 + im[:, :, 2] * 0.21
    cv2.imshow("convertRBGtoGray", i)
    cv2.waitKey(0)

def convertColorSpaces():
    im = cv2.imread("hellenergy.jpg")
    i = cv2.cvtColor(im, cv2.COLOR_RGB2GRAY)
    cv2.imshow("convertColorSpaces", i)
    cv2.waitKey(0)

def copyColorChannels():
    pass

def modifyGrayValue(value):
    im = cv2.imread("hellenergy.jpg")
    i = cv2.cvtColor(im, cv2.COLOR_RGB2HSV)
    i[:, :, 2] = i[:, :, 2] / value
    irgb = cv2.cvtColor(i, cv2.COLOR_HSV2RGB)
    cv2.imshow("modifyGrayValue", irgb)
    cv2.waitKey(0)

if __name__ == "__main__":
    #convertColorSpaces()
    #convertRBGtoGray()
    modifyGrayValue(2)