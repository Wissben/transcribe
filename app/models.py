from app import db


class Transcription(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    transcription = db.Column(db.String(length=500))
    def __repr__(self):
        return '<{} : {}>'.format(self.id,self.transcription)


class Transcription_saved(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    audio_path = db.Column(db.String(length=120))
    transcription = db.Column(db.String(length=500))

    def __repr__(self):
        return '<{} : {} :{}>'.format(self.id, self.audio_path, self.transcription)
