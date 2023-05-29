from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Web App with Python Flask and Docker!'

app.run(host='0.0.0.0', port=8000)
