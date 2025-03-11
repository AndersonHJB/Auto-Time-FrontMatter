from flask import Flask, jsonify, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/time', methods=['GET'])
def get_time():
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    data = {
        "time": current_time,
        "author": "AI悦创",
        "site": "bornforthis.cn"
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
