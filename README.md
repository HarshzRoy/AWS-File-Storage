# AWS S3 File Storage Web App

A modern, user-friendly web application for uploading, downloading, and managing files in your AWS S3 bucket—without needing to use the AWS Console directly.

## Features
- Beautiful, modern UI for file upload, download, and deletion
- Secure login with your own S3 credentials (never exposed to other users)
- Step-by-step setup instructions for S3 CORS and IAM permissions
- Drag-and-drop file upload
- No AWS Console or CLI knowledge required
- Easily extensible for more features and branding

## Why Use This App Instead of Direct AWS S3 Access?

**1. User-Friendly Interface**
- No AWS Console complexity—just a simple, clean web interface
- Drag-and-drop uploads, easy downloads, and file management

**2. Credential Protection & Security**
- Users never see or handle AWS credentials directly
- Session-based authentication and easy logout

**3. Custom Features & Branding**
- Add your own logo, colors, and help content
- Integrate with other tools or automate workflows

**4. Simplified Permissions**
- No need to manage AWS IAM for every user—set up once and go

**5. Centralized Support & Help**
- Built-in setup instructions and help links
- Add your own support or FAQ content

**6. Extensible**
- Add support for other storage backends (Google Cloud, Azure, local, etc.)
- Expose your own API for other apps

## Setup

1. **Clone the repository:**
   ```sh
   git clone https://github.com/HarshzRoy/AWS-File-Storage.git
   cd AWS-File-Storage
   ```
2. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
3. **Run the app:**
   ```sh
   python app.py
   ```
4. **Open your browser:**
   Go to [http://localhost:5000/](http://localhost:5000/)

5. **First time setup?**
   - Click "Need help? Setup instructions" on the login page for step-by-step S3 configuration (CORS, IAM permissions, etc.)

## S3 Setup Requirements
- CORS policy (see Setup Instructions page)
- IAM permissions: `s3:GetObject`, `s3:PutObject`, `s3:ListBucket`, `s3:DeleteObject`

## License
MIT 