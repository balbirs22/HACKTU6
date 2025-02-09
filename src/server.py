import os
import subprocess
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from werkzeug.utils import secure_filename
import main  # Contains process_resume()

app = Flask(__name__, static_folder="../TestRoad")  # Serve static files from TestRoad/
CORS(app)

# Configure the folder for uploaded resumes.
UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'uploads')
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

ALLOWED_EXTENSIONS = {'pdf', 'doc', 'docx'}

def allowed_file(filename):
    """Check if file extension is allowed."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Serve static files (CSS, JS, Images) correctly
@app.route("/static/<path:filename>")
def static_files(filename):
    return send_from_directory(app.static_folder, filename)

@app.route("/")
def index():
    return send_from_directory(app.static_folder, "index.html")

@app.route("/resume-checker")
def resume_checker():
    return send_from_directory(app.static_folder, "resume-checker.html")

@app.route("/upload_resume", methods=["POST"])
def upload_resume():
    print("Received a request to /upload_resume")
    
    if "file" not in request.files:
        print("Error: No file part in request")
        return jsonify({"error": "No file part in the request"}), 400
    
    file = request.files["file"]
    if file.filename == "":
        print("Error: No file selected")
        return jsonify({"error": "No file selected"}), 400
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        file.save(filepath)
        
        print(f"✅ File saved at: {filepath}")
        
        # Process the Resume
        result = main.process_resume(filepath)
        
        print("✅ Processing complete, sending response:", result)

        # Run sendMail.py in the background
        subprocess.Popen(["python", "src/sendMail.py"])

        return jsonify(result), 200
    else:
        print("Error: File type not allowed")
        return jsonify({"error": "File type not allowed"}), 400

if __name__ == "__main__":
    app.run(debug=True, port=5000)
