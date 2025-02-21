import cv2
import numpy as np
import concurrent.futures
import time

# Function to rotate an image and store rotated templates
def rotate_image(image, angle):
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
    return cv2.warpAffine(image, matrix, (w, h))

# Function to process an angle in parallel
def process_angle(angle):
    rotated_template = rotated_templates[angle]

    if rotated_template.shape[0] <= roi.shape[0] and rotated_template.shape[1] <= roi.shape[1]:
        result = cv2.matchTemplate(roi, rotated_template, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, max_loc = cv2.minMaxLoc(result)
        return angle, max_val, max_loc, rotated_template.shape
    return None

# Load images
image = cv2.imread("image.jpg", 0)
template = cv2.imread("template.jpg", 0)

# ✅ Step 1: Select ROI Interactively
image_color = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)  # Convert to color for display
roi_box = cv2.selectROI("Select ROI", image_color, fromCenter=False, showCrosshair=True)
cv2.destroyAllWindows()  # Close the ROI selection window

# Extract ROI coordinates
x, y, w, h = roi_box
roi = image[y:y+h, x:x+w]

# ✅ Step 2: Resize images for faster processing
scale_percent = 35  # Adjust for speed-accuracy balance
roi = cv2.resize(roi, (roi.shape[1] * scale_percent // 100, roi.shape[0] * scale_percent // 100))
template = cv2.resize(template, (template.shape[1] * scale_percent // 100, template.shape[0] * scale_percent // 100))

# ✅ Step 3: Precompute Rotated Templates
angles = range(0, 360, 10)  # Rotating in 10-degree steps
rotated_templates = {angle: rotate_image(template, angle) for angle in angles}

# ✅ Step 4: Multi-threading for Faster Execution
best_angle, best_val, best_match, best_size = 0, -1, None, (0, 0)

start_time = time.time()  # Start Timer

with concurrent.futures.ThreadPoolExecutor() as executor:
    results = executor.map(process_angle, angles)

# Find the best match
for res in results:
    if res and res[1] > best_val:
        best_angle, best_val, best_match, best_size = res

end_time = time.time()  # End Timer
print(f"Best match at angle: {best_angle}, confidence: {best_val}")
print(f"Total Execution Time: {end_time - start_time:.3f} sec")

# ✅ Draw ROI for visualization
cv2.rectangle(image_color, (x, y), (x + w, y + h), (255, 0, 0), 2)  # Blue box for ROI

# ✅ Draw rectangle on best match (Inside ROI)
if best_match:
    top_left = (x + best_match[0], y + best_match[1])  # Adjust match to full image
    h, w = best_size
    bottom_right = (top_left[0] + w, top_left[1] + h)

    cv2.rectangle(image_color, top_left, bottom_right, (0, 255, 0), 2)  # Green rectangle on match

# ✅ Show the result
cv2.imshow("Detected Template with ROI", image_color)
cv2.waitKey(0)
cv2.destroyAllWindows()
