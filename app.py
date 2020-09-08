from flask import Flask
import yaml
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

yml = yaml.load(open("db.yaml"))
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:pass@localhost:1995/sridb'
db = SQLAlchemy(app)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
