import cv2 as cv
import numpy as np

x0, y0 = None, None # The initial coordinates of the moues event
drawing = False

def draw_line(event, x, y, flags,*params) -> None:

  """
  Mouse event handling function.
  Draws a rectangle on mouse event.
  """

  global x0, y0, drawing

  image, = params # Unpack params tuple
  colour = [0,0,255] # Green

  # Start drawing rectangle on down click

  if event == cv.EVENT_LBUTTONDOWN:
    drawing =True
    x0, y0 = x, y

  pt1, pt2 = (x0, y0), (x, y)

  # Expand rectangle size if mouse is moved while downclicked

  if event == cv.EVENT_MOUSEMOVE and drawing:
    cv.line(image, pt1, pt2, colour, 1)

  # End drawing when downclick released
  elif event == cv.EVENT_LBUTTONUP and drawing:
    drawing = False
    cv.line(image, pt1, pt2, colour, 1)

  return None


def draw_rectangle(event, x, y, flags,*params) -> None:

  """
  Mouse event handling function.
  Draws a rectangle on mouse event.
  """

  global x0, y0, drawing

  image, = params # Unpack params tuple
  colour = [0,0,255] # Green

  # Start drawing rectangle on down click

  if event == cv.EVENT_LBUTTONDOWN:
    drawing =True
    x0, y0 = x, y

  pt1, pt2 = (x0, y0), (x, y)

  # Expand rectangle size if mouse is moved while downclicked

  if event == cv.EVENT_MOUSEMOVE and drawing:
    cv.rectangle(image, pt1, pt2, colour, -1)

  # End drawing when downclick released
  elif event == cv.EVENT_LBUTTONUP and drawing:
    drawing = False
    cv.rectangle(image, pt1, pt2, colour, -1)

  return None


def main() -> None:

  blank = np.zeros((720, 720, 3), dtype=np.uint8) # Create 720x720 blank image with 3 colour channels

  cv.namedWindow("Image") # Name current window "Image"
  cv.setMouseCallback("Image", draw_line, param=(blank))

  while True:
    cv.imshow("Image", blank)
    key = cv.waitKey(1)

    if key == ord('l'): # press l to toggle line mode
      cv.setMouseCallback("Image", draw_line, param=(blank))
    elif key == ord('r'): # press r to toggle rectangle mode
      cv.setMouseCallback("Image", draw_rectangle, param=(blank))
    if key ==ord('d'): # press d to turn off window
      break

  cv.destroyAllWindows()

if __name__=="__main__":
    main()
    