from app import db

class ProjectRegistrationModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64))
    Supervisor1Name = db.Column(db.String(64))

    def __repr__(self):
        return '<ProjectRegistrationModel {}>'.format(self.username) 
