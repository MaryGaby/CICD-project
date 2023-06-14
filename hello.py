# hello.py
import os
from flask import Flask

app = Flask(__name__)
env_config = os.getenv("PROD_APP_SETTINGS", "config.DevelopmentConfig")
app.config.from_object(env_config)

@app.route('/')
def hello():
    return 'Hello, Worldd!'

if __name__ == '__main__':
    app.run()