from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/', methods=['GET', 'POST'])
@cross_origin()
def main():
    post_params = request.get_json()
    print(post_params)
    return {'answer': str(post_params)}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
