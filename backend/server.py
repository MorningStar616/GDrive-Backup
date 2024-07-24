import os
from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['ALLOWED_EXTENSIONS'] = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

# Define the scopes for accessing Google Drive
SCOPES = ['https://www.googleapis.com/auth/drive.file']

# Define the path to the credentials JSON file downloaded from Google Developers Console
CREDENTIALS_FILE = r"C:\Users\HP\Desktop\Projects\credentials.json"

# Define the destination folder in Google Drive
DESTINATION_FOLDER_ID = '1OjYB51eyhxDkhDLXHJEx-auP16whcNlO'

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def authenticate():
    flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES)
    credentials = flow.run_local_server(port=0)
    return credentials

def upload_file(service, file_path, folder_id):
    try:
        if not os.path.exists(file_path):
            print(f"File does not exist: {file_path}")
            return None, "File does not exist."

        print(f"Uploading file: {file_path}")
        file_metadata = {
            'name': os.path.basename(file_path),
            'parents': [folder_id]
        }
        media = MediaFileUpload(file_path)
        file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
        print(f"File uploaded successfully to Google Drive with ID: {file.get('id')}")
        return file.get('id'), None
    except HttpError as error:
        print(f"An error occurred: {error}")
        if error.resp.status == 404:
            return None, "The specified folder ID was not found. Please check the folder ID."
        else:
            return None, f"HTTP error occurred: {error.resp.status}"

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        
        credentials = authenticate()
        service = build('drive', 'v3', credentials=credentials)
        file_id, error = upload_file(service, file_path, DESTINATION_FOLDER_ID)
        
        if error:
            return jsonify({'error': error}), 500

        return jsonify({'message': 'File uploaded and backed up successfully', 'file_id': file_id}), 200
    else:
        return jsonify({'error': 'File type not allowed'}), 400

if __name__ == '__main__':
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    app.run(debug=True)
