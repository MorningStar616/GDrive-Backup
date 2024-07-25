# GDrive-Backup

## Description

GDrive-Backup is a web application that allows users to upload files from their local machine to a Google Drive folder. This application is built using Flask for the backend and React for the frontend. The backend handles file uploads and Google Drive API integration, while the frontend provides an intuitive interface for file selection and upload.

## Features

- Secure file upload to a designated Google Drive folder.
- Real-time feedback on the upload status.
- Responsive design for a seamless user experience on different devices.

## Prerequisites

- Python 3.x
- Node.js and npm
- Google Cloud Project with OAuth 2.0 credentials

## Setup

### Backend

1. Clone the repository:

   ```sh
   git clone https://github.com/YourUsername/GDrive-Backup.git
   cd GDrive-Backup/backend
   
2. Create a virtual environment and install dependencies:

   '''sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    pip install -r requirements.txt

3. Create a .env file in the backend directory and add your Google OAuth credentials:

   '''makefile
   GOOGLE_CLIENT_ID=your-client-id
   GOOGLE_CLIENT_SECRET=your-client-secret

4. Run the Flask application:

   '''sh
   flask run

###Frontend

1. Navigate to the frontend directory:

   '''sh
   cd ../frontend

2. Install dependencies:

   '''sh
    npm install

3. Start the React application:

   '''sh
   npm run dev

##Usage
  - Open your web browser and go to http://localhost:3000.
  - Click on the upload box to select a file or drag and drop a file into the box.
  - Click the "Upload" button to upload the file to Google Drive.
  - Check the response message for the upload status.

##Contributing
  - Fork the repository.
  - Create a new branch (git checkout -b feature/your-feature).
  - Commit your changes (git commit -m 'Add some feature').
  - Push to the branch (git push origin feature/your-feature).
  -Open a pull request.



