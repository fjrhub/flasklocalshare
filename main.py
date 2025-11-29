from flask import Flask, request, render_template, send_from_directory, redirect, url_for
import os

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/")
def home():
    files = os.listdir(UPLOAD_FOLDER)
    return render_template("index.html", files=files)

@app.route("/upload/", methods=["POST"])
def upload_file():
    if 'file' not in request.files:
        return redirect(url_for("home"))

    file = request.files['file']

    if file.filename == '':
        return redirect(url_for("home"))

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    # Langsung redirect ke halaman download
    return redirect(url_for("download_file", filename=file.filename))


@app.route("/download/<filename>")
def download_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename, as_attachment=True)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
