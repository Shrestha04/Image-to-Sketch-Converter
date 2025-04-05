from flask import Flask, request, jsonify, send_file, render_template
from PIL import Image
import cv2
import numpy as np
import io

app = Flask(__name__)

def convert_to_sketch(image):
    image = np.array(image.convert('RGB'))  
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    inverted_image = 255 - gray_image
    blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)
    inverted_blurred = 255 - blurred
    pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0)
    return pencil_sketch

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    try:
        if 'image' not in request.files:
            return jsonify({'error': 'No image part'}), 400
        file = request.files['image']
        if file.filename == '':
            return jsonify({'error': 'No selected file'}), 400
        image = Image.open(file.stream)
        sketch = convert_to_sketch(image)

        sketch_image = Image.fromarray(sketch)

        img_io = io.BytesIO()
        sketch_image.save(img_io, 'PNG')
        img_io.seek(0)

        return send_file(img_io, mimetype='image/png')
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
