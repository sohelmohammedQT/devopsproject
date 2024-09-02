from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:mysecretpassword@localhost:5432/postgres'
db = SQLAlchemy(app)

@app.route('/api/status', methods=['GET'])
def status():
    return {"status": "API is running!"}, 200

if __name__ == '__main__':
    app.run(debug=True)

