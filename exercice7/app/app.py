from flask import Flask
import os
import socket

app = Flask(__name__)

@app.route('/')
def home():
    return f"Hello from Flask! Hostname: {socket.gethostname()}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.getenv("APP_PORT", 10011)))