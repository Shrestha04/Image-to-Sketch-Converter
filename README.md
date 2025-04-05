# Python-Project
# 🖼️ Image to Sketch Converter 🎨

This is a simple and creative web application that converts uploaded images into pencil sketches using Python, Flask, OpenCV, and a touch of frontend magic ✨.

## 🚀 Features

- Upload any image file (JPEG, PNG, etc.)
- Get a beautiful pencil sketch version instantly
- Download the sketch to your device
- Stylish and responsive frontend


## 🛠️ Technologies Used

- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Python Flask
- **Image Processing:** OpenCV
- **Design:** Google Fonts, Modern UI styling

## 📸 Preview

![Preview](mainpageimage.png)
![Preview](originalimage.png)
![Preview]("resultimage.png")


## 🧠 How it Works

1. User uploads an image through the web UI.
2. The image is sent to a Flask backend.
3. OpenCV processes the image:
   - Converts to grayscale
   - Inverts the image
   - Applies Gaussian blur
   - Combines with original grayscale to create a pencil sketch
4. The sketch is returned to the frontend for viewing and download.



