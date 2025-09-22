from flask import Flask, request
import pandas as pd
import os

app = Flask(__name__)
excel_path = 'user_data.xlsx'

# Initialize Excel if not exists
if not os.path.exists(excel_path):
    df = pd.DataFrame(columns=['Name', 'Age', 'Comments'])
    df.to_excel(excel_path, index=False)

@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    new_data = pd.DataFrame([{
        'Name': data.get('name'),
        'Age': data.get('age'),
        'Comments': data.get('comments')
    }])
    df = pd.read_excel(excel_path)
    df = pd.concat([df, new_data], ignore_index=True)
    df.to_excel(excel_path, index=False)
    return {'status': 'success'}, 200

if __name__ == '__main__':
    app.run(debug=True)
