from flask import Flask, request, send_from_directory

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to the CTF challenge!"

@app.route('/file/<path:filename>', methods=['GET'])
def serve_file(filename):
    return send_from_directory('restricted', filename)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
