from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/users")
def root():
    return jsonify({'userId': 42}), 200


@app.route("/health")
def health():
    return jsonify({"status": "up"}), 200


if __name__ == "__main__":
    app.run(host='0.0.0.0')
