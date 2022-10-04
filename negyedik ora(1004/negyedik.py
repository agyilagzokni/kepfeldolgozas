import cv2
import numpy


def performManualThresh(thresh : int):
    img = cv2.imread("hellenergy.jpg", 0)
    thresh_value = int(thresh)
    mask = cv2.threshold(img, thresh_value, 255, cv2.THRESH_BINARY_INV) #csak 0 és 1 értékek, az adott küszöbszámtól függően

    cv2.imshow("mask", mask[1])

    masked_img = numpy.bitwise_and(img, mask[1]) #csak azon pixelek megjelenítése, amelyek a maskban 1 értéket vesznek fel
    cv2.imshow("masked", masked_img)
    cv2.waitKey(0)

def performAlgorithmicThresh():
    img = cv2.imread("rose.jpg", 0)
    mask = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    masked_img = numpy.bitwise_and(img, mask[1])
    cv2.imshow("mask", mask[1])
    cv2.imshow("masked", masked_img)
    cv2.waitKey(0)

#A manuális es az adaptív egyetlen threshold értékkel dolgozik, míg az adaptív minden régióra egy új küszöbértéket számol ki,
#ezért különböző fényviszonyok közt is jól működik
def performAdaptiveThresh(blocksize : int):
    img = cv2.imread("text.png", 0)
    masked = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, blocksize, 2)
    cv2.imshow("masked", masked)
    cv2.waitKey(0)

if __name__ == "__main__":
    #performManualThresh(200)
    #performAlgorithmicThresh()
    performAdaptiveThresh(5)