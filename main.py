from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def main():
    post_params = request.form.to_dict()
    return {'answer': str(post_params)}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
