from os import getenv

from flask import Flask
from flask_redis import FlaskRedis

from api.api_handler import api_blueprint


app = Flask(__name__)
app.config['REDIS_URL'] = 'redis://:{}@redis:{}/{}'.format(
    getenv('REDIS_PASSWORD'), getenv('REDIS_PORT'), getenv('REDIS_DATABASES')
)
redis_client = FlaskRedis(app)

app.register_blueprint(api_blueprint(redis_client), url_prefix='/api/v1')
