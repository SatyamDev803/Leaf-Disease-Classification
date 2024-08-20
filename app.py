from flask import Flask, render_template, request, redirect
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
import numpy as np
import os
from PIL import Image

app = Flask(__name__)

MODEL_PATH = "models/2.keras" 
try:
    model = load_model(MODEL_PATH)
    print("Model loaded successfully.")
except Exception as e:
    print(f"Error loading model: {e}")

model = load_model(MODEL_PATH)

class_names = ['Early Blight', 'Late Blight', 'Healthy']

def predict(image_path):
    try:
        # Load and preprocess the image
        img = Image.open(image_path)
        img = img.resize((256, 256))  # Resize to match model input size
        img = img_to_array(img)
        img = np.expand_dims(img, axis=0)  # Add batch dimension

        # Predict the class
        predictions = model.predict(img)
        print(f"Predictions: {predictions}")  # print predictions
        predicted_class = class_names[np.argmax(predictions[0])]
        confidence = round(100 * (np.max(predictions[0])), 2)
        return predicted_class, confidence
    except Exception as e:
        print(f"Error in prediction: {e}")
        return "Error", 0

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Check if an image was uploaded
        if 'file' not in request.files:
            return redirect(request.url)
        
        file = request.files['file']
        
        if file.filename == '':
            return redirect(request.url)
        
        if file:
            # Save the file to the static location
            file_path = os.path.join('static', file.filename)
            file.save(file_path)
            
            # Make prediction
            predicted_class, confidence = predict(file_path)
            
            # Return the result
            return render_template('index.html', prediction=predicted_class, confidence=confidence, img_path=file_path)
    
    return render_template('index.html', prediction=None, confidence=None)

from flask_caching import Cache
cache = Cache(app, config={'CACHE_TYPE': 'simple'})

@app.route('/clear_cache')
def clear_cache():
    cache.clear()
    return 'Cache cleared!'

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
    
