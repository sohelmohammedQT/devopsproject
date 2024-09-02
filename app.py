from flask import Flask

app = Flask(__name__)

@app.route('/api/status', methods=['GET'])
def status():
    return {"status": "API is running!"}, 200

if __name__ == '__main__':
    app.run(debug=True)

