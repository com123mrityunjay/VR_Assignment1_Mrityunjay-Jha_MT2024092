**Report on Image Stitching for Panorama Creation**
===================================================

**1\. Introduction**
--------------------

The objective of this project was to create a seamless panorama by stitching multiple overlapping images using computer vision techniques. The process involved detecting key points, matching features, computing transformations, and blending images. This report summarizes what was attempted, what worked, what didn't, and the final approach taken.

**2\. What Was Tried**
----------------------

-   **Feature Detection:** Used **SIFT** to extract key points from overlapping images.
-   **Feature Matching:** Applied **FLANN-based matcher** with **Lowe's ratio test** to filter matches.
-   **Homography Calculation:** Used **RANSAC** to compute a transformation matrix.
-   **Image Warping & Blending:** Warped one image onto the other's coordinate frame and blended the images.

**3\. What Worked**
-------------------

-   **SIFT + FLANN** provided robust feature matching even with varying lighting and perspectives.
-   **RANSAC-based homography** effectively aligned the images by removing outliers.
-   **Image warping with translation adjustment** helped merge images on a larger canvas.

**4\. What Didn't Work**
------------------------

-   **Insufficient feature matches** caused failures in homography estimation for some images.
-   **Visible seams and exposure differences** made some transitions noticeable.
-   **Scaling to multiple images** required iterative stitching and careful blending.

**5\. Final Approach**
----------------------

1.  **SIFT for key point detection** due to its accuracy and robustness.
2.  **FLANN-based feature matching** with Lowe's ratio test for reliable correspondences.
3.  **Homography estimation using RANSAC** to align images correctly.
4.  **Image warping with translation adjustment** to ensure proper alignment.
5.  **Blending techniques (feathering/multi-band blending)** to minimize visible seams.

**6\. Conclusion**
------------------

The final approach successfully stitched overlapping images into a panorama. Future improvements could include **better blending techniques** and **global optimization for multiple images** to enhance accuracy and seamlessness.
