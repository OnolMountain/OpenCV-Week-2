import cv2 as cv
import numpy as np

def main():
    # load image
    face = cv.imread("WIN_20230908_11_14_23_Pro.jpg")

    
    # set two points coordiante 
    point1 = (200, 300)
    point2 = (300, 200)
    

    x = np.array([x / 20 for x in range(0, 2000)])
    y = 600 - 50 * np.sin(x)
    x = 100 + x * 5
    x = [round(num) for num in x]
    y = [round(num) for num in y]
    coordinates = []
    for i in range(len(x)):
        coordinate = (x[i], y[i])
        coordinates.append(coordinate)
 

    centre = (400 , 400)
    radius = (50)
    colour_blue = (0, 0, 300)


    # draw the line in the image
    cv.line(face, point1, point2, colour_blue , thickness = 2)

    # draw the rectangle
    cv.rectangle(face, point1, point2, (0, 300, 0), thickness = 2)

    # draw the circle with blue line
    cv.circle(face, centre, radius, (300, 0, 0), thickness = 2)

    # draw the polyline
    cv.polylines(face, [np.array(coordinates)], isClosed = 0, color = (300, 300, 300), thickness = 1)

    # diaplay cv image
    cv.imshow("Face", face)

    # close the image when you press any key
    cv.waitKey(0)


if __name__ == "__main__":

    main()
    