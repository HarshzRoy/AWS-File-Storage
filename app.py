from flask import Flask, request, send_from_directory, render_template, jsonify, redirect, url_for, session
import os
import boto3
from botocore.exceptions import ClientError

app = Flask(__name__)
# Change this to a secure random value
app.secret_key = 'replace_with_a_long_random_secret_key'

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# --- Login page ---


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        access_key = request.form['access_key']
        secret_key = request.form['secret_key']
        region = request.form['region']
        bucket = request.form['bucket']
        # Try to connect to S3
        try:
            s3 = boto3.client(
                's3',
                aws_access_key_id=access_key,
                aws_secret_access_key=secret_key,
                region_name=region
            )
            # Try to list the bucket to verify credentials
            s3.head_bucket(Bucket=bucket)
            session['s3'] = {
                'access_key': access_key,
                'secret_key': secret_key,
                'region': region,
                'bucket': bucket
            }
            return redirect(url_for('index'))
        except ClientError as e:
            return render_template('login.html', error='Could not connect to S3: ' + str(e))
    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('s3', None)
    return redirect(url_for('login'))

# --- Require login decorator ---


def require_login(f):
    from functools import wraps

    @wraps(f)
    def decorated(*args, **kwargs):
        if 's3' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated


@app.route('/')
@require_login
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
@require_login
def upload_file():
    if 'file' not in request.files:
        return jsonify({'success': False, 'error': 'No file part'})
    file = request.files['file']
    if file.filename == '':
        return jsonify({'success': False, 'error': 'No selected file'})
    filename = file.filename
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return jsonify({'success': True})


@app.route('/files', methods=['GET'])
@require_login
def list_files():
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    return jsonify({'files': files})


@app.route('/download/<filename>', methods=['GET'])
@require_login
def download_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)


@app.route('/delete/<filename>', methods=['POST'])
@require_login
def delete_file(filename):
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    if os.path.exists(file_path):
        os.remove(file_path)
        return jsonify({'success': True})
    else:
        return jsonify({'success': False, 'error': 'File not found'}), 404


@app.route('/setup')
def setup():
    return render_template('setup.html')


if __name__ == '__main__':
    app.run(debug=True, port=5001)
