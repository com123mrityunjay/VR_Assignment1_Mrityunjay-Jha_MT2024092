**Report on Coin Counting Using Image Processing Techniques**

Introduction
------------

The objective of this project is to count the total number of coins in an image using OpenCV. The approach involves detecting edges, segmenting individual coins, and calculating the total count. The methodology includes grayscale conversion, Gaussian blurring, thresholding, and contour detection.

* * * * *

**Approach and Implementation**
-------------------------------

### **1\. Detecting All Coins in the Image**

To detect the coins in the image, the following steps were undertaken:

-   **Read and Preprocess the Image:** The image is read using OpenCV's `cv2.imread()` and resized to a fixed dimension.
-   **Blurring:** A Gaussian blur with a kernel size of (7,7) is applied to reduce noise and improve edge detection.
-   **Grayscale Conversion:** The image is converted to grayscale for easier processing.
-   **Thresholding:** Binary thresholding is applied to create a clear separation between the coins and the background.
-   **Contour Detection:** Using `cv2.findContours()`, the external boundaries of objects in the image are identified. The contours are drawn over the original image to visualize detected coins.

### **2\. Segmentation of Each Coin**

To segment individual coins, the following techniques were applied:

-   **Region-Based Segmentation:** Thresholding isolates the coins from the background by converting the image to binary.
-   **Contour Sorting:** The detected contours are sorted based on their area, filtering out small, irrelevant contours.
-   **Coin Extraction:** Individual coins are segmented based on the contours, and each segmented coin can be displayed separately.

### **3\. Counting the Total Number of Coins**

-   The total number of coins is determined by filtering out noise and small contours below a certain area threshold (500 pixels in this case).
-   Each valid contour is counted and displayed with its bounding area.
-   Finally, the number of detected coins is displayed on the screen.

* * * * *

**Results and Observations**
----------------------------

### **What Worked:**

-   The Gaussian blur effectively reduced noise and helped in achieving smoother edge detection.
-   Thresholding successfully separated the coins from the background, making contour detection more accurate.
-   Contour-based area filtering helped in eliminating small unwanted objects and noise from the image.
-   The `cv2.drawContours()` function effectively outlined the detected coins in the image.

### **What Did Not Work:**

-   Some overlapping or touching coins were detected as a single object.
-   The method struggled with coins that had similar intensity as the background.
-   Shadows and reflections in the image sometimes led to inaccurate detections.

* * * * *

**Final Approach and Future Improvements**
------------------------------------------

-   To improve detection, **adaptive thresholding** or **Canny edge detection** can be explored.
-   **Watershed segmentation** could be used to separate overlapping coins more effectively.
-   **Morphological operations** (e.g., erosion and dilation) can help in reducing noise and refining the segmentation.
-   Implementing **machine learning-based object detection models** like YOLO or Faster R-CNN could lead to more robust results.

* * * * *

**Conclusion**
--------------

The project successfully detects and counts coins in an image using OpenCV. Despite some challenges, the approach is effective for basic coin detection tasks. Further improvements can be made to handle overlapping coins and varying lighting conditions.

* * * * *


![alt text](https://github.com/com123mrityunjay/VR_Assignment1_Mrityunjay-Jha_MT2024092/blob/main/part_1/output.png)
