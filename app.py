from flask import Flask, request, json
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)

@app.route('/')
def home_page():
    return 'working'

swagger_uri = '/swagger'
api_uri = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    swagger_uri,
    api_uri,
    config={
        'app_name': "Srinivas-flask-api"
    }
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=swagger_uri)



if __name__ == '__main__':
    app.run()
