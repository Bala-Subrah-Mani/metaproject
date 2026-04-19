from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "MetaSense AI - Research Methodology Evaluator"

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    if file:
        filepath = os.path.join('uploads', file.filename)
        os.makedirs('uploads', exist_ok=True)
        file.save(filepath)
        return jsonify({"message": "File uploaded successfully", "filename": file.filename})
    return jsonify({"error": "No file uploaded"}), 400

@app.route('/analyze', methods=['POST'])
def analyze():
    # Dummy NLP logic (placeholder)
    return jsonify({
        "methodology_score": 75,
        "missing_sections": ["Dataset Description", "Threats to Validity"],
        "suggestions": ["Add dataset details", "Include validity discussion"]
    })

if __name__ == '__main__':
    app.run(debug=True)
