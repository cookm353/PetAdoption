from unittest import TestCase

from app import app
from models import db, Pet

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pets_test'
app.config['SQLALCHEMY_ECHO'] = False
app.config['TESTING'] = True
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']

db.drop_all()
db.create_all()

class Test_Pet(TestCase):
    def setUp(self):
        Pet.query.delete()
        lucy = Pet(name='Lucy', species='Cat', age=2, available=False,
                   notes='Very vocal and affectionate')
        
        db.session.add(lucy)
        db.session.commit()
        
        self.lucy = lucy
        
    def tearDown(self):
        db.session.rollback()