from flask import Blueprint, jsonify, request
from app.phishing_url.prediction_model import classify_url  # Adjusted import path
from app.phishing_url.URL_extractor import extract_features  # Adjusted import path

phishing_detector = Blueprint("url_checker", __name__)

@phishing_detector.post("/predict")
def detect_phishing():  # Renamed function to avoid conflict
    try:
        # Validate input
        data = request.get_json()
        if not data or 'url' not in data:
            return jsonify({
                'error': 'URL is required',
                'status': 400
            }), 400

        url = data['url'].strip()
        if not url:
            return jsonify({
                'error': 'URL cannot be empty',
                'status': 400
            }), 400

        # Process URL and get prediction
        features = extract_features(url)
        result = classify_url(features)

        return jsonify({
            'url': url,
            'prediction': result['status'],
            'confidence': result['confidence'],
            'detected_features': result['active_features'],
            'status': 200
        })

    except Exception as e:
        return jsonify({
            'error': str(e),
            'status': 500
        }), 500

