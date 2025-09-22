# User Input Form Flask Application

## Overview
This is a Flask web application that allows users to submit personal information (name, age, comments) through a web form. The data is stored in an Excel file (`user_data.xlsx`) for persistence.

## Project Structure
- `app.py` - Main Flask application with API endpoints
- `index.html` - Frontend form interface
- `requirements.txt` - Python dependencies
- `user_data.xlsx` - Data storage file (auto-generated)

## Features
- Web form for data collection (name, age, comments)
- RESTful API endpoint for data submission
- Excel file storage for data persistence
- CORS enabled for cross-origin requests
- Bootstrap-free responsive design

## Technical Stack
- Backend: Flask (Python)
- Frontend: HTML/JavaScript
- Data Storage: Excel files via pandas
- Dependencies: flask, pandas, openpyxl, flask-cors

## Setup and Configuration
- Configured for Replit environment
- Runs on host 0.0.0.0:5000
- CORS enabled for frontend/backend integration
- Deployment configured for autoscale

## Recent Changes (2025-09-22)
- Imported from GitHub and configured for Replit
- Added CORS support and proper host configuration
- Set up Flask server workflow on port 5000
- Configured deployment settings for production
- Updated frontend to use relative API URLs

## User Preferences
- Default deployment: autoscale (stateless web app)
- Data persistence: Excel files
- Development mode enabled with debug=True