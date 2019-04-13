import logging
import os
from logging.handlers import SMTPHandler, RotatingFileHandler

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_migrate import Migrate
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy

from app.config import Config

def setup_file_logging():
    if not os.path.exists('logs'):
        os.mkdir('logs')
    fh = RotatingFileHandler('logs/main_app.log', maxBytes=1024 * 20, backupCount=15)
    fh.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
    ))
    app.logger.addHandler(fh)
    app.logger.setLevel(logging.INFO)
    app.logger.info('The application started')


app = Flask(__name__)
app.config.from_object(Config)

# Post-app-creating initilization
socketio = SocketIO(app)
Bootstrap(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

if not app.debug:
    setup_file_logging()

if __name__ == '__main__':
    socketio.run(app)

from app import routes, models, errors
