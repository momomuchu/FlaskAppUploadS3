from flask import Flask, render_template, request
from uploader import upload_file

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        bucket = request.form['bucket']
        key = request.form['key']

        if file and bucket and key:
            file_path = file.filename
            file.save(file_path)

            if upload_file(file_path, bucket, key):
                return "File uploaded successfully!"
            else:
                return "File upload failed."

    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)
