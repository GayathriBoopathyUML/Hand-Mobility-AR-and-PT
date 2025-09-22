from flask import Flask, request, send_from_directory
from flask_cors import CORS
import pandas as pd
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
excel_path = 'user_data.xlsx'

# Initialize Excel if not exists
if not os.path.exists(excel_path):
    df = pd.DataFrame(columns=['Name', 'Age', 'Comments'])
    df.to_excel(excel_path, index=False, engine='openpyxl')

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    new_data = pd.DataFrame([{
        'Name': data.get('name'),
        'Age': data.get('age'),
        'Comments': data.get('comments')
    }])
    
    # Check if Excel file exists, if not create new DataFrame
    if os.path.exists(excel_path):
        df = pd.read_excel(excel_path, engine='openpyxl')
        df = pd.concat([df, new_data], ignore_index=True)
    else:
        df = new_data
    
    df.to_excel(excel_path, index=False, engine='openpyxl')
    return {'status': 'success'}, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
