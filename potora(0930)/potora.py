import cv2
import numpy

imgName = "kep.jfif"

def runFilters():
    img = cv2.imread(imgName, 0)
    value = 3
    medianValue = 5
    filtered_box = cv2.boxFilter(img, -1, (value, value)) #összefüggő zajok eltávolitasa
    filtered_gauss = cv2.GaussianBlur(img, (value, value), 3) #összefüggő zajok eltávolitasa
    filtered_median = cv2.medianBlur(img, medianValue) #nagyon kiugro (vagy random) értékek javitására hasznos
    #mindharom zaj eltávolítására hasznos
    cv2.imshow("box", filtered_box)
    cv2.imshow("gauss", filtered_gauss)
    cv2.imshow("median", filtered_median)
    cv2.imshow("eredeti", img)
    cv2.waitKey()

if __name__ == "__main__":
    runFilters()