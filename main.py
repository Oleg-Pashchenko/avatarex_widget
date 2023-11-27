from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

import openai_connector

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/', methods=['GET', 'POST'])
@cross_origin()
def main():
    post_params = request.get_json()
    print(post_params)
    response = {'answer': openai_connector.knowledge_mode(post_params['messages'])}
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8083, debug=True)
