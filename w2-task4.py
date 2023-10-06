import cv2 as cv
import numpy as np

def main():
    # load image
    face = cv.imread("park.png")
    p = cv.imread("WIN_20230908_11_14_23_Pro.jpg")
    # kernel truple
    ksize = (5,5)
 
    # diaplay cv image
    cv.imshow("Original", face)

    # apply the blurring effect
    blur_face = cv.blur(face, ksize)
    # diaplay cv image
    cv.imshow("Blur", blur_face)

    gauss_face = cv.GaussianBlur(face, ksize, sigmaX = 0, sigmaY = 0)
    # diaplay cv image
    cv.imshow("Average", gauss_face)

    median_face = cv.medianBlur(face, 5)
    # diaplay cv image
    cv.imshow("MedianBlur", median_face)

    biliteral_face = cv.bilateralFilter(face, 10, 100, 100)
    # diaplay cv image
    cv.imshow("Biliteral", biliteral_face)

    filter_face = cv.filter2D(p, 10, face) # by using the value of p to convolve with the face
    # diaplay cv image
    cv.imshow("Filter2D", filter_face)

    

    # close the image when you press any key
    cv.waitKey(0)


if __name__ == "__main__":

    main()
    