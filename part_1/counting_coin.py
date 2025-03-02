import numpy as np
import cv2

# Read the image from the specified file path
img = cv2.imread("one.jpg")

# Resize the image to a fixed dimension (width: 640, height: 800) for consistency
img = cv2.resize(img, (640, 800))

# Create a copy of the original image for later use (to draw contours without altering the original)
image_copy = img.copy()

# Apply Gaussian blur to the image to reduce noise and smooth out details.
# The kernel size is (7, 7) and the standard deviation in the X direction is 3.
img = cv2.GaussianBlur(img, (7, 7), 3)

# Convert the blurred image to grayscale; this simplifies further processing like thresholding.
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply binary thresholding to the grayscale image.
# Pixels with intensity above 170 are set to 255 (white) and those below are set to 0 (black).
ret, thresh = cv2.threshold(gray, 170, 255, cv2.THRESH_BINARY)

# Find contours in the thresholded image.
# RETR_TREE retrieves all of the contours and reconstructs a full hierarchy of nested contours.
# CHAIN_APPROX_NONE stores all the points of the contours.
contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

# Create a dictionary to store contour areas with their corresponding index
area = {}
for i in range(len(contours)):
    cnt = contours[i]
    ar = cv2.contourArea(cnt)  # Compute the area of the contour
    area[i] = ar  # Map contour index to its area

# Sort the contours by area in descending order (largest area first)
# Each element in 'srt' is a tuple (index, area)
srt = sorted(area.items(), key=lambda x: x[1], reverse=True)

# Convert the sorted list of tuples to a NumPy array of type int
results = np.array(srt).astype("int")

# Count the number of contours (potential coins) with an area greater than 500 pixels.
# np.argwhere returns indices where the condition is True.
num = np.argwhere(results[:, 1] > 500).shape[0]

# Loop over the detected contours (starting from index 1 to ignore the largest contour,
# which is often the boundary of the image or a large non-coin area)
for i in range(1, num):
    # Draw the contour on the image copy.
    # The contour color is set to green (0, 255, 0) and thickness to 3.
    image_copy = cv2.drawContours(image_copy, contours, results[i, 0], (0, 255, 0), 3)

# Print the number of coins detected.
# Subtract 1 because the largest contour (index 0) is not considered a coin.
print("Number of coins is ", num - 1)

# Display the final image with detected contours
cv2.imshow("final", image_copy)

# Wait indefinitely until a key is pressed
cv2.waitKey(0)

# Close all OpenCV windows
cv2.destroyAllWindows()

