from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

import openai_connector

app = Flask(__name__)
CORS(app, supports_credentials=True)


@app.route('/', methods=['POST'])
@cross_origin()
def main():
    post_params = request.get_json()
    print(post_params)
    response = {'answer': openai_connector.knowledge_mode(post_params['messages'])}

    # Set Access-Control-Allow-Headers in the response headers

    resp = jsonify(response)
    resp.headers.add('Access-Control-Allow-Origin', '*')
    return resp



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8083, debug=True)
