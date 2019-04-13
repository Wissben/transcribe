import os
import pprint
import random

from flask import render_template
from flask_socketio import emit

from app import app, db
from app import socketio
from app.config import APP_STATIC
from app.models import Transcription,Transcription_saved

AUTHORIZED_EXTENSIONS = ['wav', 'mp3']
app.config['UPLOAD_FOLDER'] = os.path.join(APP_STATIC)
PROBAS = []
DATA = []


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@socketio.on('trans')
def handle_message(json):
    pprint.pprint(json['bytes'])
    byte_array = b''.join(json['bytes'])

    transc = Transcription_saved(audio_path=app.config['SAVING_PATH'], transcription=str(json['utterance']))
    db.session.add(transc)
    db.session.commit()
    id = transc.id
    transc.audio_path = transc.transcription + '_' + str(id)
    with open(app.config['SAVING_PATH'] + transc.audio_path + '.wav', mode='bw') as fd:
        fd.write(byte_array)


@socketio.on('connect')
def init():
    all = Transcription.query.all()
    random_index = random.randrange(0, len(all))
    emit('recieve', {'utterance': str(all[random_index].transcription),
                     'id': str(all[random_index].id)}
         )
