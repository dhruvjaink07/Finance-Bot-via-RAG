import joblib
import os
# from URL_extractor import extract_features
def classify_url(features):

    try:
        # Load model
        model_path = os.path.join(os.path.dirname(__file__), 'phishing_model.joblib')
        model = joblib.load(model_path)
        
        # Make prediction
        prediction = model.predict(features)[0]
        confidence = model.predict_proba(features)[0][1] * 100
        
        # Get active features
        active_features = {
            feature: value for feature, value 
            in features.iloc[0].items() if value > 0
        }
        
        return {
            'status': 'PHISHING' if prediction else 'LEGITIMATE',
            'confidence': f"{confidence:.1f}%",
            'active_features': active_features
        }
        
    except Exception as e:
        raise Exception(f"Prediction error: {str(e)}")
    
# print(classify_url(extract_features("https://www.canva.com/design/DAFl7ChBdDM/r4eSUvu_ANmkqukuwM7_6Q/view?utm_content=DAFl7ChBdDM&utm_campaign=designshare&utm_medium=link&utm_source=viewer")))  # Example usage