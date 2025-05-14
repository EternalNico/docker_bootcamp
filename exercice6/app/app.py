import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    environment = os.getenv("APP_ENV", "development")
    return f"Hello from Flask in {environment} environment!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.getenv("APP_PORT", 10008)))