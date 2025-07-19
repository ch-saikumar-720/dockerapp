from flask import Flask, jsonify

app = Flask(__name__)  # Corrected: Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to Flask inside Docker!"})  # Fixed typo in message

if __name__ == '__main__':  # Corrected: proper if-statement and __name__ variable
    app.run(host='0.0.0.0', port=5000)  # Corrected: changed `port-5000` to `port=5000`

