import cv2
import numpy as np

def stitch_images(img1, img2):
    # Convert images to grayscale for feature detection
    gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    # Initialize SIFT detector (if SIFT is unavailable, consider using ORB)
    sift = cv2.SIFT_create()
    kp1, des1 = sift.detectAndCompute(gray1, None)
    kp2, des2 = sift.detectAndCompute(gray2, None)

    # Match descriptors using FLANN based matcher
    FLANN_INDEX_KDTREE = 1
    index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
    search_params = dict(checks=50)
    flann = cv2.FlannBasedMatcher(index_params, search_params)
    
    # k=2 to apply Lowe's ratio test
    matches = flann.knnMatch(des1, des2, k=2)
    good_matches = []
    for m, n in matches:
        if m.distance < 0.7 * n.distance:
            good_matches.append(m)

    # Proceed if enough good matches are found
    if len(good_matches) > 10:
        # Extract locations of good matches
        src_pts = np.float32([kp1[m.queryIdx].pt for m in good_matches]).reshape(-1, 1, 2)
        dst_pts = np.float32([kp2[m.trainIdx].pt for m in good_matches]).reshape(-1, 1, 2)
        
        # Compute homography matrix using RANSAC
        H, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
        
        # Get dimensions of the images
        h1, w1 = img1.shape[:2]
        h2, w2 = img2.shape[:2]
        
        # Get the canvas dimensions by transforming the corners of img1
        pts_img1 = np.float32([[0,0], [0, h1], [w1, h1], [w1, 0]]).reshape(-1,1,2)
        pts_img1_trans = cv2.perspectiveTransform(pts_img1, H)
        
        # Combine the transformed corners with the corners of img2
        pts = np.concatenate((pts_img1_trans, np.float32([[0,0], [0, h2], [w2, h2], [w2, 0]]).reshape(-1,1,2)), axis=0)
        [xmin, ymin] = np.int32(pts.min(axis=0).ravel() - 0.5)
        [xmax, ymax] = np.int32(pts.max(axis=0).ravel() + 0.5)
        
        # Compute translation homography to shift the panorama
        translation_dist = [-xmin, -ymin]
        H_translation = np.array([[1, 0, translation_dist[0]],
                                  [0, 1, translation_dist[1]],
                                  [0, 0, 1]])
        
        # Warp img1 and blend with img2 on the canvas
        result = cv2.warpPerspective(img1, H_translation.dot(H), (xmax-xmin, ymax-ymin))
        result[translation_dist[1]:h2+translation_dist[1], translation_dist[0]:w2+translation_dist[0]] = img2
        
        return result
    else:
        raise Exception("Not enough matches found to stitch images.")

# Example usage:
if __name__ == '__main__':
    # Load your overlapping images
    img1 = cv2.imread('DSC_0171.jpg')
    img2 = cv2.imread('DSC_0172.jpg')

    if img1 is None or img2 is None:
        raise Exception("One or both images could not be loaded. Check the file paths.")

    try:
        panorama = stitch_images(img1, img2)
        # Save the final panorama
        cv2.imwrite('panorama.jpg', panorama)
        # Display the result (optional)
        cv2.imshow('Panorama', panorama)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    except Exception as e:
        print("Error during stitching:", e)

