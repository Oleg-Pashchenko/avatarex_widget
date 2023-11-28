from flask import Flask, request, jsonify
from flask_cors import CORS

import openai_connector

app = Flask(__name__)
CORS(app, supports_credentials=True)

@app.route('/', methods=['POST'])
def main():
    post_params = request.get_json()
    print(post_params)
    response = {'answer': openai_connector.knowledge_mode(post_params['messages'])}

    # Flask-CORS will handle CORS headers, so you don't need to add them manually

    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8083, debug=True)
