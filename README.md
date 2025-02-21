# 🎯 Template Matching with Rotation using OpenCV and Multi-threading

This project demonstrates template matching with rotation using OpenCV. 🖼️ It utilizes multi-threading to accelerate the search for the best-matching angle of the template inside a selected region of interest (ROI) in an image. ⚡

## 🚀 Features

- **🎯 Interactive ROI Selection**: Users can select a region of interest (ROI) in the image.
- **🔄 Template Rotation**: The template is rotated in 10-degree steps (customizable) to find the best match.
- **⚡ Multi-threading for Speed Optimization**: Uses Python's `concurrent.futures.ThreadPoolExecutor` for parallel processing.
- **🎯 Efficient Matching**: Finds the best-matching angle quickly for precise template detection.
- **🖼️ Visualization**: Draws the ROI and best match location on the image for easy interpretation.

## 📥 Installation

Ensure you have Python installed along with the required dependencies:

```sh
pip install opencv-python numpy
```

## 🛠️ Usage

1. Clone this repository:
   ```sh
   git clone <repo_url>
   cd <repo_name>
   ```
2. Place your `image.jpg` and `template.jpg` files in the project directory.
3. Run the script:
   ```sh
   python template_matching.py
   ```
4. Select the ROI interactively when prompted.
5. View the detected template location in the output window.

## 🔍 Code Workflow

- **🖼️ Step 1**: Load images and allow the user to select an ROI interactively.
- **⚡ Step 2**: Resize images to improve processing speed.
- **🔄 Step 3**: Precompute rotated templates for efficient searching.
- **🤖 Step 4**: Use multi-threading to find the best match efficiently.
- **✅ Step 5**: Draw the results and display the final detection visually.

## 📊 Example Output

- The script will display the original image with:
  - **🟦 A blue rectangle** marking the selected ROI.
  - **🟩 A green rectangle** highlighting the best-matching template location.
- The terminal will output:
  ```
  Best match at angle: XX, confidence: X.XX
  Total Execution Time: X.XXX sec
  ```

## ⚙️ Customization

- Adjust the rotation step size by modifying `angles = range(0, 360, 10)`.
- Change `scale_percent = 35` to adjust the image scaling factor.
- Experiment with different OpenCV template matching methods, such as `cv2.TM_CCOEFF_NORMED`.

## 📜 License

This project is licensed under the MIT License.

## 🤝 Contributions

Contributions, pull requests, and suggestions are welcome! 🚀

## 👨‍💻 Author

[Your Name]

