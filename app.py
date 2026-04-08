from flask import Flask, render_template, request
from utils.parser import extract_text
from utils.analyzer import analyze_resume
import os

app = Flask(__name__)


UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    
    if request.method == 'POST':
        file = request.files['resume']
        role = request.form.get('role')

        if file:
            file_path = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(file_path)

            resume_text = extract_text(file_path)   
            result = analyze_resume(resume_text, role)

    return render_template('index.html', result=result)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  
    app.run(host="0.0.0.0", port=port)
