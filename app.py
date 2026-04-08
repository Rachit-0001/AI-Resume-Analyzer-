from flask import Flask, render_template, request
from utils.parser import extract_text
from utils.analyzer import analyze_resume
import os


    
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    
    if request.method == 'POST':
        file = request.files['resume']
        role = request.form.get('role')

        resume_text = extract_text(file)
        result = analyze_resume(resume_text, role)

    return render_template('index.html', result=result)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
