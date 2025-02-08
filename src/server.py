# server.py

import os
from flask import Flask, request, jsonify
from flask_cors import CORS  # Enable CORS to handle cross-origin requests
from werkzeug.utils import secure_filename
import main  # Import main.py which contains process_resume()

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Configure the folder to store uploaded resumes.
UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Define allowed file extensions.
ALLOWED_EXTENSIONS = {'pdf', 'doc', 'docx'}

def allowed_file(filename):
    """Check if file extension is allowed"""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload_resume', methods=['POST'])
def upload_resume():
    """Handle resume upload and processing"""
    print("Received a request to /upload_resume")

    if 'file' not in request.files:
        print("Error: No file part in request")
        return jsonify({"error": "No file part in the request"}), 400

    file = request.files['file']
    if file.filename == '':
        print("Error: No file selected")
        return jsonify({"error": "No file selected"}), 400

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        print(f"File saved at: {filepath}")
        
        # Process the resume using process_resume() from main.py.
        result = main.process_resume(filepath)
        
        print("Processing complete, sending response:", result)

        return jsonify({"message": "File uploaded and processed", "result": result}), 200
    else:
        print("Error: File type not allowed")
        return jsonify({"error": "File type not allowed"}), 400

if __name__ == '__main__':
    app.run(debug=True, port=5000)
