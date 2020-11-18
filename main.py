from flask import Flask


application = Flask(__name__)


@application.route('/')
def home_page():
    return 'working'

if __name__ == '__main__':
    application.run()
