from flask import jsonify
from flask import Flask
import os
# Flask app to identify whether the alarm has been triggered...
app = Flask(__name__)

@app.route('/')
def index():
    """API index route"""
    return jsonify({'status': 'ok'})


@app.route('/alarm/')
def alarm():
    return jsonify({'status': 'alarm activated'})


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=int(os.environ.get('PORT', '8000')))