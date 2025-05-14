from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    db_password = open('/run/secrets/db_password').read().strip()
    api_key = open('/run/secrets/api_key').read().strip()
    return f"Hello, Flask is running! DB Password: {db_password}, API Key: {api_key}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)