import os
import subprocess
from flask import Flask, render_template, flash, request, redirect, url_for
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'cc'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

app = Flask (__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submission", methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            output = "Incorrect Input.  Must be walk.css"
            return render_template("submission.html", output=output)
        file = request.files['file']
        if file.filename == '':
            output = "Incorrect Input.  Must be walk.css"
            return render_template("submission.html", output=output)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            testInfo = subprocess.run("./comp_exec.py", shell = True, stdout = subprocess.PIPE, universal_newlines = True)
            output = testInfo.stdout
            return render_template("submission.html", output=output)
        return "File not found"

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
