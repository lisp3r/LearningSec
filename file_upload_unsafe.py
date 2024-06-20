import os
from flask import Flask, flash, request, redirect, url_for, send_file, abort

UPLOAD_FOLDER = 'uploads'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/uploads')
def download_file():
    filename = request.args.get('file', '')
    path_to_file = os.path.join(app.config["UPLOAD_FOLDER"], filename) #/
    if os.path.isfile(path_to_file):
        return send_file(path_to_file)
    else:
        abort(404, 'Requested File Not Found')


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))  # uploads/pic.png
        return redirect(url_for('download_file', name=file.filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''


app.run()