from flask import Flask, request, json

app = Flask(__name__)

@app.route('/')
def home_page():
    return 'working'

if __name__ == '__main__':
    app.run()
