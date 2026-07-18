# Face Detection Using OpenCV

A beginner-friendly, modular Computer Vision application that detects human faces in static images. It leverages the power of OpenCV's Haar Cascade Classifier to identify facial features and provides a visual output with bounding boxes around the detected faces.

## 🚀 Features
- **Efficient Detection:** Uses pre-trained Haar Cascades to detect frontal faces with high accuracy in images.

- **Visual Feedback:** Automatically draws green rectangular bounding boxes around all identified faces.

- **Face Count:** Provides a summary of the number of faces detected in the console.

- **Modular Architecture:** The project is broken down into specific modules for loading, detecting, and visualizing, making the code highly maintainable.

- **Built-in Resource Management:** Uses OpenCV’s native haarcascades path to avoid manual file management.
```text
Face_Detection_Using_OpenCV/
│
├── main.py              # Main execution loop
├── detector.py          # Haar Cascade logic for face identification
├── image_loader.py      # Utility for loading images
├── visualization.py     # Image processing for drawing rectangles
├── sample.jpg           # Image file for testing
├── requirements.txt     # Project dependencies
└── README.md            # Documentation