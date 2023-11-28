from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

import openai_connector

app = Flask(__name__)
CORS(app, supports_credentials=True)


@app.route('/', methods=['POST'])
@cross_origin(supports_credentials=True)
def main():
    post_params = request.get_json()
    print(post_params)
    response = {'answer': openai_connector.knowledge_mode(post_params['messages'])}

    # Set Access-Control-Allow-Origin and other necessary headers
    resp = jsonify(response)

    # Add the following headers to allow cross-origin requests
    resp.headers.add('Access-Control-Allow-Origin', '*')
    resp.headers.add('Access-Control-Allow-Methods', 'POST')
    resp.headers.add('Access-Control-Allow-Headers', 'Content-Type')

    return resp


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8083, debug=True)
