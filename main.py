from flask import Flask, request, jsonify
from flask_cors import CORS
import openai_connector
import json

app = Flask(__name__)
CORS(app, supports_credentials=True)


@app.route('/', methods=['POST'])
def main():
    post_data = request.get_data(as_text=True)
    post_params = json.loads(post_data)

    print(post_params)
    response = {'answer': openai_connector.knowledge_mode(post_params['messages'])}

    return jsonify(response)


if __name__ == '__main__':
    app.run(host='0.0.0.0', ssl_context=('cert.pem', 'key.pem'), threaded=True, port=8083, debug=True)
