import cv2

class ShapeDetector:
	def __init__(self):
		pass

	def detect(self, c):
		
		# initialize the shape name and approximate contour
		shape = "unidentified"
		perimeter = cv2.arcLength(c, True)
		approx = cv2.approxPolyDP(c, 0.04 * perimeter, True)

		# given our approx contour, we can move on to performing shape detection
		# if the shape is a rectangle, it will have 3 vertices
		if len(approx) == 3:
			shape = "triangle"

		elif len(approx) == 4:
			# compute the bounding box of the contour and use the bounding box to compute the aspect ratio
			(x, y, w, h) = cv2.boundingRect(approx)
			ar = w / float(h)

			# a square will have an aspect ratio that is approximately equal to 1, otherwise, 
			# the shape is a rectangle
			shape = "square" if ar >= 0.95 and ar <= 1.05 else "rectangle"

		elif len(approx) == 5:
			shape = "pentagon"

		else:
			shape = "circle"

		# return the name of the shape
		return shape