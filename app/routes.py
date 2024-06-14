from flask import render_template, request, jsonify
from app import app
import pickle
import os

# Load the trained model
model_path = os.path.join(os.path.dirname(__file__), '..', 'spam_classifier.pkl')
if os.path.exists(model_path) and os.path.getsize(model_path) > 0:
    with open(model_path, 'rb') as f:
        clf = pickle.load(f)
else:
    raise FileNotFoundError("The model file is missing or empty.")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    message = data['message']
    prediction = clf.predict([message])
    result = 'spam' if prediction[0] == 1 else 'ham'
    return jsonify({'prediction': result})
