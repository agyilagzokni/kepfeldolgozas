import numpy
import cv2

def demoImageIO():
    im = cv2.imread("hellenergy.jpg", 0)
    im2 = cv2.imread("hellenergy.jpg", 1)

    formatParameters_png = []
    formatParameters_png.append(cv2.IMWRITE_PNG_COMPRESSION)
    formatParameters_png.append(5)

    formatParameters_jpg = []
    formatParameters_jpg.append(cv2.IMWRITE_JPEG_QUALITY)
    formatParameters_jpg.append(90)

    cv2.imwrite("out.png", im, formatParameters_png)
    cv2.imwrite("out.jpg", im2, formatParameters_jpg)

def extractChannels():
    img = cv2.imread("kep.jpg")
    img_red = img[:, :, 2]
    img_green = img[:, :, 1]
    img_blue = img[:, :, 0]
    cv2.imshow("red", img_red)
    cv2.imshow("green", img_green)
    cv2.imshow("blue", img_blue)
    
    cv2.waitKey()

#M = numpy.full((480, 640), 100, numpy.uint8)
#cv2.imshow("M", M)
#cv2.waitKey()

extractChannels()