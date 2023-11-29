from flask import Flask, request, jsonify
import openai_connector

app = Flask(__name__)


@app.route('/widget-api', methods=['POST'])
def main():
    print('yes')
    post_params = request.json
    print(post_params)
    response = {'answer': openai_connector.knowledge_mode(post_params['messages'])}
    return jsonify(response)


if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True, port=8083, debug=True)
