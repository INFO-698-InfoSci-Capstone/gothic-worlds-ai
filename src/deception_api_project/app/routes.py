from flask import Blueprint, request, jsonify, current_app
from app.model.loader import predict_deception_score_from_model  # Make sure this function is exposed in your loader.py

import logging

logger = logging.getLogger(__name__)

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return jsonify({'message': 'Deception Score API is running'})

@main.route('/predict', methods=['POST'])
def predict_deception_score():
    data = request.get_json()
    logger.info(f"Received request: {data.get('text')}")
    if not data or 'text' not in data:
        return jsonify({'error': 'Invalid input. No text provided'}), 400

    text = data['text']
    try:
        vectorized = current_app.vectorizer.transform([text])
        prediction = current_app.model.predict(vectorized)[0]
        return jsonify({'deception_score': round(prediction, 2)})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@main.route("/predict_with_cnn", methods=["POST"])
def predict_with_cnn():
    data = request.get_json()
    logger.info(f"Received request: {data.get('text')}")
    if not data or "text" not in data:
        return jsonify({"error": "Missing 'text' field in JSON"}), 400

    text = data["text"]
    score = predict_deception_score_from_model(text)
    return jsonify({
        "input": text,
        "deception_score": round(score, 2)
    })