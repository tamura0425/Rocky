from flask import Flask
from flask import request, make_response, jsonify
from flask_cors import CORS
from utils import wakati
from flask import Flask, render_template


app = Flask(__name__, static_folder='../frontend/dist/static', template_folder='../frontend/dist')

@app.route('/',defaults={'path':''})
@app.route('/<path:path>')
def index(path):
    return render_template('index.html')















if __name__ == "__main__":
    app.debug = True
#    app.run(host='127.0.0.1', port=5000)
