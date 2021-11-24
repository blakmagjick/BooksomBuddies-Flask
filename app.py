from flask import Flask, jsonify

import models

from dotenv import load_dotenv 
load_dotenv()

DEBUG=True
PORT=8000 

app = Flask(__name__) 

@app.route('/')
def test():
    return 'Server connected'

if __name__ == '__main__':
    app.run(debug=DEBUG, port=PORT)
