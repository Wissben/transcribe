from app.models import Transcription
from app import db
import re
from app import app
from random import randrange

Transcription.query.delete()

def load_from_file(path_to_file):
    with open(path_to_file,'r') as fd:
        return [re.sub('[^a-zA-Z\?\!, ]','',line) for line in fd.readlines()]

lines = load_from_file('transc_01.trs')
for item,value  in enumerate(lines):
    to_add = Transcription(transcription=value)
    db.session.add(to_add)
    print('[INFO] : ', to_add)

db.session.commit()

