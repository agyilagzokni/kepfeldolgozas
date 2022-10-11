import cv2
import numpy

def dilatacio(): #vastagit
    im = cv2.imread("morp_test.png", 0)
    kernel = numpy.ones((5, 5), dtype=numpy.uint8)

    dilated = cv2.dilate(im, kernel)
    cv2.imshow("dilated", dilated)

def erozio(): #vékonyít
    im = cv2.imread("morp_test.png", 0)
    kernel = numpy.ones((5, 5), dtype=numpy.uint8)
    eroded = cv2.erode(im, kernel)
    cv2.imshow("eroded", eroded)

def nyitas(): #kisebb képhibák eltávolítása dilatacioval és erozioval
    im = cv2.imread("morp_test_open.png", 0)
    kernel = numpy.ones((3,3), dtype=numpy.uint8)
    kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))

    eroded = cv2.erode(im, kernel)
    dilated = cv2.dilate(eroded, kernel)
    cv2.imshow("nyitas", dilated)

def zaras():
    im = cv2.imread("morp_test_closed.png", 0)
    kernel = numpy.ones((3,3), dtype=numpy.uint8)
    kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (7, 7))

    dilated = cv2.dilate(im, kernel)
    eroded = cv2.erode(dilated, kernel)
    cv2.imshow("zaras", eroded)

if __name__ == "__main__":
    cv2.imshow("eredeti", cv2.imread("morp_test_closed.png", 0))
    #dilatacio()
    #erozio()
    #nyitas()
    zaras()
    cv2.waitKey(0)